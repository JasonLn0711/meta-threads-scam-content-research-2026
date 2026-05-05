"""Prompt-shaped query generation for advanced synthetic discovery runs."""

from __future__ import annotations

import hashlib
import json
from typing import Any


DEFAULT_HIGH_SIGNAL_FEATURES = ["guaranteed_return", "off_platform_contact", "authority_impersonation"]

SIGNAL_QUERY_LIBRARY: dict[str, list[dict[str, str]]] = {
    "guaranteed_return": [
        {
            "query": "保證收益 投資老師 加群",
            "strategy": "guaranteed_return_cluster",
            "expected_signal": "guaranteed_return",
        },
        {
            "query": "穩賺 明牌 私訊 投資",
            "strategy": "guaranteed_return_cluster",
            "expected_signal": "guaranteed_return",
        },
    ],
    "off_platform_contact": [
        {
            "query": "LINE 投資群 老師 助理",
            "strategy": "off_platform_contact_cluster",
            "expected_signal": "off_platform_contact",
        },
        {
            "query": "私訊 領取 股票名單 群組",
            "strategy": "off_platform_contact_cluster",
            "expected_signal": "off_platform_contact",
        },
    ],
    "authority_impersonation": [
        {
            "query": "投資老師 助理 分析師 帶單",
            "strategy": "authority_impersonation_cluster",
            "expected_signal": "authority_impersonation",
        },
        {
            "query": "官方分析師 股票健檢 私訊",
            "strategy": "authority_impersonation_cluster",
            "expected_signal": "authority_impersonation",
        },
    ],
    "urgency": [
        {
            "query": "限時名額 明牌 開盤前",
            "strategy": "urgency_teaser_cluster",
            "expected_signal": "urgency",
        },
        {
            "query": "最後免費分享 股票代碼 立刻",
            "strategy": "urgency_teaser_cluster",
            "expected_signal": "urgency",
        },
    ],
    "hard_negative_warning": [
        {
            "query": "反詐 投資心得 風險提醒",
            "strategy": "hard_negative_calibration",
            "expected_signal": "hard_negative_warning",
        },
        {
            "query": "一般投資討論 不要相信 加群",
            "strategy": "hard_negative_calibration",
            "expected_signal": "hard_negative_warning",
        },
    ],
}


def build_prompt(context: dict[str, Any]) -> str:
    """Build the prompt an approved LLM adapter would receive."""
    safe_context = {
        "recent_performance": context.get("recent_performance", {}),
        "language_distribution": context.get("language_distribution", {"zh-Hant": 1.0}),
        "high_signal_features": context.get("high_signal_features", DEFAULT_HIGH_SIGNAL_FEATURES),
        "failed_clusters": context.get("failed_clusters", []),
        "top_clusters": context.get("top_clusters", []),
        "top_concepts": context.get("top_concepts", []),
        "dynamic_intelligence": context.get("dynamic_intelligence", {}),
        "exploration_priorities": context.get("exploration_priorities", []),
        "predicted_variants": context.get("predicted_variants", []),
        "selfplay_priorities": context.get("selfplay_priorities", []),
    }
    return (
        "You are generating search queries to discover investment-scam research candidates.\n"
        "Goal: maximize scam-worthy candidates per reviewer hour.\n"
        "Rules: exploit high-performing semantic clusters, explore nearby variations, "
        "avoid generic finance queries, keep outputs short, and preserve human final judgment.\n"
        "Output JSON objects with query, strategy, expected_signal, and exploration flag.\n"
        f"Context:\n{json.dumps(safe_context, ensure_ascii=False, sort_keys=True)}"
    )


def generate_queries(context: dict[str, Any] | None = None, *, count: int = 10) -> list[dict[str, Any]]:
    """Generate structured query objects from context without calling external APIs."""
    context = context or {}
    prompt = build_prompt(context)
    features = list(context.get("high_signal_features") or DEFAULT_HIGH_SIGNAL_FEATURES)
    failed_signals = set(_signals_from_clusters(context.get("failed_clusters", [])))

    candidates: list[dict[str, Any]] = []
    candidates.extend(_query_candidates_for_selfplay(context.get("selfplay_priorities", []), prompt=prompt))
    candidates.extend(_query_candidates_for_predictions(context.get("predicted_variants", []), prompt=prompt))
    candidates.extend(_query_candidates_for_concepts(context.get("top_concepts", []), prompt=prompt))
    candidates.extend(_query_candidates_for_intelligence(context.get("exploration_priorities", []), prompt=prompt))
    for feature in features:
        candidates.extend(_query_candidates_for_signal(feature, mode="exploit", prompt=prompt))

    for nearby in _nearby_exploration_signals(features):
        if nearby not in failed_signals:
            candidates.extend(_query_candidates_for_signal(nearby, mode="explore", prompt=prompt))

    candidates.extend(_query_candidates_for_signal("hard_negative_warning", mode="explore", prompt=prompt))
    deduped = _dedupe_queries(candidates)
    return deduped[: max(1, count)]


def _query_candidates_for_signal(signal: str, *, mode: str, prompt: str) -> list[dict[str, Any]]:
    templates = SIGNAL_QUERY_LIBRARY.get(signal, SIGNAL_QUERY_LIBRARY["hard_negative_warning"])
    return [
        {
            "query_id": _query_id(template["query"], mode),
            "query": template["query"],
            "query_string": template["query"],
            "strategy": template["strategy"],
            "expected_signal": template["expected_signal"],
            "exploration": mode == "explore",
            "mode": mode,
            "budget": 7 if mode == "exploit" else 5,
            "llm_prompt_hash": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
            "llm_backend": "local_prompt_policy_v1",
        }
        for template in templates
    ]


def _query_candidates_for_concepts(concepts: list[dict[str, Any]], *, prompt: str) -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    for concept in concepts[:3]:
        signal = str(concept.get("dominant_signal") or concept.get("expected_signal") or "guaranteed_return")
        if signal == "hard_negative_warning":
            continue
        templates = SIGNAL_QUERY_LIBRARY.get(signal, SIGNAL_QUERY_LIBRARY["guaranteed_return"])
        base = templates[0]
        concept_name = str(concept.get("concept_name") or "").strip()
        query = base["query"] if not concept_name else f"{concept_name} 投資 私訊"
        candidates.append(
            {
                "query_id": _query_id(query, "concept"),
                "query": query,
                "query_string": query,
                "strategy": base["strategy"],
                "expected_signal": base["expected_signal"],
                "concept_id": concept.get("concept_id"),
                "exploration": False,
                "mode": "concept_exploit",
                "budget": 7,
                "llm_prompt_hash": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
                "llm_backend": "local_prompt_policy_v1",
            }
        )
    return candidates


def _query_candidates_for_intelligence(priorities: list[dict[str, Any]], *, prompt: str) -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    for priority in priorities[:3]:
        signal = str(priority.get("dominant_signal") or "off_platform_contact")
        if signal == "hard_negative_warning":
            signal = "urgency"
        templates = SIGNAL_QUERY_LIBRARY.get(signal, SIGNAL_QUERY_LIBRARY["off_platform_contact"])
        base = templates[0]
        concept_name = str(priority.get("concept_name") or "").strip()
        if concept_name:
            query = f"{concept_name} 變形 投資 私訊"
        else:
            query = f"新型 投資 私訊 群組 {str(priority.get('concept_id', 'concept'))[-6:]}"
        candidates.append(
            {
                "query_id": _query_id(query, "intelligence"),
                "query": query,
                "query_string": query,
                "strategy": f"dynamic_{base['strategy']}",
                "expected_signal": base["expected_signal"],
                "concept_id": priority.get("concept_id"),
                "exploration": True,
                "mode": "dynamic_explore",
                "budget": 5,
                "exploration_priority": priority.get("exploration_priority", 0.0),
                "llm_prompt_hash": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
                "llm_backend": "local_prompt_policy_v1",
            }
        )
    return candidates


def _query_candidates_for_predictions(predictions: list[dict[str, Any]], *, prompt: str) -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    for prediction in predictions[:3]:
        signal = str(prediction.get("origin_dominant_signal") or "off_platform_contact")
        if signal == "hard_negative_warning":
            signal = "urgency"
        templates = SIGNAL_QUERY_LIBRARY.get(signal, SIGNAL_QUERY_LIBRARY["off_platform_contact"])
        base = templates[0]
        query = str(prediction.get("search_query") or "").strip()
        if not query:
            query = f"{str(prediction.get('variant_name', 'variant'))} 投資 交流"
        candidates.append(
            {
                "query_id": _query_id(query, "predictive"),
                "query": query,
                "query_string": query,
                "strategy": f"predictive_{str(prediction.get('evasion_type', 'simulation'))}",
                "expected_signal": base["expected_signal"],
                "concept_id": prediction.get("origin_concept_id"),
                "variant_id": prediction.get("variant_id"),
                "evasion_type": prediction.get("evasion_type"),
                "predictive_risk_score": prediction.get("risk_score", 0.0),
                "exploration": True,
                "mode": "predictive_explore",
                "budget": 5,
                "exploration_priority": prediction.get("risk_score", 0.0),
                "llm_prompt_hash": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
                "llm_backend": "local_prompt_policy_v1",
            }
        )
    return candidates


def _query_candidates_for_selfplay(priorities: list[dict[str, Any]], *, prompt: str) -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    for priority in priorities[:3]:
        signal = str(priority.get("origin_dominant_signal") or "off_platform_contact")
        if signal == "hard_negative_warning":
            signal = "urgency"
        templates = SIGNAL_QUERY_LIBRARY.get(signal, SIGNAL_QUERY_LIBRARY["off_platform_contact"])
        base = templates[0]
        query = str(priority.get("search_query") or "").strip()
        if not query:
            query = f"{str(priority.get('evasion_characteristic', 'abstract_variant'))} investment discussion"
        candidates.append(
            {
                "query_id": _query_id(query, "selfplay"),
                "query": query,
                "query_string": query,
                "strategy": f"selfplay_{str(priority.get('evasion_characteristic', 'abstract'))}",
                "expected_signal": base["expected_signal"],
                "concept_id": priority.get("origin_concept_id"),
                "selfplay_variant_id": priority.get("variant_id"),
                "selfplay_evasion_characteristic": priority.get("evasion_characteristic"),
                "selfplay_reward_signal": priority.get("selfplay_reward_signal", 0.0),
                "selfplay_detector_confidence": priority.get("detector_confidence", 0.0),
                "exploration": True,
                "mode": "selfplay_explore",
                "budget": 5,
                "exploration_priority": priority.get("exploration_priority", 0.0),
                "llm_prompt_hash": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
                "llm_backend": "local_prompt_policy_v1",
            }
        )
    return candidates


def _nearby_exploration_signals(features: list[str]) -> list[str]:
    priority = ["urgency", "authority_impersonation", "off_platform_contact", "guaranteed_return"]
    return [signal for signal in priority if signal not in set(features)]


def _signals_from_clusters(clusters: list[dict[str, Any]]) -> list[str]:
    signals: list[str] = []
    for cluster in clusters:
        signal = cluster.get("expected_signal") or cluster.get("theme") or cluster.get("signal")
        if signal:
            signals.append(str(signal))
    return signals


def _dedupe_queries(queries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    deduped: list[dict[str, Any]] = []
    for query in queries:
        key = str(query["query"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(query)
    return deduped


def _query_id(query: str, mode: str) -> str:
    digest = hashlib.sha1(f"{mode}:{query}".encode("utf-8")).hexdigest()[:10]
    return f"llm_{mode}_{digest}"
