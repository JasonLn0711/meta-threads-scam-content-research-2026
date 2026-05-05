# Decision 0134 - Record V2 Batch 0009 Context-Gating Policy Check

Date: 2026-05-05

## Status

Accepted as a completed metadata-only v2 policy check.

## Decision

Record Batch 0009 as supporting the active context-gating policy.

The policy-weighted allocation improved batch-level reviewer-hour value compared
with Batch 0008:

```text
Batch 0008 high_value_candidates_per_hour: 21.492537
Batch 0009 high_value_candidates_per_hour: 64.285714
Batch 0008 batch_svs: 0.001386349
Batch 0009 batch_svs: 0.007244616
```

The fast lane stayed high-yield and low-burden:

```text
strong_source_priority:
  reviewed_count: 8
  scam_count: 8
  yield_rate: 1.0
  average_review_time_seconds: 34.75
  needs_thread_rate: 0.0
  second_review_rate: 0.125
```

## Rationale

Batch 0009 used the Batch 0008 context-gating policy prospectively rather than
running another balanced comparison.

The result supports the policy:

- `strong_source_priority` remains the first reviewer-capacity lane.
- `result_display_clean_holdout` remains stable hard-negative calibration.
- `result_display_low_context_transition` remains capped boundary triage.
- `result_display_thread_required` remains capped slow-context diagnostics.
- `成果展示` remains a routing/context signal, not a priority positive-yield
  signal by itself.

## Evidence

- `data/candidate_intake/batch_0009_intake.yaml`
- `data/candidate_intake/batch_0009_conversion_report.yaml`
- `data/candidates/batch_0009/*.yaml`
- `metrics/batch_logs/batch_0009_run_log.yaml`
- `metrics/contrast_scores/latest.yaml`
- `metrics/signal_scores/latest_ranking.yaml`
- `experiments/evaluation-notes/0105-v2-batch-0009-context-gating-policy-check-result.md`
- `docs/63-context-gating-policy.md`

## Scope

This is a reviewer-routing decision over structured metadata only.

It does not authorize:

- external data access;
- raw Threads content storage;
- PII storage;
- URLs, handles, screenshots, browser artifacts, or controlled-store locators in
  git;
- broad collection;
- sparse schema auto-promotion;
- model training;
- production detection;
- legal fraud determination;
- enforcement, takedown, or public-warning actions.

## Next Action

Use the supported context-gating policy as the routing base for a Reviewer Assist
Layer labor-savings evaluation: schema prefill, summary-assisted review,
priority explanation, correction-rate tracking, and reviewer-time measurement
under human final judgment.
