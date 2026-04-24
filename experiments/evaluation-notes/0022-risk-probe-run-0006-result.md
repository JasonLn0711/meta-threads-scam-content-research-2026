# Risk-Probe Run 0006 Result

## Purpose

Record the repo-safe aggregate result of the normalized no-space risk-probe retry after run 0005 returned only query echoes and user-interface text.

This note contains no raw Threads content, item URLs, handles, screenshots, cookies, tokens, browser profiles, HAR files, raw visible text, raw storage paths, or sensitive investigative material.

## Run Scope

| Field | Value |
|---|---|
| Run ID | `CRAWL-THREADS-PILOT-V1-0006` |
| Date | `2026-04-24` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Purpose | test whether normalized no-space risk-probe phrases avoid query-echo artifacts |
| Probe seeds | 5 |
| Candidate cap | 5 candidate lines per probe seed |
| Delay | 30 seconds between page/object fetches |
| Collection path | browser-rendered, fresh isolated context, no stored user browser profile or cookies |

## Probe Matrix Tested

| Probe ID | Domain | Signal family | Query seed |
|---|---|---|---|
| RP-0006-01 | investment | guaranteed outcome | `投資保證獲利` |
| RP-0006-02 | stocks/investment | private-channel migration | `股票LINE投資群` |
| RP-0006-03 | crypto | wallet/deposit/reward action | `加密貨幣空投錢包` |
| RP-0006-04 | crypto/trading | urgency or deposit action | `比特幣入金限時` |
| RP-0006-05 | side income/recruitment | easy-income/private-channel/testimonial pressure | `副業月入私訊` |

## Result

| Metric | Value |
|---|---:|
| Probe seeds requested | 5 |
| Page responses with HTTP 200 | 5 |
| Non-query lines surfaced after query echoes were excluded | 5 |
| Extractable real content candidates | 0 |
| Selected items | 0 |
| Local records built | 0 |
| High-risk yield | 0 |
| Medium-risk yield | 0 |
| Second-review load | 0 |

## Finding

The normalized no-space retry did not produce extractable real item content. After exact query echoes and known interface text were excluded, the remaining page text was generic onboarding or user-interface copy, not evidence from Threads items.

No `manual_entry_0016.json` was created. This remains the correct outcome because query terms and user-interface text cannot become item evidence.

## Method Implication

Runs 0005 and 0006 together show that public unauthenticated browser-rendered search is not a reliable candidate-generation path for high-risk risk-probe queries. The next experiment should not keep changing query strings in the same access mode.

## Decision

```text
approved_session_or_api_access_review_required_before_item_16
```

## Required Before Item 16

- Open a new run record before collecting item 0016.
- Confirm the approved browser-rendered session/access or API/session-aware path outside git.
- Keep credentials, cookies, browser profiles, tokens, HAR files, raw output, source URLs, handles, and screenshots outside git.
- Keep the same seed-matrix labeling guardrail: query terms can only find candidates and cannot become labels.
- If approved session/API access still returns only query echoes or UI text, stop and record no extractable item.
