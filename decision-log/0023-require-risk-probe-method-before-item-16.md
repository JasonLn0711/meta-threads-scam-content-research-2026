# Decision 0023: Require Risk-Probe Method Before Item 16

## Date

2026-04-24

## Decision

Do not continue item 16 under the same topic-only seed method. Before collecting item 16, open a new run record for a controlled high-risk case-finding method study.

The pilot may continue only with limits. This decision does not authorize open-ended scraping, profile review, landing-page capture, redirect-chain expansion, screenshot/OCR collection, broad reply capture, raw identifier retention, production monitoring, or legal fraud determinations.

## Context

The first 15 controlled local records were collected under browser-rendered, one-item-at-a-time run records and strict-validated with zero schema errors and zero warnings.

The aggregate result is source- and risk-skewed:

- 15 local records total
- 14 `non_scam`
- 1 adjudicated final `uncertain`
- 0 `scam`
- 0 medium/high-risk records
- 14 text-only records
- 1 private-message boundary record
- no screenshots, OCR, replies, external links, redirect chains, landing pages, or profile context

This means the pipeline works, but the current topic-only search seed path is not producing the positive-risk bucket needed for baseline evaluation or a meaningful 50-item pilot.

## Options Considered

| Option | Decision |
|---|---|
| Continue item 16 with the same topic-only seeds | Rejected; likely to overproduce low-risk comparators. |
| Jump to 50 items now | Rejected; composition and evidence mix are not adequate. |
| Stop the pilot entirely | Rejected; collection mechanics and governance controls are working. |
| Add a controlled risk-probe method before item 16 | Accepted. |

## Rationale

Finding high-risk cases is a sampling and evidence-design problem, not just a volume problem.

The current seed path tests whether ordinary finance/crypto topics create false positives. That is useful, but it does not test high-risk lures. A risk-probe method can test whether controlled combinations of approved domains and visible signal families improve yield while preserving privacy, redaction, and platform controls.

## Consequences

- Record the high-risk case-finding method in `experiments/evaluation-notes/0020-high-risk-case-finding-method-study.md`.
- Open a new run record before item 16 if risk-probe seeds or any new evidence fields are used.
- Keep all item-level outputs local/ignored unless separately sanitized and approved.
- Continue strict validation after every local record.
- Route all uncertain, low-confidence, and high-risk items to second review before the next gate.

## Follow-Up

Before item 16:

1. Define the risk-probe seed matrix in a run record.
2. Keep the candidate cap at 5 per seed unless a later decision narrows it further.
3. Preserve the 30-second minimum delay and single-worker behavior.
4. Record high-risk yield, false-positive pressure, redaction burden, stop-condition rate, and second-review load.
5. Reassess whether the pilot can continue toward item 20 or 25 after the risk-probe result.
