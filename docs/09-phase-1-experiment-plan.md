# Phase-1 Experiment Plan

## Goal

The phase-1 experiment program should determine which low-cost signals improve human-review-oriented triage for Threads scam-like content.

The first program should start with controlled launch details, local workspace preflight, 1-2 manual rehearsal records, 5-item calibration, and a first 10-15 item checkpoint before completing the conditional 50-item pilot. A manually reviewed 100-200 item slice is only a later option after pilot review. If annotation capacity is limited, fewer high-quality governed items are preferable to a larger noisy slice.

## Experiment A: Text-Only vs Text Plus OCR

| Field | Plan |
|---|---|
| Hypothesis | OCR text from images improves recall for scam-like items where key claims are embedded in images or screenshots. |
| Data needed | Items with post text, attached images, OCR output, and human labels. |
| Method | Run the same rule baseline on post text only, then on post text plus OCR text. |
| Output | Risk tier, `signal_tags`, explainable reasons, and changed decisions. |
| Metrics | Precision, recall, F1, evidence completeness, OCR error rate, reviewer burden. |
| Failure modes | OCR misses text, image contains irrelevant personal data, OCR adds false positives, screenshots are low quality. |
| Decision implications | Continue OCR if it improves recall or evidence completeness without unacceptable false positives. |

## Experiment B: Post-Only vs Post Plus Comments

| Field | Plan |
|---|---|
| Hypothesis | Replies and comments add decisive redirection and persuasion signals missing from original posts. |
| Data needed | Items with post text, selected replies/comments, and labels. |
| Method | Compare baseline output using post text only against post plus reply/comment text. |
| Output | Cases where risk tier changes due to comment context. |
| Metrics | Recall lift, precision change, reviewer time per item, evidence reason quality. |
| Failure modes | Comments are noisy, unrelated, or too time-consuming to annotate. |
| Decision implications | Include comments in MVP if they materially improve triage for report-worthy cases. |

## Deferred Experiment C: Model-Assisted Explanation

| Field | Plan |
|---|---|
| Current status | Not part of the governed Phase 1 launch. |
| Prerequisites | Governed real evidence, stable labels, completed pilot decision memo, and a later decision record that explicitly authorizes model-assisted testing. |
| Failure modes | Overstated certainty, inconsistent reasoning, privacy concerns, cost growth, and scope drift before manual evidence operations are stable. |
| Decision implications | Revisit only after Phase 1 answers the manual collection, annotation, redaction, and baseline-readiness questions. |

## Deferred Experiment F: Embedding-Based Scam Spectrum

| Field | Plan |
|---|---|
| Current status | Brainstorming only; not part of the active pilot. |
| Hypothesis | When enough confirmed scam and comparator examples exist, embeddings may help map scam-like content into families, boundary zones, and nearest-neighbor review examples. |
| Prerequisites | Larger governed dataset, stable second-reviewed labels, redacted or controlled-store-governed text, non-scam comparators, and a later decision record authorizing model-assisted analysis. |
| Method | Embed redacted item text, selected reply context, and OCR text if approved; inspect clusters and nearest neighbors; compare against rule-library families. |
| Failure modes | Embedding similarity is mistaken for proof, false positives cluster around legitimate finance education, sensitive text leaks into model artifacts, or clusters overfit to a small confirmed-pointer set. |
| Decision implications | Use only as a reviewer aid or method-study tool unless a later evaluation proves value and governance approves expansion. |

## Deferred Experiment G: Potential Exposure Or Victim-Risk Study

| Field | Plan |
|---|---|
| Current status | Brainstorming only; not approved for active collection. |
| Hypothesis | Reshares, quote-like activity, replies, and other interactions around confirmed scam posts may help study exposure patterns and possible victim-risk cohorts. |
| Prerequisites | Explicit CIB/stakeholder approval for interaction-level data, stricter user-identifier governance, controlled-store-only raw graph storage, redaction/pseudonymization plan, and ethics/legal review. |
| Method | If approved later, represent interactors as pseudonymous exposure nodes, not confirmed victims; separate exposure, suspected victimization, and confirmed victimization. |
| Failure modes | Resharers or commenters are falsely labeled as victims, raw identifiers leak, profile graph scope expands too quickly, or outreach implications are mishandled. |
| Decision implications | Treat this as a possible prevention/research dataset, not an enforcement or accusation workflow. |

## Experiment D: Binary Classification vs Risk Triage

| Field | Plan |
|---|---|
| Hypothesis | Risk triage is more useful than binary scam/non-scam classification for early Threads research. |
| Data needed | Annotated items with confidence, uncertainty, and evidence status. |
| Method | Compare binary labels against triage tiers such as high, medium, low, and insufficient evidence. |
| Output | Reviewer queue recommendations and ambiguous-case handling. |
| Metrics | Reviewer burden, false positive harm, uncertain case routing, stakeholder usefulness. |
| Failure modes | Triage tiers become vague, reviewers disagree, stakeholders still require binary decisions. |
| Decision implications | Use triage in phase-1 MVP unless stakeholders require a binary reporting layer. |

## Experiment E: With-Link Signals vs Without-Link Signals

| Field | Plan |
|---|---|
| Hypothesis | Visible link and redirection signals improve precision for high-risk triage. |
| Data needed | Items with visible links, handles, private-channel instructions, or link text. |
| Method | Compare baseline features with and without link/redirection fields. Capture redirect or landing evidence only under approved CIB run records. |
| Output | Risk tier changes and reasons involving external movement. |
| Metrics | Precision, recall, false positive rate on legitimate links, reviewer usefulness. |
| Failure modes | Legitimate creators use links, shorteners create overflagging, link context unavailable. |
| Decision implications | Keep link features if they improve high-risk review queues without broad overflagging. |

## Experiment Order

1. Create dataset v1 and finish annotation pass.
2. Run text-only keyword/rule baseline.
3. Add OCR and compare.
4. Add comments/replies and compare.
5. Add visible link/redirection signals and compare.
6. Write an error analysis and narrowing memo.
7. Revisit deferred embedding or exposure/victim-risk studies only after a later decision record approves the scope.

## Minimum Experiment Output

Each experiment must produce:

- Dataset version.
- Method description.
- Cost estimate.
- Metric table.
- Five to ten representative errors.
- Decision: continue, modify, defer, or stop.
