"""Cosine similarity helpers for precomputed discovery-only embeddings."""

from __future__ import annotations

import math
from typing import Any

from engine.common import candidate_id, embedding_vector


def cosine_similarity(left: list[float], right: list[float]) -> float:
    if not left or not right or len(left) != len(right):
        return 0.0
    numerator = sum(a * b for a, b in zip(left, right, strict=True))
    left_norm = math.sqrt(sum(a * a for a in left))
    right_norm = math.sqrt(sum(b * b for b in right))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return numerator / (left_norm * right_norm)


def candidates_with_embeddings(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [candidate for candidate in candidates if embedding_vector(candidate)]


def pairwise_embedding_similarity(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    embedded = candidates_with_embeddings(candidates)
    pairs: list[dict[str, Any]] = []
    for left_index, left in enumerate(embedded):
        for right in embedded[left_index + 1 :]:
            pairs.append(
                {
                    "left": candidate_id(left),
                    "right": candidate_id(right),
                    "cosine_similarity": round(
                        cosine_similarity(embedding_vector(left), embedding_vector(right)),
                        6,
                    ),
                }
            )
    return pairs


def nearest_neighbors(candidates: list[dict[str, Any]], top_k: int = 3) -> list[dict[str, Any]]:
    embedded = candidates_with_embeddings(candidates)
    rows: list[dict[str, Any]] = []
    for candidate in embedded:
        neighbors = []
        for other in embedded:
            if candidate_id(other) == candidate_id(candidate):
                continue
            neighbors.append(
                {
                    "candidate_id": candidate_id(other),
                    "cosine_similarity": round(
                        cosine_similarity(embedding_vector(candidate), embedding_vector(other)),
                        6,
                    ),
                }
            )
        rows.append(
            {
                "candidate_id": candidate_id(candidate),
                "neighbors": sorted(neighbors, key=lambda row: -row["cosine_similarity"])[:top_k],
            }
        )
    return rows
