# Reason Codes And Thresholds

## Stable Reason Codes

| Reason code | Meaning | Typical source |
|---|---|---|
| `GUARANTEED_PROFIT` | Guaranteed, fixed, no-loss, or risk-free outcome language | post, reply, OCR |
| `LOW_EFFORT_HIGH_RETURN` | Easy money, passive income, unusually large benefit | post, reply, OCR |
| `HIGH_FEE_COURSE_FUNNEL` | High-fee course, academy, membership, coaching, or trading-education funnel | post, reply, OCR |
| `BEGINNER_EASY_MONEY` | Beginner or no-experience earning framing | post, reply, OCR |
| `MENTOR_COPYTRADE_LANGUAGE` | Teacher, mentor, signal group, copy-trade lure | post, reply, OCR |
| `PRIVATE_REDIRECT` | DM, group, LINE, WhatsApp, Telegram, private channel | text or structured redirect field |
| `IMPLICIT_DM_CONTACT_REQUEST` | DM/private-message request that withholds public contact details and may move delivery of links or handles into private chat | post, reply, OCR |
| `CONTACT_HANDLE_PRESENT` | Visible handle, phone, email, or messaging ID | contact-handle field or text |
| `EXTERNAL_LINK_PRESENT` | Visible link, URL, shortener, or click-link instruction | link field or text |
| `URGENCY_PRESSURE` | Scarcity, deadline, today-only, act-now pressure | post, reply, OCR |
| `TESTIMONIAL_PATTERN` | Proof, results, withdrawal proof, profit screenshot | post, reply, OCR |
| `SCREENSHOT_EVIDENCE` | Screenshot-heavy or screenshot-as-proof framing | screenshot field or text |
| `PSEUDO_OFFICIAL_LANGUAGE` | Official, support, verification, subsidy, registration framing | post, reply, OCR |
| `CELEBRITY_ENDORSEMENT_PATTERN` | Celebrity, expert, news, or endorsement framing | post, reply, OCR |
| `PAYMENT_OR_CREDENTIAL_REQUEST` | Fee, deposit, wallet, password, bank, identity, verification ask | post, reply, OCR |
| `OCR_SUSPICIOUS_TEXT` | Suspicious signal was found in OCR text | derived |
| `REPLY_FUNNEL_PATTERN` | Suspicious signal was found in replies/comments | derived |
| `MULTI_SIGNAL_CONVERGENCE` | Multiple independent signal families co-occurred | scoring bonus |

Reason codes are not legal conclusions. They are traceable review reasons.

## Default Thresholds

Configured in `configs/baseline_rule_config.yaml`.

| Setting | Default | Interpretation |
|---|---:|---|
| `medium_threshold` | 5 | Enough signal for review-worthy `medium` risk. |
| `high_threshold` | 9 | Score needed before `high` risk can be considered. |
| `high_min_categories` | 2 | At least two signal families required for high risk. |
| `multi_signal_convergence_min_categories` | 3 | Number of families that makes convergence especially meaningful. |
| `binary_positive_policy` | `medium_or_high` | Binary baseline treats medium/high as `scam_like`. |

## Weight Philosophy

| Signal type | Default behavior |
|---|---|
| Link-only evidence | Weak alone; should not create high risk. |
| Screenshot-style evidence | Weak alone; useful when paired with claim, proof, OCR, or redirect. |
| Urgency | Weak alone; common in legitimate marketing. |
| Guaranteed profit | Strong, but strongest when paired with redirect/proof/payment evidence. |
| High-fee course funnel | Weak to medium alone; stronger when paired with financial outcome, guarantee, private contact, testimonial, or reply-dispute evidence. |
| Implicit DM request | Weak alone; stronger when paired with investment/profit framing, anti-scam camouflage, proof, urgency, or payment cues. |
| Payment or credential ask | Severe signal, but high-risk assignment still requires guardrails. |
| OCR-only lure | Adds evidence-context value and explains why images matter. |
| Reply-only funnel | Adds evidence-context value and explains why replies matter. |

## Convergence Bonuses

Default bonuses:

- lure plus redirect/contact evidence
- payment/credential plus redirect/contact evidence
- three or more signal families

These bonuses encode the first-principles idea that scam-like triage value often emerges from combinations, not isolated terms.

## Tuning Rules

Tune after inspecting real annotated errors:

- If false positives are high, reduce weak-signal weights before raising thresholds globally.
- If false negatives hide in OCR, increase OCR context or specific OCR signal weights.
- If reply funnels matter, keep `REPLY_FUNNEL_PATTERN` but inspect noisy comment contexts.
- If legitimate creators are overflagged for links, keep link weight low and require convergence.
- Record every threshold change in an experiment note.
