#!/usr/bin/env python3
"""Run the defensive self-play simulation loop."""

from __future__ import annotations

import argparse

from src.selfplay.logging import SELFPLAY_STATE_PATH
from src.selfplay.runner import run_selfplay


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rounds", type=int, default=1, help="Number of self-play rounds to run.")
    parser.add_argument("--variants-per-round", type=int, default=2, help="Synthetic variants generated per round.")
    parser.add_argument("--reset", action="store_true", help="Reset local self-play logs before running.")
    args = parser.parse_args()

    records = run_selfplay(
        rounds=args.rounds,
        variants_per_round=args.variants_per_round,
        reset=args.reset,
        log=True,
    )

    detector_rewards = []
    adversary_rewards = []
    confidences = []
    for record in records:
        summary = record["summary"]
        detector_rewards.append(float(summary["average_detector_reward"]))
        adversary_rewards.append(float(summary["average_adversary_reward"]))
        confidences.append(float(summary["average_detection_confidence"]))
        print(
            "round={round} variants={variants} detector_reward={detector:.3f} "
            "adversary_reward={adversary:.3f} detection_confidence={confidence:.3f} novelty={novelty}".format(
                round=record["round"],
                variants=summary["variant_count"],
                detector=float(summary["average_detector_reward"]),
                adversary=float(summary["average_adversary_reward"]),
                confidence=float(summary["average_detection_confidence"]),
                novelty=summary["novelty_count"],
            )
        )

    if detector_rewards:
        print("detector_reward_trend=" + " -> ".join(f"{reward:.3f}" for reward in detector_rewards))
        print("adversary_reward_trend=" + " -> ".join(f"{reward:.3f}" for reward in adversary_rewards))
        print("detection_confidence_trend=" + " -> ".join(f"{confidence:.3f}" for confidence in confidences))
        print(f"detector_reward_change={detector_rewards[-1] - detector_rewards[0]:+.3f}")
    print(f"selfplay_state={SELFPLAY_STATE_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
