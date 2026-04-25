# Decision 0057: Record Brand/Patent Extreme-ROI Contact-Funnel Rule

## Status

Accepted.

## Decision

Add `brand_patent_extreme_roi_contact_funnel` as a signal tag and `BRAND_PATENT_EXTREME_ROI_CONTACT_FUNNEL` as a baseline reason code.

This signal covers investment posts that combine:

- major-brand, patent, order-backlog, exclusive-technology, or catalyst authority;
- extreme small-stake-to-large-return or unusually high target-price framing;
- contact/private-message, like/follow, `+1`, or similar action-gated follow-up.

## Context

Confirmed pointer `0045` shows a dense investment scam-like pattern: many stock-specific buy/target instructions, a loss-rescue hook, extreme ROI framing, major-brand/patent/catalyst authority, a visible contact route, and author replies reinforcing private follow-up and testimonial proof.

Existing `dark_horse_stock_target_price_dm_funnel` and `mass_stock_command_list_group_funnel` partly cover the case, but this decision records the narrower authority package: brand/patent/catalyst claims plus extreme ROI and contact gating.

## Boundaries

- Do not use this rule for ordinary company news, analyst target-price discussion, technology-sector commentary, or patent/order announcements.
- The rule requires convergence: catalyst authority plus extreme ROI framing plus contact/action-gated follow-up.
- Raw URL, raw handle, stock names, stock codes, brand names, price values, visible contact ID, post text, replies, screenshots, and browser artifacts remain in the controlled store only.

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

Future confirmed pointers can identify this high-risk authority package without storing sensitive raw evidence in git and without overgeneralizing legitimate catalyst or company-news discussion.
