# 0149 - Record Reviewer Assist Expansion Batch 0011 Result

Date: 2026-05-05

## Decision

Record Batch `0011` as an empirical metadata-only assisted-review result and
select `expand_assist_evaluation` as the next bounded Reviewer Assist direction.

This decision does not authorize new collection, live Threads/Meta automation,
real LLM/API calls, model training, production detection, public warning,
enforcement action, or final automated scam decisions.

## Context

Decision `0148` opened a bounded expansion slice using Batch `0008` as the
balanced context-gating manual baseline. The reviewer-facing packet hid manual
baseline labels, confidence values, review times, and second-review decisions.

The completed Batch `0011` result is stored as:

- `data/reviewer_assist_eval/batch_0011_assisted_review_result.yaml`
- `data/reviewer_assist_eval/batch_0011_aggregate_result.yaml`
- `experiments/evaluation-notes/0108-reviewer-assist-expansion-batch-0008-result.md`

## Result Summary

| Metric | Manual baseline | Assisted review | Difference |
|---|---:|---:|---:|
| Reviewed candidates | 16 | 16 | 0 |
| Total review seconds | 670.0 | 530.0 | -140.0 |
| Average review seconds | 41.875 | 33.125 | -8.75 |
| Median review seconds | 38.5 | 29.5 | -9.0 |
| P95 review seconds | 60.0 | 54.0 | -6.0 |
| Candidates reviewed per hour | 85.970149 | 108.679245 | +22.709096 |
| High-value candidates per reviewer hour | 21.492537 | 27.169811 | +5.677274 |
| Yield rate | 0.25 | 0.25 | 0.0 |
| Uncertainty rate | 0.5 | 0.5 | 0.0 |
| Second-review rate | 0.375 | 0.5 | +0.125 |

The assisted condition reduced average review time by `20.895522%`, increased
candidates reviewed per hour by `26.415094%`, and increased high-value
candidates per reviewer hour by `26.415096%` while preserving the same final
label mix.

## Rationale

The result supports further Reviewer Assist evaluation because:

- review burden decreased across the balanced metadata-only slice;
- final label distribution remained stable: 4 scam, 4 non-scam, 8 uncertain;
- hard-negative calibration remained protected in the clean holdout lane;
- raw-evidence exclusion was confirmed for all entries;
- the result preserved uncertainty instead of forcing weak boundary cases into
  confident scam or non-scam labels.

The result also shows a limitation:

- the `result_display_thread_required` lane remains slow and uncertain because
  missing thread context is the bottleneck, not reviewer orientation alone.

## Consequences

Continue Reviewer Assist evaluation, but keep the expansion bounded and
metadata-safe.

The next design revision should:

- preserve `strong_source_priority` fast-lane support;
- preserve hard-negative warnings and clean holdout calibration;
- revise the `result_display_thread_required` lane so thread dependency is
  surfaced earlier and treated as an evidence bottleneck;
- keep measuring review time, p95 time, reviewer-hour yield, correction rates,
  insufficient-evidence rate, second-review rate, and hard-negative pressure;
- avoid treating Batch `0008`, Batch `0009`, Batch `0010`, Batch `0011`, or
  current case fragments as representative of all Threads investment scams.

## Boundaries

This decision remains inside the repo's single highest priority: designing a
governed automatic or assisted method for discovering review-worthy Threads
investment-scam candidates with manageable reviewer burden.

It does not change the hard boundary against raw evidence in git, uncontrolled
collection, production detection, legal fraud claims, enforcement claims, or
automated final judgments.
