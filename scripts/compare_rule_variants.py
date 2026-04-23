#!/usr/bin/env python3
"""Compare rule baseline variants for Threads dataset v1."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from rule_baseline_v1 import predict_record
from thread_dataset_utils import load_records


VARIANTS = ["text_only", "text_reply", "text_ocr", "all"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Dataset file: .csv, .json, or .jsonl")
    parser.add_argument("--output", type=Path, help="Optional Markdown report path")
    parser.add_argument(
        "--variants",
        nargs="+",
        choices=VARIANTS,
        default=VARIANTS,
        help="Variants to compare",
    )
    args = parser.parse_args()

    records = load_records(args.input)
    predictions_by_variant = {
        variant: [predict_record(record, variant) for record in records] for variant in args.variants
    }
    report = render_report(records, predictions_by_variant)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(f"report_written: {args.output}")
    else:
        print(report)
    return 0


def render_report(
    records: list[dict[str, Any]],
    predictions_by_variant: dict[str, list[dict[str, str]]],
) -> str:
    lines: list[str] = []
    lines.append("# Rule Baseline Variant Comparison")
    lines.append("")
    lines.append(f"- Items: {len(records)}")
    lines.append(f"- Variants: {', '.join(predictions_by_variant)}")
    lines.append("")
    lines.append("## Metric Summary")
    lines.append("")
    lines.append("| Variant | Binary items | TP | FP | FN | Precision | Recall | F1 | High-risk predictions |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    metrics_by_variant = {
        variant: compute_metrics(predictions) for variant, predictions in predictions_by_variant.items()
    }
    for variant, metrics in metrics_by_variant.items():
        lines.append(
            "| {variant} | {binary_items} | {tp} | {fp} | {fn} | {precision:.3f} | {recall:.3f} | {f1:.3f} | {high_risk} |".format(
                variant=variant,
                **metrics,
            )
        )
    lines.append("")

    if "text_only" in predictions_by_variant:
        lines.extend(render_changed_decisions(predictions_by_variant))

    lines.append("## Interpretation Notes")
    lines.append("")
    lines.append("- Treat this as a baseline QA report, not a production performance claim.")
    lines.append("- Compare `text_only` to `text_ocr` to estimate OCR lift.")
    lines.append("- Compare `text_only` to `text_reply` to estimate reply-context lift.")
    lines.append("- Compare `text_only` to `all` to estimate the value of all low-cost signals.")
    lines.append("- Review false positives manually before tuning rules.")
    lines.append("")
    return "\n".join(lines)


def compute_metrics(predictions: list[dict[str, str]]) -> dict[str, float | int]:
    binary = [prediction for prediction in predictions if prediction["gold_label"] in {"scam", "non_scam"}]
    tp = sum(1 for pred in binary if pred["gold_label"] == "scam" and pred["predicted_label"] == "scam")
    fp = sum(1 for pred in binary if pred["gold_label"] == "non_scam" and pred["predicted_label"] == "scam")
    fn = sum(1 for pred in binary if pred["gold_label"] == "scam" and pred["predicted_label"] != "scam")
    predicted_positive = tp + fp
    gold_positive = tp + fn
    precision = tp / predicted_positive if predicted_positive else 0.0
    recall = tp / gold_positive if gold_positive else 0.0
    f1 = (2 * precision * recall / (precision + recall)) if precision + recall else 0.0
    high_risk = sum(1 for pred in predictions if pred["predicted_risk_level"] == "high")
    return {
        "binary_items": len(binary),
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "high_risk": high_risk,
    }


def render_changed_decisions(predictions_by_variant: dict[str, list[dict[str, str]]]) -> list[str]:
    lines: list[str] = []
    baseline_by_id = {pred["item_id"]: pred for pred in predictions_by_variant["text_only"]}
    lines.append("## Changes Versus Text Only")
    lines.append("")
    for variant, predictions in predictions_by_variant.items():
        if variant == "text_only":
            continue
        changed = []
        for prediction in predictions:
            baseline = baseline_by_id.get(prediction["item_id"])
            if not baseline:
                continue
            if prediction["predicted_risk_level"] != baseline["predicted_risk_level"]:
                changed.append(
                    f"{prediction['item_id']}: {baseline['predicted_risk_level']} -> {prediction['predicted_risk_level']}"
                )
        lines.append(f"### `{variant}`")
        lines.append("")
        if changed:
            for item in changed[:30]:
                lines.append(f"- {item}")
            if len(changed) > 30:
                lines.append(f"- ... {len(changed) - 30} more")
        else:
            lines.append("- No risk-level changes.")
        lines.append("")
    return lines


if __name__ == "__main__":
    raise SystemExit(main())
