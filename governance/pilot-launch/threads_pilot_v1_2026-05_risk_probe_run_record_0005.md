# Risk-Probe Browser Run Record 0005

This is the non-sensitive tracked run record for the first high-risk case-finding method experiment after the first 15 controlled local records yielded no medium/high-risk examples.

Do not add raw Threads content, screenshots, full item URLs, raw handles, credentials, cookies, tokens, browser profiles, HAR files, exact raw storage paths, access-list details, or sensitive investigative notes to this file. Exact sensitive values remain in the CIB-controlled store or local ignored working files.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `CRAWL-THREADS-PILOT-V1-0005` |
| Date opened | `2026-04-24` |
| Operator ID | `AUTO-OP-01` |
| Project owner | `PROJECT-OWNER-01` |
| Governance reviewer | `GOV-REVIEWER-01` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Collection batch ID | `threads_pilot_v1_2026-05` |
| Controlled launch record | `CTRL-THREADS-PILOT-V1-CIB-2026-04-23` |
| Prior decision | `0023-require-risk-probe-method-before-item-16` |
| Purpose | test a small risk-probe seed matrix before item 16 |
| Current gate | `risk_probe_result_review_required_before_item_16` |
| Run status | `completed_no_extractable_item` |

## Required Pre-Run Gate

| Check | Status | Notes |
|---|---|---|
| First 15-item limited extension completed | complete | 15-record aggregate strict validation passed with zero errors and warnings. |
| Source-strategy gate recorded | complete | Decision 0023 requires a risk-probe method before item 16. |
| Method study exists | complete | `experiments/evaluation-notes/0020-high-risk-case-finding-method-study.md`. |
| Raw output storage outside git | required | Use controlled/local raw store with run ID `CRAWL-THREADS-PILOT-V1-0005`; exact path outside git. |
| Redacted local output path prepared | complete | Local-only `data/interim/manual_entry_0016.json` through `manual_entry_0020.json` if selected. |

## Risk-Probe Seed Matrix

Query terms are candidate-generation probes only. They must not become labels by themselves.

| Probe ID | Risk domain | Visible signal family | Query seed | Max candidates reviewed |
|---|---|---|---|---:|
| RP-0005-01 | investment | guaranteed outcome | `投資 保證獲利` | 5 |
| RP-0005-02 | stocks/investment | private-channel migration | `股票 LINE 投資群` | 5 |
| RP-0005-03 | crypto | wallet/deposit/reward action | `加密貨幣 錢包 空投` | 5 |
| RP-0005-04 | crypto/trading | urgency or deposit action | `比特幣 入金 限時` | 5 |
| RP-0005-05 | side income/recruitment | easy-income/private-channel/testimonial pressure | `副業 月入 私訊` | 5 |

## Authorized Acquisition Path

| Check | Status | Notes |
|---|---|---|
| CIB authorization applies to this run | complete | Approved under Decision 0018, Decision 0022, and the controlled launch record. |
| Source category is approved | complete | CIB-authorized Threads scam/scam-like content research examples. |
| Acquisition path | complete | Browser-rendered retrieval using a fresh isolated browser context; no stored user browser profile or user cookies loaded. |
| API retrieval | not_used | Browser-rendered path only for this risk-probe run. |
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

Risk-probe query matches are not labels. A selected item may be `non_scam`, `uncertain`, `insufficient_evidence`, or `scam` only based on observable retained evidence in the local redacted record.

## Success Sequence

For each selected item:

1. Fill the next local-only `manual_entry_####.json` with approved minimized fields.
2. Build the matching local `manual_record_####.json`.
3. Strict-validate the local record.
4. Second-review any `uncertain`, low-confidence, or high-risk item before the next gate.
5. Rebuild the local aggregate outside git.

## Run Result

| Result field | Value |
|---|---|
| Run started? | yes |
| Run completed? | yes |
| Candidates reviewed | 25 candidate lines surfaced by the page |
| Extractable candidates reviewed | 0 real content candidates |
| Selected items | 0 |
| Stop condition triggered? | yes |
| Stop condition | risk-probe search returned only query echo, login/user-interface text, or policy/navigation text; no real item content could be redacted |
| Local records built? | no; no `manual_entry_0016.json` was created |
| Strict validation result | not_applicable_no_selected_item |
| High-risk candidate yield | 0 |
| False-positive pressure | high; probe terms appeared as query echoes rather than item evidence |
| Redaction burden | not_tested_on_real_content |
| Second-review load | 0 |
| Decision after run | `revise_risk_probe_access_or_seed_method_before_item_16` |

## Aggregate Probe Result

| Probe ID | Query seed | Page status | Candidate cap respected? | Extractable real candidates | Selected items |
|---|---|---:|---|---:|---:|
| RP-0005-01 | `投資 保證獲利` | 200 | yes | 0 | 0 |
| RP-0005-02 | `股票 LINE 投資群` | 200 | yes | 0 | 0 |
| RP-0005-03 | `加密貨幣 錢包 空投` | 200 | yes | 0 | 0 |
| RP-0005-04 | `比特幣 入金 限時` | 200 | yes | 0 | 0 |
| RP-0005-05 | `副業 月入 私訊` | 200 | yes | 0 | 0 |

## Method Finding

The risk-probe seed matrix is conceptually valid, but this browser-rendered search path did not expose real item content for multi-term risk-probe queries. The visible page text was limited to query echoes and generic user-interface or policy/navigation text, so no item could be selected without violating the labeling guardrail.

The run confirms an important methodological risk: if query terms are surfaced as page text, the collector must not mistake the query echo for evidence. Query terms are candidate-generation probes only.

## Next Action

Do not create item 0016 from this run. Before item 16, revise the risk-probe acquisition path in a new run record. The next run should test either an approved browser-rendered session/access path, an approved API/session-aware path, or a narrower no-query-echo candidate-generation method, while preserving the same labeling guardrail.
