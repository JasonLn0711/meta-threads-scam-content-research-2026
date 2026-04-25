# Method Revision Run Record 0011

This is the non-sensitive tracked run record for the method-revision step required after run 0010 exhausted all five item 0017 risk-probe seeds without selecting a safe redacted item.

Do not add raw Threads content, screenshots, full item URLs, raw handles, credentials, cookies, tokens, browser profiles, HAR files, full API responses, exact raw storage paths, access-list details, or sensitive investigative notes to this file. Exact sensitive values remain in the CIB-controlled store or local ignored working files.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `CRAWL-THREADS-PILOT-V1-0011` |
| Date opened | `2026-04-25` |
| Operator ID | `AUTO-OP-01` |
| Project owner | `PROJECT-OWNER-01` |
| Governance reviewer | `GOV-REVIEWER-01` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Collection batch ID | `threads_pilot_v1_2026-05` |
| Controlled launch record | `CTRL-THREADS-PILOT-V1-CIB-2026-04-23` |
| Prior run | `CRAWL-THREADS-PILOT-V1-0010` |
| Prior decision | `pause_item_0017_collection_and_open_method_revision_before_run_0011` |
| Purpose | revise the item 0017 candidate-diagnostic method before any further item attempt |
| Current gate | `candidate_diagnostic_design_ready_not_executed` |
| Run status | `opened_not_started` |

## Required Pre-Run Gate

| Check | Status | Notes |
|---|---|---|
| Run 0010 completed | complete | Five planned seeds attempted; no item 0017 selected. |
| Decision 0026 recorded | complete | Method revision is required before any further item 0017 attempt. |
| Existing 16-record checkpoint strict-valid | required | Validate the local 16-record aggregate before any execution. |
| Browser storage-state artifact | required | Must exist in controlled storage and pass readiness check before any execution. |
| Item 0017 absent | required | Do not proceed if `manual_entry_0017.json` already exists unexpectedly. |

## Method Change

Run 0010 treated candidate selection as an immediate gate: candidates were rejected if they did not already show enough co-occurring visible signals. Run 0011 separates candidate diagnostics from item selection.

The first phase may review candidates for aggregate metadata only. It must not create an item record unless a candidate is reviewable under the approved field allowlist.

## Revised Candidate-Diagnostic Design

| Stage | Purpose | Output |
|---|---|---|
| Access readiness | Confirm approved browser storage-state/session path still works. | Readiness pass/fail only. |
| Candidate diagnostic pass | Review up to 5 candidates per revised seed for aggregate signal metadata. | Repo-safe counts only; no raw text in git. |
| Reviewability gate | Decide whether one candidate has enough visible evidence under the current field allowlist. | yes/no decision for item 0017. |
| Item build gate | If reviewable, create only one local `manual_entry_0017.json`. | Local ignored JSON only. |
| Validation gate | Build and strict-validate `manual_record_0017.json` and the aggregate. | Local ignored outputs plus repo-safe summary. |

## Revised Seed Plan

Use seeds that combine two visible signal families more deliberately. Query terms remain retrieval hints only; they cannot become labels.

| Probe ID | Risk domain | Required visible signal pair | Query seed | Max candidates reviewed |
|---|---|---|---|---:|
| RP-0011-01 | crypto | private-channel migration plus wallet/deposit action | `加密貨幣錢包私訊LINE` | 5 |
| RP-0011-02 | crypto/trading | urgency plus wallet/deposit action | `虛擬貨幣入金限時錢包` | 5 |
| RP-0011-03 | investment/stocks | private-channel migration plus testimonial/proof | `股票獲利截圖LINE群` | 5 |
| RP-0011-04 | side income/recruitment | private-channel migration plus easy-income claim | `副業月入私訊加LINE` | 5 |

## Candidate Diagnostic Metrics

For each seed, record only aggregate metadata:

| Metric | Meaning |
|---|---|
| candidates_reviewed | Number of visible candidates reviewed, capped at 5. |
| negation_or_warning_count | Candidates rejected because they warn against or negate risk claims. |
| single_signal_count | Candidates with exactly one visible signal family. |
| multi_signal_count | Candidates with two or more visible signal families. |
| reviewable_candidate_count | Candidates that may support item 0017 under the approved field allowlist. |
| stop_condition | Any access, privacy, raw-evidence, or field-scope blocker. |

## Run Limits

| Limit | Value |
|---|---|
| Collection attempt allowed in this run | only after diagnostic gate finds a reviewable candidate |
| Target selected item count | at most 1 |
| Target local item ID | `threads_pilot_v1_0017` |
| Candidate review cap | 5 candidates per revised probe seed |
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
| post text | yes | minimized visible text excerpt only if item 0017 is selected |
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
- more than 5 candidates must be reviewed for any revised probe seed
- the run starts collecting beyond item 0017
- unrelated personal data is captured and cannot be redacted safely
- profile graph, follower/following, broad account history, or broad comment capture becomes necessary
- external landing-page or redirect-chain capture becomes necessary
- an item needs screenshots, OCR, replies, or image evidence to be reviewable
- selected output cannot be reduced to approved redacted local JSON fields

## Run Result

| Result field | Value |
|---|---|
| Run started? | no |
| Run completed? | no |
| Diagnostic candidates reviewed | 0 |
| Selected items | 0 |
| Local records built? | no |
| Strict validation result | pending |
| Decision after run | pending |

## Next Action

Before execution, re-check approved browser storage-state readiness, strict-validate the existing 16-record aggregate, and confirm `manual_entry_0017.json` is absent. Then run only the diagnostic pass for `RP-0011-01`; do not create item 0017 unless a candidate is reviewable under this run record.
