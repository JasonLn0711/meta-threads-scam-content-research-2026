#!/usr/bin/env python3
"""Run the metadata-only v2 dual-track research operating system."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from engine.common import load_candidates, load_sparse_schema, write_yaml
from engine.common import load_yaml
from engine.discrepancy.detect import detect_discrepancies
from engine.embedding.clustering import cluster_embedding_candidates
from engine.feature_discovery.propose import build_review_queue, generate_feature_candidates
from engine.sparse.clustering import cluster_sparse_candidates
from engine.sparse.contrast import build_contrast_aware_scores
from engine.sparse.ranking import rank_signals


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate-dir", type=Path, default=Path("data/candidates"))
    parser.add_argument("--schema", type=Path, default=Path("data-contracts/candidate_record_v2.schema.yaml"))
    parser.add_argument(
        "--sparse-schema",
        type=Path,
        default=Path("meta-system/sparse_schema/sparse_features_v2.yaml"),
    )
    parser.add_argument("--sparse-threshold", type=float, default=0.45)
    parser.add_argument("--embedding-threshold", type=float, default=0.85)
    parser.add_argument("--embedding-far-threshold", type=float, default=0.25)
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--sparse-output", type=Path, default=Path("outputs/sparse_clusters/latest.yaml"))
    parser.add_argument("--embedding-output", type=Path, default=Path("outputs/embedding_clusters/latest.yaml"))
    parser.add_argument("--discrepancy-output", type=Path, default=Path("outputs/discrepancy_reports/latest.yaml"))
    parser.add_argument("--ranking-output", type=Path, default=Path("metrics/signal_scores/latest_ranking.yaml"))
    parser.add_argument("--contrast-output", type=Path, default=Path("metrics/contrast_scores/latest.yaml"))
    parser.add_argument("--feature-output-dir", type=Path, default=Path("meta-system/feature_candidates"))
    parser.add_argument(
        "--feature-review-queue-output",
        type=Path,
        default=Path("meta-system/feature_review_queue/latest.yaml"),
    )
    args = parser.parse_args()

    sparse_schema = load_sparse_schema(args.sparse_schema)
    candidates = load_candidates(
        args.candidate_dir,
        schema_path=args.schema,
        sparse_schema_path=args.sparse_schema,
        validate=True,
    )

    sparse_clusters = cluster_sparse_candidates(candidates, sparse_schema, threshold=args.sparse_threshold)
    embedding_clusters = cluster_embedding_candidates(
        candidates,
        threshold=args.embedding_threshold,
        top_k=args.top_k,
    )
    discrepancy_report = detect_discrepancies(
        candidates,
        sparse_clusters,
        embedding_close_threshold=args.embedding_threshold,
        embedding_far_threshold=args.embedding_far_threshold,
    )
    ranking = rank_signals(candidates, sparse_schema)
    contrast_scores = build_contrast_aware_scores(candidates, sparse_schema)
    feature_candidates = generate_feature_candidates(discrepancy_report)
    existing_review_queue = None
    if args.feature_review_queue_output.exists():
        loaded_queue = load_yaml(args.feature_review_queue_output)
        if isinstance(loaded_queue, dict):
            existing_review_queue = loaded_queue
    review_queue = build_review_queue(feature_candidates, existing_review_queue)

    write_yaml(args.sparse_output, sparse_clusters)
    write_yaml(args.embedding_output, embedding_clusters)
    write_yaml(args.discrepancy_output, discrepancy_report)
    write_yaml(args.ranking_output, ranking)
    write_yaml(args.contrast_output, contrast_scores)
    args.feature_output_dir.mkdir(parents=True, exist_ok=True)
    for feature_candidate in feature_candidates:
        write_yaml(args.feature_output_dir / f"{feature_candidate['feature_id']}.yaml", feature_candidate)
    if feature_candidates:
        write_yaml(args.feature_review_queue_output, review_queue)

    print(f"candidates_checked: {len(candidates)}")
    print(f"sparse_clusters_written: {args.sparse_output}")
    print(f"embedding_clusters_written: {args.embedding_output}")
    print(f"discrepancy_report_written: {args.discrepancy_output}")
    print(f"signal_ranking_written: {args.ranking_output}")
    print(f"contrast_scores_written: {args.contrast_output}")
    print(f"feature_candidates_written: {len(feature_candidates)}")
    if feature_candidates:
        print(f"feature_review_queue_written: {args.feature_review_queue_output}")
    else:
        print("feature_review_queue_written: skipped_no_new_feature_candidates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
