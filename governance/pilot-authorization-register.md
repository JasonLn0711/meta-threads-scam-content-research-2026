# Pilot Authorization Register

## Purpose

Use this register to track whether a source, collection method, and field set are approved for the Threads pilot.

This file is a governance index, not a place for sensitive details. Do not paste raw evidence, source URLs, personal data, stakeholder case material, or confidential legal analysis here.

## Current Status

| Date | Scope | Status | Notes |
|---|---|---|---|
| 2026-04-23 | Synthetic examples for templates, calibration, and tooling dry runs | `approved_synthetic_only` | No real Threads evidence, no personal data, no live URLs, no raw screenshots. |
| 2026-04-23 | Real 50-item Threads pilot | `approved_with_limits` | Launch packet recorded; exact source, storage, access, retention, and redaction limits must be completed in controlled record before collection. |
| 2026-04-23 | Immediate 500-item real collection without limitations | `rejected_or_paused` | Unlimited collection is not a valid authorization state. Use `docs/32-500-item-expansion-plan.md`. |

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
| AUTH-THREADS-PILOT-V1-2026-04-23 | 2026-04-23 | stakeholder/manual public source category | manual only | post text, selected replies, OCR excerpts, redacted screenshot references, normalized/redacted links, redacted handles, visible redirects, metadata notes | controlled location outside git; exact path outside repo | pilot-only; review after decision memo | `approved_with_limits` | project owner | `go_with_limits`; exact source/storage/access/retention/redaction launch record required before first item. |
| EXPAND-500-UNLIMITED-2026-04-23 | 2026-04-23 | unspecified | unspecified/unlimited | "all fields" requested, not accepted | unspecified | unspecified | `rejected_or_paused` | project owner | Replaced with staged expansion plan and work order. |

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
