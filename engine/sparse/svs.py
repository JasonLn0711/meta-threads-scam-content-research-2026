"""Signal Value Score calculation for sparse metadata features."""

from __future__ import annotations

from collections import defaultdict
from statistics import mean
from typing import Any

from engine.common import (
    active_sparse_features,
    batch_id,
    candidate_id,
    feature_weights,
    review_decision,
    review_time_seconds,
    second_review_required,
    sparse_feature_value,
)


def information_density(candidate: dict[str, Any], sparse_schema: dict[str, Any]) -> float:
    weights = feature_weights(sparse_schema)
    total_weight = sum(weights.values()) or 1.0
    active_weight = sum(weights.get(feature, 0.0) for feature in active_sparse_features(candidate))
    return active_weight / total_weight


def cognitive_load(candidate: dict[str, Any], sparse_schema: dict[str, Any]) -> float:
    config = sparse_schema.get("cognitive_load", {})
    load = float(config.get("base", 1.0))
    if sparse_feature_value(candidate, "needs_thread"):
        load += float(config.get("needs_thread_weight", 0.0))
    if second_review_required(candidate):
        load += float(config.get("second_review_weight", 0.0))
    active_count = len(active_sparse_features(candidate))
    threshold = int(config.get("dense_feature_threshold", active_count + 1))
    if active_count > threshold:
        load += (active_count - threshold) * float(config.get("dense_feature_penalty_per_feature", 0.0))
    return max(load, 1.0)


def svs_score(yield_rate: float, info_density: float, review_time: float, load: float) -> float:
    return (yield_rate * info_density) / (max(review_time, 1.0) * max(load, 1.0))


def score_candidate_group(candidates: list[dict[str, Any]], sparse_schema: dict[str, Any]) -> dict[str, Any]:
    if not candidates:
        return {
            "reviewed_count": 0,
            "scam_count": 0,
            "yield_rate": 0.0,
            "information_density": 0.0,
            "review_time": 0.0,
            "cognitive_load": 0.0,
            "svs": 0.0,
        }
    scam_count = sum(1 for candidate in candidates if review_decision(candidate) == "scam")
    yield_rate = scam_count / len(candidates)
    avg_info_density = mean(information_density(candidate, sparse_schema) for candidate in candidates)
    avg_review_time = mean(review_time_seconds(candidate) for candidate in candidates)
    avg_cognitive_load = mean(cognitive_load(candidate, sparse_schema) for candidate in candidates)
    return {
        "reviewed_count": len(candidates),
        "scam_count": scam_count,
        "yield_rate": round(yield_rate, 6),
        "information_density": round(avg_info_density, 6),
        "review_time": round(avg_review_time, 6),
        "cognitive_load": round(avg_cognitive_load, 6),
        "svs": round(svs_score(yield_rate, avg_info_density, avg_review_time, avg_cognitive_load), 9),
    }


def signal_scores(candidates: list[dict[str, Any]], sparse_schema: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for feature_name in sparse_schema.get("features", {}):
        feature_candidates = [
            candidate for candidate in candidates if sparse_feature_value(candidate, str(feature_name))
        ]
        score = score_candidate_group(feature_candidates, sparse_schema)
        rows.append(
            {
                "signal_id": str(feature_name),
                **score,
            }
        )
    return sorted(rows, key=lambda row: (-float(row["svs"]), str(row["signal_id"])))


def batch_scores(candidates: list[dict[str, Any]], sparse_schema: dict[str, Any]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for candidate in candidates:
        grouped[batch_id(candidate)].append(candidate)
    rows = []
    for group_id, group_candidates in sorted(grouped.items()):
        rows.append({"batch_id": group_id, **score_candidate_group(group_candidates, sparse_schema)})
    return rows


def build_latest_ranking(candidates: list[dict[str, Any]], sparse_schema: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": "signal_scores_v1",
        "decision_layer": "sparse_primary",
        "formula": "SVS = (yield_rate * information_density) / (review_time * cognitive_load)",
        "positive_yield_definition": "human research label scam, not legal fraud",
        "candidate_count": len(candidates),
        "candidate_ids": [candidate_id(candidate) for candidate in candidates],
        "ranked_signals": signal_scores(candidates, sparse_schema),
        "batch_scores": batch_scores(candidates, sparse_schema),
        "guardrails": {
            "raw_threads_content_included": False,
            "embedding_used_for_decision": False,
            "human_review_required": True,
        },
    }
