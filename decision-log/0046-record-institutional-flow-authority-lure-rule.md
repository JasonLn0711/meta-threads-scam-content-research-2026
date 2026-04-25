# Decision 0046: Record Institutional-Flow Authority Lure Rule

## Date

2026-04-25

## Status

Accepted

## Decision

Add `institutional_flow_authority_lure` as a signal tag and `INSTITUTIONAL_FLOW_AUTHORITY_LURE` as a baseline reason code.

This signal covers cases where institutional flow, foreign-investor data, futures/spot market numbers, macro-event framing, or market-wide authority cues are used to justify a strong trading action such as buy, hold, full-position, strong long, do not fear, or follow the author.

## Trigger

The project owner supplied a confirmed Threads scam pointer for item `0035`. The repo records only the repo-safe rule implication, not the raw URL, raw handle, raw post text, raw replies, screenshot, HTML, or source case ID.

## Rationale

Earlier rules covered market-direction herding, past-performance profit proof, and account-level multi-post clustering. Item `0035` adds a distinct authority-laundering pattern: external market data and macro-event interpretation are used to make the author's trading instruction feel safer or inevitable.

For high-recall CIB triage, this matters when it converges with past-performance proof, full-position/do-long language, follower reassurance, or reply chorus showing readers are acting on the author's direction.

## Boundaries

- Ordinary macro analysis or institutional-flow commentary is not automatically scam-like.
- A bullish or bearish market opinion alone is not enough.
- The signal should reinforce item-level evidence; it is strongest when paired with profit proof, herding chorus, guru authority, individualized stock advice, stock-community funnel, or private-channel cues.
- Do not claim legal fraud determination from this rule.
- Do not store raw URLs, raw handles, screenshots, raw post text, raw reply text, or source case IDs in git.

## Files Updated

- `docs/04-taxonomy.md`
- `docs/06-annotation-guideline-v1.md`
- `docs/30-annotator-onboarding-quickstart.md`
- `docs/43-reason-codes-and-thresholds.md`
- `data-contracts/labeling_schema_v1.json`
- `data-contracts/thread_item_schema_v1.json`
- `src/baselines/taxonomy.py`
- `src/baselines/signal_extractor.py`
- `src/baselines/explainability.py`
- `configs/baseline_rule_config.yaml`
- `governance/pilot-launch/threads_pilot_v1_2026-05_guideline_revision_log.md`

## Next Action

Use the rule for future confirmed pointers and controlled captures, but keep second review required when this signal materially affects a `scam` or `high` label.
