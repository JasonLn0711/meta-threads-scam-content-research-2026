# Batch 0007 Result-Display Context Split

## Purpose

Test the current bottleneck after Batch 0006: `result_display_context_review`
is useful as a slow lane, but it is still too broad.

Batch 0007 does not expand collection volume. It creates a capped
manual-assisted review batch to test whether broad result-display context cases
can be split into lower-cost and higher-cost sub-lanes using structured metadata
only.

This is not a collection authorization, production detector step, legal fraud
judgment, or enforcement workflow.

## First-Principle Question

The question is not:

```text
Are result-display cases scam or non-scam?
```

The question is:

```text
Can the system route result-display cases by reviewer burden before spending
full review effort?
```

## Source Evidence

Batch 0006 showed:

```text
result_display_context_review:
  reviewed_count: 4
  scam_count: 0
  uncertain_count: 4
  review_time: 49.75
  needs_thread_rate: 1.0
  second_review_rate: 1.0
  uncertainty_rate: 1.0
  svs: 0.0
```

Global contrast-aware score after Batch 0006:

```text
result_display_context_review:
  reviewed_count: 13
  scam_count: 0
  uncertain_count: 11
  review_time: 46.692308
  needs_thread_rate: 1.0
  second_review_rate: 0.846154
  uncertainty_rate: 0.846154
  svs: 0.0
```

Source artifacts:

- `experiments/batch_variants/0006-post-review-routing-result.md`
- `metrics/batch_logs/batch_0006_run_log.yaml`
- `metrics/contrast_scores/latest.yaml`
- `outputs/research_candidates/RC_0004.md`

## Batch Design

Use four result-display sub-lanes:

```text
A: result_display_low_context_transition
B: result_display_thread_required
C: result_display_emotional_thread_required
D: result_display_clean_holdout
```

Target size:

```text
12 candidate stubs total
3 stubs per sub-lane
```

The cap is intentional. The goal is to test routing precision, not increase
candidate volume.

## Lane A: Result Display Low-Context Transition

Routing hypothesis:

```text
成果展示 AND NOT 保證收益 AND (誘導聯絡 OR reply_funnel) AND NOT needs_thread
```

Measurement focus:

- whether the case can be reviewed with lower time cost;
- whether second review stays lower than Lane B and Lane C;
- whether visible transition structure is enough to reduce context burden;
- whether the lane still remains low direct positive yield.

Expected behavior:

```text
result_display_visible_transition_low_context
```

## Lane B: Result Display Thread Required

Routing hypothesis:

```text
成果展示 AND NOT 保證收益 AND needs_thread AND NOT 情緒操控
```

Measurement focus:

- whether thread requirement alone explains slow review;
- whether uncertainty remains high;
- whether this lane should stay slow but not second-review-heavy by default.

Expected behavior:

```text
result_display_thread_context_required
```

## Lane C: Result Display Emotional Thread Required

Routing hypothesis:

```text
成果展示 AND NOT 保證收益 AND needs_thread AND 情緒操控
```

Measurement focus:

- whether emotional pressure plus thread requirement increases second-review
  burden;
- whether this sub-lane deserves higher context-review priority;
- whether `情緒操控` is amplifying reviewer cost rather than positive yield.

Expected behavior:

```text
result_display_emotional_context_burden
```

## Lane D: Result Display Clean Holdout

Routing hypothesis:

```text
成果展示 AND NOT 保證收益 AND NOT (誘導聯絡 OR 社群導流 OR reply_funnel OR needs_thread OR 情緒操控)
```

Measurement focus:

- hard-negative calibration;
- baseline review time;
- whether standalone result display remains low burden;
- whether this holdout prevents over-generalizing `成果展示`.

Expected behavior:

```text
standalone_result_display_holdout
```

## Candidate Feature Under Review

Batch 0007 tests, but does not promote, this feature hypothesis:

```text
feature_id: context_required_result_display
activation_rule: 成果展示 AND needs_thread AND NOT 保證收益
```

The feature proposal is stored at:

- `meta-system/feature_candidates/context_required_result_display.yaml`

It must remain pending unless a human reviewer explicitly accepts it in:

- `meta-system/feature_review_queue/latest.yaml`

## Review Fields Required

Each reviewed intake entry must complete:

- all sparse feature observations as `0` or `1`;
- review decision: `scam`, `non_scam`, or `uncertain`;
- confidence;
- review time in seconds;
- second-review requirement;
- completion gates confirming no raw evidence or PII entered the repo.

## Success Conditions

Batch 0007 succeeds if it produces one of these decisions:

- Lane A review time is lower than Lane B or Lane C: create a low-context
  transition routing rule.
- Lane B and Lane C both stay high burden: keep all result-display context cases
  in slow review.
- Lane C is more second-review-heavy than Lane B: consider a separate
  emotional-context burden feature candidate.
- Lane D remains low-burden and non-scam or uncertain: preserve it as hard-negative
  calibration.
- No lane separates: do not add features; keep Batch 0006 routing and stop
  optimizing this branch for now.

## Measurement Plan

After human review fills `data/candidate_intake/batch_0007_intake.yaml`, run:

```bash
./.venv/bin/python scripts/validate_candidate_intake_v2.py data/candidate_intake/batch_0007_intake.yaml --expected-count 12
./.venv/bin/python scripts/convert_candidate_intake_v2.py data/candidate_intake/batch_0007_intake.yaml --report-output data/candidate_intake/batch_0007_conversion_report.yaml
./.venv/bin/python scripts/convert_candidate_intake_v2.py data/candidate_intake/batch_0007_intake.yaml --report-output data/candidate_intake/batch_0007_conversion_report.yaml --write-candidates
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
- `metrics/batch_logs/batch_0007_run_log.yaml`

## Guardrails

- no raw Threads content
- no PII
- no URLs, handles, screenshots, browser artifacts, credentials, or controlled-store
  locators
- no external systems accessed by this artifact
- no embedding-based decisions
- no automatic feature promotion
- no legal fraud, enforcement, takedown, or public warning claim
