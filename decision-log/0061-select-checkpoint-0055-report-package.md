# Decision 0061: Select Checkpoint 0055 Report Package

## Status

Accepted.

## Decision

Pause new collection by default and create a CIB/165-facing checkpoint report package based on the 55-record checkpoint ending at `threads_pilot_v1_0055`.

The next primary artifacts are:

- `reports/threads-scam-content-checkpoint-0055-v0.1.md`
- `reports/checkpoint-0055-decision-request.md`
- `reports/checkpoint-0055-review-checklist.md`

This decision does not reject future collection. It says the project should not open another browser-session tranche by habit after run 0038 reached its caps.

## Context

The 55-record checkpoint now has:

- 55 strict-valid local records;
- 17 `scam` / high-risk records;
- 23 `non_scam` records;
- 9 `uncertain` records;
- 6 `insufficient_evidence` records;
- a high-recall baseline with recall `1.000` and false negatives `0`;
- a documented false-positive burden of 7;
- a hard-negative anti-scam warning boundary;
- a closed stakeholder-approved Option A browser-session tranche;
- a run index connecting run records, evaluation notes, decision logs, labels, risk levels, and validation outcomes.

Run 0038 showed that approved browser-session capture is operationally feasible, but it mainly added uncertainty and insufficient-evidence examples instead of final scam/high-risk records.

## Options Considered

| Option | Decision | Rationale |
|---|---|---|
| Open another browser-session tranche immediately | Rejected by default | The latest tranche reached caps and did not add final scam/high-risk examples. Another tranche needs an explicit calibration purpose and new caps. |
| Wait for confirmed pointers only | Allowed later | Confirmed pointers remain the higher-yield source for final scam/high-risk rule learning. |
| Create checkpoint 0055 report package | Accepted | Converts the current evidence system into a reviewable stakeholder artifact and prevents collection drift. |
| Start embedding/model training | Rejected | Dataset is too small and biased; model/artifact governance is not approved. |
| Expand broad crawler collection | Rejected | Broad expansion would increase governance, privacy, and source-skew risk without a clear evidence gap. |

## Report Scope

The checkpoint report should include:

- purpose and audience;
- what the 55-record checkpoint proves;
- what it does not prove;
- aggregate label/risk/source/content-shape distribution;
- delta from checkpoint 0042;
- rule-family and hard-negative lessons;
- baseline performance and false-positive/false-negative interpretation;
- acquisition lesson comparing confirmed pointers and browser-session candidate search;
- governance and redaction boundaries;
- next decision options.

The report must not include raw URLs, handles, raw post text, raw reply text, screenshots, contact IDs, stock names, stock codes, price values, raw HTML, browser/session material, or stakeholder case IDs.

## Consequence

The next stakeholder-facing decision should choose one of:

- pause browser-session expansion and wait for CIB/stakeholder confirmed pointers;
- use the 55-record checkpoint as the current CIB/165-facing review package;
- open another bounded browser-session tranche only for calibration, with explicit candidate and selected-item caps.

No item `0056` collection should begin until that decision is recorded.
