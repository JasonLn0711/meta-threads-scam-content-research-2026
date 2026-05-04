"""Generate safe exploration tasks and candidate stubs.

The exploration layer proposes where to look next. It does not collect external
content, store raw evidence, or make candidate decisions.
"""

from __future__ import annotations

from typing import Any


SIGNAL_HINTS: dict[str, dict[str, Any]] = {
    "保證收益": {
        "source_hint": "value-claim candidate surface",
        "search_cues": ["guarantee-or-certainty cue", "low-friction value promise", "funnel-adjacent evidence"],
        "expected_behavior": "guarantee_or_certainty_anchor",
    },
    "成果展示": {
        "source_hint": "result-display candidate surface",
        "search_cues": ["result display cue", "testimonial or proof-of-outcome structure", "funnel-adjacent evidence"],
        "expected_behavior": "result_display_anchor",
    },
    "review_stable_funnel_anchor": {
        "source_hint": "low-burden funnel/value anchor",
        "search_cues": ["funnel-stage anchor", "value-stage anchor", "no second-review trigger"],
        "expected_behavior": "review_stable_funnel_or_value_anchor",
    },
    "reply_funnel": {
        "source_hint": "reply/comment funnel",
        "search_cues": ["reply involvement", "contact transition cue", "thread-mediated funnel"],
        "expected_behavior": "reply_level_contact_or_group_transition",
    },
    "社群導流": {
        "source_hint": "group/community transition",
        "search_cues": ["community movement cue", "group invitation structure", "audience migration cue"],
        "expected_behavior": "community_funnel_transition",
    },
    "誘導聯絡": {
        "source_hint": "contact-transition surface",
        "search_cues": ["contact cue", "structured contact transition", "manual-assisted verification cue"],
        "expected_behavior": "contact_transition",
    },
    "needs_thread": {
        "source_hint": "thread-context dependency",
        "search_cues": ["context-dependent cue", "reply required to interpret", "high review burden warning"],
        "expected_behavior": "thread_context_dependency",
    },
    "情緒操控": {
        "source_hint": "pressure or reassurance surface",
        "search_cues": ["urgency cue", "fear or reassurance cue", "scarcity or pressure structure"],
        "expected_behavior": "emotional_pressure_or_reassurance",
    },
}


def generate_exploration_plan(
    ranking: dict[str, Any],
    discrepancy: dict[str, Any],
    embedding: dict[str, Any],
    stubs_per_task: int = 5,
) -> tuple[dict[str, Any], dict[str, Any]]:
    tasks: list[dict[str, Any]] = []
    tasks.extend(_discrepancy_tasks(discrepancy))
    tasks.extend(_low_coverage_signal_tasks(ranking))
    tasks.extend(_embedding_outlier_tasks(embedding))

    ranked_tasks = _rank_tasks(tasks)
    for index, task in enumerate(ranked_tasks, 1):
        task["task_id"] = f"EXP_{index:04d}"

    stubs = _candidate_stubs(ranked_tasks, stubs_per_task=stubs_per_task)

    task_output = {
        "schema_version": "exploration_tasks_v1",
        "purpose": "propose where to look next to maximize high-value candidate discovery per unit reviewer effort",
        "source_inputs": [
            "metrics/signal_scores/latest_ranking.yaml",
            "outputs/discrepancy_reports/latest.yaml",
            "outputs/embedding_clusters/latest.yaml",
        ],
        "policy": {
            "external_access_allowed": False,
            "raw_threads_evidence_storage_allowed": False,
            "pii_allowed": False,
            "collection_mode": "safe_manual_assisted_only",
            "max_stubs_per_task": stubs_per_task,
        },
        "summary": {
            "task_count": len(ranked_tasks),
            "high_discrepancy_task_count": sum(1 for task in ranked_tasks if task["gap_type"] == "high_discrepancy"),
            "low_coverage_task_count": sum(1 for task in ranked_tasks if task["gap_type"] == "low_coverage_high_potential"),
            "embedding_outlier_task_count": sum(1 for task in ranked_tasks if task["gap_type"] == "embedding_outlier"),
        },
        "tasks": ranked_tasks,
        "guardrails": {
            "external_systems_accessed": False,
            "raw_threads_content_included": False,
            "pii_included": False,
            "embedding_used_for_decision": False,
            "tasks_are_collection_suggestions_only": True,
        },
    }

    stub_output = {
        "schema_version": "candidate_stubs_v1",
        "purpose": "metadata-only candidate stubs for safe manual-assisted exploration",
        "source_tasks": "exploration/tasks/latest.yaml",
        "summary": {
            "stub_count": len(stubs),
            "task_count": len(ranked_tasks),
        },
        "candidate_stubs": stubs,
        "guardrails": {
            "external_systems_accessed": False,
            "raw_threads_content_included": False,
            "pii_included": False,
            "collection_method_limited_to_safe_manual_assisted": True,
        },
    }
    return task_output, stub_output


def _discrepancy_tasks(discrepancy: dict[str, Any]) -> list[dict[str, Any]]:
    tasks = []
    for case in discrepancy.get("cases", []):
        case_type = str(case.get("type") or "")
        candidate_ids = [str(item) for item in case.get("candidate_ids", [])]
        if case_type not in {"missed_pattern", "over_generalization"}:
            continue
        priority = "high" if case_type == "missed_pattern" else "medium"
        tasks.append(
            {
                "task_id": "PENDING",
                "gap_type": "high_discrepancy",
                "hypothesis": f"{case_type} case suggests current sparse representation is missing or over-broad for a reusable behavior pattern.",
                "source_hint": "discrepancy follow-up",
                "search_cues": ["case-linked metadata pattern", "shared behavior unit", "manual-assisted comparison"],
                "priority": priority,
                "reason": [
                    f"discrepancy case {case.get('case_id')}",
                    f"case type: {case_type}",
                    f"candidate count: {len(candidate_ids)}",
                ],
                "expected_impact": {
                    "clustering": "reduce active discrepancy if a stable behavior feature is confirmed",
                    "reviewer_effort": "focus review on pattern confirmation rather than broad search",
                },
                "rank": {
                    "gap_score": 3.0 if priority == "high" else 2.0,
                    "coverage_score": len(candidate_ids),
                    "impact_score": 3.0,
                },
            }
        )
    return tasks


def _low_coverage_signal_tasks(ranking: dict[str, Any]) -> list[dict[str, Any]]:
    tasks = []
    for signal in ranking.get("ranked_signals", []):
        reviewed_count = int(signal.get("reviewed_count") or 0)
        yield_rate = float(signal.get("yield_rate") or 0.0)
        svs = float(signal.get("svs") or 0.0)
        if reviewed_count == 0 or reviewed_count > 2 or yield_rate < 0.5 or svs <= 0:
            continue
        signal_id = str(signal.get("signal_id") or "")
        hint = SIGNAL_HINTS.get(signal_id, {})
        priority = "high" if reviewed_count == 1 and yield_rate >= 1.0 else "medium"
        tasks.append(
            {
                "task_id": "PENDING",
                "gap_type": "low_coverage_high_potential",
                "hypothesis": f"`{signal_id}` has high early yield but too little coverage; a small manual-assisted batch can test whether it scales without increasing reviewer burden.",
                "source_hint": hint.get("source_hint", f"{signal_id} candidate surface"),
                "search_cues": hint.get("search_cues", [f"{signal_id} metadata cue", "behavior-level match", "manual-assisted verification"]),
                "priority": priority,
                "reason": [
                    f"reviewed_count={reviewed_count}",
                    f"yield_rate={yield_rate}",
                    f"svs={svs}",
                    "low coverage with high potential",
                ],
                "signal_hint": signal_id,
                "expected_behavior": hint.get("expected_behavior", f"{signal_id}_behavior"),
                "expected_impact": {
                    "clustering": "test whether the signal forms a stable sparse cluster across more candidates",
                    "reviewer_effort": "measure whether high-yield signal remains low-burden in a small batch",
                },
                "rank": {
                    "gap_score": 2.5,
                    "coverage_score": max(0, 3 - reviewed_count),
                    "impact_score": 3.0 if yield_rate >= 1.0 else 2.0,
                },
            }
        )
    return tasks


def _embedding_outlier_tasks(embedding: dict[str, Any]) -> list[dict[str, Any]]:
    tasks = []
    nearest_by_id = {
        str(row.get("candidate_id")): row.get("neighbors", []) for row in embedding.get("nearest_neighbors", [])
    }
    for cluster in embedding.get("clusters", []):
        candidate_ids = [str(item) for item in cluster.get("candidate_ids", [])]
        if len(candidate_ids) != 1:
            continue
        candidate = candidate_ids[0]
        max_similarity = max((float(row.get("cosine_similarity") or 0.0) for row in nearest_by_id.get(candidate, [])), default=0.0)
        if max_similarity > 0.25:
            continue
        tasks.append(
            {
                "task_id": "PENDING",
                "gap_type": "embedding_outlier",
                "hypothesis": "A singleton discovery-only embedding cluster may indicate an underrepresented behavior family or a hard-negative boundary that sparse features should learn to describe.",
                "source_hint": "embedding singleton follow-up",
                "search_cues": ["outlier-like metadata shape", "hard-negative contrast", "manual-assisted sparse annotation"],
                "priority": "medium",
                "reason": [
                    f"singleton embedding cluster candidate={candidate}",
                    f"max_neighbor_similarity={round(max_similarity, 6)}",
                    "embedding outlier used only as exploration cue",
                ],
                "signal_hint": "embedding_singleton_outlier",
                "expected_behavior": "underrepresented_or_boundary_behavior",
                "expected_impact": {
                    "clustering": "test whether the singleton is a new sparse family or a safe negative boundary",
                    "reviewer_effort": "avoid broad search by collecting only a tiny contrast set",
                },
                "rank": {
                    "gap_score": 2.0,
                    "coverage_score": 1,
                    "impact_score": 1.5,
                },
            }
        )

    skipped = [str(item) for item in embedding.get("skipped_missing_embedding", [])]
    if skipped:
        tasks.append(
            {
                "task_id": "PENDING",
                "gap_type": "embedding_outlier",
                "hypothesis": "Candidates missing vectors may represent evidence-shape gaps; a small manual-assisted check can decide whether vector absence is harmless metadata sparsity or an exploration blind spot.",
                "source_hint": "missing embedding coverage check",
                "search_cues": ["missing vector metadata", "non-embedded candidate shape", "safe manual-assisted completeness check"],
                "priority": "low",
                "reason": [
                    f"missing_embedding_count={len(skipped)}",
                    "embedding absence is not a decision signal",
                ],
                "signal_hint": "missing_embedding_metadata_gap",
                "expected_behavior": "metadata_completeness_gap",
                "expected_impact": {
                    "clustering": "improve future outlier detection coverage if vector absence is systematic",
                    "reviewer_effort": "prevent wasting review time on incomplete metadata paths",
                },
                "rank": {
                    "gap_score": 1.0,
                    "coverage_score": len(skipped),
                    "impact_score": 1.0,
                },
            }
        )
    return tasks


def _rank_tasks(tasks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    priority_weight = {"high": 3, "medium": 2, "low": 1}
    return sorted(
        tasks,
        key=lambda task: (
            -priority_weight.get(str(task.get("priority")), 0),
            -float(task.get("rank", {}).get("gap_score", 0)),
            -float(task.get("rank", {}).get("impact_score", 0)),
            -float(task.get("rank", {}).get("coverage_score", 0)),
            str(task.get("source_hint")),
        ),
    )


def _candidate_stubs(tasks: list[dict[str, Any]], stubs_per_task: int) -> list[dict[str, Any]]:
    stubs = []
    for task in tasks:
        for index in range(1, stubs_per_task + 1):
            stubs.append(
                {
                    "candidate_stub_id": f"STUB_{len(stubs) + 1:04d}",
                    "task_id": task["task_id"],
                    "signal_hint": task.get("signal_hint", task.get("gap_type", "exploration_gap")),
                    "expected_behavior": task.get("expected_behavior", "behavior_pattern_to_verify"),
                    "collection_method": "safe / manual-assisted",
                    "raw_threads_evidence_allowed": False,
                    "pii_allowed": False,
                }
            )
    return stubs
