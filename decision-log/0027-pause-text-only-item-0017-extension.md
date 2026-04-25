# Decision 0027: Pause Text-Only Item 0017 Extension

## Date

2026-04-25

## Decision

Pause the item 0017 text-only visible search-result extension and require a scoped evidence-path study before any further item 0017 attempt.

The next step is not another automatic candidate-collection run. The next step is a repo-safe study deciding whether the project should request a narrower evidence-scope expansion, change acquisition path, revise extraction beyond visible search-result text, or stop the item 0017 extension.

## Context

Run 0010 attempted five browser-session risk-probe seeds for item 0017 and selected no safe redacted item.

Run 0011 revised the method by separating candidate diagnostics from item selection, adding a query-echo filter, and testing four revised seeds. One local item 0017 trace was built, but second review excluded it because the retained visible text was only a query echo. After the query-echo filter patch, all revised seeds produced no accepted item 0017.

The local item 0017 trace remains strict-valid as an excluded method-review artifact, but it must not count as an accepted research item and must not unlock item 0018.

## Options Considered

| Option | Decision |
|---|---|
| Keep trying more text-only visible search-result seeds | Rejected; runs 0010 and 0011 already show low yield and query/interface echo risk. |
| Advance to item 0018 anyway | Rejected; item 0017 has no accepted strict-valid research item. |
| Treat excluded item 0017 as accepted because it is schema-valid | Rejected; schema validity is not evidence validity. |
| Expand immediately to replies, screenshots/OCR, links, profiles, or landing pages | Rejected for now; each requires explicit scoped authorization and a new run record. |
| Pause collection and open a scoped evidence-path study | Accepted. |

## Rationale

The current blocker is no longer access readiness, query design, or schema validation. The blocker is evidence sufficiency within the currently allowed field scope. Text-only visible search-result candidates are not producing independent reviewable content for item 0017.

Continuing to add seeds would mostly increase cost and false-positive pressure. A scoped evidence-path study can decide which evidence expansion, if any, is justified before the project changes data handling or collection scope.

## Consequences

- Do not advance to item 0018.
- Do not create another item 0017 attempt under the same text-only search-result method.
- Do not count the excluded item 0017 trace as an accepted research item.
- The latest accepted dataset checkpoint remains the 16 accepted records, plus an excluded local method-review trace for item 0017.
- A new run record is required before any additional item 0017 attempt.
- Any expansion to replies, screenshots/OCR, external links, landing pages, profile context, or redirects must be explicitly scoped before collection.

## Follow-Up

Open a repo-safe evidence-path study that compares:

1. keep current field scope and stop item 0017 extension;
2. allow a narrow reply-context check;
3. allow screenshot/OCR only for candidate reviewability;
4. allow domain-only external-link or redirect-category evidence;
5. switch to an approved API/session-aware path if it can return structured candidate content without raw-response leakage.

The study must recommend one next run design before any new collection.
