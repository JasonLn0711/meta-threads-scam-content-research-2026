"""Contrast-aware reviewer routing over sparse metadata features."""

from __future__ import annotations

from statistics import mean
from typing import Any

from engine.common import (
    active_sparse_features,
    batch_id,
    candidate_id,
    review_decision,
    second_review_required,
    sparse_feature_value,
)
from engine.sparse.svs import score_candidate_group


LANE_ORDER = [
    "strong_source_priority",
    "guarantee_context_review",
    "result_display_low_context_transition",
    "result_display_thread_required",
    "result_display_emotional_thread_required",
    "result_display_context_review",
    "result_display_contrast_holdout",
    "other_metadata_review",
]

LANE_DEFINITIONS = {
    "strong_source_priority": {
        "pre_review_activation_rule": "保證收益 AND (誘導聯絡 OR 社群導流 OR reply_funnel OR review_stable_funnel_anchor) AND NOT needs_thread",
        "routing_action": "fast_priority_review",
        "context_gate": "single_item_review",
        "interpretation": "High-value source arm when a guarantee/certainty anchor has executable transition structure and low thread burden.",
    },
    "guarantee_context_review": {
        "pre_review_activation_rule": "保證收益 AND NOT strong_source_priority",
        "routing_action": "priority_context_review",
        "context_gate": "thread_or_second_review_as_needed",
        "interpretation": "Guarantee/certainty anchor remains important, but needs slower review when transition structure is weak or context burden is high.",
    },
    "result_display_low_context_transition": {
        "pre_review_activation_rule": "成果展示 AND NOT 保證收益 AND NOT needs_thread AND (誘導聯絡 OR 社群導流 OR reply_funnel OR review_stable_funnel_anchor)",
        "routing_action": "low_context_transition_review",
        "context_gate": "single_item_review",
        "interpretation": "Result display with visible transition structure can be reviewed without full-thread context, but remains uncertain without explicit guarantee.",
    },
    "result_display_thread_required": {
        "pre_review_activation_rule": "成果展示 AND NOT 保證收益 AND needs_thread AND NOT 情緒操控",
        "routing_action": "thread_context_review",
        "context_gate": "thread_required",
        "interpretation": "Result display that requires thread context should be routed to slower review before a decision is attempted.",
    },
    "result_display_emotional_thread_required": {
        "pre_review_activation_rule": "成果展示 AND NOT 保證收益 AND needs_thread AND 情緒操控",
        "routing_action": "thread_context_second_review",
        "context_gate": "thread_required_plus_second_review",
        "interpretation": "Result display with emotional pressure and thread dependency is a high cognitive-load review path, not a fast positive-yield signal.",
    },
    "result_display_context_review": {
        "pre_review_activation_rule": "成果展示 AND NOT 保證收益 AND context cues that do not match the explicit Batch 0007 sub-lanes",
        "routing_action": "slow_context_review",
        "context_gate": "manual_context_triage",
        "interpretation": "Fallback for result-display context cases that do not yet fit a stable sub-lane.",
    },
    "result_display_contrast_holdout": {
        "pre_review_activation_rule": "成果展示 AND NOT 保證收益 AND NOT (誘導聯絡 OR 社群導流 OR reply_funnel OR needs_thread OR 情緒操控)",
        "routing_action": "contrast_or_hard_negative_pool",
        "context_gate": "holdout_calibration",
        "interpretation": "Standalone result display is useful for hard-negative contrast and boundary calibration.",
    },
    "other_metadata_review": {
        "pre_review_activation_rule": "candidate does not match the defined contrast lanes",
        "routing_action": "standard_review",
        "context_gate": "standard_review",
        "interpretation": "Keep in standard metadata review until a useful contrast pattern is observed.",
    },
}


def assign_contrast_lane(candidate: dict[str, Any]) -> str:
    """Assign a candidate to one sparse-feature routing lane.

    The lane is not a label. It is a reviewer-effort routing hypothesis based on
    structured metadata only.
    """

    guarantee = bool(sparse_feature_value(candidate, "保證收益"))
    result_display = bool(sparse_feature_value(candidate, "成果展示"))
    needs_thread = bool(sparse_feature_value(candidate, "needs_thread"))
    executable_transition = any(
        sparse_feature_value(candidate, feature)
        for feature in ("誘導聯絡", "社群導流", "reply_funnel", "review_stable_funnel_anchor")
    )
    context_cue = any(
        sparse_feature_value(candidate, feature)
        for feature in ("誘導聯絡", "社群導流", "reply_funnel", "needs_thread", "情緒操控")
    )

    if guarantee and executable_transition and not needs_thread:
        return "strong_source_priority"
    if guarantee:
        return "guarantee_context_review"
    if result_display:
        if not needs_thread and executable_transition:
            return "result_display_low_context_transition"
        if needs_thread and sparse_feature_value(candidate, "情緒操控"):
            return "result_display_emotional_thread_required"
        if needs_thread:
            return "result_display_thread_required"
        if context_cue:
            return "result_display_context_review"
        return "result_display_contrast_holdout"
    return "other_metadata_review"


def build_contrast_aware_scores(
    candidates: list[dict[str, Any]],
    sparse_schema: dict[str, Any],
) -> dict[str, Any]:
    lane_groups = {lane: [] for lane in LANE_ORDER}
    candidate_routes = []

    for candidate in candidates:
        lane = assign_contrast_lane(candidate)
        lane_groups.setdefault(lane, []).append(candidate)
        candidate_routes.append(
            {
                "candidate_id": candidate_id(candidate),
                "batch_id": batch_id(candidate),
                "lane": lane,
                "routing_action": LANE_DEFINITIONS[lane]["routing_action"],
                "context_gate": LANE_DEFINITIONS[lane]["context_gate"],
                "active_sparse_features": active_sparse_features(candidate),
                "review_decision": review_decision(candidate),
                "second_review_required": second_review_required(candidate),
                "guardrail": "structured_metadata_only",
            }
        )

    lane_scores = [_lane_score(lane, lane_groups.get(lane, []), sparse_schema) for lane in LANE_ORDER]
    return {
        "schema_version": "contrast_aware_scores_v1",
        "decision_layer": "sparse_primary_reviewer_routing",
        "purpose": "route reviewed sparse metadata patterns by expected value per reviewer effort",
        "not_a_classifier": True,
        "formula": "lane SVS uses (yield_rate * information_density) / (review_time * cognitive_load); lane routing is a testable reviewer-effort hypothesis",
        "positive_yield_definition": "human research label scam, not legal fraud",
        "candidate_count": len(candidates),
        "lane_definitions": LANE_DEFINITIONS,
        "lane_scores": lane_scores,
        "candidate_routes": candidate_routes,
        "recommendations": _recommendations(lane_scores),
        "guardrails": {
            "raw_threads_content_included": False,
            "pii_included": False,
            "embedding_used_for_decision": False,
            "sparse_schema_updated": False,
            "human_review_required": True,
            "legal_or_enforcement_decision_made": False,
        },
    }


def _lane_score(
    lane: str,
    candidates: list[dict[str, Any]],
    sparse_schema: dict[str, Any],
) -> dict[str, Any]:
    score = score_candidate_group(candidates, sparse_schema)
    reviewed_count = len(candidates)
    uncertain_count = sum(1 for candidate in candidates if review_decision(candidate) == "uncertain")
    non_scam_count = sum(1 for candidate in candidates if review_decision(candidate) == "non_scam")
    needs_thread_count = sum(1 for candidate in candidates if sparse_feature_value(candidate, "needs_thread"))
    second_review_count = sum(1 for candidate in candidates if second_review_required(candidate))
    confidence_values = [
        float(candidate.get("review", {}).get("confidence"))
        for candidate in candidates
        if isinstance(candidate.get("review", {}).get("confidence"), (int, float))
    ]

    return {
        "lane": lane,
        "routing_action": LANE_DEFINITIONS[lane]["routing_action"],
        "candidate_ids": [candidate_id(candidate) for candidate in candidates],
        **score,
        "non_scam_count": non_scam_count,
        "uncertain_count": uncertain_count,
        "needs_thread_rate": _rate(needs_thread_count, reviewed_count),
        "second_review_rate": _rate(second_review_count, reviewed_count),
        "uncertainty_rate": _rate(uncertain_count, reviewed_count),
        "average_confidence": round(mean(confidence_values), 6) if confidence_values else 0.0,
        "interpretation": LANE_DEFINITIONS[lane]["interpretation"],
    }


def _rate(count: int, total: int) -> float:
    if not total:
        return 0.0
    return round(count / total, 6)


def _recommendations(lane_scores: list[dict[str, Any]]) -> list[str]:
    by_lane = {row["lane"]: row for row in lane_scores}
    strong = by_lane.get("strong_source_priority", {})
    result_low_context = by_lane.get("result_display_low_context_transition", {})
    result_thread = by_lane.get("result_display_thread_required", {})
    result_emotional_thread = by_lane.get("result_display_emotional_thread_required", {})
    holdout = by_lane.get("result_display_contrast_holdout", {})
    recommendations = []

    if float(strong.get("svs") or 0.0) > float(result_low_context.get("svs") or 0.0):
        recommendations.append(
            "Prioritize strong_source_priority candidates when reviewer capacity is constrained."
        )
    if int(result_low_context.get("reviewed_count") or 0) and float(
        result_low_context.get("needs_thread_rate") or 0.0
    ) == 0.0:
        recommendations.append(
            "Route result_display_low_context_transition to single-item review; do not require full thread by default."
        )
    if float(result_thread.get("needs_thread_rate") or 0.0) >= 0.5:
        recommendations.append(
            "Route result_display_thread_required to full-thread context review before decision."
        )
    if float(result_emotional_thread.get("second_review_rate") or 0.0) >= 0.5:
        recommendations.append(
            "Route result_display_emotional_thread_required to full-thread plus second-review queue when capacity allows."
        )
    if int(holdout.get("reviewed_count") or 0):
        recommendations.append(
            "Keep result_display_contrast_holdout candidates as hard-negative or boundary calibration material."
        )
    if not recommendations:
        recommendations.append("Keep collecting small contrast batches before changing routing policy.")
    return recommendations
