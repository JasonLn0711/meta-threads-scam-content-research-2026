"""Stable adaptive policy for query selection and candidate prioritization."""

from __future__ import annotations

import hashlib
import json
from typing import Any

from src.evidence.storage import utc_now


VALID_DEPLOYMENT_MODES = ("shadow", "assist", "partial")

DEFAULT_WEIGHTS = {
    "expected_reward_prior": 0.2,
    "candidate_score": 0.24,
    "concept_confidence": 0.14,
    "predictive_risk": 0.12,
    "selfplay_reward": 0.12,
    "robustness": 0.1,
    "feedback_bonus": 0.08,
}


def default_policy_state(state: dict[str, Any] | None = None) -> dict[str, Any]:
    """Return a complete, conservative policy state."""
    state = dict(state or {})
    weights = dict(DEFAULT_WEIGHTS)
    weights.update({key: float(value) for key, value in state.get("weights", {}).items() if key in weights})
    weights = _normalize_weights(weights)
    return {
        "schema_version": "adaptive_policy_state_v1",
        "policy_version": int(state.get("policy_version", 1)),
        "deployment_mode": state.get("deployment_mode", "shadow"),
        "weights": weights,
        "max_policy_shift": float(state.get("max_policy_shift", 0.12)),
        "partial_candidate_threshold": float(state.get("partial_candidate_threshold", 0.72)),
        "query_limit": int(state.get("query_limit", 3)),
        "candidate_limit": int(state.get("candidate_limit", 5)),
        "training_examples": int(state.get("training_examples", 0)),
        "last_updated": state.get("last_updated", utc_now()),
        "raw_source_included": False,
    }


def policy(
    context: dict[str, Any],
    *,
    state: dict[str, Any] | None = None,
    mode: str | None = None,
) -> dict[str, Any]:
    """Return query-selection and candidate-prioritization actions."""
    policy_state = default_policy_state(state)
    deployment_mode = mode or str(policy_state.get("deployment_mode", "shadow"))
    if deployment_mode not in VALID_DEPLOYMENT_MODES:
        raise ValueError(f"unsupported deployment mode: {deployment_mode}")

    queries = [_score_query(query, policy_state) for query in context.get("queries", [])]
    candidates = [_score_candidate(candidate, policy_state) for candidate in context.get("candidates", [])]
    queries = sorted(queries, key=lambda row: (-float(row["priority_score"]), str(row.get("query_id", ""))))
    candidates = sorted(candidates, key=lambda row: (-float(row["priority_score"]), str(row.get("candidate_id", ""))))
    selected_queries = [_apply_query_mode(row, deployment_mode) for row in queries[: policy_state["query_limit"]]]
    candidate_priorities = [
        _apply_candidate_mode(row, deployment_mode, policy_state) for row in candidates[: policy_state["candidate_limit"]]
    ]
    feature_summary = _feature_summary(selected_queries, candidate_priorities)
    action = {
        "schema_version": "adaptive_policy_action_v1",
        "action_id": _action_id(context, deployment_mode, selected_queries, candidate_priorities),
        "created_at": utc_now(),
        "mode": deployment_mode,
        "deployment_effect": _deployment_effect(deployment_mode),
        "query_selection": selected_queries,
        "candidate_prioritization": candidate_priorities,
        "feature_summary": feature_summary,
        "guardrails": {
            "human_final_judgment_required": True,
            "no_external_collection": True,
            "no_enforcement_action": True,
            "raw_content_included": False,
            "max_policy_shift": policy_state["max_policy_shift"],
        },
        "policy_version": policy_state["policy_version"],
        "raw_source_included": False,
    }
    return action


def _score_query(query: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    weights = state["weights"]
    features = {
        "expected_reward_prior": _clamp(query.get("expected_reward_prior", query.get("reward", 0.0))),
        "predictive_risk": _clamp(query.get("predictive_risk_score", 0.0)),
        "selfplay_reward": _clamp(query.get("selfplay_reward_signal", 0.0)),
        "robustness": _clamp(query.get("robustness", query.get("exploration_priority", 0.0))),
        "feedback_bonus": _clamp(query.get("human_feedback_score", 0.0)),
    }
    score = (
        0.18
        + (weights["expected_reward_prior"] * features["expected_reward_prior"])
        + (weights["predictive_risk"] * features["predictive_risk"])
        + (weights["selfplay_reward"] * features["selfplay_reward"])
        + (weights["robustness"] * features["robustness"])
        + (weights["feedback_bonus"] * features["feedback_bonus"])
    )
    return {
        "query_id": query.get("query_id"),
        "query_string": query.get("query_string") or query.get("query"),
        "strategy": query.get("strategy"),
        "expected_signal": query.get("expected_signal"),
        "priority_score": round(_clamp(score), 6),
        "reason_codes": _query_reason_codes(features),
        "features": features,
        "raw_source_included": False,
    }


def _score_candidate(candidate: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    weights = state["weights"]
    features_in = candidate.get("features", {})
    features = {
        "candidate_score": _clamp(candidate.get("score", features_in.get("score", 0.0))),
        "concept_confidence": _clamp(features_in.get("concept_confidence", candidate.get("concept_confidence", 0.0))),
        "predictive_risk": _clamp(features_in.get("predictive_risk_score", candidate.get("predictive_risk_score", 0.0))),
        "selfplay_reward": _clamp(features_in.get("selfplay_reward_signal", candidate.get("selfplay_reward_signal", 0.0))),
        "robustness": _clamp(features_in.get("exploration_priority", candidate.get("robustness", 0.0))),
        "feedback_bonus": _clamp(candidate.get("human_feedback_score", 0.0)),
    }
    score = (
        0.12
        + (weights["candidate_score"] * features["candidate_score"])
        + (weights["concept_confidence"] * features["concept_confidence"])
        + (weights["predictive_risk"] * features["predictive_risk"])
        + (weights["selfplay_reward"] * features["selfplay_reward"])
        + (weights["robustness"] * features["robustness"])
        + (weights["feedback_bonus"] * features["feedback_bonus"])
    )
    return {
        "candidate_id": candidate.get("candidate_id"),
        "query_id": candidate.get("query_id"),
        "evidence_ref": candidate.get("evidence_ref"),
        "priority_score": round(_clamp(score), 6),
        "reason_codes": _candidate_reason_codes(features),
        "features": features,
        "raw_content_included": False,
    }


def _apply_query_mode(query: dict[str, Any], mode: str) -> dict[str, Any]:
    row = dict(query)
    row["policy_action"] = {
        "shadow": "record_only",
        "assist": "suggest_query",
        "partial": "eligible_query_seed",
    }[mode]
    row["human_approval_required"] = True
    return row


def _apply_candidate_mode(candidate: dict[str, Any], mode: str, state: dict[str, Any]) -> dict[str, Any]:
    row = dict(candidate)
    if mode == "shadow":
        action = "record_only"
    elif mode == "assist":
        action = "suggest_review_priority"
    else:
        threshold = float(state["partial_candidate_threshold"])
        action = "route_to_review_queue" if float(row["priority_score"]) >= threshold else "hold_for_sampling"
    row["policy_action"] = action
    row["human_final_decision_required"] = True
    return row


def _deployment_effect(mode: str) -> str:
    return {
        "shadow": "record_only_no_workflow_impact",
        "assist": "suggestion_only_human_decides",
        "partial": "limited_metadata_routing_human_final",
    }[mode]


def _query_reason_codes(features: dict[str, float]) -> list[str]:
    reasons = []
    if features["expected_reward_prior"] >= 0.5:
        reasons.append("historical_query_reward")
    if features["predictive_risk"] >= 0.4:
        reasons.append("predictive_variant_priority")
    if features["selfplay_reward"] >= 0.35:
        reasons.append("selfplay_robustness_gap")
    if features["robustness"] >= 0.4:
        reasons.append("exploration_priority")
    return reasons or ["baseline_stable_policy"]


def _candidate_reason_codes(features: dict[str, float]) -> list[str]:
    reasons = []
    if features["candidate_score"] >= 0.55:
        reasons.append("candidate_score")
    if features["concept_confidence"] >= 0.55:
        reasons.append("concept_match")
    if features["predictive_risk"] >= 0.4:
        reasons.append("predictive_risk")
    if features["selfplay_reward"] >= 0.35:
        reasons.append("selfplay_gap")
    return reasons or ["low_confidence_sampling"]


def _feature_summary(queries: list[dict[str, Any]], candidates: list[dict[str, Any]]) -> dict[str, float]:
    rows = [row.get("features", {}) for row in queries + candidates]
    keys = set().union(*(row.keys() for row in rows)) if rows else set()
    return {key: round(sum(float(row.get(key, 0.0)) for row in rows) / len(rows), 6) for key in sorted(keys)}


def _action_id(
    context: dict[str, Any],
    mode: str,
    queries: list[dict[str, Any]],
    candidates: list[dict[str, Any]],
) -> str:
    material = json.dumps(
        {
            "context_id": context.get("context_id"),
            "mode": mode,
            "queries": [query.get("query_id") for query in queries],
            "candidates": [candidate.get("candidate_id") for candidate in candidates],
        },
        ensure_ascii=False,
        sort_keys=True,
    )
    digest = hashlib.sha1(material.encode("utf-8")).hexdigest()[:12]
    return f"policy_action_{digest}"


def _normalize_weights(weights: dict[str, float]) -> dict[str, float]:
    clipped = {key: max(0.0, float(value)) for key, value in weights.items()}
    total = sum(clipped.values()) or 1.0
    return {key: round(value / total, 6) for key, value in sorted(clipped.items())}


def _clamp(value: Any) -> float:
    try:
        numeric = float(value)
    except (TypeError, ValueError):
        numeric = 0.0
    return max(0.0, min(1.0, numeric))
