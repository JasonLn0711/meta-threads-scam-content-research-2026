# Budget Fit Analysis

## Budget Frame

The practical budget is approximately NTD 1.8 million. This supports a focused research MVP, not a production-grade detection platform.

## Realistic Under NTD 1.8M

- Taxonomy and annotation guideline development.
- Stakeholder interviews and evidence-standard clarification.
- Small manually reviewed dataset of 100 to 500 items across phases.
- Lightweight OCR integration for approved images.
- Simple keyword and rule baselines.
- Small LLM-assisted review experiments.
- Evaluation memos, error analysis, and narrowing recommendations.
- Minimal scripts for schema validation and metrics.

## Not Realistic Under NTD 1.8M

- Continuous platform monitoring.
- Full Meta cross-platform integration.
- Production enforcement tooling.
- Large-scale labeling operation.
- Heavy video understanding.
- Deepfake detection as a mainline capability.
- Large custom model training.
- Robust adversarial detection against adaptive scammers.

## What To Do First

1. Lock taxonomy and annotation rules.
2. Build the dataset schema.
3. Collect a small, balanced, legally safe sample.
4. Annotate the first batch.
5. Run text-only rules.
6. Add OCR, comments, and link-signal ablations.
7. Write a decision memo.

## Explicitly Postpone

- Short video until text/image/comment evidence is proven insufficient.
- Long video until there is a separate budget and annotation plan.
- Deepfake indicators until there is a concrete stakeholder sample and expert review path.
- Automated collection until authorized.
- Classifier training until labels are stable.
- Dashboard or web app until reviewer workflow is proven.

## Ranked ROI

| Rank | Item | ROI | Risk | Recommendation |
|---:|---|---|---|---|
| 1 | Taxonomy and annotation guide | High | Low | Do immediately |
| 2 | Dataset schema and evidence fields | High | Low | Do immediately |
| 3 | Manual sample and annotation | High | Medium | Do immediately with governance |
| 4 | Text keyword/rule baseline | High | Low | Do immediately |
| 5 | OCR augmentation | High | Medium | Add after text baseline |
| 6 | Comment/reply context | High | Medium | Sample and compare |
| 7 | Visible link/redirection features | High | Medium | Include without crawling |
| 8 | LLM-assisted explanations | Medium | Medium | Test on small subset |
| 9 | Text classifier | Medium | Medium to high | Wait for more labels |
| 10 | Short video study | Medium | High | Later only if necessary |
| 11 | Long video analysis | Low | High | Defer |
| 12 | Deepfake detection | Low for phase 1 | Very high | Defer |

## Budget Guardrail

If an activity does not improve evidence quality, annotation reliability, signal comparison, or narrowing decisions, it should not be funded in phase 1.
