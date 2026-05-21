"""Discovery-only embedding clustering over precomputed vectors."""

from __future__ import annotations

from collections import defaultdict
from typing import Any

from engine.common import candidate_id, embedding_vector
from engine.embedding.similarity import (
    candidates_with_embeddings,
    cosine_similarity,
    nearest_neighbors,
    pairwise_embedding_similarity,
)


def cluster_embedding_candidates(
    candidates: list[dict[str, Any]],
    threshold: float = 0.85,
    top_k: int = 3,
) -> dict[str, Any]:
    embedded = candidates_with_embeddings(candidates)
    skipped = [candidate_id(candidate) for candidate in candidates if not embedding_vector(candidate)]
    embedded_ids = [candidate_id(candidate) for candidate in embedded]
    parent = {item_id: item_id for item_id in embedded_ids}

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

    for left_index, left in enumerate(embedded):
        for right in embedded[left_index + 1 :]:
            if cosine_similarity(embedding_vector(left), embedding_vector(right)) >= threshold:
                union(candidate_id(left), candidate_id(right))

    grouped: dict[str, list[str]] = defaultdict(list)
    for item_id in embedded_ids:
        grouped[find(item_id)].append(item_id)

    clusters = []
    for index, members in enumerate(sorted(grouped.values(), key=lambda items: (-len(items), items)), 1):
        clusters.append(
            {
                "cluster_id": f"embedding-cluster-{index:04d}",
                "candidate_ids": sorted(members),
            }
        )

    return {
        "schema_version": "embedding_clusters_v1",
        "discovery_only": True,
        "decision_layer_used": False,
        "labels_or_decisions_included": False,
        "similarity": "cosine_similarity_over_precomputed_vectors",
        "threshold": threshold,
        "candidate_count": len(candidates),
        "embedded_candidate_count": len(embedded),
        "skipped_missing_embedding": skipped,
        "clusters": clusters,
        "nearest_neighbors": nearest_neighbors(candidates, top_k=top_k),
        "pairwise_similarity": pairwise_embedding_similarity(candidates),
        "guardrails": {
            "raw_threads_content_included": False,
            "sparse_schema_updated": False,
            "human_decision_made": False,
        },
    }
