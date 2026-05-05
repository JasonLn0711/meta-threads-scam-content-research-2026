# Batch 0012 Reviewer Rules

Use this file as the reviewer-facing rule sheet for the Decision `0150`
Reviewer Assist thread-required lane revision.

This file is safe to show reviewers. Do not show reviewers
`data/reviewer_assist_eval/batch_0012_work_order.yaml` directly because that
controller-side file contains prior assisted outcomes and timings from Batch
`0011`.

## Review Goal

Evaluate whether a revised Reviewer Assist context gate helps reviewers decide
the correct next action faster when metadata may be insufficient.

The goal is not to force a scam/non-scam label from metadata. The goal is to
avoid wasting reviewer time on under-contextualized candidates and to route
thread-dependent items to the right next step.

This is not a production detector test and not a legal fraud determination.

## What Reviewers May See

Reviewers may see only metadata-safe fields:

- `workbench_id`;
- `source_candidate_id`;
- `source_stub_id`;
- `task_id`;
- `routing_lane`;
- `slice_role`;
- `signal_hint`;
- `expected_behavior`;
- revised Reviewer Assist outputs prepared from structured metadata only:
  - context dependency gate;
  - context reason codes;
  - minimal context needed;
  - safe next action;
  - metadata label guardrail;
  - priority explanation;
  - missing-evidence note;
  - second-review suggestion.

## What Reviewers Must Not See

Do not show reviewers:

- prior assisted final label;
- prior assisted review time;
- prior second-review decision;
- prior insufficient-evidence decision;
- raw Threads post text;
- raw reply text;
- raw OCR text;
- URLs or handles;
- screenshots;
- browser/session artifacts;
- credentials, cookies, tokens, or secrets;
- controlled-store locators;
- stakeholder case IDs;
- private personal data.

## Required Fields To Fill

For every candidate, reviewers must fill:

| Field | Allowed values |
|---|---|
| `context_gate_review_time_seconds` | numeric seconds |
| `human_context_gate_decision` | `metadata_sufficient_for_label` / `needs_thread_before_label` / `needs_second_review_before_label` / `hard_negative_metadata_sufficient` / `not_reviewable_metadata_only` |
| `metadata_only_label_or_not_reviewable` | `scam` / `non_scam` / `uncertain` / `not_reviewable` / `not_applicable` |
| `context_gate_usefulness_rating` | 1 / 2 / 3 / 4 / 5 |
| `context_gate_omission_risk` | `low` / `medium` / `high` |
| `context_gate_status` | `accepted` / `accepted_with_minor_correction` / `needs_major_correction` / `unusable` |
| `minimal_context_request_status` | `accepted` / `accepted_with_minor_correction` / `over_requested` / `under_requested` / `not_applicable` |
| `over_request_risk` | `low` / `medium` / `high` |
| `under_request_risk` | `low` / `medium` / `high` |
| `second_review_required` | `true` / `false` |
| `insufficient_evidence` | `true` / `false` |
| `raw_evidence_excluded_from_git` | must be `true` |

## Context-Gate Decision Rules

Use `needs_thread_before_label` when metadata suggests the candidate cannot be
resolved without thread, reply, or surrounding context.

Use `metadata_sufficient_for_label` only when the metadata is enough to support
a human label under the current taxonomy and no missing thread context is needed.

Use `hard_negative_metadata_sufficient` when the metadata is enough to preserve
a hard-negative or clean holdout decision without full-thread review.

Use `needs_second_review_before_label` when metadata is reviewable but the
summary, signal, hard-negative, or context gate is contested.

Use `not_reviewable_metadata_only` when the allowed metadata is too weak for a
meaningful review and adding raw evidence to git would be required.

## Label Rules

For Batch `0012`, the label field is secondary to the next-action gate.

If the context gate decision is `needs_thread_before_label`, use:

```text
metadata_only_label_or_not_reviewable: uncertain
```

unless the reviewer believes the item is not reviewable under the metadata-only
boundary, in which case use `not_reviewable`.

Do not upgrade a thread-required item to confident `scam` or `non_scam` only
because the metadata contains investment vocabulary, result display, reply
funnel, or group-transition hints.

## Second-Review Rules

Set `second_review_required: true` when:

- the context gate is contested;
- the metadata-only label is `uncertain`;
- the item is routed to `needs_thread_before_label`;
- `context_gate_omission_risk` is `medium` or `high`;
- the minimal context request is under-requested or over-requested;
- a hard-negative control may be over-routed into thread review;
- a fast-lane control may be slowed or downgraded by the context gate;
- the reviewer hesitates for any governance, privacy, or evidence-sufficiency
  reason.

## Hard-Negative And Over-Request Rules

Do not treat `成果展示` or result-display metadata as a positive scam signal by
itself.

Do not request thread context by habit for clean result-display holdouts if the
metadata is enough to preserve a hard-negative decision.

Set `over_request_risk` to `medium` or `high` if the revised gate sends too many
control cases to thread review without a clear missing-evidence reason.

Set `under_request_risk` to `medium` or `high` if the revised gate leaves a
thread-dependent item in metadata-only labeling despite unresolved context.

## Raw-Evidence Stop Rule

Stop the review if completing a field would require adding any forbidden raw
evidence to git.

Set `raw_evidence_excluded_from_git: true` only if no raw Threads text, reply
text, OCR text, URL, handle, screenshot, browser artifact, credential,
controlled-store locator, stakeholder case ID, or private personal data was
added to tracked repo files.

## Output Location

Completed reviewer fills should be written to a separate assisted-review result
file, not into the controller work order directly:

```text
data/reviewer_assist_eval/batch_0012_context_gate_result.yaml
```

After all 12 candidates are filled, update:

```text
experiments/evaluation-notes/0109-reviewer-assist-thread-required-lane-revision-result.md
```
