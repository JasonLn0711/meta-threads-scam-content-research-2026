# Public-Surface Patrol Script Redline Review

Date: 2026-05-06

Decision context: `0156`

## Reviewed Proposal

A proposed `patrol_threads.py` would:

- open Threads search pages with several investment-scam-related queries;
- scroll the visible page;
- read `body.inner_text`;
- score the full visible body text with keyword rules;
- capture screenshots when the score crosses a threshold;
- write YAML records with query, search URL, screenshot path, score, signals,
  and pending human-review status.

## Boundary Decision

Do not add this live patrol script to the repo in its proposed form.

The proposal contains useful method ideas, but it still crosses the current
governed boundary because it would be a live browser collection script against
Threads before a filled public-surface patrol work order and run-scoped
authorization exist.

## Specific Redlines

| Proposal element | Status | Reason |
|---|---|---|
| `page.goto("https://www.threads.net/search?q=...")` | not allowed in tracked script yet | This is live collection behavior before a work order and run-scoped decision. |
| `page.locator("body").inner_text()` | not allowed as default | This is broad visible-page text extraction, not metadata-only route capture. |
| `page.screenshot(...)` under repo `evidence/screenshots` | rejected | Raw screenshots and screenshot paths must stay outside git-facing artifacts. |
| `search_url` in YAML records | rejected | Raw Threads URLs are forbidden in repo-facing records. |
| `screenshot_local_path` in YAML records | rejected | Exact local raw-artifact paths and screenshot paths are forbidden in repo-facing records. |
| 4 queries times 20 scrolls | too broad for first v0 | Decision `0156` expects a tiny work-ordered viability run, not a default patrol. |
| Keyword score from full page body | weak diagnostic only | It can double-count repeated visible text and cannot identify item-level evidence. |
| `pending_human_review` only | incomplete | Review-worthy yield needs a later human `review_worthy` field or final reviewed label. |

## Accepted Method Ideas

The following ideas are retained:

- public-surface route first;
- no login or bypass;
- one worker;
- bounded queries and scroll depth;
- human-reproducibility trace;
- simple transparent signal hints;
- human review before conclusions;
- `review_worthy_rate` as the first usefulness metric.

## Safe Replacement

Instead of adding a live crawler script, this repo adds:

- `templates/public_surface_patrol_work_order.md` as the run gate;
- `scripts/evaluate_public_surface_patrol_records.py` as a metrics-only local
  evaluator for future repo-safe metadata records;
- `tests/test_public_surface_patrol_metrics.py` to ensure forbidden raw URL and
  screenshot-path fields are rejected.

The metrics script can compute:

```text
review_worthy_rate = human-review-worthy candidates / generated candidates
```

It does not open a browser, read Threads pages, collect raw text, capture
screenshots, or access external systems.

## Decision Implication

The next safe action remains:

```text
official API access check
-> if insufficient, fill public_surface_patrol_work_order.md
-> only then decide whether a tiny capped browser-assist run can be authorized
```

No live Threads patrol starts from this redline review.
