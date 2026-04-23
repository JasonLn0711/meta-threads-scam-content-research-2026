# Data Authorization Request: Threads Pilot v1

## Request Identity

- Request ID: `DREQ-THREADS-PILOT-V1-2026-04-23`
- Date: `2026-04-23`
- Request owner: project owner
- Dataset or batch ID: `threads_pilot_v1_2026-05`
- Source owner or stakeholder: stakeholder owner, exact identity held outside git if sensitive

## Proposed Source

- Source type: `stakeholder_provided` / `manual_public`
- Platform: Threads
- Proposed collection method: manual only
- Proposed sample size: 50
- Proposed date range: after readiness sign-off through `2026-05-31`, unless stakeholder limits specify otherwise
- Expected content forms: text, text plus image, selected replies/comments, OCR text, visible links, redacted handles, visible platform redirects, screenshot-style posts where approved

## Purpose

- Research question: Can a small, governed Threads pilot support consistent scam-content annotation and simple baseline comparison?
- Intended use: first-round collection, annotation, audit, and baseline comparison
- Expected experiment or annotation activity: 50-item pilot annotation, QA, adjudication, dataset audit, rule-baseline comparison
- Why this source is necessary: synthetic records validated the workflow but cannot test real ambiguity, redaction burden, OCR quality, source skew, or baseline behavior

## Fields Requested

| Field | Status | Notes |
|---|---|---|
| `post_text` | approved | Redact unnecessary personal data. |
| `reply_texts` | approved | Selected relevant replies/comments only. |
| `image_paths` / screenshot reference | approved_with_limits | Redacted local reference only; no raw screenshots in git. |
| `ocr_text` | approved_with_limits | Risk-relevant OCR text after privacy review. |
| `external_links` | approved_with_limits | Normalized or redacted visible-link references; no crawling. |
| `visible_contact_handles` | approved_with_limits | Category or redacted handle only. |
| `visible_platform_redirects` | approved | Platform/category labels allowed. |
| `source_url_if_stored` | approved_with_limits | Redacted reference only in repo-visible files. |
| screenshot snapshot | approved_with_limits | Redacted snapshot outside git only. |
| link snapshot | denied | Do not crawl, expand, visit, or snapshot destinations. |
| limited metadata notes | approved | Non-sensitive notes only. |

## Privacy And Redaction

- Personal data expected: possible handles, names, screenshots, visible comments, URLs, and OCR text.
- Redaction required: yes, before annotation and before any sharing.
- Raw storage location: controlled location outside git; exact location intentionally not recorded here.
- Who may access raw evidence: project owner, governance reviewer, collector, assigned reviewers only.
- What may be committed to git: aggregate non-sensitive docs, empty templates, synthetic examples, and non-sensitive launch records only.
- What must never be committed: raw screenshots, raw personal data, full sensitive URLs, credentials, browser profiles, stakeholder case packets, or investigative details.
- Controlled launch details required before first item: exact source, exact raw storage location, exact access list, retention/deletion rule, and redaction limits.

## Retention And Sharing

- Retention period: pilot-only retention; review after pilot decision memo.
- Deletion rule: raw evidence deletion or archival decision must be recorded after pilot result summary.
- Publication/demo restrictions: no external examples or raw evidence without later approval.
- Can aggregate metrics be shared: internal aggregate metrics allowed.
- Can redacted examples be shown: internal only after review.
- Can synthetic derivatives be created: yes, if clearly marked non-evidence.

## Platform And Legal Review

- Platform terms reviewed: must be confirmed by governance reviewer before first item.
- Legal/policy reviewer: governance reviewer role.
- Known restrictions: no automation, scraping, crawling, redirect expansion, landing-page capture, or profile/account review.
- Open concerns: exact raw storage path and access list must remain outside git and be confirmed before first item.

## Decision

- Decision: `approved_with_limits`
- Approved fields: post text, selected replies, risk-relevant OCR, normalized/redacted visible links, redacted contact handles, visible platform redirects, limited metadata, redacted screenshot references
- Disallowed fields: raw screenshots in git, full sensitive URLs in repo-visible files, link snapshots, landing-page captures, account/profile graph data
- Approved collection window: after readiness sign-off through `2026-05-31`, unless stakeholder limits specify otherwise
- Approved sample size: 50
- Required follow-up: confirm exact raw storage and access list outside git before first item
- Required controlled launch record: exact source, storage, access, retention, and redaction limits
- Decision owner: project owner / stakeholder owner
- Decision date: `2026-04-23`

## Link To Governance

Final decision recorded in `threads_pilot_v1_2026-05_authorization_decision.md` and summarized in `governance/pilot-authorization-register.md`.
