# Batch 0008 Context-Gate Reviewer-Hour Value

## Purpose

Batch 0008 tests whether the context gates learned in Batch 0007 improve
reviewer-hour allocation.

The goal is not to collect more broadly. The goal is to compare which lane
deserves scarce reviewer attention when candidate review time, full-thread
reading, second review, and uncertainty are all counted.

This is not a collection authorization, production detector step, legal fraud
judgment, enforcement workflow, public-warning workflow, or model-training step.

## First-Principle Question

The question is not:

```text
Can result-display cases be classified?
```

The question is:

```text
Which reviewed metadata lane maximizes high-value candidate discovery per
reviewer hour?
```

## Source Evidence

After Batch 0007:

```text
strong_source_priority:
  reviewed_count: 14
  yield_rate: 1.0
  review_time: 37.428571
  cognitive_load: 1.246429
  svs: 0.017651939

result_display_low_context_transition:
  reviewed_count: 3
  yield_rate: 0.0
  review_time: 41.333333
  needs_thread_rate: 0.0
  second_review_rate: 0.0

result_display_thread_required:
  reviewed_count: 12
  yield_rate: 0.0
  review_time: 46.5
  needs_thread_rate: 1.0
  second_review_rate: 0.833333

result_display_contrast_holdout:
  reviewed_count: 6
  yield_rate: 0.0
  review_time: 37.333333
  non_scam_count: 6
```

Source artifacts:

- `metrics/contrast_scores/latest.yaml`
- `metrics/batch_logs/batch_0007_run_log.yaml`
- `experiments/evaluation-notes/0103-v2-batch-0007-context-gating-result.md`
- `outputs/research_candidates/RC_0006.md`

## Batch Design

Use four arms:

```text
A: strong_source_priority
B: result_display_low_context_transition
C: result_display_thread_required
D: result_display_clean_holdout
```

Target size:

```text
16 candidate stubs total
4 stubs per arm
```

This cap is intentional. Batch 0008 is a reviewer-hour value test, not a scale
test.

## Arm A: Strong Source Priority Control

Routing hypothesis:

```text
保證收益 AND (誘導聯絡 OR 社群導流 OR reply_funnel OR review_stable_funnel_anchor) AND NOT needs_thread
```

Measurement focus:

- confirm high yield per reviewer hour;
- confirm low full-thread-reading burden;
- confirm low second-review burden;
- use as positive control against context gates.

Expected behavior:

```text
guarantee_executable_transition_fast_lane
```

## Arm B: Result Display Low-Context Transition

Routing hypothesis:

```text
成果展示 AND NOT 保證收益 AND NOT needs_thread AND visible transition structure
```

Measurement focus:

- whether cheap review remains cheap across a slightly larger capped sample;
- whether uncertainty stays high even without thread burden;
- whether this lane should be reviewed cheaply or deprioritized.

Expected behavior:

```text
result_display_low_context_transition
```

## Arm C: Result Display Thread Required

Routing hypothesis:

```text
成果展示 AND NOT 保證收益 AND needs_thread AND NOT 情緒操控
```

Measurement focus:

- full-thread-reading burden;
- second-review rate;
- uncertainty rate;
- whether any positive yield justifies the cost.

Expected behavior:

```text
result_display_thread_required
```

## Arm D: Result Display Clean Holdout

Routing hypothesis:

```text
成果展示 AND NOT 保證收益 AND NOT (誘導聯絡 OR 社群導流 OR reply_funnel OR needs_thread OR 情緒操控)
```

Measurement focus:

- hard-negative calibration;
- low-burden non-scam boundary;
- protection against over-generalizing `成果展示`;
- false-positive pressure.

Expected behavior:

```text
result_display_clean_holdout
```

## Reviewer-Hour Metrics

Compute after human review:

```text
candidates_per_reviewer_hour = 3600 / average_review_time_seconds

high_value_candidates_per_hour =
  candidates_per_reviewer_hour * yield_rate

burden_adjusted_value =
  high_value_candidates_per_hour / cognitive_load
```

Also record:

- full-thread-reading rate;
- second-review rate;
- uncertainty rate;
- hard-negative stability;
- lane SVS;
- signal SVS movement;
- cluster/discrepancy movement.

## Success Conditions

Batch 0008 succeeds if it supports one of these decisions:

- Arm A remains much higher value than B/C/D: prioritize `strong_source_priority`
  when reviewer capacity is constrained.
- Arm B stays cheap but low yield: keep it as single-item triage, not fast
  priority.
- Arm C remains high cost and low yield: restrict it to slow context review or
  sample sparingly.
- Arm D remains low-cost non-scam: preserve it as hard-negative calibration.
- Any result-display arm improves yield meaningfully: design a narrower follow-up
  before changing sparse schema.

## Measurement Plan

After human review fills `data/candidate_intake/batch_0008_intake.yaml`, run:

```bash
./.venv/bin/python scripts/validate_candidate_intake_v2.py data/candidate_intake/batch_0008_intake.yaml --expected-count 16
./.venv/bin/python scripts/convert_candidate_intake_v2.py data/candidate_intake/batch_0008_intake.yaml --report-output data/candidate_intake/batch_0008_conversion_report.yaml
./.venv/bin/python scripts/convert_candidate_intake_v2.py data/candidate_intake/batch_0008_intake.yaml --report-output data/candidate_intake/batch_0008_conversion_report.yaml --write-candidates
./.venv/bin/python scripts/validate_candidate_v2.py data/candidates
./.venv/bin/python scripts/run_v2_ros.py
./.venv/bin/python scripts/run_contrast_aware_scoring.py
./.venv/bin/python scripts/generate_feature_candidates_v1.py
./.venv/bin/python scripts/generate_exploration_tasks.py
```

Compare:

- `metrics/contrast_scores/latest.yaml`
- `metrics/signal_scores/latest_ranking.yaml`
- `outputs/sparse_clusters/latest.yaml`
- `outputs/discrepancy_reports/latest.yaml`
- `metrics/batch_logs/batch_0008_run_log.yaml`

## Guardrails

- no raw Threads content
- no PII
- no URLs, handles, screenshots, browser artifacts, credentials, or controlled-store
  locators
- no external systems accessed by this artifact
- no embedding-based decisions
- no automatic feature promotion
- no legal fraud, enforcement, takedown, or public warning claim
