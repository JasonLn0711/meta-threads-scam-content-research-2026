# Decision 0041: Record Stock-Rescue Group Funnel Rule

## Date

2026-04-25

## Status

Accepted

## Decision

Add `stock_rescue_group_funnel` as a signal tag and `STOCK_RESCUE_GROUP_FUNNEL` as a baseline reason code.

This signal covers trapped-stock rescue, portfolio help, synchronized operation, free stock-community access, or stock-help group funnels.

## Trigger

The project owner supplied a confirmed Threads scam pointer for item `0032`. The repo records only the repo-safe rule implication, not the raw URL, raw handle, raw post text, screenshot, raw external link, HTML, or source case ID.

The captured pattern is:

- offers help for trapped stocks or uncertain holdings;
- encourages users to ask for individual stock references or consultation;
- promotes a free stock-learning/community/group path;
- invites synchronized operation or following the poster's operation;
- uses a LINE/OpenChat-style or shortener-based group link.

## Rationale

Earlier rules covered implicit DM conversion, high-fee course funnels, comment-code lead magnets, and past-performance proof. Item `0032` adds a direct group-funnel pattern: the content may present itself as free help or a learning circle, while moving users into off-platform stock consultation and group persuasion.

For the CIB-authorized pilot, false negatives are more costly than explainable false positives at triage. The signal should be preserved when it converges with investment/profit framing, trapped-stock rescue, synchronized operation, private stock consultation, LINE/OpenChat, shorteners, or free guru framing.

## Boundaries

- Ordinary investment groups are not automatically `scam`.
- A shortener alone is not enough for a `scam` label.
- Labeling must be based on the whole collected `thread_item`.
- Do not claim legal fraud determination from this rule.
- Do not store raw URLs, raw handles, screenshots, raw post text, raw reply text, raw external links, or source case IDs in git.

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
