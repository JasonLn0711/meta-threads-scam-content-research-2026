# Decision 0132 - Record V2 Batch 0008 Context-Gating Policy

Date: 2026-05-04

## Status

Accepted as a v2 research-routing policy.

## Decision

Adopt the Batch 0008 reviewer-hour value result as a context-gating policy for
structured metadata review.

The policy routes future candidates into:

```text
strong_source_priority -> fast priority review
result_display_low_context_transition -> cheap boundary triage
result_display_thread_required -> slow context review or capped diagnostic sample
result_display_clean_holdout -> hard-negative calibration
```

## Evidence

- `data/candidate_intake/batch_0008_intake.yaml`
- `data/candidate_intake/batch_0008_conversion_report.yaml`
- `data/candidates/batch_0008/*.yaml`
- `metrics/batch_logs/batch_0008_run_log.yaml`
- `metrics/contrast_scores/latest.yaml`
- `metrics/signal_scores/latest_ranking.yaml`
- `experiments/evaluation-notes/0104-v2-batch-0008-reviewer-hour-value-result.md`
- `docs/63-context-gating-policy.md`
- `outputs/research_candidates/RC_0007.md`

## Rationale

Batch 0008 shows that `strong_source_priority` remains the highest reviewer-hour
value lane:

```text
yield_rate: 1.0
average_review_time_seconds: 33.25
high_value_candidates_per_hour: 108.270677
needs_thread_rate: 0.0
second_review_rate: 0.0
uncertainty_rate: 0.0
```

The result-display lanes did not justify broader priority review:

```text
result_display_low_context_transition:
  yield_rate: 0.0
  uncertainty_rate: 1.0
  second_review_rate: 0.5

result_display_thread_required:
  yield_rate: 0.0
  average_review_time_seconds: 57.25
  needs_thread_rate: 1.0
  second_review_rate: 1.0

result_display_clean_holdout:
  non_scam_count: 4
  uncertainty_rate: 0.0
```

## Scope

This is a reviewer-routing decision, not a label decision.

It does not authorize:

- raw Threads content storage;
- PII storage;
- external access;
- broad collection;
- sparse schema auto-promotion;
- model training;
- production detection;
- legal fraud determination;
- enforcement, takedown, or public-warning actions.

## Next Action

Use `docs/63-context-gating-policy.md` when designing Batch 0009 or any future
reviewer-assist routing check. Do not promote Batch 0008 features because the
latest feature discovery run produced zero valid auto-generated feature
candidates.
