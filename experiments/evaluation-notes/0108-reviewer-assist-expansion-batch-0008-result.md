# 0108 - Reviewer Assist Expansion Batch 0008 Result

Date: 2026-05-05

Status: empirical assisted-review result completed

Decision record: `decision-log/0149-record-reviewer-assist-expansion-batch-0011-result.md`

## Purpose

This note records the empirical metadata-only assisted-review result for
Decision `0148`.

It expands the Reviewer Assist evaluation after Decision `0147` by using Batch
`0008`, a balanced context-gating baseline with fast, boundary, slow-context,
and hard-negative calibration lanes.

## Boundary

This is an empirical assisted-review result for the Batch `0011` workbench.
It is still metadata-only and repo-safe:

- no raw Threads post text, reply text, OCR text, URLs, handles, screenshots,
  browser artifacts, controlled-store locators, credentials, or private evidence
  are stored in git;
- reviewer-facing rules and fill sheets hide the manual baseline labels,
  confidence, review times, and second-review decisions;
- the result is not a platform-wide Threads investment-scam claim;
- the result is not a legal fraud, enforcement, public-warning, model-training,
  production-detector, or final automated scam-decision claim.

## Inputs

- Decision: `decision-log/0148-open-reviewer-assist-expansion-slice-batch-0008.md`
- Result decision: `decision-log/0149-record-reviewer-assist-expansion-batch-0011-result.md`
- Experiment plan: `experiments/batch_variants/0011-reviewer-assist-expansion-batch-0008.md`
- Work order: `data/reviewer_assist_eval/batch_0011_work_order.yaml`
- Reviewer-facing rules: `data/reviewer_assist_eval/batch_0011_reviewer_rules.md`
- Reviewer-facing fill template: `data/reviewer_assist_eval/batch_0011_reviewer_fill_sheet_template.yaml`
- Assisted-review result: `data/reviewer_assist_eval/batch_0011_assisted_review_result.yaml`
- Aggregate result: `data/reviewer_assist_eval/batch_0011_aggregate_result.yaml`
- Manual baseline result: `experiments/evaluation-notes/0104-v2-batch-0008-reviewer-hour-value-result.md`
- Manual baseline run log: `metrics/batch_logs/batch_0008_run_log.yaml`

## Aggregate Result

| Metric | Manual baseline | Assisted review | Difference |
|---|---:|---:|---:|
| Reviewed candidates | 16 | 16 | 0 |
| Total review seconds | 670.0 | 530.0 | -140.0 |
| Average review seconds | 41.875 | 33.125 | -8.75 |
| Median review seconds | 38.5 | 29.5 | -9.0 |
| P95 review seconds | 60.0 | 54.0 | -6.0 |
| Candidates reviewed per hour | 85.970149 | 108.679245 | +22.709096 |
| High-value candidates per reviewer hour | 21.492537 | 27.169811 | +5.677274 |
| Scam / high-value count | 4 | 4 | 0 |
| Non-scam count | 4 | 4 | 0 |
| Uncertain count | 8 | 8 | 0 |
| Yield rate | 0.25 | 0.25 | 0.0 |
| Uncertainty rate | 0.5 | 0.5 | 0.0 |
| Second-review rate | 0.375 | 0.5 | +0.125 |
| Raw-evidence leakage incidents | 0 required | 0 | 0 |

The assisted condition reduced average review time by `20.895522%` and raised
candidates reviewed per hour by `26.415094%`. High-value candidates per reviewer
hour rose by `26.415096%` because the final label mix stayed stable while total
review time fell.

## Assist Quality

| Metric | Assisted review |
|---|---:|
| Summary usefulness mean | 3.9375 |
| Summary rating 4-5 percent | 0.75 |
| Schema-prefill accepted | 8 |
| Schema-prefill accepted with minor correction | 8 |
| Signal suggestions accepted | 8 |
| Signal suggestions accepted with minor correction | 8 |
| Hard-negative warning accepted or not applicable | 16 |
| Priority explanation accepted | 16 |
| Insufficient-evidence rate | 0.5 |

## Lane Result

| Lane | Count | Assisted avg seconds | Final labels | Interpretation |
|---|---:|---:|---|---|
| `strong_source_priority` | 4 | 23.0 | 4 scam | Fast-lane orientation is strong. |
| `result_display_low_context_transition` | 4 | 33.75 | 4 uncertain | Assist helps schema orientation but does not resolve boundary uncertainty. |
| `result_display_thread_required` | 4 | 51.75 | 4 uncertain | Context dependency remains the main bottleneck. |
| `result_display_clean_holdout` | 4 | 24.0 | 4 non-scam | Hard-negative calibration remains protected. |

## Interpretation

Batch `0011` supports continued Reviewer Assist evaluation. The assisted review
condition reduced review burden while preserving the same high-value count,
non-scam count, uncertainty rate, and raw-evidence exclusion boundary.

The increase in second-review rate is not treated as a failure by itself. In
this slice, it reflects conservative uncertainty handling in boundary and
thread-required lanes. The design risk is narrower: when thread context is the
main bottleneck, metadata-only assistance helps orientation but cannot replace
the missing context.

## Decision

Selected option: `expand_assist_evaluation`

Expansion is bounded. It does not authorize new collection, live Threads/Meta
automation, real LLM/API calls, model training, production detection, or final
automated scam decisions.

The next Reviewer Assist design step should preserve the fast-lane and
hard-negative behaviors while revising the `result_display_thread_required`
lane so missing thread context is surfaced earlier and does not look like a
solved classification problem.
