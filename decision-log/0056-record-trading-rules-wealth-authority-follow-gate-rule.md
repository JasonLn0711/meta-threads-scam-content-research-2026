# Decision 0056: Record Trading-Rules Wealth-Authority Follow-Gate Rule

## Status

Accepted.

## Decision

Add `trading_rules_wealth_authority_follow_gate` as a signal tag and `TRADING_RULES_WEALTH_AUTHORITY_FOLLOW_GATE` as a baseline reason code.

This signal covers investment posts that combine:

- wealth, long-experience, or unusually successful trader authority;
- compact trading-rule, discipline, or buy/sell timing checklist framing;
- action-gated follow-up through like, follow, `+1`, get-on-board, or similar public-to-private lead magnet language.

## Context

Confirmed pointer `0044` shows a softer funnel than visible external links or explicit private-message instructions. The top-level content builds authority through claimed experience and wealth, presents a simple trading-rule checklist, and the continuation asks readers to engage and follow for stock-buying or timing help.

This pattern matters because scammers may avoid direct contact links, LINE IDs, or website URLs in the public post while still using engagement actions to identify interested users for later contact or persuasion.

## Boundaries

- Do not label every trading checklist or stock-discipline post as scam-like.
- The rule requires convergence: authority framing plus trading-rule/checklist framing plus action-gated follow-up.
- Ordinary educational content, transparent newsletters, harmless engagement prompts, and general market commentary should remain non-scam unless additional scam-like signals appear.
- Raw URL, raw handle, raw post text, raw replies, screenshots, and browser artifacts remain in the controlled store only.

## Implementation

Updated:

- `src/baselines/taxonomy.py`
- `src/baselines/signal_extractor.py`
- `src/baselines/explainability.py`
- `configs/baseline_rule_config.yaml`
- `data-contracts/labeling_schema_v1.json`
- `data-contracts/thread_item_schema_v1.json`
- `docs/04-taxonomy.md`
- `docs/06-annotation-guideline-v1.md`
- `docs/30-annotator-onboarding-quickstart.md`
- `docs/43-reason-codes-and-thresholds.md`
- `governance/pilot-launch/threads_pilot_v1_2026-05_guideline_revision_log.md`

## Consequence

Future confirmed pointers can preserve this specific funnel family without overgeneralizing ordinary investment education. Baseline scoring can now surface this soft lead-magnet path as a redirect/contact-family signal when it converges with investment-lure evidence.
