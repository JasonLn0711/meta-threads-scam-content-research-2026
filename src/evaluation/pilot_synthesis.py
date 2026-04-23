"""Aggregate-only pilot result synthesis helpers."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

from src.evaluation.metrics import preferred_gold_label
from src.evaluation.triage_metrics import preferred_gold_risk


DECISION_OPTIONS = {
    "expand_to_100_200",
    "revise_guideline_first",
    "revise_schema_first",
    "narrow_sources",
    "pause",
    "synthetic_dry_run_no_expansion_decision",
}


def synthesize_pilot(
    records: list[dict[str, Any]],
    *,
    calibration_run_dir: str | Path | None = None,
    governance_rating: str = "unknown",
    privacy_rating: str = "unknown",
    reviewer_burden_rating: str = "unknown",
) -> dict[str, Any]:
    dataset = dataset_summary(records)
    calibration = load_calibration_artifacts(calibration_run_dir) if calibration_run_dir else {}
    warnings = warning_flags(dataset, calibration)
    decision = recommend_decision(
        dataset,
        calibration,
        warnings,
        governance_rating=governance_rating,
        privacy_rating=privacy_rating,
        reviewer_burden_rating=reviewer_burden_rating,
    )
    return {
        "dataset": dataset,
        "calibration": calibration,
        "warnings": warnings,
        "decision": decision,
        "ratings": {
            "governance": governance_rating,
            "privacy_redaction": privacy_rating,
            "reviewer_burden": reviewer_burden_rating,
        },
    }


def dataset_summary(records: list[dict[str, Any]]) -> dict[str, Any]:
    total = len(records)
    label_counts = Counter(preferred_gold_label(record) or "<blank>" for record in records)
    risk_counts = Counter(preferred_gold_risk(record) or "<blank>" for record in records)
    source_counts = Counter(str(record.get("source_type") or "<blank>") for record in records)
    auth_counts = Counter(str(record.get("authorization_status") or "<blank>") for record in records)
    evidence_counts = Counter(str(record.get("evidence_sufficiency") or "<blank>") for record in records)
    confidence_counts = Counter(str(record.get("annotation_confidence") or "<blank>") for record in records)
    content_counts = Counter(content_shape(record) for record in records)

    return {
        "total_items": total,
        "label_counts": dict(sorted(label_counts.items())),
        "label_rates": _rates(label_counts, total),
        "risk_counts": dict(sorted(risk_counts.items())),
        "source_type_counts": dict(sorted(source_counts.items())),
        "authorization_status_counts": dict(sorted(auth_counts.items())),
        "evidence_sufficiency_counts": dict(sorted(evidence_counts.items())),
        "annotation_confidence_counts": dict(sorted(confidence_counts.items())),
        "content_shape_counts": dict(sorted(content_counts.items())),
        "all_synthetic": all(str(record.get("authorization_status")) == "synthetic_only" for record in records),
        "review_status_counts": dict(
            sorted(Counter(str(record.get("review_status") or "<blank>") for record in records).items())
        ),
    }


def load_calibration_artifacts(run_dir: str | Path) -> dict[str, Any]:
    path = Path(run_dir)
    artifacts: dict[str, Any] = {"run_dir": str(path)}
    for name in (
        "calibration_summary.json",
        "changed_decisions.json",
        "baseline_all_error_analysis.json",
    ):
        artifact_path = path / name
        if artifact_path.exists():
            artifacts[name.removesuffix(".json")] = json.loads(artifact_path.read_text(encoding="utf-8"))
    return artifacts


def warning_flags(dataset: dict[str, Any], calibration: dict[str, Any]) -> list[dict[str, str]]:
    warnings: list[dict[str, str]] = []
    total = max(int(dataset.get("total_items", 0)), 1)
    label_counts = dataset.get("label_counts", {})
    uncertain_rate = label_counts.get("uncertain", 0) / total
    insufficient_rate = label_counts.get("insufficient_evidence", 0) / total

    if dataset.get("all_synthetic"):
        warnings.append(
            {
                "code": "synthetic_only",
                "severity": "info",
                "message": "Dataset is synthetic-only; do not make pilot expansion claims.",
            }
        )
    if uncertain_rate > 0.30:
        warnings.append(
            {
                "code": "high_uncertain_rate",
                "severity": "yellow",
                "message": f"`uncertain` rate is {uncertain_rate:.1%}, above the 30% warning threshold.",
            }
        )
    if insufficient_rate > 0.20:
        warnings.append(
            {
                "code": "high_insufficient_evidence_rate",
                "severity": "yellow",
                "message": f"`insufficient_evidence` rate is {insufficient_rate:.1%}, above the 20% warning threshold.",
            }
        )

    errors = calibration.get("baseline_all_error_analysis", {})
    if errors.get("false_positive_count", 0):
        warnings.append(
            {
                "code": "baseline_false_positives",
                "severity": "yellow",
                "message": f"Baseline all-signal false positives: {errors['false_positive_count']}.",
            }
        )
    if errors.get("false_negative_count", 0):
        warnings.append(
            {
                "code": "baseline_false_negatives",
                "severity": "yellow",
                "message": f"Baseline all-signal false negatives: {errors['false_negative_count']}.",
            }
        )
    return warnings


def recommend_decision(
    dataset: dict[str, Any],
    calibration: dict[str, Any],
    warnings: list[dict[str, str]],
    *,
    governance_rating: str,
    privacy_rating: str,
    reviewer_burden_rating: str,
) -> dict[str, str]:
    if dataset.get("all_synthetic"):
        return {
            "recommendation": "synthetic_dry_run_no_expansion_decision",
            "rationale": "This run used synthetic-only data, so it can validate tooling but cannot support a real pilot expansion decision.",
        }
    if governance_rating == "red" or privacy_rating == "red":
        return {
            "recommendation": "pause",
            "rationale": "Governance or privacy/redaction was rated red; expansion is blocked.",
        }
    codes = {warning["code"] for warning in warnings}
    if "high_insufficient_evidence_rate" in codes:
        return {
            "recommendation": "revise_schema_first",
            "rationale": "Too many items lack sufficient evidence; collection fields or evidence requirements need revision before expansion.",
        }
    if "high_uncertain_rate" in codes:
        return {
            "recommendation": "revise_guideline_first",
            "rationale": "Too many items are uncertain; annotation boundaries should be revised before expansion.",
        }
    if "baseline_false_positives" in codes:
        return {
            "recommendation": "revise_guideline_first",
            "rationale": "Baseline false positives need error review before threshold loosening or data expansion.",
        }
    if reviewer_burden_rating == "red":
        return {
            "recommendation": "narrow_sources",
            "rationale": "Reviewer burden was rated red; narrow sources or evidence fields before expansion.",
        }
    return {
        "recommendation": "expand_to_100_200",
        "rationale": "No blocking warning was detected from aggregate labels, evidence sufficiency, calibration errors, or provided ratings.",
    }


def render_result_summary(synthesis: dict[str, Any]) -> list[str]:
    dataset = synthesis["dataset"]
    calibration = synthesis["calibration"]
    decision = synthesis["decision"]
    lines = [
        "# Pilot Result Summary Draft",
        "",
        "## Dataset Composition",
        "",
        _table_from_counts("Label bucket", dataset["label_counts"]),
        "",
        _table_from_counts("Risk level", dataset["risk_counts"]),
        "",
        "## Evidence And Source Shape",
        "",
        _table_from_counts("Evidence sufficiency", dataset["evidence_sufficiency_counts"]),
        "",
        _table_from_counts("Content shape", dataset["content_shape_counts"]),
        "",
        _table_from_counts("Source type", dataset["source_type_counts"]),
        "",
        "## Calibration Summary",
        "",
    ]
    rows = calibration.get("calibration_summary", [])
    if rows:
        lines.extend(
            [
                "| Profile | Variant | Binary items | Precision | Recall | F1 | FP | FN | High | Medium | Low |",
                "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for row in rows:
            if row["variant"] == "all":
                lines.append(
                    "| {profile} | {variant} | {binary_metric_items} | {precision:.3f} | {recall:.3f} | {f1:.3f} | {false_positive} | {false_negative} | {high_predictions} | {medium_predictions} | {low_predictions} |".format(
                        **row
                    )
                )
    else:
        lines.append("- Calibration artifacts were not provided.")
    lines.extend(
        [
            "",
            "## Warning Flags",
            "",
        ]
    )
    warnings = synthesis["warnings"]
    if warnings:
        for warning in warnings:
            lines.append(f"- `{warning['severity']}` `{warning['code']}`: {warning['message']}")
    else:
        lines.append("- No warning flags from the aggregate synthesis.")
    lines.extend(
        [
            "",
            "## Recommended Decision",
            "",
            f"- Recommendation: `{decision['recommendation']}`",
            f"- Rationale: {decision['rationale']}",
        ]
    )
    return lines


def render_decision_memo(synthesis: dict[str, Any]) -> list[str]:
    dataset = synthesis["dataset"]
    decision = synthesis["decision"]
    ratings = synthesis["ratings"]
    return [
        "# Pilot Decision Memo Draft",
        "",
        "## Executive Decision",
        "",
        f"Decision: `{decision['recommendation']}`",
        "",
        decision["rationale"],
        "",
        "## Inputs Reviewed",
        "",
        "| Input | Reviewed? | Notes |",
        "|---|---|---|",
        "| Dataset records | yes | Aggregate counts only. |",
        "| Calibration run | yes | If provided, only local aggregate artifacts were read. |",
        "| Raw evidence | no | This script must not inspect raw screenshots, URLs, or personal data. |",
        "",
        "## Decision Rubric",
        "",
        "| Dimension | Rating | Notes |",
        "|---|---|---|",
        f"| Governance | {ratings['governance']} | Provide final human rating before real expansion. |",
        f"| Privacy/redaction | {ratings['privacy_redaction']} | Provide final human rating before real expansion. |",
        "| Schema completeness | auto | See evidence sufficiency and warning flags. |",
        "| Label quality | auto | See uncertain/insufficient-evidence rates. |",
        "| Evidence sufficiency | auto | See summary counts. |",
        "| Baseline usefulness | auto | See calibration and error counts. |",
        f"| Reviewer burden | {ratings['reviewer_burden']} | Provide final human rating before real expansion. |",
        "",
        "## Dataset Summary",
        "",
        f"- Total items: {dataset['total_items']}",
        f"- Label counts: `{dataset['label_counts']}`",
        f"- Evidence sufficiency counts: `{dataset['evidence_sufficiency_counts']}`",
        "",
        "## Required Human Checks Before Finalizing",
        "",
        "- Confirm governance and privacy/redaction ratings.",
        "- Review false positives and false negatives manually.",
        "- Confirm reviewer burden and confusing fields.",
        "- Replace this draft with final project-owner rationale before committing a real pilot decision.",
    ]


def content_shape(record: dict[str, Any]) -> str:
    has_text = bool(str(record.get("post_text") or "").strip())
    has_image = bool(record.get("has_image"))
    has_reply = bool(record.get("has_reply") or record.get("reply_texts"))
    has_ocr = bool(str(record.get("ocr_text") or "").strip())
    has_link = bool(record.get("has_external_link") or record.get("external_links"))
    redirects = [value for value in record.get("visible_platform_redirects", []) if value != "none"]

    if has_image and has_ocr and record.get("screenshot_style") in {"screenshot_style", "screenshot_heavy"}:
        return "screenshot_ocr"
    if has_text and has_image:
        return "text_image_post"
    if has_reply:
        return "reply_context"
    if has_link or redirects:
        return "link_or_redirect"
    if has_text:
        return "text_only"
    return "low_context"


def _rates(counts: Counter[str], total: int) -> dict[str, float]:
    if total == 0:
        return {}
    return {key: round(value / total, 6) for key, value in sorted(counts.items())}


def _table_from_counts(label: str, counts: dict[str, int]) -> str:
    lines = [
        f"| {label} | Count |",
        "|---|---:|",
    ]
    for key, value in counts.items():
        lines.append(f"| `{key}` | {value} |")
    return "\n".join(lines)
