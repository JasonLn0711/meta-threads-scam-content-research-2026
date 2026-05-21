"""Rule-based candidate scoring for review prioritization."""

from __future__ import annotations

from typing import Any


WEIGHTS = {
    "guaranteed_return": 0.4,
    "impersonation": 0.3,
    "off_platform_contact": 0.2,
    "urgency": 0.1,
}


def score_candidate(features: dict[str, Any]) -> float:
    """Return a weighted ranking score. This is not a classifier."""
    score = 0.0
    for feature_name, weight in WEIGHTS.items():
        score += weight if bool(features.get(feature_name)) else 0.0
    if bool(features.get("hard_negative_warning")):
        score -= 0.6
    return round(max(0.0, min(1.0, score)), 6)


def select_top_k(candidates: list[dict[str, Any]], k: int = 5) -> list[dict[str, Any]]:
    """Select top-K candidates for review by score, keeping deterministic ties."""
    return sorted(
        candidates,
        key=lambda candidate: (-float(candidate.get("score", 0.0)), candidate.get("candidate_id", "")),
    )[: max(0, k)]
