# Checkpoint 0081 Track B Condition Resolution Tracker

## Purpose

Track the hard conditions that must be resolved before Track B capped live method-test execution can begin.

This is an operational gate tracker, not another review package and not an abstract readiness cycle.

Track B remains blocked until every required condition is resolved in repo-safe form.

## Current Status

| Field | Value |
|---|---|
| Checkpoint | `threads_pilot_v1_0081` |
| Related decision | `decision-log/0121-record-final-gate-review-response-track-a-now-track-b-conditional.md` |
| Track A result | `reports/checkpoint-0081-track-a-zero-new-evidence-dry-run-report.md` |
| Track B checklist | `reports/checkpoint-0081-track-b-capped-live-method-test-condition-checklist.md` |
| Condition response request | `reports/checkpoint-0081-track-b-condition-response-request.md` |
| Track B status | `blocked_pending_condition_signoff` |
| Item `0082` authorized | no |
| Open-ended collection authorized | no |
| Broad crawler/browser expansion authorized | no |
| Raw evidence in git authorized | no |

## Blocking Conditions

| Condition group | Required repo-safe response | Current status | Blocks Track B? | Notes |
|---|---|---|---:|---|
| Legal/privacy no-veto | `no_veto` / `approved_with_conditions` / `veto` | pending | yes | Must cover approved browser-session candidates, reply/comment categorization, OCR-derived text handling, profile-context categories, external contact/link categories, retention, deletion, redaction, and aggregate sharing boundary. |
| CIB/internal owner acceptance | `accepted_boundary` / `accepted_with_conditions` / `not_accepted` | pending | yes | Must confirm capped method-test boundary and no enforcement/legal-determination use. |
| Technical/governance execution control | `confirmed_controls` / `confirmed_with_conditions` / `not_confirmed` | pending | yes | Must confirm caps, source arms, metrics, daily stop checks, hard-negative arm, and no overflow queue. |
| Controlled-store custodian | repo-safe custodian alias recorded | pending | yes | Must be assigned before any live evidence boundary is used. |
| Track B reviewer role aliases | repo-safe role aliases recorded | pending | yes | Must assign primary reviewer, second reviewer, stop-rule owner, daily stop-check owner, validation owner, and reporting owner. |
| Raw-evidence exclusion check | pre-commit/check command or procedure recorded | pending | yes | Must be ready before any Track B report is committed. |
| Track A limitations reviewed | limitations mapped to Track B controls | pass | no | See section below. |

## Track A Limitation Mapping

Track A completed with limitations. Those limitations become Track B controls:

| Track A limitation | Track B control |
|---|---|
| Real human reviewer time was not measured | Track B must record `review_time_minutes` for every reviewed candidate and daily average review time. |
| Duplicate rate was not measured | Track B must record dedupe status, duplicate cluster IDs when repo-safe, and duplicate rate by source arm. |
| Hard-negative false-positive pressure was not measured | Track B must preserve the 50-candidate hard-negative probe arm and report hard-negative FP pressure. |
| OCR quality was not tested | Track B OCR/image source arm must record `ocr_needed`, `ocr_decisive`, and `ocr_quality` without raw OCR in git. |
| Controlled-store handling was not tested | Track B cannot start until controlled-store custodian and legal/privacy boundary are recorded. |

## Proposed Repo-Safe Track B Role Aliases

These aliases are proposed placeholders. They do not identify private people, account IDs, email addresses, or external contact details.

| Role | Proposed alias | Status |
|---|---|---|
| Primary Track B reviewer | `track_b_primary_reviewer_role` | pending confirmation |
| Second Track B reviewer | `track_b_second_reviewer_role` | pending confirmation |
| Technical/governance owner | `track_b_technical_governance_owner` | pending confirmation |
| Legal/privacy owner | `track_b_legal_privacy_owner` | pending confirmation |
| Controlled-store custodian | `track_b_controlled_store_custodian` | pending confirmation |
| Stop-rule owner | `track_b_stop_rule_owner` | pending confirmation |
| Daily stop-check owner | `track_b_daily_stop_check_owner` | pending confirmation |
| Validation owner | `track_b_validation_owner` | pending confirmation |
| Reporting owner | `track_b_reporting_owner` | pending confirmation |
| CIB/internal owner | `track_b_cib_internal_owner` | pending confirmation |

## Required Source And Cap Locks

These are already locked by decision `0121` and must not be changed without a later decision.

| Source arm | Surfaced candidate cap |
|---|---:|
| Checkpoint-derived seed replay | 30 |
| Reviewer-supplied candidates | 30 |
| Approved browser-session risk-probe matrix | 110 |
| Reply/comment funnel cue candidates | 60 |
| OCR/image-cue candidates | 20 |
| Hard-negative probe arm | 50 |
| Total | 300 |

| Cap | Value |
|---|---:|
| Human-reviewed candidates | 150 |
| Accepted strict-valid records | 75 |
| Intake window | 14 calendar days |

No overflow queue is allowed.

## Repo-Safe Response Form

Use this response shape to resolve the pending conditions.

```text
Track B condition response

Legal/privacy status:
no_veto / approved_with_conditions / veto

CIB/internal owner status:
accepted_boundary / accepted_with_conditions / not_accepted

Technical/governance status:
confirmed_controls / confirmed_with_conditions / not_confirmed

Controlled-store custodian alias:
[repo-safe alias only]

Reviewer role aliases:
- primary:
- second:
- stop-rule owner:
- daily stop-check owner:
- validation owner:
- reporting owner:

Raw-evidence exclusion check:
ready / not_ready / conditions

Conditions:
[repo-safe text only]

Explicit non-authorizations confirmed:
yes / no
```

Do not include real names, private contact details, raw Threads URLs, handles, screenshots, raw post text, raw reply text, contact IDs, credentials, browser/session artifacts, exact controlled-store paths, stakeholder case IDs, or private recipient details.

## Explicit Non-Authorizations

This tracker does not authorize:

- Track B execution before all conditions pass;
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
- raw evidence in git.

## Next Action

Collect repo-safe condition responses using:

```text
reports/checkpoint-0081-track-b-condition-response-request.md
```

After every blocking condition is resolved, update:

```text
reports/checkpoint-0081-track-b-capped-live-method-test-condition-checklist.md
```

Do not start Track B until that checklist is fully green.
