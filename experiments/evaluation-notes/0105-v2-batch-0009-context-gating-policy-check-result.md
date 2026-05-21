# 0105 - V2 Batch 0009 Context-Gating Policy Check Result

Date: 2026-05-05

## First-Principle Question

Batch 0009 tested whether the active context-gating policy improves high-value
candidate discovery per reviewer hour when it controls the next metadata-only
batch.

The question was not whether the system can decide legal fraud or production
scam detection. The question was whether scarce reviewer capacity should be
weighted toward `strong_source_priority` while preserving small calibration and
diagnostic probes.

## Inputs

- Experiment plan: `experiments/batch_variants/0009-context-gating-policy-check.md`
- Intake worksheet: `data/candidate_intake/batch_0009_intake.yaml`
- Conversion report: `data/candidate_intake/batch_0009_conversion_report.yaml`
- Candidate records: `data/candidates/batch_0009/*.yaml`
- Run log: `metrics/batch_logs/batch_0009_run_log.yaml`
- Policy: `docs/63-context-gating-policy.md`

All entries are structured metadata only. No raw Threads content, PII, URLs,
handles, screenshots, browser artifacts, credentials, or controlled-store
locators are included.

## Conversion Result

```text
intake_count: 12
converted_count: 12
blocked_count: 0
written_count: 12
candidate_records_written: true
```

## Batch Result

```text
reviewed_count: 12
scam_count: 8
non_scam_count: 2
uncertain_count: 2
yield_rate: 0.666667
information_density: 0.496981
average_review_time_seconds: 37.333333
cognitive_load: 1.225
svs: 0.007244616
```

Reviewer-hour view:

```text
candidates_per_reviewer_hour: 96.428571
high_value_candidates_per_hour: 64.285714
burden_adjusted_value: 52.478134
needs_thread_rate: 0.083333
second_review_rate: 0.25
uncertainty_rate: 0.166667
```

Comparison target from Batch 0008:

```text
batch_0008_high_value_candidates_per_hour: 21.492537
batch_0008_batch_svs: 0.001386349
```

Batch 0009 improved both:

```text
batch_0009_high_value_candidates_per_hour: 64.285714
batch_0009_batch_svs: 0.007244616
```

## Lane Results

### A - strong_source_priority

```text
reviewed_count: 8
scam_count: 8
yield_rate: 1.0
average_review_time_seconds: 34.75
high_value_candidates_per_hour: 103.597122
needs_thread_rate: 0.0
second_review_rate: 0.125
uncertainty_rate: 0.0
```

Interpretation:

The fast lane passed the prospective check. It stayed above the `0.75` yield
floor and below the 40-second average review-time ceiling. One borderline
fast-lane candidate required second review because the stable funnel anchor was
absent, so the policy should preserve second-review override rather than turning
the lane into automatic acceptance.

### B - result_display_clean_holdout

```text
reviewed_count: 2
non_scam_count: 2
yield_rate: 0.0
average_review_time_seconds: 35.0
needs_thread_rate: 0.0
second_review_rate: 0.0
uncertainty_rate: 0.0
```

Interpretation:

The clean holdout remained stable hard-negative calibration. It protects the
system from treating `成果展示` as positive-yield by itself.

### C - result_display_low_context_transition

```text
reviewed_count: 1
uncertain_count: 1
yield_rate: 0.0
average_review_time_seconds: 42.0
second_review_rate: 1.0
uncertainty_rate: 1.0
```

Interpretation:

The low-context boundary probe should remain capped. It is useful for boundary
learning, not priority positive-yield review.

### D - result_display_thread_required

```text
reviewed_count: 1
uncertain_count: 1
yield_rate: 0.0
average_review_time_seconds: 58.0
needs_thread_rate: 1.0
second_review_rate: 1.0
uncertainty_rate: 1.0
```

Interpretation:

The slow-context diagnostic remained expensive and uncertain. It should not be
expanded into routine review under constrained reviewer capacity.

## Signal Movement

After Batch 0009:

```text
保證收益:
  reviewed_count: 29
  yield_rate: 0.931034
  review_time: 37.413793
  svs: 0.01353643

review_stable_funnel_anchor:
  reviewed_count: 33
  yield_rate: 0.787879
  review_time: 40.121212
  svs: 0.011390594

成果展示:
  reviewed_count: 52
  yield_rate: 0.153846
  review_time: 44.076923
  svs: 0.000785721
```

Decision:

`保證收益` remains the strongest positive sparse signal. `成果展示` remains a
context/routing signal and should not be promoted as a priority positive-yield
signal by itself.

## Failure Modes

- One fast-lane candidate required second review because the stable funnel anchor
  was absent.
- The low-context and thread-required result-display probes remained uncertain.
- Sparse clustering still places all 76 candidates in one broad cluster at the
  current threshold.
- Embedding remains discovery-only and too sparse for operational routing.
- Feature discovery produced zero auto-generated features because the latest
  discrepancy report has no valid `missed_pattern` group with size >= 3.

## Decision Implication

Batch 0009 supports the active context-gating policy.

Use `strong_source_priority` first when reviewer capacity is constrained,
preserve `result_display_clean_holdout` as hard-negative calibration, and keep
result-display boundary/context probes capped.

Do not promote new sparse features, expand collection, train models, or make
production/legal/enforcement claims from Batch 0009 alone.

## Next Action

Use the supported context-gating policy as the routing base for a
Reviewer Assist Layer labor-savings evaluation: schema prefill, summary-assisted
review, priority explanation, correction-rate tracking, and reviewer-time
measurement under human final judgment.
