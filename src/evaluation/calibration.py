"""Calibration helpers for rule-baseline variant and threshold comparisons."""

from __future__ import annotations

import copy
import csv
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

from src.baselines.risk_scoring import load_rule_config
from src.baselines.rule_based import predict_batch
from src.baselines.types import RuleConfig
from src.evaluation.error_analysis import error_analysis
from src.evaluation.metrics import binary_metrics, preferred_gold_label
from src.evaluation.triage_metrics import preferred_gold_risk, triage_metrics


def load_calibration_profiles(path: str | Path) -> dict[str, dict[str, Any]]:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    profiles = data.get("profiles", {})
    if not isinstance(profiles, dict):
        raise ValueError(f"{path} must contain a profiles mapping")
    return profiles


def load_profile_config(base_config_path: str | Path, profile: dict[str, Any]) -> RuleConfig:
    base_data = yaml.safe_load(Path(base_config_path).read_text(encoding="utf-8"))
    if not isinstance(base_data, dict):
        raise ValueError(f"{base_config_path} must contain a YAML mapping")
    merged = deep_merge(base_data, profile.get("overrides", {}))
    return _config_from_mapping(merged)


def run_calibration_matrix(
    records: list[dict[str, Any]],
    base_config_path: str | Path,
    profiles: dict[str, dict[str, Any]],
    variants: list[str],
) -> dict[str, dict[str, list[dict[str, Any]]]]:
    matrix: dict[str, dict[str, list[dict[str, Any]]]] = {}
    for profile_name, profile in profiles.items():
        config = load_profile_config(base_config_path, profile)
        matrix[profile_name] = {}
        for variant in variants:
            matrix[profile_name][variant] = predict_batch(records, config=config, variant=variant)
    return matrix


def summarize_matrix(
    records: list[dict[str, Any]],
    matrix: dict[str, dict[str, list[dict[str, Any]]]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for profile_name, variants in matrix.items():
        for variant, predictions in variants.items():
            binary = binary_metrics(records, predictions)
            triage = triage_metrics(records, predictions)
            risk_counts = Counter(str(prediction["risk_level_pred"]) for prediction in predictions)
            rows.append(
                {
                    "profile": profile_name,
                    "variant": variant,
                    "items": len(predictions),
                    "binary_metric_items": binary["binary_metric_items"],
                    "precision": binary["precision"],
                    "recall": binary["recall"],
                    "f1": binary["f1"],
                    "false_positive": binary["false_positive"],
                    "false_negative": binary["false_negative"],
                    "triage_exact_agreement": triage["exact_agreement"],
                    "high_predictions": risk_counts.get("high", 0),
                    "medium_predictions": risk_counts.get("medium", 0),
                    "low_predictions": risk_counts.get("low", 0),
                    "skipped_label_counts": binary["skipped_label_counts"],
                }
            )
    return rows


def changed_decisions(
    matrix: dict[str, dict[str, list[dict[str, Any]]]],
    reference_profile: str = "baseline",
    reference_variant: str = "text_only",
) -> list[dict[str, Any]]:
    reference_predictions = matrix.get(reference_profile, {}).get(reference_variant, [])
    reference_by_id = {prediction["item_id"]: prediction for prediction in reference_predictions}
    changes: list[dict[str, Any]] = []

    for profile_name, variants in matrix.items():
        for variant, predictions in variants.items():
            if profile_name == reference_profile and variant == reference_variant:
                continue
            for prediction in predictions:
                ref = reference_by_id.get(prediction["item_id"])
                if not ref:
                    continue
                if prediction["risk_level_pred"] == ref["risk_level_pred"]:
                    continue
                changes.append(
                    {
                        "item_id": prediction["item_id"],
                        "reference_profile": reference_profile,
                        "reference_variant": reference_variant,
                        "reference_risk": ref["risk_level_pred"],
                        "profile": profile_name,
                        "variant": variant,
                        "risk": prediction["risk_level_pred"],
                        "total_score": prediction["total_score"],
                        "reason_codes": prediction["reason_codes"],
                    }
                )
    return changes


def export_reviewer_worksheet(
    path: str | Path,
    records: list[dict[str, Any]],
    predictions: list[dict[str, Any]],
) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "item_id",
        "gold_label",
        "gold_risk_level",
        "pred_binary",
        "pred_risk_level",
        "total_score",
        "subtype_hint",
        "reason_codes",
        "explanations",
        "top_matched_signals",
        "review_priority",
        "reviewer_final_label",
        "reviewer_final_risk",
        "reviewer_notes",
    ]
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for record, prediction in zip(records, predictions, strict=False):
            writer.writerow(_worksheet_row(record, prediction))


def render_calibration_report(
    *,
    input_path: str,
    base_config_path: str,
    profile_path: str,
    summary_rows: list[dict[str, Any]],
    changes: list[dict[str, Any]],
    baseline_all_errors: dict[str, Any],
    worksheet_path: str,
) -> list[str]:
    lines = [
        "# Rule Baseline Calibration Report",
        "",
        f"- Input: `{input_path}`",
        f"- Base config: `{base_config_path}`",
        f"- Calibration profiles: `{profile_path}`",
        f"- Reviewer worksheet: `{worksheet_path}`",
        "",
        "## Metric Matrix",
        "",
        "| Profile | Variant | Binary items | Precision | Recall | F1 | FP | FN | Triage agreement | High | Medium | Low |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summary_rows:
        lines.append(
            "| {profile} | {variant} | {binary_metric_items} | {precision:.3f} | {recall:.3f} | {f1:.3f} | {false_positive} | {false_negative} | {triage_exact_agreement:.3f} | {high_predictions} | {medium_predictions} | {low_predictions} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Changed Decisions",
            "",
            f"- Changed risk decisions versus baseline/text_only: {len(changes)}",
        ]
    )
    for change in changes[:30]:
        lines.append(
            "- {item_id}: {reference_risk} -> {risk} via `{profile}/{variant}`".format(**change)
        )
    if len(changes) > 30:
        lines.append(f"- ... {len(changes) - 30} more")

    lines.extend(
        [
            "",
            "## Baseline All-Signal Error Counts",
            "",
            f"- False positives: {baseline_all_errors['false_positive_count']}",
            f"- False negatives: {baseline_all_errors['false_negative_count']}",
            f"- Medium-risk ambiguity items: {baseline_all_errors['medium_risk_ambiguity_count']}",
            "",
            "## Interpretation Rules",
            "",
            "- Treat synthetic results as tooling checks, not performance evidence.",
            "- Review false positives before loosening thresholds.",
            "- Prefer threshold/config edits over Python edits after real pilot data arrives.",
            "- Keep link-only and urgency-only items out of high risk unless stronger evidence converges.",
        ]
    )
    return lines


def deep_merge(base: dict[str, Any], overrides: dict[str, Any]) -> dict[str, Any]:
    merged = copy.deepcopy(base)
    for key, value in (overrides or {}).items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = copy.deepcopy(value)
    return merged


def _config_from_mapping(data: dict[str, Any]) -> RuleConfig:
    scoring = data.get("scoring", {})
    return RuleConfig(
        signal_weights={str(key): float(value) for key, value in data.get("signal_weights", {}).items()},
        thresholds=dict(scoring.get("thresholds", {})),
        combination_bonuses=list(scoring.get("combination_bonuses", [])),
        subtype_mappings=list(scoring.get("subtype_mappings", [])),
        reason_code_order=list(data.get("reason_code_order", [])),
        max_signal_instances_per_code=int(scoring.get("max_signal_instances_per_code", 2)),
    )


def _worksheet_row(record: dict[str, Any], prediction: dict[str, Any]) -> dict[str, Any]:
    top = _unique_top_signals(prediction.get("matched_signals", []), limit=5)
    return {
        "item_id": str(record.get("item_id") or prediction.get("item_id") or ""),
        "gold_label": preferred_gold_label(record),
        "gold_risk_level": preferred_gold_risk(record),
        "pred_binary": prediction.get("binary_pred", ""),
        "pred_risk_level": prediction.get("risk_level_pred", ""),
        "total_score": prediction.get("total_score", ""),
        "subtype_hint": prediction.get("subtype_hint") or "",
        "reason_codes": "|".join(prediction.get("reason_codes", [])),
        "explanations": " ".join(prediction.get("explanations", [])),
        "top_matched_signals": "|".join(
            f"{signal.get('signal_code')}:{signal.get('source_field')}" for signal in top
        ),
        "review_priority": _review_priority(record, prediction),
        "reviewer_final_label": "",
        "reviewer_final_risk": "",
        "reviewer_notes": "",
    }


def _review_priority(record: dict[str, Any], prediction: dict[str, Any]) -> str:
    gold = preferred_gold_label(record)
    risk = prediction.get("risk_level_pred")
    if gold == "non_scam" and prediction.get("binary_pred") == "scam_like":
        return "false_positive_review"
    if gold == "scam" and prediction.get("binary_pred") != "scam_like":
        return "false_negative_review"
    if gold in {"uncertain", "insufficient_evidence"}:
        return "ambiguity_review"
    if risk == "high":
        return "high_risk_reason_check"
    if risk == "medium":
        return "medium_risk_threshold_check"
    return "spot_check"


def _unique_top_signals(signals: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    seen: set[tuple[str, str]] = set()
    unique: list[dict[str, Any]] = []
    for signal in signals:
        key = (str(signal.get("signal_code")), str(signal.get("source_field")))
        if key in seen:
            continue
        seen.add(key)
        unique.append(signal)
        if len(unique) >= limit:
            break
    return unique
