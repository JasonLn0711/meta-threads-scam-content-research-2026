"""Dependency-light KMeans-style clustering for local embeddings."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .encoder import euclidean_distance


_LAST_MODEL: "ClusterModel | None" = None


@dataclass
class ClusterModel:
    centers: list[list[float]]
    assignments: list[int]
    counts: list[int]

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": "cluster_model_v1",
            "algorithm": "deterministic_kmeans",
            "centers": self.centers,
            "assignments": self.assignments,
            "counts": self.counts,
        }


def fit_clusters(
    embeddings: list[list[float]],
    *,
    cluster_count: int | None = None,
    max_iterations: int = 12,
) -> ClusterModel:
    """Fit a small deterministic KMeans model over embeddings."""
    global _LAST_MODEL
    if not embeddings:
        raise ValueError("fit_clusters requires at least one embedding")
    _validate_embeddings(embeddings)

    k = cluster_count or min(4, max(1, int(len(embeddings) ** 0.5)))
    k = max(1, min(k, len(embeddings)))
    centers = [list(embeddings[index]) for index in _initial_center_indices(embeddings, k)]
    assignments = [0] * len(embeddings)

    for _ in range(max_iterations):
        changed = False
        for index, embedding in enumerate(embeddings):
            cluster_index = _nearest_center_index(embedding, centers)
            if assignments[index] != cluster_index:
                changed = True
            assignments[index] = cluster_index
        centers = _recompute_centers(embeddings, assignments, centers)
        if not changed:
            break

    counts = [assignments.count(index) for index in range(k)]
    _LAST_MODEL = ClusterModel(centers=centers, assignments=assignments, counts=counts)
    return _LAST_MODEL


def assign_cluster(embedding: list[float], model: ClusterModel | None = None) -> dict[str, Any]:
    """Assign one embedding to the nearest cluster center."""
    model = model or _LAST_MODEL
    if model is None:
        raise ValueError("assign_cluster requires a fitted model")
    cluster_index = _nearest_center_index(embedding, model.centers)
    distance = euclidean_distance(embedding, model.centers[cluster_index])
    return {
        "cluster_id": f"C{cluster_index:02d}",
        "cluster_index": cluster_index,
        "embedding_distance": round(distance, 6),
    }


def _initial_center_indices(embeddings: list[list[float]], k: int) -> list[int]:
    if k == 1:
        return [0]
    step = max(1, len(embeddings) // k)
    indices = [min(index * step, len(embeddings) - 1) for index in range(k)]
    return sorted(set(indices))[:k]


def _nearest_center_index(embedding: list[float], centers: list[list[float]]) -> int:
    return min(range(len(centers)), key=lambda index: euclidean_distance(embedding, centers[index]))


def _recompute_centers(
    embeddings: list[list[float]],
    assignments: list[int],
    old_centers: list[list[float]],
) -> list[list[float]]:
    dim = len(embeddings[0])
    new_centers: list[list[float]] = []
    for cluster_index in range(len(old_centers)):
        members = [embedding for embedding, assignment in zip(embeddings, assignments) if assignment == cluster_index]
        if not members:
            new_centers.append(old_centers[cluster_index])
            continue
        center = [sum(member[axis] for member in members) / len(members) for axis in range(dim)]
        new_centers.append([round(value, 8) for value in center])
    return new_centers


def _validate_embeddings(embeddings: list[list[float]]) -> None:
    dim = len(embeddings[0])
    if dim == 0:
        raise ValueError("embeddings must be non-empty vectors")
    for embedding in embeddings:
        if len(embedding) != dim:
            raise ValueError("all embeddings must have the same dimension")
