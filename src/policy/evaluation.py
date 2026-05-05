"""Evaluation reports for adaptive policy deployment loops."""

from __future__ import annotations

import statistics
from typing import Any

from src.evidence.storage import utc_now
from src.policy.logging import POLICY_EVALUATION_LOG, append_jsonl


def evaluate_policy(logs: list[dict[str, Any]], *, log: bool = False) -> dict[str, Any]:
    """Compute reviewer-hour reward, latency, and robustness from policy logs."""
    outcomes = [entry.get("outcome", entry) for entry in logs if entry.get("outcome") or entry.get("human_feedback")]
    total_scam = sum(int(outcome.get("human_feedback", {}).get("scam_count", 0) or 0) for outcome in outcomes)
    total_minutes = round(
        sum(float(outcome.get("human_feedback", {}).get("review_minutes", 0.0) or 0.0) for outcome in outcomes),
        3,
    )
    reward_per_hour = round(total_scam / (total_minutes / 60.0), 6) if total_minutes > 0 else 0.0
    lags = [
        float(outcome.get("delayed_outcomes", {}).get("average_time_lag_rounds"))
        for outcome in outcomes
        if outcome.get("delayed_outcomes", {}).get("average_time_lag_rounds") is not None
    ]
    error_counts = [int(outcome.get("system_errors", {}).get("count", 0) or 0) for outcome in outcomes]
    total_errors = sum(error_counts)
    robustness = _robustness_score(logs, total_errors)
    mode_counts: dict[str, int] = {}
    for entry in logs:
        mode = str(entry.get("action", {}).get("mode") or entry.get("mode") or "unknown")
        mode_counts[mode] = mode_counts.get(mode, 0) + 1
    report = {
        "schema_version": "adaptive_policy_evaluation_v1",
        "created_at": utc_now(),
        "decision_count": len(logs),
        "mode_counts": mode_counts,
        "reward_per_reviewer_hour": reward_per_hour,
        "total_review_minutes": total_minutes,
        "scam_count": total_scam,
        "detection_latency_rounds": round(statistics.fmean(lags), 6) if lags else None,
        "system_error_count": total_errors,
        "robustness": robustness,
        "raw_source_included": False,
    }
    if log:
        append_jsonl(POLICY_EVALUATION_LOG, report)
    return report


def _robustness_score(logs: list[dict[str, Any]], total_errors: int) -> float:
    if not logs:
        return 0.0
    error_component = max(0.0, 1.0 - (total_errors / max(1, len(logs))))
    selfplay_scores = []
    for entry in logs:
        summary = entry.get("action", {}).get("feature_summary", {})
        if "selfplay_reward" in summary:
            selfplay_scores.append(1.0 - min(1.0, float(summary.get("selfplay_reward", 0.0))))
    selfplay_component = statistics.fmean(selfplay_scores) if selfplay_scores else error_component
    return round(max(0.0, min(1.0, (0.55 * error_component) + (0.45 * selfplay_component))), 6)
