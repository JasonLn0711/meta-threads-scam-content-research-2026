# Batch 0006 Routing Validation Metric Note

## Purpose

Record the metric-level interpretation of Batch 0006 after all 12
human-reviewed structured metadata entries were converted into v2 candidate
records.

This note is a summary pointer. The full result is in
`experiments/batch_variants/0006-post-review-routing-result.md`.

## Result

Batch 0006 validated the first contrast-aware routing loop:

```text
strong_source_priority:
  reviewed_count: 4
  yield_rate: 1.0
  review_time: 32.5
  needs_thread_rate: 0.0
  second_review_rate: 0.0
  svs: 0.020606701

result_display_context_review:
  reviewed_count: 4
  yield_rate: 0.0
  review_time: 49.75
  needs_thread_rate: 1.0
  second_review_rate: 1.0
  uncertainty_rate: 1.0
  svs: 0.0
```

The system learned a routing distinction:

```text
high-value fast lane = guarantee/certainty anchor + executable transition + low context burden
high-cost slow lane = result display + context burden + uncertainty
```

## Decision

Keep contrast-aware routing active for the next small batch. Do not increase
collection volume until the broad sparse-cluster over-generalization problem is
tracked through a feature-review queue or a narrower routing rule.

## Guardrails

- metadata-only
- no raw Threads content
- no PII
- no embedding-based decisions
- no automatic sparse-schema promotion
