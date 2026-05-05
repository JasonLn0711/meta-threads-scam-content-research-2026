# Decision 0147: Record Reviewer Assist Labor-Savings Evaluation Result

Date: 2026-05-05

Status: recorded aggregate-only shadow result

## Decision

Record the Decision `0146` Reviewer Assist execution workbench result and choose:

```text
expand_assist_evaluation
```

This decision means the Reviewer Assist evaluation should continue on another
bounded metadata-only or separately governed slice. It does not authorize broad
collection, live Threads access, model training, production detection, legal
fraud determinations, enforcement recommendations, public warnings, or raw
evidence in git.

## Result Basis

Inputs:

- `data/reviewer_assist_eval/batch_0010_work_order.yaml`
- `data/reviewer_assist_eval/batch_0010_assisted_review_result.yaml`
- `data/reviewer_assist_eval/batch_0010_aggregate_result.yaml`
- `experiments/evaluation-notes/0107-reviewer-assist-labor-savings-evaluation-result.md`
- `metrics/batch_logs/batch_0009_run_log.yaml`

The result compares Batch `0009` manual baseline metrics against the completed
metadata-only assisted-review fill.

## Aggregate Result

```text
reviewed_candidates: 12
manual_average_review_seconds: 37.333333
assisted_average_review_seconds: 28.750000
average_review_seconds_difference: -8.583333
average_review_time_drop_percent: 22.9911
manual_median_review_seconds: 35.500000
assisted_median_review_seconds: 25.500000
manual_p95_nearest_rank_seconds: 58.000000
assisted_p95_nearest_rank_seconds: 53.000000
manual_high_value_candidates_per_hour: 64.285714
assisted_high_value_candidates_per_hour: 83.478261
review_worthy_yield_manual: 0.666667
review_worthy_yield_assisted: 0.666667
second_review_rate_manual: 0.250000
second_review_rate_assisted: 0.250000
manual_assisted_final_label_mismatch_rate: 0.000000
raw_evidence_leakage_incidents: 0
```

## Assist Quality

```text
summary_usefulness_mean: 4.416667
summary_rating_4_to_5_rate: 0.916667
schema_prefill_accepted_or_minor_rate: 1.000000
schema_prefill_correction_rate: 0.250000
signal_suggestion_accepted_or_minor_rate: 1.000000
signal_suggestion_correction_rate: 0.166667
priority_explanation_accepted_or_minor_rate: 1.000000
priority_explanation_correction_rate: 0.083333
hard_negative_warning_acceptance_rate_among_applicable_entries: 1.000000
hard_negative_over_or_missed_warning_count: 0
```

## Interpretation

The result supports continuing Reviewer Assist evaluation because assisted
review reduced average, median, and nearest-rank p95 review time while preserving
manual-baseline final labels, second-review rate, hard-negative warning quality,
and raw-evidence exclusion.

## Limitations

This result must not be generalized as a complete Threads investment-scam
finding. Batch `0009` is a policy-weighted metadata-only slice, not a
representative sample of all Threads investment scams.

The result should be read as evidence that the Reviewer Assist workflow is worth
testing on another bounded slice, not as evidence that the project has solved
automatic discovery.

## Next Review Point

Open a next bounded Reviewer Assist evaluation slice that preserves:

- metadata-only tracked artifacts;
- no new collection without a separate governed decision;
- hidden manual-baseline labels in reviewer-facing materials;
- human final judgment;
- hard-negative calibration;
- second-review override;
- aggregate-only reporting.
