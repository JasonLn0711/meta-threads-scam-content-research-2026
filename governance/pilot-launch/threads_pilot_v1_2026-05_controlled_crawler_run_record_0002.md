# Controlled Browser/API Run Record 0002

This is the non-sensitive tracked run record for the next one-item controlled rehearsal after static run 0001 produced no extractable candidate item.

Do not add raw Threads content, screenshots, full item URLs, raw handles, credentials, cookies, tokens, browser profiles, HAR files, exact raw storage paths, access-list details, or sensitive investigative notes to this file. Exact sensitive values remain in the CIB-controlled store.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `CRAWL-THREADS-PILOT-V1-0002` |
| Date opened | `2026-04-24` |
| Operator ID | `AUTO-OP-01` |
| Project owner | `PROJECT-OWNER-01` |
| Governance reviewer | `GOV-REVIEWER-01` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Collection batch ID | `threads_pilot_v1_2026-05` |
| Controlled launch record | `CTRL-THREADS-PILOT-V1-CIB-2026-04-23` |
| Prior run | `CRAWL-THREADS-PILOT-V1-0001` |
| Purpose | one-item controlled browser-rendered or API/session-aware rehearsal |
| Current gate | `ready_for_controlled_item_entry` |
| Run status | `completed_one_item_built_strict_validated` |

## Authorized Acquisition Path

| Check | Status | Notes |
|---|---|---|
| CIB authorization applies to this run | complete | Approved under Decision 0018 and Decision 0022. |
| Source category is approved | complete | CIB-authorized Threads scam/scam-like content research examples. |
| Acquisition path | complete | Run 0002 uses browser-rendered session-aware retrieval. Approved API/session-aware retrieval remains a later fallback only if this run is closed or this record is updated before execution. |
| Reason for path change | complete | Run 0001 static fetch returned only a dynamic search app shell and no extractable candidate item. |
| Platform/access conditions checked | complete | Used a fresh isolated browser context with no stored user browser profile or user cookies loaded. Search results rendered; login UI text was visible but did not block candidate review. |
| Credentials/session storage outside git | complete | Use `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-CREDENTIALS` and `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-SESSION-ARTIFACTS`; no credentials, cookies, tokens, browser profiles, or HAR files entered git. |
| Raw output storage outside git | complete | Raw visible text and screenshot were retained outside the repo for run review only. Use `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-RAW` with run ID `CRAWL-THREADS-PILOT-V1-0002`; exact path outside git. |
| Automation log storage outside git | complete | Use `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-AUTOMATION-LOGS`; repo keeps only non-sensitive summary. |
| Redacted local output path prepared | complete | `data/interim/manual_entry_0001.json` remains ignored/local working data and contains one minimized redacted selected item. |
| Run does not require unapproved source/context | complete | Selected item required no profile graph, broad account context, external landing-page capture, or other context outside the run limits. |

## Seed And Candidate Scope

| Field | Value |
|---|---|
| Seed set | Same approved query set recorded in run 0001: `投資`, `賺錢`, `股票`, `虛擬貨幣`, `加密貨幣`. |
| Seed for run 0002 | One seed only: seed 1 by default, unless the operator records a different approved seed in the controlled store before execution. |
| Search surface | Threads search results only. |
| Candidate review cap | 5 candidate items maximum. |
| Selected output cap | exactly 1 selected rehearsal item. |
| If zero usable candidates | stop and record `completed_no_extractable_item`. |
| If more than one plausible item appears | select one only; do not collect a batch. |

## Run Limits

| Limit | Value |
|---|---|
| Target selected item count | 1 |
| Candidate review cap | 5 |
| Runtime cap | 30 minutes |
| Parallel workers | 1 |
| Minimum delay between page/API/object fetches | 30 seconds |
| Retry cap per failed fetch | 1 |
| Burst behavior | none |
| Browser rendering allowed? | yes, if selected as the one execution path |
| Approved API retrieval allowed? | no for this run unless this record is updated before execution |
| Session-aware access allowed? | yes, only with session artifacts outside git |
| Redirect capture allowed? | visible platform/category redirect only; no external landing-page fetch in this run |
| Landing-page capture allowed? | no |
| Profile/account context allowed? | no |
| Broad reply/comment capture allowed? | no |
| Screenshot capture allowed? | yes, raw outside git only; redacted reference only in local record |
| OCR allowed? | yes, privacy-reviewed excerpt only in local record |

## Field Allowlist

| Field | Allowed? | Repo-visible representation |
|---|---|---|
| post text | yes | redacted visible text or excerpt |
| selected replies/comments | yes, only if visible in the selected result context | selected redacted replies only |
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
- the selected path needs credentials, cookies, tokens, browser profiles, HAR files, or raw session details in git
- raw evidence would enter git
- more than 5 candidate items must be reviewed to find one usable item
- the run starts to collect more than one selected item
- unrelated personal data is captured and cannot be redacted safely
- profile graph, follower/following, broad account history, or broad comment capture becomes necessary
- external landing-page or redirect-chain capture becomes necessary
- the selected item cannot be redacted into the approved schema fields
- browser-rendered/API output cannot be reduced to one approved redacted `manual_entry_0001.json`

## Success Sequence

Only after exactly one selected controlled item is available:

1. Fill `data/interim/manual_entry_0001.json` with approved redacted fields only.
2. Build the local record:

```bash
.venv/bin/python scripts/build_manual_collection_record.py data/interim/manual_entry_0001.json \
  --ack-controlled-details \
  --output data/interim/manual_record_0001.json \
  --collection-log data/interim/threads_pilot_v1_collection_log.csv
```

3. Strict-validate the local record:

```bash
.venv/bin/python scripts/validate_thread_dataset.py data/interim/manual_record_0001.json --strict
```

4. Complete the local rehearsal checklist and aggregate review.
5. Reassess whether the first 10-15 item checkpoint can begin.

## Run Result

| Result field | Value |
|---|---|
| Run started? | yes |
| Run completed? | yes |
| Execution path selected? | yes; browser-rendered session-aware retrieval |
| Candidates reviewed | 5 |
| Selected items | 1 |
| Stop condition triggered? | no |
| Stop condition | not_triggered |
| Raw output path recorded outside git? | yes; raw visible text and screenshot retained outside the repo only |
| Redacted item entered into `manual_entry_0001.json`? | yes; local-only minimized entry |
| `manual_record_0001.json` built? | yes; local-only output |
| Strict validation result | pass; checked_records 1, errors 0, warnings 0 |
| Redaction review result | pass_with_limits |
| Decision after run | pass_with_limits_pending_aggregate_review |

## Next Action

Complete the local controlled rehearsal checklist and aggregate review. If the aggregate review records `pass_with_limits`, the first 10-15 item checkpoint may begin only under those limits: one browser-rendered item at a time, at most 5 candidates reviewed per selected item, no raw evidence in git, no source URL or handle retention in git, no profile graph, no landing-page capture, and strict validation after each local record.
