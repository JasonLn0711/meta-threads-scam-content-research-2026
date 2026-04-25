# Evidence-Path Design Run Record 0012

This is the non-sensitive tracked run record for the scoped evidence-path design step required after run 0011 produced no accepted item 0017 under text-only visible search-result methods.

Do not add raw Threads content, screenshots, full item URLs, raw handles, credentials, cookies, tokens, browser profiles, HAR files, full API responses, exact raw storage paths, access-list details, or sensitive investigative notes to this file. Exact sensitive values remain in the CIB-controlled store or local ignored working files.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `CRAWL-THREADS-PILOT-V1-0012` |
| Date opened | `2026-04-25` |
| Operator ID | `AUTO-OP-01` |
| Project owner | `PROJECT-OWNER-01` |
| Governance reviewer | `GOV-REVIEWER-01` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Collection batch ID | `threads_pilot_v1_2026-05` |
| Controlled launch record | `CTRL-THREADS-PILOT-V1-CIB-2026-04-23` |
| Prior run | `CRAWL-THREADS-PILOT-V1-0011` |
| Prior decision | `open_scoped_evidence_path_design_run_0012` |
| Purpose | define scoped evidence-path field boundaries before any further item 0017 attempt |
| Current gate | `open_separate_execution_run_0013_before_collection` |
| Run status | `design_reviewed_accepted_no_collection` |

## Required Pre-Run Gate

| Check | Status | Notes |
|---|---|---|
| Decision 0028 recorded | complete | Scoped evidence-path study selected. |
| Run 0011 completed | complete | No accepted item 0017 after revised diagnostics. |
| Item 0017 status | excluded | Local trace is `insufficient_evidence` / `not_reviewable`; it does not unlock item 0018. |
| Existing local aggregate strict-valid | required | Validate the local aggregate before any future execution. |
| Approved browser storage-state artifact | required before execution | Not needed for design-only drafting, but required before any future browser execution. |

## Design Scope

Run 0012 is a design run. It does not authorize collection, item creation, screenshots/OCR, landing-page capture, profile review, broad comment capture, or full redirect-chain crawling.

The design defines two possible evidence additions for a later run:

1. domain-only visible-link or redirect-category evidence, and
2. narrow reply-context feasibility review.

## Field Boundary: Domain-Only Visible-Link Or Redirect Category

| Field | Allowed in later scoped run? | Boundary |
|---|---|---|
| Full URL | no | Do not store full URL in git. |
| Domain-only external link | yes, if visible in selected candidate text | Store only normalized domain category or redacted domain-only reference. |
| Redirect category | yes, if visible without opening landing page | Store category such as `private_chat`, `wallet`, `exchange`, `unknown`, or `none`. |
| Redirect-chain crawling | no | Do not follow redirect chains. |
| Landing-page capture | no | Do not open or store landing pages. |
| Tracking parameters | no | Strip and do not store. |
| Raw link evidence | controlled store only if needed | No repo-visible raw URL. |

## Field Boundary: Narrow Reply-Context Feasibility

| Field | Allowed in later scoped run? | Boundary |
|---|---|---|
| Broad replies/comments | no | Do not capture thread-wide discussion. |
| Narrow adjacent reply context | feasibility only | At most the minimum visible adjacent context needed to decide whether the candidate is query/interface text or independent content. |
| Reply author identity | no | Do not store handles or account identifiers in git. |
| Reply text in git | no by default | Repo-visible output should be aggregate or redacted summary unless a later run explicitly allows minimized reply text. |
| Reply count metrics | yes | Aggregate counts only. |
| Personal data in replies | stop condition | Stop if unrelated personal data cannot be safely excluded. |

## Explicitly Out Of Scope

- item 0018
- screenshots/OCR
- landing-page capture
- full redirect-chain crawling
- broad profile review
- follower/following graph review
- broad comments/replies
- full raw URL retention in git
- raw candidate text in git
- cookies, tokens, browser profiles, HAR files, or raw API responses in git
- production scoring, public accusation, or legal fraud determination

## Candidate Reviewability Test For Later Run

A later execution run may consider a candidate reviewable only if all are true:

- it is not an exact-query or near-query echo;
- it is not interface/search/onboarding text;
- it has independent visible candidate content;
- any link evidence can be reduced to domain-only or redirect-category form;
- any reply-context check is narrow and does not require broad comment capture;
- no screenshot/OCR, landing page, profile graph, or raw identifier retention is required.

## Stop Conditions For Later Run

Stop immediately if:

- login challenge, captcha, account warning, 403/429, or platform warning appears;
- reviewability requires screenshots/OCR, landing pages, broad profile review, broad comments, or redirect-chain crawling;
- full URLs, handles, raw reply text, raw candidate text, or unrelated personal data would need to enter git;
- more than 5 candidates must be reviewed for one seed;
- the run attempts item 0018;
- selected output cannot be reduced to approved redacted local JSON fields.

## Run Result

| Result field | Value |
|---|---|
| Run started? | no; design only |
| Run completed? | yes; design reviewed |
| Collection performed? | no |
| Candidate reviewed? | no |
| Selected items | 0 |
| Local records built? | no |
| Strict validation result | local aggregate remains strict-valid |
| Decision after design | `open_run_0013_scoped_execution_record_only` |

## Next Action

Open a separate execution run record for at most one item 0017 attempt under these boundaries. Do not execute collection directly from this design record.
