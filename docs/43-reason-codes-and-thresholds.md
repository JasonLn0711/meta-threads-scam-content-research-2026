# Reason Codes And Thresholds

## Stable Reason Codes

| Reason code | Meaning | Typical source |
|---|---|---|
| `GUARANTEED_PROFIT` | Guaranteed, fixed, no-loss, or risk-free outcome language | post, reply, OCR |
| `LOW_EFFORT_HIGH_RETURN` | Easy money, passive income, unusually large benefit | post, reply, OCR |
| `PAST_PERFORMANCE_PROFIT_PROOF` | Past stock-pick performance, limit-up proof, hit-rate, profit table, or wealth-result claim | post, reply, OCR |
| `HIGH_FEE_COURSE_FUNNEL` | High-fee course, academy, membership, coaching, or trading-education funnel | post, reply, OCR |
| `STOCK_RESCUE_GROUP_FUNNEL` | Trapped-stock rescue, synchronized operation, free stock community, or stock-help group funnel | post, reply, OCR |
| `INDIVIDUAL_STOCK_ADVICE_REPLY_FUNNEL` | Repeated individualized stock buy/hold/add/wait/sell guidance in replies | reply, OCR |
| `MARKET_DIRECTION_HERDING_CHORUS` | Strong market-direction call amplified by buy/add/hold/refill/following chorus in replies | post, reply, OCR |
| `INSTITUTIONAL_FLOW_AUTHORITY_LURE` | Institutional flow, foreign-investor data, or macro-event authority cues used to justify strong trading action | post, reply, OCR |
| `LIFESTYLE_TRUST_MARKET_REASSURANCE_FUNNEL` | Lifestyle or parasocial trust framing paired with market fear reassurance and buy/hold/add guidance | post, reply, OCR |
| `BEGINNER_EASY_MONEY` | Beginner or no-experience earning framing | post, reply, OCR |
| `MENTOR_COPYTRADE_LANGUAGE` | Teacher, mentor, signal group, copy-trade lure | post, reply, OCR |
| `PRIVATE_REDIRECT` | DM, group, LINE, WhatsApp, Telegram, private channel | text or structured redirect field |
| `IMPLICIT_DM_CONTACT_REQUEST` | DM/private-message request that withholds public contact details and may move delivery of links or handles into private chat | post, reply, OCR |
| `COMMENT_CODE_LEAD_MAGNET` | Follow, comment, code, or keyword instruction used as a lead magnet for stock picks, methods, lists, or benefits | post, reply, OCR |
| `STOCK_PICK_PLAYBOOK_KEYWORD_FUNNEL` | Named short-term stock-pick lure with follow/message/code gate for complete operation script or playbook | post, reply, OCR |
| `TRAPPED_POSITION_DM_PLAYBOOK_REPLY` | Trapped-position or loss-anxiety reply moved into DM/private playbook guidance | reply, OCR |
| `DARK_HORSE_STOCK_TARGET_PRICE_DM_FUNNEL` | Hidden or dark-horse stock target-price lure gated behind follow, message, code, or private-share action | post, reply, OCR |
| `CODED_ANIMAL_STOCK_LIMIT_UP_GROUP_FUNNEL` | Animal-coded or obscured low-price stock lure with near-term limit-up/exit claim and group/message gate | post, reply, OCR |
| `MASS_STOCK_COMMAND_LIST_GROUP_FUNNEL` | Mass stock buy/sell/limit-up command list that converts readers into a daily stock-signal group or quota | post, reply, OCR |
| `TRADING_RULES_WEALTH_AUTHORITY_FOLLOW_GATE` | Trading-rule list and wealth/experience authority lure gated behind like, follow, `+1`, or get-on-board action | post, reply, OCR |
| `BRAND_PATENT_EXTREME_ROI_CONTACT_FUNNEL` | Brand, patent, order-backlog, or catalyst authority plus extreme ROI and contact/private-message gate | post, reply, OCR |
| `REPLY_IMPERSONATION_CONTACT_HIJACK` | Replies impersonate/certify/ride on poster identity to redirect readers to contact or group paths | reply, OCR |
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
| Past-performance proof | Medium alone; stronger when paired with stock-pick authority, wealth-result claims, free-sharing guru framing, or conversion signals. |
| High-fee course funnel | Weak to medium alone; stronger when paired with financial outcome, guarantee, private contact, testimonial, or reply-dispute evidence. |
| Stock-rescue group funnel | Medium to strong when paired with LINE/OpenChat, shorteners, private stock-holding consultation, synchronized operation, or free guru framing. |
| Individual stock advice reply funnel | Medium alone; stronger when paired with prediction-proof, profit framing, group-join comments, or private-channel migration. |
| Market-direction herding chorus | Medium to strong; high-risk calibrated when a strong market-direction call is amplified by repeated user action-taking comments or other funnel context. |
| Institutional-flow authority lure | Medium alone; stronger when paired with past-performance proof, full-position/do-long instructions, guru authority, or follower reassurance/action comments. |
| Lifestyle-trust market reassurance funnel | Medium alone; stronger when paired with follower trust, private-channel/contact hijack replies, stock-pick proof, or repeated account-level lure behavior. |
| Implicit DM request | Weak alone; stronger when paired with investment/profit framing, anti-scam camouflage, proof, urgency, or payment cues. |
| Comment-code lead magnet | Weak alone; stronger when paired with investment/profit framing, fake authority, target-price claims, named stock picks, or reply-context warnings. |
| Stock-pick playbook keyword funnel | Strong when a named short-term pick, FOMO, prior winners, and a follow/message/code action gate converge. |
| Trapped-position DM playbook reply | Strong when loss anxiety or trapped-position help becomes a private-message or operation-playbook conversion point. |
| Dark-horse stock target-price DM funnel | Strong when a hidden stock, high target-price lure, catalyst claim, urgency, and follow/message/code/private-share action gate converge. |
| Coded animal stock limit-up group funnel | Strong when an animal-coded/obscured low-price target, near-term limit-up/exit claim, prepared-data framing, and group/message action gate converge. |
| Mass stock-command list group funnel | Strong when many specific buy/sell/limit-up commands, claimed call accuracy, free daily signals, and group/quota conversion converge. |
| Trading-rules wealth-authority follow gate | Strong when wealth/experience authority, compact trading-rule guidance, and like/follow/`+1`/get-on-board gating converge. |
| Brand/patent extreme-ROI contact funnel | Strong when brand/patent/catalyst authority, extreme small-stake-to-large-return framing, and contact/private-message gating converge. |
| Reply impersonation/contact hijack | Strong when repeated under high-attention investment posts, especially with LINE/group paths, official-contact claims, anti-scam camouflage, or daily list/holding-viewpoint offers. |
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

- Treat anti-scam warning posts as hard-negative calibration examples. Scam vocabulary quoted for warning, education, or victim-prevention should not score like an active funnel unless the post also introduces a new conversion path.
- If false positives are high, reduce weak-signal weights before raising thresholds globally.
- If false negatives hide in OCR, increase OCR context or specific OCR signal weights.
- If reply funnels matter, keep `REPLY_FUNNEL_PATTERN` but inspect noisy comment contexts.
- If legitimate creators are overflagged for links, keep link weight low and require convergence.
- Record every threshold change in an experiment note.
