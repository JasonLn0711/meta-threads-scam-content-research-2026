# Decision 0146: Open Reviewer Assist Evaluation Execution Workbench

Date: 2026-05-05

Status: opened as execution workbench; no assisted-review result yet

## Decision

Open a metadata-only execution workbench for Decision `0145`.

The workbench turns the Reviewer Assist labor-savings evaluation from a design
package into a fillable evaluation slice. It uses Batch `0009` as the manual
baseline and prepares the same repo-safe candidate slice for an assisted-review
condition.

This decision does not close the evaluation. It records that the next concrete
step is to fill the assisted-review condition and then synthesize aggregate-only
results.

## Why This Is The Next Step

Decision `0143` records that current collected examples are partial fragments,
not a representative map of all Threads investment scams. Decision `0144`
records governed automatic or assisted candidate discovery as the single highest
priority. Decision `0145` opens the labor-savings evaluation package.

The next step therefore should not summarize known cases or infer broad scam
patterns. It should test whether Reviewer Assist can reduce review burden while
preserving the discovery method's quality controls.

## What This Opens

This decision opens:

- a metadata-only work order under `data/reviewer_assist_eval/`;
- a result workbench under `experiments/evaluation-notes/`;
- a controlled path for comparing Batch `0009` manual baseline metrics against
  a later assisted-review condition;
- a rule that assisted-review outputs remain pending until human review fills
  the required fields.

## Baseline

Use Batch `0009` as the manual baseline:

```text
reviewed_count: 12
yield_rate: 0.666667
average_review_time_seconds: 37.333333
candidates_per_reviewer_hour: 96.428571
high_value_candidates_per_hour: 64.285714
needs_thread_rate: 0.083333
second_review_rate: 0.25
uncertainty_rate: 0.166667
```

These are baseline comparison metrics only. They do not establish platform-wide
coverage, a complete taxonomy, legal fraud, or production detector readiness.

## Required Assisted-Review Fill

The assisted condition must fill, for each candidate:

- reviewer-facing candidate summary usefulness;
- signal-family suggestion acceptance or correction;
- schema-prefill acceptance or correction;
- hard-negative warning acceptance or correction;
- priority explanation acceptance or correction;
- missing-evidence note acceptance or correction;
- human final label or explicit `not_reviewable`;
- review time;
- second-review requirement;
- insufficient-evidence flag;
- raw-evidence exclusion confirmation.

## What This Does Not Open

This decision does not authorize:

- new Threads or Meta data collection;
- live Threads access;
- raw Threads text, raw reply text, raw OCR text, raw URLs, handles, screenshots,
  browser/session artifacts, credentials, stakeholder case IDs, or
  controlled-store locators in git;
- model training;
- real LLM/API calls;
- automated final scam decisions;
- legal fraud determinations;
- enforcement recommendations;
- public warnings;
- production detector claims.

## Workbench Artifacts

- `data/reviewer_assist_eval/README.md`
- `data/reviewer_assist_eval/batch_0010_work_order.yaml`
- `experiments/evaluation-notes/0107-reviewer-assist-labor-savings-evaluation-result.md`

## Next Review Point

After the assisted-review fields are filled, update the result workbench with
aggregate-only metrics and choose one:

- `expand_assist_evaluation`;
- `revise_assist_design`;
- `keep_shadow_only`;
- `pause_assist_layer`;
- `request_new_governed_source_slice`.
