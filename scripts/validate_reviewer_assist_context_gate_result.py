#!/usr/bin/env python3
"""Validate and recompute the Batch 0012 context-gate result."""

from __future__ import annotations

import argparse
import math
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from engine.common import load_yaml


DEFAULT_RESULT = REPO_ROOT / "data" / "reviewer_assist_eval" / "batch_0012_context_gate_result.yaml"
DEFAULT_PACKET = REPO_ROOT / "data" / "reviewer_assist_eval" / "batch_0012_reviewer_context_gate_packet.yaml"

REQUIRED_REVIEWER_FIELDS = (
    "context_gate_review_time_seconds",
    "human_context_gate_decision",
    "metadata_only_label_or_not_reviewable",
    "context_gate_usefulness_rating",
    "context_gate_omission_risk",
    "context_gate_status",
    "minimal_context_request_status",
    "over_request_risk",
    "under_request_risk",
    "second_review_required",
    "insufficient_evidence",
    "raw_evidence_excluded_from_git",
)

DECISIONS = {
    "metadata_sufficient_for_label",
    "needs_thread_before_label",
    "needs_second_review_before_label",
    "hard_negative_metadata_sufficient",
    "not_reviewable_metadata_only",
}

LABELS = {"scam", "non_scam", "uncertain", "not_reviewable", "not_applicable"}
RISK = {"low", "medium", "high"}
CONTEXT_GATE_STATUS = {"accepted", "accepted_with_minor_correction", "needs_major_correction", "unusable"}
MINIMAL_CONTEXT_STATUS = {
    "accepted",
    "accepted_with_minor_correction",
    "over_requested",
    "under_requested",
    "not_applicable",
}

FORBIDDEN_KEYS = {
    "raw_threads_text",
    "raw_reply_text",
    "raw_ocr_text",
    "url",
    "urls",
    "handle",
    "handles",
    "screenshot",
    "screenshots",
    "browser_artifact",
    "browser_artifacts",
    "controlled_store_locator",
    "controlled_store_locators",
    "credential",
    "credentials",
    "cookie",
    "cookies",
    "token",
    "tokens",
    "stakeholder_case_id",
}


def percentile(values: list[float], p: float) -> float:
    ordered = sorted(values)
    if not ordered:
        return 0.0
    rank = (len(ordered) - 1) * p
    lower = math.floor(rank)
    upper = math.ceil(rank)
    if lower == upper:
        return ordered[int(rank)]
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (rank - lower)


def rate(numerator: int, denominator: int) -> float:
    return 0.0 if denominator == 0 else numerator / denominator


def compute_summary(entries: list[dict[str, Any]]) -> dict[str, Any]:
    times = [float(entry["reviewer_fields"]["context_gate_review_time_seconds"]) for entry in entries]
    decisions = Counter(entry["reviewer_fields"]["human_context_gate_decision"] for entry in entries)
    labels = Counter(entry["reviewer_fields"]["metadata_only_label_or_not_reviewable"] for entry in entries)

    by_role: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in entries:
        role = entry["reviewer_visible_metadata"]["slice_role"]
        by_role[role].append(entry)

    def role_times(role: str) -> list[float]:
        return [float(entry["reviewer_fields"]["context_gate_review_time_seconds"]) for entry in by_role[role]]

    target = by_role["target_thread_required"]
    boundary = by_role["boundary_control"]
    hard_negative = by_role["hard_negative_control"]
    fast_lane = by_role["fast_lane_control"]

    return {
        "reviewed_count": len(entries),
        "total_context_gate_review_time_seconds": round(sum(times), 6),
        "average_context_gate_review_time_seconds": round(statistics.mean(times), 6),
        "median_context_gate_review_time_seconds": round(statistics.median(times), 6),
        "p95_context_gate_review_time_seconds": round(percentile(times, 0.95), 6),
        "decision_counts": {
            "needs_thread_before_label": decisions["needs_thread_before_label"],
            "needs_second_review_before_label": decisions["needs_second_review_before_label"],
            "hard_negative_metadata_sufficient": decisions["hard_negative_metadata_sufficient"],
            "metadata_sufficient_for_label": decisions["metadata_sufficient_for_label"],
            "not_reviewable_metadata_only": decisions["not_reviewable_metadata_only"],
        },
        "metadata_only_label_counts": {
            "scam": labels["scam"],
            "non_scam": labels["non_scam"],
            "uncertain": labels["uncertain"],
            "not_reviewable": labels["not_reviewable"],
            "not_applicable": labels["not_applicable"],
        },
        "target_thread_required": {
            "count": len(target),
            "correct_thread_before_label_count": sum(
                entry["reviewer_fields"]["human_context_gate_decision"] == "needs_thread_before_label"
                for entry in target
            ),
            "correct_thread_before_label_rate": rate(
                sum(
                    entry["reviewer_fields"]["human_context_gate_decision"] == "needs_thread_before_label"
                    for entry in target
                ),
                len(target),
            ),
            "metadata_only_overreach_count": sum(
                entry["reviewer_fields"]["metadata_only_label_or_not_reviewable"] in {"scam", "non_scam"}
                for entry in target
            ),
            "average_context_gate_review_time_seconds": round(statistics.mean(role_times("target_thread_required")), 6),
            "second_review_rate": rate(sum(entry["reviewer_fields"]["second_review_required"] for entry in target), len(target)),
            "insufficient_evidence_rate": rate(sum(entry["reviewer_fields"]["insufficient_evidence"] for entry in target), len(target)),
        },
        "boundary_control": {
            "count": len(boundary),
            "boundary_control_over_request_count": sum(
                entry["reviewer_fields"]["human_context_gate_decision"] == "needs_thread_before_label"
                for entry in boundary
            ),
            "second_review_before_label_count": sum(
                entry["reviewer_fields"]["human_context_gate_decision"] == "needs_second_review_before_label"
                for entry in boundary
            ),
            "metadata_only_overreach_count": sum(
                entry["reviewer_fields"]["metadata_only_label_or_not_reviewable"] in {"scam", "non_scam"}
                for entry in boundary
            ),
            "average_context_gate_review_time_seconds": round(statistics.mean(role_times("boundary_control")), 6),
            "second_review_rate": rate(sum(entry["reviewer_fields"]["second_review_required"] for entry in boundary), len(boundary)),
            "insufficient_evidence_rate": rate(sum(entry["reviewer_fields"]["insufficient_evidence"] for entry in boundary), len(boundary)),
        },
        "hard_negative_control": {
            "count": len(hard_negative),
            "hard_negative_over_request_count": sum(
                entry["reviewer_fields"]["human_context_gate_decision"] == "needs_thread_before_label"
                for entry in hard_negative
            ),
            "hard_negative_preserved_count": sum(
                entry["reviewer_fields"]["human_context_gate_decision"] == "hard_negative_metadata_sufficient"
                for entry in hard_negative
            ),
            "hard_negative_preservation_rate": rate(
                sum(
                    entry["reviewer_fields"]["human_context_gate_decision"] == "hard_negative_metadata_sufficient"
                    for entry in hard_negative
                ),
                len(hard_negative),
            ),
            "average_context_gate_review_time_seconds": round(statistics.mean(role_times("hard_negative_control")), 6),
            "second_review_rate": rate(sum(entry["reviewer_fields"]["second_review_required"] for entry in hard_negative), len(hard_negative)),
            "insufficient_evidence_rate": rate(sum(entry["reviewer_fields"]["insufficient_evidence"] for entry in hard_negative), len(hard_negative)),
        },
        "fast_lane_control": {
            "count": len(fast_lane),
            "fast_lane_slowdown_count": sum(
                entry["reviewer_fields"]["human_context_gate_decision"] != "metadata_sufficient_for_label"
                for entry in fast_lane
            ),
            "metadata_sufficient_fast_lane_count": sum(
                entry["reviewer_fields"]["human_context_gate_decision"] == "metadata_sufficient_for_label"
                for entry in fast_lane
            ),
            "metadata_sufficient_fast_lane_rate": rate(
                sum(
                    entry["reviewer_fields"]["human_context_gate_decision"] == "metadata_sufficient_for_label"
                    for entry in fast_lane
                ),
                len(fast_lane),
            ),
            "average_context_gate_review_time_seconds": round(statistics.mean(role_times("fast_lane_control")), 6),
            "second_review_rate": rate(sum(entry["reviewer_fields"]["second_review_required"] for entry in fast_lane), len(fast_lane)),
            "insufficient_evidence_rate": rate(sum(entry["reviewer_fields"]["insufficient_evidence"] for entry in fast_lane), len(fast_lane)),
        },
        "risk_summary": {
            "high_over_request_risk_count": sum(entry["reviewer_fields"]["over_request_risk"] == "high" for entry in entries),
            "medium_over_request_risk_count": sum(entry["reviewer_fields"]["over_request_risk"] == "medium" for entry in entries),
            "high_under_request_risk_count": sum(entry["reviewer_fields"]["under_request_risk"] == "high" for entry in entries),
            "medium_under_request_risk_count": sum(entry["reviewer_fields"]["under_request_risk"] == "medium" for entry in entries),
            "raw_evidence_leakage_incidents": sum(
                entry["reviewer_fields"]["raw_evidence_excluded_from_git"] is not True for entry in entries
            ),
        },
    }


def validate_entries(entries: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for entry in entries:
        wid = entry.get("workbench_id", "<missing>")
        if wid in seen:
            errors.append(f"{wid}: duplicate workbench_id")
        seen.add(wid)
        metadata = entry.get("reviewer_visible_metadata")
        if not isinstance(metadata, dict):
            errors.append(f"{wid}: reviewer_visible_metadata must be a mapping")
            continue
        fields = entry.get("reviewer_fields")
        if not isinstance(fields, dict):
            errors.append(f"{wid}: reviewer_fields must be a mapping")
            continue
        for key in REQUIRED_REVIEWER_FIELDS:
            if key not in fields:
                errors.append(f"{wid}: missing reviewer field {key}")
            elif fields[key] is None:
                errors.append(f"{wid}: reviewer field {key} is blank")
        if fields.get("human_context_gate_decision") not in DECISIONS:
            errors.append(f"{wid}: invalid human_context_gate_decision")
        if fields.get("metadata_only_label_or_not_reviewable") not in LABELS:
            errors.append(f"{wid}: invalid metadata_only_label_or_not_reviewable")
        if fields.get("context_gate_omission_risk") not in RISK:
            errors.append(f"{wid}: invalid context_gate_omission_risk")
        if fields.get("over_request_risk") not in RISK:
            errors.append(f"{wid}: invalid over_request_risk")
        if fields.get("under_request_risk") not in RISK:
            errors.append(f"{wid}: invalid under_request_risk")
        if fields.get("context_gate_status") not in CONTEXT_GATE_STATUS:
            errors.append(f"{wid}: invalid context_gate_status")
        if fields.get("minimal_context_request_status") not in MINIMAL_CONTEXT_STATUS:
            errors.append(f"{wid}: invalid minimal_context_request_status")
        if not isinstance(fields.get("context_gate_review_time_seconds"), (int, float)):
            errors.append(f"{wid}: context_gate_review_time_seconds must be numeric")
        if fields.get("raw_evidence_excluded_from_git") is not True:
            errors.append(f"{wid}: raw_evidence_excluded_from_git must be true")
    return errors


def compare_summary(expected: Any, actual: Any, path: str = "") -> list[str]:
    errors: list[str] = []
    if isinstance(actual, dict):
        if not isinstance(expected, dict):
            return [f"{path or 'summary'}: expected mapping, found {type(expected).__name__}"]
        for key, actual_value in actual.items():
            next_path = f"{path}.{key}" if path else key
            errors.extend(compare_summary(expected.get(key), actual_value, next_path))
    elif isinstance(actual, float):
        if not isinstance(expected, (int, float)) or not math.isclose(float(expected), actual, rel_tol=1e-6, abs_tol=1e-6):
            errors.append(f"{path}: expected {actual}, found {expected}")
    else:
        if expected != actual:
            errors.append(f"{path}: expected {actual!r}, found {expected!r}")
    return errors


def packet_alignment_warnings(result: dict[str, Any], packet: dict[str, Any]) -> list[str]:
    packet_entries = {entry.get("workbench_id"): entry for entry in packet.get("candidate_entries", [])}
    warnings: list[str] = []
    for entry in result.get("candidate_entries", []):
        wid = entry.get("workbench_id")
        packet_entry = packet_entries.get(wid)
        if not packet_entry:
            warnings.append(f"{wid}: not found in source packet")
            continue
        result_metadata = entry.get("reviewer_visible_metadata", {})
        packet_metadata = packet_entry.get("reviewer_visible_metadata", {})
        for key in ("source_candidate_id", "source_stub_id", "task_id", "routing_lane", "slice_role", "signal_hint", "expected_behavior"):
            if result_metadata.get(key) != packet_metadata.get(key):
                warnings.append(f"{wid}: metadata mismatch for {key}: result={result_metadata.get(key)!r} packet={packet_metadata.get(key)!r}")
        result_outputs = entry.get("revised_assist_outputs", {})
        packet_outputs = packet_entry.get("revised_assist_outputs", {})
        for key in (
            "context_dependency_gate",
            "context_reason_codes",
            "minimal_context_needed",
            "safe_next_action",
            "metadata_label_guardrail",
            "priority_explanation",
            "missing_evidence_note",
            "second_review_suggestion",
        ):
            if result_outputs.get(key) != packet_outputs.get(key):
                warnings.append(
                    f"{wid}: revised_assist_outputs mismatch for {key}: "
                    f"result={result_outputs.get(key)!r} packet={packet_outputs.get(key)!r}"
                )
    return warnings


def forbidden_key_errors(value: Any, path: str = "") -> list[str]:
    errors: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            key_text = str(key)
            child_path = f"{path}.{key_text}" if path else key_text
            if key_text.lower() in FORBIDDEN_KEYS:
                errors.append(f"forbidden key {child_path}")
            errors.extend(forbidden_key_errors(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            errors.extend(forbidden_key_errors(child, f"{path}[{index}]"))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--result", type=Path, default=DEFAULT_RESULT)
    parser.add_argument("--packet", type=Path, default=DEFAULT_PACKET)
    parser.add_argument("--strict-packet", action="store_true", help="Fail if result metadata differs from source packet")
    args = parser.parse_args()

    result = load_yaml(args.result)
    packet = load_yaml(args.packet)
    if not isinstance(result, dict):
        print(f"error: {args.result} must contain a YAML object", file=sys.stderr)
        return 1
    if not isinstance(packet, dict):
        print(f"error: {args.packet} must contain a YAML object", file=sys.stderr)
        return 1

    entries = result.get("candidate_entries", [])
    if not isinstance(entries, list):
        print("error: candidate_entries must be a list", file=sys.stderr)
        return 1

    computed = compute_summary(entries)
    errors = []
    errors.extend(validate_entries(entries))
    errors.extend(forbidden_key_errors(result))
    errors.extend(compare_summary(result.get("aggregate_context_gate_summary"), computed))
    warnings = packet_alignment_warnings(result, packet)

    print(f"checked_entries: {len(entries)}")
    print(f"errors: {len(errors)}")
    print(f"packet_alignment_warnings: {len(warnings)}")
    print(f"reviewed_count: {computed['reviewed_count']}")
    print(f"average_context_gate_review_time_seconds: {computed['average_context_gate_review_time_seconds']}")
    print(f"target_correct_thread_before_label_rate: {computed['target_thread_required']['correct_thread_before_label_rate']}")
    print(f"raw_evidence_leakage_incidents: {computed['risk_summary']['raw_evidence_leakage_incidents']}")
    for error in errors:
        print(f"ERROR: {error}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        return 1
    if args.strict_packet and warnings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
