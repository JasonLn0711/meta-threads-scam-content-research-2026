# Decision 0032: Close Run 0015 And Require New Run Design

## Date

2026-04-25

## Decision

Close run 0015 for further collection and require a new run record or decision before attempting item `0024`.

Run 0015 produced strict-valid and second-reviewed local records through item `0023`, but its 20-candidate review cap has been exhausted. The remaining selected-item capacity cannot be used without a new candidate-review authorization.

## Context

Run 0015 was opened after stakeholders approved all proposed evidence families with limits. It allowed:

- at most 20 candidates reviewed;
- at most 10 selected items;
- approved browser/session execution;
- raw/session/candidate artifacts in the controlled store only;
- repo-safe redacted local records;
- second review before counting.

The run reviewed 20 candidates and selected 6 local items, `0018` through `0023`. Second review finalized 4 `non_scam` / `low` false-positive pressure cases and 2 `uncertain` / `medium` boundary cases.

The project owner also recorded a CIB policy preference: for this pilot, false negatives are more harmful than explainable false positives. The owner further clarified that scam evidence may appear in replies/comments, including scam websites, scam links, LINE or other messaging-app links, add-friend links, and other private-channel migration signals.

## Options Considered

| Option | Decision |
|---|---|
| Continue run 0015 until 10 selected items | Rejected; the candidate-review cap is already exhausted. |
| Treat the 23-record checkpoint as enough to proceed to broad 50-item completion | Rejected; the sample still has no final `scam` or high-risk records. |
| Close run 0015 and require a new bounded run design before item `0024` | Accepted. |

## Rationale

The latest checkpoint proves the richer evidence pipeline can build and validate records, but it also shows a budget-design flaw: one seed consumed the full candidate-review cap before later seed families were sampled.

The next run should rebalance the candidate budget across seed families, include a bounded reply/comment evidence lane when authorized by the run record, and preserve the same raw-data controls, redaction rules, strict validation, and second-review gates.

## Consequences

- Item `0024` remains blocked until a new run record or decision is opened.
- Run 0015 remains usable as evidence for pipeline readiness and false-positive/uncertainty calibration.
- Run 0015 does not authorize item `0028`.
- The project should not claim high-risk case-finding success from this checkpoint.
- The next design must separate candidate budget, selected-item budget, and seed-family coverage.
- The next design must prioritize false-negative reduction at triage while preserving human second review before final labels.
- Top-level post text alone is insufficient when approved reply/comment evidence is available.

## Follow-Up

Open the next bounded run design before item `0024`.

The next design should set per-seed or per-family candidate caps so guaranteed-outcome, private-channel migration, wallet/deposit action, urgency, testimonial proof, and negation/control families each have a chance to be tested without one query exhausting the whole run.

It should also define a narrow reply/comment review window and redaction rule for links, contact handles, add-friend links, wallet/deposit requests, and private-channel migration signals.
