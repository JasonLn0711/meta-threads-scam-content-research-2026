# Batch 0011 Reviewer Rules

Use this file as the reviewer-facing rule sheet for the Decision `0148`
Reviewer Assist expansion slice.

This file is safe to show reviewers. Do not show reviewers
`data/reviewer_assist_eval/batch_0011_work_order.yaml` directly because that
controller-side file contains manual-baseline labels, confidence, review times,
and second-review decisions.

## Review Goal

Evaluate whether Reviewer Assist helps reviewers process metadata-only
candidate slices faster while preserving:

- human final judgment;
- uncertainty;
- hard-negative protection;
- second-review override;
- raw-evidence exclusion;
- aggregate-only reporting.

This is not a production detector test and not a legal fraud determination.

## What Reviewers May See

Reviewers may see only metadata-safe fields:

- `workbench_id`;
- `source_candidate_id`;
- `source_stub_id`;
- `task_id`;
- `routing_lane`;
- `signal_hint`;
- `expected_behavior`;
- Reviewer Assist outputs prepared from structured metadata only:
  - candidate summary;
  - signal-family suggestions;
  - schema-prefill draft;
  - hard-negative warning;
  - priority explanation;
  - missing-evidence note;
  - second-review suggestion.

## What Reviewers Must Not See

Do not show reviewers:

- manual-baseline final label;
- manual-baseline confidence;
- manual-baseline review time;
- manual-baseline second-review decision;
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
| `assisted_review_time_seconds` | numeric seconds |
| `assisted_human_final_label_or_not_reviewable` | `scam` / `non_scam` / `uncertain` / `not_reviewable` |
| `summary_usefulness_rating` | 1 / 2 / 3 / 4 / 5 |
| `summary_omission_risk` | `low` / `medium` / `high` |
| `schema_prefill_status` | `accepted` / `accepted_with_minor_correction` / `needs_major_correction` / `unusable` |
| `schema_prefill_correction_category` | short metadata-safe category, or `none` |
| `signal_suggestion_status` | `accepted` / `accepted_with_minor_correction` / `rejected` |
| `signal_correction_category` | short metadata-safe category, or `none` |
| `hard_negative_warning_status` | `accepted` / `not_applicable` / `over_warned` / `missed_warning` |
| `priority_explanation_status` | `accepted` / `accepted_with_minor_correction` / `rejected` |
| `second_review_required` | `true` / `false` |
| `insufficient_evidence` | `true` / `false` |
| `raw_evidence_excluded_from_git` | must be `true` |

## Label Rules

Use labels only as review outcomes for this metadata-only slice:

- `scam`: metadata is sufficient for the reviewer to mark the candidate as
  review-worthy scam-like content under the project taxonomy.
- `non_scam`: metadata supports a hard-negative or ordinary-content outcome.
- `uncertain`: metadata is insufficient or ambiguous but still reviewable.
- `not_reviewable`: the candidate cannot be reviewed under the allowed
  metadata-only boundary.

Do not make legal fraud determinations, enforcement recommendations, public
warnings, or production detector claims.

## Second-Review Rules

Set `second_review_required: true` when:

- the summary may hide decisive context;
- `summary_omission_risk` is `medium` or `high`;
- `needs_thread` or thread dependency affects the decision;
- a hard-negative warning is missed, over-warned, or contested;
- schema prefill needs major correction or is unusable;
- signal suggestions are rejected;
- the final label is `uncertain`;
- the reviewer hesitates for any governance, privacy, or evidence-sufficiency
  reason.

## Hard-Negative Rules

Do not treat `成果展示` or result-display metadata as a positive scam signal by
itself.

Use hard-negative warning review to protect:

- clean result-display holdouts;
- ordinary investment discussion;
- anti-scam or warning content;
- educational/risk-disclosure content;
- low-context transition fragments without sufficient evidence.

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
data/reviewer_assist_eval/batch_0011_assisted_review_result.yaml
```

After all 16 candidates are filled, update:

```text
experiments/evaluation-notes/0108-reviewer-assist-expansion-batch-0008-result.md
data/reviewer_assist_eval/batch_0011_aggregate_result.yaml
```
