# Decision 0040: Record Past-Performance Profit-Proof Rule

## Date

2026-04-25

## Status

Accepted

## Decision

Add `past_performance_profit_proof` as a signal tag and `PAST_PERFORMANCE_PROFIT_PROOF` as a baseline reason code.

This signal covers past stock-pick performance, hit-rate, limit-up, profit-table, or wealth-result claims used as proof of the poster's ability.

## Trigger

The project owner supplied a confirmed Threads scam pointer for item `0031`. The repo records only the repo-safe rule implication, not the raw URL, raw handle, raw post text, screenshot, HTML, or source case ID.

The captured pattern is:

- multiple named stock-pick or recommendation claims;
- percentage gain or limit-up proof;
- wealth-result language suggesting followers became rich;
- "not charging" or free-sharing framing;
- financial-freedom or altruistic-guru credibility framing.

## Rationale

Earlier rules covered implicit DM conversion, high-fee course funnels, and comment-code lead magnets. Item `0031` adds another common trust-building layer: a poster can use alleged past performance and wealth-result proof to establish authority before any later conversion step appears.

For the CIB-authorized pilot, false negatives are more costly than explainable false positives at triage. The signal should be preserved when it converges with investment/profit framing, named stock picks, percentage-gain proof, free-sharing guru framing, private-channel migration, comment-code funnels, or payment/course signals.

## Boundaries

- Historical stock discussion is not automatically a `scam` label.
- Ordinary investment journaling or performance review is not automatically scam-like.
- A single performance screenshot is not enough by itself; labeling must rest on the whole collected `thread_item`.
- Do not claim legal fraud determination from this rule.
- Do not store raw URLs, raw handles, screenshots, raw post text, raw reply text, or source case IDs in git.

## Files Updated

- `docs/04-taxonomy.md`
- `docs/06-annotation-guideline-v1.md`
- `docs/30-annotator-onboarding-quickstart.md`
- `data-contracts/labeling_schema_v1.json`
- `data-contracts/thread_item_schema_v1.json`
- `docs/43-reason-codes-and-thresholds.md`
- `src/baselines/taxonomy.py`
- `src/baselines/signal_extractor.py`
- `src/baselines/explainability.py`
- `configs/baseline_rule_config.yaml`
- `governance/pilot-launch/threads_pilot_v1_2026-05_guideline_revision_log.md`

## Next Action

Use the rule for future confirmed pointers and controlled captures, but keep second review required when this signal materially affects a `scam` or `high` label.
