# Evaluation Framework

## Evaluation Principle

Do not rely only on model metrics. The phase-1 system is useful only if it improves human review, preserves evidence, handles ambiguity, and avoids overclaiming.

## Core Metrics

| Metric | Why it matters |
|---|---|
| Precision | Measures how often high-risk flags are actually review-worthy. |
| Recall | Measures how many labeled scam-like items are surfaced. |
| F1 | Balances precision and recall for baseline comparison. |
| Reviewer burden | Measures time and effort required per item. |
| Triage usefulness | Measures whether outputs help prioritize review. |
| Explainability quality | Measures whether reasons are specific, evidence-based, and reviewable. |
| Evidence completeness | Measures whether needed text, OCR, comments, and links are present. |
| Robustness to wording variation | Measures whether slight wording changes break the baseline. |
| Ambiguity handling quality | Measures whether uncertain and insufficient-evidence cases are routed properly. |
| Human review workflow usefulness | Measures whether reviewers can act on the output. |

## Suggested Quantitative Measures

- Precision at high-risk tier.
- Recall for `scam` items.
- False positive rate among legitimate finance or marketing posts.
- Percentage of items requiring second review.
- Average annotation minutes per item.
- Percentage of outputs with at least one evidence-backed reason.
- Percentage of cases with complete evidence snapshot.

## Suggested Qualitative Review

For each experiment, inspect:

- Top false positives.
- Top false negatives.
- Cases where OCR changed the result.
- Cases where comments changed the result.
- Cases where links changed the result.
- Ambiguous examples that caused reviewer disagreement.
- Examples where the baseline used weak or misleading reasons.

## Reviewer Burden

Measure:

- Time to annotate text-only item.
- Time to annotate text plus image item.
- Time to annotate post plus comments.
- Time to resolve uncertain cases.
- Number of fields reviewers found confusing.

Reviewer burden is a first-class metric because a technically stronger method may still fail if it creates too much manual work.

## Explainability Rubric

| Score | Meaning |
|---|---|
| 0 | No reason provided. |
| 1 | Generic reason without evidence. |
| 2 | Specific signal named, weak evidence reference. |
| 3 | Specific signal with clear evidence source. |
| 4 | Multiple signals with uncertainty and missing evidence described. |

## Acceptance Standard For Phase 1

Phase 1 does not need production-grade performance. It needs evidence that a narrow MVP is worth continuing.

Continue if:

- Simple baselines identify high-risk review candidates with explainable reasons.
- OCR, comments, or link signals show measurable added value.
- Reviewers can apply labels consistently enough to support comparison.

Cut or narrow if:

- Labels are inconsistent even after guideline revision.
- Most useful evidence is unavailable.
- Baselines are dominated by false positives.
- Reviewer burden is too high for the expected operational value.
