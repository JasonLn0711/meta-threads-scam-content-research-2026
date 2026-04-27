# Decision 0117: Record Checkpoint 0081 Investment-Scam Discovery Method Technical/Governance Review Response

## Status

accepted

## Date

2026-04-27

## Decision

Record the technical/governance reviewer response for the checkpoint `threads_pilot_v1_0081` investment-scam discovery method design package.

Reviewer status:

```text
approve_design_for_next_decision
```

Reviewer conclusion:

```text
The design is sufficient to proceed to a capped investment-scam discovery method-test decision draft.
```

## Context

Decision `0116` opened a design-only method-test charter draft and signal-family matrix for the first-principle research goal:

```text
Find a scalable, stable, and reviewable method for discovering Threads investment-scam candidates at volume.
```

The technical/governance reviewer accepted the design as mature enough for the next decision gate. The reviewer did not request another abstract governance package, generic shadow-pilot charter, or further package polishing before the next decision draft.

The reviewer emphasized that approval for next-decision planning is not execution authorization.

## Reviewer Response Summary

| Field | Response |
|---|---|
| Checkpoint reviewed | `threads_pilot_v1_0081` |
| Review package | `checkpoint-0081-investment-scam-discovery-method-technical-governance-review` |
| Review status | `approve_design_for_next_decision` |
| Can this design support a later capped method-test decision? | yes |
| Required technical changes | not blocking; move concrete fields into decision `0118` |
| Required governance changes | not blocking; convert into execution gates, stop rules, caps, and redaction rules in decision `0118` |
| Missing fields or schema concerns | address in decision `0118` through candidate-source, dedupe, evidence-completeness, signal-combination, reviewer-burden, and stop-rule audit fields |
| Missing metrics or burden measures | address in decision `0118` with provisional thresholds |
| Hard-negative / false-positive concerns | controlled by the capped method-test design; hard-negative pressure should become a primary metric |
| Legal/privacy blockers before execution | execution requires recorded legal/privacy status; drafting decision `0118` may proceed first |
| New evidence collection authorized by this response? | no |
| Item `0082` authorized by this response? | no |
| Browser/crawler expansion authorized by this response? | no |
| Embedding/model training authorized by this response? | no |
| Production detector or legal fraud determination authorized by this response? | no |

## Scope

This decision records design approval for next-decision planning only.

The next artifact must be:

```text
decision-log/0118-open-capped-investment-scam-discovery-method-test-decision-draft.md
```

Decision `0118` must be concrete enough for reviewers to approve, approve with conditions, revise, or reject future execution. It should not remain at the level of abstract readiness planning.

## Required Next Artifact Contents

Decision `0118` must specify:

- proposed execution boundary;
- candidate cap;
- human-review cap;
- accepted strict-valid record cap;
- intake window;
- source-arm design;
- signal-family triage rubric;
- candidate schema;
- dedupe method;
- evidence completeness score;
- reviewer workflow;
- reviewer burden threshold;
- hard-negative second-review triggers;
- metrics thresholds;
- stop-rule owners;
- legal/privacy execution gate;
- controlled-store and redaction boundary;
- aggregate reporting template;
- non-authorization statement;
- go/no-go criteria.

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

The technical/governance reviewer judged that the repo should stop polishing decision `0116` and move into a concrete capped decision draft. This advances the first-principle goal without confusing design approval with execution authorization.

The useful next question is no longer whether the charter is conceptually ready. It is whether a proposed capped method test has acceptable caps, sources, reviewer roles, legal/privacy gates, stop rules, and reporting boundaries.

## Consequences

- Decision `0118` is now the immediate next planning artifact.
- No collection begins from this review response.
- Any future execution must be separately approved after decision `0118` is reviewed.
- Legal/privacy status is required before execution, not before drafting decision `0118`.
- Hard-negative pressure, reviewer burden, dedupe load, evidence completeness, and source-arm yield must be treated as first-order method-test metrics.
