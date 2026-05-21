# Decision 0116: Open Checkpoint 0081 Investment-Scam Discovery Method Test Charter Draft

## Status

accepted

## Date

2026-04-27

## Decision

Open a design-only checkpoint 0081 investment-scam discovery method test charter draft.

This decision opens planning artifacts only. It does not authorize execution.

## Context

Decision `0115` realigned the repo around the first-principle goal of finding a scalable, stable, and reviewable method for discovering Threads investment-scam candidates.

The next artifact should not be a generic shadow-pilot charter. It should be a method-test charter draft that asks whether a bounded, reviewable discovery method can find investment-scam candidates across post, thread, account-context, and funnel surfaces while protecting hard negatives.

## Artifacts Opened

```text
reports/checkpoint-0081-investment-scam-discovery-method-test-charter-draft.md
docs/57-investment-scam-discovery-signal-family-matrix.md
```

## Scope

The charter draft may define:

- first-principle discovery goal;
- candidate units: post, thread, account-context, funnel;
- candidate discovery hypotheses;
- signal families;
- hard-negative boundaries;
- candidate source boundaries;
- review workflow;
- review fields;
- discovery-yield and reviewer-burden metrics;
- stop rules;
- expansion criteria;
- required decision contents before execution.

The signal-family matrix may define:

- discovery value by signal family;
- false-positive risk;
- reply/comment dependency;
- OCR dependency;
- hard-negative contrast;
- combination rules;
- review questions.

## Non-Authorizations

This decision does not authorize:

- item `0082` or later;
- candidate-discovery test execution;
- new evidence collection;
- browser/crawler expansion;
- confirmed-pointer intake;
- account/profile graph capture;
- private-message access;
- landing-page or redirect-chain capture;
- embedding or model training;
- production detection;
- legal fraud determinations;
- public release;
- automated enforcement;
- raw evidence in git.

## Rationale

The repo needs a bridge between checkpoint 0081 evidence and a future capped discovery-method test. Without this charter, the next step could drift back into generic package maintenance, low-yield collection, or model work.

This design-only charter keeps the work focused on scalable investment-scam candidate discovery while preserving the governance boundary that any execution requires a later capped decision.

## Consequences

- Future reviewers can evaluate the proposed discovery-method test before any candidate discovery begins.
- The unit of discovery is now explicitly broader than a single post: post, thread, account-context, and funnel candidates are all in scope for design.
- Future experiments must measure candidate yield, high-risk yield, scam-label yield, duplicate rate, reviewer burden, second-review rate, disagreement, hard-negative false-positive pressure, false-negative pressure, and evidence-surface dependency.
- No new collection is opened.

## Next Step

Review the charter draft and signal-family matrix with technical/governance reviewers.

If reviewers accept the design, open a separate capped method-test decision that records source boundary, candidate cap, accepted-record cap, evidence surfaces, reviewer roles, legal/privacy status, retention/redaction boundary, validation command, second-review triggers, metrics, stop rules, reporting format, and explicit non-authorizations.
