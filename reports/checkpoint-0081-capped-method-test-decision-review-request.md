# Checkpoint 0081 Capped Method-Test Decision Review Request

## Purpose

Request technical/governance and legal/privacy review of decision `0118`, the draft-only capped investment-scam discovery method-test decision.

This is a decision-readiness review. It is not a method-test execution request and does not authorize new evidence collection.

## Review Package

| Field | Value |
|---|---|
| Package name | `checkpoint-0081-capped-investment-scam-discovery-method-test-decision-review` |
| Checkpoint | `threads_pilot_v1_0081` |
| Decision draft reviewed | `decision-log/0118-open-capped-investment-scam-discovery-method-test-decision-draft.md` |
| Request status | `review_request_draft` |
| Execution authorized | no |
| New evidence collection authorized | no |
| Item `0082` authorized | no |
| Browser/crawler expansion authorized | no |
| Model training authorized | no |
| Production detector authorized | no |
| Legal fraud determination authorized | no |

## Review Question

```text
Is decision 0118 sufficiently specified to support a future final approval or rejection of a capped investment-scam discovery method test?
```

## What To Review

Please review whether decision `0118` is concrete enough in these areas:

- proposed caps;
- source-arm design;
- repo-safe method-test schema fields;
- dedupe method;
- evidence completeness score;
- signal-family combination rules;
- reviewer workflow;
- reviewer-burden thresholds;
- hard-negative protection;
- metrics and provisional thresholds;
- stop rules and stop-rule owner requirements;
- legal/privacy execution gate;
- controlled-store and redaction boundary;
- aggregate reporting template;
- go/no-go criteria;
- non-authorization language.

## Technical/Governance Review Focus

Technical/governance reviewers should check:

- whether the proposed `300 / 150 / 75 / 14-day` cap structure is reasonable;
- whether the source arms are useful for measuring discovery yield rather than merely increasing record count;
- whether the schema fields support dedupe, evidence completeness, signal-family tracking, reviewer burden, hard-negative protection, and stop-rule auditability;
- whether the proposed triage rubric is understandable and conservative enough;
- whether the hard-negative second-review triggers are sufficient;
- whether stop rules prevent governance drift;
- whether the draft is precise enough to approve, approve with conditions, revise, or block future execution.

## Legal/Privacy Review Focus

Legal/privacy reviewers should check:

- whether reviewer-supplied candidates can be used;
- whether approved browser-session risk-probe candidates can be used;
- whether OCR-derived text can be processed;
- whether profile-context category can be recorded;
- whether external-link/contact category can be recorded;
- what must remain controlled-store-only;
- whether the retention period must be narrowed;
- whether the redaction standard is sufficient;
- who owns deletion and incident handling;
- whether aggregate outputs can be shared beyond CIB/internal review.

Technical approval does not imply legal/privacy approval.

## Requested Response

| Field | Reviewer response |
|---|---|
| Review package | `checkpoint-0081-capped-investment-scam-discovery-method-test-decision-review` |
| Decision draft reviewed | `0118-open-capped-investment-scam-discovery-method-test-decision-draft` |
| Reviewer role | technical/governance / legal/privacy / other |
| Recommended status | `approve_0118_for_execution_gate_review` / `approve_with_conditions` / `revise_0118_before_gate_review` / `block_0118` |
| Technical concerns |  |
| Governance concerns |  |
| Legal/privacy concerns |  |
| Required changes before execution approval can be considered |  |
| Is execution authorized by this review? | no |
| Is new evidence collection authorized by this review? | no |
| Is item `0082` authorized by this review? | no |
| Is browser/crawler expansion authorized by this review? | no |
| Is model training authorized by this review? | no |
| Is production detector or legal fraud determination authorized by this review? | no |
| Additional notes |  |

## Raw Evidence Boundary

Reviewer responses must remain repo-safe. Do not include:

- raw Threads URLs;
- handles;
- screenshots;
- raw post text;
- raw reply/comment text;
- contact IDs;
- stock names or stock codes;
- price values;
- credentials;
- browser/session artifacts;
- controlled-store paths;
- stakeholder case IDs;
- private recipient details.

## Non-Authorization Boundary

This request does not authorize:

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
