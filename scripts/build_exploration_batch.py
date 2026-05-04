#!/usr/bin/env python3
"""Build a small metadata-only exploration batch from generated tasks."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from engine.common import load_yaml, write_yaml
from engine.exploration.batch import build_exploration_batch


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tasks", type=Path, default=Path("exploration/tasks/latest.yaml"))
    parser.add_argument("--stubs", type=Path, default=Path("data/candidate_stubs/latest.yaml"))
    parser.add_argument("--batch-id", default="batch-0004-low-coverage-high-svs")
    parser.add_argument("--selected-task-id", action="append", default=["EXP_0001", "EXP_0002"])
    parser.add_argument(
        "--batch-output",
        type=Path,
        default=Path("exploration/batches/batch_0004.yaml"),
    )
    parser.add_argument(
        "--stub-output",
        type=Path,
        default=Path("data/candidate_stubs/batch_0004.yaml"),
    )
    args = parser.parse_args()

    tasks_payload = _require_mapping(load_yaml(args.tasks), args.tasks)
    stubs_payload = _require_mapping(load_yaml(args.stubs), args.stubs)
    batch, stub_batch = build_exploration_batch(
        tasks_payload,
        stubs_payload,
        batch_id=args.batch_id,
        selected_task_ids=args.selected_task_id,
    )
    write_yaml(args.batch_output, batch)
    write_yaml(args.stub_output, stub_batch)

    print(f"batch_written: {args.batch_output}")
    print(f"selected_task_count: {len(batch['selected_tasks'])}")
    print(f"candidate_stub_count: {batch['candidate_stub_count']}")
    print(f"stub_batch_written: {args.stub_output}")
    return 0


def _require_mapping(value: object, path: Path) -> dict:
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a YAML object")
    return value


if __name__ == "__main__":
    raise SystemExit(main())
