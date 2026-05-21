# Decision 0119: Open Checkpoint 0081 Capped Investment-Scam Discovery Method-Test Decision Review Package

## Status

accepted

## Date

2026-04-27

## Decision

Open a repo-safe review package for decision `0118`, the draft-only capped investment-scam discovery method-test decision.

This decision authorizes preparing and sending decision `0118` for technical/governance and legal/privacy review. It does not authorize method-test execution.

## Context

Decision `0117` recorded technical/governance reviewer status:

```text
approve_design_for_next_decision
```

Decision `0118` then opened a concrete capped method-test decision draft. It proposes source arms, caps, schema fields, signal-combination rules, reviewer workflow, metrics thresholds, hard-negative protections, stop rules, legal/privacy gates, controlled-store boundaries, aggregate reporting, and go/no-go criteria.

The next step is not execution. The next step is to ask reviewers whether decision `0118` is sufficiently specified to proceed toward a future final execution gate.

## Review Package

Package name:

```text
checkpoint-0081-capped-investment-scam-discovery-method-test-decision-review
```

Package path:

```text
/Users/iKev/Downloads/checkpoint-0081-capped-investment-scam-discovery-method-test-decision-review
```

ZIP path:

```text
/Users/iKev/Downloads/checkpoint-0081-capped-investment-scam-discovery-method-test-decision-review.zip
```

## Review Question

Reviewers should answer:

```text
Is decision 0118 concrete enough to support a future capped investment-scam discovery method-test execution approval decision?
```

This is a decision-readiness review. It is not a request to run the method test.

## Reviewer Tracks

### Technical/Governance Track

The technical/governance reviewer should evaluate:

- whether the proposed caps are reasonable;
- whether the source arms are technically and governably usable;
- whether schema fields support dedupe, evidence completeness, signal-family tracking, reviewer burden, hard-negative protection, and stop-rule auditability;
- whether metrics and thresholds are measurable;
- whether hard-negative controls are concrete enough;
- whether stop rules are strong enough to prevent governance drift.

### Legal/Privacy Track

The legal/privacy reviewer should evaluate:

- whether reviewer-supplied candidates may be used;
- whether approved browser-session risk-probe candidates may be used;
- whether OCR-derived text may be processed;
- whether profile-context categories may be recorded;
- whether external-link/contact categories may be recorded;
- what must remain controlled-store-only;
- whether retention, redaction, deletion, and incident handling are adequate;
- whether aggregate outputs may be shared beyond CIB/internal review.

Technical approval does not imply legal/privacy approval.

## Review Status Options

Reviewers should choose one:

```text
approve_0118_for_execution_gate_review
approve_with_conditions
revise_0118_before_gate_review
block_0118
```

## Artifacts Opened

```text
reports/checkpoint-0081-capped-method-test-decision-review-request.md
reports/checkpoint-0081-capped-investment-scam-discovery-method-test-decision-review-package-qa.md
```

## Non-Authorizations

This decision does not authorize:

- method-test execution;
- item `0082`;
- new evidence collection;
- browser/crawler expansion;
- confirmed-pointer intake;
- account/profile graph capture;
- private-message access;
- landing-page or redirect-chain capture;
- embedding/model training;
- production detector claims;
- legal fraud determinations;
- public release;
- automated enforcement;
- raw evidence in git.

## Rationale

Decision `0118` is concrete enough to review, but not executable. A focused decision-review package lets technical/governance and legal/privacy reviewers evaluate caps, source arms, fields, stop rules, controlled-store boundaries, and legal/privacy blockers without opening the evidence pipeline.

This keeps the repo moving toward the first-principle goal of scalable investment-scam candidate discovery while preserving the execution gate.

## Consequences

- Decision `0118` becomes the active review target.
- The review package is prepared for Downloads and external handoff.
- No dispatch log or response tracker is recorded until the package is actually sent.
- No candidate discovery begins.
- Any future execution still requires a separate final approval with all gates satisfied.
