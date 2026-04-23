# Baseline Strategy

## Principle

Start with transparent, low-cost baselines that directly use the v1 dataset fields. The first goal is not high model performance; it is to learn which evidence fields improve human triage and which fields are too noisy, expensive, or ambiguous.

Do not add heavy models, automated collection, long-video processing, or production scoring before the first annotated dataset slice proves that the basic evidence signals are useful.

The synthetic dry run recorded in `docs/28-synthetic-pilot-dry-run-results.md` confirms that the local baseline scripts can compare the planned evidence fields. It does not establish real-world performance and should not be cited as a result on real Threads content.

The modular rule-baseline implementation is documented in:

- `docs/41-rule-baseline-implementation-plan.md`
- `docs/42-rule-system-design.md`
- `docs/43-reason-codes-and-thresholds.md`
- `docs/44-first-rule-baseline-evaluation.md`
- `docs/45-rule-baseline-calibration-workflow.md`

The tunable scoring surface is `configs/baseline_rule_config.yaml`.
Threshold-profile probes are defined in `configs/rule_calibration_variants.yaml`.

## Dataset Fields Used

| Evidence field | Baseline use |
|---|---|
| `post_text` | Text-only keyword and rule baseline. |
| `reply_texts` | Thread-context baseline for reply-only lures and redirection. |
| `ocr_text` | OCR-augmented text baseline for image and screenshot claims. |
| `external_links` | Link-presence and visible-domain risk signals. |
| `visible_contact_handles` | Private-channel or off-platform contact signal. |
| `visible_platform_redirects` | Platform migration signal such as LINE, WhatsApp, Telegram, private group, or external site. |
| `signal_tags` | Human-rule baseline inputs and audit target for annotator consistency. |
| `scam_label` | Primary supervised label. |
| `risk_level` | Triage target and queue priority. |
| `evidence_sufficiency` | Filter and error-analysis dimension. |
| `annotation_confidence` | Filter for first binary metrics and disagreement review. |
| `final_label` | Preferred label when adjudication is complete. |

## Baseline Families

| Family | Inputs | Output | First use |
|---|---|---|---|
| Text-only keyword baseline | `post_text` | signal tags and provisional risk | Minimum comparator. |
| Text rule baseline | `post_text` | `high`/`medium`/`low` risk | Combine terms such as profit plus urgency. |
| Thread-context rule baseline | `post_text`, `reply_texts` | risk and reason codes | Test whether replies reveal lures missing from post text. |
| OCR-augmented baseline | `post_text`, `ocr_text` | risk and reason codes | Test screenshot and image-text lift. |
| Link/redirection baseline | `external_links`, `visible_contact_handles`, `visible_platform_redirects` | risk and missing-evidence flags | Test whether visible funnels improve precision. |
| Human-rule baseline | `signal_tags` | expected risk level | Audit whether annotator signals map cleanly to labels. |
| Simple text classifier | `post_text`, `reply_texts`, `ocr_text` | binary or triage label | Only after enough adjudicated or high-confidence labels exist. |

## First Rule Logic

Use simple, inspectable rules:

- High risk when guaranteed benefit/profit combines with private-channel redirect, payment/credential ask, fake endorsement, or suspicious testimonial.
- Medium risk when a single strong signal appears but context is missing.
- Low risk when no meaningful signal appears or the item is not reviewable.
- Always surface missing evidence rather than hiding it inside a score.

Example high-risk rule:

```text
(guaranteed_or_risk_free_claim OR unrealistic_profit_or_benefit)
AND
(private_channel_redirect OR contact_handle_visible OR testimonial_or_earnings_screenshot)
```

Example medium-risk rule:

```text
visible_external_link
AND
vague_offer_strong_benefit
AND
evidence_sufficiency != sufficient
```

These rules should be recorded as experiment artifacts before being tuned.

The first synthetic dry run led to a small v1 rule calibration:

- guaranteed-profit plus unrealistic-benefit evidence maps to high risk
- redirect plus proof/authority plus urgency maps to high risk
- generic "before and after" wording is not a testimonial/earnings signal by itself

## First Baseline-Ready Slice

Use the following slice for the first binary baseline:

- `scam_label` in `scam`, `non_scam`
- prefer `final_label` when `review_status` is `adjudicated`
- `annotation_confidence` is `high`, or `review_status` is `adjudicated`
- `post_text` or `ocr_text` is nonempty
- `evidence_sufficiency` is `sufficient` or `partial`
- `baseline_split` is `unassigned`, `train`, `validation`, `test`, or `audit_holdout`

Exclude `insufficient_evidence` from binary precision/recall, but report its rate. Keep `uncertain` as a separate ambiguity bucket and use it for guideline revision.

## Evaluation

Report:

- precision, recall, F1 for `scam` versus `non_scam`
- confusion between high, medium, and low risk
- high-risk queue yield
- performance by content shape: text-only, text plus image, reply/context, OCR-heavy, link/redirection
- missing-evidence rate by label
- false positives among legitimate finance, marketing, recruitment, health, and giveaway posts
- false negatives where OCR or replies contained the decisive signal

Do not claim prevalence from the first dataset. The pilot and first usable batch are diagnostic samples, not representative platform samples.

## When To Add A Model

Add a simple text classifier only after:

- at least 100 usable annotated records exist
- labels are stable enough that annotators are not frequently redefining `uncertain`
- there are enough `scam` and `non_scam` examples to hold out an audit set
- rule failures show patterns that a model might reasonably capture

LLM-assisted review may be tested on a small sample for explanation quality, but it should not replace human labels or process sensitive data without approval.
