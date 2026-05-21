# Dedupe-First Full-Thread-Ready Gate

## Purpose

Use this gate before any future browser-session candidate is promoted into a selected item after run `0039`.

Run `0039` showed that larger browser-session search volume can produce strict-valid local candidate records, but the bottleneck is evidence quality, not candidate count. Browser search snippets can be duplicate, context-thin, or over-attributed from page-level signals.

This gate prevents browser candidates from becoming official checkpoint items unless they pass dedupe, source-context, reply-context, and second-review checks.

This method is repo-safe. Do not add raw Threads content, full URLs, handles, screenshots, HTML, credentials, cookies, browser storage state, contact IDs, stock names, stock codes, price values, or sensitive investigative notes to this file.

Use `templates/browser_candidate_promotion_review.md` to record the gate result for any future candidate review.

## When To Use

Use this gate only when:

- no CIB/stakeholder/project-owner confirmed pointer is available;
- a later decision authorizes a bounded browser-session candidate run;
- the approved browser/session-aware or API/session-aware path is ready;
- the goal is candidate discovery or false-positive pressure, not prevalence measurement.

If the run uses search queries, it must also satisfy [54-browser-query-diversification-rule.md](54-browser-query-diversification-rule.md) before execution.

Do not use it to justify broad crawler expansion, private-message access, profile graph capture, landing-page capture, redirect-chain capture, embedding/model training, or production detection.

## Promotion Rule

A browser-session candidate may become an official selected item only if all required gates pass:

| Gate | Required Result |
|---|---|
| Authorization gate | approved run record exists with candidate and selected-item caps |
| Access gate | approved browser/session-aware or API/session-aware path passes readiness check |
| Query-diversification gate | if search queries are used, the seed matrix varies risk domain, visible signal family, and wording style |
| Dedupe gate | candidate is not an exact or near duplicate of an existing item or local candidate |
| Source-context gate | enough source context exists to interpret the visible claim without relying on query terms |
| Reply-context gate | replies/comments are captured or explicitly determined unavailable |
| Evidence attribution gate | page-level links or search-page context are not treated as item-level evidence unless tied to the item |
| Redaction gate | repo-safe fields only; raw evidence remains in the controlled store |
| Strict-validation gate | one-item and aggregate validation pass with 0 errors and 0 warnings |
| Second-review gate | fast different-angle review accepts final label/risk/evidence family |

If any gate fails, the candidate may stay as a local controlled-run trace, but it must not be promoted into the official checkpoint.

The repo-safe promotion review should use:

```text
templates/browser_candidate_promotion_review.md
```

## Dedupe Gate

Check exact and near-duplicate pressure against:

- `post_text`;
- minimized post text;
- visible redacted contact/action patterns;
- candidate bucket hash;
- dedupe key;
- previous browser-session tranche outputs;
- existing official checkpoint records.

If the candidate repeats an existing browser-session item without new reply/source context, classify it as duplicate or near-duplicate and exclude it from promotion.

## Full-Thread-Ready Gate

Before final label promotion, the candidate must have one of:

- controlled full-thread capture with post and relevant replies/comments;
- controlled capture showing replies/comments were unavailable or inaccessible;
- confirmed-pointer context strong enough to support label without additional reply context.

Search-rendered snippets alone are insufficient for new final scam/high-risk rule-family learning.

## Labeling Consequences

Browser-session candidates should default conservatively:

- `scam` / `high` only when item-level evidence and second review support it;
- `uncertain` when surface signals exist but source/reply context is thin;
- `insufficient_evidence` when the candidate cannot be interpreted or is duplicate-only;
- `non_scam` only when protective, warning, ordinary discussion, or comparator context is sufficiently clear.

Query terms may help find candidates, but they must not become label evidence.

If the same or similar query set has already been used, the run record must explain why repetition is necessary and how the new run changes source path, extraction surface, context capture, or candidate caps.

## Preferred Next Source Order

After run `0039`, the preferred order is:

1. CIB/stakeholder/project-owner confirmed pointer.
2. Full-thread-ready capture of a narrow approved candidate.
3. Dedupe-first browser-session search for false-positive pressure or uncertainty calibration.

Do not increase browser-session caps until this gate has been tested on a small bounded run.
