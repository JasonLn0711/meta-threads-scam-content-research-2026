#!/usr/bin/env python3
"""Evaluate repo-safe public-surface patrol records.

This script does not collect Threads data, open a browser, take screenshots, or
read raw evidence. It validates metadata-only records from a future authorized
public-surface patrol and computes reviewer-yield metrics such as
review_worthy_rate.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from engine.common import load_yaml, write_yaml


DEFAULT_SCHEMA = REPO_ROOT / "data-contracts" / "discovery_candidate_v1.schema.yaml"
REQUIRED_TRACE_KEYS = {
    "route_type",
    "query_text_or_query_ref",
    "entry_point",
    "capture_time",
    "scroll_depth_bucket",
    "surface_position_bucket",
    "public_surface_check",
}


class PatrolRecordError(ValueError):
    """Raised when a public-surface patrol record is not repo-safe."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Metadata-only patrol record YAML file or directory")
    parser.add_argument(
        "--schema",
        type=Path,
        default=DEFAULT_SCHEMA,
        help="Discovery candidate v1 schema YAML",
    )
    parser.add_argument("--output", type=Path, default=None, help="Optional summary YAML output path")
    return parser.parse_args()


def yaml_paths(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(path.rglob("*.yaml")) + sorted(path.rglob("*.yml"))


def forbidden_key_set(schema: dict[str, Any]) -> set[str]:
    extra = {
        "search_url",
        "screenshot_local_path",
        "screenshot_filename",
        "visible_text",
        "body_text",
        "page_text",
        "html",
        "dom_text",
        "raw_artifact_path",
    }
    return {str(key).lower() for key in schema.get("forbidden_keys", [])} | extra


def forbidden_patterns(schema: dict[str, Any]) -> list[re.Pattern[str]]:
    return [
        re.compile(str(pattern), re.IGNORECASE)
        for pattern in schema.get("forbidden_string_patterns", [])
    ]


def validate_no_forbidden_content(
    value: Any,
    forbidden_keys: set[str],
    patterns: list[re.Pattern[str]],
    path: str = "",
) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            key_text = str(key)
            location = f"{path}.{key_text}" if path else key_text
            if key_text.lower() in forbidden_keys:
                raise PatrolRecordError(f"forbidden raw/sensitive field {location!r}")
            validate_no_forbidden_content(child, forbidden_keys, patterns, location)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            validate_no_forbidden_content(child, forbidden_keys, patterns, f"{path}[{index}]")
    elif isinstance(value, str):
        for pattern in patterns:
            if pattern.search(value):
                raise PatrolRecordError(f"forbidden raw/sensitive string at {path!r}")


def validate_public_surface_patrol_record(record: dict[str, Any], schema: dict[str, Any]) -> None:
    validate_no_forbidden_content(record, forbidden_key_set(schema), forbidden_patterns(schema))

    if record.get("schema_version") != "discovery_candidate_v1":
        raise PatrolRecordError("schema_version must be discovery_candidate_v1")
    if record.get("source_arm_id") != "controlled_browser_run_scoped":
        raise PatrolRecordError("source_arm_id must be controlled_browser_run_scoped")
    if record.get("source_access_mode") != "controlled_browser_run_scoped":
        raise PatrolRecordError("source_access_mode must be controlled_browser_run_scoped")
    if record.get("source_access_submode") != "public_surface_human_reproducible_patrol_v0":
        raise PatrolRecordError(
            "source_access_submode must be public_surface_human_reproducible_patrol_v0"
        )

    trace = record.get("human_reproducibility_trace")
    if not isinstance(trace, dict):
        raise PatrolRecordError("human_reproducibility_trace must be a mapping")
    missing_trace = sorted(REQUIRED_TRACE_KEYS - set(trace))
    if missing_trace:
        raise PatrolRecordError(f"human_reproducibility_trace missing: {', '.join(missing_trace)}")
    if trace.get("public_surface_check") is not True:
        raise PatrolRecordError("human_reproducibility_trace.public_surface_check must be true")
    artifact_ref = trace.get("raw_artifact_ref")
    if artifact_ref is not None and not isinstance(artifact_ref, str):
        raise PatrolRecordError("human_reproducibility_trace.raw_artifact_ref must be a string if present")

    review = record.get("review")
    if not isinstance(review, dict):
        raise PatrolRecordError("review must be a mapping")
    if "review_worthy" in review and not isinstance(review["review_worthy"], bool):
        raise PatrolRecordError("review.review_worthy must be boolean when present")


def review_worthy(record: dict[str, Any]) -> bool | None:
    review = record.get("review", {})
    if not isinstance(review, dict):
        return None
    if isinstance(review.get("review_worthy"), bool):
        return bool(review["review_worthy"])
    label = review.get("human_final_label_or_not_reviewable")
    if label in {"scam", "uncertain", "insufficient_evidence"}:
        return True
    if label in {"non_scam", "not_reviewable"}:
        return False
    return None


def build_summary(paths: list[Path], schema: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    valid_records: list[dict[str, Any]] = []

    for path in paths:
        try:
            payload = load_yaml(path)
            if not isinstance(payload, dict):
                raise PatrolRecordError("record must be a YAML object")
            validate_public_surface_patrol_record(payload, schema)
            valid_records.append(payload)
        except (PatrolRecordError, OSError) as exc:
            errors.append(f"{path}: {exc}")

    label_counts: Counter[str] = Counter()
    reviewed_count = 0
    worthy_count = 0
    unresolved_review_worthy = 0
    reproducible_count = 0
    query_counts: Counter[str] = Counter()
    query_worthy_counts: Counter[str] = Counter()

    for record in valid_records:
        review = record.get("review", {})
        if isinstance(review, dict):
            label = str(review.get("human_final_label_or_not_reviewable") or "pending")
            label_counts[label] += 1
            if label != "pending":
                reviewed_count += 1
        worthy = review_worthy(record)
        if worthy is True:
            worthy_count += 1
        elif worthy is None:
            unresolved_review_worthy += 1

        trace = record.get("human_reproducibility_trace", {})
        if isinstance(trace, dict) and trace.get("public_surface_check") is True:
            reproducible_count += 1
            query_ref = str(trace.get("query_text_or_query_ref") or "unknown")
            query_counts[query_ref] += 1
            if worthy is True:
                query_worthy_counts[query_ref] += 1

    generated_count = len(valid_records)
    review_worthy_rate = worthy_count / generated_count if generated_count else 0.0
    reproducible_route_rate = reproducible_count / generated_count if generated_count else 0.0
    by_query = []
    for query_ref, count in sorted(query_counts.items()):
        worthy = query_worthy_counts[query_ref]
        by_query.append(
            {
                "query_text_or_query_ref": query_ref,
                "candidate_count": count,
                "review_worthy_count": worthy,
                "review_worthy_rate": worthy / count if count else 0.0,
            }
        )

    return {
        "schema_version": "public_surface_patrol_review_metrics_v1",
        "source_records_checked": len(paths),
        "valid_record_count": generated_count,
        "invalid_record_count": len(errors),
        "generated_candidate_count": generated_count,
        "reviewed_count": reviewed_count,
        "review_worthy_count": worthy_count,
        "review_worthy_rate": round(review_worthy_rate, 6),
        "unresolved_review_worthy_count": unresolved_review_worthy,
        "human_reproducible_route_count": reproducible_count,
        "human_reproducible_route_rate": round(reproducible_route_rate, 6),
        "raw_evidence_leakage_incidents": len(errors),
        "label_counts": dict(sorted(label_counts.items())),
        "by_query": by_query,
        "errors": errors,
    }


def main() -> int:
    args = parse_args()
    schema = load_yaml(args.schema)
    if not isinstance(schema, dict):
        print(f"error: {args.schema} must contain a YAML object")
        return 1

    paths = yaml_paths(args.path)
    summary = build_summary(paths, schema)
    if args.output:
        write_yaml(args.output, summary)

    print(f"source_records_checked: {summary['source_records_checked']}")
    print(f"valid_record_count: {summary['valid_record_count']}")
    print(f"invalid_record_count: {summary['invalid_record_count']}")
    print(f"review_worthy_rate: {summary['review_worthy_rate']}")
    print(f"human_reproducible_route_rate: {summary['human_reproducible_route_rate']}")
    for error in summary["errors"]:
        print(f"- {error}")
    return 1 if summary["invalid_record_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
