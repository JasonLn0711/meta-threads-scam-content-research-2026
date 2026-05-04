# Metrics

This directory stores aggregate, repo-safe v2 metric outputs.

`signal_scores/latest_ranking.yaml` is generated from metadata-only candidate records. It measures signal value score, review burden, and batch-level yield without raw evidence.

`contrast_scores/latest.yaml` is generated from the same metadata-only candidate
records. It does not classify candidates; it proposes sparse reviewer-routing
lanes for contrast-aware batch planning.

`batch_logs/` stores one actual run log per batch. Each batch must be logged even
when it fails, blocks, produces no candidates, or changes no metric. These logs
separate planned expectations from observed results and preserve the system's
learning history without raw evidence.
