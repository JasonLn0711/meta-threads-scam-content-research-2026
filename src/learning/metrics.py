"""Reviewer simulation and reward metrics."""

from __future__ import annotations

import random
from collections import defaultdict
from typing import Any


def simulate_review(candidate: dict[str, Any], rng: random.Random | None = None) -> dict[str, Any]:
    """Simulate human review outcome and review time for one selected candidate."""
    rng = rng or random.Random()
    score = float(candidate.get("score", 0.0) or 0.0)
    features = candidate.get("features", {})
    scam_probability = min(0.9, 0.08 + (0.65 * score))
    uncertain_probability = max(0.05, 0.22 - (0.12 * score))
    if features.get("hard_negative_warning"):
        scam_probability = min(scam_probability, 0.08)
        uncertain_probability = max(uncertain_probability, 0.2)
    roll = rng.random()

    if roll < scam_probability:
        decision = "scam"
    elif roll < scam_probability + uncertain_probability:
        decision = "uncertain"
    else:
        decision = "non_scam"

    complexity = 0.2 * sum(1 for value in features.values() if value is True)
    uncertainty_penalty = 0.8 if decision == "uncertain" else 0.0
    review_minutes = 0.9 + (1.4 * (1.0 - min(score, 1.0))) + complexity + uncertainty_penalty + rng.uniform(0.0, 0.4)

    return {
        "candidate_id": candidate["candidate_id"],
        "query_id": candidate.get("query_id", ""),
        "score": score,
        "decision": decision,
        "review_minutes": round(review_minutes, 3),
        "high_value": decision == "scam",
    }


def compute_reward(results: list[dict[str, Any]]) -> float:
    """Return high-value candidates per reviewer hour."""
    total_minutes = sum(float(result.get("review_minutes", 0.0) or 0.0) for result in results)
    if total_minutes <= 0:
        return 0.0
    scam_count = sum(1 for result in results if result.get("decision") == "scam")
    return round(scam_count / (total_minutes / 60.0), 6)


def summarize_results(results: list[dict[str, Any]]) -> dict[str, Any]:
    total_minutes = round(sum(float(result.get("review_minutes", 0.0) or 0.0) for result in results), 3)
    scam_count = sum(1 for result in results if result.get("decision") == "scam")
    uncertain_count = sum(1 for result in results if result.get("decision") == "uncertain")
    non_scam_count = sum(1 for result in results if result.get("decision") == "non_scam")
    return {
        "reviewed_count": len(results),
        "scam_count": scam_count,
        "uncertain_count": uncertain_count,
        "non_scam_count": non_scam_count,
        "total_review_minutes": total_minutes,
        "reward_high_value_per_reviewer_hour": compute_reward(results),
    }


def rewards_by_query(results: list[dict[str, Any]]) -> dict[str, float]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for result in results:
        grouped[str(result.get("query_id", ""))].append(result)
    return {query_id: compute_reward(query_results) for query_id, query_results in grouped.items()}
