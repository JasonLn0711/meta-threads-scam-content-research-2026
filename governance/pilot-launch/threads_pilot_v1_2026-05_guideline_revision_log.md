# Guideline Revision Log: Threads Pilot v1

## Revision Log Identity

| Field | Value |
|---|---|
| Dataset or batch ID | `threads_pilot_v1_2026-05` |
| Annotation guideline version | `v1` |
| Log owner | `annotation_lead_01` |
| Date opened | `2026-04-23` |
| Date closed | `2026-04-23` |

## Revision Candidates

| ID | Date | Source | Guideline section | Problem observed | Proposed change | Severity | Decision | Owner |
|---|---|---|---|---|---|---|---|---|
| `GR-001` | `2026-04-23` | `calibration` | primary-label boundary, finance edge cases | Readable finance discussion was being treated as `uncertain` from topic alone. | Clarify that finance discussion without a funnel, guarantee, redirect, fee, or fake authority stays `non_scam`. | `important` | `accepted` | `annotation_lead_01` |
| `GR-002` | `2026-04-23` | `calibration` | evidence sufficiency, screenshot/OCR edge cases | Annotators downgraded decisive OCR cases because destination or profile context was not captured. | Clarify that decisive OCR can still support `sufficient` evidence and that missing destination/profile context belongs in `missing_evidence`. | `important` | `accepted` | `annotation_lead_01` |
| `GR-003` | `2026-04-23` | `calibration` | signal-tag discipline, pseudo-official reward edge cases | Generic verification wording was being tagged as a credential request without an explicit data ask. | Clarify that `credential_or_personal_data_request` requires an explicit request for login, identity, bank, or other personal details. | `important` | `accepted` | `annotation_lead_01` |
| `GR-004` | `2026-04-23` | `calibration` | annotation confidence guidance | Confidence was drifting toward subtype/tag exact-match expectations rather than core-label agreement. | Clarify that confidence should reflect likely agreement on the main label and reason, not exact subtype/tag overlap. | `minor` | `accepted` | `annotation_lead_01` |
| `GR-005` | `2026-04-25` | `stakeholder_feedback` | signal tags, private-channel funnel edge cases | CIB-confirmed scam exemplar showed investment lure wrapped in other content, with no public LINE/link/site/contact handle, but with a request for users to private-message the poster so the scam contact route can be sent in DM. | Add `implicit_dm_contact_request`; clarify that hidden-DM funnels can support escalation when combined with investment/profit or other scam-like signals. | `important` | `accepted` | `annotation_lead_01` |
| `GR-006` | `2026-04-25` | `stakeholder_feedback` | signal tags, course/membership funnel edge cases | Confirmed scam pointer showed a trading or financial-education brand narrative where high-fee course and guarantee/profit disputes were visible in selected replies/comments. | Add `high_fee_course_or_membership_funnel`; clarify that high-fee education is not automatically scam, but becomes review-worthy when paired with financial outcome, guarantee, private contact, payment, testimonial, or reply-dispute evidence. | `important` | `accepted` | `annotation_lead_01` |
| `GR-007` | `2026-04-25` | `stakeholder_feedback` | signal tags, comment-code lead magnet edge cases | Confirmed scam pointer showed a finance/authority-hype top-level post where the author's reply used a follow/code/free-receive instruction as the conversion signal. | Add `comment_code_lead_magnet`; clarify that comment-code prompts become review-worthy when paired with investment/profit framing, target-price claims, fake authority, named stock picks, or suspicious reply context. | `important` | `accepted` | `annotation_lead_01` |
| `GR-008` | `2026-04-25` | `stakeholder_feedback` | signal tags, past-performance proof edge cases | Confirmed scam pointer showed a stock-pick post using past recommendations, limit-up percentages, wealth-result claims, and free-sharing guru framing to establish investment authority. | Add `past_performance_profit_proof`; clarify that past performance proof becomes review-worthy when paired with stock-pick authority, wealth-result claims, free-sharing guru framing, or later conversion signals. | `important` | `accepted` | `annotation_lead_01` |
| `GR-009` | `2026-04-25` | `stakeholder_feedback` | signal tags, stock-rescue group funnel edge cases | Confirmed scam pointer showed a free stock community lure offering trapped-position help, synchronized operation, and LINE/OpenChat or shortener-based community access. | Add `stock_rescue_group_funnel`; clarify that stock-rescue/free-group offers become review-worthy when paired with investment framing, private stock consultation, LINE/OpenChat, shorteners, or free guru framing. | `important` | `accepted` | `annotation_lead_01` |
| `GR-010` | `2026-04-25` | `stakeholder_feedback` | signal tags, reply-level individual stock advice edge cases | Confirmed scam pointer showed a prediction-accuracy post whose replies contain repeated user stock questions and author buy/hold/add/wait style answers, plus group-join context. | Add `individual_stock_advice_reply_funnel`; clarify that repeated individualized stock advice in replies becomes review-worthy when paired with prediction-proof, profit framing, group joins, or private-channel signals. | `important` | `accepted` | `annotation_lead_01` |
| `GR-011` | `2026-04-25` | `stakeholder_feedback` | signal tags, herding chorus edge cases | Confirmed scam pointer showed a strong full-position/bullish market-direction call and a reply chorus of users saying they bought, added, held, refilled, or followed along. | Add `market_direction_herding_chorus`; clarify that strong market-direction calls become review-worthy when paired with visible follower action-taking chorus or other funnel signals. | `important` | `accepted` | `annotation_lead_01` |

## Common Sources

Use one of:

- `calibration`
- `pilot_annotation`
- `second_review`
- `adjudication`
- `dataset_audit`
- `baseline_error_analysis`
- `stakeholder_feedback`

## Severity Guide

| Severity | Meaning |
|---|---|
| `blocker` | Annotation cannot proceed consistently without the change. |
| `important` | The issue affects repeated cases or high-risk decisions. |
| `minor` | Wording cleanup or example improvement. |
| `defer` | Valid issue, but not needed for the current pilot. |

## Revision Decision Rules

Accept a revision when:

- the same disagreement appears more than once
- annotators consistently confuse two labels or signal tags
- a definition causes over-labeling of legitimate content
- a definition causes missing obvious high-risk content
- the current wording creates privacy or overclaiming risk

Defer a revision when:

- the issue depends on evidence not approved for phase 1
- the issue is about rare future modalities such as long video
- the change would add complexity before the 50-item pilot proves it is needed

## Accepted Revision Summary

| Revision ID | Accepted change | File to update | Completed? | Notes |
|---|---|---|---|---|
| `GR-001` | Finance discussion without a conversion step stays `non_scam`. | `docs/06-annotation-guideline-v1.md` | yes | Also reflected in synthetic answer-key rows for `threads-synth-v1-0004`. |
| `GR-002` | Decisive OCR can remain `sufficient` evidence; missing destination/profile context goes in `missing_evidence`. | `docs/06-annotation-guideline-v1.md` | yes | Reinforced in rehearsal watchlist and QA checklist. |
| `GR-003` | Generic verification wording alone does not justify `credential_or_personal_data_request`. | `docs/06-annotation-guideline-v1.md` | yes | Also reflected in synthetic answer-key row for `threads-synth-v1-0005`. |
| `GR-004` | Confidence should track likely agreement on the core label and reason. | `docs/06-annotation-guideline-v1.md` | yes | Reinforced in the controlled rehearsal checklist. |
| `GR-005` | Public DM/private-message requests can be a funnel signal even when public contact details are withheld. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json` | yes | Full raw exemplar URL and handle are not stored in git. Baseline reason code added as `IMPLICIT_DM_CONTACT_REQUEST`. |
| `GR-006` | High-fee trading or financial-education funnels become review-worthy when paired with financial outcome, guarantee, private-contact, payment, testimonial, or reply-dispute evidence. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json` | yes | Full raw exemplar URL and handle are not stored in git. Baseline reason code added as `HIGH_FEE_COURSE_FUNNEL`. |
| `GR-007` | Comment-code or keyword lead magnets in replies become review-worthy when paired with investment/profit framing, fake authority, target-price claims, named stock picks, or suspicious reply context. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json` | yes | Full raw exemplar URL and handle are not stored in git. Baseline reason code added as `COMMENT_CODE_LEAD_MAGNET`. |
| `GR-008` | Past stock-pick performance, limit-up screenshots, and wealth-result claims become review-worthy when used to establish investment authority or future-pick trust. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json` | yes | Full raw exemplar URL and handle are not stored in git. Baseline reason code added as `PAST_PERFORMANCE_PROFIT_PROOF`. |
| `GR-009` | Stock-rescue, synchronized-operation, or free stock-community offers become review-worthy when paired with LINE/OpenChat, shorteners, private stock consultation, or free guru framing. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json` | yes | Full raw exemplar URL and handle are not stored in git. Baseline reason code added as `STOCK_RESCUE_GROUP_FUNNEL`. |
| `GR-010` | Repeated individualized stock buy/hold/add/wait/sell guidance in replies becomes review-worthy when paired with prediction-proof, profit framing, group joins, or private-channel signals. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json` | yes | Full raw exemplar URL and handle are not stored in git. Baseline reason code added as `INDIVIDUAL_STOCK_ADVICE_REPLY_FUNNEL`. |
| `GR-011` | Strong market-direction calls become review-worthy when paired with visible buy/add/hold/refill/following chorus or other funnel signals. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json` | yes | Full raw exemplar URL and handle are not stored in git. Baseline reason code added as `MARKET_DIRECTION_HERDING_CHORUS`. |
| `GR-012` | Confirmed-pointer intake should capture top-level poster Threads ID/profile context in controlled storage, with only redacted references and category signals in repo-safe records. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json`, `data-contracts/thread_item_schema_v1.json` | yes | Poster identity context supports dedupe and repeat-source review, but is not a standalone scam label and does not authorize profile graph capture. |
| `GR-013` | CIB-detected accounts may be sampled with a small fixed candidate window to find multi-post scam-like style clusters before selecting individual posts for full-thread capture. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json`, `data-contracts/thread_item_schema_v1.json` | yes | Account-level cluster evidence is a candidate-selection and context method, not a standalone label for every post under the account. |
| `GR-014` | Institutional-flow, foreign-investor, futures/spot, or macro-event authority cues become review-worthy when used to justify strong trading action and paired with proof, herding, or follower reassurance. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json`, `data-contracts/thread_item_schema_v1.json` | yes | Full raw exemplar URL and handle are not stored in git. Baseline reason code added as `INSTITUTIONAL_FLOW_AUTHORITY_LURE`. |
| `GR-015` | CIB-detected account samples may record repo-safe posting cadence and candidate-density metadata to prioritize follow-up full-thread capture. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json`, `data-contracts/thread_item_schema_v1.json` | yes | Cadence is prioritization context, not a standalone scam label, and does not authorize continuous monitoring or follower/following graph capture. |
| `GR-016` | Reply-level impersonation/contact hijack becomes review-worthy when replies certify or ride on poster identity and redirect readers to LINE/contact/group paths. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json`, `data-contracts/thread_item_schema_v1.json` | yes | Preserve attribution uncertainty; raw contact handles, raw reply text, and raw account identifiers stay outside git. Baseline reason code added as `REPLY_IMPERSONATION_CONTACT_HIJACK`. |
| `GR-017` | Short-term stock-pick playbook funnels become review-worthy when a named pick, FOMO/strong-outcome framing, and follow/message/code action gate converge. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json`, `data-contracts/thread_item_schema_v1.json` | yes | Full raw exemplar URL, handle, stock text, and replies are not stored in git. Baseline reason code added as `STOCK_PICK_PLAYBOOK_KEYWORD_FUNNEL`. |
| `GR-018` | Trapped-position or loss-anxiety replies become review-worthy when they are moved into DM/private detailed operation playbook guidance. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json`, `data-contracts/thread_item_schema_v1.json` | yes | Full raw exemplar URL, handle, stock text, and replies are not stored in git. Baseline reason code added as `TRAPPED_POSITION_DM_PLAYBOOK_REPLY`. |
| `GR-019` | Lifestyle/travel/warmth framing becomes review-worthy when it reassures market fear and steers buy/hold/add behavior inside a broader lure or contact-hijack thread. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json`, `data-contracts/thread_item_schema_v1.json` | yes | Full raw exemplar URL, handle, post text, replies, and contact handles are not stored in git. Baseline reason code added as `LIFESTYLE_TRUST_MARKET_REASSURANCE_FUNNEL`. |
| `GR-020` | Hidden or dark-horse stock target-price lures become review-worthy when catalyst claims and urgency are gated behind follow/message/code/private-share action. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json`, `data-contracts/thread_item_schema_v1.json` | yes | Full raw exemplar URL, handle, stock names, price/target values, code text, post text, and replies are not stored in git. Baseline reason code added as `DARK_HORSE_STOCK_TARGET_PRICE_DM_FUNNEL`. |
| `GR-021` | Mass stock buy/sell/limit-up command lists become review-worthy when they convert readers into daily signal groups, free-sharing funnels, or entry quotas. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json`, `data-contracts/thread_item_schema_v1.json` | yes | Full raw exemplar URL, handle, stock names, stock codes, price values, post text, and replies are not stored in git. Baseline reason code added as `MASS_STOCK_COMMAND_LIST_GROUP_FUNNEL`. |
| `GR-022` | Animal-coded or obscured low-price stock lures become review-worthy when near-term limit-up/exit claims are gated behind group/follow/message action. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json`, `data-contracts/thread_item_schema_v1.json` | yes | Full raw exemplar URL, handle, stock names, stock codes, price values, code text, post text, and replies are not stored in git. Baseline reason code added as `CODED_ANIMAL_STOCK_LIMIT_UP_GROUP_FUNNEL`. |
| `GR-023` | Wealth/experience authority plus trading-rule checklists become review-worthy when paired with like/follow/`+1`/get-on-board action gating. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json`, `data-contracts/thread_item_schema_v1.json` | yes | Full raw exemplar URL, handle, raw post text, raw replies, and engagement details are not stored in git. Baseline reason code added as `TRADING_RULES_WEALTH_AUTHORITY_FOLLOW_GATE`. |
| `GR-024` | Major-brand, patent, order-backlog, or catalyst authority plus extreme ROI claims become review-worthy when paired with contact/private-message or like/follow/`+1` gating. | `docs/06-annotation-guideline-v1.md`, `docs/04-taxonomy.md`, `docs/30-annotator-onboarding-quickstart.md`, `data-contracts/labeling_schema_v1.json`, `data-contracts/thread_item_schema_v1.json` | yes | Full raw exemplar URL, handle, stock names, stock codes, brand names, price values, contact ID, raw post text, and replies are not stored in git. Baseline reason code added as `BRAND_PATENT_EXTREME_ROI_CONTACT_FUNNEL`. |

## Supporting Records

- `../../experiments/evaluation-notes/0012-synthetic-calibration-guideline-revision.md`
- `../../experiments/evaluation-notes/0013-controlled-rehearsal-boundary-watchlist.md`
- `../../templates/manual_collection_rehearsal_checklist.md`
- `../../templates/annotation_qa_checklist.md`

## Post-Revision Checks

After accepted changes:

- update `docs/06-annotation-guideline-v1.md`
- update `docs/04-taxonomy.md` if subtype or signal-tag vocabulary changes
- update `data-contracts/labeling_schema_v1.json` if valid values change
- update templates if new required fields or values are introduced
- record a decision-log entry for material taxonomy or label changes
- rerun calibration if the change affects primary labels or risk levels

Status for this revision set:

- `docs/06-annotation-guideline-v1.md` updated: yes
- vocabulary change requiring taxonomy/schema update: no
- onboarding and QA templates updated: yes
- synthetic calibration answer key aligned: yes
- mandatory taxonomy decision-log entry required: no
- rerun before real items required: only if annotator team changes or the same boundary fails again on real governed rehearsal items
