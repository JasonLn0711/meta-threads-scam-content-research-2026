# Decision 0033: Close Run 0016 And Require Method Decision Before Item 0028

## Date

2026-04-25

## Decision

Close run 0016 for further collection and require a new method decision or run record before attempting item `0028`.

Run 0016 produced strict-valid and second-reviewed local records through item `0027`, but its candidate-review cap and selected-item cap are both exhausted. Item `0028` was explicitly blocked in the run record.

## Context

Run 0016 was opened after checkpoint 0023 showed that run 0015 had exhausted its candidate budget before testing all evidence families. Run 0016 corrected that design by using:

- 20 total candidates reviewed;
- 4 candidates per evidence family;
- 4 selected items, `0024` through `0027`;
- a narrow reply/comment evidence lane;
- anti-scam camouflage handling;
- CIB false-negative reduction preference at triage;
- raw/session/candidate artifacts outside git;
- strict validation and second review before counting.

The run selected 4 local items. Second review finalized 2 `non_scam` / `low` false-positive pressure cases and 2 `uncertain` / `medium` boundary cases.

## Options Considered

| Option | Decision |
|---|---|
| Continue directly to item `0028` under run 0016 | Rejected; run 0016 target range and selected-item cap ended at `0027`. |
| Treat checkpoint 0027 as enough to proceed to broad 50-item completion | Rejected; the checkpoint still has no final `scam` or high-risk records. |
| Open a method decision before any item `0028` attempt | Accepted. |

## Rationale

Run 0016 improved candidate budget discipline and recall-oriented evidence coverage, but it did not solve the high-risk case-finding problem. More of the same browser/session search-result path may mostly add false-positive pressure and uncertainty boundaries.

Before item `0028`, the project should explicitly decide whether the next move is:

- another bounded collection run with revised seeds and caps;
- a method review focused on higher-risk acquisition;
- completion of the API/session-aware path;
- stakeholder or CIB handoff for redacted exemplars;
- or a pause for synthesis.

## Consequences

- Item `0028` remains blocked until a new decision or run record is opened.
- Run 0016 remains evidence that reply-aware recall and per-family caps work mechanically.
- The project should not claim high-risk case-finding success from checkpoint 0027.
- The next design must include a concrete high-risk acquisition hypothesis, not only broader candidate review.

## Follow-Up

Create a method decision before item `0028`.

The decision should choose whether to continue collection, complete API readiness, request targeted stakeholder exemplars, or pause for synthesis and reporting.
