# Risk-Probe Browser Run Record 0006

This is the non-sensitive tracked run record for a narrowed no-space risk-probe retry after run 0005 returned only query echoes and generic user-interface text.

Do not add raw Threads content, screenshots, full item URLs, raw handles, credentials, cookies, tokens, browser profiles, HAR files, exact raw storage paths, access-list details, or sensitive investigative notes to this file. Exact sensitive values remain in the CIB-controlled store or local ignored working files.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `CRAWL-THREADS-PILOT-V1-0006` |
| Date opened | `2026-04-24` |
| Operator ID | `AUTO-OP-01` |
| Project owner | `PROJECT-OWNER-01` |
| Governance reviewer | `GOV-REVIEWER-01` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Collection batch ID | `threads_pilot_v1_2026-05` |
| Controlled launch record | `CTRL-THREADS-PILOT-V1-CIB-2026-04-23` |
| Prior run | `CRAWL-THREADS-PILOT-V1-0005` |
| Purpose | test normalized no-space risk-probe phrases before item 16 |
| Current gate | `approved_session_or_api_access_review_required_before_item_16` |
| Run status | `completed_no_extractable_item` |

## Required Pre-Run Gate

| Check | Status | Notes |
|---|---|---|
| Run 0005 completed | complete | Returned no extractable item content. |
| Reason for retry | complete | Test whether no-space probe phrases reduce query-echo artifacts. |
| Raw output storage outside git | required | Use controlled/local raw store with run ID `CRAWL-THREADS-PILOT-V1-0006`; exact path outside git. |
| Redacted local output path prepared | complete | Local-only `data/interim/manual_entry_0016.json` through `manual_entry_0020.json` if selected. |

## Normalized Risk-Probe Seed Matrix

Query terms are candidate-generation probes only. They must not become labels by themselves.

| Probe ID | Risk domain | Visible signal family | Query seed | Max candidates reviewed |
|---|---|---|---|---:|
| RP-0006-01 | investment | guaranteed outcome | `投資保證獲利` | 5 |
| RP-0006-02 | stocks/investment | private-channel migration | `股票LINE投資群` | 5 |
| RP-0006-03 | crypto | wallet/deposit/reward action | `加密貨幣空投錢包` | 5 |
| RP-0006-04 | crypto/trading | urgency or deposit action | `比特幣入金限時` | 5 |
| RP-0006-05 | side income/recruitment | easy-income/private-channel/testimonial pressure | `副業月入私訊` | 5 |

## Authorized Acquisition Path

| Check | Status | Notes |
|---|---|---|
| CIB authorization applies to this run | complete | Approved under Decision 0018, Decision 0022, and the controlled launch record. |
| Source category is approved | complete | CIB-authorized Threads scam/scam-like content research examples. |
| Acquisition path | complete | Browser-rendered retrieval using a fresh isolated browser context; no stored user browser profile or user cookies loaded. |
| API retrieval | not_used | Browser-rendered path only for this retry. |
| Run does not require unapproved source/context | required | Stop if a selected item requires profile graph, landing page, redirect chain, broad comments, screenshot/OCR evidence, or raw identifier retention. |

## Run Limits

| Limit | Value |
|---|---|
| Probe seed count | 5 |
| Candidate review cap | 5 candidates per probe seed |
| Target selected item count | up to 5 |
| Target local item IDs | `threads_pilot_v1_0016` through `threads_pilot_v1_0020` if selected |
| Runtime cap | 45 minutes |
| Parallel workers | 1 |
| Minimum delay between page/object fetches | 30 seconds |
| Burst behavior | none |
| Browser rendering allowed? | yes |
| Approved API retrieval allowed? | no for this run |
| Landing-page capture allowed? | no |
| Profile/account context allowed? | no |
| Broad reply/comment capture allowed? | no |
| Screenshot capture allowed? | raw outside git only; no screenshot path in git |
| OCR allowed? | no for this run unless a later record updates the scope |

## Field Allowlist

| Field | Allowed? | Repo-visible representation |
|---|---|---|
| post text | yes | minimized visible text excerpt |
| selected replies/comments | no for this run |
| image/screenshot reference | no for this run |
| OCR text | no for this run |
| visible external links | yes if visible in selected text | domain-only or redacted reference |
| contact handles | yes if visible in selected text | category or redacted value only |
| platform redirects | yes | category only |
| source URL | yes with limits | blank or redacted reference only |
| metadata notes | yes | non-sensitive operational notes |

## Stop Conditions

Stop immediately if:

- access challenge, captcha, login block, 403/429, or platform warning appears
- the run needs stored credentials, cookies, tokens, browser profiles, HAR files, or raw session details in git
- raw evidence would enter git
- more than 5 candidates must be reviewed for any probe seed
- the run starts collecting beyond item 0020
- unrelated personal data is captured and cannot be redacted safely
- profile graph, follower/following, broad account history, or broad comment capture becomes necessary
- external landing-page or redirect-chain capture becomes necessary
- an item needs screenshots, OCR, replies, or image evidence to be reviewable
- selected output cannot be reduced to approved redacted local JSON fields

## Labeling Guardrail

Risk-probe query matches are not labels. Exact query echoes must be excluded from candidate selection.

## Run Result

| Result field | Value |
|---|---|
| Run started? | yes |
| Run completed? | yes |
| Candidates reviewed | 5 non-query lines surfaced by the page after exact query echoes were excluded |
| Extractable candidates reviewed | 0 real content candidates |
| Selected items | 0 |
| Stop condition triggered? | yes |
| Stop condition | normalized risk-probe search returned only generic onboarding/user-interface text after query echoes were excluded |
| Local records built? | no; no `manual_entry_0016.json` was created |
| Strict validation result | not_applicable_no_selected_item |
| High-risk candidate yield | 0 |
| False-positive pressure | high; the search path did not expose real candidate content |
| Redaction burden | not_tested_on_real_content |
| Second-review load | 0 |
| Decision after run | `approved_session_or_api_access_review_required_before_item_16` |

## Aggregate Probe Result

| Probe ID | Query seed | Page status | Query echo excluded? | Extractable real candidates | Selected items |
|---|---|---:|---|---:|---:|
| RP-0006-01 | `投資保證獲利` | 200 | yes | 0 | 0 |
| RP-0006-02 | `股票LINE投資群` | 200 | yes | 0 | 0 |
| RP-0006-03 | `加密貨幣空投錢包` | 200 | yes | 0 | 0 |
| RP-0006-04 | `比特幣入金限時` | 200 | yes | 0 | 0 |
| RP-0006-05 | `副業月入私訊` | 200 | yes | 0 | 0 |

## Method Finding

The normalized no-space risk-probe retry also failed to expose real item content. After exact query echoes and known interface text were excluded, the remaining visible page text was generic onboarding or user-interface copy, not item evidence.

This confirms the run-0005 finding: the current public unauthenticated browser-rendered search path is not sufficient for high-risk risk-probe candidate generation.

## Next Action

Do not create item 0016 from this run. Stop before item 16 and move to an approved browser-rendered session/access or API/session-aware access-path review under a new run record.
