# Decision 0148: Open Reviewer Assist Expansion Slice On Batch 0008

Date: 2026-05-05

Status: opened as metadata-only expansion workbench

## Decision

Open the next bounded Reviewer Assist evaluation slice after Decision `0147`.

Use Batch `0008` as the manual baseline for a second metadata-only
Reviewer Assist shadow evaluation. This expands beyond the Batch `0009`
policy-weighted slice by testing a balanced context-gating slice with four
lanes:

- `strong_source_priority`;
- `result_display_low_context_transition`;
- `result_display_thread_required`;
- `result_display_clean_holdout`.

This decision opens the workbench only. It does not record assisted-review
results yet.

## Why Batch 0008

Decision `0147` selected `expand_assist_evaluation`, but the first result used
Batch `0009`, a policy-weighted slice. Repeating only Batch `0009` would risk
overfitting the evaluation to one high-yield routing design.

Batch `0008` is a better next slice because it contains:

- a fast high-yield lane;
- a low-context boundary lane;
- a slow thread-required diagnostic lane;
- a hard-negative clean holdout lane.

That mix tests whether Reviewer Assist reduces burden not only in easy
fast-lane cases, but also in ambiguous and hard-negative calibration lanes.

## Baseline

Use Batch `0008` as the manual baseline:

```text
reviewed_count: 16
scam_count: 4
non_scam_count: 4
uncertain_count: 8
yield_rate: 0.25
average_review_time_seconds: 41.875
candidates_per_reviewer_hour: 85.970149
high_value_candidates_per_hour: 21.492537
needs_thread_rate: 0.25
second_review_rate: 0.375
uncertainty_rate: 0.5
```

These are baseline comparison metrics only. They do not prove platform-wide
coverage or production readiness.

## What This Opens

- `experiments/batch_variants/0011-reviewer-assist-expansion-batch-0008.md`
- `data/reviewer_assist_eval/batch_0011_work_order.yaml`
- `experiments/evaluation-notes/0108-reviewer-assist-expansion-batch-0008-result.md`

## Required Assisted-Review Fill

The assisted condition must fill, for each candidate:

- candidate summary usefulness;
- summary omission risk;
- signal suggestion acceptance or correction;
- schema-prefill acceptance or correction;
- hard-negative warning acceptance or correction;
- priority explanation acceptance or correction;
- human final label or explicit `not_reviewable`;
- assisted review time;
- second-review requirement;
- insufficient-evidence flag;
- raw-evidence exclusion confirmation.

## What This Does Not Open

This decision does not authorize:

- new Threads or Meta data collection;
- live Threads access;
- raw Threads text, raw reply text, raw OCR text, raw URLs, handles,
  screenshots, browser/session artifacts, credentials, stakeholder case IDs, or
  controlled-store locators in git;
- model training;
- real LLM/API calls;
- automated final scam decisions;
- legal fraud determinations;
- enforcement recommendations;
- public warnings;
- production detector claims.

## Next Review Point

After the assisted-review fields are filled, produce an aggregate-only result
under:

```text
experiments/evaluation-notes/0108-reviewer-assist-expansion-batch-0008-result.md
```

Select one:

- `expand_assist_evaluation`;
- `revise_assist_design`;
- `keep_shadow_only`;
- `pause_assist_layer`;
- `request_new_governed_source_slice`.
