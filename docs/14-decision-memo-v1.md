# Decision Memo v1

## Question

Given current information, what should we actually do first for Threads scam-content research?

## Recommendation

Start with a Threads-first, text/image/comment research MVP focused on evidence structure and human-review triage.

Do not start with production detection, cross-platform Meta integration, long video analysis, or deepfake detection. These paths are too expensive and too uncertain for the first phase under an approximate NTD 1.8 million budget.

## Rationale

Threads appears to be a high-priority report surface based on stakeholder discussion. A Threads-first scope reduces variation and allows the research team to build a defensible dataset, taxonomy, and baseline comparison quickly.

The strongest phase-1 signals are likely to appear in:

- Post text
- Replies and comments
- OCR text from images and screenshots
- Visible redirection instructions
- External links or private-channel references

These signals are cheaper, more explainable, and easier to review than video or deepfake signals.

## Recommended First Build

Build a research scaffold containing:

- Dataset schema
- Annotation guide
- Signal taxonomy
- First manually reviewed sample
- Rule-based risk scorer design
- OCR augmentation comparison
- Comment and link-signal ablation
- Optional LLM-assisted explanation test on a small subset

## What To Defer

Defer:

- Long video processing
- Deepfake indicators as a core workstream
- Full Meta cross-platform integration
- Automated collection
- Heavy classifier training
- Dashboard or production system

## Decision Criteria After 4 Weeks

Continue if:

- Reviewers can apply labels consistently.
- Text, OCR, comments, or link signals improve triage.
- Baselines produce useful, evidence-backed reasons.
- Stakeholders agree that the triage framing matches operational needs.

Cut or narrow if:

- Evidence access is too weak.
- Annotation disagreement remains high.
- OCR or comment context adds little value.
- False positives dominate likely benign content.
- The budget would be consumed before actionable learning.
