# First Checkpoint Browser Run Record 0003

This is the non-sensitive tracked run record for collecting the remaining local records needed to reach the first 10-item checkpoint.

Do not add raw Threads content, screenshots, full item URLs, raw handles, credentials, cookies, tokens, browser profiles, HAR files, exact raw storage paths, access-list details, or sensitive investigative notes to this file. Exact sensitive values remain in the CIB-controlled store.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `CRAWL-THREADS-PILOT-V1-0003` |
| Date opened | `2026-04-24` |
| Operator ID | `AUTO-OP-01` |
| Project owner | `PROJECT-OWNER-01` |
| Governance reviewer | `GOV-REVIEWER-01` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Collection batch ID | `threads_pilot_v1_2026-05` |
| Controlled launch record | `CTRL-THREADS-PILOT-V1-CIB-2026-04-23` |
| Prior successful run | `CRAWL-THREADS-PILOT-V1-0002` |
| Purpose | collect local records 0002-0010 for the first 10-item checkpoint |
| Current gate | `first_10_item_checkpoint_in_progress` |
| Run status | `completed_10_item_checkpoint_local_records` |

## Authorized Acquisition Path

| Check | Status | Notes |
|---|---|---|
| CIB authorization applies to this run | complete | Approved under Decision 0018 and Decision 0022. |
| Source category is approved | complete | CIB-authorized Threads scam/scam-like content research examples. |
| Acquisition path | complete | Browser-rendered retrieval using a fresh isolated browser context; no stored user browser profile or user cookies loaded. |
| Raw output storage outside git | required | Use CIB-controlled raw store with run ID `CRAWL-THREADS-PILOT-V1-0003`; exact path outside git. |
| Credentials/session storage outside git | complete | No user browser profile or stored cookies are loaded. If a later item requires an approved login/session, stop and update the run record first. |
| Redacted local output path prepared | complete | Local-only `data/interim/manual_entry_0002.json` through `manual_entry_0010.json` and matching local records. |
| Run does not require unapproved source/context | complete | No selected item required profile graph, landing page, redirect chain, broad comment capture, screenshot/OCR evidence, or raw identifier retention. |

## Run Limits

| Limit | Value |
|---|---|
| Additional selected item count | 9 |
| Total checkpoint target | 10 local records including item 0001 |
| Candidate review cap | 5 candidates per selected item |
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
| OCR allowed? | no for this checkpoint run unless a later record updates the scope |

## Field Allowlist

| Field | Allowed? | Repo-visible representation |
|---|---|---|
| post text | yes | minimized visible text excerpt |
| selected replies/comments | no for this checkpoint run |
| image/screenshot reference | no for this checkpoint run |
| OCR text | no for this checkpoint run |
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
- more than 5 candidates must be reviewed for any selected item
- the run starts collecting beyond item 0010
- unrelated personal data is captured and cannot be redacted safely
- profile graph, follower/following, broad account history, or broad comment capture becomes necessary
- external landing-page or redirect-chain capture becomes necessary
- an item needs screenshots, OCR, replies, or image evidence to be reviewable
- selected output cannot be reduced to approved redacted local JSON fields

## Success Sequence

For each selected item:

1. Fill the next local-only `manual_entry_####.json` with approved minimized fields.
2. Build the matching local `manual_record_####.json`.
3. Strict-validate the local record.
4. Append the local collection log.
5. Stop after item `threads_pilot_v1_0010`.

## Run Result

| Result field | Value |
|---|---|
| Run started? | yes |
| Run completed? | yes |
| Candidates reviewed | 44 |
| Selected items | 9 additional; 10 total checkpoint records including run 0002 item |
| Stop condition triggered? | no |
| Stop condition | not_triggered |
| Local records built? | yes; `manual_record_0002.json` through `manual_record_0010.json`, plus existing `manual_record_0001.json` |
| Strict validation result | pass; checkpoint JSONL checked_records 10, errors 0, warnings 0 |
| Decision after run | checkpoint_ready_for_continue_with_limits_review |

## Aggregate Result

| Metric | Value |
|---|---|
| Total local records | 10 |
| `scam` labels | 0 |
| `non_scam` labels | 9 |
| `uncertain` labels | 1 |
| `insufficient_evidence` labels | 0 |
| Text-only items | 10 |
| Items needing second review | 1 |
| Schema errors | 0 |
| Schema warnings | 0 |
| Raw evidence in git | no |
| Source mix warning | yes; all records are `manual_public` / `manual_capture` |
| Content-form warning | yes; all records are text-only |

## Next Action

Complete the local checkpoint review with decision `continue_with_limits`. Do not treat this as broad readiness for the 50-item pilot: before item 16, keep one-at-a-time browser rendering, strict validation for every local record, and pause if higher-risk items require screenshots, OCR, links, redirects, landing pages, profile graph, or raw identifier retention.
