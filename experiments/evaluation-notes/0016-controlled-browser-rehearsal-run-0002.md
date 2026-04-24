# Controlled Browser Rehearsal Run 0002

## Purpose

Record the repo-safe result of the controlled browser-rendered rehearsal after static run 0001 produced no extractable candidate item.

This note contains no raw Threads content, item URLs, handles, screenshots, cookies, tokens, browser profiles, HAR files, raw headers, raw visible text, raw storage paths, or sensitive investigative material.

## Run Scope

| Field | Value |
|---|---|
| Run ID | `CRAWL-THREADS-PILOT-V1-0002` |
| Date | `2026-04-24` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Authorization basis | Decision 0018 and Decision 0022 |
| Run record | `governance/pilot-launch/threads_pilot_v1_2026-05_controlled_crawler_run_record_0002.md` |
| Acquisition path | browser-rendered session-aware retrieval |
| Browser context | fresh isolated context; no stored user browser profile or user cookies loaded |
| Seed | seed 1 from the approved query set |
| Candidate review cap | 5 |
| Selected item count | 1 |

## Non-Sensitive Observations

| Observation | Result |
|---|---|
| Search results rendered | yes |
| Login UI text visible | yes, but it did not block candidate review |
| Access challenge/captcha/403/429/platform warning observed | no |
| Candidate items reviewed | 5 |
| Selected items | 1 |
| Selected item class | finance/investment topic-only text; no scam-funnel signal observed |
| Raw visible text and screenshot retained outside git | yes |
| Source URL, handle, and raw screenshot stored in git | no |
| Redacted item entered into `manual_entry_0001.json` | yes, local-only |
| `manual_record_0001.json` built | yes, local-only |
| Strict validation | pass: 1 record, 0 errors, 0 warnings |

## Boundary Result

The selected rehearsal item is useful as a finance-topic boundary case. It should remain `non_scam` because topic alone is not evidence of scam-like behavior.

No guaranteed-profit claim, private-channel redirect, visible external link, contact handle, payment request, credential/personal-data request, impersonation, urgency pressure, or testimonial/earnings screenshot was retained in the minimized record.

## Decision

```text
pass_with_limits
```

## Rationale

- The browser-rendered path produced one selected, minimized, schema-valid local record.
- Governance and schema checks returned zero errors and zero warnings.
- Raw visible text, screenshot, session artifacts, source URL, and handles stayed outside git.
- The rehearsal only tested one text-only, low-risk boundary item; it did not test image/OCR, redirects, landing pages, profile context, or high-risk scam-funnel examples.
- The first 10-15 item checkpoint can begin only with continued tight limits and per-item validation.

## Limits For First 10-15 Item Checkpoint

- Collect one browser-rendered item at a time.
- Review at most 5 candidates per selected item.
- Store no raw source URL, handle, screenshot, browser profile, cookie, token, or raw visible text in git.
- Do not capture profile graph, follower/following context, broad comments, external landing pages, or redirect chains unless a later run record explicitly authorizes it.
- Strict-validate each local record before counting it toward the checkpoint.
- Pause if the first scam-like item needs fields outside the current schema or redaction rules.
