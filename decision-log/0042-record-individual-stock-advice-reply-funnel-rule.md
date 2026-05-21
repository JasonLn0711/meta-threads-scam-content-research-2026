# Decision 0042: Record Individual Stock Advice Reply-Funnel Rule

## Date

2026-04-25

## Status

Accepted

## Decision

Add `individual_stock_advice_reply_funnel` as a signal tag and `INDIVIDUAL_STOCK_ADVICE_REPLY_FUNNEL` as a baseline reason code.

This signal covers reply/comment threads where the author repeatedly gives individualized buy, hold, add, wait, sell, target, or position-management guidance on specific stocks or holdings.

## Trigger

The project owner supplied a confirmed Threads scam pointer for item `0033`. The repo records only the repo-safe rule implication, not the raw URL, raw handle, raw post text, raw replies, screenshot, HTML, or source case ID.

The captured pattern is:

- top-level post claims prediction accuracy or market-timing authority;
- users ask whether specific stocks can be bought, added, held, or waited on;
- the author gives short individualized directional answers in replies;
- selected reply context includes group-join status;
- the thread creates a public proof-of-access surface that can move users toward a private or group funnel.

## Rationale

Earlier rules covered stock-rescue group funnels and past-performance proof. Item `0033` shows the reply layer itself can be decisive: individualized stock advice in comments makes the author appear accessible and authoritative, while group-join context suggests a conversion path.

For the CIB-authorized pilot, false negatives are more costly than explainable false positives at triage. The signal should be preserved when it converges with prediction-proof, profit framing, group joins, private-channel migration, or stock-rescue/free-group language.

## Boundaries

- Ordinary public stock Q&A is not automatically `scam`.
- A single opinion reply is not enough by itself.
- Labeling must be based on repeated reply-level advice and the surrounding funnel context.
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
