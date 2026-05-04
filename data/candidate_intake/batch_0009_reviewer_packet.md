# Batch 0009 Reviewer Packet

## Purpose

Batch 0009 tests the active context-gating policy prospectively.

The goal is not to balance all lanes equally. The goal is to see whether a
policy-weighted allocation improves high-value candidate discovery per reviewer
hour while preserving hard-negative calibration and limiting slow-context
review.

Use this packet together with:

- `docs/63-context-gating-policy.md`
- `data/candidate_intake/batch_0009_intake.yaml`
- `data/candidate_stubs/batch_0009.yaml`
- `experiments/batch_variants/0009-context-gating-policy-check.md`
- `metrics/contrast_scores/latest.yaml`

## First-Principle Decision

Batch 0009 answers one operating-system question:

```text
Does the context-gating policy improve reviewer-hour value when it controls
which metadata stubs receive review capacity?
```

This batch is capped at 12 intake entries because the purpose is policy checking,
not collection scale.

## Allocation

This is intentionally not a balanced experiment.

```text
A: strong_source_priority                 8 entries
B: result_display_clean_holdout           2 entries
C: result_display_low_context_transition  1 entry
D: result_display_thread_required         1 entry
```

The policy is:

```text
prioritize fast lane
preserve hard-negative calibration
keep boundary probes tiny
keep slow-context probes tiny
```

## Routing Arms

Arm A:

```text
strong_source_priority
```

Expected structure: `保證收益` plus executable transition structure, with
`needs_thread` expected absent. This is the fast reviewer-priority lane.

Arm B:

```text
result_display_clean_holdout
```

Expected structure: standalone `成果展示` without guarantee, contact, group, reply,
thread, or emotional pressure cues. This is hard-negative calibration.

Arm C:

```text
result_display_low_context_transition
```

Expected structure: `成果展示` plus visible transition metadata, with
`needs_thread` expected absent. This is cheap boundary triage.

Arm D:

```text
result_display_thread_required
```

Expected structure: `成果展示` plus thread dependency, without explicit
`保證收益` or `情緒操控`. This is a slow-context diagnostic probe.

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

## Arm-Specific Review Cues

`INTAKE_0009_A_01` through `INTAKE_0009_A_08`:
Test whether the fast lane remains high-yield and low-burden when it receives
most reviewer capacity.

`INTAKE_0009_B_01` through `INTAKE_0009_B_02`:
Check hard-negative stability and protect against over-generalizing
`成果展示`.

`INTAKE_0009_C_01`:
Keep one low-context result-display boundary probe alive without letting it
consume priority capacity.

`INTAKE_0009_D_01`:
Keep one slow-context diagnostic probe alive without letting thread-required
review dominate the batch.

## Structured Hints

Fill these with category-level descriptions only:

- `common_behaviors`
- `structural_patterns`
- `reviewer_signals`
- `hard_negative_contrast`

Allowed examples:

- `guarantee_executable_transition`
- `clean_result_display_holdout`
- `visible_transition_low_context`
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
- review time becomes too high for the capped reviewer-hour test
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
./.venv/bin/python scripts/validate_candidate_intake_v2.py data/candidate_intake/batch_0009_intake.yaml --expected-count 12
./.venv/bin/python scripts/convert_candidate_intake_v2.py data/candidate_intake/batch_0009_intake.yaml --report-output data/candidate_intake/batch_0009_conversion_report.yaml
./.venv/bin/python scripts/convert_candidate_intake_v2.py data/candidate_intake/batch_0009_intake.yaml --report-output data/candidate_intake/batch_0009_conversion_report.yaml --write-candidates
./.venv/bin/python scripts/validate_candidate_v2.py data/candidates
./.venv/bin/python scripts/run_v2_ros.py
./.venv/bin/python scripts/run_contrast_aware_scoring.py
./.venv/bin/python scripts/generate_feature_candidates_v1.py
./.venv/bin/python scripts/generate_exploration_tasks.py
```
