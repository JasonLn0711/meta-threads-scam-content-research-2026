# Taxonomy

## Label Philosophy

The taxonomy is designed for research triage. It captures observable Threads scam-content signals and uncertainty without claiming legal guilt, platform-policy violation, or actor intent.

The authoritative v1 label vocabulary is also recorded in:

```text
data-contracts/labeling_schema_v1.json
```

## Scam Label

| Label | Meaning |
|---|---|
| `scam` | The item contains enough observable scam-like signals to merit scam-risk review. |
| `non_scam` | The item does not show scam-like signals under the v1 guideline. |
| `uncertain` | Some signals are present, but evidence is mixed or context is missing. |
| `insufficient_evidence` | The available item cannot be judged from the captured evidence. |

## Scam Type

| Type | Description |
|---|---|
| `investment_lure` | Claims or implies investment opportunity, trading profit, crypto gain, loan, grant, or financial return. |
| `guaranteed_profit_claim` | Uses guaranteed, risk-free, fixed-return, or unusually high outcome language. |
| `fake_endorsement` | Appears to rely on celebrity, expert, government, media, brand, or institutional endorsement without clear support. |
| `redirect_to_private_chat` | Pushes users toward private messaging, groups, unofficial accounts, or off-platform contact. |
| `impersonation_pseudo_official` | Uses names, logos, language, or format that suggests official status. |
| `urgency_scarcity_pressure` | Uses limited time, act now, fear, scarcity, or pressure tactics. |
| `suspicious_testimonial` | Uses unverifiable success stories, before-after claims, message screenshots, or fabricated-looking proof. |
| `recruitment_side_hustle_lure` | Promises easy work, passive income, task pay, or unrealistic compensation. |
| `suspicious_crypto_trading_lure` | Crypto, wallet, exchange, token, mining, or trading-signal lure with suspicious persuasion signals. |
| `medical_health_miracle_claim` | Makes suspicious health, cure, treatment, or miracle claims tied to payment or redirection. |
| `giveaway_reward_prize_lure` | Promises prizes, rewards, giveaways, grants, subsidies, or benefits with suspicious requirements. |
| `other_high_risk_persuasion` | High-risk fraud-like persuasion not captured by the listed categories. |
| `none` | No scam subtype applies. |

Multiple types may apply, but over-selection is a taxonomy warning sign. Most items should not need more than three or four subtypes.

## Signal Tags

| Signal | Examples |
|---|---|
| `unrealistic_profit_or_benefit` | Large money, health, job, prize, or status benefit. |
| `guaranteed_or_risk_free_claim` | Guaranteed return, no-risk, daily income, fixed ROI. |
| `past_performance_profit_proof` | Past stock picks, hit-rate, limit-up, profit table, or wealth-result claims used as proof. |
| `high_fee_course_or_membership_funnel` | High-fee course, academy, membership, coaching, or trading-education funnel tied to financial outcomes. |
| `stock_rescue_group_funnel` | Stock-rescue, trapped-position help, synchronized-trading, or free stock-community funnel. |
| `individual_stock_advice_reply_funnel` | Reply/comment thread gives individualized buy, hold, add, wait, or sell guidance on specific stocks. |
| `market_direction_herding_chorus` | Strong market-direction call plus reply chorus of buying, adding, holding, or following. |
| `institutional_flow_authority_lure` | Institutional flow, foreign-investor data, macro-event framing, or market-wide authority cues justify a strong trading action. |
| `lifestyle_trust_market_reassurance_funnel` | Lifestyle/travel/warmth framing builds trust while market fear is redirected into buy/hold/add guidance. |
| `account_multi_post_style_cluster` | Same approved account shows multiple scam-like persuasion styles across several posts/replies. |
| `account_posting_cadence_metadata` | Controlled account sample includes repo-safe posting cadence or feed-density metadata for prioritization. |
| `poster_identity_context` | Poster Threads ID or profile context is captured as controlled evidence for dedupe, repeat-source review, or profile-level funnel context. |
| `private_channel_redirect` | DM me, join group, contact assistant, LINE/WhatsApp/Telegram handle. |
| `implicit_dm_contact_request` | Public post or reply asks users to private-message the poster, even when no LINE/link/site/contact handle is visible. |
| `comment_code_lead_magnet` | Reply/comment asks users to follow, comment, or use a code/keyword to receive stock picks, methods, lists, or other benefits. |
| `stock_pick_playbook_keyword_funnel` | Named short-term stock-pick lure offers a complete operation script/playbook through follow, message, or numeric-code action. |
| `hidden_stock_code_past_performance_lure` | Prior stock-pick performance proof teases an unnamed next stock/code as a high-value urgent opportunity. |
| `trapped_position_dm_playbook_reply` | Reply-level trapped-position or loss-anxiety cue is moved into DM/private playbook guidance. |
| `dark_horse_stock_target_price_dm_funnel` | Hidden or dark-horse stock target-price lure uses catalyst, urgency, and follow/message/code/private-share gating. |
| `coded_animal_stock_limit_up_group_funnel` | Animal-coded or obscured low-price stock lure promises near-term limit-up/exit timing and gates details through group/follow/message action. |
| `mass_stock_command_list_group_funnel` | Mass stock buy/sell/limit-up command list converts readers into a daily stock-signal group, quota, or free-sharing funnel. |
| `supply_chain_insider_stock_lure` | Claimed insider, procurement, supplier, or confidential corporate-meeting access justifies a specific stock opportunity. |
| `reply_impersonation_contact_hijack` | Replies appear to impersonate, certify, or ride on the poster's identity to redirect readers to LINE/contact/group paths. |
| `visible_external_link` | Visible URL, link text, shortener, landing-page reference. |
| `suspicious_domain_or_shortener` | Mismatched URL, vague domain, shortened link, disguised link text. |
| `contact_handle_visible` | Contact handle, phone, email, messaging ID. |
| `celebrity_or_public_figure_reference` | Celebrity, professor, public figure, influencer, politician. |
| `brand_or_institution_reference` | Brand, school, exchange, bank, hospital, government, news organization. |
| `pseudo_official_language` | Official-looking notice, support account, verification, subsidy, approval language. |
| `urgency_or_scarcity` | Limited slots, today only, last chance, immediate action. |
| `testimonial_or_earnings_screenshot` | Screenshots of earnings, testimonials, message screenshots, success stories. |
| `payment_deposit_or_fee_request` | Deposit, fee, wallet address, card setup, shipping fee. |
| `credential_or_personal_data_request` | Login, verification, account, bank, identity, or personal data request. |
| `reply_only_lure` | Suspicious signal appears mainly in replies/comments. |
| `ocr_only_lure` | Suspicious signal appears mainly in image OCR. |
| `vague_offer_strong_benefit` | Vague details but strong promised benefit. |
| `medical_cure_or_miracle_claim` | Cure, miracle, guaranteed health result, unsupported treatment claim. |
| `giveaway_reward_or_prize_claim` | Prize, reward, grant, subsidy, lottery, giveaway claim. |
| `recruitment_or_easy_income_claim` | Easy job, task work, passive income, fast side-hustle claim. |
| `none` | No signal applies. |

Signal tags are evidence features. They do not automatically determine the label.

## Content Form

Phase-1 content forms:

- `text_post`
- `text_image_post`
- `reply`
- `comment`
- `image_ocr`
- `screenshot_ocr`
- `external_link`
- `mixed_thread_context`

Long video, heavy video understanding, deepfake detection, account graph analysis, and broad cross-platform integration are deferred.

## Evidence Type

- `direct_text`: signal appears in post or comment text.
- `reply_comment_context`: signal appears in selected replies/comments, including links, contact handles, private-channel migration, add-friend instructions, wallet/deposit/payment instructions, or suspicious domains.
- `ocr_text`: signal appears in extracted image text.
- `visible_link`: signal appears in URL, domain, or visible link text.
- `redirection_instruction`: signal appears as an instruction to move elsewhere.
- `poster_identity_context`: controlled poster ID/profile context is used for dedupe, repeat-source analysis, or profile-level funnel context.
- `account_multi_post_context`: several posts/replies under the same approved account show complementary scam-like styles that help select candidates or interpret repeat-source behavior.
- `account_cadence_context`: account-level feed timing, visible post density, and candidate-post cadence metadata help prioritize which account or post receives full-thread review next.
- `contextual_pattern`: signal depends on a combination of post, replies, image, OCR, or visible link evidence.
- `reviewer_observation`: reviewer notes a visual or contextual pattern not captured by text.

## Explainable Reasons

Each `scam` or `uncertain` label should include at least one evidence-based reason, such as:

- "Promises guaranteed profit."
- "Uses past stock-pick performance, limit-up screenshots, or wealth-result claims as proof."
- "Offers free trapped-stock rescue or synchronized operation through a stock group or community."
- "Uses reply-thread individual stock advice to build authority and move users toward a group or private funnel."
- "Uses strong buy/hold/add market-direction calls and follower chorus to create herd pressure."
- "Uses institutional-flow, foreign-investor, or macro-event numbers as authority for strong buy/hold/do-long action."
- "Uses lifestyle warmth or parasocial trust to reassure readers during market fear and steer them toward buy/hold/add behavior."
- "Same poster or profile context links multiple confirmed scam-like pointers or shows profile-level funnel cues."
- "Same approved account shows multiple posts/replies with complementary lure styles, such as performance proof, group/sync framing, strong market-direction calls, or individualized operation language."
- "Controlled account feed shows high posting density or repeated recent candidate posts, which supports prioritizing the account for item-level review."
- "Redirects user to private messaging channel."
- "Requests private messages as the conversion path while withholding public contact details."
- "Uses a comment-code or keyword lead magnet to move readers from public hype into a follow-up funnel."
- "Uses a named stock-pick, FOMO, and numeric-code/action gate to deliver a complete operation script."
- "Uses prior buy/sell or stock-pick performance proof, then teases an unnamed next stock/code with catalyst or technical claims and urgent buying pressure."
- "Uses an animal-coded or obscured low-price stock name with near-term limit-up/exit claims and group/private-message gating."
- "Uses wealth or long-experience authority plus a trading-rule list, then gates follow-up stock help behind like/follow/`+1`/get-on-board action."
- "Uses major-brand, patent, order-backlog, or catalyst authority plus extreme small-stake-to-large-return claims and contact/private-message gating."
- "Uses claimed insider, procurement, supplier, or confidential corporate-meeting access plus major-brand authority, exclusive-supplier framing, exact price/position cues, or all-in buying behavior."
- "Moves a trapped-position or loss-anxiety reply into private detailed operation guidance."
- "Reply thread contains apparent impersonation or contact hijack that redirects readers to a group/contact path while claiming other contacts are scams."
- "Uses a high-fee trading course or membership funnel around financial outcomes."
- "Uses suspicious testimonial screenshot."
- "Claims official or celebrity association without evidence."
- "Post text is vague, but replies contain contact instructions."
- "Top-level post is benign, but selected replies contain suspicious links or private-channel migration."
- "Anti-scam wording appears together with investment/profit funnel signals."
- "OCR reveals a financial lure not present in visible post text."

## Uncertainty States

| State | Use when |
|---|---|
| `clear` | Evidence strongly supports the label. |
| `mixed_signals` | Both legitimate and suspicious signals appear. |
| `missing_context` | The item may require thread, account, or link context not available. |
| `low_quality_capture` | OCR, screenshot, or text capture is incomplete. |
| `policy_or_legal_boundary` | The question depends on policy or legal interpretation beyond annotation. |
