# Pilot Authorization Register

## Purpose

Use this register to track whether a source, collection method, and field set are approved for the Threads pilot.

This file is a governance index, not a place for sensitive details. Do not paste raw evidence, source URLs, personal data, stakeholder case material, or confidential legal analysis here.

## Current Status

| Date | Scope | Status | Notes |
|---|---|---|---|
| 2026-04-23 | Synthetic examples for templates, calibration, and tooling dry runs | `approved_synthetic_only` | No real Threads evidence, no personal data, no live URLs, no raw screenshots. |
| 2026-04-23 | Real 50-item Threads pilot | `approved_with_limits` | Launch packet recorded; exact source, storage, access, retention, and redaction limits must be completed in controlled record before collection. |
| 2026-04-23 | CIB-authorized API and automation for Threads pilot | `approved_with_limits` | Explicitly authorized in controlled launch record; every run needs source, fields, item limit, credential handling, raw output path, redaction status, and audit log. |
| 2026-04-23 | Immediate 500-item real collection without limitations | `rejected_or_paused` | Unlimited collection is not a valid authorization state. Use `docs/32-500-item-expansion-plan.md`. |
| 2026-04-23 | Low-speed automated Threads/Meta collection without legal/platform/stakeholder scope | `rejected_or_paused` | Low-speed automation is still automation. It is not accepted without recorded authorization, platform access conditions, approved scope, field limits, storage, access, retention, and redaction rules. |

## Authorization Levels

| Status | Meaning |
|---|---|
| `approved_synthetic_only` | Safe synthetic/redacted examples only. |
| `pending` | Proposed source or method is not yet approved. |
| `approved_manual` | Manual or stakeholder-provided evidence approved with limits. |
| `approved_with_limits` | Approved only for specified fields, source, storage, or sharing constraints. |
| `rejected_or_paused` | Do not collect or use. |

## Request Register

| Request ID | Date | Source type | Collection method | Approved fields summary | Raw storage | Retention | Status | Decision owner | Notes |
|---|---|---|---|---|---|---|---|---|---|
| SYNTH-2026-04-23 | 2026-04-23 | researcher_synthetic | synthetic | synthetic sample fields only | git-safe samples only; generated outputs ignored | keep as non-evidence templates | `approved_synthetic_only` | project owner | Used for dry-run QA. |
| AUTH-THREADS-PILOT-V1-2026-04-23 | 2026-04-23 | stakeholder/manual public source category | originally manual; amended by CIB controlled record | post text, selected replies, OCR excerpts, redacted screenshot references, normalized/redacted links, redacted handles, visible redirects, metadata notes | controlled location outside git; exact path outside repo | pilot-only; review after decision memo | `approved_with_limits` | project owner | `go_with_limits`; amended by `CTRL-THREADS-PILOT-V1-CIB-2026-04-23` for API and automation. |
| CTRL-THREADS-PILOT-V1-CIB-2026-04-23 | 2026-04-23 | CIB-authorized Threads research sources | manual, stakeholder-provided, API-authorized, and automation-assisted | post text, replies, OCR, screenshots, links, redirect/landing evidence, handles/contact categories, API metadata, automation logs, and redacted derived fields under run records | CIB-controlled raw, credential, session, and automation-log locations outside git | pilot-only; raw and automation artifacts reviewed by 2026-06-30 unless archived by CIB | `approved_with_limits` | CIB stakeholder / project owner | Explicit CIB authorization for API and all research-required automation; see controlled launch record and Decision 0018. |
| EVIDENCE-SCOPE-THREADS-PILOT-V1-0014 | 2026-04-25 | pending stakeholder evidence-scope decision | pending | pending choice among redacted stakeholder exemplars, risk-relevant OCR excerpts, narrow adjacent reply context, visible-link domain/category, redirect/landing evidence, or no expansion | controlled location outside git if approved; exact path outside repo | pending stakeholder decision | `pending` | stakeholder / project owner | Required by Decision 0030 before any item 0017 retry, item 0018 attempt, or high-risk evidence-expansion run. |
| EXPAND-500-UNLIMITED-2026-04-23 | 2026-04-23 | unspecified | unspecified/unlimited | "all fields" requested, not accepted | unspecified | unspecified | `rejected_or_paused` | project owner | Replaced with staged expansion plan and work order. |
| AUTO-LOW-SPEED-NO-SCOPE-2026-04-23 | 2026-04-23 | Threads/Meta public surfaces | low-speed automated collection | not approved | unspecified | unspecified | `rejected_or_paused` | project owner | Request to accept low-speed automation without legal/platform/stakeholder scope was not adopted; see `decision-log/0016-reject-low-speed-automation-without-scope.md`. |

## Decision Summary Template

When a real source is approved, add a row above and summarize:

- approved source type
- allowed collection method
- approved fields
- raw storage location category
- access list category
- retention rule
- screenshot policy
- URL/link policy
- publication/demo limits
- stakeholder authorization decision ID
- readiness review decision
- decision owner and date

Do not include sensitive source details in this register. Put sensitive approvals in the controlled location named by the project owner, then reference only the approval ID here.
