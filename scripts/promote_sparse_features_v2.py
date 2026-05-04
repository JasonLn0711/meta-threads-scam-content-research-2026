#!/usr/bin/env python3
"""Promote only human-accepted v2 feature candidates into a sparse schema copy."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from engine.common import load_sparse_schema, load_yaml, write_yaml
from engine.feature_discovery.propose import promote_accepted_features


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sparse-schema",
        type=Path,
        default=Path("meta-system/sparse_schema/sparse_features_v1.yaml"),
    )
    parser.add_argument(
        "--feature-dir",
        type=Path,
        default=Path("meta-system/feature_candidates"),
    )
    parser.add_argument(
        "--review-queue",
        type=Path,
        default=Path("meta-system/feature_review_queue/latest.yaml"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("meta-system/sparse_schema/sparse_features_v2.yaml"),
    )
    args = parser.parse_args()

    sparse_schema = load_sparse_schema(args.sparse_schema)
    feature_candidates = []
    for path in sorted(args.feature_dir.glob("*.yaml")):
        candidate = load_yaml(path)
        if isinstance(candidate, dict) and candidate.get("feature_id"):
            feature_candidates.append(candidate)
    review_queue = load_yaml(args.review_queue)
    if not isinstance(review_queue, dict):
        raise ValueError(f"{args.review_queue} must contain a YAML object")

    updated_schema = promote_accepted_features(sparse_schema, feature_candidates, review_queue)
    if args.output.name == "sparse_features_v2.yaml":
        updated_schema["schema_version"] = "sparse_features_v2"
        updated_schema["title"] = "Sparse Feature Schema v2"
    promoted_count = len(updated_schema.get("features", {})) - len(sparse_schema.get("features", {}))
    write_yaml(args.output, updated_schema)

    print(f"feature_candidates_checked: {len(feature_candidates)}")
    print(f"promoted_features: {promoted_count}")
    print(f"updated_sparse_schema_written: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
