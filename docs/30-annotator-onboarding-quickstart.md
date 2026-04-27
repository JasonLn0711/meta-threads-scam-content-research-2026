# Annotator Onboarding Quickstart

## Purpose

This quickstart is the minimum practical onboarding path for anyone labeling Threads `thread_item` records in the phase-1 scam-content pilot.

It is intentionally shorter than the full annotation guideline. Annotators should use this as a desk reference, then consult `docs/06-annotation-guideline-v1.md` for edge cases.

## Before You Annotate

You must have:

- read `docs/06-annotation-guideline-v1.md`
- read the edge-case sections for finance, recruitment, giveaways, health, celebrity references, screenshots, and incomplete posts
- completed the synthetic or redacted calibration exercise
- been assigned a pseudonymous annotator ID such as `ann_01`
- confirmed that the annotation file is in an approved local-only location under `data/interim/`
- confirmed that raw screenshots, source packets, or sensitive evidence are not in git

If any of these are missing, pause and ask the project owner.

## The Unit You Label

Label one `thread_item` at a time.

A `thread_item` can include:

- original post text
- selected replies/comments
- OCR text from image or screenshot content
- visible links
- visible contact handles
- visible redirection signals
- approved poster identity/profile context fields
- evidence-status and redaction notes

Do not add outside research unless the collection protocol explicitly provided it. Label only the evidence in the row and attached approved context.

## Primary Label Decision

Use one primary `scam_label`.

| Label | Use when |
|---|---|
| `scam` | Observable evidence strongly supports a scam-like lure, deceptive persuasion, suspicious redirect, fake authority, payment/credential ask, or fraud-like setup. |
| `non_scam` | The item is ordinary conversation, legitimate marketing, education, commentary, satire, news, or benign opinion with no meaningful scam-like signal. |
| `uncertain` | Suspicious signals exist, but evidence is mixed, context is missing, or a legitimate explanation remains plausible. |
| `insufficient_evidence` | The item cannot be reviewed meaningfully because required text, OCR, image, link, or context is missing or unreadable. |

Quick test:

```text
Can I write "The item shows..." and name visible evidence?
```

If yes and the evidence is strong, use `scam`. If the note is mostly "it feels suspicious," use `uncertain` or `insufficient_evidence`.

## Risk Level

| Risk | Use when |
|---|---|
| `high` | Multiple reinforcing signals or severe harm signals are visible. |
| `medium` | Some scam-like signals are present but evidence is mixed or incomplete. |
| `low` | No meaningful scam-like signal, weak signal only, or not enough reviewable evidence. |

Risk is triage priority, not a legal conclusion.

## Evidence Sufficiency

| Value | Use when |
|---|---|
| `sufficient` | The available evidence supports the label. |
| `partial` | Enough evidence exists for a tentative label, but important context is missing. |
| `insufficient` | Evidence is too incomplete for confidence, but some content is visible. |
| `not_reviewable` | The item cannot be reviewed because the capture is missing, unreadable, broken, or out of scope. |

Do not confuse low confidence with insufficient evidence. If the row has enough evidence to make a cautious judgment, use `uncertain` plus low confidence rather than `insufficient_evidence`.

## Confidence

| Value | Use when |
|---|---|
| `high` | Another trained annotator would probably choose the same label. |
| `medium` | The label is reasonable but depends on interpretation. |
| `low` | The evidence is weak, ambiguous, low quality, or likely to cause disagreement. |

Low confidence is useful. It routes cases to review.

## Signal Tags

Choose only tags supported by visible evidence. Use `none` only when no signal applies.

High-value tags to watch:

- `guaranteed_or_risk_free_claim`
- `unrealistic_profit_or_benefit`
- `past_performance_profit_proof`
- `high_fee_course_or_membership_funnel`
- `stock_rescue_group_funnel`
- `individual_stock_advice_reply_funnel`
- `market_direction_herding_chorus`
- `institutional_flow_authority_lure`
- `lifestyle_trust_market_reassurance_funnel`
- `account_multi_post_style_cluster`
- `account_posting_cadence_metadata`
- `poster_identity_context`
- `private_channel_redirect`
- `implicit_dm_contact_request`
- `comment_code_lead_magnet`
- `stock_pick_playbook_keyword_funnel`
- `trapped_position_dm_playbook_reply`
- `dark_horse_stock_target_price_dm_funnel`
- `coded_animal_stock_limit_up_group_funnel`
- `mass_stock_command_list_group_funnel`
- `reply_impersonation_contact_hijack`
- `visible_external_link`
- `contact_handle_visible`
- `pseudo_official_language`
- `urgency_or_scarcity`
- `testimonial_or_earnings_screenshot`
- `payment_deposit_or_fee_request`
- `credential_or_personal_data_request`
- `reply_only_lure`
- `ocr_only_lure`

Signal tags are evidence features. They do not automatically determine the label.

For confirmed investment-scam pointers, pay special attention to combinations: prior named stock wins, limit-up or percentage proof, screenshot-style profit tables, luxury-result claims, and "no fee / already financially free / just sharing or making friends" language together can be a high-risk trust funnel. The no-fee language may reduce suspicion rather than reduce risk.

## Required Note Style

Write short, evidence-based notes.

Use:

```text
Evidence observed: OCR says "guaranteed daily profit" and reply redirects to Telegram.
Missing evidence: link destination not captured.
Reason for uncertainty: endorsement cannot be verified from collected item alone.
```

Avoid:

```text
Looks bad.
Definitely criminal.
Fake for sure.
I know this account is suspicious.
```

## When To Send To Review

Set `review_status` to `needs_second_review` when:

- `scam_label` is `scam` and `risk_level` is `high`
- `scam_label` is `uncertain`
- `annotation_confidence` is `low`
- `evidence_sufficiency` is `partial`, `insufficient`, or `not_reviewable`
- the item depends mainly on OCR-only or reply-only evidence
- you are unsure whether the item is aggressive legal marketing or scam-like
- the item relies on past stock-pick performance, limit-up screenshots, or wealth-result claims to establish investment authority
- the item offers trapped-stock rescue, synchronized operation, or a free stock community with a LINE/OpenChat, shortener, private-message, or off-platform group path
- the author repeatedly gives individualized stock buy/hold/add/wait/sell guidance in replies while group, profit, or private-channel signals are present
- the author makes a strong market-direction call and the reply thread shows multiple users echoing buy/add/hold/refill/following behavior
- institutional-flow, foreign-investor, futures/spot, or macro-event numbers are used to make a strong trading action feel safe or inevitable
- lifestyle/travel/warmth framing reassures readers during market fear while steering buy/hold/add behavior
- a controlled account-level sample finds two or more scam-like style families across multiple posts/replies from the same approved account
- a controlled account-level sample shows recent posting density or repeated candidate-post timing that helps prioritize full-thread capture
- poster identity/profile context links the item to repeat-source, profile-level redirect, investment identity, authority/guru, or stock-picking positioning evidence
- the item asks users to private-message the poster for investment/profit-related details while public contact details are absent
- an author reply asks users to follow, comment a code, or use a keyword to receive investment/profit-related material
- a named short-term stock pick is paired with FOMO and a follow/message/code gate for a complete operation playbook
- wealth or long-experience authority plus a trading-rule list is paired with like/follow/`+1`/get-on-board action gating
- major-brand/patent/catalyst authority plus extreme small-stake-to-large-return claims are paired with contact/private-message gating
- a trapped-position or loss-anxiety reply is moved into private message or detailed operation playbook guidance
- replies appear to impersonate/certify a poster identity and redirect readers to LINE/contact/group paths
- a high-fee trading or investment course funnel is paired with guaranteed-profit, private-contact, payment, testimonial, or reply-context dispute evidence

## Common Mistakes

| Mistake | Correct approach |
|---|---|
| Labeling all finance content as `scam` | Require visible guarantee, fake authority, private redirect, payment/credential ask, or suspicious testimonial. |
| Treating every past-performance post as scam | Past performance becomes review-worthy when it is used as proof of the poster's authority and converges with strong gain claims, guru framing, free-sharing lures, or conversion signals. |
| Treating every stock community as scam | A group becomes review-worthy when it promises trapped-stock rescue, synchronized operation, free stock help, or portfolio advice while moving users to LINE/OpenChat, a shortener, or private contact. |
| Treating every stock Q&A reply as scam | Individual reply advice becomes review-worthy when it repeats across users and converges with prediction-proof, profit, group, or private-channel signals. |
| Treating every bullish/bearish opinion as scam | Market-direction herding requires both a strong call and visible follower chorus or action-taking context. |
| Treating ordinary macro commentary as scam | Institutional-flow authority matters when external market data is used to push strong trading action and converges with other lure signals. |
| Treating lifestyle posts as scam | Lifestyle trust matters only when it reinforces market reassurance, trading instruction, or funnel behavior. |
| Treating every post under a detected account as scam | Account-level clustering helps find candidates; each selected post still needs item-level evidence. |
| Treating high posting frequency as scam | Cadence metadata is prioritization context; it needs scam-like content signals or CIB/stakeholder confirmation. |
| Treating poster Threads ID as a label | Poster identity is context for dedupe and repeat-source review; it must reinforce item evidence and should be redacted in git. |
| Using `uncertain` for unreadable records | Use `insufficient_evidence` when the item cannot be reviewed. |
| Treating any link as malicious | Record `visible_external_link`, but label based on surrounding evidence. |
| Treating a missing public LINE/link as automatically benign | Check whether the post or replies ask users to DM for investment/profit details; use `implicit_dm_contact_request` when visible. |
| Treating every comment-code prompt as scam | A code/keyword prompt is review-worthy when it converges with investment/profit framing, stock picks, fake authority, target-price claims, or suspicious reply context. |
| Treating every named stock pick as scam | Stock-pick playbook funnels require FOMO or strong outcome framing plus a follow/message/code action gate. |
| Treating every trading-rule checklist as scam | Trading-rule authority funnels require wealth/experience authority plus an action gate for follow-up stock help. |
| Treating every company-news catalyst as scam | Brand/patent catalyst funnels require extreme ROI framing plus contact or action-gated follow-up. |
| Treating every loss question as scam | Trapped-position risk matters when the answer moves into private guidance or a playbook funnel. |
| Assuming suspicious replies are authored by the poster | Record attribution uncertainty. Reply-level impersonation/contact hijack can still create thread-level scam risk. |
| Treating all paid education as benign or all expensive courses as scams | Look for the whole pattern: price, financial outcome claims, private contact, testimonials, payment path, and reply-context disputes. |
| Overusing signal tags | Use tags only for visible evidence. Do not infer hidden intent. |
| Forgetting missing evidence | Fill `missing_evidence` when OCR, link, image, or context is absent. |
| Making legal claims | Use research labels only; do not claim criminal fraud. |

## End-Of-Session Check

Before handing off your annotation file:

- every row has one `scam_label`
- every row has one `risk_level`
- every row has one `evidence_sufficiency`
- every row has one `annotation_confidence`
- `signal_tags` is not blank
- poster identity/profile fields are filled when the run record authorized capture
- `annotation_notes` explains the strongest evidence or uncertainty
- high-risk, uncertain, low-confidence, and partial-evidence items are marked for review
- no raw personal data was pasted into notes
