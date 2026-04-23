#!/usr/bin/env python3
"""Run the modular Threads rule-based scam-content baseline."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.baselines.io_utils import load_records, write_json, write_summary
from src.baselines.risk_scoring import load_rule_config
from src.baselines.rule_based import predict_batch
from src.baselines.types import VALID_VARIANTS
from src.evaluation.error_analysis import error_analysis
from src.evaluation.metrics import binary_metrics, has_any_labels
from src.evaluation.triage_metrics import triage_metrics


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Dataset file: .csv, .json, or .jsonl")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/baseline_rule_config.yaml"),
        help="Rule config YAML path",
    )
    parser.add_argument(
        "--variant",
        choices=VALID_VARIANTS,
        default="all",
        help="Evidence fields to use",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("experiments/baselines/outputs"),
        help="Directory for local generated baseline outputs",
    )
    parser.add_argument(
        "--run-name",
        help="Optional run directory name. Defaults to a timestamped name.",
    )
    args = parser.parse_args()

    records = load_records(args.input)
    config = load_rule_config(args.config)
    predictions = predict_batch(records, config=config, variant=args.variant)

    run_name = args.run_name or default_run_name(args.variant)
    run_dir = args.output_dir / run_name
    run_dir.mkdir(parents=True, exist_ok=True)

    write_json(run_dir / "predictions.json", predictions)

    summary: dict[str, Any] = {
        "run_name": run_name,
        "input": str(args.input),
        "config": str(args.config),
        "variant": args.variant,
        "items": len(records),
        "predictions_path": str(run_dir / "predictions.json"),
    }

    if has_any_labels(records):
        evaluation = {
            "binary": binary_metrics(records, predictions),
            "triage": triage_metrics(records, predictions),
        }
        errors = error_analysis(records, predictions)
        summary["evaluation_summary_path"] = str(run_dir / "evaluation_summary.json")
        summary["error_analysis_path"] = str(run_dir / "error_analysis.json")
        write_json(run_dir / "evaluation_summary.json", evaluation)
        write_json(run_dir / "error_analysis.json", errors)
        summary["binary"] = evaluation["binary"]
        summary["triage"] = evaluation["triage"]
        summary["errors"] = {
            "false_positive_count": errors["false_positive_count"],
            "false_negative_count": errors["false_negative_count"],
            "medium_risk_ambiguity_count": errors["medium_risk_ambiguity_count"],
        }

    write_summary(run_dir / "summary.md", render_summary(summary))
    print_terminal_summary(summary, run_dir)
    return 0


def default_run_name(variant: str) -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"rule-baseline-{variant}-{timestamp}"


def render_summary(summary: dict[str, Any]) -> list[str]:
    lines = [
        "# Rule Baseline Run Summary",
        "",
        f"- Run name: `{summary['run_name']}`",
        f"- Input: `{summary['input']}`",
        f"- Config: `{summary['config']}`",
        f"- Variant: `{summary['variant']}`",
        f"- Items: {summary['items']}",
        f"- Predictions: `{summary['predictions_path']}`",
    ]
    if "evaluation_summary_path" in summary:
        binary = summary["binary"]
        triage = summary["triage"]
        lines.extend(
            [
                f"- Evaluation: `{summary['evaluation_summary_path']}`",
                f"- Error analysis: `{summary['error_analysis_path']}`",
                "",
                "## Binary Metrics",
                "",
                f"- Binary metric items: {binary['binary_metric_items']}",
                f"- Accuracy: {binary['accuracy']:.3f}",
                f"- Precision: {binary['precision']:.3f}",
                f"- Recall: {binary['recall']:.3f}",
                f"- F1: {binary['f1']:.3f}",
                f"- TP/TN/FP/FN: {binary['true_positive']}/{binary['true_negative']}/{binary['false_positive']}/{binary['false_negative']}",
                "",
                "## Triage Metrics",
                "",
                f"- Triage metric items: {triage['triage_metric_items']}",
                f"- Exact agreement: {triage['exact_agreement']:.3f}",
            ]
        )
    else:
        lines.append("- Evaluation: skipped because no labels were present.")
    return lines


def print_terminal_summary(summary: dict[str, Any], run_dir: Path) -> None:
    print(f"run_dir: {run_dir}")
    print(f"items: {summary['items']}")
    print(f"variant: {summary['variant']}")
    if "binary" in summary:
        binary = summary["binary"]
        print(f"binary_metric_items: {binary['binary_metric_items']}")
        print(f"precision: {binary['precision']:.3f}")
        print(f"recall: {binary['recall']:.3f}")
        print(f"f1: {binary['f1']:.3f}")
        print(f"false_positive: {binary['false_positive']}")
        print(f"false_negative: {binary['false_negative']}")
    else:
        print("evaluation: skipped_no_labels")


if __name__ == "__main__":
    raise SystemExit(main())
