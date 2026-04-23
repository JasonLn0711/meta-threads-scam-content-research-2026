#!/usr/bin/env python3
"""Compatibility wrapper for the first Threads rule baseline.

The implementation now lives under ``src/baselines``. This wrapper preserves
the original CSV-oriented CLI used by existing experiment docs.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.baselines.io_utils import load_records
from src.baselines.risk_scoring import load_rule_config
from src.baselines.rule_based import predict_item
from src.baselines.types import VALID_VARIANTS
from src.evaluation.metrics import binary_metrics


DEFAULT_CONFIG = Path("configs/baseline_rule_config.yaml")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Dataset file: .csv, .json, or .jsonl")
    parser.add_argument(
        "--variant",
        choices=VALID_VARIANTS,
        default="all",
        help="Evidence fields to use",
    )
    parser.add_argument("--output", type=Path, help="Optional prediction CSV path")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG, help="Rule config YAML path")
    args = parser.parse_args()

    records = load_records(args.input)
    predictions = [predict_record(record, args.variant, config_path=args.config) for record in records]

    if args.output:
        write_predictions(args.output, predictions)
    else:
        write_predictions_to_handle(sys.stdout, predictions)

    print_metrics(records, predictions, args.variant, args.output)
    return 0


def predict_record(
    record: dict[str, Any],
    variant: str,
    config_path: Path = DEFAULT_CONFIG,
) -> dict[str, str]:
    config = load_rule_config(config_path)
    prediction = predict_item(record, config=config, variant=variant)
    risk = str(prediction["risk_level_pred"])
    legacy_label = "scam" if risk == "high" else "uncertain" if risk == "medium" else "non_scam"

    return {
        "item_id": str(record.get("item_id", "")),
        "baseline_variant": variant,
        "predicted_label": legacy_label,
        "predicted_risk_level": risk,
        "matched_signal_tags": "|".join(prediction["reason_codes"]) if prediction["reason_codes"] else "none",
        "baseline_reasons": " ".join(prediction["explanations"]) if prediction["explanations"] else "No baseline risk pattern matched.",
        "gold_label": str(record.get("final_label") or record.get("scam_label") or ""),
        "gold_risk_level": str(record.get("final_risk_level") or record.get("risk_level") or ""),
    }


def write_predictions(path: Path, predictions: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        write_predictions_to_handle(handle, predictions)


def write_predictions_to_handle(handle: Any, predictions: list[dict[str, str]]) -> None:
    fieldnames = [
        "item_id",
        "baseline_variant",
        "predicted_label",
        "predicted_risk_level",
        "matched_signal_tags",
        "baseline_reasons",
        "gold_label",
        "gold_risk_level",
    ]
    writer = csv.DictWriter(handle, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(predictions)


def print_metrics(
    records: list[dict[str, Any]],
    predictions: list[dict[str, str]],
    variant: str,
    output: Path | None,
) -> None:
    modular_predictions = [
        {
            "binary_pred": "scam_like" if prediction["predicted_label"] == "scam" else "not_scam_like"
        }
        for prediction in predictions
    ]
    metrics = binary_metrics(records, modular_predictions)
    stream = sys.stderr if output is None else sys.stdout
    print("", file=stream)
    print(f"baseline_variant: {variant}", file=stream)
    print(f"items: {len(records)}", file=stream)
    print(f"binary_metric_items: {metrics['binary_metric_items']}", file=stream)
    print(f"true_positive: {metrics['true_positive']}", file=stream)
    print(f"false_positive: {metrics['false_positive']}", file=stream)
    print(f"false_negative: {metrics['false_negative']}", file=stream)
    print(f"precision: {metrics['precision']:.3f}", file=stream)
    print(f"recall: {metrics['recall']:.3f}", file=stream)
    print(f"f1: {metrics['f1']:.3f}", file=stream)
    if output:
        print(f"predictions_written: {output}", file=stream)


if __name__ == "__main__":
    raise SystemExit(main())
