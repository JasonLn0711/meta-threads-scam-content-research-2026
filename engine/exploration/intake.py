"""Build metadata-only intake worksheets for exploration batches."""

from __future__ import annotations

from typing import Any


SPARSE_FEATURES_V2 = [
    "誘導聯絡",
    "保證收益",
    "社群導流",
    "情緒操控",
    "成果展示",
    "reply_funnel",
    "needs_thread",
    "review_stable_funnel_anchor",
]


def build_candidate_intake(
    stub_batch: dict[str, Any],
    batch_plan: dict[str, Any],
) -> dict[str, Any]:
    batch_id = str(stub_batch.get("batch_id") or batch_plan.get("batch_id") or "")
    intake_entries = []

    for index, stub in enumerate(stub_batch.get("candidate_stubs", []), 1):
        signal_hint = str(stub.get("signal_hint") or "")
        intake_entries.append(
            {
                "intake_id": f"INTAKE_{index:04d}",
                "candidate_stub_id": str(stub.get("candidate_stub_id") or ""),
                "task_id": str(stub.get("task_id") or ""),
                "signal_hint": signal_hint,
                "expected_behavior": str(stub.get("expected_behavior") or ""),
                "fill_status": "pending_manual_review",
                "sparse_feature_observations": _feature_observations(signal_hint),
                "structured_hints_to_fill": {
                    "common_behaviors": [],
                    "structural_patterns": [],
                    "reviewer_signals": [],
                    "hard_negative_contrast": "pending",
                    "metadata_only_note": "Do not paste raw Threads text, URLs, handles, screenshots, identifiers, or controlled-store locators.",
                },
                "review_metadata_to_fill": {
                    "decision": "pending",
                    "confidence": "pending",
                    "review_time_seconds": "pending",
                    "second_review_required": "pending",
                },
                "candidate_record_output_target": f"data/candidates/batch_0004/{batch_id}_{index:04d}.yaml",
                "completion_gate": {
                    "raw_threads_content_excluded": "pending",
                    "pii_excluded": "pending",
                    "only_structured_metadata": "pending",
                    "human_review_completed": "pending",
                },
            }
        )

    return {
        "schema_version": "candidate_intake_batch_v1",
        "batch_id": batch_id,
        "purpose": "manual-assisted metadata fill worksheet for Batch 0004 candidate stubs",
        "source_batch_plan": "exploration/batches/batch_0004.yaml",
        "source_stub_batch": "data/candidate_stubs/batch_0004.yaml",
        "status": "pending_manual_assisted_fill",
        "candidate_count": len(intake_entries),
        "selected_task_ids": stub_batch.get("selected_task_ids", []),
        "target_signal_hints": stub_batch.get("summary", {}).get("target_signal_hints", []),
        "before_metrics": batch_plan.get("before_metrics", {}),
        "intake_entries": intake_entries,
        "completion_rules": [
            "Fill only structured metadata observations.",
            "Do not paste raw Threads content into this repo.",
            "Do not include PII, raw URLs, handles, screenshots, browser artifacts, credentials, or controlled-store locators.",
            "Do not infer final labels before human review.",
            "Convert to candidate_record_v2 only after completion gates are satisfied.",
        ],
        "after_fill_commands": [
            "./.venv/bin/python scripts/validate_candidate_v2.py data/candidates",
            "./.venv/bin/python scripts/run_v2_ros.py",
            "./.venv/bin/python scripts/generate_feature_candidates_v1.py",
            "./.venv/bin/python scripts/generate_exploration_tasks.py",
        ],
        "guardrails": {
            "external_systems_accessed": False,
            "raw_threads_content_included": False,
            "pii_included": False,
            "candidate_records_fabricated": False,
            "this_file_authorizes_collection": False,
        },
    }


def validate_candidate_intake(intake: dict[str, Any], expected_count: int | None = None) -> list[str]:
    errors: list[str] = []
    if intake.get("schema_version") != "candidate_intake_batch_v1":
        errors.append("schema_version must be candidate_intake_batch_v1")
    entries = intake.get("intake_entries", [])
    if not isinstance(entries, list):
        errors.append("intake_entries must be a list")
        return errors
    if expected_count is not None and len(entries) != expected_count:
        errors.append(f"expected {expected_count} intake entries, found {len(entries)}")
    for entry in entries:
        if entry.get("fill_status") not in {"pending_manual_review", "completed", "not_fillable"}:
            errors.append(f"{entry.get('intake_id')}: invalid fill_status")
        features = entry.get("sparse_feature_observations", {})
        missing = [name for name in SPARSE_FEATURES_V2 if name not in features]
        if missing:
            errors.append(f"{entry.get('intake_id')}: missing sparse feature observations {missing}")
    guardrails = intake.get("guardrails", {})
    if guardrails.get("candidate_records_fabricated") is not False:
        errors.append("guardrail candidate_records_fabricated must be false")
    if guardrails.get("this_file_authorizes_collection") is not False:
        errors.append("guardrail this_file_authorizes_collection must be false")
    return errors


def _feature_observations(signal_hint: str) -> dict[str, str]:
    observations = {feature: "pending" for feature in SPARSE_FEATURES_V2}
    if signal_hint in observations:
        observations[signal_hint] = "expected_from_stub"
    if signal_hint == "成果展示":
        observations["review_stable_funnel_anchor"] = "test_if_supported"
    if signal_hint == "保證收益":
        observations["review_stable_funnel_anchor"] = "test_if_supported"
    return observations
