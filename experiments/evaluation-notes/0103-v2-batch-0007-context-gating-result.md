# Batch 0007 Context-Gating Result

## Status

Completed on 2026-05-04.

This is a real experiment log, not a tutorial. No fake results are included.

## First-Principle Question

The question was not whether `成果展示` is scam.

The question was:

```text
Can result-display cases be routed by reviewer burden before spending full
thread-review effort?
```

## Inputs

- Intake worksheet: `data/candidate_intake/batch_0007_intake.yaml`
- Conversion report: `data/candidate_intake/batch_0007_conversion_report.yaml`
- Candidate records: `data/candidates/batch_0007/*.yaml`
- Run log: `metrics/batch_logs/batch_0007_run_log.yaml`
- Routing output: `metrics/contrast_scores/latest.yaml`

## What Is Done

- 12 metadata-only intake entries were completed by human review.
- 12 candidate records were written.
- Candidate validation passed with 48 total records and 0 errors.
- v2 ROS was rerun.
- Contrast-aware routing was updated to include result-display context gates.

## Results

Batch-level result:

```text
reviewed_count: 12
scam_count: 0
non_scam_count: 3
uncertain_count: 9
review_time: 44.583333
cognitive_load: 1.6625
svs: 0.0
```

Lane-level result:

```text
result_display_low_context_transition:
  reviewed_count: 3
  uncertain_count: 3
  review_time: 41.333333
  needs_thread_rate: 0.0
  second_review_rate: 0.0

result_display_thread_required:
  reviewed_count: 3
  uncertain_count: 3
  review_time: 49.0
  needs_thread_rate: 1.0
  second_review_rate: 1.0

result_display_emotional_thread_required:
  reviewed_count: 3
  uncertain_count: 3
  review_time: 51.0
  needs_thread_rate: 1.0
  second_review_rate: 1.0

result_display_contrast_holdout:
  reviewed_count: 3
  non_scam_count: 3
  review_time: 37.0
  needs_thread_rate: 0.0
  second_review_rate: 0.0
```

## Interpretation

Batch 0007 did not improve positive yield.

It did improve routing knowledge:

- low-context result-display transitions do not require full-thread review by default;
- thread-required result-display cases should not go to fast priority review;
- emotional plus thread-required result-display cases are high cognitive-load review paths;
- clean result-display holdouts remain useful hard-negative calibration material.

## Decision

Adopt context gating in the reviewer-routing layer.

Do not promote a new sparse feature yet. `context_required_result_display` remains
pending in the feature review queue.

## Guardrails

- no raw Threads content
- no PII
- no URLs, handles, screenshots, browser artifacts, credentials, or controlled-store
  locators
- no embedding-based decision
- no legal fraud, enforcement, takedown, or public-warning claim
- no sparse schema promotion without human acceptance
