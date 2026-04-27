# Decision 0120: Open Final Capped Investment-Scam Discovery Method-Test Execution Authorization Package

## Status

accepted

## Date

2026-04-27

## Decision

Open a final execution authorization package for the capped investment-scam discovery method test proposed in decision `0118`.

This decision does not execute the method test. It prepares the final authorization packet required for technical/governance, legal/privacy, and CIB/internal owner sign-off.

## Context

Decision `0118` opened a draft-only capped method-test decision. Decision `0119` packaged decision `0118` for technical/governance and legal/privacy review.

The aggressive reviewer response was:

```text
Recommended status: approve_0118_for_execution_gate_review
Reviewer stance: 0118 is concrete enough to proceed to final execution authorization gate.
```

The reviewer did not authorize execution. The reviewer recommended preparing the final authorization package now so the project can stop cycling through abstract readiness review and instead ask whether a tightly capped test should be approved.

## Execution Tracks For Final Gate

The final authorization package separates two tracks:

| Track | Scope | New evidence? | Purpose |
|---|---|---:|---|
| Track A | zero-new-evidence dry run using existing repo-safe checkpoint materials | no | Test SOP, schema fields, reviewer workflow, metrics recording, stop-rule logging, and aggregate reporting. |
| Track B | capped live candidate-discovery method test under approved source arms | yes, only if explicitly approved | Test scalable investment-scam candidate discovery yield, reviewer burden, hard-negative pressure, dedupe, and evidence completeness. |

Track A and Track B require separate approval responses. Approval for Track A does not imply approval for Track B.

## Proposed Track B Cap Refinement

Decision `0118` proposed `300 / 150 / 75 / 14 days`. This final-gate package keeps those overall caps and refines the surfaced-candidate source arms to add an explicit hard-negative probe arm.

| Source arm | Surfaced candidate cap |
|---|---:|
| Checkpoint-derived seed replay | 30 |
| Reviewer-supplied candidates | 30 |
| Approved browser-session risk-probe matrix | 110 |
| Reply/comment funnel cue candidates | 60 |
| OCR/image-cue candidates | 20 |
| Hard-negative probe arm | 50 |
| Total | 300 |

Human-reviewed candidate cap remains `150`. Accepted strict-valid record cap remains `75`. Intake window remains `14 calendar days`.

## Artifacts Opened

```text
reports/checkpoint-0081-final-capped-method-test-authorization-request.md
reports/checkpoint-0081-final-capped-method-test-execution-sop.md
reports/checkpoint-0081-final-capped-method-test-reviewer-assignment-table.md
reports/checkpoint-0081-final-capped-method-test-legal-privacy-gate-memo.md
reports/checkpoint-0081-final-capped-method-test-controlled-store-boundary.md
reports/checkpoint-0081-final-capped-method-test-candidate-record-template.md
reports/checkpoint-0081-final-capped-method-test-stop-rule-incident-template.md
reports/checkpoint-0081-final-capped-method-test-aggregate-report-template.md
reports/checkpoint-0081-final-capped-method-test-execution-authorization-package-qa.md
```

## Final-Gate Reviewer Response Options

Reviewers should choose one:

```text
approve_track_a_dry_run_only
approve_track_a_and_track_b_execution
approve_with_conditions
revise_before_execution
block_execution
```

## Required Sign-Off Before Any Execution

Execution may begin only if the final response records:

- approved track scope: Track A only or Track A plus Track B;
- legal/privacy status;
- reviewer role aliases;
- source-arm caps;
- surfaced-candidate cap;
- human-review cap;
- accepted-record cap;
- intake window;
- controlled-store handling;
- retention and redaction rules;
- strict validation command;
- stop-rule owner;
- daily stop-rule check owner;
- aggregate reporting format;
- explicit non-authorizations.

## Non-Authorizations

This decision does not authorize:

- method-test execution;
- item `0082`;
- open-ended collection;
- broad browser/crawler expansion;
- confirmed-pointer intake outside the approved source-arm design;
- account/profile graph capture;
- private-message access;
- landing-page or redirect-chain capture;
- embedding/model training;
- production detector claims;
- legal fraud determinations;
- public warning lists;
- public release;
- automated enforcement;
- raw evidence in git.

## Rationale

The project's first-principle goal is to find a scalable, stable, and reviewable method for discovering Threads investment-scam candidates. Decision `0118` is sufficiently concrete to move to final gate preparation. Continuing to produce abstract readiness artifacts would delay the method test without reducing the main execution risks.

The correct next question is whether reviewers approve Track A, Track B, both with conditions, or neither.

## Consequences

- The active package shifts from decision-readiness review to final execution authorization review.
- Track A can be considered independently from Track B.
- Track B remains blocked until legal/privacy status, reviewer roles, controlled-store handling, source caps, and stop-rule ownership are approved.
- No data collection begins from this decision alone.
