"""Closed-loop discovery round runner."""

from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Any

from src.candidate.builder import create_candidate, write_candidate_batch
from src.candidate.scoring import score_candidate, select_top_k
from src.discovery.connector import fetch_candidates
from src.discovery.query_generator import generate_queries
from src.evidence.ingestion import ingest_evidence
from src.evidence.storage import REPO_ROOT
from src.learning.bandit import Bandit
from src.learning.metrics import rewards_by_query, simulate_review, summarize_results


LEARNING_STATE_DIR = REPO_ROOT / "data/learning_state"
BANDIT_STATE_PATH = LEARNING_STATE_DIR / "bandit_state.json"
METRICS_PATH = LEARNING_STATE_DIR / "metrics.json"
ROUND_LOG_PATH = LEARNING_STATE_DIR / "rounds.jsonl"


def run_round(
    *,
    round_number: int,
    bandit: Bandit,
    query_count: int = 3,
    top_k: int = 5,
    seed: int = 20260505,
) -> dict[str, Any]:
    selected_query_ids = bandit.select_queries(query_count)
    queries = generate_queries(bandit.to_state(), selected_query_ids=selected_query_ids, query_count=query_count)
    candidates: list[dict[str, Any]] = []

    for query in queries:
        for item in fetch_candidates(query):
            evidence = ingest_evidence(
                item["raw_text"],
                {
                    "source": "synthetic_mock_threads",
                    "query_id": query["query_id"],
                    "strategy": query["strategy"],
                    "mock_item_id": item["mock_item_id"],
                    "round": round_number,
                },
                actor="closed_loop_runner",
            )
            candidate = create_candidate(
                evidence["evidence_id"],
                item["raw_text"],
                query_id=query["query_id"],
                source_item_id=item["mock_item_id"],
                evidence_hash=evidence["sha256"],
            )
            candidate["score"] = score_candidate(candidate["features"])
            candidates.append(candidate)

    selected_candidates = select_top_k(candidates, top_k)
    candidate_path = write_candidate_batch(selected_candidates, round_number=round_number)
    rng = random.Random(seed + round_number)
    review_results = [simulate_review(candidate, rng) for candidate in selected_candidates]
    summary = summarize_results(review_results)
    query_rewards = rewards_by_query(review_results)

    for query in queries:
        bandit.update(query["query_id"], query_rewards.get(query["query_id"], 0.0))

    round_record = {
        "schema_version": "closed_loop_round_v1",
        "round": round_number,
        "queries": queries,
        "candidate_count": len(candidates),
        "selected_count": len(selected_candidates),
        "selected_candidate_path": str(candidate_path.relative_to(REPO_ROOT)),
        "review_results": review_results,
        "query_rewards": query_rewards,
        "summary": summary,
        "bandit_state_after_round": bandit.to_state(),
    }
    persist_round(round_record, bandit)
    return round_record


def persist_round(round_record: dict[str, Any], bandit: Bandit) -> None:
    LEARNING_STATE_DIR.mkdir(parents=True, exist_ok=True)
    bandit.save(BANDIT_STATE_PATH)
    metrics = load_metrics()
    metrics["rounds"].append(
        {
            "round": round_record["round"],
            "reward_high_value_per_reviewer_hour": round_record["summary"]["reward_high_value_per_reviewer_hour"],
            "scam_count": round_record["summary"]["scam_count"],
            "reviewed_count": round_record["summary"]["reviewed_count"],
            "total_review_minutes": round_record["summary"]["total_review_minutes"],
            "query_rewards": round_record["query_rewards"],
        }
    )
    METRICS_PATH.write_text(json.dumps(metrics, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with ROUND_LOG_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(round_record, ensure_ascii=False, sort_keys=True) + "\n")


def load_metrics() -> dict[str, Any]:
    if not METRICS_PATH.exists():
        return {"schema_version": "closed_loop_metrics_v1", "rounds": []}
    return json.loads(METRICS_PATH.read_text(encoding="utf-8"))


def reset_learning_state() -> None:
    for path in (BANDIT_STATE_PATH, METRICS_PATH, ROUND_LOG_PATH):
        path.unlink(missing_ok=True)
