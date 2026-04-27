# Decision 0114: Open Checkpoint 0081 Shadow Pilot Readiness Gap Analysis

## Status

accepted

## Date

2026-04-27

## Decision

Open a design-only operational-readiness gap analysis for checkpoint `threads_pilot_v1_0081`.

This decision does not authorize a shadow pilot.

This decision does not authorize new evidence collection.

## Context

Checkpoint `threads_pilot_v1_0081` is accepted for internal research checkpoint use with conditions. The next useful question is no longer whether the repo can collect another item. The next useful question is whether the evidence system, annotation rules, reviewer workflow, governance boundary, metrics, and stop rules are ready to support a future shadow-only operational pilot design.

The gap analysis is recorded in:

```text
reports/checkpoint-0081-shadow-pilot-readiness-gap-analysis.md
```

## Scope

The gap analysis may identify:

- recipient adoption gates;
- technical/governance review needs;
- legal/privacy boundary needs;
- shadow-pilot SOP requirements;
- reviewer workflow fields;
- reviewer burden metrics;
- false-positive and false-negative pressure metrics;
- hard-negative protection requirements;
- evidence intake boundaries;
- stop/no-go rules;
- future decision requirements.

## Non-Authorizations

This decision does not authorize:

- item `0082` or later;
- a shadow pilot execution;
- new confirmed-pointer intake;
- broad browser-session expansion;
- crawler/search-query candidate discovery;
- account/profile graph capture;
- private-message access;
- landing-page or redirect-chain capture;
- embedding or model training;
- production detection;
- legal fraud determinations;
- external sharing;
- public release;
- raw evidence in git.

## Rationale

Checkpoint 0081 has enough research value to support internal adoption and workflow planning. It does not yet have enough operational evidence, legal/privacy clearance, reviewer-burden measurement, or stop-rule maturity to support deployment or broad expansion.

Opening a design-only readiness gap analysis moves the repo forward without confusing readiness planning with execution authorization.

## Consequences

- The repo can now discuss shadow-pilot readiness without opening item `0082`.
- Future collection remains blocked until a separate capped decision is recorded.
- Future shadow-pilot execution remains blocked until a separate capped decision records source boundary, candidate cap, reviewer roles, legal/privacy status, evidence boundary, retention, redaction, metrics, stop rules, and reporting format.
- Baseline metrics remain smoke-test calibration evidence only, not production performance claims.

## Next Step

Use the gap analysis to prepare a draft shadow-pilot charter.

The draft charter must remain design-only unless a later decision explicitly authorizes a capped shadow-only pilot.
