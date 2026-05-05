#!/usr/bin/env python3
"""Run the synthetic closed-loop discovery + evidence + bandit system."""

from __future__ import annotations

import argparse

from src.learning.bandit import Bandit
from src.learning.runner import BANDIT_STATE_PATH, load_metrics, reset_learning_state, run_round


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rounds", type=int, default=1, help="Number of closed-loop rounds to run.")
    parser.add_argument("--top-k", type=int, default=5, help="Candidates selected for simulated review per round.")
    parser.add_argument("--query-count", type=int, default=3, help="Query arms selected per round.")
    parser.add_argument("--epsilon", type=float, default=0.2, help="Epsilon-greedy exploration rate.")
    parser.add_argument("--seed", type=int, default=20260505, help="Deterministic simulation seed.")
    parser.add_argument("--reset", action="store_true", help="Reset local learning state before running.")
    args = parser.parse_args()

    if args.rounds < 1:
        raise ValueError("--rounds must be at least 1")
    if args.reset:
        reset_learning_state()

    bandit = Bandit.load(BANDIT_STATE_PATH, epsilon=args.epsilon, seed=args.seed, reset=args.reset)
    rewards: list[float] = []
    starting_round = _next_round_number()

    for offset in range(args.rounds):
        round_number = starting_round + offset
        record = run_round(
            round_number=round_number,
            bandit=bandit,
            query_count=args.query_count,
            top_k=args.top_k,
            seed=args.seed,
        )
        summary = record["summary"]
        rewards.append(float(summary["reward_high_value_per_reviewer_hour"]))
        selected_ids = ", ".join(query["query_id"] for query in record["queries"])
        print(
            "round={round} queries=[{queries}] candidates={candidate_count} selected={selected_count} "
            "scam={scam_count} review_minutes={minutes:.3f} reward_per_hour={reward:.3f}".format(
                round=record["round"],
                queries=selected_ids,
                candidate_count=record["candidate_count"],
                selected_count=record["selected_count"],
                scam_count=summary["scam_count"],
                minutes=float(summary["total_review_minutes"]),
                reward=float(summary["reward_high_value_per_reviewer_hour"]),
            )
        )

    if rewards:
        delta = rewards[-1] - rewards[0]
        print("reward_trend=" + " -> ".join(f"{reward:.3f}" for reward in rewards))
        print(f"reward_change={delta:+.3f} high_value_candidates_per_reviewer_hour")
    print(f"bandit_state={BANDIT_STATE_PATH}")
    return 0


def _next_round_number() -> int:
    rounds = load_metrics().get("rounds", [])
    if not rounds:
        return 1
    return max(int(round_record.get("round", 0)) for round_record in rounds) + 1


if __name__ == "__main__":
    raise SystemExit(main())
