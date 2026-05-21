# v2 Contrast-Aware Routing Result

## Purpose

Record the first contrast-aware reviewer-routing run after Batch 0005.

This is not a classifier, legal fraud decision, enforcement recommendation, or
production detector. It is a sparse metadata scoring layer for allocating
reviewer effort.

## Why This Step Exists

Batch 0005 showed that the whole-batch SVS can drop when a batch intentionally
includes hard negatives and ambiguous contrast cases. That is not enough by
itself to guide the next batch.

The next useful question is:

```text
Can the system route high-value source-arm candidates separately from
context-cost contrast candidates?
```

## Inputs

- Candidate records: `data/candidates/*.yaml`
- Sparse schema: `meta-system/sparse_schema/sparse_features_v2.yaml`
- Signal ranking: `metrics/signal_scores/latest_ranking.yaml`
- Batch 0005 log: `metrics/batch_logs/batch_0005_run_log.yaml`

## Output

- Contrast scores: `metrics/contrast_scores/latest.yaml`

## Lane Design

The scorer assigns candidates into sparse reviewer-routing lanes:

- `strong_source_priority`
- `guarantee_context_review`
- `result_display_context_review`
- `result_display_contrast_holdout`
- `other_metadata_review`

These lanes are routing hypotheses, not labels.

## Result

`strong_source_priority`:

```text
reviewed_count: 10
scam_count: 10
yield_rate: 1.0
review_time: 39.4
cognitive_load: 1.27
svs: 0.016682973
needs_thread_rate: 0.0
second_review_rate: 0.0
routing_action: fast_priority_review
```

`result_display_context_review`:

```text
reviewed_count: 9
scam_count: 0
non_scam_count: 2
uncertain_count: 7
yield_rate: 0.0
review_time: 45.333333
cognitive_load: 2.305556
svs: 0.0
needs_thread_rate: 1.0
second_review_rate: 0.777778
uncertainty_rate: 0.777778
routing_action: slow_context_review
```

`result_display_contrast_holdout`:

```text
reviewed_count: 1
non_scam_count: 1
needs_thread_rate: 0.0
second_review_rate: 0.0
routing_action: contrast_or_hard_negative_pool
```

## Interpretation

The system now separates two things that were previously mixed:

- high-value candidate discovery source arm: `保證收益 + executable transition`
- high-cost context arm: `成果展示` without explicit guarantee but with context cues

This is the right shape. It does not say `成果展示` is safe. It says broad result
display should not receive fast-priority review unless another sparse condition
explains why it is valuable.

## Decision Implication

Use contrast-aware routing in the next small batch:

```text
fast lane: strong_source_priority
slow lane: result_display_context_review
holdout lane: result_display_contrast_holdout
```

The next experiment should measure whether this routing lowers reviewer effort
without reducing high-value candidate discovery.

## Failure Modes

- The current lane result is still small-sample.
- `strong_source_priority` includes older Batch 0004 and synthetic dry-run records,
  not only Batch 0005.
- Batch 0004 and Batch 0005 records lack embedding vectors, so this is sparse
  routing only.
- This layer must not auto-promote features or replace human review.

## Guardrails

- no raw Threads content
- no PII
- no URLs, handles, screenshots, browser artifacts, credentials, or controlled-store
  locators
- no external systems accessed by this artifact
- no embedding-based decisions
- no automatic feature promotion
- no legal fraud, enforcement, takedown, or public warning claim
