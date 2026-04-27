# Decision 0124: Record Track B Day 1 Source-Arm Intake Start

## Status

accepted

## Date

2026-04-28

## Decision

Record Track B Day 1 source-arm intake start under run `0054`.

This decision opens the Day 1 intake-control layer for Track B. It does not record any surfaced, reviewed, accepted, or validated candidates yet.

## Context

Decision `0122` authorized Track B start after formal signoff. Decision `0123` recorded Day 0 operational start and local-only workspace readiness.

The next step is to begin Day 1 source-arm intake control so future candidates can be counted, deduped, reviewed, second-reviewed, hard-negative checked, and stopped if thresholds are crossed.

## Scope

Day 1 may use only the locked Track B source arms:

| Source arm | Surfaced candidate cap |
|---|---:|
| Checkpoint-derived seed replay | 30 |
| Reviewer-supplied candidates | 30 |
| Approved browser-session risk-probe matrix | 110 |
| Reply/comment funnel cue candidates | 60 |
| OCR/image-cue candidates | 20 |
| Hard-negative probe arm | 50 |

Total surfaced candidate cap: `300`.

Human-reviewed candidate cap: `150`.

Accepted strict-valid record cap: `75`.

No overflow queue is allowed.

## Day 1 Opening Counters

| Metric | Value |
|---|---:|
| Candidates surfaced | 0 |
| Candidates reviewed | 0 |
| Accepted strict-valid records | 0 |
| Duplicate count | 0 |
| Insufficient-evidence count | 0 |
| Hard-negative false-positive pressure count | 0 |
| Stop-rule triggers | 0 |

## Required Daily Stop-Rule Check

Day 1 must record:

- surfaced candidates;
- reviewed candidates;
- source-arm counts;
- duplicate rate;
- insufficient-evidence rate;
- hard-negative false-positive pressure;
- average reviewer time;
- second-review rate;
- reviewer disagreement rate;
- raw evidence leakage;
- stop-rule triggers;
- pause requirement.

## Non-Authorizations

This decision does not authorize:

- item `0082`;
- open-ended collection;
- broad crawler/browser expansion;
- private-message access;
- account/profile graph capture;
- landing-page or redirect-chain capture;
- model or embedding training;
- production detector claims;
- legal fraud determinations;
- automated enforcement;
- public release;
- raw evidence in git;
- any activity outside the locked Track B caps.

## Next Action

Proceed with the first Day 1 source-arm activity only if each candidate can be recorded in repo-safe form and raw evidence remains controlled-store-only.

If no candidate is surfaced during a Day 1 block, record a zero-count daily stop-check rather than silently extending the run.
