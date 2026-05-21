"""Feedback collection and reward shaping for adaptive policy logs."""

from __future__ import annotations

import statistics
from typing import Any

from src.evidence.storage import utc_now
from src.policy.logging import POLICY_FEEDBACK_LOG, append_jsonl


def collect_feedback(
    action: dict[str, Any],
    *,
    human_labels: list[dict[str, Any]] | None = None,
    delayed_outcomes: list[dict[str, Any]] | None = None,
    system_errors: list[dict[str, Any]] | None = None,
    log: bool = False,
) -> dict[str, Any]:
    """Collect metadata-only feedback and compute a bounded reward."""
    labels = list(human_labels or [])
    delayed = list(delayed_outcomes or [])
    errors = list(system_errors or [])
    scam_count = sum(1 for label in labels if label.get("decision") == "scam")
    review_minutes = round(sum(float(label.get("review_minutes", 0.0) or 0.0) for label in labels), 3)
    reward_per_hour = round(scam_count / (review_minutes / 60.0), 6) if review_minutes > 0 else 0.0
    normalized_review_reward = min(1.0, reward_per_hour / 24.0)
    delayed_score = _delayed_score(delayed)
    error_penalty = min(0.5, 0.12 * len(errors))
    reward = max(0.0, min(1.0, (0.78 * normalized_review_reward) + (0.17 * delayed_score) - error_penalty))
    outcome = {
        "schema_version": "adaptive_policy_feedback_v1",
        "action_id": action.get("action_id"),
        "created_at": utc_now(),
        "human_feedback": {
            "label_count": len(labels),
            "scam_count": scam_count,
            "review_minutes": review_minutes,
            "reward_per_reviewer_hour": reward_per_hour,
        },
        "delayed_outcomes": {
            "count": len(delayed),
            "observed_count": sum(1 for row in delayed if row.get("observed")),
            "average_time_lag_rounds": _average_time_lag(delayed),
        },
        "system_errors": {
            "count": len(errors),
            "types": sorted({str(error.get("type", "unknown")) for error in errors}),
        },
        "reward": round(reward, 6),
        "simulated_feedback": bool(action.get("simulated_feedback", False)),
        "raw_source_included": False,
    }
    if log:
        append_jsonl(POLICY_FEEDBACK_LOG, outcome)
    return outcome


def _delayed_score(delayed_outcomes: list[dict[str, Any]]) -> float:
    if not delayed_outcomes:
        return 0.0
    observed = sum(1 for row in delayed_outcomes if row.get("observed"))
    return max(0.0, min(1.0, observed / len(delayed_outcomes)))


def _average_time_lag(delayed_outcomes: list[dict[str, Any]]) -> float | None:
    lags = [float(row["time_lag_rounds"]) for row in delayed_outcomes if row.get("time_lag_rounds") is not None]
    if not lags:
        return None
    return round(statistics.fmean(lags), 6)
