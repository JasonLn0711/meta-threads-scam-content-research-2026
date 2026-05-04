#!/usr/bin/env python3
"""Report on or convert completed candidate intake entries into v2 records."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from engine.common import load_schema, load_sparse_schema, load_yaml, write_yaml
from engine.exploration.convert_intake import build_intake_conversion_report
from engine.exploration.intake import validate_candidate_intake


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "intake_path",
        nargs="?",
        type=Path,
        default=Path("data/candidate_intake/batch_0004_intake.yaml"),
        help="Candidate intake YAML to inspect or convert",
    )
    parser.add_argument(
        "--report-output",
        type=Path,
        default=Path("data/candidate_intake/batch_0004_conversion_report.yaml"),
        help="Where to write the conversion report",
    )
    parser.add_argument(
        "--write-candidates",
        action="store_true",
        help="Write candidate_record_v2 files for entries that pass every gate",
    )
    parser.add_argument(
        "--fail-on-blocked",
        action="store_true",
        help="Return a non-zero status when any intake entry is blocked",
    )
    args = parser.parse_args()

    intake = load_yaml(args.intake_path)
    if not isinstance(intake, dict):
        print(f"error: {args.intake_path} must contain a YAML object")
        return 1

    intake_errors = validate_candidate_intake(intake)
    if intake_errors:
        for error in intake_errors:
            print(f"error: {error}")
        return 1

    report = build_intake_conversion_report(
        intake,
        load_schema(),
        load_sparse_schema(),
        write_candidates=args.write_candidates,
        repo_root=REPO_ROOT,
    )
    write_yaml(args.report_output, report)

    summary = report["summary"]
    print(f"conversion_report_written: {args.report_output}")
    print(f"intake_count: {summary['intake_count']}")
    print(f"converted_count: {summary['converted_count']}")
    print(f"blocked_count: {summary['blocked_count']}")
    print(f"written_count: {summary['written_count']}")
    print(f"status: {report['status']}")

    if args.fail_on_blocked and summary["blocked_count"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
