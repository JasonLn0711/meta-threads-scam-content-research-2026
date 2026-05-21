# Risk-Probe Run 0005 Result

## Purpose

Record the repo-safe aggregate result of the first high-risk case-finding risk-probe experiment.

This note contains no raw Threads content, item URLs, handles, screenshots, cookies, tokens, browser profiles, HAR files, raw visible text, raw storage paths, or sensitive investigative material.

## Run Scope

| Field | Value |
|---|---|
| Run ID | `CRAWL-THREADS-PILOT-V1-0005` |
| Date | `2026-04-24` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Purpose | test whether domain plus signal-family query probes improve high-risk discovery |
| Probe seeds | 5 |
| Candidate cap | 5 candidate lines per probe seed |
| Delay | 30 seconds between page/object fetches |
| Collection path | browser-rendered, fresh isolated context, no stored user browser profile or cookies |

## Probe Matrix Tested

| Probe ID | Domain | Signal family | Query seed |
|---|---|---|---|
| RP-0005-01 | investment | guaranteed outcome | `投資 保證獲利` |
| RP-0005-02 | stocks/investment | private-channel migration | `股票 LINE 投資群` |
| RP-0005-03 | crypto | wallet/deposit/reward action | `加密貨幣 錢包 空投` |
| RP-0005-04 | crypto/trading | urgency or deposit action | `比特幣 入金 限時` |
| RP-0005-05 | side income/recruitment | easy-income/private-channel/testimonial pressure | `副業 月入 私訊` |

## Result

| Metric | Value |
|---|---:|
| Probe seeds requested | 5 |
| Page responses with HTTP 200 | 5 |
| Candidate lines surfaced by page | 25 |
| Extractable real content candidates | 0 |
| Selected items | 0 |
| Local records built | 0 |
| High-risk yield | 0 |
| Medium-risk yield | 0 |
| Second-review load | 0 |

## Finding

The risk-probe idea was tested, but the current browser-rendered search path did not expose extractable item content for these multi-term risk-probe queries. The visible candidate lines were query echoes or generic user-interface / policy / navigation text, not real item content.

No `manual_entry_0016.json` was created. This is the correct outcome: query terms are candidate-generation probes only and cannot be treated as evidence or labels.

## Method Implication

The result does not prove that high-risk content is absent. It shows that the current unauthenticated browser-rendered multi-term search path is not a reliable candidate-generation method for risk-probe queries.

## Decision

```text
revise_risk_probe_access_or_seed_method_before_item_16
```

## Required Before Item 16

- Open a new run record before collecting item 0016.
- Keep the same label guardrail: query terms cannot become item evidence.
- Test either an approved browser-rendered session/access path, an approved API/session-aware path, or a narrower candidate-generation method that avoids query-echo artifacts.
- Preserve the candidate cap, pacing, raw-output boundary, and one-item-at-a-time review discipline unless a later decision explicitly changes them.
- If the next method still returns only query echoes or UI text, record another no-extractable-item result rather than creating a fake item.
