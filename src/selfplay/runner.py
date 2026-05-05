"""Runnable defensive self-play loop."""

from __future__ import annotations

import statistics
from pathlib import Path
from typing import Any

from src.concepts.builder import CONCEPTS_DIR
from src.evidence.storage import utc_now
from src.selfplay.adversary import generate_variant
from src.selfplay.detector import DEFAULT_THRESHOLD, detect
from src.selfplay.judge import compute_rewards
from src.selfplay.logging import SELFPLAY_STATE_PATH, read_json, reset_selfplay_logs, write_json
from src.selfplay.simulation import generate_simulated_data


DEFAULT_CONCEPT = {
    "concept_id": "selfplay_default_concept",
    "concept_name": "Abstract investment-scam lure",
    "description": "A synthetic concept used only when no stored concepts are available.",
    "attack_pattern": "Build trust -> introduce vague opportunity -> pressure interpretation without details.",
    "psychological_hook": "trust plus opportunity framing",
    "risk_level": "medium",
    "dominant_signal": "authority_impersonation",
    "keywords": ["abstract", "trust", "opportunity"],
    "metrics": {"scam_rate": 0.5, "sample_count": 0},
}


def run_selfplay(
    *,
    rounds: int,
    variants_per_round: int = 2,
    reset: bool = False,
    concepts: list[dict[str, Any]] | None = None,
    log: bool = True,
) -> list[dict[str, Any]]:
    """Run multiple self-play rounds and persist safe logs."""
    if rounds < 1:
        raise ValueError("rounds must be at least 1")
    if variants_per_round < 1:
        raise ValueError("variants_per_round must be at least 1")
    if reset:
        reset_selfplay_logs()
    state = load_selfplay_state()
    concept_pool = concepts or load_concepts()
    start_round = _next_round_number(state)
    records = []
    for offset in range(rounds):
        record = run_selfplay_round(
            round_number=start_round + offset,
            concepts=concept_pool,
            state=state,
            variants_per_round=variants_per_round,
            log=log,
        )
        records.append(record)
        state = record["state_after_round"]
        write_json(SELFPLAY_STATE_PATH, state)
    return records


def run_selfplay_round(
    *,
    round_number: int,
    concepts: list[dict[str, Any]],
    state: dict[str, Any] | None = None,
    variants_per_round: int = 2,
    log: bool = False,
) -> dict[str, Any]:
    """Run one adversary/detector/judge exchange round."""
    state = _default_state(state)
    concept_pool = concepts or [DEFAULT_CONCEPT]
    selected_concepts = _select_concepts(concept_pool, state, variants_per_round)
    exchanges = []
    for concept in selected_concepts:
        variant = generate_variant(
            concept,
            difficulty=float(state["adversary"]["difficulty"]),
            strategy_bias=state["adversary"].get("last_successful_evasion"),
            log=log,
        )
        simulated = generate_simulated_data(variant, log=log)
        detection = detect(simulated, concept_pool, detector_state=state["detector"], log=log)
        rewards = compute_rewards(variant, detection, log=log)
        exchanges.append({"concept": _concept_ref(concept), "variant": variant, "simulated": simulated, "detection": detection, "rewards": rewards})

    summary = _round_summary(round_number, exchanges)
    state_after = _update_state(state, round_number, exchanges, summary)
    return {
        "schema_version": "selfplay_round_v1",
        "round": round_number,
        "generated_at": utc_now(),
        "exchange_count": len(exchanges),
        "exchanges": exchanges,
        "summary": summary,
        "state_after_round": state_after,
        "raw_source_included": False,
    }


def load_concepts(concepts_dir: Path = CONCEPTS_DIR) -> list[dict[str, Any]]:
    """Load stored metadata-only concepts, falling back to a synthetic default."""
    if not concepts_dir.exists():
        return [DEFAULT_CONCEPT]
    concepts = []
    for path in sorted(concepts_dir.glob("concept_*.json")):
        try:
            concepts.append(read_json(path))
        except Exception:
            continue
    return concepts or [DEFAULT_CONCEPT]


def load_selfplay_state(path: Path = SELFPLAY_STATE_PATH) -> dict[str, Any]:
    return _default_state(read_json(path))


def load_selfplay_priorities(path: Path = SELFPLAY_STATE_PATH) -> list[dict[str, Any]]:
    state = load_selfplay_state(path)
    return list(state.get("selfplay_priorities", []))


def _default_state(state: dict[str, Any] | None = None) -> dict[str, Any]:
    state = dict(state or {})
    return {
        "schema_version": "defensive_selfplay_state_v1",
        "rounds": list(state.get("rounds", [])),
        "adversary": {
            "difficulty": float(state.get("adversary", {}).get("difficulty", 0.32)),
            "last_successful_evasion": state.get("adversary", {}).get("last_successful_evasion"),
        },
        "detector": {
            "robustness": float(state.get("detector", {}).get("robustness", 0.34)),
            "threshold": float(state.get("detector", {}).get("threshold", DEFAULT_THRESHOLD)),
        },
        "reward_progression": list(state.get("reward_progression", [])),
        "selfplay_priorities": list(state.get("selfplay_priorities", [])),
        "updated_at": state.get("updated_at", utc_now()),
        "raw_source_included": False,
    }


def _select_concepts(
    concepts: list[dict[str, Any]],
    state: dict[str, Any],
    count: int,
) -> list[dict[str, Any]]:
    priority_ids = [str(row.get("origin_concept_id")) for row in state.get("selfplay_priorities", [])]

    def rank(concept: dict[str, Any]) -> tuple[int, float, str]:
        concept_id = str(concept.get("concept_id"))
        priority_rank = priority_ids.index(concept_id) if concept_id in priority_ids else 999
        scam_rate = float(concept.get("metrics", {}).get("scam_rate", 0.0) or 0.0)
        risk_boost = {"high": 0.2, "medium": 0.1, "low": 0.0}.get(str(concept.get("risk_level", "low")), 0.0)
        return (priority_rank, -(scam_rate + risk_boost), concept_id)

    return sorted(concepts, key=rank)[:count]


def _round_summary(round_number: int, exchanges: list[dict[str, Any]]) -> dict[str, Any]:
    confidences = [float(exchange["detection"]["confidence"]) for exchange in exchanges]
    adversary_rewards = [float(exchange["rewards"]["adversary_reward"]) for exchange in exchanges]
    detector_rewards = [float(exchange["rewards"]["detector_reward"]) for exchange in exchanges]
    novelty_count = sum(1 for exchange in exchanges if exchange["detection"].get("novelty"))
    return {
        "round": round_number,
        "average_detection_confidence": round(statistics.fmean(confidences), 6) if confidences else 0.0,
        "average_adversary_reward": round(statistics.fmean(adversary_rewards), 6) if adversary_rewards else 0.0,
        "average_detector_reward": round(statistics.fmean(detector_rewards), 6) if detector_rewards else 0.0,
        "novelty_count": novelty_count,
        "variant_count": len(exchanges),
    }


def _update_state(
    state: dict[str, Any],
    round_number: int,
    exchanges: list[dict[str, Any]],
    summary: dict[str, Any],
) -> dict[str, Any]:
    adversary_reward = float(summary["average_adversary_reward"])
    detector_reward = float(summary["average_detector_reward"])
    difficulty = _clamp(float(state["adversary"]["difficulty"]) + 0.035 + (0.06 * (detector_reward - adversary_reward)))
    robustness = _clamp(float(state["detector"]["robustness"]) + (0.07 * adversary_reward) + (0.025 * detector_reward))
    priorities = _build_priorities(exchanges)
    rounds = list(state.get("rounds", []))
    rounds.append(
        {
            "round": round_number,
            "average_adversary_reward": round(adversary_reward, 6),
            "average_detector_reward": round(detector_reward, 6),
            "average_detection_confidence": summary["average_detection_confidence"],
            "variant_count": summary["variant_count"],
        }
    )
    progression = list(state.get("reward_progression", []))
    progression.append(
        {
            "round": round_number,
            "adversary_reward": round(adversary_reward, 6),
            "detector_reward": round(detector_reward, 6),
            "detection_confidence": summary["average_detection_confidence"],
        }
    )
    return {
        "schema_version": "defensive_selfplay_state_v1",
        "rounds": rounds,
        "adversary": {
            "difficulty": round(difficulty, 6),
            "last_successful_evasion": priorities[0]["evasion_characteristic"] if priorities else None,
        },
        "detector": {
            "robustness": round(robustness, 6),
            "threshold": state["detector"]["threshold"],
        },
        "reward_progression": progression,
        "selfplay_priorities": priorities,
        "updated_at": utc_now(),
        "raw_source_included": False,
    }


def _build_priorities(exchanges: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for exchange in exchanges:
        variant = exchange["variant"]
        detection = exchange["detection"]
        rewards = exchange["rewards"]
        adversary_reward = float(rewards.get("adversary_reward", 0.0) or 0.0)
        confidence = float(detection.get("confidence", 0.0) or 0.0)
        priority = min(1.0, (0.65 * adversary_reward) + (0.35 * (1.0 - confidence)))
        rows.append(
            {
                "variant_id": variant.get("variant_id"),
                "origin_concept_id": variant.get("origin_concept_id"),
                "origin_concept_name": variant.get("origin_concept_name"),
                "origin_dominant_signal": variant.get("origin_dominant_signal"),
                "evasion_characteristic": variant.get("evasion_characteristic"),
                "variant_strategy": variant.get("variant_strategy"),
                "search_query": variant.get("search_query"),
                "selfplay_reward_signal": round(adversary_reward, 6),
                "detector_confidence": round(confidence, 6),
                "exploration_priority": round(priority, 6),
                "simulated": True,
                "raw_source_included": False,
            }
        )
    return sorted(rows, key=lambda row: (-float(row["exploration_priority"]), str(row["variant_id"])))[:6]


def _concept_ref(concept: dict[str, Any]) -> dict[str, Any]:
    return {
        "concept_id": concept.get("concept_id"),
        "concept_name": concept.get("concept_name"),
        "dominant_signal": concept.get("dominant_signal"),
        "risk_level": concept.get("risk_level"),
    }


def _next_round_number(state: dict[str, Any]) -> int:
    rounds = state.get("rounds", [])
    if not rounds:
        return 1
    return max(int(row.get("round", 0)) for row in rounds) + 1


def _clamp(value: float) -> float:
    return max(0.0, min(1.0, float(value)))
