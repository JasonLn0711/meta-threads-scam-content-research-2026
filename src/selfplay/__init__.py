"""Defensive self-play simulation layer."""

from src.selfplay.adversary import generate_variant
from src.selfplay.detector import detect
from src.selfplay.judge import compute_rewards
from src.selfplay.runner import load_selfplay_priorities, run_selfplay, run_selfplay_round
from src.selfplay.simulation import generate_simulated_data

__all__ = [
    "compute_rewards",
    "detect",
    "generate_simulated_data",
    "generate_variant",
    "load_selfplay_priorities",
    "run_selfplay",
    "run_selfplay_round",
]
