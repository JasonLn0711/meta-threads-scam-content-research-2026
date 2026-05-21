# 0010 - Reviewer Assist Labor-Savings Evaluation

## Purpose

Test whether Reviewer Assist improves the governed automatic or assisted discovery method by reducing review burden while preserving candidate quality, hard-negative protection, and human final judgment.

This is not a new collection batch. It is an evaluation design for comparable metadata-only review slices.

## First-Principle Question

```text
Can assisted review improve automatic or assisted discovery of review-worthy
Threads investment-scam candidates beyond current fragments without increasing
false-positive, hard-negative, or governance risk?
```

## Baseline

Use Batch 0009 as the routing baseline:

- `strong_source_priority` receives scarce reviewer capacity first;
- `result_display_clean_holdout` preserves hard-negative calibration;
- `result_display_low_context_transition` remains capped boundary triage;
- `result_display_thread_required` remains capped slow-context diagnostics.

Batch 0009 produced:

```text
reviewed_count: 12
yield_rate: 0.666667
average_review_time_seconds: 37.333333
high_value_candidates_per_hour: 64.285714
second_review_rate: 0.25
needs_thread_rate: 0.083333
```

These numbers are comparison context only. They do not prove platform-wide coverage.

## Study Design

Use paired or comparable slices:

| Slice | Condition | Purpose |
|---|---|---|
| A | manual baseline | Measure review time and final human decisions without assist outputs |
| B | assisted review | Measure whether summaries, signal hints, prefill, warnings, and priority explanations reduce burden |

If exact pairing is unavailable, the result note must mark the comparison as `exploratory_comparable_slice`, not as a controlled paired test.

## Assisted Output Package

For each assisted-review candidate, prepare repo-safe draft outputs:

- one-sentence candidate summary;
- signal-family suggestions;
- schema-prefill draft;
- hard-negative warning;
- priority explanation;
- missing-evidence note;
- second-review suggestion.

Every output must include:

- `human_decision_required: true`;
- uncertainty note;
- repo-safe evidence-reference category;
- no raw evidence.

## Measurement Fields

Use:

- `templates/reviewer_assist_labor_savings_worksheet.md`;
- `templates/schema_prefill_correction_log_template.csv`;
- `templates/summary_usefulness_rubric.md`;
- `templates/signal_family_extraction_qa_table.csv`;
- `templates/hard_negative_hesitation_log_template.csv`;
- `templates/priority_ranking_evaluation_table.csv`;
- `templates/labor_savings_aggregate_report_template.md`;
- `templates/reviewer_assist_governance_checklist.md`.

## Success Conditions

The evaluation supports expansion only if:

- average or median review time drops;
- p95 review time does not worsen materially;
- schema-prefill acceptance is high enough to reduce work;
- correction burden is not higher than manual filling burden;
- summaries are useful without hiding decisive context;
- priority ranking does not over-prioritize hard negatives;
- second-review and disagreement rates stay controlled;
- raw-evidence leakage remains zero.

## Failure Conditions

Pause or revise if:

- assisted review saves no meaningful time;
- summaries or prefilled fields cause hidden correction work;
- hard-negative false-positive pressure increases;
- reviewers disagree more often;
- the method overfits known case fragments;
- the evaluation requires raw evidence in git;
- assist outputs imply final scam, legal, enforcement, or public-warning decisions.

## Expected Output

Decision `0146` creates the execution workbench under:

```text
experiments/evaluation-notes/0107-reviewer-assist-labor-savings-evaluation-result.md
```

The assisted-review fields are now filled in
`data/reviewer_assist_eval/batch_0010_assisted_review_result.yaml`, and Decision
`0147` records the aggregate-only result.

The final result chooses:

- `expand_assist_evaluation`.

Other possible decisions remain:

- `revise_assist_design`;
- `keep_shadow_only`;
- `pause_assist_layer`;
- `request_new_governed_source_slice`.
