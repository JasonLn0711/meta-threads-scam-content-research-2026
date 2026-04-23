# Taxonomy

## Label Philosophy

The taxonomy is designed for research triage. It should capture observable signals and uncertainty without claiming legal guilt.

## Scam Label

| Label | Meaning |
|---|---|
| `scam_like` | The item contains enough scam-like signals to merit high-risk review. |
| `not_scam` | The item does not show scam-like signals under this guideline. |
| `uncertain` | Some signals are present, but evidence is mixed or context is missing. |
| `insufficient_evidence` | The available item cannot be judged from the captured evidence. |

## Scam Type

| Type | Description |
|---|---|
| `investment_lure` | Claims or implies investment opportunity, trading profit, crypto gain, or financial return. |
| `guaranteed_profit` | Uses guaranteed, risk-free, or unusually high return language. |
| `fake_endorsement` | Appears to rely on celebrity, expert, government, brand, or media endorsement without clear support. |
| `redirect_private_channel` | Pushes users toward private messaging, groups, unofficial accounts, or off-platform contact. |
| `impersonation_pseudo_official` | Uses names, logos, language, or format that suggests official status. |
| `high_pressure_urgency` | Uses limited time, act now, fear, scarcity, or pressure tactics. |
| `suspicious_testimonial` | Uses unverifiable success stories, before-after claims, or fabricated-looking proof. |
| `loan_or_grant_lure` | Promises loans, grants, debt relief, subsidies, or financial aid with suspicious terms. |
| `job_or_side_income_lure` | Promises easy work, passive income, or unrealistic compensation. |
| `medical_or_health_claim` | Makes suspicious health, cure, or treatment claims tied to payment or redirection. |
| `other_scam_like` | Scam-like risk not captured by the listed categories. |

Multiple types may apply.

## Risk Signals

| Signal | Examples |
|---|---|
| Profit promise | Guaranteed return, daily income, risk-free trading, fixed ROI. |
| Urgency | Limited slots, today only, last chance, immediate action. |
| Private redirection | DM me, join group, contact assistant, Line/WhatsApp/Telegram handle. |
| Suspicious link | Shortener, newly seen domain, misleading URL text, off-platform funnel. |
| Fake authority | Official-looking phrasing, government-like format, news-like presentation. |
| Social proof | Screenshots of earnings, testimonials, message screenshots, success stories. |
| Identity borrowing | Celebrity, professor, public figure, institution, brand, or media reference. |
| Ambiguous offer | Vague details but strong promised benefit. |
| Payment or credential ask | Deposit, fee, wallet address, account verification, personal information request. |

## Content Form

- `text_post`
- `text_image_post`
- `reply`
- `comment`
- `image_ocr`
- `screenshot_ocr`
- `external_link`
- `mixed_thread_context`

## Evidence Type

- `direct_text`: signal appears in post or comment text.
- `ocr_text`: signal appears in extracted image text.
- `visible_link`: signal appears in URL, domain, or visible link text.
- `redirection_instruction`: signal appears as an instruction to move elsewhere.
- `contextual_pattern`: signal depends on combination of post, replies, and image text.
- `reviewer_observation`: reviewer notes a visual or contextual pattern not captured by text.

## Explainable Reasons

Each high-risk or uncertain label should include at least one reason, such as:

- "Promises guaranteed profit."
- "Redirects user to private messaging channel."
- "Uses suspicious testimonial screenshot."
- "Claims official or celebrity association without evidence."
- "Post text is vague, but replies contain contact instructions."
- "OCR reveals a financial lure not present in visible post text."

## Uncertainty States

| State | Use when |
|---|---|
| `clear` | Evidence strongly supports the label. |
| `mixed_signals` | Both legitimate and suspicious signals appear. |
| `missing_context` | The item may require thread, account, or link context not available. |
| `low_quality_capture` | OCR, screenshot, or text capture is incomplete. |
| `policy_or_legal_boundary` | The question depends on policy or legal interpretation beyond annotation. |
