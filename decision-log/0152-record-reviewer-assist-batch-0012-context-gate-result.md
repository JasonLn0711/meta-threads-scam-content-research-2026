# 0152 - Record Reviewer Assist Batch 0012 Context-Gate Result

Date: 2026-05-05

## Decision

Record Batch `0012` as an empirical metadata-only context-gate result and
select `adopt_context_gate_revision` for the thread-required lane.

This decision does not authorize new Threads/Meta collection, live browser/API
automation, real LLM/API calls, model training, production detection, legal
fraud determination, enforcement action, public warning, or final automated
scam decisions.

## Context

Decision `0150` opened Batch `0012` as a thread-required context-gate revision.
Decision `0151` prepared the reviewer-facing context-gate packet and explicitly
left reviewer fields blank.

The completed Batch `0012` result is stored as:

- `data/reviewer_assist_eval/batch_0012_context_gate_result.yaml`
- `data/reviewer_assist_eval/batch_0012_aggregate_result.yaml`
- `experiments/evaluation-notes/0109-reviewer-assist-thread-required-lane-revision-result.md`

## Result Summary

| Metric | Batch 0011 baseline | Batch 0012 revised gate | Difference |
|---|---:|---:|---:|
| Target lane reviewed candidates | 4 | 4 | 0 |
| Target lane average seconds | 51.75 | 29.5 | -22.25 |
| Correct thread-before-label routing rate | pending | 1.0 | n/a |
| Metadata-only overreach count | pending | 0 | n/a |
| Boundary-control over-request count | pending | 0 | n/a |
| Hard-negative over-request count | pending | 0 | n/a |
| Fast-lane slowdown count | pending | 0 | n/a |
| Raw-evidence leakage incidents | 0 required | 0 | 0 |

Across all 12 entries, total context-gate review time was `300.0` seconds,
average time was `25.0` seconds, median time was `27.5` seconds, and p95 time
was `30.45` seconds.

## Rationale

The result supports adopting the context-gate revision because:

- all 4 thread-required target cases were routed to
  `needs_thread_before_label`;
- target-lane average time fell from `51.75` seconds in Batch `0011` to `29.5`
  seconds in Batch `0012`;
- no target case was pushed into a confident metadata-only scam or non-scam
  label;
- boundary controls were routed to second review instead of thread review by
  habit;
- both clean holdout hard negatives were preserved;
- both fast-lane controls remained metadata sufficient and were not slowed;
- raw-evidence leakage remained `0`.

## QA Note

Validation found `0` aggregate or required-field errors and `12`
source-packet alignment warnings.

The warnings are traceability warnings, not aggregate calculation failures. They
come from expected-behavior alias differences and from the completed result
using fast-lane controls `STUB_0008_A_01` / `STUB_0008_A_02`, while the
generated source packet used `STUB_0008_A_03` / `STUB_0008_A_04`.

The result is therefore accepted as an empirical context-gate result, but future
reuse of the packet generator must reconcile the fast-lane control selection
before reviewer delivery.

## Consequences

Adopt the context-gate revision for future thread-required Reviewer Assist
evaluation, with two constraints:

- use the gate to route thread-required candidates to context-before-label
  review, not to make final scam decisions;
- reconcile packet/source alias alignment before generating another
  reviewer-facing packet.

The next bounded step may be a governed result synthesis or a new bounded slice
that uses the adopted context gate. It must not become broad collection,
platform-wide detection, legal fraud determination, or production enforcement.

## Boundaries

This decision remains inside the repo's single highest priority: designing a
governed automatic or assisted method for discovering review-worthy Threads
investment-scam candidates with manageable reviewer burden.

It does not change the hard boundary against raw evidence in git, uncontrolled
collection, production detection, legal fraud claims, enforcement claims, or
automated final judgments.
