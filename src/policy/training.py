"""Offline and safe-update training for adaptive policy weights."""

from __future__ import annotations

import statistics
from typing import Any

from src.evidence.storage import utc_now
from src.policy.logging import POLICY_DECISION_LOG, POLICY_STATE_PATH, read_json, read_jsonl, write_json
from src.policy.policy import DEFAULT_WEIGHTS, default_policy_state
from src.selfplay.logging import SELFPLAY_STATE_PATH, read_json as read_selfplay_json


def train_policy(
    logs: list[dict[str, Any]],
    *,
    prior_state: dict[str, Any] | None = None,
    learning_rate: float = 0.12,
    max_weight_delta: float = 0.06,
) -> dict[str, Any]:
    """Train policy weights from past metadata logs with bounded movement."""
    state = default_policy_state(prior_state)
    if not logs:
        return state
    rewards = [_reward_from_log(entry) for entry in logs]
    avg_reward = statistics.fmean(rewards) if rewards else 0.0
    target = _target_weights(logs)
    weights = dict(state["weights"])
    updated = {}
    largest_delta = 0.0
    for key in DEFAULT_WEIGHTS:
        desired = target.get(key, weights.get(key, DEFAULT_WEIGHTS[key]))
        delta = max(-max_weight_delta, min(max_weight_delta, learning_rate * (desired - weights[key])))
        updated[key] = max(0.0, weights[key] + delta)
        largest_delta = max(largest_delta, abs(delta))
    updated = _normalize(updated)
    trained = dict(state)
    trained["weights"] = updated
    trained["policy_version"] = int(state["policy_version"]) + 1
    trained["training_examples"] = int(state.get("training_examples", 0)) + len(logs)
    trained["last_train_reward"] = round(avg_reward, 6)
    trained["largest_weight_delta"] = round(largest_delta, 6)
    trained["last_updated"] = utc_now()
    trained["raw_source_included"] = False
    return trained


def update_policy(
    new_data: list[dict[str, Any]],
    *,
    state: dict[str, Any] | None = None,
    historical_logs: list[dict[str, Any]] | None = None,
    persist: bool = True,
) -> dict[str, Any]:
    """Safely update policy using recent and historical logs."""
    base_state = default_policy_state(state)
    history = list(historical_logs or [])
    recent = list(new_data or [])
    historical_reward = statistics.fmean([_reward_from_log(entry) for entry in history]) if history else 0.0
    recent_reward = statistics.fmean([_reward_from_log(entry) for entry in recent]) if recent else historical_reward
    learning_rate = 0.06 if history and recent_reward + 0.08 < historical_reward else 0.1
    training_window = (history[-80:] + recent[-40:]) if history else recent[-40:]
    updated = train_policy(training_window, prior_state=base_state, learning_rate=learning_rate)
    updated["safe_update"] = {
        "historical_examples": len(history),
        "recent_examples": len(recent),
        "historical_reward": round(historical_reward, 6),
        "recent_reward": round(recent_reward, 6),
        "learning_rate": learning_rate,
        "overfit_guard": "reduced_rate_on_reward_drop" if learning_rate < 0.1 else "standard_bounded_update",
    }
    if persist:
        write_json(POLICY_STATE_PATH, updated)
    return updated


def load_combined_training_logs(
    *,
    include_selfplay: bool = True,
    decision_log_limit: int = 200,
) -> list[dict[str, Any]]:
    """Combine policy decision logs with self-play-derived exploration signals."""
    logs = read_jsonl(POLICY_DECISION_LOG, limit=decision_log_limit)
    if include_selfplay:
        logs.extend(_selfplay_training_logs())
    return logs


def load_policy_state() -> dict[str, Any]:
    return default_policy_state(read_json(POLICY_STATE_PATH))


def _target_weights(logs: list[dict[str, Any]]) -> dict[str, float]:
    totals = {key: 0.0 for key in DEFAULT_WEIGHTS}
    reward_total = 0.0
    for entry in logs:
        reward = max(0.0, _reward_from_log(entry))
        features = _features_from_log(entry)
        reward_total += reward
        for key in totals:
            totals[key] += reward * float(features.get(key, 0.0))
    if reward_total <= 0:
        return dict(DEFAULT_WEIGHTS)
    raw = {key: totals[key] / reward_total for key in totals}
    return _normalize(raw)


def _features_from_log(entry: dict[str, Any]) -> dict[str, float]:
    action = entry.get("action", {})
    summary = action.get("feature_summary") or entry.get("feature_summary") or {}
    return {
        "expected_reward_prior": _float(summary.get("expected_reward_prior", summary.get("reward", 0.0))),
        "candidate_score": _float(summary.get("candidate_score", 0.0)),
        "concept_confidence": _float(summary.get("concept_confidence", 0.0)),
        "predictive_risk": _float(summary.get("predictive_risk", 0.0)),
        "selfplay_reward": _float(summary.get("selfplay_reward", 0.0)),
        "robustness": _float(summary.get("robustness", 0.0)),
        "feedback_bonus": _float(summary.get("feedback_bonus", 0.0)),
    }


def _reward_from_log(entry: dict[str, Any]) -> float:
    if entry.get("reward") is not None:
        return _float(entry.get("reward"))
    outcome = entry.get("outcome", entry)
    return _float(outcome.get("reward", 0.0))


def _selfplay_training_logs() -> list[dict[str, Any]]:
    state = read_selfplay_json(SELFPLAY_STATE_PATH)
    rows = []
    for priority in state.get("selfplay_priorities", []):
        reward = _float(priority.get("exploration_priority", priority.get("selfplay_reward_signal", 0.0)))
        rows.append(
            {
                "schema_version": "selfplay_policy_training_bridge_v1",
                "source": "selfplay",
                "action": {
                    "mode": "shadow",
                    "feature_summary": {
                        "expected_reward_prior": 0.0,
                        "candidate_score": 0.0,
                        "concept_confidence": 0.0,
                        "predictive_risk": 0.0,
                        "selfplay_reward": _float(priority.get("selfplay_reward_signal", 0.0)),
                        "robustness": 1.0 - _float(priority.get("detector_confidence", 0.0)),
                        "feedback_bonus": 0.0,
                    },
                },
                "outcome": {"reward": reward},
                "reward": reward,
                "raw_source_included": False,
            }
        )
    return rows


def _normalize(values: dict[str, float]) -> dict[str, float]:
    clipped = {key: max(0.0, float(value)) for key, value in values.items()}
    total = sum(clipped.values()) or 1.0
    return {key: round(value / total, 6) for key, value in sorted(clipped.items())}


def _float(value: Any) -> float:
    try:
        return max(0.0, min(1.0, float(value)))
    except (TypeError, ValueError):
        return 0.0
