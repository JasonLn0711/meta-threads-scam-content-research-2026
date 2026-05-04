# Reviewer Assist Layer Design

## 1. Purpose

Design a Reviewer Assist Layer for labor-efficient Threads investment-scam candidate discovery.

The layer should help reviewers understand candidates faster, avoid reading full raw threads whenever possible, see signal-family summaries, see hard-negative warnings, get schema fields pre-filled, prioritize candidates, record decisions faster, and generate aggregate metrics.

The reviewer assist layer does not replace the reviewer. It changes the reviewer's job from reading and structuring everything manually to verifying, correcting, and deciding.

This is a research and workflow design layer. It is not a production detector, legal fraud determination system, enforcement system, public warning list, account-targeting system, broad crawler, or raw-evidence store.

## 2. Why Reviewer Burden Is A Core Research Constraint

The repo's updated first-principle goal is to use a small amount of human labor to find enough review-worthy Threads investment-scam candidates.

Reviewer labor is therefore not an implementation detail. It is part of the research question.

A source arm or discovery method can appear promising if it surfaces many candidates, but still fail if reviewers must manually read long threads, inspect image text, infer signal families, copy evidence into schema fields, write summaries, check hard negatives, and prepare aggregate notes for every candidate.

Labor reduction should be measured directly, not assumed from automation.

The design goal is to test whether structured assistance can preserve human final judgment while reducing avoidable manual work.

## 3. Human Tasks To Reduce

The assist layer should reduce:

- first-pass reading of long posts, replies, comments, and OCR text;
- manual summarization of candidate evidence;
- manual extraction of investment-scam signal families;
- manual identification of visible private-channel, link, group, or contact cues;
- manual hard-negative screening for ordinary investment discussion, financial education, and anti-scam warnings;
- manual schema field copying and normalization;
- manual prioritization of candidates for review;
- manual creation of repo-safe reviewer notes;
- manual aggregation of review-time, correction, disagreement, and yield metrics.

The layer should reduce time and friction while keeping the evidence auditable.

## 4. Human Tasks That Must Remain Human

Human reviewers must retain:

- final `scam`, `non_scam`, `uncertain`, or `insufficient_evidence` label decisions;
- final risk-level decisions;
- evidence sufficiency judgments;
- hard-negative acceptance or rejection;
- uncertainty handling;
- second review and adjudication;
- exception escalation;
- governance boundary interpretation;
- decisions to continue, revise, pause, or stop a method;
- any legal, policy, enforcement, or external-sharing decision outside this repo.

The assist layer may suggest, summarize, prefill, rank, and flag. It must not decide.

## 5. Reviewer Assist Layer Architecture

Use this layered architecture:

| Layer | Role | Output |
|---|---|---|
| 1. Candidate intake boundary | Accept only authorized, bounded, source-linked candidates | Intake record, source arm, authorization status |
| 2. Evidence-surface parser | Separate post text, replies, OCR text, links, contact cues, and context notes | Structured evidence surfaces |
| 3. OCR/image cue extraction | Extract image text and image-only investment/contact cues when authorized | OCR summary, image-cue flags, OCR confidence notes |
| 4. Thread/reply summarizer | Summarize long thread and reply context for reviewer triage | Short summary with evidence references and missing-context notes |
| 5. Signal-family extractor | Map visible evidence to investment-scam signal families | Candidate signal-family list with confidence and source surface |
| 6. Hard-negative checker | Highlight ordinary investment, education, anti-scam warning, or context-thin risks | Hard-negative warning and reviewer questions |
| 7. Priority ranking assistant | Rank candidate review priority without final labeling | Priority tier, reasons, and uncertainty notes |
| 8. Schema prefill engine | Fill draft schema fields from authorized evidence | Prefilled fields, source references, uncertainty markers |
| 9. Human reviewer console | Let reviewers verify, correct, decide, and record final outcomes | Human-reviewed label, corrections, review time, notes |
| 10. Metrics and audit logger | Record labor, correction, yield, and disagreement metrics | Aggregate metrics and audit trail |
| 11. Governance/stop-rule monitor | Enforce caps, boundaries, leakage checks, and stop rules | Stop-rule warnings, blocked actions, repo-safe status |

```text
authorized candidate
→ evidence surfaces
→ summaries and signal families
→ hard-negative and priority assistance
→ schema prefill
→ human verification, correction, and decision
→ aggregate metrics and governance audit
```

## 6. Input And Output Boundaries

Inputs may include only authorized, bounded, repo-safe or controlled-store-linked evidence:

- redacted post text;
- redacted replies/comments;
- OCR text from authorized images;
- visible link/contact category or redacted reference;
- source arm and run metadata;
- dedupe/source-linkage metadata;
- controlled-store references when permitted;
- reviewer role alias and review timing fields.

Inputs must not include:

- raw personal data beyond approved evidence fields;
- credentials, tokens, session artifacts, or browser exports;
- unnecessary screenshots or unredacted images in git;
- private-message content;
- account/profile graph data;
- landing-page or redirect-chain captures unless separately authorized;
- raw evidence committed to the repo.

Outputs may include:

- summaries;
- extracted signal families;
- hard-negative warnings;
- priority suggestions;
- draft schema prefill;
- reviewer correction logs;
- final human-reviewed labels;
- aggregate metrics;
- repo-safe audit notes.

Outputs must not include:

- final machine-only scam determinations;
- legal fraud determinations;
- enforcement recommendations;
- takedown recommendations;
- public warning lists;
- account-targeting lists;
- raw evidence in git.

## 7. System Functions

The layer should support these functions:

| Function | Reviewer value | Required constraint |
|---|---|---|
| Candidate normalization | Makes source arms comparable | Preserve source arm, authorization, and dedupe state |
| Evidence surface separation | Helps reviewers inspect only relevant surfaces first | Keep post, reply, OCR, and link/contact evidence distinct |
| Thread/reply summary | Reduces long-thread reading burden | Include missing-context and evidence-reference notes |
| OCR cue extraction | Finds image-only claims and contact cues | Mark OCR uncertainty and require reviewer verification |
| Signal-family extraction | Shows why the candidate may be review-worthy | Do not treat a signal as a final label |
| Hard-negative warning | Reduces false-positive pressure | Always expose strongest non-scam explanation |
| Priority ranking | Helps allocate scarce review time | Rank for review priority only, not enforcement |
| Schema prefill | Reduces manual field entry | Track accepted, corrected, and rejected fields |
| Reviewer decision capture | Speeds final label and note recording | Human reviewer owns final outcome |
| Metrics aggregation | Measures labor savings and yield | Aggregate only; no raw evidence in git |
| Stop-rule monitoring | Prevents scope drift | Block unauthorized collection, raw evidence leakage, and cap overflow |

## 8. UI Concept

The UI concept is a reviewer console for internal research demonstration, not a production dashboard.

The first screen should help a reviewer answer:

- Is this candidate worth reviewing now?
- What evidence surfaces are present?
- What is the short summary?
- Which signal families appear?
- What is the strongest hard-negative warning?
- What schema fields were prefilled?
- What needs correction before final review?

Recommended panels:

| Panel | Contents |
|---|---|
| Candidate header | Candidate alias, source arm, authorization status, priority suggestion, stop-rule status |
| Evidence summary | Short post/reply/OCR summary with source-surface references |
| Signal families | Extracted signal tags grouped by post, reply, OCR, link/contact, or context |
| Hard-negative check | Strongest non-scam explanation, uncertainty, and reviewer questions |
| Prefilled schema | Draft fields with accept/correct/reject controls |
| Human decision | Final label, risk level, evidence sufficiency, confidence, notes, second-review flag |
| Metrics capture | Start/stop review time, full-thread-read flag, correction counts, summary rating |

The UI should not hide raw evidence permanently. It should reduce default reading burden while allowing reviewers to open the original controlled evidence when needed.

## 9. API Concept

The API concept should support evaluation of a workflow, not production detection.

Suggested internal endpoints or function boundaries:

| Boundary | Purpose |
|---|---|
| `POST /assist/candidate/normalize` | Normalize one authorized candidate into evidence surfaces |
| `POST /assist/candidate/summarize` | Produce post, reply, and OCR summaries with references |
| `POST /assist/candidate/signals` | Extract signal-family candidates with source-surface notes |
| `POST /assist/candidate/hard-negative-check` | Produce hard-negative warnings and reviewer questions |
| `POST /assist/candidate/prefill` | Produce draft schema fields and uncertainty markers |
| `POST /assist/candidate/priority` | Suggest review priority, not final label |
| `POST /review/decision` | Record human decision, corrections, timing, and second-review status |
| `GET /metrics/aggregate` | Return aggregate labor, yield, correction, and disagreement metrics |
| `POST /governance/stop-rule-check` | Check caps, authorization, leakage status, and blocked actions |

If implemented, API responses should carry evidence references, confidence/uncertainty fields, and explicit `human_decision_required: true`.

## 10. Schema Prefill Concept

The schema prefill engine should generate draft values for existing research fields when evidence supports them.

Likely prefillable fields include:

- `has_reply`;
- `has_image`;
- `image_count`;
- `has_external_link`;
- `visible_platform_redirects`;
- `visible_contact_handles` as redacted/category references only;
- `ocr_text` or OCR summary reference when authorized;
- `language`;
- `screenshot_style`;
- `scam_type` draft candidates;
- `signal_tags` draft candidates;
- `evidence_sufficiency` draft candidate;
- `annotation_confidence` draft candidate;
- `missing_evidence`;
- `metadata_notes`;
- `privacy_redaction_notes`;
- `dedupe_key` or `near_duplicate_group_id` when available.

Fields that must remain human-final include:

- `scam_label`;
- `risk_level`;
- `review_status`;
- `adjudication_status`;
- `disagreement_flag`;
- `final_label`;
- `final_risk_level`;
- `annotation_notes` after reviewer correction;
- any field whose value requires interpreting ambiguous evidence.

Every prefilled field should have:

- source evidence reference;
- generated value;
- reviewer action: `accepted`, `corrected`, `rejected`, or `not_reviewed`;
- correction note when changed;
- reason when rejected.

## 11. Metrics For Labor Reduction

Labor reduction must be measured directly.

| Metric | Definition | Use |
|---|---|---|
| average review time per candidate | Mean elapsed human review time | Measures overall labor burden |
| median review time | Median elapsed human review time | Shows typical review burden |
| p95 review time | 95th percentile review time | Shows worst-tail burden and scale risk |
| candidates reviewed per hour | Reviewed candidates divided by reviewer hours | Measures throughput |
| summary usefulness rating | Reviewer rating of generated summary usefulness | Tests whether summaries reduce reading burden |
| signal extraction correction rate | Share of extracted signals corrected or rejected | Measures signal-assist quality |
| schema prefill acceptance rate | Share of prefilled fields accepted unchanged | Measures field-assist quality |
| schema prefill correction rate | Share of prefilled fields corrected | Measures hidden correction burden |
| percentage of candidates requiring full original-thread reading | Share needing full evidence read after assist | Measures residual manual-reading burden |
| second-review rate | Share requiring second review | Measures ambiguity and review complexity |
| reviewer disagreement rate | Share with conflicting reviewer judgments | Measures guidance and evidence clarity |
| hard-negative false-positive pressure | Rate of ordinary/warning content over-prioritized or overflagged | Protects trust and governance |
| high-risk yield per reviewer hour | Final high-risk candidates per reviewer hour | Measures joint yield and labor efficiency |
| review-worthy yield per reviewer hour | Review-worthy candidates per reviewer hour | Measures source-arm and workflow efficiency |

Compare assisted review against manual review on comparable slices before claiming labor savings.

## 12. Governance Boundaries

The Reviewer Assist Layer must preserve the repo's existing non-authorizations:

- no item `0082` unless separately authorized;
- no open-ended collection;
- no broad crawler/browser expansion;
- no private-message access;
- no account/profile graph capture;
- no landing-page or redirect-chain capture unless separately authorized;
- no model training unless separately authorized;
- no production detector claim;
- no legal fraud determination;
- no automated enforcement;
- no public release;
- no raw evidence in git.

The layer may operate only on authorized candidates and approved evidence fields. It must respect source-arm caps, controlled-store handling, redaction, strict validation, leakage checks, aggregate-only reporting, and stop-rule ownership.

## 13. Failure Modes

Key failure modes include:

- summaries omit decisive reply, OCR, or hard-negative context;
- reviewers trust prefilled fields without verification;
- prefill appears efficient but creates high correction burden;
- ranking over-prioritizes investment vocabulary without funnel evidence;
- hard-negative warnings are too weak or too noisy;
- source arms with high apparent yield create long review tails;
- full-thread reading remains necessary for most candidates;
- second-review load increases because summaries create ambiguity;
- audit logs capture sensitive raw evidence;
- API/UI demonstration becomes mistaken for production readiness;
- automation begins to imply final labels, legal fraud, enforcement, public warning, or account targeting.

## 14. Relationship To Track B

Track B should produce the evidence needed to design and evaluate the Reviewer Assist Layer.

Track B should not merely ask:

```text
Did we find candidates?
```

It must also ask:

```text
Which reviewer tasks consumed the most time?
Which fields could be prefilled?
Which signal families were easiest to summarize?
Which hard-negative cases caused reviewer hesitation?
Which source arms produced the best yield per reviewer hour?
```

Track B outputs should therefore include labor observations, correction counts, summary-usefulness notes, full-thread-read flags, hard-negative hesitation notes, and source-arm yield-per-reviewer-hour metrics. Without these observations, the Reviewer Assist Layer would become guesswork rather than a validated research workflow.

Batch 0008 produced the first explicit context-gating policy for reviewer-hour
allocation:

- fast lane: `strong_source_priority`;
- boundary lane: `result_display_low_context_transition`;
- slow context lane: `result_display_thread_required`;
- calibration lane: `result_display_clean_holdout`.

The policy is recorded in [docs/63-context-gating-policy.md](63-context-gating-policy.md).
Reviewer Assist should treat this as a routing rule before asking reviewers to
spend full-thread or second-review effort.

## 15. Recommended Next Artifacts

Create these artifacts only after Track B supplies enough evidence to ground them:

- reviewer-assist evaluation plan;
- assisted-review worksheet template;
- schema-prefill correction log template;
- summary-usefulness rubric;
- signal-family extraction QA table;
- hard-negative hesitation log;
- priority-ranking evaluation table;
- labor-savings aggregate report template;
- decision-support UI/API demonstration plan;
- governance review checklist for any assisted-review prototype.

Do not implement a UI, API, model training flow, or production-like service until a later decision explicitly authorizes the scope.
