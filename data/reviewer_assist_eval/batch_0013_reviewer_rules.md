# Batch 0013 Reviewer Rules

Use this file as the reviewer-facing rule sheet for Decision `0154`.

Batch `0013` is a bounded reuse check for the reconciled Batch `0012` context
gate. It uses existing Batch `0009` metadata-safe aliases only. It is not a new
collection run and not an empirical result until reviewers fill the packet.

## Review Goal

Evaluate whether the reconciled context gate helps reviewers decide the correct
next action faster on a small policy-weighted metadata slice.

The goal is not to force a scam/non-scam label from metadata. The goal is to
preserve uncertainty, route thread-dependent items to the smallest necessary
context step, protect clean holdouts, and avoid slowing strong fast-lane cases.

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

- prior baseline label;
- prior baseline review time;
- prior second-review decision;
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

## Control-Specific Rules

For `target_thread_required`, do not force a confident metadata-only label if
thread or reply context is missing.

For `boundary_control`, do not request thread context by habit. If metadata is
weak but reviewable, route to second review before label.

For `hard_negative_control`, preserve clean holdouts when result-display
metadata appears alone without guarantee, contact, group, reply, pressure, or
thread-dependency signals.

For `fast_lane_control`, do not slow a strong-source priority case only because
the context gate exists. Reviewers may override only if the metadata is
specifically contested.

## Raw-Evidence Stop Rule

Stop the review if completing a field would require adding any forbidden raw
evidence to git.

Set `raw_evidence_excluded_from_git: true` only if no raw Threads text, reply
text, OCR text, URL, handle, screenshot, browser artifact, credential,
controlled-store locator, stakeholder case ID, or private personal data was
added to tracked repo files.

## Output Location

Completed reviewer fills should be written to a separate result file:

```text
data/reviewer_assist_eval/batch_0013_context_gate_result.yaml
```

After all 8 candidates are filled, update:

```text
experiments/evaluation-notes/0110-reviewer-assist-context-gate-bounded-reuse-result.md
```
