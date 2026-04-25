# Decision 0051: Record Lifestyle-Trust Market Reassurance Funnel Rule

## Date

2026-04-25

## Status

Accepted

## Decision

Add `lifestyle_trust_market_reassurance_funnel` as a signal tag and `LIFESTYLE_TRUST_MARKET_REASSURANCE_FUNNEL` as a baseline reason code.

This signal covers lifestyle, travel, warmth, gratitude, or parasocial closeness paired with market fear reassurance and concrete buy, hold, add, low-buy, or keep-position guidance.

## Trigger

The project owner supplied a confirmed Threads scam pointer for item `0039`. The repo records only the repo-safe rule implication, not the raw URL, raw handle, raw post text, raw replies, screenshot, HTML, contact handles, or source case ID.

## Rationale

Item `0039` shows trust laundering: personal lifestyle imagery and warm parasocial tone are mixed with market panic interpretation, reassurance, and trading instructions. The reply layer also contains follower trust and repeated contact/group hijack replies, which reinforces thread-level risk.

## Boundaries

- Do not label ordinary lifestyle posts, greetings, travel content, or benign market commentary as scam-like by themselves.
- The signal requires convergence: lifestyle/trust framing plus market fear reassurance plus concrete buy/hold/add guidance.
- It is strongest when paired with follower trust comments, private-channel/contact hijack replies, repeated stock-pick proof, strong market-direction calls, or account-level cluster evidence.
- Do not store raw URLs, raw handles, raw post text, raw reply text, screenshots, HTML, contact handles, or source case IDs in git.

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

Use this rule when lifestyle trust and market fear reassurance are used to steer trading action, especially when reply-level contact hijack or follower trust appears in the same thread.
