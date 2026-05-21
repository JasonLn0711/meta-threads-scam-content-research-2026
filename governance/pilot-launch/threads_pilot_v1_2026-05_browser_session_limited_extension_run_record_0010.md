# Browser-Session Limited Extension Run Record 0010

This is the non-sensitive tracked run record for the next approved browser storage-state/session-aware limited extension after item 0016 second review.

Do not add raw Threads content, screenshots, full item URLs, raw handles, credentials, cookies, tokens, browser profiles, HAR files, full API responses, exact raw storage paths, access-list details, or sensitive investigative notes to this file. Exact sensitive values remain in the CIB-controlled store or local ignored working files.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `CRAWL-THREADS-PILOT-V1-0010` |
| Date opened | `2026-04-25` |
| Operator ID | `AUTO-OP-01` |
| Project owner | `PROJECT-OWNER-01` |
| Governance reviewer | `GOV-REVIEWER-01` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Collection batch ID | `threads_pilot_v1_2026-05` |
| Controlled launch record | `CTRL-THREADS-PILOT-V1-CIB-2026-04-23` |
| Prior run | `CRAWL-THREADS-PILOT-V1-0009` |
| Prior decision | `open_limited_browser_session_extension_0010_with_negation_filter` |
| Purpose | attempt a limited item 0017-0020 extension through the approved browser storage-state path |
| Current gate | `method_review_required_before_any_further_item_0017_attempt` |
| Run status | `completed_no_selected_item_from_all_five_seeds` |

## Required Pre-Run Gate

| Check | Status | Notes |
|---|---|---|
| Run 0009 completed | complete | Item 0016 built and strict-validated locally. |
| Item 0016 second review | complete | Final local label changed to `non_scam` / `low`. |
| False-positive lesson applied | required | Candidate screening must exclude negated guaranteed-profit or risk-warning statements before selection. |
| Browser storage-state artifact | required | Must exist in controlled storage and pass readiness check before execution. |
| Existing 16-record checkpoint strict-valid | required | Validate the local 16-record aggregate before attempting item 0017. |

## Authorized Acquisition Path

| Check | Status | Notes |
|---|---|---|
| CIB authorization applies to this run | complete | Approved under Decision 0018 and the controlled launch record. |
| Source category is approved | complete | CIB-authorized Threads scam/scam-like content research examples. |
| Acquisition path | approved | Browser-rendered retrieval using approved Playwright Chromium storage-state artifact in controlled storage. |
| API retrieval | not_used | Browser storage-state path only unless a later run record changes this. |
| Query terms as labels | forbidden | Query terms are candidate-generation probes only. |

## Candidate Screening Update

Before any item is selected, reject candidates where the only apparent risk signal is a negated or warning-style statement such as:

- no guarantee, no risk-free claim, or risk-loss warning
- cautionary advice against guaranteed-profit promises
- educational or skeptical discussion without wallet, deposit, contact, urgency, or private-channel action

This filter is a candidate-screening rule only. It does not create a positive scam label and does not replace annotation review.

## Candidate Probe Plan

Use at most one risk-probe seed at a time. For each selected seed, stop after the first selectable real candidate or after reviewing 5 visible candidates. Stop the entire run after item `threads_pilot_v1_0020` or earlier if a stop condition triggers.

| Probe ID | Risk domain | Visible signal family | Query seed | Max candidates reviewed |
|---|---|---|---|---:|
| RP-0010-01 | investment | private-channel migration plus outcome claim | `投資穩賺LINE` | 5 |
| RP-0010-02 | stocks/investment | teacher/group/testimonial pressure | `股票老師帶單群` | 5 |
| RP-0010-03 | crypto | wallet/deposit/reward action | `加密貨幣空投錢包` | 5 |
| RP-0010-04 | crypto/trading | deposit or urgent action | `虛擬貨幣入金限時` | 5 |
| RP-0010-05 | side income/recruitment | private-channel migration | `副業月入私訊LINE` | 5 |

## Run Limits

| Limit | Value |
|---|---|
| Collection attempt allowed in this run | yes; limited extension only |
| Target selected item count | up to 4 |
| Target local item IDs | `threads_pilot_v1_0017` through `threads_pilot_v1_0020` |
| Candidate review cap | 5 candidates per selected probe seed |
| Runtime cap | 45 minutes |
| Parallel workers | 1 |
| Minimum delay between page/object fetches | 30 seconds |
| Burst behavior | none |
| Browser rendering allowed? | yes |
| Approved API retrieval allowed? | no |
| Landing-page capture allowed? | no |
| Profile/account context review allowed? | no beyond loaded session state needed for access |
| Broad reply/comment capture allowed? | no |
| Screenshot capture allowed? | raw outside git only if needed for audit; no screenshot path in git |
| OCR allowed? | no for this run |

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

- login challenge, captcha, account warning, 403/429, or platform warning appears
- the run requires credential values, cookies, tokens, browser profiles, HAR files, or raw session details to enter git
- raw evidence would enter git
- more than 5 candidates must be reviewed for any selected probe seed
- the run starts collecting beyond item 0020
- unrelated personal data is captured and cannot be redacted safely
- profile graph, follower/following, broad account history, or broad comment capture becomes necessary
- external landing-page or redirect-chain capture becomes necessary
- an item needs screenshots, OCR, replies, or image evidence to be reviewable
- selected output cannot be reduced to approved redacted local JSON fields

## Success Sequence

For each selected item:

1. Confirm approved browser storage-state readiness.
2. Review at most 5 candidates for the selected probe seed.
3. Apply the negation/risk-warning exclusion before selection.
4. Fill the next local-only `manual_entry_####.json` with approved minimized fields.
5. Build the matching local `manual_record_####.json`.
6. Strict-validate the local record and aggregate.
7. Stop after item `threads_pilot_v1_0020` or earlier if no safe selectable candidate exists.

## Run Result

| Result field | Value |
|---|---|
| Run started? | yes |
| Run completed? | yes; all five planned seeds attempted |
| Candidates reviewed | 25 total; 5 each for `RP-0010-01` through `RP-0010-05` |
| Selected items | 0 |
| Stop condition triggered? | no |
| Local records built? | no |
| Strict validation result | not_applicable; no item built |
| Decision after run | `pause_for_method_review_before_more_item_0017_attempts` |

## Next Action

The first item 0017 attempt used `RP-0010-01`, reviewed 5 candidates, applied the negation/risk-warning exclusion, and selected no item. The second item 0017 attempt used `RP-0010-02`, reviewed 5 candidates, applied the same exclusion, and selected no item. The third item 0017 attempt used `RP-0010-03`, reviewed 5 candidates, applied the same exclusion, and selected no item. The fourth item 0017 attempt used `RP-0010-04`, reviewed 5 candidates, applied the same exclusion, and selected no item. The fifth item 0017 attempt used `RP-0010-05`, reviewed 5 candidates, applied the same exclusion, and selected no item. No `manual_entry_0017.json` was created.

Do not advance to item 0018. Do not run another item 0017 seed until a method review records why the approved browser-session risk-probe matrix produced no safe selectable item and whether the next attempt should change seed design, candidate extraction, evidence requirements, or acquisition path.
