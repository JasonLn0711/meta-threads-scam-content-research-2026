# Limited Extension Browser Run Record 0004

This is the non-sensitive tracked run record for the item 11-15 limited extension after the first 10-item checkpoint decision `continue_with_limits`.

Do not add raw Threads content, screenshots, full item URLs, raw handles, credentials, cookies, tokens, browser profiles, HAR files, exact raw storage paths, access-list details, or sensitive investigative notes to this file. Exact sensitive values remain in the CIB-controlled store or local ignored working files.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `CRAWL-THREADS-PILOT-V1-0004` |
| Date opened | `2026-04-24` |
| Operator ID | `AUTO-OP-01` |
| Project owner | `PROJECT-OWNER-01` |
| Governance reviewer | `GOV-REVIEWER-01` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Collection batch ID | `threads_pilot_v1_2026-05` |
| Controlled launch record | `CTRL-THREADS-PILOT-V1-CIB-2026-04-23` |
| Prior checkpoint decision | `continue_with_limits` |
| Purpose | collect local records 0011-0015 as a limited extension before item 16 |
| Current gate | `source_strategy_review_required_before_item_16` |
| Run status | `completed_15_item_limited_extension` |

## Required Pre-Run Gate

| Check | Status | Notes |
|---|---|---|
| First 10-item checkpoint completed | complete | Decision was `continue_with_limits`. |
| Required second review completed before item 16 | complete | The one prior `uncertain` item was adjudicated locally as `non_scam` / `low`; item-level review remains outside git. |
| Raw output storage outside git | required | Use controlled/local raw store with run ID `CRAWL-THREADS-PILOT-V1-0004`; exact path outside git. |
| Redacted local output path prepared | complete | Local-only `data/interim/manual_entry_0011.json` through `manual_entry_0015.json` and matching local records. |

## Authorized Acquisition Path

| Check | Status | Notes |
|---|---|---|
| CIB authorization applies to this run | complete | Approved under Decision 0018 and Decision 0022. |
| Source category is approved | complete | CIB-authorized Threads scam/scam-like content research examples. |
| Acquisition path | complete | Browser-rendered retrieval using a fresh isolated browser context; no stored user browser profile or user cookies loaded. |
| API retrieval | not_used | Browser-rendered path only for this limited extension. |
| Run does not require unapproved source/context | required | Stop if a selected item requires profile graph, landing page, redirect chain, broad comments, screenshot/OCR evidence, or raw identifier retention. |

## Run Limits

| Limit | Value |
|---|---|
| Additional selected item count | 5 |
| Target local item IDs | `threads_pilot_v1_0011` through `threads_pilot_v1_0015` |
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
- more than 5 candidates must be reviewed for any selected item
- the run starts collecting beyond item 0015
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
4. Append or rebuild the local checkpoint-extension aggregate outside git.
5. Stop after item `threads_pilot_v1_0015`.

## Run Result

| Result field | Value |
|---|---|
| Run started? | yes |
| Run completed? | yes |
| Candidates reviewed | 25 |
| Selected items | 5 additional; 15 total checkpoint-extension records |
| Stop condition triggered? | no |
| Stop condition | not_triggered |
| Local records built? | yes; `manual_record_0011.json` through `manual_record_0015.json`, plus rebuilt aggregate local records |
| Strict validation result | pass; 15-record JSONL and CSV checked_records 15, errors 0, warnings 0 |
| Decision after run | `limited_extension_complete_source_strategy_review_required` |

## Aggregate Result

| Metric | Value |
|---|---|
| Total local records | 15 |
| `scam` labels | 0 |
| `non_scam` labels | 14 |
| `uncertain` labels | 1 final after adjudication |
| `insufficient_evidence` labels | 0 |
| Low-risk records | 15 |
| Medium/high-risk records | 0 |
| Text-only items | 14 |
| Private-message boundary items | 1 |
| Items second-reviewed before item 16 | 2 |
| Schema errors | 0 |
| Schema warnings | 0 |
| Raw evidence in git | no |
| Source mix warning | yes; all records are `manual_public` / `manual_capture` |
| Content-form warning | yes; no screenshots, OCR, replies, external links, landing pages, or redirect chains tested |

## Next Action

The limited extension is complete and strict-valid, but it did not find high-risk examples. Do not treat this as readiness for the full 50-item pilot. Before item 16, record a high-risk case-finding method study and open a new run record if the next tranche uses risk-probe seeds or any fields beyond this run.
