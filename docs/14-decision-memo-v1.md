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

- dataset schema
- annotation guide
- signal taxonomy
- stakeholder authorization gate
- controlled launch details completed outside git
- local-only pilot workspace and item-1 preflight
- 1-2 item manual collection rehearsal
- 5-item annotator calibration
- first 10-15 item checkpoint before completing the 50-item pilot
- conditional 50-item pilot only after checkpoint review
- conditional 100-200 item first usable dataset only after a pilot decision memo
- rule-based risk scorer
- OCR augmentation comparison
- comment and link-signal ablation

Defer optional LLM-assisted explanation tests until Phase 1 produces governed real evidence and a later decision record explicitly authorizes that scope.

## Current Status As Of 2026-04-23

The scaffold, governance gate, report-v0 package, synthetic samples, local QA/baseline scripts, controlled-launch templates, local workspace tooling, preflight verification, rehearsal guidance, calibration guidance, and first-checkpoint protocol now exist.

A synthetic-only integrated rehearsal has validated the repo tooling path:

- schema validation passes on sample CSV and JSON
- manual record building works on synthetic local input
- calibration files can be prepared
- agreement comparison can produce local disagreement artifacts
- dataset audit flags synthetic source skew and evidence limitations
- rule-baseline variants compare `post_text`, `reply_texts`, `ocr_text`, links, handles, and redirects
- reviewer packets and synthesis drafts can be generated locally

This does not authorize real collection and does not establish real-world performance. The next human action is to complete the controlled launch record outside git. After that, initialize the local workspace, run item-1 preflight, rehearse 1-2 records, run 5-item calibration, and stop at the first 10-15 item checkpoint before deciding whether to continue to 50.

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
