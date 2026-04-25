# Decision 0031: Record Stakeholder Evidence-Expansion Approval

## Date

2026-04-25

## Decision

Record that stakeholders approved all proposed evidence families for the next governed Threads evidence-expansion step.

This approval unlocks a new run record, but it does not authorize unlimited collection, raw evidence in git, production detection, legal fraud determinations, public accusations, broad scraping, or uncontrolled profile/graph review.

## Context

Decision 0030 required a stakeholder evidence-scope review before any item 0017 retry, item 0018 attempt, or higher-risk case-finding collection run.

The stakeholder decision is now reported as approval for all proposed evidence families:

- redacted stakeholder exemplars;
- risk-relevant OCR excerpts;
- screenshot raw storage in the controlled store;
- narrow adjacent reply context;
- visible-link domain/category evidence;
- redirect or landing-page evidence;
- profile/account context review if needed for the scoped item-level question.

## Options Considered

| Option | Decision |
|---|---|
| Treat approval as unlimited collection | Rejected; this would violate the pilot's staged governance model. |
| Record approval but keep item 0018 blocked forever | Rejected; the gate has now been answered. |
| Record approval as `approved_with_limits` and require a bounded run record | Accepted. |

## Rationale

The project can now test whether richer evidence resolves the high-risk discovery blocker. However, the approval changes field scope, not the project's safety model.

Every run still needs exact item limits, candidate caps, raw-storage boundaries, redaction checks, second-review ownership, and stop conditions.

## Consequences

- Evidence-scope gate 0014 is completed as `approve_narrow_expansion`.
- Item 0018 can move from blocked to eligible for a new bounded run record.
- The next run must be opened before collection starts.
- Raw evidence, screenshots, full URLs, handles, cookies, tokens, browser profiles, HAR files, full API responses, and sensitive investigative notes remain outside git.
- Any selected item must be reduced to approved redacted fields, built locally, strict-validated, and second-reviewed before counting.

## Follow-Up

Open run 0015 as the first evidence-expansion run record for at most 10 selected items, beginning with item 0018.

Run 0015 must cite gate 0014 and define:

- allowed evidence families;
- candidate review cap of at most 20 candidates;
- selected item cap of at most 10 items;
- controlled-store raw storage boundary;
- repo-safe redaction boundary;
- second-review requirement;
- stop conditions.
