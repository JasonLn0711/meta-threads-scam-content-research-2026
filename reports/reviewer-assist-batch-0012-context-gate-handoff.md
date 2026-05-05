# Reviewer Assist Batch 0012 Context-Gate Handoff

Date: 2026-05-05

Status: ready for human context-gate review; not an empirical result yet

## Purpose

Batch `0012` is the next governed step after the Batch `0011` empirical
Reviewer Assist result.

The goal is to test whether a revised context gate helps reviewers reach the
correct next action faster when `result_display_thread_required` metadata is
not enough for a confident label.

This handoff does not claim a completed review result. It prepares the
reviewer-facing packet, hides prior Batch `0011` outcomes, and leaves all human
review fields blank.

## First-Principle Fit

The repo's single highest priority is:

```text
Design a governed automatic or assisted method for discovering review-worthy
Threads investment-scam candidates with manageable reviewer burden.
```

Batch `0012` supports that priority because the main bottleneck is no longer
only "find suspicious-looking metadata." The bottleneck is whether the system
can identify when metadata is insufficient, ask for the smallest necessary
context, protect hard negatives, and avoid wasting reviewer time.

## Reviewer-Facing Packet

Use this packet for the assisted condition:

```text
data/reviewer_assist_eval/batch_0012_reviewer_context_gate_packet.yaml
```

It was generated from:

```text
data/reviewer_assist_eval/batch_0012_reviewer_fill_sheet_template.yaml
```

using:

```bash
.venv/bin/python scripts/build_reviewer_assist_context_gate_packet.py
```

The packet includes:

- reviewer-visible metadata aliases;
- revised context-gate assist outputs;
- blank human reviewer fields;
- packet quality checks.

The packet does not include:

- prior Batch `0011` assisted labels;
- prior Batch `0011` review timings;
- prior second-review or insufficient-evidence decisions;
- raw Threads text, reply text, OCR text, URLs, handles, screenshots,
  browser/session artifacts, controlled-store locators, private data, or
  stakeholder case IDs.

## Reviewer Rules

Reviewer rules remain here:

```text
data/reviewer_assist_eval/batch_0012_reviewer_rules.md
```

The key rule is that `metadata_only_label_or_not_reviewable` is secondary to
the next-action gate.

If metadata is insufficient, reviewers should not force `scam` or `non_scam`.
They should use `needs_thread_before_label`, `needs_second_review_before_label`,
or `not_reviewable_metadata_only` as appropriate.

## Slice Design

| Role | Count | Purpose |
|---|---:|---|
| `target_thread_required` | 4 | Test early routing to thread-before-label rather than metadata-only overreach |
| `boundary_control` | 4 | Check whether the gate avoids over-requesting thread context for low-context transition cases |
| `hard_negative_control` | 2 | Check whether clean result-display holdouts stay protected |
| `fast_lane_control` | 2 | Check whether strong-source priority cases are not slowed by the context gate |

## Fields Human Reviewers Must Fill

For each of the 12 entries, fill:

- `context_gate_review_time_seconds`;
- `human_context_gate_decision`;
- `metadata_only_label_or_not_reviewable`;
- `context_gate_usefulness_rating`;
- `context_gate_omission_risk`;
- `context_gate_status`;
- `minimal_context_request_status`;
- `over_request_risk`;
- `under_request_risk`;
- `second_review_required`;
- `insufficient_evidence`;
- `raw_evidence_excluded_from_git`.

Do not fill these fields by copying Batch `0011`.

## Completion Target

After human fill, write the completed result to:

```text
data/reviewer_assist_eval/batch_0012_context_gate_result.yaml
```

Then update:

```text
experiments/evaluation-notes/0109-reviewer-assist-thread-required-lane-revision-result.md
```

The result should report, at minimum:

- target-lane average, median, and p95 context-gate review time;
- correct thread-before-label routing rate;
- metadata-only overreach count;
- boundary-control over-request count;
- hard-negative over-request count;
- fast-lane slowdown count;
- second-review rate;
- insufficient-evidence rate;
- raw-evidence leakage incidents.

## Stop Conditions

Stop instead of synthesizing a favorable result if:

- any raw Threads text, reply text, OCR text, URL, handle, screenshot,
  browser/session artifact, credential, stakeholder case ID, or controlled-store
  locator would enter tracked git files;
- the packet or result exposes prior Batch `0011` labels or timings to the
  reviewer;
- the context gate becomes a final scam, legal fraud, enforcement, or
  public-warning decision;
- target thread-required cases receive confident metadata-only labels despite
  unresolved context;
- clean holdout controls are broadly over-routed into thread review without a
  specific missing-evidence reason;
- the result is framed as representative of all Threads investment scams.

## Current Next Action

The next human action is:

```text
Fill the 12 reviewer_fields entries in the Batch 0012 context-gate packet,
record review time per entry, and keep raw evidence out of git.
```

The next agent action after the human fill is:

```text
Validate the completed result, compute aggregate context-gate metrics, and
record whether the revision should be adopted, revised again, capped, paused,
or moved to a separately governed thread-context capture design.
```
