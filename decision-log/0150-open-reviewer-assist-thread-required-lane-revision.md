# 0150 - Open Reviewer Assist Thread-Required Lane Revision

Date: 2026-05-05

## Decision

Open Batch `0012` as a bounded metadata-only Reviewer Assist revision slice
focused on the `result_display_thread_required` lane.

This decision does not authorize new Threads/Meta collection, live browser/API
automation, real LLM/API calls, model training, production detection, legal
fraud determination, enforcement action, public warning, or final automated
scam decisions.

## Context

Decision `0149` recorded Batch `0011` as an empirical metadata-only
assisted-review result and selected bounded `expand_assist_evaluation`.

Batch `0011` showed that Reviewer Assist can reduce review time across a
balanced metadata-only slice. It also showed a specific bottleneck:

```text
result_display_thread_required:
  count: 4
  assisted_average_review_time_seconds: 51.75
  uncertain_count: 4
  second_review_required_count: 4
  insufficient_evidence_count: 4
```

The problem is not that the reviewer needs a stronger label suggestion. The
problem is that metadata-only assistance should detect thread dependency
earlier and route the item to the correct next action before the reviewer spends
time trying to resolve an under-contextualized label.

## Batch 0012 Purpose

Batch `0012` tests a revised context gate for Reviewer Assist.

The revised assist output must make the evidence bottleneck explicit:

- whether metadata is sufficient for a label;
- whether thread or reply context is required before any confident label;
- which missing context is minimally needed;
- whether the correct next action is metadata label, thread-context request,
  second review, hard-negative check, or metadata-only not-reviewable;
- whether the assistant is over-requesting thread context for control lanes.

## Evaluation Slice

The slice uses existing metadata-only aliases from the Batch `0008` / Batch
`0011` evaluation path:

- 4 `result_display_thread_required` target cases;
- 4 `result_display_low_context_transition` boundary controls;
- 2 `result_display_clean_holdout` hard-negative controls;
- 2 `strong_source_priority` fast-lane regression controls.

No raw evidence, URLs, handles, screenshots, browser artifacts, controlled-store
locators, or private data are added to git.

## Success Criteria

Batch `0012` supports the revision only if:

- thread-required target cases are routed to `needs_thread_before_label` or an
  equivalent context-first action without confident metadata-only overreach;
- control cases are not broadly over-routed into thread-required review;
- reviewer time-to-correct-next-action improves against the Batch `0011`
  thread-required average of `51.75` seconds;
- hard-negative controls remain protected;
- fast-lane controls are not slowed by the new gate;
- raw-evidence leakage remains `0`;
- human reviewers retain final judgment and can override every assist output.

## Artifacts

Create and use:

- `experiments/batch_variants/0012-reviewer-assist-thread-required-lane-revision.md`
- `data/reviewer_assist_eval/batch_0012_work_order.yaml`
- `data/reviewer_assist_eval/batch_0012_reviewer_rules.md`
- `data/reviewer_assist_eval/batch_0012_reviewer_fill_sheet_template.yaml`
- `experiments/evaluation-notes/0109-reviewer-assist-thread-required-lane-revision-result.md`

## Boundary

This revision remains inside the repo's single highest priority: designing a
governed automatic or assisted method for discovering review-worthy Threads
investment-scam candidates with manageable reviewer burden.

It is not a broader source-arm expansion and not a claim that current cases are
representative of all Threads investment scams.
