# Baseline Experiment Plan

## Purpose

The modular rule baseline is the first trusted comparison point for Threads scam-content triage. It is transparent enough for reviewers to audit and cheap enough to run after each annotation batch.

## First Comparisons

Run these comparisons after the first authorized annotated slice:

| Comparison | Variant | Decision question |
|---|---|---|
| Post text only | `text_only` | What does top-level text catch by itself? |
| Post text plus replies | `text_reply` | Do replies/comments reveal redirect or payment funnels? |
| Post text plus OCR | `text_ocr` | Does image text improve recall or evidence completeness? |
| Full phase-1 signals | `all` | Do visible links, handles, redirects, replies, and OCR improve triage? |
| Threshold variants | config copies | Which thresholds keep high-risk precision acceptable? |

## Minimum Outputs

Each baseline run should produce:

- predictions JSON
- evaluation summary JSON
- error analysis JSON
- short summary Markdown
- a short experiment note with keep/revise/drop decision

## Likely Blind Spots

- Legitimate finance, recruiting, health, creator, and promotional content can share surface wording.
- OCR may include unrelated screenshot text.
- Replies may be noisy, sarcastic, or unrelated.
- Link presence alone is weak because legitimate creators use links.
- Synthetic examples overrepresent clear cases.

## Next Tuning Cycle

After 30-50 real annotated items:

1. Review false positives first.
2. Inspect false negatives with OCR or reply evidence.
3. Tune `configs/baseline_rule_config.yaml`.
4. Re-run all four variants.
5. Record the new threshold decision before adding models.
