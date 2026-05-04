"""Detect discovery gaps between sparse and embedding clusters."""

from __future__ import annotations

from typing import Any

from engine.common import candidate_id, embedding_vector
from engine.embedding.similarity import cosine_similarity


def cluster_map(cluster_output: dict[str, Any]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for cluster in cluster_output.get("clusters", []):
        for item_id in cluster.get("candidate_ids", []):
            mapping[str(item_id)] = str(cluster.get("cluster_id"))
    return mapping


def detect_discrepancies(
    candidates: list[dict[str, Any]],
    sparse_clusters: dict[str, Any],
    embedding_close_threshold: float = 0.85,
    embedding_far_threshold: float = 0.25,
) -> dict[str, Any]:
    sparse_by_candidate = cluster_map(sparse_clusters)
    cases: list[dict[str, Any]] = []
    embedded = [candidate for candidate in candidates if embedding_vector(candidate)]

    for left_index, left in enumerate(embedded):
        for right in embedded[left_index + 1 :]:
            left_id = candidate_id(left)
            right_id = candidate_id(right)
            similarity = cosine_similarity(embedding_vector(left), embedding_vector(right))
            same_sparse = sparse_by_candidate.get(left_id) == sparse_by_candidate.get(right_id)

            if similarity >= embedding_close_threshold and not same_sparse:
                cases.append(
                    {
                        "case_id": f"disc-{len(cases) + 1:04d}",
                        "type": "missed_pattern",
                        "candidate_ids": [left_id, right_id],
                        "embedding_similarity": round(similarity, 6),
                        "sparse_same_cluster": False,
                        "description": "Candidates are close in discovery-only embedding space but not grouped by sparse features; review for a missing explainable feature.",
                    }
                )
            elif same_sparse and similarity <= embedding_far_threshold:
                cases.append(
                    {
                        "case_id": f"disc-{len(cases) + 1:04d}",
                        "type": "over_generalization",
                        "candidate_ids": [left_id, right_id],
                        "embedding_similarity": round(similarity, 6),
                        "sparse_same_cluster": True,
                        "description": "Candidates share a sparse cluster but are far in discovery-only embedding space; review whether the sparse feature is too broad.",
                    }
                )

    return {
        "schema_version": "discrepancy_report_v1",
        "discovery_only": True,
        "embedding_close_threshold": embedding_close_threshold,
        "embedding_far_threshold": embedding_far_threshold,
        "summary": {
            "case_count": len(cases),
            "missed_pattern": sum(1 for case in cases if case["type"] == "missed_pattern"),
            "over_generalization": sum(1 for case in cases if case["type"] == "over_generalization"),
        },
        "cases": cases,
        "guardrails": {
            "raw_threads_content_included": False,
            "embedding_used_for_decision": False,
            "sparse_schema_updated": False,
            "human_review_required_for_changes": True,
        },
    }
