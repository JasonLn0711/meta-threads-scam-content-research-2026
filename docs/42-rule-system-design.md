# Rule System Design

## Design Principles

The first trusted detector should be transparent, adjustable, explainable, easy to debug, and reviewer-friendly.

The rule system is built around observable evidence fields, not account inference or hidden collection. Every matched signal preserves:

- stable signal code
- reason code
- category
- source field
- matched pattern or structured-field origin
- matched text where feasible
- weight

## Data Flow

```text
thread_item record
  -> field normalization
  -> signal extraction
  -> weighted scoring
  -> convergence bonuses and high-risk guardrails
  -> binary and triage prediction
  -> reason codes, explanations, score breakdown
  -> optional evaluation against labels
```

## Signal Families

| Family | Category | Example signals | Why it matters |
|---|---|---|---|
| Textual lure | `textual_lure` | guaranteed profit, easy money, copy trade, beginner earning | Captures the core persuasive claim. |
| Redirect/contact | `redirect_contact` | LINE, WhatsApp, Telegram, DM, handles, external links | Captures movement away from public review context. |
| Urgency/pressure | `urgency_pressure` | limited seats, today only, act now | Adds persuasion pressure but is weak alone. |
| Testimonial/screenshot | `testimonial_screenshot` | proof screenshots, student success, account balance | Captures proof-like persuasion and screenshot-heavy posts. |
| Pseudo-official/endorsement | `pseudo_official_endorsement` | official, support, verification, celebrity/expert framing | Captures authority borrowing and impersonation hints. |
| Payment/credential | `payment_credential` | fee, deposit, wallet transfer, password, bank info | Severe evidence, but still review context is required. |
| OCR context | `ocr_context` | suspicious wording found in image text | Shows that image/OCR changed the evidence state. |
| Reply funnel | `reply_funnel` | suspicious redirect or ask appears in replies | Shows that comment context changed the evidence state. |

## Conservative Scoring

The system separates scoring from extraction:

- extraction says what was observed
- scoring says how much it matters
- explanation says why a reviewer should inspect it

Default scoring uses:

- `medium_threshold: 5`
- `high_threshold: 9`
- `high_min_categories: 2`
- `binary_positive_policy: medium_or_high`

Weak single signals such as a visible link or screenshot style can contribute evidence, but cannot create high risk alone. High risk requires enough score and independent signal families.

## Variants

| Variant | Fields used | Comparison question |
|---|---|---|
| `text_only` | `post_text` | What can post text alone catch? |
| `text_reply` | `post_text`, `reply_texts` | Do replies/comments reveal funneling? |
| `text_ocr` | `post_text`, `ocr_text` | Does image text improve triage? |
| `all` | all phase-1 fields | What is the value of all low-cost signals together? |

## Output Contract

Each prediction includes:

- `item_id`
- `binary_pred`
- `risk_level_pred`
- `subtype_hint`
- `total_score`
- `reason_codes`
- `explanations`
- `score_breakdown`
- `matched_signals`
- `reviewer_note`

This shape is suitable for later triage packets or reviewer worksheets.
