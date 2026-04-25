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
| `high_fee_course_or_membership_funnel` | High-fee course, academy, membership, coaching, or trading-education funnel tied to financial outcomes. |
| `private_channel_redirect` | DM me, join group, contact assistant, LINE/WhatsApp/Telegram handle. |
| `implicit_dm_contact_request` | Public post or reply asks users to private-message the poster, even when no LINE/link/site/contact handle is visible. |
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
- `contextual_pattern`: signal depends on a combination of post, replies, image, OCR, or visible link evidence.
- `reviewer_observation`: reviewer notes a visual or contextual pattern not captured by text.

## Explainable Reasons

Each `scam` or `uncertain` label should include at least one evidence-based reason, such as:

- "Promises guaranteed profit."
- "Redirects user to private messaging channel."
- "Requests private messages as the conversion path while withholding public contact details."
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
