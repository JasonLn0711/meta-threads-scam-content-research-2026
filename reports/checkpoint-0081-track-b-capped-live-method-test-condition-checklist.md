# Checkpoint 0081 Track B Capped Live Method-Test Condition Checklist

## Purpose

Record the hard conditions required before Track B can begin under decision `0121`.

Track B is a capped live candidate-discovery method test. It is not item `0082`, not checkpoint continuation by habit, not open-ended collection, and not production detection.

Track B cannot begin until every required condition below is complete.

## Current Status

| Field | Value |
|---|---|
| Authorization decision | `decision-log/0121-record-final-gate-review-response-track-a-now-track-b-conditional.md` |
| Track | `track_b_capped_live_method_test` |
| Execution status | `conditionally_approved_blocked_until_all_conditions_pass` |
| Condition resolution tracker | `reports/checkpoint-0081-track-b-condition-resolution-tracker.md` |
| Item `0082` authorized | no |
| Open-ended collection authorized | no |
| Broad crawler/browser expansion authorized | no |
| Private-message access authorized | no |
| Account/profile graph capture authorized | no |
| Landing-page / redirect-chain capture authorized | no |
| Model training authorized | no |
| Production detector authorized | no |
| Legal fraud determination authorized | no |
| Raw evidence in git authorized | no |

## Hard Condition Checklist

| Condition | Required state before Track B | Current status | Notes |
|---|---|---|---|
| Legal/privacy reviewer status | no veto / approved with recorded conditions | pending | Track B cannot start while unresolved. |
| CIB/internal owner status | accepts capped method-test boundary | pending | Must accept that this is not item `0082` or enforcement. |
| Technical/governance owner status | confirms execution controls | pending | Must confirm caps, metrics, and stop-rule use. |
| Controlled-store custodian | assigned | pending | Required for any live evidence boundary. |
| Primary reviewer role alias | assigned | pending | Repo-safe alias only. |
| Second reviewer role alias | assigned | pending | Repo-safe alias only. |
| Stop-rule owner | assigned | pending | Required before any candidate intake. |
| Daily stop-check owner | assigned | pending | Required before any candidate intake. |
| Validation owner | assigned | pending | Must own strict validation output. |
| Reporting owner | assigned | pending | Must own aggregate-only reporting. |
| Source-arm caps | locked | pass | Caps inherited from decision `0121`; no overflow queue. |
| Surfaced candidate cap | locked at 300 | pass | No overflow queue. |
| Human-reviewed candidate cap | locked at 150 | pass | No overflow queue. |
| Accepted strict-valid record cap | locked at 75 | pass | No overflow queue. |
| Intake window | locked at 14 calendar days | pass | No extension without later decision. |
| Daily stop-rule checklist | ready | pass | `reports/checkpoint-0081-final-capped-method-test-stop-rule-incident-template.md` |
| Candidate record template | ready | pass | `reports/checkpoint-0081-final-capped-method-test-candidate-record-template.md` |
| Aggregate-only report template | ready | pass | `reports/checkpoint-0081-final-capped-method-test-aggregate-report-template.md` |
| Controlled-store boundary | documented | pass_pending_custodian | `reports/checkpoint-0081-final-capped-method-test-controlled-store-boundary.md`; custodian still pending. |
| Strict validation command | command shape ready | pending_output_target | Use `python3 scripts/validate_thread_dataset.py <track_b_dataset>.json --strict` after an approved repo-safe output exists. |
| Raw evidence exclusion scan/check | required | pending | Must be run before any Track B report is committed. |
| Track A dry-run result | should be complete before Track B | pass_with_limitations | `reports/checkpoint-0081-track-a-zero-new-evidence-dry-run-report.md`; limitations must be reviewed before Track B. |
| Track A limitation mapping | limitations mapped to Track B controls | pass | `reports/checkpoint-0081-track-b-condition-resolution-tracker.md` maps each limitation to a Track B control. |

## Source-Arm Caps

| Source arm | Surfaced candidate cap |
|---|---:|
| Checkpoint-derived seed replay | 30 |
| Reviewer-supplied candidates | 30 |
| Approved browser-session risk-probe matrix | 110 |
| Reply/comment funnel cue candidates | 60 |
| OCR/image-cue candidates | 20 |
| Hard-negative probe arm | 50 |
| Total | 300 |

Human-reviewed candidate cap: `150`.

Accepted strict-valid record cap: `75`.

Intake window: `14 calendar days`.

## Required Stop Thresholds

Track B must pause or stop when thresholds below are crossed.

| Metric | Pass | Pause / stop |
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
| Baseline misuse as enforcement | 0 | any occurrence |

## Hard-Negative Probe Requirement

Track B is not valid without the hard-negative probe arm.

The hard-negative probe arm must test false-positive pressure against:

- genuine anti-scam warning;
- ordinary investment discussion;
- financial education;
- general market commentary;
- personal investment journaling;
- legitimate finance creator content;
- public contact information without funnel behavior;
- educational chart or screenshot content;
- news discussion;
- risk warning content.

## Track B Explicit Prohibitions

Track B must not include:

- private-message access;
- account/profile graph capture;
- landing-page or redirect-chain capture;
- raw URL, handle, screenshot, raw post text, raw reply text, contact ID, stock identifier, credential, browser/session artifact, exact controlled-store path, stakeholder case ID, or private recipient detail in git;
- production detector claims;
- legal fraud determinations;
- automated enforcement;
- public warning lists;
- model or embedding training;
- overflow queue beyond caps.

## Minimum Start Condition

Track B may begin only when all `pending` or `pass_pending_*` fields in this checklist are resolved to `pass` or a recorded condition that does not block execution.

If any hard condition remains unresolved, Track B remains blocked and only Track A may proceed.

## Next Action

Do not open another abstract review package.

Do:

1. collect repo-safe condition responses in `reports/checkpoint-0081-track-b-condition-resolution-tracker.md`;
2. resolve Track B pending conditions;
3. start Track B only after this checklist is fully green.
