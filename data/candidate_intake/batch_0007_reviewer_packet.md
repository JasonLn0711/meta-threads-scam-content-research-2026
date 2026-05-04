# Batch 0007 Reviewer Packet

## Purpose

This packet turns Batch 0007 into a low-burden routing-split task.

The goal is not to decide legal fraud. The goal is to test whether broad
`result_display_context_review` cases can be split into lower-cost and
higher-cost review lanes using structured metadata only.

Use this packet together with:

- `data/candidate_intake/batch_0007_intake.yaml`
- `data/candidate_stubs/batch_0007.yaml`
- `experiments/batch_variants/0007-result-display-context-split.md`
- `metrics/contrast_scores/latest.yaml`

## First-Principle Decision

Batch 0007 answers one operating-system question:

```text
Should result-display context cases stay one slow lane, or can the system split
them into review-cost sub-lanes before spending full reviewer effort?
```

This batch is capped at 12 intake entries because the purpose is routing
precision, not collection scale.

## Routing Lanes

Lane A:

```text
result_display_low_context_transition
```

Expected structure: `成果展示` plus visible transition metadata, with
`needs_thread` expected absent.

Lane B:

```text
result_display_thread_required
```

Expected structure: `成果展示` plus thread dependency, without explicit
`保證收益` or emotional-pressure amplification.

Lane C:

```text
result_display_emotional_thread_required
```

Expected structure: `成果展示` plus both thread dependency and `情緒操控`.

Lane D:

```text
result_display_clean_holdout
```

Expected structure: standalone `成果展示` without guarantee, contact, group, reply,
thread, or emotional pressure cues.

## Fill Rules

Fill sparse features as `0` or `1` only.

`decision` must be one of:

- `scam`
- `non_scam`
- `uncertain`

This is a research label only. It is not a legal fraud label and not an
enforcement recommendation.

Record actual elapsed `review_time_seconds`. Do not estimate after the fact if
timing was not observed.

Set `second_review_required: true` when a second reviewer is needed because the
case is ambiguous, high-impact, or hard to classify from structured metadata.

## Lane-Specific Review Cues

`INTAKE_0007_A_01` through `INTAKE_0007_A_03`:
Test whether visible transition metadata can reduce review time when no full
thread is needed. Do not assume positive yield.

`INTAKE_0007_B_01` through `INTAKE_0007_B_03`:
Test whether `needs_thread` alone explains slow review. The expected signal is
review cost, not label direction.

`INTAKE_0007_C_01` through `INTAKE_0007_C_03`:
Test whether `needs_thread + 情緒操控` creates a higher second-review burden than
Lane B.

`INTAKE_0007_D_01` through `INTAKE_0007_D_03`:
Test hard-negative or boundary value. These cases should remain useful even if
they do not produce positive yield.

## Structured Hints

Fill these with category-level descriptions only:

- `common_behaviors`
- `structural_patterns`
- `reviewer_signals`
- `hard_negative_contrast`

Allowed examples:

- `result_display_visible_transition`
- `thread_context_required`
- `emotional_context_burden`
- `standalone_result_holdout`
- `hard_negative_boundary`
- `low_context_transition`

Do not paste raw wording, handles, identifiers, links, screenshots, browser
artifacts, or controlled-store locators.

## Stop Rules

Stop the batch entry instead of filling it if any of these are required:

- raw Threads content would need to be pasted into this repo
- PII, handles, links, screenshots, browser artifacts, or credentials would need
  to be stored
- a controlled-store locator would need to be stored
- routing cannot be assessed without raw evidence leakage
- review time becomes too high for the capped routing-split study
- the case would require an enforcement, legal, or public-warning judgment

## Done Condition

The batch is ready to enter the v2 ROS only when:

- all 12 intake entries have `fill_status: completed`
- every sparse feature is `0` or `1`
- every review field is filled
- every completion gate is `true`
- the conversion report shows `blocked_count: 0`

Then run:

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
