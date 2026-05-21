# Checkpoint 0081 Final Capped Method-Test Execution Authorization Request

## Purpose

Request final gate review for a capped investment-scam discovery method test derived from checkpoint `threads_pilot_v1_0081` and decision `0118`.

This request asks reviewers whether to approve Track A only, approve Track A plus Track B, approve with conditions, revise before execution, or block execution.

This request does not itself authorize execution.

## Package Identity

| Field | Value |
|---|---|
| Package name | `checkpoint-0081-final-capped-investment-scam-discovery-method-test-execution-authorization` |
| Checkpoint | `threads_pilot_v1_0081` |
| Source decision draft | `decision-log/0118-open-capped-investment-scam-discovery-method-test-decision-draft.md` |
| Final package decision | `decision-log/0120-open-final-capped-investment-scam-discovery-method-test-execution-authorization-package.md` |
| Package status | `final_gate_review_request` |
| Execution authorized by this request | no |
| New evidence collection authorized by this request | no |
| Item `0082` authorized | no |

## Requested Decision

Choose exactly one:

```text
approve_track_a_dry_run_only
approve_track_a_and_track_b_execution
approve_with_conditions
revise_before_execution
block_execution
```

## Track A: Zero-New-Evidence Dry Run

Track A uses existing repo-safe checkpoint materials only.

Purpose:

- test the execution SOP;
- test candidate-review record fields;
- test reviewer workflow;
- test second-review triggers;
- test hard-negative checks;
- test daily stop-rule logging;
- test aggregate reporting format;
- test strict-validation readiness.

Track A does not authorize:

- new candidate discovery;
- browser session use;
- new evidence collection;
- raw evidence expansion;
- item `0082`;
- public release.

## Track B: Capped Live Candidate-Discovery Method Test

Track B may proceed only if explicitly approved by final gate response.

Overall proposed caps:

| Cap | Value |
|---|---:|
| Surfaced candidates | 300 |
| Human-reviewed candidates | 150 |
| Accepted strict-valid records | 75 |
| Intake window | 14 calendar days |

Proposed source arms:

| Source arm | Surfaced candidate cap |
|---|---:|
| Checkpoint-derived seed replay | 30 |
| Reviewer-supplied candidates | 30 |
| Approved browser-session risk-probe matrix | 110 |
| Reply/comment funnel cue candidates | 60 |
| OCR/image-cue candidates | 20 |
| Hard-negative probe arm | 50 |

## Pass / Pause Criteria

| Metric | Pass | Fail / pause |
|---|---:|---:|
| Review-worthy yield | >= 40% | < 25% |
| High-risk yield | >= 20% | < 10% |
| Final scam-label yield | >= 15% | < 8% |
| Hard-negative false-positive pressure | <= 15% | > 20% |
| Duplicate rate | <= 25% | > 35% |
| Insufficient-evidence rate | <= 30% | > 40% |
| Average review time | <= 12 min | > 18 min |
| Second-review rate | <= 40% | > 55% |
| Reviewer disagreement rate | <= 20% | > 30% |
| Raw evidence leakage | 0 | any occurrence |
| Enforcement misuse | 0 | any occurrence |

## Required Reviewer Checks

Technical/governance reviewer:

- cap reasonableness;
- source-arm balance;
- reviewer burden;
- hard-negative arm design;
- daily stop-rule checks;
- aggregate report usability;
- no production/enforcement drift.

Legal/privacy reviewer:

- Track A permissibility using repo-safe checkpoint records;
- Track B source-arm permissibility;
- OCR-derived text handling;
- profile-context category handling;
- external-link/contact category handling;
- controlled-store-only boundary;
- retention, deletion, redaction, and incident ownership;
- aggregate sharing boundary.

CIB/internal owner:

- operational need;
- reviewer role assignment;
- source-arm priority;
- stop-rule ownership;
- whether Track A only or Track A plus Track B should proceed.

## Non-Authorization Boundary

This request does not authorize:

- execution without final approval;
- item `0082`;
- open-ended collection;
- broad crawler/browser expansion;
- private-message access;
- account/profile graph capture;
- landing-page or redirect-chain capture;
- embedding/model training;
- production detector claims;
- legal fraud determinations;
- public warning lists;
- automated enforcement;
- raw evidence in git.
