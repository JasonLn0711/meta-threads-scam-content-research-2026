# Annotation Guideline v1

## Purpose

This guide supports first-round human annotation for Threads scam-content research. It is designed for a small annotation team working with text posts, text plus image posts, replies/comments, OCR text, screenshot-style images, visible links, and visible redirection signals.

These are research labels. They do not prove fraud, criminal intent, platform-policy violation, or legal liability. Annotators should label observable evidence and preserve uncertainty.

## Unit Of Annotation

Annotate one `thread_item` at a time.

A `thread_item` may be:

- a top-level Threads post
- a reply/comment
- a post with one or more images
- a text-only post
- a post with text, image, OCR text, and relevant replies
- a screenshot-style post
- a post containing visible external links, contact handles, or redirection signals

Do not add extra background research unless the collection protocol explicitly provides it. If the available item is incomplete, label the missing evidence instead of guessing.

## Primary Labels

| Label | Use when | Do not use when |
|---|---|---|
| `scam` | Observable evidence strongly supports a scam-like lure, deceptive persuasion pattern, suspicious redirection, fake endorsement, payment/credential ask, or high-risk fraud-like setup. | The content is merely annoying, promotional, political, speculative, or aggressive but lacks deception evidence. |
| `non_scam` | The item appears to be ordinary conversation, legitimate marketing, education, commentary, satire, news, or benign opinion with no meaningful scam-like signal. | There are unresolved redirection, impersonation, payment, or guaranteed-benefit signals. |
| `uncertain` | Some suspicious signals are present, but evidence is mixed, context is missing, or a legitimate explanation remains plausible. | The capture is too poor to review at all; use `insufficient_evidence` instead. |
| `insufficient_evidence` | The item cannot support a meaningful judgment because text, OCR, image, source context, link context, or reply context is missing or unreadable. | The item has enough evidence for a weak but reviewable judgment; use `uncertain` with low confidence. |

### Quick Decision Test

Use `scam` only when you can write a short evidence note beginning with "The item shows..." and name the observable signals. If the note depends mainly on "this feels suspicious," use `uncertain` or `insufficient_evidence`.

### Boundary Checks

- Use `non_scam` when the item is readable and only shows ordinary discussion, education, commentary, or opinion. Topic alone is not a scam signal.
- Use `uncertain` only when at least one concrete suspicious signal is visible, but not strong enough for `scam`.
- Use `insufficient_evidence` only when the captured item is not reviewable enough to support even a weak judgment.
- Do not downgrade to `insufficient_evidence` only because full profile history, destination pages, or broader off-item context were not captured.

## Scam Subtypes

Select all applicable `scam_type` values. Use `none` for `non_scam` unless a subtype is being recorded for a hard-negative analysis.

| Subtype | Definition | Common evidence |
|---|---|---|
| `investment_lure` | Financial opportunity, investment club, trading method, loan, grant, or wealth opportunity lure. | Join group, learn secret method, expert trader, investment mentor. |
| `guaranteed_profit_claim` | Guaranteed, fixed, risk-free, unusually high, or certain financial outcome. | Daily profit, no loss, guaranteed return, fixed ROI. |
| `fake_endorsement` | Unsupported use of celebrity, expert, media, government, brand, school, or institution endorsement. | Famous person image, "as seen on," fake news card, official-looking quote. |
| `redirect_to_private_chat` | Main conversion step moves users to private chat, group, assistant, or off-platform contact. | LINE, WhatsApp, Telegram, DM, private group, contact handle. |
| `impersonation_pseudo_official` | Uses official-looking names, logos, notices, support framing, or institutional language. | Verification notice, fake support, government-like benefit post, exchange-like branding. |
| `urgency_scarcity_pressure` | Pressure tactics that reduce scrutiny. | Limited seats, today only, last chance, act now, urgent deadline. |
| `suspicious_testimonial` | Unverifiable social proof or proof-of-success used to persuade. | Profit screenshots, message screenshots, before/after claims, repeated praise. |
| `recruitment_side_hustle_lure` | Job, task, remote work, passive income, or side-hustle offer with suspicious terms. | High pay for easy tasks, deposit before work, vague recruiter, private chat. |
| `suspicious_crypto_trading_lure` | Crypto, exchange, token, wallet, trading-signal, or mining lure with scam-like signals. | Wallet transfer, secret signals, guaranteed crypto returns, private trading group. |
| `medical_health_miracle_claim` | Health, cure, treatment, supplement, or miracle claim tied to unrealistic result, payment, or suspicious redirection. | Guaranteed cure, doctor-looking endorsement, miracle before/after, order link. |
| `giveaway_reward_prize_lure` | Prize, giveaway, reward, grant, subsidy, lottery, or free benefit lure. | Claim reward, pay shipping fee, verify account, limited winners. |
| `other_high_risk_persuasion` | Fraud-like persuasion not captured above. | Explain in `annotation_notes`. |
| `none` | No scam subtype applies. | Use for ordinary non-scam items. |

## Risk Levels

Risk level is a triage priority, not a final truth claim.

| Risk | Use when | Example |
|---|---|---|
| `high` | Strong evidence or multiple reinforcing signals suggest likely harm or urgent review value. | Guaranteed profit plus private chat redirect and earnings screenshot. |
| `medium` | Some scam-like signals exist but evidence is incomplete, mixed, or lower severity. | Vague finance offer plus contact handle but no guarantee or payment ask. |
| `low` | No meaningful scam-like signal, weak signal only, or item is not reviewable enough for risk escalation. | Ordinary finance discussion or unreadable screenshot. |

For `insufficient_evidence`, usually use `low` risk unless the visible fragments show a severe high-risk signal.

## Evidence Sufficiency

| Value | Meaning |
|---|---|
| `sufficient` | Available text, OCR, replies, image context, or link/redirection evidence supports the label. |
| `partial` | Enough evidence exists for a tentative label, but important context is missing. |
| `insufficient` | Evidence is too incomplete for a confident judgment, but some content is visible. |
| `not_reviewable` | The item cannot be reviewed because the capture is unreadable, missing, broken, or outside scope. |

Evidence sufficiency is separate from label. A case can be `uncertain` with `partial` evidence, or `insufficient_evidence` with `not_reviewable` evidence.

Mark evidence as `sufficient` when the captured text, OCR, replies, or visible handles/links support the core label without needing uncaptured destinations or profile history. Record missing link destination, source identity, or off-screen context in `missing_evidence` instead of lowering sufficiency by default.

## Annotation Confidence

| Value | Meaning |
|---|---|
| `high` | Another trained annotator is likely to choose the same label from the same evidence. |
| `medium` | The label is reasonable but depends on interpretation or missing context. |
| `low` | The evidence is weak, ambiguous, low quality, or likely to cause disagreement. |

Use low confidence freely. The goal is not to force certainty; the goal is to learn where the guideline needs improvement.

Choose confidence based on likely agreement on the primary label and core reason, not on whether every subtype or marginal tag will match exactly. A case can be high-confidence `scam` even if subtype or tag selection may need adjudication.

## Signal Tags

Select all observable `signal_tags`. Use `none` only when no signal applies.

| Signal tag | Use when |
|---|---|
| `unrealistic_profit_or_benefit` | The item promises unusually large money, health, job, prize, or status benefit. |
| `guaranteed_or_risk_free_claim` | The item says or strongly implies guaranteed, certain, no-risk, fixed, or loss-free outcome. |
| `past_performance_profit_proof` | The item uses past stock picks, hit-rate, limit-up, profit table, or wealth-result claims as proof of the poster's ability. |
| `high_fee_course_or_membership_funnel` | The item promotes or defends a high-fee course, academy, coaching, membership, or trading-education funnel tied to financial outcomes. |
| `stock_rescue_group_funnel` | The item offers trapped-stock rescue, portfolio help, synchronized trading, or a free stock community/group as the conversion path. |
| `individual_stock_advice_reply_funnel` | The reply/comment thread gives individualized buy, hold, add, wait, or sell guidance on specific stocks or holdings. |
| `market_direction_herding_chorus` | The item makes a strong market-direction call and the reply/comment thread amplifies it with buy, add, hold, refill, or follow-along responses. |
| `institutional_flow_authority_lure` | The item uses institutional flow, foreign-investor data, macro-event framing, or market-wide authority cues to justify strong trading action. |
| `lifestyle_trust_market_reassurance_funnel` | Lifestyle/travel/warmth or parasocial trust framing is paired with market fear reassurance and buy/hold/add guidance. |
| `account_multi_post_style_cluster` | A CIB-detected or approved account shows multiple scam-like persuasion styles across several posts/replies. |
| `account_posting_cadence_metadata` | A controlled account sample records repo-safe posting cadence or feed-density metadata for prioritization. |
| `poster_identity_context` | The approved record includes poster Threads ID/profile context for controlled-store linkage, dedupe, repeat-source review, or profile-level funnel context. |
| `private_channel_redirect` | The item directs users to private chat, group, assistant, or off-platform contact. |
| `implicit_dm_contact_request` | The item asks users to private-message the poster or another account to receive details, even when no public LINE/link/site/contact handle is visible. |
| `comment_code_lead_magnet` | The item asks users to follow, comment, reply with a code, or use a keyword to receive stock picks, methods, lists, or other benefits. |
| `stock_pick_playbook_keyword_funnel` | The item names a short-term stock pick and offers a complete operation script/playbook through follow, message, or numeric-code action. |
| `hidden_stock_code_past_performance_lure` | The item uses prior stock-pick performance proof to tease an unnamed next stock/code as a high-value urgent opportunity. |
| `trapped_position_dm_playbook_reply` | A reply about being trapped, losing money, or needing stock help is moved into private message or detailed operation playbook guidance. |
| `dark_horse_stock_target_price_dm_funnel` | The item teases a hidden or dark-horse stock with low-current/high-target-price framing, catalyst claims, urgency, and follow/message/code/private-share gating. |
| `coded_animal_stock_limit_up_group_funnel` | The item uses an animal-coded or obscured low-price stock name with near-term limit-up/exit claims and gates details through group, follow, message, or +1 action. |
| `mass_stock_command_list_group_funnel` | The item gives a mass list of stock buy/sell/limit-up commands, then offers daily accurate stock calls, free group sharing, entry quota, or similar funnel. |
| `trading_rules_wealth_authority_follow_gate` | The item uses wealth or long-experience authority plus a trading-rule/discipline list, then gates follow-up stock help behind like, follow, `+1`, or get-on-board action. |
| `brand_patent_extreme_roi_contact_funnel` | The item uses major-brand, patent, order-backlog, or catalyst authority with extreme small-stake-to-large-return claims and contact/private-message gating. |
| `supply_chain_insider_stock_lure` | The item uses claimed insider, procurement, supplier, or confidential corporate-meeting access to justify a specific stock opportunity. |
| `reply_impersonation_contact_hijack` | Replies appear to impersonate, certify, or ride on the poster's identity to redirect readers to LINE/contact/group paths. |
| `visible_external_link` | A visible URL, link text, shortener, or landing-page reference appears. |
| `suspicious_domain_or_shortener` | The visible URL looks mismatched, shortened, disguised, vague, or unrelated to the claimed source. |
| `contact_handle_visible` | A handle, phone number, email, LINE/WhatsApp/Telegram ID, or similar contact appears. |
| `celebrity_or_public_figure_reference` | A celebrity, politician, professor, public figure, or influencer is used as authority or bait. |
| `brand_or_institution_reference` | A brand, school, exchange, bank, government, hospital, or news organization is central to the claim. |
| `pseudo_official_language` | The wording or layout imitates official notice, customer support, approval, subsidy, or verification. |
| `urgency_or_scarcity` | The item uses limited slots, deadlines, today-only framing, fear, or pressure. |
| `testimonial_or_earnings_screenshot` | The item relies on success stories, chat screenshots, profit screenshots, or before/after proof. |
| `payment_deposit_or_fee_request` | The item asks for payment, deposit, fee, wallet transfer, shipping fee, or card setup. |
| `credential_or_personal_data_request` | The item asks for login, verification, identity, bank, account, or personal information. |
| `reply_only_lure` | The suspicious signal appears mainly in replies/comments. |
| `ocr_only_lure` | The suspicious signal appears mainly in image OCR. |
| `vague_offer_strong_benefit` | The offer is unclear but promises a strong benefit. |
| `medical_cure_or_miracle_claim` | The item makes a miracle cure, guaranteed health result, or unsupported treatment claim. |
| `giveaway_reward_or_prize_claim` | The item claims a prize, reward, grant, subsidy, lottery, or giveaway. |
| `recruitment_or_easy_income_claim` | The item claims easy job income, task pay, passive income, or unrealistic remote work. |

Signal tags are evidence features. They do not automatically determine the label.

Do not add a broader tag when a narrower visible tag already explains the evidence. Generic "verify your account" wording supports `pseudo_official_language`; add `credential_or_personal_data_request` only when the item explicitly asks for login, identity, bank, or other personal information. Use `vague_offer_strong_benefit` only when a strong benefit is promised or strongly implied; ordinary discussion about savings, gains, losses, or risk level is not enough.

## Decision Principles

- Label what is visible in the collected item.
- Treat the approved `thread_item` as the evidence unit: top-level post, selected replies/comments, OCR, visible links, handles, and redirects can all carry decisive evidence.
- Preserve uncertainty when context is missing.
- Do not claim criminality or intent.
- Do not label content `scam` based on a single weak signal unless that signal is severe, such as a direct credential or payment ask.
- Separate "suspicious but plausible" from "evidence supports scam-like classification."
- Treat false negatives as especially serious for the CIB-authorized pilot. If approved evidence shows a concrete scam-like redirect, payment/deposit, credential, wallet, private-channel, or add-friend step, escalate to `uncertain` or `scam` instead of dismissing the item because the top-level post looks benign.
- Treat false positives as serious but acceptable when they are explainable and routed to review. Legitimate finance, health, recruitment, political, and promotional speech can look intense without being a scam, so second review must separate high-recall triage from final labels.
- Record missing evidence instead of filling gaps from memory or assumptions.
- Use `annotation_notes` to explain the strongest evidence and the biggest uncertainty.

## Edge-Case Handling

### Aggressive But Legal Marketing

Hard-selling, hype, discounts, influencer copy, urgency, and testimonials are common in legal marketing. Use `non_scam` or `uncertain` unless deception, fake authority, suspicious redirection, payment/credential risk, or unrealistic guaranteed outcome is visible.

### Legitimate Financial Education

Posts explaining investing, trading risk, crypto concepts, budgeting, or market opinion are not scams by default. Use `non_scam` when the content includes risk warnings, educational framing, neutral discussion, ordinary recordkeeping, no private redirect, and no guaranteed profit. Use `uncertain` if it becomes a vague funnel.

Anti-scam warning posts are important hard negatives. Use `non_scam` when the author is warning readers not to join suspicious groups, not to trust stock-call teachers, not to chase promised returns, or not to follow pump-and-dump style schemes, and the visible thread does not ask readers to DM, join the author's group, pay, open an account, or follow a private investment method. These posts may mention scam terms, promised returns, stock groups, foreign-market trading, or victim-loss stories; quote/description of the scam method is not itself a conversion signal.

Escalate from anti-scam warning to `uncertain` only if the same post or replies also introduce a new offer, private channel, contact path, paid service, affiliate path, or "safe" replacement investment group controlled by the author.

### Legitimate Investment Discussion

Do not label a post `scam` just because it discusses stocks, crypto, options, trading, or side income. Escalate when investment content adds guaranteed returns, private signal groups, fake endorsement, deposit request, wallet transfer, or pressure.

### Anti-Scam Camouflage With Investment Funnel

Do not treat anti-scam wording as automatically benign. Some items may repeatedly say they hate, oppose, or warn against scams while also telling readers they can earn money through the author's investment path, group, method, teacher, account, or channel.

Escalate to `uncertain` or `scam` when anti-scam language appears together with any concrete funnel signal: suspicious website or link, LINE/Telegram/WhatsApp/Facebook Messenger/Instagram contact, add-friend link, private group, contact handle, wallet/deposit/payment instruction, guaranteed or unusually strong profit claim, or testimonial proof. Use second review for these cases because the anti-scam wording may be camouflage rather than genuine negation.

### Implicit DM Funnel Without Public Contact Details

Do not require a public LINE link, scam website, contact handle, or visible external URL before recognizing a private-channel funnel. A CIB-confirmed stakeholder exemplar showed that a scam-like investment lure may be wrapped inside another story or ordinary-looking content, then ask users in the post or replies to private-message the poster. The contact route, LINE link, scam site, or other off-platform step may be delivered only after the victim enters DM.

Use `implicit_dm_contact_request` when the visible item asks readers to DM/private-message for details, opportunities, methods, quotas, instructions, or investment/profit information while withholding public contact details. Combine it with `private_channel_redirect`; add `reply_only_lure` when the DM request appears only in selected replies/comments.

Escalate to `uncertain` or `scam` when an implicit DM request co-occurs with investment/profit framing, guaranteed or unusually strong benefit language, testimonial proof, anti-scam camouflage, urgency, payment/deposit/wallet cues, or fake authority. Use second review because legitimate creators also ask for DMs, and the label must rest on the whole evidence pattern, not the DM request alone.

### Comment-Code Lead Magnet In Replies

Do not require a visible LINE link, external URL, or explicit DM request before recognizing a funnel. A scam-like item may use a public post for broad attention, then use the author's own reply/comment to ask readers to follow, comment a code, use a keyword, or request a free list, stock pick, method, quota, or other benefit.

Use `comment_code_lead_magnet` when the public thread contains a code/keyword/number or "free receive" style instruction that creates a follow-up funnel. Combine it with `reply_only_lure` when the conversion signal appears mainly in the author's reply/comment rather than the top-level post.

Escalate to `uncertain` or `scam` when this signal co-occurs with investment/profit framing, a claimed target price, guaranteed or unusually strong upside language, fake celebrity or authority framing, named stock picks, or comments warning that the pattern is scam-like. Do not label ordinary engagement prompts, polls, jokes, or harmless newsletter signups as scam by this signal alone.

### Stock-Pick Playbook Keyword Funnel

Do not label every named stock discussion as `scam`. Legitimate analysts and ordinary users discuss specific stocks, entry timing, and technical setups.

Use `stock_pick_playbook_keyword_funnel` when the item combines a named short-term stock pick with FOMO language, recent winner comparison, near-certain movement framing, or easy-entry wording, then asks readers to follow, message, or send a numeric code/keyword to receive a complete operation script, buy/sell playbook, or similar private follow-up.

Use `hidden_stock_code_past_performance_lure` when the item uses a prior buy/sell result, past stock-pick performance, or recent winner as proof of trading authority, then teases an unnamed next stock, hidden code, or small set of numbers as a high-value opportunity with catalyst, technical, or urgency cues. Combine it with `comment_code_lead_magnet` when the post asks readers to comment a keyword or phrase so details can be shared individually. Do not use this tag for ordinary performance recaps unless the next-stock/code teaser and action pressure are both visible.

Use `dark_horse_stock_target_price_dm_funnel` when the item hides or teases a "dark horse" stock, compares a low current price to a much higher target or expected price, adds catalyst claims such as major technology or brand cooperation, then gates the promised stock details behind follow, like, private message, numeric code, or free-share action. Do not use this tag for ordinary target-price discussion unless the hidden-stock lure and private/action gate are both visible.

Use `coded_animal_stock_limit_up_group_funnel` when the item uses an animal-coded or obscured stock nickname, frames it as a low-price target, promises near-term limit-up or exit timing, and gates the prepared details through a group, follow, message, or `+1` action. This is a narrower variant of hidden-stock and stock-pick funnels; do not use it when an animal nickname appears without an investment-action gate.

Use `mass_stock_command_list_group_funnel` when the item publishes a large list of specific stock buy, sell, hold, exit, limit-up, or get-on/get-off commands, claims unusually accurate stock calls or free sharing, and then moves readers toward a daily stock-signal group, quota, follow/comment action, or similar conversion path. Do not use this tag for ordinary watchlists or market notes unless the mass command list and group/quota/free-signal funnel both appear.

Use `trading_rules_wealth_authority_follow_gate` when the item presents the poster as wealthy, highly experienced, or unusually successful, gives a compact trading-rule or discipline list, and then asks readers to like, follow, comment `+1`, or get on board to receive stock help, picks, or buy-timing guidance. Do not use this tag for ordinary educational checklists unless the authority framing and action gate both appear.

Use `brand_patent_extreme_roi_contact_funnel` when the item uses major-brand, patent, order-backlog, exclusive-technology, or catalyst authority to justify an extreme small-stake-to-large-return claim, then gates the stock detail, reference, entry timing, or follow-up through a contact handle, private message, like/follow action, or `+1`. Do not use this tag for ordinary company news or analyst target-price discussion unless the extreme ROI and contact/action gate are both visible.

Use `supply_chain_insider_stock_lure` when the item frames a stock opportunity through claimed insider, family-connected, procurement, supplier, or confidential corporate-meeting access; adds major-brand or institutional authority; and converts the story into buying pressure with exclusive-supplier, technical-proof, exact-price, position-size, or all-in personal-buying cues. Do not use this tag for ordinary supply-chain news unless the insider-access story and investment-action lure are both visible.

Escalate to `uncertain` or `scam` when this signal co-occurs with past-performance proof, limit-up or multi-day board claims, private-channel migration, stock-community/group language, contact handles, or urgency such as do-not-miss, enter on a specific day, close-eyes entry, or break-high certainty. This is a funnel pattern: the public post creates urgency and the reply/action gate moves readers toward a private playbook.

### Trapped-Position DM Playbook Reply

Do not label every reply to an investment question as scam-like. Legitimate commenters ask for help with losing positions and legitimate analysts may answer publicly.

Use `trapped_position_dm_playbook_reply` when a user expresses being trapped, losing money, needing stock help, or asking what to do, and the author or adjacent account moves the answer into private message, private guidance, or a detailed operation playbook instead of a transparent public explanation.

Escalate to `uncertain` or `scam` when this signal co-occurs with short-term stock-pick lures, promised rebound/limit-up framing, private-channel migration, stock-rescue group framing, named-stock playbooks, or prior-performance proof. The risk is that loss anxiety becomes the conversion point into private persuasion.

### Reply Impersonation Or Contact Hijack

Do not assume the top-level poster authored every suspicious reply. Scam-like threads may contain replies from accounts that appear to impersonate, certify, or ride on the poster's identity and then redirect readers to LINE, private groups, daily lists, holdings viewpoints, or other contact paths.

Use `reply_impersonation_contact_hijack` when selected replies claim an official/verified contact route, say other contacts are scams, publish a LINE/contact/group path, or repeatedly post near-identical contact instructions under a high-attention investment post.

Escalate to `scam` or `uncertain` when this signal co-occurs with investment/profit framing, follower trust in the poster, anti-scam camouflage, daily list/holding-viewpoint offers, or repeated contact handles. Preserve attribution uncertainty in `annotation_notes`: the evidence may show thread-level scam risk or hijack risk even if the top-level post itself presents as benign, humble, or anti-scam.

When a top-level investment post uses humble/non-analyst/no-benefit language, follower-profit or loss-recovery framing, and inability-to-reply pressure, inspect replies especially carefully. Adjacent accounts may publish the actual LINE/private-group/contact route while claiming to protect readers from scams. Anti-scam wording in those replies does not neutralize risk when the same reply gives a "safe" contact path, daily watchlist, holdings viewpoint, or group-entry cue.

### Past-Performance Profit Proof

Do not label an item `scam` only because it discusses historical stock movement or shows ordinary investment records. Legitimate finance discussion may review past performance.

Use `past_performance_profit_proof` when the poster uses past stock recommendations, hit-rate language, limit-up percentages, profit tables, "people who followed me got rich" claims, or wealth-result proof to establish trust in the poster's future picks or method.

Escalate to `uncertain` or `scam` when this signal co-occurs with free-sharing or altruistic guru framing, "I am already financially free" credibility claims, named stock picks, unusually strong gain claims, reply/contact/code funnels, private-channel migration, or payment/course signals. Keep second review required because past performance proof can be fabricated, selectively sampled, or legitimate marketing depending on the whole evidence unit.

When a CIB/stakeholder-confirmed pointer combines multiple prior named stock wins, limit-up or percentage-gain proof, a screenshot-style profit table, "followers got rich" or luxury-result claims, and "I do not charge because I am already financially free / just sharing or making friends" language, treat the combination as a high-risk trust funnel. The no-fee claim does not neutralize the lure; it can be part of the credibility strategy that makes later stock picks, private contact, or group conversion feel safer.

### Stock-Rescue Group Funnel

Do not label ordinary stock discussion, portfolio education, or community building as `scam` only because it mentions a group. Legitimate communities exist.

Use `stock_rescue_group_funnel` when the item offers to help users with trapped positions, stock rescue, stock diagnosis, synchronized operation, or free stock-community access, especially when the conversion path is a LINE/OpenChat group, shortener, private message, or off-platform community.

Escalate to `uncertain` or `scam` when this signal co-occurs with investment/profit framing, free/altruistic guru claims, "learn with me" or "follow my operation" framing, visible shorteners, LINE/Telegram/WhatsApp/FB Messenger/IG group links, or requests to send individual stock holdings privately. This is a high-risk funnel because users may disclose holdings and then be moved into off-platform persuasion.

### Individual Stock Advice Reply Funnel

Do not label ordinary replies about public market opinions as `scam` only because a commenter asks a finance question.

Use `individual_stock_advice_reply_funnel` when the author repeatedly answers commenters' specific stock or holding questions with buy, hold, add, wait, exit, target, or position-management guidance. This matters because the reply thread can become a public proof-of-access surface: readers see that the poster gives quick personalized answers, then may join a group or private channel for more.

Escalate to `uncertain` or `scam` when this signal co-occurs with claimed prediction accuracy, past-performance proof, "make everyone rich" framing, stock-rescue/free-group language, private-channel migration, or comments indicating group-join status. Keep second review required because legitimate analysts may discuss stocks publicly; the risk comes from the full funnel pattern, not one reply.

### Market-Direction Herding Chorus

Do not label an item `scam` only because the author has a bullish or bearish market opinion. Market commentary can be legitimate.

Use `market_direction_herding_chorus` when the author makes a strong directional call such as full-position, no-retreat, buy-the-dip, hold, add, or ignore bearish voices, and the visible reply thread shows multiple users echoing buy/add/hold/refill/follow-along actions.

Escalate to `uncertain` or `scam` when this signal co-occurs with prediction-proof, guru authority, group/private-channel context, individualized stock advice, stock-rescue group funnels, or comments indicating users are acting on the author's direction. This signal is about social-pressure amplification, not about one bullish sentence.

### Institutional-Flow Authority Lure

Do not label ordinary macro analysis or institutional-flow commentary as `scam` by itself. Legitimate market commentary often discusses foreign investors, futures positions, index flows, central banks, war risk, weekend risk, or sector rotation.

Use `institutional_flow_authority_lure` when institutional-flow, foreign-investor, futures/spot market numbers, macro-event interpretation, or market-wide authority cues are used to push a strong trading action such as buy, hold, full-position, strong long, do not fear, or follow the author.

Escalate to `uncertain` or `scam` when this signal co-occurs with past-performance profit proof, market-direction herding chorus, guru/teacher authority, individualized stock advice, stock-rescue/community funnel, private-channel migration, or replies showing readers feel reassured and act on the author's direction. This signal captures authority laundering: external market data is used to make the author's trading instruction feel safer or inevitable.

### Lifestyle-Trust Market Reassurance Funnel

Do not label ordinary lifestyle posts, travel photos, greetings, or market commentary as scam-like by themselves. Creators often mix personal life and market notes.

Use `lifestyle_trust_market_reassurance_funnel` when lifestyle, travel, warmth, gratitude, or parasocial closeness is used together with market fear/reassurance language and concrete buy, hold, add, low-buy, or keep-position guidance.

Escalate to `uncertain` or `scam` when this signal co-occurs with follower trust comments, private-channel/contact hijack replies, repeated stock-pick proof, strong market-direction calls, or an account-level cluster showing similar investment-lure behavior. This signal captures trust laundering: emotional safety and lifestyle intimacy make the trading instruction feel less risky.

### Poster Identity And Profile Context

When a run record authorizes full-thread capture for a CIB-confirmed scam pointer, record the top-level poster's Threads ID and narrow profile context in the controlled store. In repo-safe records, use `poster_threads_id_ref` only as a controlled-store reference, salted hash, or redacted handle; do not place raw handles, raw profile URLs, profile photos, follower/following lists, or unrelated personal data in git unless a separate approval explicitly says so.

Use `poster_identity_context` when poster identity/profile context is part of the evidence package for dedupe, repeat-source review, or profile-level funnel interpretation. This tag does not mean the account is legally guilty, and it is not enough by itself to label a post `scam`.

Profile-context signals may include investment identity claims, profile-level redirect/contact cues, repeated confirmed-pointer source status, authority/guru positioning, profit/stock-picking positioning, or cross-post/repost amplification. Escalate only when these profile signals reinforce post, reply, OCR, link, payment, credential, or private-channel evidence.

### Account-Level Multi-Post Style Cluster

Some investment-scam accounts may not expose the full funnel in one post. A CIB-detected or otherwise approved account can contain several posts and replies with different but complementary styles: performance proof, group or synchronized-operation framing, strong market-direction calls, individual stock operation language, anti-scam camouflage, private-channel cues, or follower action chorus.

Use `account_multi_post_style_cluster` when a controlled account-level sampling run reviews several candidate posts under the same approved account and finds two or more scam-like style families. This method is for candidate discovery, dedupe, repeat-source context, and prioritizing which individual posts need full-thread capture.

Do not label every post under the account as `scam` only because the account is CIB-detected or because another post is confirmed. Each selected item still needs its own item-level evidence from post text, replies/comments, OCR, links, contact handles, payment/credential cues, or approved profile context. Keep the candidate cap small, store raw profile/post URLs only in the controlled store, and never capture follower/following graphs unless a later run record explicitly authorizes that expansion.

### Account Posting Cadence Metadata

When a CIB-detected or approved scam account is sampled, record repo-safe feed-level cadence metadata if technically available: visible candidate-post count, visible time-bucket distribution, whether several posts appear in a short recent window, and whether the visible feed repeatedly returns to the same lure families.

Use `account_posting_cadence_metadata` when this cadence summary is attached to an account-level sample or to an item selected from that sample. This metadata helps prioritize accounts and choose which candidate post should receive full-thread capture next.

Do not use cadence alone as a scam label. High posting frequency can be normal for creators, news accounts, or active communities. Escalate only when cadence converges with scam-like style clusters, profit-proof claims, private-channel cues, repeated operation instructions, follower reassurance/action comments, or CIB/stakeholder confirmation. Do not run continuous monitoring or collect profile history beyond the approved small sampling window.

### High-Fee Trading Course Or Membership Funnel

Do not label a course, academy, mentor, or membership offer as `scam` only because it is expensive. Paid education can be legitimate.

Escalate when a high-fee trading, investing, crypto, or financial-education funnel appears together with scam-like evidence: guaranteed or disputed guaranteed-profit claims, vague or defensive legitimacy framing, private-channel contact, screenshots/testimonials, fake authority, pressure to join, unusual payment structure, or selected replies/comments that expose claims not obvious in the top-level post.

Use `high_fee_course_or_membership_funnel` when the collected evidence shows a course, academy, membership, coaching, or trading-education funnel whose price, promised outcome, or reply context is central to the risk assessment. Add `reply_only_lure` when the decisive guarantee, dispute, contact, or payment detail appears mainly in selected replies/comments.

### Finance Discussion Without A Conversion Step

A post about routines, spreadsheets, gains/losses, or risk level is usually `non_scam` when it does not ask the reader to join, DM, pay, trust special access, or follow a secret method. Do not treat mild curiosity or investment vocabulary alone as `investment_lure`. Move to `uncertain` only when a visible funnel or a strong implied benefit is actually present.

Investment-experience or trading-psychology posts can be trust-building starters when they establish the poster as experienced, disciplined, or psychologically skilled, especially when a redacted external-link category is present. Keep these as `uncertain` and raise risk only when evidence is partial; promote to `scam` only if fuller post/reply context shows private-message conversion, community migration, stock-tip guidance, reassurance, guarantees, contact cues, or other funnel mechanics.

### Satire Or Parody

Use `non_scam` when satire/parody is clear. Use `uncertain` when satire is plausible but not obvious. Do not treat public figure imagery alone as a scam signal.

### Politics

Political persuasion, outrage, misinformation risk, or policy disagreement is not this label task. Use `scam` only if the item includes a financial, identity, prize, recruitment, health, or payment/credential lure.

### Celebrity Gossip Or Endorsement-Looking Posts

Celebrity news or gossip may be benign. Use `fake_endorsement` only when the public figure appears to be used as authority for a product, investment, reward, medical claim, or private-channel funnel.

### Motivational Wealth Content

"Work hard," "build wealth," or lifestyle bragging is usually not enough. Label `uncertain` or `scam` only when paired with a specific lure, guarantee, private contact, screenshot proof, payment step, or vague high-benefit offer.

### Screenshot-Only Claims

Use OCR when available. If OCR shows clear scam-like claims, annotate those signals and mark `screenshot_style`. If the screenshot is unreadable or lacks source context, use `insufficient_evidence` or `uncertain` and record `ocr_missing_or_low_quality`.

If OCR alone contains the decisive lure, the case may still be `sufficient` evidence even when the source profile, full landing page, or destination link was not captured. Mark the missing context in `missing_evidence` rather than downgrading automatically.

### Incomplete Posts With Suspicious Comments

If the post is benign but replies contain a clear lure, use `reply_only_lure` and label based on the whole `thread_item` if replies were intentionally captured as context. If comments are secondhand claims without direct evidence, use `uncertain`.

For the CIB-authorized pilot, narrow relevant reply/comment context is a high-value evidence surface, not optional decoration. Scam-like behavior may appear only in comments, including suspicious websites, shortened or disguised links, LINE/WhatsApp/Telegram/contact links, add-friend links, wallet/deposit instructions, or private-channel migration. When a run record authorizes reply capture, reviewers must inspect the approved narrow reply window before finalizing a low-risk label.

### Medical Or Health Miracle Claims

Health content is high-risk when it claims guaranteed cure, miracle result, fake doctor/authority support, urgent purchase, or suspicious redirect. Ordinary wellness discussion or personal experience is not enough.

### Recruitment Or Job Opportunity Posts

Legitimate hiring can include pay, remote work, and contact instructions. Escalate when the job is vague, pay is unrealistic, private chat is required, upfront payment/deposit is requested, or identity/bank details are requested early.

### Giveaway, Reward, Or Prize Posts

Legitimate giveaways exist. Escalate when the item requests fees, credentials, personal data, private contact, suspicious links, or official-looking reward claims with weak source identity.

Official-looking reward language plus a fee or private-channel step supports `scam` and often `impersonation_pseudo_official`. Do not add `credential_or_personal_data_request` unless the item actually asks for account, identity, login, or other personal details.

## Required Annotation Note Style

Write short evidence notes:

```text
Evidence observed: OCR says "guaranteed daily profit" and reply redirects to Telegram.
Missing evidence: link destination not captured.
Reason for uncertainty: public figure endorsement cannot be verified from item alone.
```

Avoid:

- "Looks bad."
- "Definitely criminal."
- "Fake for sure."
- "I know this account is suspicious" unless that evidence is part of the captured item.

## Second Review And Adjudication

Send an item to second review when:

- label is `scam` and risk is `high`
- label is `uncertain`
- annotation confidence is `low`
- evidence sufficiency is `partial`, `insufficient`, or `not_reviewable`
- the top-level post appears benign but selected replies/comments contain links, contact handles, private-channel migration, add-friend instructions, wallet/deposit/payment instructions, or suspicious domains
- the item uses anti-scam, scam-hating, or scam-warning language while also promoting an investment/profit path or showing contact/link/private-channel signals
- the item relies on past stock-pick performance, limit-up screenshots, or wealth-result claims to establish investment authority
- the item offers trapped-stock rescue, synchronized operation, or a free stock community with a LINE/OpenChat, shortener, private-message, or off-platform group path
- the author repeatedly gives individualized buy/hold/add/wait/sell guidance in replies while the thread also shows investment authority, profit, group, or private-channel signals
- the author makes a strong market-direction call and the reply thread shows multiple users echoing buy/add/hold/refill/following behavior
- the item asks users to private-message the poster for investment/profit-related details while public contact details are absent
- the author uses replies/comments to ask readers to follow, comment a code, or use a keyword to receive investment/profit-related material
- a high-fee trading, investing, crypto, or financial-education funnel is paired with guaranteed-profit, private-contact, testimonial, payment, or reply-context dispute evidence
- annotators disagree on primary label, risk level, or key scam subtype

Use `templates/adjudication_template.md` to resolve disagreements. If the same disagreement appears repeatedly, revise this guideline after the 50-item pilot.
