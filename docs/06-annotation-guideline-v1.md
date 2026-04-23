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

## Annotation Confidence

| Value | Meaning |
|---|---|
| `high` | Another trained annotator is likely to choose the same label from the same evidence. |
| `medium` | The label is reasonable but depends on interpretation or missing context. |
| `low` | The evidence is weak, ambiguous, low quality, or likely to cause disagreement. |

Use low confidence freely. The goal is not to force certainty; the goal is to learn where the guideline needs improvement.

## Signal Tags

Select all observable `signal_tags`. Use `none` only when no signal applies.

| Signal tag | Use when |
|---|---|
| `unrealistic_profit_or_benefit` | The item promises unusually large money, health, job, prize, or status benefit. |
| `guaranteed_or_risk_free_claim` | The item says or strongly implies guaranteed, certain, no-risk, fixed, or loss-free outcome. |
| `private_channel_redirect` | The item directs users to private chat, group, assistant, or off-platform contact. |
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

## Decision Principles

- Label what is visible in the collected item.
- Preserve uncertainty when context is missing.
- Do not claim criminality or intent.
- Do not label content `scam` based on a single weak signal unless that signal is severe, such as a direct credential or payment ask.
- Separate "suspicious but plausible" from "evidence supports scam-like classification."
- Treat false positives as serious. Legitimate finance, health, recruitment, political, and promotional speech can look intense without being a scam.
- Record missing evidence instead of filling gaps from memory or assumptions.
- Use `annotation_notes` to explain the strongest evidence and the biggest uncertainty.

## Edge-Case Handling

### Aggressive But Legal Marketing

Hard-selling, hype, discounts, influencer copy, urgency, and testimonials are common in legal marketing. Use `non_scam` or `uncertain` unless deception, fake authority, suspicious redirection, payment/credential risk, or unrealistic guaranteed outcome is visible.

### Legitimate Financial Education

Posts explaining investing, trading risk, crypto concepts, budgeting, or market opinion are not scams by default. Use `non_scam` when the content includes risk warnings, educational framing, no private redirect, and no guaranteed profit. Use `uncertain` if it becomes a vague funnel.

### Legitimate Investment Discussion

Do not label a post `scam` just because it discusses stocks, crypto, options, trading, or side income. Escalate when investment content adds guaranteed returns, private signal groups, fake endorsement, deposit request, wallet transfer, or pressure.

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

### Incomplete Posts With Suspicious Comments

If the post is benign but replies contain a clear lure, use `reply_only_lure` and label based on the whole `thread_item` if replies were intentionally captured as context. If comments are secondhand claims without direct evidence, use `uncertain`.

### Medical Or Health Miracle Claims

Health content is high-risk when it claims guaranteed cure, miracle result, fake doctor/authority support, urgent purchase, or suspicious redirect. Ordinary wellness discussion or personal experience is not enough.

### Recruitment Or Job Opportunity Posts

Legitimate hiring can include pay, remote work, and contact instructions. Escalate when the job is vague, pay is unrealistic, private chat is required, upfront payment/deposit is requested, or identity/bank details are requested early.

### Giveaway, Reward, Or Prize Posts

Legitimate giveaways exist. Escalate when the item requests fees, credentials, personal data, private contact, suspicious links, or official-looking reward claims with weak source identity.

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
- annotators disagree on primary label, risk level, or key scam subtype

Use `templates/adjudication_template.md` to resolve disagreements. If the same disagreement appears repeatedly, revise this guideline after the 50-item pilot.
