#!/usr/bin/env python3
"""Run the advanced synthetic discovery loop."""

from __future__ import annotations

import argparse

from src.pipeline.runner import ADVANCED_BANDIT_PATH, run_rounds


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rounds", type=int, default=1, help="Number of advanced discovery rounds to run.")
    parser.add_argument("--query-count", type=int, default=6, help="LLM-shaped query objects generated per round.")
    parser.add_argument("--top-k", type=int, default=5, help="Candidates selected for simulated review per round.")
    parser.add_argument("--alpha", type=float, default=0.8, help="LinUCB uncertainty weight.")
    parser.add_argument("--seed", type=int, default=20260505, help="Deterministic simulation seed.")
    parser.add_argument("--reset", action="store_true", help="Reset advanced local learning state before running.")
    args = parser.parse_args()

    records = run_rounds(
        rounds=args.rounds,
        query_count=args.query_count,
        top_k=args.top_k,
        alpha=args.alpha,
        seed=args.seed,
        reset=args.reset,
    )
    rewards = [float(record["summary"]["reward_high_value_per_reviewer_hour"]) for record in records]

    for record in records:
        summary = record["summary"]
        print(
            "round={round} queries={queries} candidates={candidate_count} selected={selected_count} "
            "scam={scam_count} review_minutes={minutes:.3f} reward_per_hour={reward:.3f}".format(
                round=record["round"],
                queries=len(record["queries"]),
                candidate_count=record["candidate_count"],
                selected_count=record["selected_count"],
                scam_count=summary["scam_count"],
                minutes=float(summary["total_review_minutes"]),
                reward=float(summary["reward_high_value_per_reviewer_hour"]),
            )
        )

    if rewards:
        print("reward_trend=" + " -> ".join(f"{reward:.3f}" for reward in rewards))
        print(f"reward_change={rewards[-1] - rewards[0]:+.3f} scam-worthy_candidates_per_reviewer_hour")
    print(f"contextual_bandit_state={ADVANCED_BANDIT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
