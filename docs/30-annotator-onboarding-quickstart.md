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
- `private_channel_redirect`
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

## Common Mistakes

| Mistake | Correct approach |
|---|---|
| Labeling all finance content as `scam` | Require visible guarantee, fake authority, private redirect, payment/credential ask, or suspicious testimonial. |
| Using `uncertain` for unreadable records | Use `insufficient_evidence` when the item cannot be reviewed. |
| Treating any link as malicious | Record `visible_external_link`, but label based on surrounding evidence. |
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
- `annotation_notes` explains the strongest evidence or uncertainty
- high-risk, uncertain, low-confidence, and partial-evidence items are marked for review
- no raw personal data was pasted into notes

