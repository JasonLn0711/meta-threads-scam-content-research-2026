# Batch 0006 Contrast-Aware Routing Validation

## Purpose

Run the smallest useful validation batch after the first contrast-aware routing
score.

Batch 0005 showed that `保證收益 + executable transition` should be routed
differently from `成果展示 + context burden`. Batch 0006 tests whether that routing
decision can reduce reviewer effort while preserving high-value candidate
discovery.

This is not a collection authorization, production detector step, legal fraud
judgment, or enforcement workflow.

## First-Principle Question

The question is not:

```text
Can the system label more scam-like content?
```

The question is:

```text
Can contrast-aware routing increase high-value candidate discovery per unit
reviewer effort?
```

## Source Evidence

Current contrast-aware routing result:

```text
strong_source_priority:
  reviewed_count: 10
  yield_rate: 1.0
  review_time: 39.4
  cognitive_load: 1.27
  svs: 0.016682973
  needs_thread_rate: 0.0
  second_review_rate: 0.0

result_display_context_review:
  reviewed_count: 9
  yield_rate: 0.0
  review_time: 45.333333
  cognitive_load: 2.305556
  svs: 0.0
  needs_thread_rate: 1.0
  second_review_rate: 0.777778
  uncertainty_rate: 0.777778
```

Source artifacts:

- `metrics/contrast_scores/latest.yaml`
- `experiments/evaluation-notes/0101-v2-contrast-aware-routing-result.md`
- `metrics/batch_logs/batch_0005_run_log.yaml`
- `outputs/research_candidates/RC_0003.md`

## Batch Design

Use four routing lanes:

```text
A: strong_source_priority
B: result_display_context_review
C: result_display_contrast_holdout
D: guarantee_context_review
```

Target size:

```text
12 candidate stubs total
4 stubs in Lane A
4 stubs in Lane B
2 stubs in Lane C
2 stubs in Lane D
```

This cap is intentional. The goal is to validate routing, not increase volume.

## Lane A: Strong Source Priority

Routing rule:

```text
保證收益 AND (誘導聯絡 OR 社群導流 OR reply_funnel OR review_stable_funnel_anchor)
AND NOT needs_thread
```

Measurement focus:

- whether high yield persists
- whether review time stays low
- whether second-review remains uncommon
- whether `needs_thread` stays low

Expected behavior:

```text
guarantee_executable_transition_fast_lane
```

## Lane B: Result Display Context Review

Routing rule:

```text
成果展示 AND NOT 保證收益 AND
(誘導聯絡 OR 社群導流 OR reply_funnel OR needs_thread OR 情緒操控)
```

Measurement focus:

- whether uncertainty remains high
- whether `needs_thread` explains review burden
- whether slow review is justified
- whether a burden-aware subfeature is needed

Expected behavior:

```text
result_display_context_cost_lane
```

## Lane C: Result Display Contrast Holdout

Routing rule:

```text
成果展示 AND NOT 保證收益 AND
NOT (誘導聯絡 OR 社群導流 OR reply_funnel OR needs_thread OR 情緒操控)
```

Measurement focus:

- hard-negative usefulness
- low-burden contrast value
- whether standalone result display should stay out of fast review

Expected behavior:

```text
standalone_result_display_holdout
```

## Lane D: Guarantee Context Review

Routing rule:

```text
保證收益 AND NOT strong_source_priority
```

Measurement focus:

- whether guarantee language without a stable transition still creates burden
- whether it needs slower priority context review
- whether `needs_thread` or second review explains uncertainty

Expected behavior:

```text
guarantee_context_edge_case
```

## Review Fields Required

Each reviewed intake entry must complete:

- all sparse feature observations as `0` or `1`
- review decision: `scam`, `non_scam`, or `uncertain`
- confidence
- review time in seconds
- second-review requirement
- completion gates confirming no raw evidence or PII entered the repo

## Success Conditions

Batch 0006 succeeds if it produces one of these decisions:

- Lane A keeps high SVS and low burden: keep fast-priority routing.
- Lane B stays high burden and high uncertainty: route broad result-display context
  candidates to slow review.
- Lane C remains low-burden non-scam or uncertain: preserve it as hard-negative
  calibration.
- Lane D separates from Lane A by burden: keep guarantee context as slower priority
  review.
- Any lane changes unexpectedly: write a feature candidate or revise routing before
  scaling.

## Result Artifact

Post-review result is recorded in:

- `experiments/batch_variants/0006-post-review-routing-result.md`
- `metrics/batch_logs/batch_0006_run_log.yaml`
- `outputs/research_candidates/RC_0004.md`

## Measurement Plan

After human review fills `data/candidate_intake/batch_0006_intake.yaml`, run:

```bash
./.venv/bin/python scripts/validate_candidate_intake_v2.py data/candidate_intake/batch_0006_intake.yaml --expected-count 12
./.venv/bin/python scripts/convert_candidate_intake_v2.py data/candidate_intake/batch_0006_intake.yaml --report-output data/candidate_intake/batch_0006_conversion_report.yaml
./.venv/bin/python scripts/convert_candidate_intake_v2.py data/candidate_intake/batch_0006_intake.yaml --report-output data/candidate_intake/batch_0006_conversion_report.yaml --write-candidates
./.venv/bin/python scripts/validate_candidate_v2.py data/candidates
./.venv/bin/python scripts/run_v2_ros.py
./.venv/bin/python scripts/generate_feature_candidates_v1.py
./.venv/bin/python scripts/generate_exploration_tasks.py
```

Compare:

- `metrics/contrast_scores/latest.yaml`
- `metrics/signal_scores/latest_ranking.yaml`
- `outputs/sparse_clusters/latest.yaml`
- `outputs/discrepancy_reports/latest.yaml`
- `metrics/batch_logs/batch_0006_run_log.yaml`

## Guardrails

- no raw Threads content
- no PII
- no URLs, handles, screenshots, browser artifacts, credentials, or controlled-store
  locators
- no external systems accessed by this artifact
- no embedding-based decisions
- no automatic feature promotion
- no legal fraud, enforcement, takedown, or public warning claim
