# Browser-Session Execution Run Record 0009

This is the non-sensitive tracked run record for the first approved browser storage-state/session-aware execution attempt after run 0008 prepared and validated the browser storage-state path.

Do not add raw Threads content, screenshots, full item URLs, raw handles, credentials, cookies, tokens, browser profiles, HAR files, full API responses, exact raw storage paths, access-list details, or sensitive investigative notes to this file. Exact sensitive values remain in the CIB-controlled store or local ignored working files.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `CRAWL-THREADS-PILOT-V1-0009` |
| Date opened | `2026-04-25` |
| Operator ID | `AUTO-OP-01` |
| Project owner | `PROJECT-OWNER-01` |
| Governance reviewer | `GOV-REVIEWER-01` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Collection batch ID | `threads_pilot_v1_2026-05` |
| Controlled launch record | `CTRL-THREADS-PILOT-V1-CIB-2026-04-23` |
| Prior run | `CRAWL-THREADS-PILOT-V1-0008` |
| Purpose | attempt exactly one item-0016 candidate through the approved browser storage-state path |
| Current gate | `ready_for_single_item_browser_session_execution` |
| Run status | `opened_not_yet_executed` |

## Required Pre-Run Gate

| Check | Status | Notes |
|---|---|---|
| Run 0008 completed | complete | Browser storage-state path prepared. |
| Browser storage-state artifact | complete | Exists in controlled storage and passes shape validation. |
| Approved account reference | complete | `APPROVED_BROWSER_ACCOUNT_0001`; raw account details remain in controlled store only. |
| Item 0016 still absent | complete | No `manual_entry_0016.json` or `manual_record_0016.json` exists. |
| Existing 15-record checkpoint strict-valid | complete | Existing local aggregate remains strict-valid. |

## Authorized Acquisition Path

| Check | Status | Notes |
|---|---|---|
| CIB authorization applies to this run | complete | Approved under Decision 0018 and the controlled launch record. |
| Source category is approved | complete | CIB-authorized Threads scam/scam-like content research examples. |
| Acquisition path | approved | Browser-rendered retrieval using approved Playwright Chromium storage-state artifact in controlled storage. |
| API retrieval | not_used | Browser storage-state path only for this run. |
| Query terms as labels | forbidden | Query terms are candidate-generation probes only. |

## Candidate Probe Plan

Use at most one risk-probe seed at a time. Stop after the first selectable real candidate or after reviewing 5 visible candidates for the selected seed.

| Probe ID | Risk domain | Visible signal family | Query seed | Max candidates reviewed |
|---|---|---|---|---:|
| RP-0009-01 | investment | guaranteed outcome | `投資保證獲利` | 5 |
| RP-0009-02 | stocks/investment | private-channel migration | `股票LINE投資群` | 5 |
| RP-0009-03 | crypto | wallet/deposit/reward action | `加密貨幣空投錢包` | 5 |
| RP-0009-04 | crypto/trading | urgency or deposit action | `比特幣入金限時` | 5 |
| RP-0009-05 | side income/recruitment | easy-income/private-channel/testimonial pressure | `副業月入私訊` | 5 |

## Run Limits

| Limit | Value |
|---|---|
| Collection attempt allowed in this run | yes; exactly one selected item at most |
| Target selected item count | 1 |
| Target local item ID | `threads_pilot_v1_0016` |
| Runtime cap | 30 minutes |
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
- more than 5 candidates must be reviewed for the selected probe seed
- the run starts collecting beyond item 0016
- unrelated personal data is captured and cannot be redacted safely
- profile graph, follower/following, broad account history, or broad comment capture becomes necessary
- external landing-page or redirect-chain capture becomes necessary
- an item needs screenshots, OCR, replies, or image evidence to be reviewable
- selected output cannot be reduced to approved redacted local JSON fields

## Execution Command Shape

The execution worker must use the approved storage-state artifact from controlled storage and must not copy the artifact into git.

If an item is selected, build only the redacted local `data/interim/manual_entry_0016.json`, then:

```bash
python scripts/build_manual_collection_record.py data/interim/manual_entry_0016.json \
  --ack-controlled-details \
  --output data/interim/manual_record_0016.json \
  --collection-log data/interim/threads_pilot_v1_collection_log.csv

python scripts/validate_thread_dataset.py data/interim/manual_record_0016.json --strict
```

## Run Result

| Result field | Value |
|---|---|
| Run started? | no |
| Run completed? | no |
| Candidates reviewed | 0 |
| Extractable candidates reviewed | 0 |
| Selected items | 0 |
| Stop condition triggered? | not_applicable_not_executed |
| Local records built? | no; no `manual_entry_0016.json` was created |
| Strict validation result | not_applicable_not_executed |
| Decision after run | `execute_single_item_browser_session_attempt_before_item_16` |

## Decision

Run 0009 is opened and ready for a single item-0016 browser-session execution attempt.

Do not treat storage-state readiness as permission to expand the batch. This run is only for one selected item, with at most 5 candidates reviewed for the selected probe seed.
