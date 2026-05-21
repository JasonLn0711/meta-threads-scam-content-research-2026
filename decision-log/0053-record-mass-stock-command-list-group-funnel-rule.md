# Decision 0053: Record Mass Stock-Command List Group Funnel Rule

## Date

2026-04-25

## Status

Accepted

## Decision

Add `mass_stock_command_list_group_funnel` as a signal tag and `MASS_STOCK_COMMAND_LIST_GROUP_FUNNEL` as a baseline reason code.

This signal covers mass stock buy, sell, exit, get-on/get-off, or limit-up command lists that claim accurate stock calls or free sharing and convert readers into a daily stock-signal group, quota, follow/comment action, or similar funnel.

## Trigger

The project owner supplied a confirmed Threads scam pointer for item `0041`. The repo records only the repo-safe rule implication, not the raw URL, raw handle, raw stock names, raw stock codes, raw price values, raw post text, raw replies, screenshot, HTML, or source case ID.

## Rationale

Item `0041` shows a public mass command-list pattern: many stock-specific entry/exit or strong-outcome instructions are paired with claimed call accuracy and a free daily group or quota conversion path. This differs from a single stock-pick playbook and from a hidden dark-horse target-price lure.

## Boundaries

- Do not label ordinary watchlists, ordinary portfolio notes, or ordinary market commentary as scam-like by themselves.
- The signal requires convergence: mass stock command list plus claimed accuracy/free sharing plus group/quota/follow-comment conversion.
- It is strongest when paired with private-channel redirect, comment-code lead magnets, past-performance proof, guaranteed/limit-up claims, urgency, or account-level cluster evidence.
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

Use this rule when a mass stock command list is used as proof and pressure before moving readers into a daily signal group, quota, or free-sharing action gate.
