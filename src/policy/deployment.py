"""Governed deployment-loop scaffolding for adaptive policy decisions."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable

from src.evidence.storage import REPO_ROOT, utc_now
from src.policy.evaluation import evaluate_policy
from src.policy.feedback import collect_feedback
from src.policy.logging import POLICY_DECISION_LOG, append_jsonl
from src.policy.policy import VALID_DEPLOYMENT_MODES, default_policy_state, policy
from src.selfplay.runner import load_selfplay_priorities


FeedbackProvider = Callable[[dict[str, Any], dict[str, Any]], dict[str, Any]]


def run_deployment_loop(
    contexts: list[dict[str, Any]],
    *,
    mode: str = "shadow",
    state: dict[str, Any] | None = None,
    feedback_provider: FeedbackProvider | None = None,
    log: bool = True,
) -> dict[str, Any]:
    """Run policy decisions over metadata-only contexts and log feedback."""
    if mode not in VALID_DEPLOYMENT_MODES:
        raise ValueError(f"unsupported deployment mode: {mode}")
    policy_state = default_policy_state(state)
    records = []
    for context in contexts:
        action = policy(context, state=policy_state, mode=mode)
        feedback = (
            feedback_provider(context, action)
            if feedback_provider
            else _synthetic_metadata_feedback(context, action)
        )
        outcome = collect_feedback(
            {**action, "simulated_feedback": feedback.get("simulated_feedback", False)},
            human_labels=feedback.get("human_labels", []),
            delayed_outcomes=feedback.get("delayed_outcomes", []),
            system_errors=feedback.get("system_errors", []),
            log=log,
        )
        record = log_decision(context, action, outcome=outcome, reward=outcome["reward"], log=log)
        records.append(record)
    report = evaluate_policy(records, log=log)
    return {
        "schema_version": "adaptive_policy_deployment_run_v1",
        "created_at": utc_now(),
        "mode": mode,
        "decision_count": len(records),
        "records": records,
        "evaluation": report,
        "raw_source_included": False,
    }


def log_decision(
    context: dict[str, Any],
    action: dict[str, Any],
    *,
    outcome: dict[str, Any] | None = None,
    reward: float | None = None,
    log: bool = True,
) -> dict[str, Any]:
    """Append one context/action/outcome/reward record."""
    entry = {
        "schema_version": "adaptive_policy_context_action_v1",
        "created_at": utc_now(),
        "context": sanitize_context(context),
        "action": action,
        "outcome": outcome,
        "reward": reward if reward is not None else (outcome or {}).get("reward"),
        "raw_source_included": False,
    }
    if log:
        append_jsonl(POLICY_DECISION_LOG, entry)
    return entry


def build_policy_contexts_from_sources(*, limit: int = 5) -> list[dict[str, Any]]:
    """Build metadata-only policy contexts from self-play and local metrics."""
    contexts: list[dict[str, Any]] = []
    for index, priority in enumerate(load_selfplay_priorities()[:limit]):
        contexts.append(
            {
                "schema_version": "adaptive_policy_context_v1",
                "context_id": f"selfplay_bridge_{index + 1:04d}",
                "source": "selfplay_bridge",
                "queries": [
                    {
                        "query_id": f"selfplay_query_{index + 1:04d}",
                        "query_string": priority.get("search_query"),
                        "strategy": f"selfplay_{priority.get('evasion_characteristic', 'abstract')}",
                        "expected_signal": priority.get("origin_dominant_signal"),
                        "selfplay_reward_signal": priority.get("selfplay_reward_signal", 0.0),
                        "exploration_priority": priority.get("exploration_priority", 0.0),
                    }
                ],
                "candidates": [],
                "selfplay_priority": priority,
                "raw_source_included": False,
            }
        )
    contexts.extend(_contexts_from_advanced_metrics(limit=max(0, limit - len(contexts))))
    while len(contexts) < limit:
        index = len(contexts) + 1
        contexts.append(_default_context(index))
    return contexts[:limit]


def sanitize_context(context: dict[str, Any]) -> dict[str, Any]:
    """Keep logs metadata-only even if a caller passes extra fields."""
    allowed = {
        "schema_version",
        "context_id",
        "source",
        "queries",
        "candidates",
        "selfplay_priority",
        "round",
        "raw_source_included",
    }
    sanitized = {key: context[key] for key in allowed if key in context}
    sanitized["raw_source_included"] = False
    return sanitized


def _contexts_from_advanced_metrics(*, limit: int) -> list[dict[str, Any]]:
    if limit <= 0:
        return []
    path = REPO_ROOT / "data/learning_state/advanced_metrics.json"
    if not path.exists():
        return []
    metrics = json.loads(path.read_text(encoding="utf-8"))
    contexts = []
    rows = sorted(
        metrics.get("query_performance", {}).values(),
        key=lambda row: (-float(row.get("reward", 0.0) or 0.0), str(row.get("id", ""))),
    )
    for index, row in enumerate(rows[:limit]):
        contexts.append(
            {
                "schema_version": "adaptive_policy_context_v1",
                "context_id": f"advanced_metrics_{index + 1:04d}",
                "source": "advanced_metrics",
                "queries": [
                    {
                        "query_id": row.get("id"),
                        "query_string": row.get("id"),
                        "strategy": "historical_query_arm",
                        "expected_signal": row.get("expected_signal"),
                        "expected_reward_prior": min(1.0, float(row.get("reward", 0.0) or 0.0) / 24.0),
                    }
                ],
                "candidates": [],
                "raw_source_included": False,
            }
        )
    return contexts


def _default_context(index: int) -> dict[str, Any]:
    return {
        "schema_version": "adaptive_policy_context_v1",
        "context_id": f"default_policy_context_{index:04d}",
        "source": "default_synthetic_context",
        "queries": [
            {
                "query_id": f"default_query_{index:04d}",
                "query_string": "metadata-only investment-scam research seed",
                "strategy": "shadow_baseline",
                "expected_signal": "authority_impersonation",
                "expected_reward_prior": 0.25,
            }
        ],
        "candidates": [
            {
                "candidate_id": f"default_candidate_{index:04d}",
                "score": 0.42,
                "features": {"concept_confidence": 0.35, "exploration_priority": 0.25},
                "raw_content_included": False,
            }
        ],
        "raw_source_included": False,
    }


def _synthetic_metadata_feedback(context: dict[str, Any], action: dict[str, Any]) -> dict[str, Any]:
    selected = action.get("candidate_prioritization") or action.get("query_selection") or []
    labels = []
    for index, row in enumerate(selected[:3]):
        score = float(row.get("priority_score", 0.0) or 0.0)
        decision = "scam" if score >= 0.3 else "uncertain"
        labels.append(
            {
                "decision": decision,
                "confidence": round(min(0.95, 0.45 + score), 6),
                "review_minutes": round(max(1.2, 3.2 - score), 3),
            }
        )
    delayed = []
    if context.get("source") == "selfplay_bridge":
        delayed.append({"observed": True, "time_lag_rounds": 1})
    return {
        "human_labels": labels,
        "delayed_outcomes": delayed,
        "system_errors": [],
        "simulated_feedback": True,
    }
