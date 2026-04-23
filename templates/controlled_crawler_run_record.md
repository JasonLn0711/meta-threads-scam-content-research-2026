# Controlled Crawler Run Record

Use this template before any crawler, API, browser automation, redirect capture, landing-page capture, screenshot, or OCR acquisition run.

Keep filled copies local-only or in the controlled store if they contain raw source details, URLs, handles, credentials, session information, run logs, storage paths, or sensitive investigative notes.

## Run Identity

| Field | Value |
|---|---|
| Run ID |  |
| Date |  |
| Operator ID | `AUTO-OP-01` |
| Project owner | `PROJECT-OWNER-01` |
| Governance reviewer | `GOV-REVIEWER-01` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Collection batch ID | `threads_pilot_v1_2026-05` |
| Controlled launch record | `CTRL-THREADS-PILOT-V1-CIB-2026-04-23` |
| Purpose | first one-item controlled crawler rehearsal |
| Current gate | `ready_for_controlled_item_entry` |

## Authorization And Source

| Check | Status | Notes |
|---|---|---|
| CIB authorization applies to this run | yes / no |  |
| Source category is approved | yes / no |  |
| Platform/access conditions checked | yes / no |  |
| Credentials/session storage outside git | yes / no / n/a |  |
| Raw output storage outside git | yes / no |  |
| Redacted local output path prepared | yes / no |  |
| Run does not require unapproved source/context | yes / no |  |

## Run Limits

| Limit | Value |
|---|---|
| Target selected item count | 1 |
| Candidate review cap | 5 |
| Runtime cap | 30 minutes |
| Parallel workers | 1 |
| Minimum delay between fetches | 30 seconds |
| Retry cap per failed fetch | 1 |
| Redirect capture allowed? | yes / no |
| Landing-page capture allowed? | yes / no |
| Profile/account context allowed? | yes / no |
| Broad reply/comment capture allowed? | yes / no |
| Screenshot capture allowed? | yes / no |
| OCR allowed? | yes / no |

## Field Allowlist

| Field | Allowed? | Repo-visible representation |
|---|---|---|
| post text | yes / no | redacted visible text or excerpt |
| selected replies/comments | yes / no | selected redacted replies only |
| image/screenshot reference | yes / no | redacted local reference only |
| OCR text | yes / no | risk-relevant privacy-reviewed excerpt |
| visible external links | yes / no | domain-only or redacted reference |
| contact handles | yes / no | category or redacted value |
| platform redirects | yes / no | category only |
| source URL | yes / no | blank or redacted reference |
| metadata notes | yes / no | non-sensitive operational notes |

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

## Run Result

| Result field | Value |
|---|---|
| Run started? | yes / no |
| Run completed? | yes / no |
| Candidates reviewed |  |
| Selected items |  |
| Stop condition triggered? | yes / no |
| Raw output path recorded outside git? | yes / no |
| Redacted item entered into `manual_entry_0001.json`? | yes / no |
| `manual_record_0001.json` built? | yes / no |
| Strict validation result |  |
| Redaction review result | pass / limited / blocked |
| Decision after run | `pass_ready_for_calibration_or_first_10_15` / `pass_with_limits` / pause outcome |

## Notes

Write only non-sensitive operational notes here.
