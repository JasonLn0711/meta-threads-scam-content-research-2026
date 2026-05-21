"""Sparse rule-based clustering over metadata features."""

from __future__ import annotations

from collections import defaultdict
from typing import Any

from engine.common import active_sparse_features, candidate_id, feature_weights


def sparse_similarity(
    left: dict[str, Any],
    right: dict[str, Any],
    sparse_schema: dict[str, Any],
) -> dict[str, Any]:
    weights = feature_weights(sparse_schema)
    left_features = set(active_sparse_features(left))
    right_features = set(active_sparse_features(right))
    shared = sorted(left_features & right_features)
    union = sorted(left_features | right_features)
    union_weight = sum(weights.get(feature, 0.0) for feature in union) or 1.0
    shared_weight = sum(weights.get(feature, 0.0) for feature in shared)
    return {
        "shared_features": shared,
        "shared_features_count": len(shared),
        "weighted_overlap": round(shared_weight / union_weight, 6),
    }


def cluster_sparse_candidates(
    candidates: list[dict[str, Any]],
    sparse_schema: dict[str, Any],
    threshold: float = 0.45,
) -> dict[str, Any]:
    candidate_ids = [candidate_id(candidate) for candidate in candidates]
    parent = {item_id: item_id for item_id in candidate_ids}

    def find(item_id: str) -> str:
        while parent[item_id] != item_id:
            parent[item_id] = parent[parent[item_id]]
            item_id = parent[item_id]
        return item_id

    def union(left: str, right: str) -> None:
        left_root = find(left)
        right_root = find(right)
        if left_root != right_root:
            parent[right_root] = left_root

    pairwise: list[dict[str, Any]] = []
    for left_index, left in enumerate(candidates):
        for right in candidates[left_index + 1 :]:
            similarity = sparse_similarity(left, right, sparse_schema)
            row = {
                "left": candidate_id(left),
                "right": candidate_id(right),
                **similarity,
            }
            pairwise.append(row)
            if similarity["weighted_overlap"] >= threshold:
                union(candidate_id(left), candidate_id(right))

    grouped: dict[str, list[str]] = defaultdict(list)
    by_id = {candidate_id(candidate): candidate for candidate in candidates}
    for item_id in candidate_ids:
        grouped[find(item_id)].append(item_id)

    clusters = []
    for index, members in enumerate(sorted(grouped.values(), key=lambda items: (-len(items), items)), 1):
        feature_sets = [set(active_sparse_features(by_id[member])) for member in members]
        active_features = sorted(set().union(*feature_sets)) if feature_sets else []
        core_features = sorted(set.intersection(*feature_sets)) if feature_sets else []
        clusters.append(
            {
                "cluster_id": f"sparse-cluster-{index:04d}",
                "candidate_ids": sorted(members),
                "active_features": active_features,
                "core_features": core_features,
            }
        )

    return {
        "schema_version": "sparse_clusters_v1",
        "decision_layer": "sparse_primary",
        "similarity": "weighted_jaccard_over_binary_sparse_features",
        "threshold": threshold,
        "candidate_count": len(candidates),
        "clusters": clusters,
        "pairwise_similarity": pairwise,
        "guardrails": {
            "raw_threads_content_included": False,
            "embedding_used_for_decision": False,
        },
    }
