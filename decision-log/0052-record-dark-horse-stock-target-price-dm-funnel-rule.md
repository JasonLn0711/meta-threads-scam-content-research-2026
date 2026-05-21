# Decision 0052: Record Dark-Horse Stock Target-Price DM Funnel Rule

## Date

2026-04-25

## Status

Accepted

## Decision

Add `dark_horse_stock_target_price_dm_funnel` as a signal tag and `DARK_HORSE_STOCK_TARGET_PRICE_DM_FUNNEL` as a baseline reason code.

This signal covers hidden or "dark horse" stock lures that compare low current price to much higher target or expected price, add catalyst claims, and gate the promised stock details behind follow, like, message, numeric-code, or private-share action.

## Trigger

The project owner supplied a confirmed Threads scam pointer for item `0040`. The repo records only the repo-safe rule implication, not the raw URL, raw handle, raw stock names, raw price/target values, raw code, raw post text, raw replies, screenshot, HTML, or source case ID.

## Rationale

Item `0040` shows a conversion pattern that is narrower than ordinary stock commentary: a public stock-command list and hidden-stock teaser are paired with strong target-price framing, urgency, catalyst authority, and repeated author replies steering individual users toward follow/message delivery.

## Boundaries

- Do not label ordinary target-price discussion, ordinary stock watchlists, or ordinary technology-catalyst commentary as scam-like by themselves.
- The signal requires convergence: hidden/dark-horse stock framing plus high target-price lure plus action/private-share gate.
- It is strongest when paired with repeated author replies, comment-code lead magnets, private-channel redirect, past-performance proof, urgency, or account-level cluster evidence.
- Do not store raw URLs, raw handles, raw stock names, raw price/target values, raw code, raw post text, raw reply text, screenshots, HTML, or source case IDs in git.

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

Use this rule for hidden-stock target-price funnels where the promised details are withheld until the reader follows, messages, enters a code, or otherwise enters a private/action-gated path.
