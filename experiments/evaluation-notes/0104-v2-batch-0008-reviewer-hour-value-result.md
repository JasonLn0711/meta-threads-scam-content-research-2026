# 0104 - V2 Batch 0008 Reviewer-Hour Value Result

Date: 2026-05-04

## First-Principle Question

The purpose of Batch 0008 was not to improve scam classification.

The question was:

```text
Which reviewed metadata lane maximizes high-value candidate discovery per
reviewer hour?
```

## Inputs

- Experiment plan: `experiments/batch_variants/0008-context-gate-reviewer-hour-value.md`
- Intake worksheet: `data/candidate_intake/batch_0008_intake.yaml`
- Conversion report: `data/candidate_intake/batch_0008_conversion_report.yaml`
- Candidate records: `data/candidates/batch_0008/*.yaml`
- Run log: `metrics/batch_logs/batch_0008_run_log.yaml`

All entries are structured metadata only. No raw Threads content, PII, URLs,
handles, screenshots, browser artifacts, credentials, or controlled-store
locators are included.

## Conversion Result

```text
intake_count: 16
converted_count: 16
blocked_count: 0
written_count: 16
candidate_records_written: true
```

## Batch Result

```text
reviewed_count: 16
scam_count: 4
non_scam_count: 4
uncertain_count: 8
yield_rate: 0.25
information_density: 0.319293
average_review_time_seconds: 41.875
cognitive_load: 1.375
svs: 0.001386349
```

Reviewer-hour view:

```text
candidates_per_reviewer_hour: 85.970149
high_value_candidates_per_hour: 21.492537
burden_adjusted_value: 15.630936
needs_thread_rate: 0.25
second_review_rate: 0.375
uncertainty_rate: 0.5
```

## Arm Results

### A - strong_source_priority

```text
reviewed_count: 4
scam_count: 4
yield_rate: 1.0
average_review_time_seconds: 33.25
candidates_per_reviewer_hour: 108.270677
high_value_candidates_per_hour: 108.270677
needs_thread_rate: 0.0
second_review_rate: 0.0
uncertainty_rate: 0.0
```

Interpretation:

This remains the best reviewer-hour lane. It is not a legal determination or a
production decision path, but it is the strongest reviewed metadata route when
reviewer capacity is constrained.

### B - result_display_low_context_transition

```text
reviewed_count: 4
scam_count: 0
uncertain_count: 4
yield_rate: 0.0
average_review_time_seconds: 42.5
second_review_rate: 0.5
uncertainty_rate: 1.0
```

Interpretation:

This lane is cheaper than thread-required review, but it still did not produce
positive yield. It should remain a cheap boundary triage lane, not a priority
source arm.

### C - result_display_thread_required

```text
reviewed_count: 4
scam_count: 0
uncertain_count: 4
yield_rate: 0.0
average_review_time_seconds: 57.25
needs_thread_rate: 1.0
second_review_rate: 1.0
uncertainty_rate: 1.0
```

Interpretation:

This is the most expensive reviewed lane in the batch and produced no positive
yield. It should be restricted to slow context review or tiny diagnostic probes.

### D - result_display_clean_holdout

```text
reviewed_count: 4
non_scam_count: 4
yield_rate: 0.0
average_review_time_seconds: 34.5
needs_thread_rate: 0.0
second_review_rate: 0.0
uncertainty_rate: 0.0
```

Interpretation:

This lane is useful as hard-negative calibration. It protects the system from
over-generalizing `成果展示`.

## Signal Movement

After Batch 0008:

```text
保證收益:
  reviewed_count: 21
  yield_rate: 0.904762
  review_time: 38.428571
  svs: 0.012487227

成果展示:
  reviewed_count: 46
  yield_rate: 0.130435
  review_time: 44.565217
  svs: 0.00064165
```

Decision:

`保證收益` remains the primary high-value sparse signal. `成果展示` remains a
context/routing signal and should not be treated as a priority positive-yield
signal by itself.

## Failure Modes

- Result-display lanes B and C produced zero positive yield in this capped batch.
- Thread-required result-display review had the highest review burden.
- Sparse clustering still produces one broad cluster at the current threshold.
- Embedding discovery remains limited because only synthetic examples have
  precomputed vectors.
- Feature discovery produced zero auto-generated features because the latest
  discrepancy report has no valid `missed_pattern` group with size >= 3.

## Decision Implication

Prioritize `strong_source_priority` when reviewer capacity is constrained.

Keep result-display lanes for:

- hard-negative calibration;
- context-gating diagnostics;
- small targeted probes;
- reviewer workflow design.

Do not broaden review around `成果展示` unless a narrower source arm or behavior
feature shows positive reviewer-hour value.

## Next Action

Write a context-gating policy note that turns Batch 0007 and Batch 0008 into a
review routing rule:

```text
Fast lane: strong_source_priority
Boundary lane: result_display_low_context_transition
Slow lane: result_display_thread_required
Calibration lane: result_display_clean_holdout
```

No sparse feature promotion is justified by Batch 0008.
