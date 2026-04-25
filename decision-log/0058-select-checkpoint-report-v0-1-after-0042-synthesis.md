# Decision 0058: Select Checkpoint Report v0.1 After 0042 Synthesis

## Status

Accepted.

## Decision

Pause new collection by default and start a CIB/165-facing checkpoint report v0.1 based on the 42-record checkpoint ending at `threads_pilot_v1_0042`.

The next primary artifact is:

- `reports/threads-scam-content-checkpoint-0042-v0.1.md`

This decision does not reject future confirmed-pointer intake. It says the project should not continue collecting by habit until the 42-record evidence system has been turned into a reviewable report and checkpoint decision package.

## Context

The 42-record checkpoint now has:

- 42 strict-valid local records;
- 14 `scam` / high-risk records;
- 22 `non_scam` records;
- 5 `uncertain` records;
- 1 `insufficient_evidence` record;
- a high-recall baseline with recall `1.000` and false negatives `0`;
- a documented false-positive burden of 6;
- a hard-negative anti-scam warning example;
- a run index connecting run records, evaluation notes, decision logs, labels, risk levels, and validation status.

The project has therefore crossed from acquisition feasibility into evidence-system reviewability.

## Options Considered

| Option | Decision | Rationale |
|---|---|---|
| Continue approved confirmed pointers immediately | Defer | Useful, but would increase item count before stakeholders review the current evidence system. |
| Pause collection and create checkpoint report v0.1 | Accepted | Converts current work into a reviewable artifact and prevents uncontrolled scope drift. |
| Start embedding/model training | Rejected | Dataset is too small and biased; model/artifact governance is not approved. |
| Expand broad crawler collection | Rejected | Confirmed-pointer intake is higher-yield; broad crawler expansion would increase governance and source-skew risk. |

## Report Scope

The checkpoint report should include:

- purpose and audience;
- what the 42-record checkpoint proves;
- what it does not prove;
- aggregate label/risk/source/content-shape distribution;
- rule-family summary;
- hard-negative anti-scam warning lesson;
- baseline performance and false-positive/false-negative interpretation;
- governance and redaction boundaries;
- next decision options.

The report must not include raw URLs, handles, raw post text, raw reply text, screenshots, contact IDs, stock names, stock codes, price values, raw HTML, browser/session material, or stakeholder case IDs.

## Consequence

The project should be reviewed as a research evidence system before more data is collected. The next stakeholder-facing decision should choose either:

- resume bounded confirmed-pointer intake with a fixed small tranche and next checkpoint boundary; or
- keep collection paused and refine report/rule guidance for CIB/165 review.
