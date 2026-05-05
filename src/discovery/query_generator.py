"""Query-arm generation for closed-loop discovery experiments."""

from __future__ import annotations

from typing import Any


QUERY_TEMPLATES: tuple[dict[str, Any], ...] = (
    {
        "query_id": "arm_guaranteed_return",
        "query_string": "保證獲利 投資 社群",
        "strategy": "guaranteed_return_cluster",
        "budget": 7,
        "prior_weight": 0.55,
    },
    {
        "query_id": "arm_authority_impersonation",
        "query_string": "投資老師 助理 分析師",
        "strategy": "authority_impersonation_cluster",
        "budget": 6,
        "prior_weight": 0.45,
    },
    {
        "query_id": "arm_off_platform_contact",
        "query_string": "LINE 加群 投資 私訊",
        "strategy": "off_platform_contact_cluster",
        "budget": 7,
        "prior_weight": 0.5,
    },
    {
        "query_id": "arm_urgent_teaser",
        "query_string": "限時 名額 明牌 投資",
        "strategy": "urgency_teaser_cluster",
        "budget": 6,
        "prior_weight": 0.35,
    },
    {
        "query_id": "arm_hard_negative",
        "query_string": "投資心得 市場討論 反詐提醒",
        "strategy": "hard_negative_calibration",
        "budget": 5,
        "prior_weight": 0.15,
    },
)


def known_query_ids() -> list[str]:
    return [template["query_id"] for template in QUERY_TEMPLATES]


def generate_queries(
    bandit_state: dict[str, Any] | None,
    *,
    selected_query_ids: list[str] | None = None,
    query_count: int = 3,
) -> list[dict[str, Any]]:
    """Return query objects with static templates and bandit-derived weights."""
    state = bandit_state or {}
    arms = state.get("arms", {}) if isinstance(state, dict) else {}
    ranked_templates = sorted(
        (_query_with_weight(template, arms.get(template["query_id"], {})) for template in QUERY_TEMPLATES),
        key=lambda query: (-float(query["weight"]), query["query_id"]),
    )

    if selected_query_ids:
        by_id = {query["query_id"]: query for query in ranked_templates}
        return [by_id[query_id] for query_id in selected_query_ids if query_id in by_id]

    return ranked_templates[: max(1, query_count)]


def _query_with_weight(template: dict[str, Any], arm_state: dict[str, Any]) -> dict[str, Any]:
    trials = int(arm_state.get("trials", 0) or 0)
    average_reward = float(arm_state.get("average_reward", 0.0) or 0.0)
    prior_weight = float(template["prior_weight"])
    dynamic_weight = prior_weight + (average_reward / 60.0)
    budget_boost = 2 if trials and average_reward >= 20 else 0
    return {
        "query_id": template["query_id"],
        "query_string": template["query_string"],
        "strategy": template["strategy"],
        "budget": int(template["budget"]) + budget_boost,
        "weight": round(dynamic_weight, 6),
        "trials": trials,
        "average_reward": average_reward,
        "source": "mock_connector",
    }
