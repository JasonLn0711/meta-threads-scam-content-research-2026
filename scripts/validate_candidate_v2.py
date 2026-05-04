#!/usr/bin/env python3
"""Validate metadata-only v2 candidate YAML records."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from engine.common import (
    CandidateValidationError,
    candidate_paths,
    load_schema,
    load_sparse_schema,
    load_yaml,
    validate_candidate,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Candidate YAML file or directory")
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path("data-contracts/candidate_record_v2.schema.yaml"),
        help="Candidate schema YAML",
    )
    parser.add_argument(
        "--sparse-schema",
        type=Path,
        default=Path("meta-system/sparse_schema/sparse_features_v2.yaml"),
        help="Sparse feature schema YAML",
    )
    args = parser.parse_args()

    schema = load_schema(args.schema)
    sparse_schema = load_sparse_schema(args.sparse_schema)
    paths = candidate_paths(args.path) if args.path.is_dir() else [args.path]

    errors: list[str] = []
    for path in paths:
        try:
            candidate = load_yaml(path)
            if not isinstance(candidate, dict):
                raise CandidateValidationError("candidate must be a YAML object")
            validate_candidate(candidate, schema, sparse_schema, source_path=path)
        except CandidateValidationError as exc:
            errors.append(str(exc))

    print(f"checked_candidates: {len(paths)}")
    print(f"errors: {len(errors)}")
    for error in errors:
        print(f"- {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
