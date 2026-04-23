#!/usr/bin/env python3
"""Run rule-baseline variant and threshold calibration workbench."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.baselines.io_utils import load_records, write_json, write_summary
from src.baselines.types import VALID_VARIANTS
from src.evaluation.calibration import (
    changed_decisions,
    export_reviewer_worksheet,
    load_calibration_profiles,
    render_calibration_report,
    run_calibration_matrix,
    summarize_matrix,
)
from src.evaluation.error_analysis import error_analysis


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Dataset file: .csv, .json, or .jsonl")
    parser.add_argument(
        "--base-config",
        type=Path,
        default=Path("configs/baseline_rule_config.yaml"),
        help="Base rule config YAML path",
    )
    parser.add_argument(
        "--profile-config",
        type=Path,
        default=Path("configs/rule_calibration_variants.yaml"),
        help="Calibration profile YAML path",
    )
    parser.add_argument(
        "--variants",
        nargs="+",
        choices=VALID_VARIANTS,
        default=list(VALID_VARIANTS),
        help="Evidence variants to compare",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("experiments/baselines/outputs"),
        help="Directory for local generated calibration outputs",
    )
    parser.add_argument("--run-name", help="Optional run directory name")
    args = parser.parse_args()

    records = load_records(args.input)
    profiles = load_calibration_profiles(args.profile_config)
    matrix = run_calibration_matrix(records, args.base_config, profiles, args.variants)
    summary_rows = summarize_matrix(records, matrix)
    changes = changed_decisions(matrix)

    run_name = args.run_name or default_run_name()
    run_dir = args.output_dir / run_name
    run_dir.mkdir(parents=True, exist_ok=True)

    baseline_all = matrix.get("baseline", {}).get("all")
    worksheet_predictions = baseline_all or next(iter(next(iter(matrix.values())).values()))
    worksheet_path = run_dir / "reviewer_worksheet.csv"
    export_reviewer_worksheet(worksheet_path, records, worksheet_predictions)

    baseline_errors = error_analysis(records, worksheet_predictions)
    write_json(run_dir / "calibration_summary.json", summary_rows)
    write_json(run_dir / "changed_decisions.json", changes)
    write_json(run_dir / "baseline_all_error_analysis.json", baseline_errors)
    write_json(run_dir / "matrix_predictions.json", matrix)

    report = render_calibration_report(
        input_path=str(args.input),
        base_config_path=str(args.base_config),
        profile_path=str(args.profile_config),
        summary_rows=summary_rows,
        changes=changes,
        baseline_all_errors=baseline_errors,
        worksheet_path=str(worksheet_path),
    )
    write_summary(run_dir / "calibration_report.md", report)

    print(f"run_dir: {run_dir}")
    print(f"items: {len(records)}")
    print(f"profiles: {', '.join(profiles)}")
    print(f"variants: {', '.join(args.variants)}")
    print(f"summary_rows: {len(summary_rows)}")
    print(f"changed_decisions: {len(changes)}")
    print(f"reviewer_worksheet: {worksheet_path}")
    return 0


def default_run_name() -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"rule-calibration-{timestamp}"


if __name__ == "__main__":
    raise SystemExit(main())
