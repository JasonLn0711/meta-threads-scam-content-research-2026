# Batch 0006 Reviewer Packet

## Purpose

This packet turns Batch 0006 into a low-burden routing validation task.

The goal is not to decide legal fraud. The goal is to test whether
contrast-aware routing improves high-value candidate discovery per unit reviewer
effort.

Use this packet together with:

- `data/candidate_intake/batch_0006_intake.yaml`
- `data/candidate_stubs/batch_0006.yaml`
- `experiments/batch_variants/0006-contrast-aware-routing-validation.md`
- `metrics/contrast_scores/latest.yaml`

## First-Principle Decision

Batch 0006 answers one operating-system question:

```text
Should the system route 保證收益 + executable transition to fast priority review
and 成果展示 + context burden to slow context review?
```

This batch is capped at 12 intake entries because the purpose is routing
validation, not collection scale.

## Routing Lanes

Lane A:

```text
strong_source_priority
```

Expected structure: `保證收益` plus contact/group/reply/funnel anchor, with
`needs_thread` expected absent.

Lane B:

```text
result_display_context_review
```

Expected structure: `成果展示` without `保證收益`, plus context burden such as
contact, group, reply, thread, or emotional pressure.

Lane C:

```text
result_display_contrast_holdout
```

Expected structure: standalone `成果展示` without guarantee, contact, group, reply,
thread, or emotional pressure cues.

Lane D:

```text
guarantee_context_review
```

Expected structure: `保證收益` is present, but the transition is weak, unstable,
or context-heavy.

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

`INTAKE_0006_A_01` through `INTAKE_0006_A_04`:
Test whether guarantee plus executable transition can be reviewed quickly without
thread context. If `needs_thread` becomes true, explain the burden using
structured hints only.

`INTAKE_0006_B_01` through `INTAKE_0006_B_04`:
Test whether result display without guarantee remains context-costly. Do not
label it safe just because `保證收益` is absent.

`INTAKE_0006_C_01` and `INTAKE_0006_C_02`:
Test hard-negative or boundary value. These should stay useful even if they do
not produce positive yield.

`INTAKE_0006_D_01` and `INTAKE_0006_D_02`:
Test guarantee edge cases. The key question is whether a guarantee cue without
stable transition belongs in slower priority context review.

## Structured Hints

Fill these with category-level descriptions only:

- `common_behaviors`
- `structural_patterns`
- `reviewer_signals`
- `hard_negative_contrast`

Allowed examples:

- `guarantee_executable_transition`
- `result_display_context_cost`
- `standalone_result_holdout`
- `guarantee_context_edge`
- `thread_context_required`
- `hard_negative_boundary`

Do not paste raw wording, handles, identifiers, links, screenshots, browser
artifacts, or controlled-store locators.

## Stop Rules

Stop the batch entry instead of filling it if any of these are required:

- raw Threads content would need to be pasted into this repo
- PII, handles, links, screenshots, browser artifacts, or credentials would need
  to be stored
- a controlled-store locator would need to be stored
- routing cannot be assessed without raw evidence leakage
- review time becomes too high for the capped routing study
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
./.venv/bin/python scripts/validate_candidate_intake_v2.py data/candidate_intake/batch_0006_intake.yaml --expected-count 12
./.venv/bin/python scripts/convert_candidate_intake_v2.py data/candidate_intake/batch_0006_intake.yaml --report-output data/candidate_intake/batch_0006_conversion_report.yaml
./.venv/bin/python scripts/convert_candidate_intake_v2.py data/candidate_intake/batch_0006_intake.yaml --report-output data/candidate_intake/batch_0006_conversion_report.yaml --write-candidates
./.venv/bin/python scripts/validate_candidate_v2.py data/candidates
./.venv/bin/python scripts/run_v2_ros.py
./.venv/bin/python scripts/generate_feature_candidates_v1.py
./.venv/bin/python scripts/generate_exploration_tasks.py
```
