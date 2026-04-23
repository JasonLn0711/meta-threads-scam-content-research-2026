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
| Run status | `ready_pending_seed_or_target` |

## Access, Session, And Output Confirmation

| Check | Status | Notes |
|---|---|---|
| CIB authorization applies to this run | complete | Approved under Decision 0018 and Decision 0022. |
| Source category is approved | complete | CIB-authorized Threads scam/scam-like content research examples. |
| Platform/access conditions checked | complete_with_sensitive_details_outside_git | Exact access path, account/session state, and any platform-specific constraints remain in the CIB-controlled store. |
| Credentials/session storage outside git | complete | Use `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-CREDENTIALS` and `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-SESSION-ARTIFACTS`; no credentials, cookies, tokens, browser profiles, or HAR files enter git. |
| Raw output storage outside git | complete | Use `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-RAW` with run ID `CRAWL-THREADS-PILOT-V1-0001`; exact path outside git. |
| Automation log storage outside git | complete | Use `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-AUTOMATION-LOGS`; repo may keep only non-sensitive summary. |
| Redacted local output path prepared | complete | `data/interim/manual_entry_0001.json` remains ignored/local working data. |
| Run does not require unapproved source/context | pending_execution | Confirm during execution; stop if the crawler needs context outside this record. |
| Concrete seed, URL, query, or access target available | missing | Required before execution; do not invent a seed or target. |

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
| Redirect capture allowed? | no for first run unless this record is updated before execution |
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

## Run Result

| Result field | Value |
|---|---|
| Run started? | no |
| Run completed? | no |
| Candidates reviewed | 0 |
| Selected items | 0 |
| Stop condition triggered? | yes |
| Stop condition | concrete seed, URL, query, or access target missing |
| Raw output path recorded outside git? | prepared |
| Redacted item entered into `manual_entry_0001.json`? | no |
| `manual_record_0001.json` built? | no |
| Strict validation result | not_run |
| Redaction review result | not_run |
| Decision after run | blocked_missing_seed_or_target |

## Next Action

Provide or select one concrete CIB-approved seed, URL, query, or access target outside git. Then execute the one-item crawler rehearsal under this record, redact the selected item into `data/interim/manual_entry_0001.json`, build `manual_record_0001.json`, and run strict validation.
