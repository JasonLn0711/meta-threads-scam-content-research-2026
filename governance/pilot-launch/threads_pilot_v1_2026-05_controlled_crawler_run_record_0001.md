# Controlled Crawler Run Record 0001

This is the non-sensitive tracked run record for the first controlled low-speed crawler rehearsal.

Do not add raw Threads content, screenshots, full URLs, raw handles, case IDs, credentials, browser artifacts, automation logs, exact raw storage paths, access-list details, or sensitive investigative notes to this file. Exact sensitive values remain in the CIB-controlled store.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `CRAWL-THREADS-PILOT-V1-0001` |
| Date opened | `2026-04-24` |
| Operator ID | `AUTO-OP-01` |
| Project owner | `PROJECT-OWNER-01` |
| Governance reviewer | `GOV-REVIEWER-01` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Collection batch ID | `threads_pilot_v1_2026-05` |
| Controlled launch record | `CTRL-THREADS-PILOT-V1-CIB-2026-04-23` |
| Purpose | first one-item controlled crawler rehearsal |
| Current gate | `ready_for_controlled_item_entry` |
| Run status | `completed_no_extractable_item` |

## Access, Session, And Output Confirmation

| Check | Status | Notes |
|---|---|---|
| CIB authorization applies to this run | complete | Approved under Decision 0018 and Decision 0022. |
| Source category is approved | complete | CIB-authorized Threads scam/scam-like content research examples. |
| Platform/access conditions checked | complete_with_stop_condition | Seed 1 returned a platform canonical redirect, then a 200 search-page app shell. No login, captcha, 403, 429, or platform warning was observed in the static fetch. |
| Credentials/session storage outside git | complete | The canonical response included a session-related header artifact; its value was not copied into git. Use `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-CREDENTIALS` and `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-SESSION-ARTIFACTS`; no credentials, cookies, tokens, browser profiles, or HAR files enter git. |
| Raw output storage outside git | complete | Raw headers and HTML were retained outside the repo for run review only. Use `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-RAW` with run ID `CRAWL-THREADS-PILOT-V1-0001`; exact path outside git. |
| Automation log storage outside git | complete | Use `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-AUTOMATION-LOGS`; repo may keep only non-sensitive summary. |
| Redacted local output path prepared | complete | `data/interim/manual_entry_0001.json` remains ignored/local working data. |
| Run does not require unapproved source/context | complete_with_stop_condition | Static search fetch produced no extractable public item. Selecting an item now requires a browser-rendered, API, or otherwise updated run path before continuing. |
| Concrete seed, URL, query, or access target available | complete | Seed set supplied by project owner; first run uses only seed 1. |

## Seed Set

| Seed | Query | URL | Use in run 0001 |
|---:|---|---|---|
| 1 | `投資` | `https://www.threads.net/search?q=投資` | yes |
| 2 | `賺錢` | `https://www.threads.net/search?q=賺錢` | reserve |
| 3 | `股票` | `https://www.threads.net/search?q=股票` | reserve |
| 4 | `虛擬貨幣` | `https://www.threads.net/search?q=虛擬貨幣` | reserve |
| 5 | `加密貨幣` | `https://www.threads.net/search?q=加密貨幣` | reserve |

## Run Limits

| Limit | Value |
|---|---|
| Target selected item count | 1 |
| Candidate review cap | 5 |
| Runtime cap | 30 minutes |
| Parallel workers | 1 |
| Minimum delay between fetches | 30 seconds |
| Retry cap per failed fetch | 1 |
| Burst behavior | none |
| Redirect capture allowed? | platform canonical redirect only; no external redirect capture |
| Landing-page capture allowed? | no for first run unless this record is updated before execution |
| Profile/account context allowed? | no for first run unless this record is updated before execution |
| Broad reply/comment capture allowed? | no |
| Screenshot capture allowed? | yes, raw outside git only; redacted reference only in local record |
| OCR allowed? | yes, privacy-reviewed excerpt only in local record |

## Field Allowlist

| Field | Allowed? | Repo-visible representation |
|---|---|---|
| post text | yes | redacted visible text or excerpt |
| selected replies/comments | yes | selected redacted replies only |
| image/screenshot reference | yes | redacted local reference only |
| OCR text | yes | risk-relevant privacy-reviewed excerpt |
| visible external links | yes | domain-only or redacted reference |
| contact handles | yes | category or redacted value |
| platform redirects | yes | category only |
| source URL | yes with limits | blank or redacted reference |
| metadata notes | yes | non-sensitive operational notes |

## Stop Conditions

Stop immediately if:

- access challenge, captcha, login block, 403/429, or platform warning appears
- the run needs fields outside the allowlist
- raw evidence would enter git
- credentials/session artifacts would enter git
- unrelated personal data is captured and cannot be redacted safely
- the run is drifting beyond one selected item
- broad profile/account graph capture becomes necessary
- redirect, landing-page, or profile context is needed but not allowed above
- no concrete seed, URL, query, or target is available
- static search fetch returns only a dynamic app shell and no extractable candidate item

## Run Result

| Result field | Value |
|---|---|
| Run started? | yes |
| Run completed? | yes; stopped after seed 1 static-fetch assessment |
| Candidates reviewed | 0 |
| Selected items | 0 |
| Stop condition triggered? | yes |
| Stop condition | Seed 1 produced a 301 platform canonical redirect followed by a 200 search-page app shell with no extractable post text fields; item selection would require an updated browser-rendered/API/session-aware run path. |
| Raw output path recorded outside git? | yes; raw headers and HTML retained outside the repo only |
| Redacted item entered into `manual_entry_0001.json`? | no |
| `manual_record_0001.json` built? | no |
| Strict validation result | not_run; build correctly blocked because no selected item exists |
| Redaction review result | blocked_no_item |
| Decision after run | pause_for_collection_fix |

## Next Action

Do not move to the first 10-15 item checkpoint. The next controlled run is tracked in `threads_pilot_v1_2026-05_controlled_crawler_run_record_0002.md`, which switches from static fetch to a single browser-rendered session-aware path with explicit session, rendering, raw-output, and redaction controls. API/session-aware retrieval remains a later fallback only if the run record is updated or a later record is opened. Only after one selected item is redacted, built, and strict-validated can the project reassess checkpoint readiness.
