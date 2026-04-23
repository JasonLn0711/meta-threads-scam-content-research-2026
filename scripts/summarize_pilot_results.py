#!/usr/bin/env python3
"""Draft aggregate-only pilot result summary and decision memo."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.baselines.io_utils import load_records, write_json, write_summary
from src.evaluation.pilot_synthesis import (
    render_decision_memo,
    render_result_summary,
    synthesize_pilot,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Dataset file: .csv, .json, or .jsonl")
    parser.add_argument(
        "--calibration-run-dir",
        type=Path,
        help="Optional run directory from scripts/run_rule_calibration.py",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("experiments/evaluation-notes/outputs"),
        help="Directory for local generated synthesis outputs",
    )
    parser.add_argument("--run-name", help="Optional run directory name")
    parser.add_argument(
        "--governance-rating",
        choices=["green", "yellow", "red", "unknown"],
        default="unknown",
    )
    parser.add_argument(
        "--privacy-rating",
        choices=["green", "yellow", "red", "unknown"],
        default="unknown",
    )
    parser.add_argument(
        "--reviewer-burden-rating",
        choices=["green", "yellow", "red", "unknown"],
        default="unknown",
    )
    args = parser.parse_args()

    records = load_records(args.input)
    synthesis = synthesize_pilot(
        records,
        calibration_run_dir=args.calibration_run_dir,
        governance_rating=args.governance_rating,
        privacy_rating=args.privacy_rating,
        reviewer_burden_rating=args.reviewer_burden_rating,
    )

    run_name = args.run_name or default_run_name()
    run_dir = args.output_dir / run_name
    run_dir.mkdir(parents=True, exist_ok=True)

    write_json(run_dir / "pilot_synthesis_summary.json", synthesis)
    write_summary(run_dir / "pilot_result_summary_draft.md", render_result_summary(synthesis))
    write_summary(run_dir / "pilot_decision_memo_draft.md", render_decision_memo(synthesis))

    print(f"run_dir: {run_dir}")
    print(f"items: {synthesis['dataset']['total_items']}")
    print(f"recommendation: {synthesis['decision']['recommendation']}")
    print(f"warnings: {len(synthesis['warnings'])}")
    print(f"result_summary: {run_dir / 'pilot_result_summary_draft.md'}")
    print(f"decision_memo: {run_dir / 'pilot_decision_memo_draft.md'}")
    return 0


def default_run_name() -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"pilot-synthesis-{timestamp}"


if __name__ == "__main__":
    raise SystemExit(main())
