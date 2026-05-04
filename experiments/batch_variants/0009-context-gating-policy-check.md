# Batch 0009 Context-Gating Policy Check

## Purpose

Batch 0009 tests whether the Batch 0008 context-gating policy improves reviewer
allocation when used prospectively.

The goal is not to classify more cases. The goal is to test whether a policy
derived from reviewed metadata can allocate scarce reviewer time toward higher
value lanes while preserving hard-negative calibration and limiting slow-context
burden.

This is not a collection authorization, production detector step, legal fraud
judgment, enforcement workflow, public-warning workflow, model-training step, or
raw-evidence storage step.

## First-Principle Question

The question is:

```text
Does using the context-gating policy improve high-value candidate discovery per
reviewer hour compared with the balanced Batch 0008 design?
```

The question is not:

```text
Can the system decide whether content is scam?
```

## Source Evidence

Batch 0008 established:

```text
strong_source_priority:
  yield_rate: 1.0
  average_review_time_seconds: 33.25
  high_value_candidates_per_hour: 108.270677
  needs_thread_rate: 0.0
  second_review_rate: 0.0

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
  needs_thread_rate: 0.0
  second_review_rate: 0.0
```

Source artifacts:

- `docs/63-context-gating-policy.md`
- `experiments/evaluation-notes/0104-v2-batch-0008-reviewer-hour-value-result.md`
- `metrics/batch_logs/batch_0008_run_log.yaml`
- `metrics/contrast_scores/latest.yaml`
- `metrics/signal_scores/latest_ranking.yaml`
- `outputs/research_candidates/RC_0007.md`

## Batch Design

Use a policy-weighted allocation instead of balanced arms:

```text
A: strong_source_priority                 8 stubs
B: result_display_clean_holdout           2 stubs
C: result_display_low_context_transition  1 stub
D: result_display_thread_required         1 stub
```

Total size:

```text
12 candidate stubs
```

This cap is intentional. Batch 0009 is a policy-check batch, not a scale test.

## Arm A: Fast Priority Review

Routing hypothesis:

```text
保證收益 AND
(誘導聯絡 OR 社群導流 OR reply_funnel OR review_stable_funnel_anchor)
AND NOT needs_thread
```

Allocation:

```text
8 / 12 stubs
```

Measurement focus:

- whether high yield survives a policy-weighted follow-up;
- whether review time remains low;
- whether second-review and full-thread burden stay low;
- whether batch-level high-value candidates per hour improves over Batch 0008.

Expected behavior:

```text
guarantee_executable_transition_fast_lane
```

## Arm B: Hard-Negative Calibration

Routing hypothesis:

```text
成果展示 AND NOT 保證收益 AND
NOT (誘導聯絡 OR 社群導流 OR reply_funnel OR needs_thread OR 情緒操控)
```

Allocation:

```text
2 / 12 stubs
```

Measurement focus:

- preserve hard-negative boundary;
- check that result-display clean holdouts remain low burden;
- protect against over-generalizing `成果展示`.

Expected behavior:

```text
clean_result_display_holdout
```

## Arm C: Cheap Boundary Triage

Routing hypothesis:

```text
成果展示 AND NOT 保證收益 AND NOT needs_thread AND
(誘導聯絡 OR 社群導流 OR reply_funnel OR review_stable_funnel_anchor)
```

Allocation:

```text
1 / 12 stub
```

Measurement focus:

- keep one boundary probe alive without letting it consume priority capacity;
- verify whether uncertainty remains high;
- verify whether second-review pressure appears even without full-thread burden.

Expected behavior:

```text
result_display_boundary_triage
```

## Arm D: Slow Context Diagnostic

Routing hypothesis:

```text
成果展示 AND NOT 保證收益 AND needs_thread AND NOT 情緒操控
```

Allocation:

```text
1 / 12 stub
```

Measurement focus:

- keep one slow-context diagnostic sample;
- confirm whether the lane remains high burden;
- prevent thread-required review from dominating the reviewer-hour budget.

Expected behavior:

```text
result_display_thread_required_diagnostic
```

## Expected Reviewer-Hour Effect

Batch 0009 should improve batch-level reviewer-hour value only if the
policy-weighted allocation keeps fast-lane yield high and does not let
result-display diagnostics dominate review time.

Expected comparison target:

```text
Batch 0008 high_value_candidates_per_hour: 21.492537
Batch 0008 batch_svs: 0.001386349
```

Success is not guaranteed. If the fast lane degrades, the policy must be revised.

## Success Conditions

Batch 0009 supports the policy if:

- batch-level high-value candidates per reviewer hour improves over Batch 0008;
- `strong_source_priority` remains high-yield and low-burden;
- clean holdout remains stable enough for hard-negative calibration;
- low-context and thread-required result-display probes remain capped;
- no sparse feature is promoted without human acceptance.

## Failure Conditions

Batch 0009 weakens the policy if:

- `strong_source_priority` yield drops below `0.75`;
- fast-lane average review time rises above `40` seconds;
- batch-level high-value candidates per hour does not improve over Batch 0008;
- the holdout lane becomes ambiguous;
- the slow-context lane again consumes high review time without discovery value;
- the batch creates pressure to treat `成果展示` as a positive-yield signal by
  itself.

## Measurement Plan

After human review fills `data/candidate_intake/batch_0009_intake.yaml`, run:

```bash
./.venv/bin/python scripts/validate_candidate_intake_v2.py data/candidate_intake/batch_0009_intake.yaml --expected-count 12
./.venv/bin/python scripts/convert_candidate_intake_v2.py data/candidate_intake/batch_0009_intake.yaml --report-output data/candidate_intake/batch_0009_conversion_report.yaml
./.venv/bin/python scripts/convert_candidate_intake_v2.py data/candidate_intake/batch_0009_intake.yaml --report-output data/candidate_intake/batch_0009_conversion_report.yaml --write-candidates
./.venv/bin/python scripts/validate_candidate_v2.py data/candidates
./.venv/bin/python scripts/run_v2_ros.py
./.venv/bin/python scripts/run_contrast_aware_scoring.py
./.venv/bin/python scripts/generate_feature_candidates_v1.py
./.venv/bin/python scripts/generate_exploration_tasks.py
```

Compare:

- `metrics/batch_logs/batch_0009_run_log.yaml`
- `metrics/contrast_scores/latest.yaml`
- `metrics/signal_scores/latest_ranking.yaml`
- `outputs/sparse_clusters/latest.yaml`
- `outputs/discrepancy_reports/latest.yaml`

## Guardrails

- no raw Threads content
- no PII
- no URLs, handles, screenshots, browser artifacts, credentials, or controlled-store
  locators
- no sparse schema auto-promotion
- no embedding-based decision
- no legal, enforcement, public-warning, or production-detector claim
