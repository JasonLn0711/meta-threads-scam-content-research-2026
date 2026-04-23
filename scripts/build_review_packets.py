#!/usr/bin/env python3
"""Build local-only Markdown triage packets for reviewer inspection."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.baselines.io_utils import load_records
from src.baselines.types import VALID_VARIANTS
from src.review.triage_packet import build_packets, load_predictions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Dataset file: .csv, .json, or .jsonl")
    parser.add_argument(
        "--predictions-json",
        type=Path,
        help="Optional predictions.json from scripts/run_rule_baseline.py",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/baseline_rule_config.yaml"),
        help="Rule config YAML path if predictions are generated on the fly",
    )
    parser.add_argument(
        "--variant",
        choices=VALID_VARIANTS,
        default="all",
        help="Baseline variant if predictions are generated on the fly",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("experiments/evaluation-notes/outputs"),
        help="Directory for local generated review packet outputs",
    )
    parser.add_argument("--run-name", help="Optional run directory name")
    parser.add_argument(
        "--max-text-chars",
        type=int,
        default=900,
        help="Maximum characters shown per text evidence field",
    )
    args = parser.parse_args()

    records = load_records(args.input)
    predictions = load_predictions(args.predictions_json) if args.predictions_json else None
    run_name = args.run_name or default_run_name()
    run_dir = args.output_dir / run_name

    result = build_packets(
        records,
        output_dir=run_dir,
        predictions=predictions,
        config_path=args.config,
        variant=args.variant,
        max_text_chars=args.max_text_chars,
    )

    print(f"run_dir: {result['output_dir']}")
    print(f"packet_count: {result['packet_count']}")
    print(f"index: {result['index_path']}")
    print(f"csv_index: {result['csv_index_path']}")
    print(f"manifest: {result['manifest_path']}")
    return 0


def default_run_name() -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"review-packets-{timestamp}"


if __name__ == "__main__":
    raise SystemExit(main())
