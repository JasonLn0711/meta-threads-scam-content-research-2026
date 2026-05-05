#!/usr/bin/env python3
"""Build a reviewer-facing Batch 0012 context-gate packet.

The script intentionally reads the reviewer fill template, not the controller
work order, so prior Batch 0011 labels and timings cannot leak into the packet.
It fills only revised assist outputs. Human reviewer fields remain blank.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from engine.common import load_yaml, write_yaml


DEFAULT_TEMPLATE = REPO_ROOT / "data" / "reviewer_assist_eval" / "batch_0012_reviewer_fill_sheet_template.yaml"
DEFAULT_OUTPUT = REPO_ROOT / "data" / "reviewer_assist_eval" / "batch_0012_reviewer_context_gate_packet.yaml"

REQUIRED_ASSIST_FIELDS = (
    "context_dependency_gate",
    "context_reason_codes",
    "minimal_context_needed",
    "safe_next_action",
    "metadata_label_guardrail",
    "priority_explanation",
    "missing_evidence_note",
    "second_review_suggestion",
)

REVIEWER_FIELD_KEYS = (
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

FORBIDDEN_EXPOSED_KEYS = {
    "prior_assisted_outcome_hidden",
    "prior_assisted_outcome",
    "prior_assisted_label",
    "prior_assisted_review_time_seconds",
    "manual_baseline",
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
}


def behavior_reason(expected_behavior: str) -> str:
    if "contact" in expected_behavior:
        return "contact_path_context_dependency"
    if "group" in expected_behavior:
        return "group_transition_context_dependency"
    if "reply" in expected_behavior:
        return "reply_funnel_context_dependency"
    if "stable_anchor" in expected_behavior:
        return "stable_anchor_boundary_check"
    if "ambiguous" in expected_behavior:
        return "ambiguous_transition_context_dependency"
    return "metadata_context_boundary_check"


def target_missing_note(expected_behavior: str) -> str:
    if "reply" in expected_behavior:
        return "reply_path_requires_thread_context"
    if "ambiguous" in expected_behavior:
        return "ambiguous_transition_cannot_be_resolved_from_structured_metadata_only"
    return "thread_dependency_blocks_confident_metadata_only_label"


def boundary_profile(expected_behavior: str) -> dict[str, str]:
    if "reply" in expected_behavior:
        return {
            "reason": "reply_funnel_without_guarantee",
            "risk_code": "hard_negative_boundary_protection",
            "guardrail": "do_not_escalate_result_display_to_scam_label",
            "priority": "boundary_control_for_over_request_check",
            "missing": "visible_transition_without_explicit_guarantee",
        }
    if "group" in expected_behavior:
        return {
            "reason": "group_cue_without_guarantee",
            "risk_code": "over_request_control",
            "guardrail": "protect_against_group_cue_overreach",
            "priority": "boundary_control_for_context_gate_specificity",
            "missing": "group_transition_hint_without_explicit_guarantee",
        }
    if "stable_anchor" in expected_behavior:
        return {
            "reason": "stable_anchor_without_guarantee",
            "risk_code": "over_request_control",
            "guardrail": "stable_anchor_is_not_enough_for_positive_label",
            "priority": "boundary_control_for_context_gate_specificity",
            "missing": "stable_anchor_without_contact_or_guarantee",
        }
    return {
        "reason": "contact_transition_without_guarantee",
        "risk_code": "hard_negative_boundary_protection",
        "guardrail": "do_not_request_thread_context_by_habit",
        "priority": "boundary_control_for_over_request_check",
        "missing": "no_explicit_guarantee_observed_in_metadata",
    }


def hard_negative_profile(expected_behavior: str) -> dict[str, str]:
    if "secondary" in expected_behavior:
        return {
            "reason": "false_positive_pressure_check",
            "guardrail": "result_display_alone_is_not_positive_signal",
            "priority": "hard_negative_control_for_context_gate_specificity",
        }
    return {
        "reason": "no_contact_group_reply_thread_or_emotional_pressure",
        "guardrail": "do_not_request_thread_context_by_habit",
        "priority": "hard_negative_control_for_over_request_check",
    }


def fast_lane_profile(expected_behavior: str) -> dict[str, str]:
    if "group" in expected_behavior:
        return {
            "reason": "guarantee_group_transition",
            "guardrail": "do_not_slow_fast_lane_without_specific_missing_context",
        }
    return {
        "reason": "guarantee_executable_transition",
        "guardrail": "no_thread_request_needed_when_guarantee_and_transition_are_metadata_sufficient",
    }


def build_assist_outputs(metadata: dict[str, Any]) -> dict[str, Any]:
    role = str(metadata.get("slice_role", ""))
    lane = str(metadata.get("routing_lane", ""))
    expected_behavior = str(metadata.get("expected_behavior", ""))
    reason = behavior_reason(expected_behavior)

    if role == "target_thread_required":
        return {
            "context_dependency_gate": "needs_thread_before_label",
            "context_reason_codes": [
                "result_display_thread_required_lane",
                reason,
                "metadata_only_label_overreach_risk",
            ],
            "minimal_context_needed": "thread_or_reply_context_required_outside_git_before_confident_label",
            "safe_next_action": "route_to_thread_context_review_before_label",
            "metadata_label_guardrail": "do_not_label_scam_or_non_scam_from_metadata_only",
            "priority_explanation": "target_lane_for_context_dependency_bottleneck",
            "missing_evidence_note": target_missing_note(expected_behavior),
            "second_review_suggestion": True,
        }

    if role == "boundary_control":
        profile = boundary_profile(expected_behavior)
        return {
            "context_dependency_gate": "needs_second_review_before_label",
            "context_reason_codes": [
                "result_display_low_context_transition",
                profile["reason"],
                profile["risk_code"],
            ],
            "minimal_context_needed": "no_thread_by_default; second_reviewer_may_check_metadata_boundary",
            "safe_next_action": "route_to_second_review_before_label",
            "metadata_label_guardrail": profile["guardrail"],
            "priority_explanation": profile["priority"],
            "missing_evidence_note": profile["missing"],
            "second_review_suggestion": True,
        }

    if role == "hard_negative_control":
        profile = hard_negative_profile(expected_behavior)
        return {
            "context_dependency_gate": "hard_negative_metadata_sufficient",
            "context_reason_codes": [
                "clean_result_display_holdout",
                profile["reason"],
                "hard_negative_boundary",
            ],
            "minimal_context_needed": "not_applicable",
            "safe_next_action": "preserve_hard_negative_metadata_decision",
            "metadata_label_guardrail": profile["guardrail"],
            "priority_explanation": profile["priority"],
            "missing_evidence_note": "no_missing_context_needed_for_clean_holdout_metadata",
            "second_review_suggestion": False,
        }

    if role == "fast_lane_control":
        profile = fast_lane_profile(expected_behavior)
        return {
            "context_dependency_gate": "metadata_sufficient_for_label",
            "context_reason_codes": [
                "strong_source_priority",
                profile["reason"],
                "no_thread_dependency",
            ],
            "minimal_context_needed": "not_applicable",
            "safe_next_action": "metadata_sufficient_fast_lane_label",
            "metadata_label_guardrail": profile["guardrail"],
            "priority_explanation": "fast_lane_control_for_slowdown_check",
            "missing_evidence_note": "no_missing_context_for_metadata_level_triage",
            "second_review_suggestion": False,
        }

    raise ValueError(f"Unsupported slice_role {role!r} for lane {lane!r}")


def blank_reviewer_fields(template_fields: dict[str, Any]) -> dict[str, Any]:
    fields = {key: template_fields.get(key) for key in REVIEWER_FIELD_KEYS}
    missing = [key for key in REVIEWER_FIELD_KEYS if key not in template_fields]
    if missing:
        raise ValueError(f"Reviewer field template is missing: {', '.join(missing)}")
    return fields


def build_packet(template: dict[str, Any]) -> dict[str, Any]:
    entries = []
    role_counts: Counter[str] = Counter()
    lane_counts: Counter[str] = Counter()

    for entry in template.get("candidate_entries", []):
        metadata = entry.get("reviewer_visible_metadata")
        if not isinstance(metadata, dict):
            raise ValueError(f"{entry.get('workbench_id')}: reviewer_visible_metadata must be a mapping")
        assist_outputs = build_assist_outputs(metadata)
        reviewer_fields = blank_reviewer_fields(entry.get("reviewer_fields", {}))
        role_counts[str(metadata.get("slice_role"))] += 1
        lane_counts[str(metadata.get("routing_lane"))] += 1
        entries.append(
            {
                "workbench_id": entry.get("workbench_id"),
                "reviewer_visible_metadata": metadata,
                "revised_assist_outputs": assist_outputs,
                "reviewer_fields": reviewer_fields,
            }
        )

    packet = {
        "schema_version": "reviewer_assist_context_gate_packet_v1",
        "evaluation_id": template.get("evaluation_id"),
        "decision_id": template.get("decision_id"),
        "source_rules": template.get("source_rules"),
        "source_reviewer_fill_template": str(DEFAULT_TEMPLATE.relative_to(REPO_ROOT)),
        "status": "ready_for_human_context_gate_review",
        "result_boundary": {
            "reviewer_facing_packet": True,
            "empirical_assisted_review_result": False,
            "reviewer_fields_prefilled": False,
            "prior_assisted_outcomes_exposed": False,
            "manual_baseline_exposed": False,
            "raw_threads_content_used": False,
            "raw_reply_text_used": False,
            "raw_ocr_text_used": False,
            "urls_handles_screenshots_browser_artifacts_used": False,
            "controlled_store_locators_used": False,
            "legal_fraud_or_enforcement_claim": False,
            "note": "PACKET ONLY - HUMAN REVIEWER FIELDS MUST BE FILLED SEPARATELY",
        },
        "reviewer_visibility": template.get("reviewer_visibility"),
        "rating_scale": template.get("rating_scale"),
        "candidate_entries": entries,
        "packet_quality_checks": {
            "candidate_count": len(entries),
            "slice_role_counts": dict(sorted(role_counts.items())),
            "routing_lane_counts": dict(sorted(lane_counts.items())),
            "all_revised_assist_outputs_filled": True,
            "reviewer_fields_blank": True,
            "prior_assisted_outcomes_hidden": True,
            "raw_evidence_excluded_from_packet": True,
        },
    }
    validate_packet(packet)
    return packet


def validate_packet(packet: dict[str, Any]) -> None:
    errors: list[str] = []
    entries = packet.get("candidate_entries")
    if not isinstance(entries, list) or len(entries) != 12:
        errors.append(f"candidate_entries must contain 12 entries, got {len(entries) if isinstance(entries, list) else 'non-list'}")

    for key_path, key, value in iter_keys(packet):
        if key in FORBIDDEN_EXPOSED_KEYS:
            errors.append(f"forbidden reviewer-facing key at {key_path}")
        if key == "reviewer_fields" and isinstance(value, dict):
            filled = [field for field, field_value in value.items() if field_value is not None]
            if filled:
                errors.append(f"{key_path} must remain blank, found filled fields: {', '.join(filled)}")
        if key == "revised_assist_outputs" and isinstance(value, dict):
            missing = [field for field in REQUIRED_ASSIST_FIELDS if not value.get(field) and value.get(field) is not False]
            if missing:
                errors.append(f"{key_path} missing assist fields: {', '.join(missing)}")

    if errors:
        raise ValueError("\n".join(errors))


def iter_keys(value: Any, path: str = ""):
    if isinstance(value, dict):
        for key, child in value.items():
            key_text = str(key)
            child_path = f"{path}.{key_text}" if path else key_text
            yield child_path, key_text, child
            yield from iter_keys(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from iter_keys(child, f"{path}[{index}]")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE, help="Reviewer fill template YAML")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Reviewer-facing packet output YAML")
    parser.add_argument("--check-only", action="store_true", help="Validate packet generation without writing output")
    args = parser.parse_args()

    template = load_yaml(args.template)
    if not isinstance(template, dict):
        print(f"error: {args.template} must contain a YAML object", file=sys.stderr)
        return 1

    try:
        packet = build_packet(template)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if not args.check_only:
        write_yaml(args.output, packet)
        print(f"wrote: {args.output.relative_to(REPO_ROOT)}")
    print(f"candidate_count: {len(packet['candidate_entries'])}")
    print(f"slice_role_counts: {packet['packet_quality_checks']['slice_role_counts']}")
    print("reviewer_fields_blank: true")
    print("prior_assisted_outcomes_exposed: false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
