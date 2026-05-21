"""Concept graph and evolution heuristics for metadata-only simulations."""

from __future__ import annotations

import itertools
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from src.embedding.encoder import encode
from src.evidence.storage import REPO_ROOT, utc_now
from src.intelligence.yaml_store import write_yaml


CONCEPT_GRAPH_PATH = REPO_ROOT / "data/concept_graph.yaml"


def build_concept_graph(
    concepts: list[dict[str, Any]],
    candidates: list[dict[str, Any]],
    *,
    output_path: Path = CONCEPT_GRAPH_PATH,
) -> dict[str, Any]:
    """Build a metadata-only concept graph from concepts and candidate matches."""
    nodes = [_concept_node(concept) for concept in concepts]
    node_ids = {node["concept_id"] for node in nodes}
    edges: list[dict[str, Any]] = []
    edges.extend(_transition_edges(candidates, node_ids))
    edges.extend(_co_occurrence_edges(candidates, node_ids))
    edges.extend(detect_evolution(concepts))
    graph = {
        "schema_version": "concept_graph_v1",
        "generated_at": utc_now(),
        "nodes": nodes,
        "edges": sorted(edges, key=lambda row: (row["type"], row["source"], row["target"])),
        "summary": _graph_summary(nodes, edges),
        "raw_content_included": False,
    }
    write_yaml(output_path, graph)
    return graph


def detect_evolution(concepts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Detect likely concept evolution edges from similarity plus keyword drift."""
    edges: list[dict[str, Any]] = []
    for left, right in itertools.combinations(concepts, 2):
        source = str(left.get("concept_id", ""))
        target = str(right.get("concept_id", ""))
        if not source or not target or source == target:
            continue
        similarity = _concept_similarity(left, right)
        drift = _keyword_drift(left, right)
        same_signal = left.get("dominant_signal") == right.get("dominant_signal")
        if similarity >= 0.68 and (drift >= 0.25 or same_signal):
            weight = round(min(1.0, (0.65 * similarity) + (0.35 * drift)), 6)
            edges.append(
                {
                    "source": source,
                    "target": target,
                    "type": "evolution",
                    "weight": weight,
                    "embedding_similarity": round(similarity, 6),
                    "keyword_drift": round(drift, 6),
                    "reason": _evolution_reason(left, right, similarity, drift),
                }
            )
    return edges


def _concept_node(concept: dict[str, Any]) -> dict[str, Any]:
    metrics = concept.get("metrics", {}) if isinstance(concept.get("metrics"), dict) else {}
    return {
        "concept_id": concept.get("concept_id"),
        "concept_name": concept.get("concept_name"),
        "risk_level": concept.get("risk_level", "unknown"),
        "dominant_signal": concept.get("dominant_signal"),
        "derived_from_cluster": concept.get("derived_from_cluster"),
        "scam_rate": metrics.get("scam_rate", 0.0),
        "sample_count": metrics.get("sample_count", 0),
    }


def _transition_edges(candidates: list[dict[str, Any]], node_ids: set[str]) -> list[dict[str, Any]]:
    ordered = sorted(candidates, key=lambda item: (item.get("round", 0), item.get("created_at", ""), item.get("candidate_id", "")))
    counts: Counter[tuple[str, str]] = Counter()
    outgoing: Counter[str] = Counter()
    previous: str | None = None
    for candidate in ordered:
        current = _primary_concept_id(candidate)
        if current not in node_ids:
            previous = current
            continue
        if previous and previous in node_ids and previous != current:
            counts[(previous, current)] += 1
            outgoing[previous] += 1
        previous = current

    return [
        {
            "source": source,
            "target": target,
            "type": "transition",
            "weight": round(count / outgoing[source], 6) if outgoing[source] else 0.0,
            "count": count,
        }
        for (source, target), count in counts.items()
    ]


def _co_occurrence_edges(candidates: list[dict[str, Any]], node_ids: set[str]) -> list[dict[str, Any]]:
    counts: Counter[tuple[str, str]] = Counter()
    candidate_total = max(1, len(candidates))
    for candidate in candidates:
        ids = sorted(concept_id for concept_id in _candidate_concept_ids(candidate) if concept_id in node_ids)
        for source, target in itertools.combinations(ids, 2):
            if source != target:
                counts[(source, target)] += 1

    return [
        {
            "source": source,
            "target": target,
            "type": "co_occurrence",
            "weight": round(count / candidate_total, 6),
            "count": count,
        }
        for (source, target), count in counts.items()
    ]


def _candidate_concept_ids(candidate: dict[str, Any]) -> list[str]:
    features = candidate.get("features", {}) if isinstance(candidate.get("features"), dict) else {}
    ids: list[str] = []
    for value in (
        features.get("concept_id"),
        candidate.get("concept_id"),
        candidate.get("matched_concept"),
    ):
        if value:
            ids.append(str(value))
    for key in ("concept_ids", "related_concept_ids"):
        for value in features.get(key, []) or []:
            if value:
                ids.append(str(value))
    return sorted(set(ids))


def _primary_concept_id(candidate: dict[str, Any]) -> str | None:
    features = candidate.get("features", {}) if isinstance(candidate.get("features"), dict) else {}
    for value in (features.get("concept_id"), candidate.get("concept_id"), candidate.get("matched_concept")):
        if value:
            return str(value)
    ids = _candidate_concept_ids(candidate)
    return ids[0] if ids else None


def _concept_similarity(left: dict[str, Any], right: dict[str, Any]) -> float:
    left_text = _concept_text(left)
    right_text = _concept_text(right)
    return _cosine(encode(left_text), encode(right_text))


def _concept_text(concept: dict[str, Any]) -> str:
    keywords = " ".join(str(keyword) for keyword in concept.get("keywords", []))
    return " ".join(
        [
            str(concept.get("concept_name", "")),
            str(concept.get("description", "")),
            str(concept.get("attack_pattern", "")),
            str(concept.get("psychological_hook", "")),
            keywords,
        ]
    )


def _keyword_drift(left: dict[str, Any], right: dict[str, Any]) -> float:
    left_keywords = {str(keyword).lower() for keyword in left.get("keywords", []) if keyword}
    right_keywords = {str(keyword).lower() for keyword in right.get("keywords", []) if keyword}
    if not left_keywords and not right_keywords:
        return 0.0
    overlap = len(left_keywords & right_keywords)
    union = len(left_keywords | right_keywords)
    return 1.0 - (overlap / union if union else 0.0)


def _cosine(left: list[float], right: list[float]) -> float:
    numerator = sum(a * b for a, b in zip(left, right))
    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))
    if left_norm == 0.0 or right_norm == 0.0:
        return 0.0
    return max(0.0, min(1.0, numerator / (left_norm * right_norm)))


def _evolution_reason(left: dict[str, Any], right: dict[str, Any], similarity: float, drift: float) -> str:
    if left.get("dominant_signal") == right.get("dominant_signal"):
        return "Same dominant signal with semantic proximity."
    if drift >= 0.45:
        return "Semantic proximity with visible keyword drift."
    return "Nearby semantic concepts; review as possible mutation."


def _graph_summary(nodes: list[dict[str, Any]], edges: list[dict[str, Any]]) -> dict[str, Any]:
    degree: dict[str, int] = defaultdict(int)
    edge_counts: Counter[str] = Counter()
    for edge in edges:
        degree[str(edge["source"])] += 1
        degree[str(edge["target"])] += 1
        edge_counts[str(edge["type"])] += 1
    central = sorted(degree.items(), key=lambda item: (-item[1], item[0]))[:5]
    return {
        "node_count": len(nodes),
        "edge_count": len(edges),
        "edge_counts": dict(sorted(edge_counts.items())),
        "central_concepts": [{"concept_id": concept_id, "degree": count} for concept_id, count in central],
    }
