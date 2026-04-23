# Pilot Checkpoint Review

Use this template after the first 10-15 real pilot items are collected or annotated. Keep this file free of raw Threads content, screenshots, URLs, handles, case IDs, credentials, browser exports, and sensitive investigative details.

## Checkpoint Identity

| Field | Value |
|---|---|
| Checkpoint ID |  |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Collection batch ID | `threads_pilot_v1_2026-05` |
| Checkpoint type | collection / annotation / combined |
| Review date |  |
| Reviewed item count |  |
| Review owner |  |
| Governance reviewer |  |
| Annotation lead |  |
| Controlled launch details confirmed? | yes / no |

## Collection Composition

| Bucket | Count | Notes |
|---|---:|---|
| likely scam or high-risk scam-like |  |  |
| likely non-scam comparator |  |  |
| uncertain or ambiguous |  |  |
| insufficient-evidence or low-context |  |  |
| excluded before annotation |  |  |

## Content-Form Mix

| Content form | Count | Notes |
|---|---:|---|
| text-only |  |  |
| text plus image |  |  |
| screenshot-style item |  |  |
| OCR-relevant item |  |  |
| reply/comment context |  |  |
| visible link or redirection signal |  |  |

## Collection And Redaction QA

| Check | Status | Notes |
|---|---|---|
| Raw evidence stayed outside git |  |  |
| Controlled source limits followed |  |  |
| Controlled storage limits followed |  |  |
| Controlled access limits followed |  |  |
| Controlled retention limits followed |  |  |
| Controlled redaction limits followed |  |  |
| No automation, crawling, or bulk export used |  |  |
| Screenshot status filled where needed |  |  |
| Link status filled where needed |  |  |
| OCR text privacy-reviewed where present |  |  |
| Contact handles redacted or categorized |  |  |
| Source URLs omitted, normalized, or redacted |  |  |
| Exclusion reasons recorded |  |  |

## Review Dimensions

| Dimension | Rating | Evidence or issue summary |
|---|---|---|
| Governance compliance | green / yellow / red |  |
| Redaction quality | green / yellow / red |  |
| Collection burden | green / yellow / red |  |
| Annotation consistency | green / yellow / red / not_available |  |
| Evidence sufficiency | green / yellow / red |  |
| OCR quality | green / yellow / red / not_applicable |  |
| Reply/comment usefulness | green / yellow / red / not_applicable |  |
| Visible link/handle handling | green / yellow / red / not_applicable |  |
| Unapproved context pressure | none / limited / blocking |  |

## Annotation QA

Complete if first-pass labels exist.

| Check | Status | Notes |
|---|---|---|
| No blank primary labels |  |  |
| No blank evidence sufficiency values |  |  |
| No blank annotation confidence values |  |  |
| `signal_tags` uses `none` when no signal applies |  |  |
| High-risk `scam` items routed to second review |  |  |
| `uncertain` items routed to second review |  |  |
| Low-confidence items routed to second review |  |  |
| Notes are evidence-based |  |  |
| Notes avoid legal conclusions |  |  |
| Notes avoid raw personal data |  |  |

## Early Label Distribution

Complete if labels exist.

| Label | Count | Notes |
|---|---:|---|
| `scam` |  |  |
| `non_scam` |  |  |
| `uncertain` |  |  |
| `insufficient_evidence` |  |  |

## Warning Thresholds

| Warning | Observed? | Follow-up |
|---|---|---|
| `uncertain` above 40 percent |  |  |
| `insufficient_evidence` above 30 percent |  |  |
| repeated missing required fields |  |  |
| any raw identifiers in notes |  |  |
| screenshots or links hard to redact |  |  |
| annotators need unapproved context |  |  |
| source skew already severe |  |  |
| same label disagreement repeated |  |  |
| schema field confusion or burden |  |  |
| checkpoint item needed unapproved context |  |  |

## Decision

Choose one:

- `continue_to_50`
- `continue_with_limits`
- `pause_for_redaction_fix`
- `pause_for_collection_fix`
- `pause_for_guideline_fix`
- `pause_for_authorization_review`
- `stop_pilot`

Decision:

```text

```

## Decision Evidence

| Decision option | Evidence supporting or rejecting this option |
|---|---|
| continue |  |
| continue with limits |  |
| pause |  |
| revise guideline first |  |
| revise schema first |  |
| narrow sources |  |

## Limits If Continuing

Complete if the decision is `continue_with_limits`.

| Limit type | Required limit before item 16 |
|---|---|
| Source/source category |  |
| Permitted fields |  |
| Redaction |  |
| Screenshot/OCR |  |
| URL/link/handle handling |  |
| Review routing |  |

## Required Follow-Up

| Follow-up | Owner | Due date | Required before continuing? |
|---|---|---|---|
|  |  |  | yes / no |

## Decision Rationale

Summarize the reason for the checkpoint decision in 3-6 bullets.

- 
