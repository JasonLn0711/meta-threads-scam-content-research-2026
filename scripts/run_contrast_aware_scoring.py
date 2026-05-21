#!/usr/bin/env python3
"""Run contrast-aware reviewer routing over metadata-only candidate records."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from engine.common import load_candidates, load_sparse_schema, write_yaml
from engine.sparse.contrast import build_contrast_aware_scores


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate-dir", type=Path, default=Path("data/candidates"))
    parser.add_argument("--schema", type=Path, default=Path("data-contracts/candidate_record_v2.schema.yaml"))
    parser.add_argument(
        "--sparse-schema",
        type=Path,
        default=Path("meta-system/sparse_schema/sparse_features_v2.yaml"),
    )
    parser.add_argument("--output", type=Path, default=Path("metrics/contrast_scores/latest.yaml"))
    args = parser.parse_args()

    sparse_schema = load_sparse_schema(args.sparse_schema)
    candidates = load_candidates(
        args.candidate_dir,
        schema_path=args.schema,
        sparse_schema_path=args.sparse_schema,
        validate=True,
    )
    scores = build_contrast_aware_scores(candidates, sparse_schema)
    write_yaml(args.output, scores)

    print(f"candidate_count: {scores['candidate_count']}")
    print(f"lane_count: {len(scores['lane_scores'])}")
    print(f"contrast_scores_written: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
