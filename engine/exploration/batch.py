"""Build small metadata-only exploration batches from generated tasks."""

from __future__ import annotations

from typing import Any


def build_exploration_batch(
    tasks_payload: dict[str, Any],
    stubs_payload: dict[str, Any],
    batch_id: str,
    selected_task_ids: list[str],
) -> tuple[dict[str, Any], dict[str, Any]]:
    tasks_by_id = {str(task.get("task_id")): task for task in tasks_payload.get("tasks", [])}
    stubs = [
        stub
        for stub in stubs_payload.get("candidate_stubs", [])
        if str(stub.get("task_id")) in selected_task_ids
    ]
    selected_tasks = [tasks_by_id[task_id] for task_id in selected_task_ids if task_id in tasks_by_id]

    batch = {
        "schema_version": "exploration_batch_v1",
        "batch_id": batch_id,
        "purpose": "small manual-assisted exploration batch for low-coverage high-SVS signals",
        "selected_task_ids": selected_task_ids,
        "selected_tasks": selected_tasks,
        "candidate_stub_count": len(stubs),
        "candidate_stub_ids": [str(stub.get("candidate_stub_id")) for stub in stubs],
        "before_metrics": {
            "discrepancy_case_count": 0,
            "target_signals": {
                "成果展示": {
                    "reviewed_count": 1,
                    "yield_rate": 1.0,
                    "svs": 0.0068438,
                },
                "保證收益": {
                    "reviewed_count": 1,
                    "yield_rate": 1.0,
                    "svs": 0.0068438,
                },
            },
        },
        "success_checks": [
            "Target signal SVS remains high or changes in an explainable way after new metadata is reviewed.",
            "`review_stable_funnel_anchor` remains useful or produces a clear failure mode.",
            "New missed-pattern discrepancies, if any, produce feature hypotheses rather than schema changes.",
            "Reviewer effort stays bounded: 10 stubs maximum for this batch.",
        ],
        "stop_rules": [
            "Stop if any step would require raw Threads content in git.",
            "Stop if any step would require PII, handles, raw URLs, screenshots, browser exports, credentials, or controlled-store paths.",
            "Stop if manual-assisted review cannot keep evidence metadata-only.",
            "Stop if reviewer burden exceeds the planned 10-stub batch.",
        ],
        "guardrails": {
            "external_systems_accessed": False,
            "raw_threads_content_included": False,
            "pii_included": False,
            "embedding_used_for_decision": False,
            "collection_method": "safe / manual-assisted",
            "this_file_authorizes_collection": False,
        },
    }

    stub_batch = {
        "schema_version": "candidate_stub_batch_v1",
        "batch_id": batch_id,
        "source_tasks": "exploration/tasks/latest.yaml",
        "source_stubs": "data/candidate_stubs/latest.yaml",
        "selected_task_ids": selected_task_ids,
        "summary": {
            "stub_count": len(stubs),
            "target_signal_hints": sorted({str(stub.get("signal_hint")) for stub in stubs}),
        },
        "candidate_stubs": stubs,
        "guardrails": {
            "external_systems_accessed": False,
            "raw_threads_content_included": False,
            "pii_included": False,
            "collection_method_limited_to_safe_manual_assisted": True,
        },
    }
    return batch, stub_batch
