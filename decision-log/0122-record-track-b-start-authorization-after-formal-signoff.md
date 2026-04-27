# Decision 0122: Record Track B Start Authorization After Formal Signoff

## Status

accepted

## Date

2026-04-27

## Decision

Record that Track B formal signoff conditions are satisfied and Track B may begin under locked caps.

## Track

`track_b_capped_live_method_test`

## Signoff Basis

| Signoff | Status |
|---|---|
| Legal/privacy reviewer | `no_veto` |
| CIB/internal owner | `accepted_boundary` |
| Technical/governance controls | `confirmed_controls` |
| Controlled-store custodian alias | assigned |
| Reviewer role aliases | assigned |
| Strict validation target | ready |
| Raw-evidence exclusion procedure | ready with conditions |

## Scope

Track B is a capped live investment-scam candidate-discovery method test.

Track B is designed to evaluate whether checkpoint 0081-derived signal families can discover review-worthy Threads investment-scam candidates under capped, human-reviewed, aggregate-only, repo-safe conditions.

## Locked Caps

| Cap | Value |
|---|---:|
| Surfaced candidates | 300 |
| Human-reviewed candidates | 150 |
| Accepted strict-valid records | 75 |
| Intake window | 14 calendar days |

| Source arm | Surfaced candidate cap |
|---|---:|
| Checkpoint-derived seed replay | 30 |
| Reviewer-supplied candidates | 30 |
| Approved browser-session risk-probe matrix | 110 |
| Reply/comment funnel cue candidates | 60 |
| OCR/image-cue candidates | 20 |
| Hard-negative probe arm | 50 |

No overflow queue is allowed.

## Required Daily Stop-Rule Check

Track B must run a daily stop-rule check covering:

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

## Stop Conditions

Track B pauses immediately if any of the following occur:

- any raw evidence leakage;
- hard-negative false-positive pressure exceeds threshold;
- duplicate rate exceeds threshold;
- insufficient-evidence rate exceeds threshold;
- average reviewer time exceeds threshold;
- second-review rate exceeds threshold;
- reviewer disagreement rate exceeds threshold;
- private-message boundary pressure appears;
- source cap is exceeded;
- candidate cap is exceeded;
- raw URL, handle, screenshot, raw post text, raw reply text, raw OCR text, contact ID, credential, browser/session artifact, exact controlled-store path, stakeholder case ID, or private recipient detail enters git-facing output;
- baseline output is described or used as enforcement recommendation.

## Reporting

Track B reporting must be aggregate-only.

The final Track B report should answer:

1. Which source arms produced the best review-worthy yield?
2. Which signal-family combinations produced high-risk candidates?
3. Where did hard-negative false-positive pressure appear?
4. Was reviewer burden acceptable?
5. Which stop rules were triggered, if any?
6. Should the method close, revise, or proceed to a second capped tranche?

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

## Rationale

The Track B formal signoff package resolved the remaining hard conditions. Legal/privacy recorded no veto. CIB/internal owner accepted the capped internal research boundary. Technical/governance controls were previously confirmed. Role aliases, controlled-store handling, strict validation target, and raw-evidence exclusion procedure are ready.

Track B may now begin under the locked cap, stop-rule, validation, and aggregate-reporting boundary.
