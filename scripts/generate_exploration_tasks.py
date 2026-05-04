#!/usr/bin/env python3
"""Generate safe exploration tasks and metadata-only candidate stubs."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from engine.common import load_yaml, write_yaml
from engine.exploration.generate import generate_exploration_plan


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ranking", type=Path, default=Path("metrics/signal_scores/latest_ranking.yaml"))
    parser.add_argument("--discrepancy", type=Path, default=Path("outputs/discrepancy_reports/latest.yaml"))
    parser.add_argument("--embedding", type=Path, default=Path("outputs/embedding_clusters/latest.yaml"))
    parser.add_argument("--stubs-per-task", type=int, default=5)
    parser.add_argument("--tasks-output", type=Path, default=Path("exploration/tasks/latest.yaml"))
    parser.add_argument("--stubs-output", type=Path, default=Path("data/candidate_stubs/latest.yaml"))
    args = parser.parse_args()

    ranking = _require_mapping(load_yaml(args.ranking), args.ranking)
    discrepancy = _require_mapping(load_yaml(args.discrepancy), args.discrepancy)
    embedding = _require_mapping(load_yaml(args.embedding), args.embedding)
    task_output, stub_output = generate_exploration_plan(
        ranking,
        discrepancy,
        embedding,
        stubs_per_task=args.stubs_per_task,
    )
    write_yaml(args.tasks_output, task_output)
    write_yaml(args.stubs_output, stub_output)

    print(f"tasks_written: {args.tasks_output}")
    print(f"task_count: {task_output['summary']['task_count']}")
    print(f"candidate_stubs_written: {args.stubs_output}")
    print(f"stub_count: {stub_output['summary']['stub_count']}")
    return 0


def _require_mapping(value: object, path: Path) -> dict:
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a YAML object")
    return value


if __name__ == "__main__":
    raise SystemExit(main())
