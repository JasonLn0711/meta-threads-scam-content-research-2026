# Reviewer Assist Batch 0013 Context-Gate Bounded Reuse Handoff

Date: 2026-05-05

Status: reviewer-facing packet ready; human review fields blank

## Purpose

Batch `0013` is the first bounded reuse check after the Batch `0012`
context-gate result was adopted and packet/source alignment was reconciled.

The goal is to test whether the context gate can be reused on a small
policy-weighted metadata slice without adding raw evidence, widening scope, or
slowing the lanes it is supposed to protect.

## First-Principle Fit

The repo's single highest priority is:

```text
Design a governed automatic or assisted method for discovering review-worthy
Threads investment-scam candidates with manageable reviewer burden.
```

Batch `0013` supports that priority only as a Reviewer Assist labor-efficiency
check. It does not discover new candidates, claim platform coverage, or produce
final automated labels.

## Reviewer-Facing Packet

Use this packet for the human-fill condition:

```text
data/reviewer_assist_eval/batch_0013_reviewer_context_gate_packet.yaml
```

It was generated from:

```text
data/reviewer_assist_eval/batch_0013_reviewer_fill_sheet_template.yaml
```

using:

```bash
.venv/bin/python scripts/build_reviewer_assist_context_gate_packet.py \
  --template data/reviewer_assist_eval/batch_0013_reviewer_fill_sheet_template.yaml \
  --output data/reviewer_assist_eval/batch_0013_reviewer_context_gate_packet.yaml
```

The packet includes:

- reviewer-visible metadata aliases;
- revised context-gate assist outputs;
- blank human reviewer fields;
- packet quality checks.

The packet does not include:

- prior baseline labels;
- prior baseline review timings;
- prior second-review decisions;
- raw Threads text, reply text, OCR text, URLs, handles, screenshots,
  browser/session artifacts, controlled-store locators, private data, or
  stakeholder case IDs.

## Reviewer Rules

Reviewer rules are here:

```text
data/reviewer_assist_eval/batch_0013_reviewer_rules.md
```

The key rule is that the next-action gate comes before the label. If metadata
is insufficient, reviewers should not force `scam` or `non_scam`.

## Slice Design

| Role | Count | Purpose |
|---|---:|---|
| `target_thread_required` | 1 | Check early routing to thread-before-label |
| `boundary_control` | 1 | Check low-context transition boundary handling |
| `hard_negative_control` | 2 | Preserve clean result-display hard negatives |
| `fast_lane_control` | 4 | Ensure strong-source priority cases are not slowed |

## Fields Human Reviewers Must Fill

For each of the 8 entries, fill:

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

Do not fill these fields by copying Batch `0009` baseline outcomes.

## Completion Target

After human fill, write the completed result to:

```text
data/reviewer_assist_eval/batch_0013_context_gate_result.yaml
```

Then update:

```text
experiments/evaluation-notes/0110-reviewer-assist-context-gate-bounded-reuse-result.md
```

The result should report, at minimum:

- average/median/p95 context-gate review time;
- target thread-before-label routing;
- boundary-control over-request / under-request risk;
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
- the packet or result exposes prior Batch `0009` labels or timings to the
  reviewer;
- the context gate becomes a final scam, legal fraud, enforcement, or
  public-warning decision;
- the result is framed as representative of all Threads investment scams;
- the slice is expanded into broad collection or source-arm execution.

## Current Next Action

```text
Fill the 8 reviewer_fields entries in the Batch 0013 context-gate packet,
record review time per entry, and keep raw evidence out of git.
```
