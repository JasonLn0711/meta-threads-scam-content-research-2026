# Decision 0030: Require Stakeholder Evidence-Scope Review

## Date

2026-04-25

## Decision

Require a stakeholder evidence-scope review before any future item 0017 retry, item 0018 attempt, or high-risk case-finding collection run.

Until that review is completed and recorded, collection remains paused after the 16 accepted local records and the excluded item 0017 method-review trace.

## Context

Decision 0029 stopped the item 0017 extension after run 0013 produced no reviewable candidate under the approved scoped evidence-path boundaries.

The current issue is not access readiness, schema validation, or redaction tooling. The current issue is that the approved field set does not produce enough independent item-level evidence for higher-risk discovery from the current source path.

The project has prepared a repo-safe stakeholder memo at `docs/51-stakeholder-evidence-expansion-memo.md`. That memo identifies possible evidence families, but it does not authorize collection.

## Options Considered

| Option | Decision |
|---|---|
| Open item 0018 under the same method | Rejected; item 0017 has no accepted research item and the method blocker remains. |
| Treat the stakeholder memo as approval | Rejected; a memo is a request, not a decision. |
| Continue with text-first browser-session evidence only | Rejected for high-risk discovery; low expected yield and high false-positive pressure. |
| Create a formal stakeholder evidence-scope review gate | Accepted. |
| Prepare a collection run before the review is completed | Rejected; the run scope would be underspecified. |

## Rationale

The project now needs a scope decision, not another acquisition attempt. The next approved evidence family could materially change privacy risk, reviewer burden, platform constraints, storage requirements, and redaction procedures.

Recording a review gate keeps the project documentation-first and prevents accidental scope expansion through operational momentum.

## Consequences

- Item 0018 remains blocked.
- No future item 0017 retry is allowed until the evidence-scope review is completed.
- The pilot authorization register must show the evidence-expansion request as `pending`.
- Any future run record must cite the completed evidence-scope review gate.
- If stakeholders reject evidence expansion, the project should move to method reporting from the 16 accepted records rather than continuing collection.

## Follow-Up

Complete `governance/pilot-launch/threads_pilot_v1_2026-05_evidence_scope_review_gate_0014.md` with a stakeholder outcome:

- `approve_narrow_expansion`
- `approve_redacted_stakeholder_examples_only`
- `hold_at_16_and_report`
- `reject_expansion`

Only `approve_narrow_expansion` or another explicitly scoped approval can unlock a new collection run.
