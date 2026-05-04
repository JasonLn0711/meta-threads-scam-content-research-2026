#!/usr/bin/env python3
"""Build a metadata-only candidate intake worksheet for Batch 0004."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from engine.common import load_yaml, write_yaml
from engine.exploration.intake import build_candidate_intake, validate_candidate_intake


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-plan", type=Path, default=Path("exploration/batches/batch_0004.yaml"))
    parser.add_argument("--stub-batch", type=Path, default=Path("data/candidate_stubs/batch_0004.yaml"))
    parser.add_argument("--output", type=Path, default=Path("data/candidate_intake/batch_0004_intake.yaml"))
    args = parser.parse_args()

    batch_plan = _require_mapping(load_yaml(args.batch_plan), args.batch_plan)
    stub_batch = _require_mapping(load_yaml(args.stub_batch), args.stub_batch)
    intake = build_candidate_intake(stub_batch, batch_plan)
    errors = validate_candidate_intake(intake, expected_count=stub_batch.get("summary", {}).get("stub_count"))
    if errors:
        for error in errors:
            print(f"error: {error}")
        return 1

    write_yaml(args.output, intake)
    print(f"candidate_intake_written: {args.output}")
    print(f"intake_entries: {len(intake['intake_entries'])}")
    print(f"status: {intake['status']}")
    return 0


def _require_mapping(value: object, path: Path) -> dict:
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a YAML object")
    return value


if __name__ == "__main__":
    raise SystemExit(main())
