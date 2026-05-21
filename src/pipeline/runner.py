"""Advanced synthetic discovery loop with embeddings and contextual bandits."""

from __future__ import annotations

import json
import random
import uuid
from collections import defaultdict
from pathlib import Path
from typing import Any

from src.bandit.contextual_bandit import ContextualBandit
from src.concepts.builder import extract_keywords, generate_concept, store_concept
from src.concepts.matcher import match_concept
from src.discovery.connector import fetch_candidates
from src.discovery.query_llm import generate_queries
from src.embedding.clustering import assign_cluster, fit_clusters
from src.embedding.encoder import detect_language, encode
from src.evidence.ingestion import ingest_evidence
from src.evidence.storage import REPO_ROOT, utc_now
from src.intelligence.adversarial import detect_adversarial_patterns
from src.intelligence.graph import build_concept_graph
from src.intelligence.temporal import track_concept_over_time
from src.learning.metrics import compute_reward, simulate_review, summarize_results
from src.prediction.logging import PREDICTED_VARIANTS_LOG, append_jsonl, reset_prediction_logs
from src.prediction.mutation import mutate_concept
from src.prediction.scoring import score_simulation
from src.prediction.simulation import generate_simulated_posts
from src.prediction.validation import track_prediction_validation
from src.selfplay.runner import load_selfplay_priorities


ADVANCED_STATE_DIR = REPO_ROOT / "data/learning_state"
ADVANCED_BANDIT_PATH = ADVANCED_STATE_DIR / "advanced_contextual_bandit_state.json"
ADVANCED_METRICS_PATH = ADVANCED_STATE_DIR / "advanced_metrics.json"
ADVANCED_ROUNDS_PATH = ADVANCED_STATE_DIR / "advanced_rounds.jsonl"


def run_round(
    *,
    round_number: int,
    bandit: ContextualBandit,
    query_count: int = 6,
    top_k: int = 5,
    seed: int = 20260505,
) -> dict[str, Any]:
    history = load_metrics()
    query_context = build_query_context(history)
    queries = generate_queries(query_context, count=query_count)
    raw_items = _fetch_query_items(queries)
    embeddings = [encode(item["raw_text"]) for item in raw_items]
    cluster_model = fit_clusters(embeddings)
    cluster_assignments = [assign_cluster(embedding, cluster_model) for embedding in embeddings]
    cluster_prior = _cluster_prior(history)
    concepts = _build_concepts_for_round(raw_items, cluster_assignments, cluster_prior)

    candidates: list[dict[str, Any]] = []
    for item, cluster in zip(raw_items, cluster_assignments):
        evidence = ingest_evidence(
            item["raw_text"],
            {
                "source": "synthetic_llm_mock_threads",
                "query_id": item["query_id"],
                "strategy": item["strategy"],
                "mock_item_id": item["mock_item_id"],
                "round": round_number,
            },
            actor="advanced_discovery_runner",
        )
        concept_match = match_concept(str(item["raw_text"]), concepts, log=True)
        features = build_candidate_features(
            item,
            cluster=cluster,
            cluster_scam_rate=cluster_prior.get(cluster["cluster_id"], 0.0),
            concept_match=concept_match,
            intelligence_context=_intelligence_context_for_match(history, concept_match),
        )
        candidate_id = _candidate_id(round_number, item, evidence["sha256"])
        candidate = {
            "schema_version": "advanced_candidate_v2",
            "candidate_id": candidate_id,
            "created_at": utc_now(),
            "round": round_number,
            "query_id": item["query_id"],
            "strategy": item["strategy"],
            "expected_signal": item["expected_signal"],
            "evidence_ref": {
                "evidence_id": evidence["evidence_id"],
                "hash_algorithm": "sha256",
                "sha256": evidence["sha256"],
            },
            "features": features,
            "score": score_advanced_candidate(features),
            "raw_content_included": False,
            "human_decision_required": True,
        }
        candidates.append(candidate)

    selected = select_top_k_with_bandit(candidates, bandit, top_k=top_k)
    rng = random.Random(seed + round_number)
    review_results = [simulate_review(candidate, rng) for candidate in selected]
    _update_bandit_from_reviews(selected, review_results, bandit)
    summary = summarize_results(review_results)
    reviewed_candidates = _attach_review_results(selected, review_results)
    dynamic_intelligence = _build_dynamic_intelligence(concepts, candidates, reviewed_candidates, round_number)

    round_record = {
        "schema_version": "advanced_discovery_round_v1",
        "round": round_number,
        "queries": queries,
        "query_context": query_context,
        "candidate_count": len(candidates),
        "selected_count": len(selected),
        "selected_candidates": [_metadata_only_candidate(candidate) for candidate in selected],
        "cluster_model": cluster_model.to_dict(),
        "review_results": review_results,
        "summary": summary,
        "query_performance": _performance_by_key(review_results, selected, "query_id"),
        "cluster_performance": _performance_by_key(review_results, selected, "cluster_id"),
        "concepts": concepts,
        "concept_match_results": [candidate["features"]["concept_match"] for candidate in candidates],
        "concept_performance": _performance_by_key(review_results, selected, "concept_id"),
        "dynamic_intelligence": dynamic_intelligence,
        "bandit_state_after_round": bandit.to_state(),
    }
    persist_round(round_record, bandit)
    return round_record


def run_rounds(
    *,
    rounds: int,
    query_count: int = 6,
    top_k: int = 5,
    alpha: float = 0.8,
    seed: int = 20260505,
    reset: bool = False,
) -> list[dict[str, Any]]:
    if rounds < 1:
        raise ValueError("rounds must be at least 1")
    if reset:
        reset_advanced_state()
    bandit = ContextualBandit.load(ADVANCED_BANDIT_PATH, alpha=alpha, reset=reset)
    start_round = _next_round_number()
    records = []
    for offset in range(rounds):
        records.append(
            run_round(
                round_number=start_round + offset,
                bandit=bandit,
                query_count=query_count,
                top_k=top_k,
                seed=seed,
            )
        )
    return records


def build_query_context(metrics: dict[str, Any]) -> dict[str, Any]:
    cluster_rows = list(metrics.get("cluster_performance", {}).values())
    top_clusters = sorted(cluster_rows, key=lambda row: row.get("reward", 0.0), reverse=True)[:3]
    failed_clusters = [row for row in cluster_rows if float(row.get("reward", 0.0) or 0.0) == 0.0][:3]
    return {
        "recent_performance": {
            "top_reward": metrics.get("reward_trend", [])[-1] if metrics.get("reward_trend") else 0.0,
            "round_count": len(metrics.get("rounds", [])),
        },
        "top_clusters": top_clusters,
        "failed_clusters": failed_clusters,
        "top_concepts": _top_concepts(metrics),
        "dynamic_intelligence": metrics.get("dynamic_intelligence", {}),
        "exploration_priorities": metrics.get("exploration_priorities", []),
        "predicted_variants": metrics.get("prediction_priorities", []),
        "selfplay_priorities": metrics.get("selfplay_priorities", []) or load_selfplay_priorities(),
        "language_distribution": metrics.get("language_distribution", {"zh-Hant": 1.0}),
        "high_signal_features": _top_signals(metrics),
    }


def build_candidate_features(
    item: dict[str, Any],
    *,
    cluster: dict[str, Any],
    cluster_scam_rate: float,
    concept_match: dict[str, Any] | None = None,
    intelligence_context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    signal = str(item.get("expected_signal", ""))
    concept_match = concept_match or {}
    intelligence_context = intelligence_context or {}
    query_priority = float(item.get("query_exploration_priority", 0.0) or 0.0)
    predictive_risk = round(float(item.get("predictive_risk_score", 0.0) or 0.0), 6)
    selfplay_reward = round(float(item.get("selfplay_reward_signal", 0.0) or 0.0), 6)
    selfplay_detector_confidence = round(float(item.get("selfplay_detector_confidence", 0.0) or 0.0), 6)
    concept_confidence = round(float(concept_match.get("confidence", 0.0) or 0.0), 6)
    related_concepts = concept_match.get("related_concepts", []) or []
    related_concept_ids = [
        str(related["concept_id"])
        for related in related_concepts
        if related.get("concept_id") and related.get("concept_id") != concept_match.get("matched_concept")
    ]
    return {
        "cluster_id": cluster["cluster_id"],
        "cluster_scam_rate": round(float(cluster_scam_rate), 6),
        "embedding_distance": cluster["embedding_distance"],
        "language": detect_language(str(item.get("raw_text", ""))),
        "concept_id": concept_match.get("matched_concept"),
        "concept_name": concept_match.get("matched_concept_name"),
        "concept_dominant_signal": concept_match.get("dominant_signal"),
        "concept_confidence": concept_confidence,
        "concept_risk_level": concept_match.get("risk_level", "unknown"),
        "is_novel_concept": bool(concept_match.get("is_novel", True)),
        "related_concept_ids": related_concept_ids,
        "concept_match": {
            "matched_concept": concept_match.get("matched_concept"),
            "matched_concept_name": concept_match.get("matched_concept_name"),
            "dominant_signal": concept_match.get("dominant_signal"),
            "confidence": concept_confidence,
            "reasoning": concept_match.get("reasoning", ""),
            "is_novel": bool(concept_match.get("is_novel", True)),
            "related_concepts": related_concepts[:4],
        },
        "concept_graph_degree": round(float(intelligence_context.get("concept_graph_degree", 0.0) or 0.0), 6),
        "concept_growth": round(float(intelligence_context.get("concept_growth", 0.0) or 0.0), 6),
        "evolution_priority": round(float(intelligence_context.get("evolution_priority", 0.0) or 0.0), 6),
        "adversarial_priority": round(float(intelligence_context.get("adversarial_priority", 0.0) or 0.0), 6),
        "exploration_priority": round(
            max(float(intelligence_context.get("exploration_priority", 0.0) or 0.0), query_priority),
            6,
        ),
        "source_concept_id": item.get("source_concept_id"),
        "predicted_variant_id": item.get("source_variant_id"),
        "prediction_evasion_type": item.get("prediction_evasion_type"),
        "predictive_risk_score": predictive_risk,
        "selfplay_variant_id": item.get("selfplay_variant_id"),
        "selfplay_evasion_characteristic": item.get("selfplay_evasion_characteristic"),
        "selfplay_reward_signal": selfplay_reward,
        "selfplay_detector_confidence": selfplay_detector_confidence,
        "expected_signal": signal,
        "exploration": bool(item.get("exploration")),
        "guaranteed_return": signal == "guaranteed_return",
        "off_platform_contact": signal == "off_platform_contact",
        "impersonation": signal == "authority_impersonation",
        "urgency": signal == "urgency",
        "hard_negative_warning": signal == "hard_negative_warning",
    }


def score_advanced_candidate(features: dict[str, Any]) -> float:
    base = 0.15 + (0.55 * float(features.get("cluster_scam_rate", 0.0) or 0.0))
    base += 0.25 if features.get("guaranteed_return") else 0.0
    base += 0.18 if features.get("off_platform_contact") else 0.0
    base += 0.16 if features.get("impersonation") else 0.0
    base += 0.08 if features.get("urgency") else 0.0
    base -= 0.45 if features.get("hard_negative_warning") else 0.0
    concept_confidence = float(features.get("concept_confidence", 0.0) or 0.0)
    if features.get("concept_risk_level") == "high":
        base += 0.18 * concept_confidence
    elif features.get("concept_risk_level") == "medium":
        base += 0.10 * concept_confidence
    if features.get("is_novel_concept"):
        base -= 0.08
    base += 0.06 * float(features.get("exploration_priority", 0.0) or 0.0)
    base += 0.08 * float(features.get("predictive_risk_score", 0.0) or 0.0)
    base += 0.05 * float(features.get("selfplay_reward_signal", 0.0) or 0.0)
    base -= min(0.25, 0.12 * float(features.get("embedding_distance", 0.0) or 0.0))
    return round(max(0.0, min(1.0, base)), 6)


def select_top_k_with_bandit(
    candidates: list[dict[str, Any]],
    bandit: ContextualBandit,
    *,
    top_k: int,
) -> list[dict[str, Any]]:
    pool = list(candidates)
    selected: list[dict[str, Any]] = []
    while pool and len(selected) < top_k:
        context_list = [_candidate_context(candidate) for candidate in pool]
        selected_context = bandit.select(context_list)
        candidate_id = selected_context["candidate_id"]
        index = next(index for index, candidate in enumerate(pool) if candidate["candidate_id"] == candidate_id)
        candidate = pool.pop(index)
        candidate["bandit_score"] = selected_context["bandit_score"]
        selected.append(candidate)
    return selected


def persist_round(round_record: dict[str, Any], bandit: ContextualBandit) -> None:
    ADVANCED_STATE_DIR.mkdir(parents=True, exist_ok=True)
    bandit.save(ADVANCED_BANDIT_PATH)
    metrics = load_metrics()
    metrics["rounds"].append(
        {
            "round": round_record["round"],
            "reward": round_record["summary"]["reward_high_value_per_reviewer_hour"],
            "scam_count": round_record["summary"]["scam_count"],
            "reviewed_count": round_record["summary"]["reviewed_count"],
            "total_review_minutes": round_record["summary"]["total_review_minutes"],
        }
    )
    metrics["reward_trend"].append(round_record["summary"]["reward_high_value_per_reviewer_hour"])
    metrics["query_performance"] = _merge_performance(metrics.get("query_performance", {}), round_record["query_performance"])
    metrics["cluster_performance"] = _merge_performance(
        metrics.get("cluster_performance", {}),
        round_record["cluster_performance"],
    )
    metrics["concept_performance"] = _merge_performance(
        metrics.get("concept_performance", {}),
        round_record["concept_performance"],
    )
    metrics["dynamic_intelligence"] = round_record["dynamic_intelligence"]
    metrics["exploration_priorities"] = _exploration_priorities(round_record["dynamic_intelligence"])
    metrics["prediction_priorities"] = _prediction_priorities(round_record["dynamic_intelligence"])
    metrics["selfplay_priorities"] = load_selfplay_priorities()
    metrics["language_distribution"] = _language_distribution(round_record["selected_candidates"])
    ADVANCED_METRICS_PATH.write_text(
        json.dumps(metrics, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    with ADVANCED_ROUNDS_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(round_record, ensure_ascii=False, sort_keys=True) + "\n")


def load_metrics() -> dict[str, Any]:
    if not ADVANCED_METRICS_PATH.exists():
        return {
            "schema_version": "advanced_discovery_metrics_v1",
            "rounds": [],
            "reward_trend": [],
            "query_performance": {},
            "cluster_performance": {},
            "concept_performance": {},
            "dynamic_intelligence": {},
            "exploration_priorities": [],
            "prediction_priorities": [],
            "selfplay_priorities": [],
            "language_distribution": {"zh-Hant": 1.0},
        }
    return json.loads(ADVANCED_METRICS_PATH.read_text(encoding="utf-8"))


def reset_advanced_state() -> None:
    for path in (ADVANCED_BANDIT_PATH, ADVANCED_METRICS_PATH, ADVANCED_ROUNDS_PATH):
        path.unlink(missing_ok=True)
    concepts_dir = REPO_ROOT / "data/concepts"
    if concepts_dir.exists():
        for pattern in (
            "concept_*.json",
            "concept_evolution.jsonl",
            "match_results.jsonl",
            "reasoning_trace.jsonl",
            "new_cluster_pool.jsonl",
        ):
            for path in concepts_dir.glob(pattern):
                path.unlink(missing_ok=True)
    for path in (
        REPO_ROOT / "data/concept_graph.yaml",
        REPO_ROOT / "data/concept_time_series.yaml",
        REPO_ROOT / "data/adversarial_patterns.yaml",
    ):
        path.unlink(missing_ok=True)
    reset_prediction_logs()


def _fetch_query_items(queries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for query in queries:
        for item in fetch_candidates(query):
            merged = dict(item)
            merged.update(
                {
                    "query_id": query["query_id"],
                    "query_string": query["query_string"],
                    "expected_signal": query["expected_signal"],
                    "exploration": query["exploration"],
                    "source_concept_id": query.get("concept_id"),
                    "source_variant_id": query.get("variant_id"),
                    "prediction_evasion_type": query.get("evasion_type"),
                    "predictive_risk_score": query.get("predictive_risk_score", 0.0),
                    "selfplay_variant_id": query.get("selfplay_variant_id"),
                    "selfplay_evasion_characteristic": query.get("selfplay_evasion_characteristic"),
                    "selfplay_reward_signal": query.get("selfplay_reward_signal", 0.0),
                    "selfplay_detector_confidence": query.get("selfplay_detector_confidence", 0.0),
                    "query_exploration_priority": query.get("exploration_priority", 0.0),
                }
            )
            items.append(merged)
    return items


def _candidate_id(round_number: int, item: dict[str, Any], sha256: str) -> str:
    material = json.dumps(
        {
            "round": round_number,
            "query_id": item.get("query_id"),
            "mock_item_id": item.get("mock_item_id"),
            "sha256": sha256,
        },
        ensure_ascii=False,
        sort_keys=True,
    )
    return f"advanced_candidate_{uuid.uuid5(uuid.NAMESPACE_URL, material)}"


def _candidate_context(candidate: dict[str, Any]) -> dict[str, Any]:
    features = candidate["features"]
    return {
        "candidate_id": candidate["candidate_id"],
        "query_id": candidate["query_id"],
        "cluster_id": features["cluster_id"],
        "cluster_scam_rate": features["cluster_scam_rate"],
        "embedding_distance": features["embedding_distance"],
        "language": features["language"],
        "concept_id": features.get("concept_id"),
        "concept_dominant_signal": features.get("concept_dominant_signal"),
        "concept_confidence": features.get("concept_confidence", 0.0),
        "concept_risk_level": features.get("concept_risk_level", "unknown"),
        "is_novel_concept": features.get("is_novel_concept", True),
        "concept_graph_degree": features.get("concept_graph_degree", 0.0),
        "concept_growth": features.get("concept_growth", 0.0),
        "evolution_priority": features.get("evolution_priority", 0.0),
        "adversarial_priority": features.get("adversarial_priority", 0.0),
        "exploration_priority": features.get("exploration_priority", 0.0),
        "predicted_variant_id": features.get("predicted_variant_id"),
        "prediction_evasion_type": features.get("prediction_evasion_type"),
        "predictive_risk_score": features.get("predictive_risk_score", 0.0),
        "selfplay_variant_id": features.get("selfplay_variant_id"),
        "selfplay_evasion_characteristic": features.get("selfplay_evasion_characteristic"),
        "selfplay_reward_signal": features.get("selfplay_reward_signal", 0.0),
        "selfplay_detector_confidence": features.get("selfplay_detector_confidence", 0.0),
        "expected_signal": features["expected_signal"],
        "exploration": features["exploration"],
    }


def _update_bandit_from_reviews(
    selected: list[dict[str, Any]],
    review_results: list[dict[str, Any]],
    bandit: ContextualBandit,
) -> None:
    by_id = {candidate["candidate_id"]: candidate for candidate in selected}
    for result in review_results:
        candidate = by_id[result["candidate_id"]]
        reward = _individual_reward(result)
        bandit.update(_candidate_context(candidate), reward)


def _individual_reward(result: dict[str, Any]) -> float:
    minutes = float(result.get("review_minutes", 0.0) or 0.0)
    if minutes <= 0 or result.get("decision") != "scam":
        return 0.0
    return round(1.0 / (minutes / 60.0), 6)


def _metadata_only_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    return {
        "candidate_id": candidate["candidate_id"],
        "query_id": candidate["query_id"],
        "strategy": candidate["strategy"],
        "expected_signal": candidate["expected_signal"],
        "evidence_ref": candidate["evidence_ref"],
        "features": candidate["features"],
        "score": candidate["score"],
        "bandit_score": candidate.get("bandit_score", {}),
        "raw_content_included": False,
    }


def _performance_by_key(
    review_results: list[dict[str, Any]],
    selected: list[dict[str, Any]],
    key: str,
) -> dict[str, dict[str, Any]]:
    candidates = {candidate["candidate_id"]: candidate for candidate in selected}
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for result in review_results:
        candidate = candidates[result["candidate_id"]]
        if key in {"cluster_id", "concept_id"}:
            value = candidate["features"].get(key) or "novel_concept_pool"
        else:
            value = candidate[key]
        grouped[str(value)].append(result)

    performance: dict[str, dict[str, Any]] = {}
    for value, results in grouped.items():
        total_minutes = round(sum(float(result["review_minutes"]) for result in results), 3)
        scam_count = sum(1 for result in results if result["decision"] == "scam")
        reviewed_count = len(results)
        performance[value] = {
            "id": value,
            "reviewed_count": reviewed_count,
            "scam_count": scam_count,
            "review_minutes": total_minutes,
            "scam_rate": round(scam_count / reviewed_count, 6) if reviewed_count else 0.0,
            "reward": compute_reward(results),
        }
        if key == "query_id":
            performance[value]["expected_signal"] = candidates[results[0]["candidate_id"]]["expected_signal"]
        if key == "concept_id":
            first_candidate = candidates[results[0]["candidate_id"]]
            performance[value]["concept_risk_level"] = first_candidate["features"].get("concept_risk_level", "unknown")
            performance[value]["concept_name"] = first_candidate["features"].get("concept_name")
            performance[value]["dominant_signal"] = first_candidate["features"].get("concept_dominant_signal")
    return performance


def _merge_performance(
    existing: dict[str, dict[str, Any]],
    new: dict[str, dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    merged = {key: dict(value) for key, value in existing.items()}
    for key, row in new.items():
        current = merged.get(
            key,
            {"id": key, "reviewed_count": 0, "scam_count": 0, "review_minutes": 0.0, "scam_rate": 0.0, "reward": 0.0},
        )
        reviewed = int(current["reviewed_count"]) + int(row["reviewed_count"])
        scam_count = int(current["scam_count"]) + int(row["scam_count"])
        minutes = round(float(current["review_minutes"]) + float(row["review_minutes"]), 3)
        merged[key] = {
            "id": key,
            "reviewed_count": reviewed,
            "scam_count": scam_count,
            "review_minutes": minutes,
            "scam_rate": round(scam_count / reviewed, 6) if reviewed else 0.0,
            "reward": round(scam_count / (minutes / 60.0), 6) if minutes > 0 else 0.0,
        }
        if row.get("expected_signal") or current.get("expected_signal"):
            merged[key]["expected_signal"] = row.get("expected_signal") or current.get("expected_signal")
        if row.get("concept_risk_level") or current.get("concept_risk_level"):
            merged[key]["concept_risk_level"] = row.get("concept_risk_level") or current.get("concept_risk_level")
        if row.get("concept_name") or current.get("concept_name"):
            merged[key]["concept_name"] = row.get("concept_name") or current.get("concept_name")
        if row.get("dominant_signal") or current.get("dominant_signal"):
            merged[key]["dominant_signal"] = row.get("dominant_signal") or current.get("dominant_signal")
    return merged


def _cluster_prior(metrics: dict[str, Any]) -> dict[str, float]:
    return {
        cluster_id: float(row.get("scam_rate", 0.0) or 0.0)
        for cluster_id, row in metrics.get("cluster_performance", {}).items()
    }


def _build_concepts_for_round(
    raw_items: list[dict[str, Any]],
    cluster_assignments: list[dict[str, Any]],
    cluster_prior: dict[str, float],
) -> list[dict[str, Any]]:
    samples_by_cluster: dict[str, list[str]] = defaultdict(list)
    for item, cluster in zip(raw_items, cluster_assignments):
        samples_by_cluster[str(cluster["cluster_id"])].append(str(item.get("raw_text", "")))

    concepts: list[dict[str, Any]] = []
    for cluster_id, samples in sorted(samples_by_cluster.items()):
        concept = generate_concept(
            {
                "cluster_id": cluster_id,
                "samples": samples[:8],
                "keywords": extract_keywords(samples),
                "scam_rate": cluster_prior.get(cluster_id, 0.0),
            }
        )
        store_concept(concept)
        concepts.append(concept)
    return concepts


def _build_dynamic_intelligence(
    concepts: list[dict[str, Any]],
    candidates: list[dict[str, Any]],
    reviewed_candidates: list[dict[str, Any]],
    round_number: int,
) -> dict[str, Any]:
    graph = build_concept_graph(concepts, candidates)
    time_series = track_concept_over_time(concepts, _concept_events(reviewed_candidates, round_number))
    adversarial = detect_adversarial_patterns(reviewed_candidates)
    priorities = _concept_priorities(graph, time_series, adversarial)
    predictive = _build_predictive_simulation(concepts, reviewed_candidates, round_number, priorities)
    return {
        "schema_version": "dynamic_intelligence_v1",
        "generated_at": utc_now(),
        "concept_graph_summary": graph["summary"],
        "concept_time_series_summary": time_series["summary"],
        "adversarial_summary": adversarial["summary"],
        "evolution_edges": [edge for edge in graph["edges"] if edge["type"] == "evolution"][:10],
        "adversarial_findings": adversarial["findings"][:10],
        "concept_priorities": priorities,
        "predictive_simulation": predictive,
        "raw_content_included": False,
    }


def _build_predictive_simulation(
    concepts: list[dict[str, Any]],
    observed_candidates: list[dict[str, Any]],
    round_number: int,
    concept_priorities: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    selected_concepts = _concepts_for_prediction(concepts, concept_priorities)
    variants: list[dict[str, Any]] = []
    for concept in selected_concepts:
        count = 1 if concept.get("risk_level") == "low" else 2
        for variant in mutate_concept(concept, count=count):
            variant["origin_round"] = round_number
            append_jsonl(PREDICTED_VARIANTS_LOG, variant)
            variants.append(variant)

    simulated_posts = generate_simulated_posts(variants, log=True)
    concept_lookup = {str(concept.get("concept_id")): concept for concept in selected_concepts}
    scores = []
    for post in simulated_posts:
        concept = concept_lookup.get(str(post.get("origin_concept_id")))
        if not concept:
            continue
        scores.append(score_simulation(post, concept, log=True))
    validation = track_prediction_validation(variants, observed_candidates, current_round=round_number, log=True)
    scored_variants = _merge_prediction_scores(variants, simulated_posts, scores)
    top_predictions = sorted(scored_variants, key=lambda row: (-float(row.get("risk_score", 0.0)), row["variant_id"]))[:6]
    return {
        "schema_version": "predictive_simulation_v1",
        "generated_at": utc_now(),
        "variant_count": len(variants),
        "simulated_post_count": len(simulated_posts),
        "top_predicted_variants": top_predictions,
        "validation_summary": validation["summary"],
        "validation_results": validation["results"][:10],
        "raw_content_included": False,
    }


def _concepts_for_prediction(
    concepts: list[dict[str, Any]],
    concept_priorities: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    def rank(concept: dict[str, Any]) -> tuple[float, float, str]:
        concept_id = str(concept.get("concept_id") or "")
        priority = concept_priorities.get(concept_id, {})
        risk_boost = {"high": 0.25, "medium": 0.12, "low": 0.0}.get(str(concept.get("risk_level", "low")), 0.0)
        score = float(priority.get("exploration_priority", 0.0) or 0.0) + risk_boost
        return (-score, -float(concept.get("metrics", {}).get("scam_rate", 0.0) or 0.0), concept_id)

    return sorted(concepts, key=rank)[:4]


def _merge_prediction_scores(
    variants: list[dict[str, Any]],
    simulated_posts: list[dict[str, Any]],
    scores: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    posts_by_variant = {str(post.get("variant_id")): post for post in simulated_posts}
    scores_by_variant = {str(score.get("variant_id")): score for score in scores}
    merged = []
    for variant in variants:
        variant_id = str(variant["variant_id"])
        score = scores_by_variant.get(variant_id, {})
        post = posts_by_variant.get(variant_id, {})
        merged.append(
            {
                "variant_id": variant_id,
                "origin_concept_id": variant.get("origin_concept_id"),
                "origin_concept_name": variant.get("origin_concept_name"),
                "origin_dominant_signal": variant.get("origin_dominant_signal"),
                "variant_name": variant.get("variant_name"),
                "evasion_type": variant.get("evasion_type"),
                "search_query": variant.get("search_query"),
                "risk_score": score.get("risk_score", 0.0),
                "embedding_similarity": score.get("embedding_similarity", 0.0),
                "novelty_score": score.get("novelty_score", 0.0),
                "simulation_id": post.get("simulation_id"),
                "simulated": True,
            }
        )
    return merged


def _attach_review_results(
    selected: list[dict[str, Any]],
    review_results: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    by_id = {result["candidate_id"]: result for result in review_results}
    reviewed = []
    for candidate in selected:
        result = by_id.get(candidate["candidate_id"], {})
        row = _metadata_only_candidate(candidate)
        row["round"] = candidate.get("round")
        row["created_at"] = candidate.get("created_at")
        row["review_decision"] = result.get("decision")
        row["review_minutes"] = result.get("review_minutes")
        row["high_value"] = result.get("high_value", False)
        reviewed.append(row)
    return reviewed


def _concept_events(reviewed_candidates: list[dict[str, Any]], round_number: int) -> list[dict[str, Any]]:
    events = []
    for candidate in reviewed_candidates:
        features = candidate.get("features", {})
        concept_id = features.get("concept_id") or "novel_concept_pool"
        events.append(
            {
                "concept_id": concept_id,
                "timestamp": candidate.get("created_at", ""),
                "period": f"round_{round_number:04d}",
                "decision": candidate.get("review_decision"),
                "high_value": candidate.get("high_value", False),
            }
        )
    return events


def _concept_priorities(
    graph: dict[str, Any],
    time_series: dict[str, Any],
    adversarial: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    priorities: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
    node_lookup = {str(node.get("concept_id")): node for node in graph.get("nodes", [])}
    max_degree = max(
        [row.get("degree", 0) for row in graph.get("summary", {}).get("central_concepts", [])] or [1]
    )
    for row in graph.get("summary", {}).get("central_concepts", []):
        concept_id = str(row.get("concept_id"))
        priorities[concept_id]["concept_graph_degree"] = round(float(row.get("degree", 0)) / max_degree, 6)

    for edge in graph.get("edges", []):
        if edge.get("type") != "evolution":
            continue
        for concept_id in (str(edge.get("source")), str(edge.get("target"))):
            priorities[concept_id]["evolution_priority"] = max(
                priorities[concept_id]["evolution_priority"],
                float(edge.get("weight", 0.0) or 0.0),
            )

    for concept in time_series.get("concepts", []):
        rows = concept.get("time_series", [])
        if rows:
            growth = max(0.0, min(1.0, float(rows[-1].get("growth", 0.0) or 0.0)))
            priorities[str(concept.get("concept_id"))]["concept_growth"] = growth

    for finding in adversarial.get("findings", []):
        concept_id = str(finding.get("concept_id") or "novel_concept_pool")
        priorities[concept_id]["adversarial_priority"] = max(
            priorities[concept_id]["adversarial_priority"],
            float(finding.get("severity", 0.0) or 0.0),
        )

    normalized = {}
    for concept_id, row in priorities.items():
        graph_degree = float(row.get("concept_graph_degree", 0.0))
        growth = float(row.get("concept_growth", 0.0))
        evolution = float(row.get("evolution_priority", 0.0))
        adversarial_priority = float(row.get("adversarial_priority", 0.0))
        exploration_priority = min(
            1.0,
            (0.25 * graph_degree) + (0.25 * growth) + (0.25 * evolution) + (0.25 * adversarial_priority),
        )
        normalized[concept_id] = {
            "concept_name": node_lookup.get(concept_id, {}).get("concept_name"),
            "dominant_signal": node_lookup.get(concept_id, {}).get("dominant_signal"),
            "concept_graph_degree": round(graph_degree, 6),
            "concept_growth": round(growth, 6),
            "evolution_priority": round(evolution, 6),
            "adversarial_priority": round(adversarial_priority, 6),
            "exploration_priority": round(exploration_priority, 6),
        }
    return dict(sorted(normalized.items()))


def _intelligence_context_for_match(metrics: dict[str, Any], concept_match: dict[str, Any]) -> dict[str, Any]:
    concept_id = concept_match.get("matched_concept") or "novel_concept_pool"
    priorities = metrics.get("dynamic_intelligence", {}).get("concept_priorities", {})
    return dict(priorities.get(concept_id, {}))


def _exploration_priorities(dynamic_intelligence: dict[str, Any]) -> list[dict[str, Any]]:
    priorities = dynamic_intelligence.get("concept_priorities", {})
    rows = [
        {"concept_id": concept_id, **values}
        for concept_id, values in priorities.items()
        if float(values.get("exploration_priority", 0.0) or 0.0) > 0.0
    ]
    return sorted(rows, key=lambda row: (-float(row["exploration_priority"]), row["concept_id"]))[:5]


def _prediction_priorities(dynamic_intelligence: dict[str, Any]) -> list[dict[str, Any]]:
    predictions = dynamic_intelligence.get("predictive_simulation", {}).get("top_predicted_variants", [])
    rows = [
        prediction
        for prediction in predictions
        if float(prediction.get("risk_score", 0.0) or 0.0) > 0.0
    ]
    return sorted(rows, key=lambda row: (-float(row["risk_score"]), str(row["variant_id"])))[:5]


def _top_concepts(metrics: dict[str, Any]) -> list[dict[str, Any]]:
    concept_rows = [
        row
        for row in metrics.get("concept_performance", {}).values()
        if row.get("id") and row.get("id") != "novel_concept_pool"
    ]
    top_rows = sorted(concept_rows, key=lambda row: row.get("reward", 0.0), reverse=True)[:3]
    return [
        {
            "concept_id": row.get("id"),
            "concept_name": row.get("concept_name"),
            "dominant_signal": row.get("dominant_signal"),
            "risk_level": row.get("concept_risk_level", "unknown"),
            "reward": row.get("reward", 0.0),
            "scam_rate": row.get("scam_rate", 0.0),
            "reviewed_count": row.get("reviewed_count", 0),
        }
        for row in top_rows
    ]


def _top_signals(metrics: dict[str, Any]) -> list[str]:
    query_rows = list(metrics.get("query_performance", {}).values())
    if not query_rows:
        return ["guaranteed_return", "off_platform_contact", "authority_impersonation"]
    query_rows = sorted(query_rows, key=lambda row: row.get("reward", 0.0), reverse=True)
    signals: list[str] = []
    for row in query_rows:
        signal = str(row.get("expected_signal") or "")
        if signal and signal != "hard_negative_warning" and signal not in signals:
            signals.append(signal)
    return signals or ["guaranteed_return", "off_platform_contact", "authority_impersonation"]


def _language_distribution(candidates: list[dict[str, Any]]) -> dict[str, float]:
    counts: dict[str, int] = defaultdict(int)
    for candidate in candidates:
        counts[str(candidate["features"].get("language", "unknown"))] += 1
    total = sum(counts.values())
    if total == 0:
        return {"unknown": 1.0}
    return {language: round(count / total, 6) for language, count in sorted(counts.items())}


def _next_round_number() -> int:
    rounds = load_metrics().get("rounds", [])
    if not rounds:
        return 1
    return max(int(round_record.get("round", 0)) for round_record in rounds) + 1
