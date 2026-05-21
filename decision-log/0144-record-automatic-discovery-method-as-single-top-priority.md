# Decision 0144: Record Automatic Discovery Method As Single Top Priority

Date: 2026-05-05

Status: accepted as project priority rule

## Decision

Record that this repo has one highest priority:

```text
Design a governed automatic or assisted method for discovering review-worthy Threads investment-scam candidates.
```

All other goals are subordinate to this priority. Governance, documentation, reports, schema work, annotation guidance, Reviewer Assist, synthetic policy loops, hard-negative protection, evidence handling, budget analysis, and labor metrics are valid only insofar as they support the discovery method and do not contradict it.

## Rationale

The current collected cases are partial fragments. A project centered on summarizing or inducing patterns from those fragments can become biased and fail to solve the real search problem. The core research need is a method that can automatically or semi-automatically find review-worthy investment-scam candidates on Threads beyond the known examples, then route them through human review with bounded burden and hard-negative protection.

## Consequences

Future work should ask:

```text
Does this improve the governed automatic or assisted discovery method?
```

If the answer is no, the work should be deferred, cut, or reframed.

Future reports and experiments must not present secondary artifacts as independent goals. They should state how they support:

- source-arm and query design;
- candidate surfacing beyond known fragments;
- dedupe and source linkage;
- context gating;
- reviewer-assist preparation;
- human review and second review;
- reviewer-burden measurement;
- hard-negative and insufficient-evidence protection;
- expansion, revision, or pause decisions for the discovery method.

## Scope Boundary

This decision does not authorize:

- unscoped automated Threads or Meta collection;
- broad crawler expansion;
- private-message access;
- account/profile graph capture;
- landing-page or redirect-chain capture outside a later decision;
- model training;
- production detector claims;
- legal fraud determinations;
- enforcement recommendations;
- public warnings;
- raw evidence in git.

Automatic or assisted discovery remains governed method design and evaluation unless a later explicit authorization opens a live data-access path.
