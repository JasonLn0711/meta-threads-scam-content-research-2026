# Decision 0029: Stop Item 0017 Extension After Run 0013

## Date

2026-04-25

## Decision

Stop the item 0017 extension for the current pilot tranche after run 0013 produced no reviewable candidate under the approved scoped evidence-path boundaries.

Do not advance to item 0018 from the current method. The accepted dataset checkpoint remains 16 accepted records, plus one excluded local item 0017 method-review trace that does not count as an accepted research item.

## Context

Run 0010 attempted five browser-session risk-probe seeds for item 0017 and selected no safe redacted item.

Run 0011 revised the method, separated diagnostics from item selection, and added query-echo filtering. A local item 0017 trace was built, but second review excluded it because retained visible text was only a query echo. All follow-up revised seeds produced no accepted item 0017.

Decision 0028 selected the smallest evidence-scope change still allowed by the current project boundaries: domain-only visible-link or redirect-category evidence plus narrow reply-context feasibility. Run 0013 executed one scoped item 0017 attempt. It found aggregate external-domain evidence, but no independent reviewable candidate content, no known redirect category, and no narrow reply-context feasibility.

## Options Considered

| Option | Decision |
|---|---|
| Continue item 0017 with more seeds under the same scoped method | Rejected; the blocker is evidence sufficiency, not seed count. |
| Treat aggregate domain-only evidence as enough to create item 0017 | Rejected; aggregate link counts are method evidence, not item-level review evidence. |
| Refine domain/redirect classification without landing pages | Deferred; may support future diagnostics but does not solve reviewability alone. |
| Request screenshots/OCR, landing pages, full redirect-chain capture, broad replies, or profile review | Rejected for this tranche; each requires explicit stakeholder-approved scope expansion. |
| Advance to item 0018 anyway | Rejected; item 0017 has no accepted strict-valid research item. |
| Stop item 0017 extension for the current pilot tranche | Accepted. |

## Rationale

The project has now tested the access path, risk-probe query design, query-echo filtering, revised diagnostic gates, and the smallest scoped evidence-path expansion. The remaining blocker is not tooling or validation. It is that the approved field allowlist does not produce enough independent, reviewable item-level evidence for item 0017 from this source path.

Continuing collection under the same boundaries would increase reviewer burden and false-positive pressure without changing the evidence problem. Expanding into screenshots/OCR, landing pages, redirect chains, broad replies, or profile context may be research-relevant later, but it changes privacy, storage, platform, and stakeholder-review requirements.

## Consequences

- Accepted records remain at 16.
- The local item 0017 trace remains excluded and must not count as an accepted research item.
- Item 0018 remains blocked.
- Run 0013 is closed with method review complete.
- The next repo-safe work should be pilot synthesis or a stakeholder evidence-expansion memo, not another collection run.
- Any future item 0017 retry requires a new scoped decision before collection.

## Follow-Up

Prepare a synthesis or stakeholder-facing method memo that states:

1. why the first 16 accepted records are the current checkpoint;
2. why item 0017 was stopped rather than forced;
3. which evidence expansion would be needed to study higher-risk cases more effectively;
4. which raw-data controls, redaction checks, and stop conditions would be required before that expansion.
