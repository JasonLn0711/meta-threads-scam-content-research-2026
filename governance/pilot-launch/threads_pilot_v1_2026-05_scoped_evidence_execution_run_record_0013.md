# Scoped Evidence Execution Run Record 0013

This is the non-sensitive tracked execution run record for a future item 0017 attempt under the run 0012 evidence-path boundaries.

Do not add raw Threads content, screenshots, full item URLs, raw handles, credentials, cookies, tokens, browser profiles, HAR files, full API responses, exact raw storage paths, access-list details, or sensitive investigative notes to this file. Exact sensitive values remain in the CIB-controlled store or local ignored working files.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `CRAWL-THREADS-PILOT-V1-0013` |
| Date opened | `2026-04-25` |
| Operator ID | `AUTO-OP-01` |
| Project owner | `PROJECT-OWNER-01` |
| Governance reviewer | `GOV-REVIEWER-01` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Collection batch ID | `threads_pilot_v1_2026-05` |
| Controlled launch record | `CTRL-THREADS-PILOT-V1-CIB-2026-04-23` |
| Prior run | `CRAWL-THREADS-PILOT-V1-0012` |
| Prior decision | `open_run_0013_scoped_execution_record_only` |
| Purpose | attempt at most one item 0017 candidate under scoped evidence-path boundaries |
| Current gate | `method_review_required_after_no_reviewable_scoped_candidate` |
| Run status | `completed_no_reviewable_candidate` |

## Required Pre-Execution Gate

| Check | Status | Notes |
|---|---|---|
| Run 0012 design accepted | complete | Field boundaries are defined. |
| Existing aggregate strict-valid | required | Validate latest local aggregate before execution. |
| Approved browser storage-state artifact | required | Must pass readiness check before execution. |
| Item 0017 status | excluded trace only | Existing trace does not count as accepted item. |
| Item 0018 | blocked | Do not attempt item 0018. |

## Acquisition Path

| Check | Status | Notes |
|---|---|---|
| Browser-rendered session path | approved for this scoped run if readiness passes | Use approved Playwright Chromium storage-state in controlled storage. |
| API path | not_used | This run uses browser-rendered session path only. |
| Query terms as labels | forbidden | Query terms are retrieval hints only. |
| Query echo filter | required | Reject exact-query and near-query echoes before reviewability. |

## Scoped Evidence Allowlist

| Evidence type | Allowed? | Boundary |
|---|---|---|
| Independent visible candidate text | yes | Minimized local-only text only if item 0017 is selected. |
| Domain-only visible-link evidence | yes | Domain category or redacted domain-only reference only; no full URL in git. |
| Redirect category | yes | Category only if visible without landing-page or redirect-chain capture. |
| Narrow adjacent reply context | feasibility only | Aggregate/redacted summary only; no broad replies/comments and no handles in git. |
| Reply count metric | yes | Aggregate count only. |
| Screenshots/OCR | no | Stop if needed. |
| Landing page | no | Stop if needed. |
| Full redirect chain | no | Stop if needed. |
| Profile/account graph | no | Stop if needed. |
| Broad comments/replies | no | Stop if needed. |
| Full raw URL | no in git | Controlled store only if unavoidable for audit. |

## Candidate Reviewability Rule

A candidate may pass reviewability only if all are true:

- not an exact-query or near-query echo;
- not interface/search/onboarding text;
- independent visible candidate content exists;
- any link evidence can be reduced to domain-only or redirect-category form;
- any reply-context check is narrow and does not require broad comment capture;
- no screenshots/OCR, landing page, profile graph, redirect chain, or raw identifier retention is required;
- candidate can be reduced to approved redacted local JSON fields.

## Run Limits

| Limit | Value |
|---|---|
| Target selected item count | at most 1 |
| Target local item ID | `threads_pilot_v1_0017` |
| Candidate review cap | 5 candidates total for the selected seed |
| Runtime cap | 30 minutes |
| Parallel workers | 1 |
| Minimum delay between page/object fetches | 30 seconds |
| Burst behavior | none |
| Item 0018 allowed? | no |

## Stop Conditions

Stop immediately if:

- login challenge, captcha, account warning, 403/429, or platform warning appears;
- more than 5 candidates must be reviewed;
- query/interface text is the only retained candidate content;
- reviewability requires screenshots/OCR, landing pages, full redirect chains, broad profile review, or broad comments;
- full URLs, handles, raw reply text, raw candidate text, or unrelated personal data would need to enter git;
- selected output cannot be reduced to approved redacted local JSON fields.

## Candidate Seed

Use one seed only for the first execution attempt.

| Probe ID | Purpose | Query seed | Max candidates reviewed |
|---|---|---|---:|
| RP-0013-01 | test domain-only link/redirect-category plus narrow reply-context feasibility | `加密貨幣錢包私訊LINE` | 5 |

## Run Result

| Result field | Value |
|---|---|
| Run started? | yes |
| Run completed? | yes |
| Candidates reviewed | 4 after query-echo filter |
| Query echoes excluded | 1 |
| Domain-only evidence | `external_domain`: 15 |
| Redirect-category evidence | `unknown`: 15 |
| Signal-family metadata | `wallet_or_deposit`: 2 |
| Narrow reply-context feasible count | 0 |
| Reviewable candidates | 0 |
| Selected items | 0 |
| Local records built? | no |
| Strict validation result | not_applicable; no item built |
| Decision after run | `pause_for_method_review_after_scoped_evidence_no_reviewable_candidate` |

## Next Action

Run 0013 found domain-only external-link evidence in aggregate form, but no reviewable candidate under the scoped field allowlist. Redirect categories were `unknown`, no narrow reply-context feasibility was available, and no local item was built.

Do not attempt item 0018. The next action is method review: decide whether to stop item 0017 extension, refine domain/redirect classification without opening landing pages, or request a separately scoped evidence expansion.
