#!/usr/bin/env python3
"""Generate ranked feature hypotheses from the latest discrepancy report."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from engine.common import load_candidates, load_sparse_schema, load_yaml, write_yaml
from engine.feature_discovery.auto_generate import auto_generate_feature_candidates


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--discrepancy-report",
        type=Path,
        default=Path("outputs/discrepancy_reports/latest.yaml"),
    )
    parser.add_argument("--candidate-dir", type=Path, default=Path("data/candidates"))
    parser.add_argument(
        "--candidate-schema",
        type=Path,
        default=Path("data-contracts/candidate_record_v2.schema.yaml"),
    )
    parser.add_argument(
        "--sparse-schema",
        type=Path,
        default=Path("meta-system/sparse_schema/sparse_features_v2.yaml"),
    )
    parser.add_argument("--min-group-size", type=int, default=3)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("meta-system/feature_candidates/auto_generated_v1.yaml"),
    )
    args = parser.parse_args()

    sparse_schema = load_sparse_schema(args.sparse_schema)
    candidates = load_candidates(
        args.candidate_dir,
        schema_path=args.candidate_schema,
        sparse_schema_path=args.sparse_schema,
        validate=True,
    )
    discrepancy_report = load_yaml(args.discrepancy_report)
    if not isinstance(discrepancy_report, dict):
        raise ValueError(f"{args.discrepancy_report} must contain a YAML object")

    output = auto_generate_feature_candidates(
        discrepancy_report,
        candidates,
        min_group_size=args.min_group_size,
    )
    output["sparse_schema_version"] = sparse_schema.get("schema_version")
    write_yaml(args.output, output)

    print(f"candidate_records_loaded: {len(candidates)}")
    print(f"input_case_count: {output['summary']['input_case_count']}")
    print(f"valid_group_count: {output['summary']['valid_group_count']}")
    print(f"feature_count: {output['summary']['feature_count']}")
    print(f"feature_candidates_written: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
