# Decision 0143: Record Sample Incompleteness And Discovery-Design Purpose

Date: 2026-05-05

Status: accepted as forward-looking project correction

## Decision

Record that the currently collected and reviewed Threads investment-scam-like cases are partial fragments, not a representative sample of all Threads investment scams.

Future work must treat existing examples as:

- seed hypotheses;
- source-arm design inputs;
- signal-family candidates;
- hard-negative controls;
- reviewer-workflow examples;
- bounded evaluation slices.

Future work must not treat existing examples as:

- the complete Threads investment-scam population;
- a platform-wide prevalence estimate;
- a complete taxonomy of scam strategies;
- proof that unobserved patterns are unimportant;
- sufficient evidence that a discovery method has solved the real search problem.

## Rationale

Retrospective induction from a limited case set can distort the research direction. The project goal is not to summarize the current examples more elegantly. The project goal is to design a governed automatic or assisted method for finding review-worthy Threads investment-scam candidates beyond the current fragments, then measure whether that method works with acceptable reviewer burden and hard-negative protection.

## Scope Boundary

This correction does not authorize:

- open-ended Threads or Meta collection;
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

Automatic or assisted discovery remains a design and evaluation objective. Any live data access, collection method, source-arm expansion, or automation run still requires explicit governed authorization.

## Consequences

Future reports, source-arm plans, policy-routing work, reviewer-assist evaluation, and signal-family updates should state whether they are:

- learning hypotheses from existing fragments;
- testing those hypotheses on new bounded slices;
- measuring discovery yield and reviewer burden;
- protecting against overfitting to known cases;
- preserving hard-negative and insufficient-evidence boundaries.

Claims about "what Threads investment scams look like" must be replaced with narrower claims about the reviewed slice, the tested source arm, or the evaluated routing policy unless a later representative sampling design supports broader language.

## Next Action

Use this correction when opening the Reviewer Assist Layer labor-savings evaluation. The evaluation should support automatic or assisted candidate discovery and should not become a case-summary exercise over the existing finite set.
