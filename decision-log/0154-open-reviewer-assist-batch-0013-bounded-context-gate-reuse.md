# 0154 - Open Reviewer Assist Batch 0013 Bounded Context-Gate Reuse

Date: 2026-05-05

## Decision

Open Batch `0013` as a bounded, metadata-only Reviewer Assist context-gate
reuse slice after the Batch `0012` packet/source reconciliation.

This is a packet-preparation and human-fill work order. It is not an empirical
result yet.

## Context

Decision `0152` adopted the Batch `0012` thread-required context gate.
Decision `0153` reconciled the packet/source alignment so the generator and
validator now report `0` packet-alignment warnings.

The next useful step is not broad collection or another source arm. It is a
small reuse check with a concrete reviewer-hour hypothesis:

```text
If the reconciled context gate is reusable, it should route a policy-weighted
metadata slice to the correct next action faster than baseline review, while
preserving hard negatives and not slowing fast-lane candidates.
```

## Slice

Use existing Batch `0009` repo-safe metadata aliases only:

| Role | Count | Purpose |
|---|---:|---|
| `target_thread_required` | 1 | Check early route to `needs_thread_before_label` |
| `boundary_control` | 1 | Check low-context transition boundary handling |
| `hard_negative_control` | 2 | Check clean result-display holdout protection |
| `fast_lane_control` | 4 | Check strong-source priority cases are not slowed |

This slice is deliberately small. It is a bounded reuse smoke/regression check,
not platform coverage and not a new discovery claim.

## Artifacts

- `experiments/batch_variants/0013-reviewer-assist-context-gate-bounded-reuse.md`
- `data/reviewer_assist_eval/batch_0013_work_order.yaml`
- `data/reviewer_assist_eval/batch_0013_reviewer_rules.md`
- `data/reviewer_assist_eval/batch_0013_reviewer_fill_sheet_template.yaml`
- `data/reviewer_assist_eval/batch_0013_reviewer_context_gate_packet.yaml`
- `reports/reviewer-assist-batch-0013-context-gate-bounded-reuse-handoff.md`
- `experiments/evaluation-notes/0110-reviewer-assist-context-gate-bounded-reuse-result.md`

## Success Conditions

The future human-filled result should measure:

- context-gate review time;
- accepted/corrected/rejected context-gate status;
- target `needs_thread_before_label` routing;
- boundary-control over-request / under-request risk;
- hard-negative over-request count;
- fast-lane slowdown count;
- second-review rate;
- insufficient-evidence rate;
- raw-evidence leakage incidents.

The packet-preparation success condition for this decision is narrower:

```text
Build a reviewer-facing packet with blank reviewer fields, no raw evidence,
no prior labels/times exposed, and 0 packet-quality errors.
```

## Boundaries

This decision does not authorize:

- new Threads/Meta collection;
- browser/API automation;
- raw Threads text, reply text, OCR text, URLs, handles, screenshots, browser
  artifacts, or controlled-store locators in git;
- real LLM/API calls;
- model training;
- production detection;
- final automated scam labels;
- legal fraud determinations;
- enforcement actions;
- public warnings.

Human reviewers remain responsible for all labels and next-action decisions.
