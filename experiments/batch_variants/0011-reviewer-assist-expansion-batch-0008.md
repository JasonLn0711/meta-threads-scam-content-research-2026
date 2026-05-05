# 0011 - Reviewer Assist Expansion On Batch 0008

Status: empirical metadata-only assisted-review result completed under Decision
`0149`.

## Purpose

Run the next metadata-only Reviewer Assist labor-savings evaluation slice after
Decision `0147`.

This expansion uses Batch `0008` as the manual baseline because it contains a
balanced context-gating mix rather than the Batch `0009` policy-weighted mix.

## First-Principle Question

```text
Does Reviewer Assist reduce review burden across fast, boundary, slow-context,
and hard-negative calibration lanes without weakening human final judgment,
hard-negative protection, or uncertainty handling?
```

## Baseline

Use Batch `0008`:

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

## Lane Mix

| Lane | Count | Purpose |
|---|---:|---|
| `strong_source_priority` | 4 | Test fast-lane assist value |
| `result_display_low_context_transition` | 4 | Test boundary triage assist value |
| `result_display_thread_required` | 4 | Test slow-context burden and missing-evidence handling |
| `result_display_clean_holdout` | 4 | Test hard-negative warning and over-generalization protection |

## Work Order

Fill:

```text
data/reviewer_assist_eval/batch_0011_work_order.yaml
```

The reviewer-facing packet must hide manual-baseline labels, confidence, review
times, and second-review decisions.

## Result Files

The completed result is recorded in:

```text
experiments/evaluation-notes/0108-reviewer-assist-expansion-batch-0008-result.md
data/reviewer_assist_eval/batch_0011_assisted_review_result.yaml
data/reviewer_assist_eval/batch_0011_aggregate_result.yaml
```

Summary: assisted average review time decreased from `41.875` to `33.125`
seconds, candidates reviewed per hour increased from `85.970149` to
`108.679245`, final label mix stayed at 4 scam, 4 non-scam, and 8 uncertain,
and raw-evidence leakage stayed at `0`.

## Guardrails

- No new collection.
- No raw evidence in git.
- No real LLM/API calls unless a later decision authorizes them.
- No model training.
- No final automated scam decisions.
- No legal, enforcement, public-warning, or production-detector claims.
- Do not treat Batch `0008` as representative of all Threads investment scams.
