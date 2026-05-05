#!/usr/bin/env python3
"""Run the governed adaptive policy deployment-loop smoke test."""

from __future__ import annotations

import argparse

from src.policy.deployment import build_policy_contexts_from_sources, run_deployment_loop
from src.policy.logging import POLICY_STATE_PATH, reset_policy_logs, write_json
from src.policy.training import load_combined_training_logs, load_policy_state, train_policy, update_policy


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=["shadow", "assist", "partial"], default="shadow")
    parser.add_argument("--rounds", type=int, default=5, help="Number of metadata-only contexts to evaluate.")
    parser.add_argument("--reset", action="store_true", help="Reset local policy logs before running.")
    parser.add_argument("--train-first", action="store_true", help="Train from existing logs before deployment loop.")
    args = parser.parse_args()

    if args.reset:
        reset_policy_logs()

    state = load_policy_state()
    if args.train_first:
        state = train_policy(load_combined_training_logs(), prior_state=state)
        write_json(POLICY_STATE_PATH, state)

    contexts = build_policy_contexts_from_sources(limit=args.rounds)
    run = run_deployment_loop(contexts, mode=args.mode, state=state, log=True)
    updated_state = update_policy(run["records"], state=state, historical_logs=load_combined_training_logs())
    evaluation = run["evaluation"]

    print(
        "mode={mode} decisions={decisions} reward_per_reviewer_hour={reward:.3f} "
        "latency={latency} robustness={robustness:.3f}".format(
            mode=args.mode,
            decisions=run["decision_count"],
            reward=float(evaluation["reward_per_reviewer_hour"]),
            latency=evaluation["detection_latency_rounds"],
            robustness=float(evaluation["robustness"]),
        )
    )
    print(f"policy_version={updated_state['policy_version']} training_examples={updated_state['training_examples']}")
    print(f"policy_state={POLICY_STATE_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
