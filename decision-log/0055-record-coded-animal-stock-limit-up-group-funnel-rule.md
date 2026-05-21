# Decision 0055: Record Coded-Animal Stock Limit-Up Group Funnel Rule

## Date

2026-04-25

## Status

Accepted

## Decision

Add `coded_animal_stock_limit_up_group_funnel` as a signal tag and `CODED_ANIMAL_STOCK_LIMIT_UP_GROUP_FUNNEL` as a baseline reason code.

This signal covers animal-coded or otherwise obscured low-price stock lures that promise near-term limit-up or exit timing, say prepared details are available, and gate the details through a group, follow, private message, or `+1` action.

## Trigger

The project owner supplied a confirmed Threads scam pointer for item `0043`. The repo records only the repo-safe rule implication, not the raw URL, raw handle, raw stock names, raw stock codes, raw price values, raw post text, raw replies, screenshot, HTML, or source case ID.

## Rationale

Item `0043` shows a recurring short-term stock-pick funnel variant: the top-level post gives many public stock-specific trading commands and wealth/free-sharing proof, while the continuation/replies tease an obscured animal-coded low-price target with near-term limit-up/exit timing and move readers into a group/private-message action gate.

## Boundaries

- Do not label animal metaphors or casual nicknames as scam-like by themselves.
- The signal requires convergence: coded/obscured stock nickname plus low-price/near-term limit-up or exit claim plus prepared-detail/group/message action gate.
- It is strongest when paired with mass stock-command lists, past-performance proof, private-channel redirect, comment-code lead magnets, or account-level cluster evidence.
- Do not store raw URLs, raw handles, raw stock names, raw stock codes, raw price values, raw post text, raw reply text, screenshots, HTML, or source case IDs in git.

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

Use this rule when a coded or obscured stock nickname is used to sell near-term limit-up/exit certainty through a group or private-message action path.
