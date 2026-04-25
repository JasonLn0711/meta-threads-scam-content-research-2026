# Decision 0026: Require Method Revision After Run 0010

## Date

2026-04-25

## Decision

Pause item 0017 collection and require a method-revision run before any further item 0017 attempt.

Run 0010 exhausted the planned five-seed browser-session risk-probe matrix without selecting a safe redacted item. The project must not advance to item 0018, rerun the same seed matrix, or expand toward the full 50-item pilot from this result.

## Context

Run 0009 proved that the approved browser-session path can produce a strict-valid local item, but item 0016 second review showed a false-positive risk from negated guaranteed-profit or risk-warning language.

Run 0010 added a negation/risk-warning candidate filter and attempted five risk-probe seeds for item 0017. Each seed reviewed at most five candidates under the approved browser-session path. No candidate met the current selection rule, and no `manual_entry_0017.json` was created.

Repo-safe aggregate diagnostics show that the session path returned candidates, but the retained candidate metadata mostly had no signal family or only one isolated signal family. No candidate was selectable by the current multi-signal rule.

## Options Considered

| Option | Decision |
|---|---|
| Continue directly to item 0018 | Rejected; item 0017 was not selected, built, or strict-validated. |
| Rerun the same five run 0010 seeds | Rejected; repeats a low-yield method without learning. |
| Relax labeling and create item 0017 from query terms alone | Rejected; query terms are retrieval hints, not evidence. |
| Expand allowed evidence to replies, screenshots/OCR, links, profiles, or landing pages immediately | Rejected; this requires a new run record and explicit field scope. |
| Open a method-revision run with candidate diagnostics before selection | Accepted. |

## Rationale

The blocker is no longer access readiness. The blocker is candidate-generation and evidence design. The current text-only visible search-result approach can surface isolated risk vocabulary, but not enough co-occurring evidence to create a reviewable item under the approved field allowlist.

A method-revision run preserves the project boundaries while allowing the team to learn whether the next improvement should be seed design, candidate extraction, evidence requirements, or acquisition path.

## Consequences

- Item 0017 remains uncreated.
- The 16-record local aggregate remains the latest strict-valid dataset checkpoint.
- Run 0010 is complete as a no-selected-item method result.
- A new run 0011 is required before any additional item 0017 attempt.
- Run 0011 must keep raw evidence, session material, URLs, handles, screenshots, and raw candidate text outside git.
- The project still cannot move to item 0018 or the full 50-item pilot.

## Follow-Up

Before item 0017:

1. Open run 0011 as a method-revision run.
2. Define candidate-diagnostic metrics separately from item-selection rules.
3. Use revised seed design that combines visible signal families more deliberately.
4. Decide whether the approved field allowlist is sufficient or whether a new scoped run must request replies, screenshots/OCR, links, or other evidence.
5. Attempt at most one item 0017 only after the revised method gate is recorded.
