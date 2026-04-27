# Decision 0118: Open Capped Investment-Scam Discovery Method-Test Decision Draft

## Status

draft_only

not_executable_until_approved

## Date

2026-04-27

## Decision

Open a draft decision for a capped investment-scam candidate-discovery method test derived from checkpoint `threads_pilot_v1_0081`.

This decision draft does not execute the method test. It defines the proposed caps, source arms, schema fields, reviewer workflow, metrics, stop rules, legal/privacy gate, and aggregate reporting requirements that must be approved or revised before any execution can begin.

## Proposed Purpose

Evaluate whether checkpoint 0081-derived signal families can discover review-worthy Threads investment-scam candidates across post, thread, account-context, and funnel surfaces under fixed caps, human review, strict validation, hard-negative protection, and aggregate-only reporting.

The method test is designed to measure candidate-discovery quality. It is not a production detector, legal fraud determination, platform prevalence estimate, automated enforcement workflow, or public warning system.

## Proposed Execution Boundary

This draft proposes a future method-test boundary only. Execution requires a later approval step that records all required gates as satisfied.

Proposed allowed test mode:

- capped candidate discovery;
- human review only;
- second review when trigger conditions are met;
- repo-safe candidate notes;
- controlled-store handling for any raw or sensitive evidence;
- strict validation before any accepted record is counted;
- aggregate-only reporting.

Not proposed:

- item `0082`;
- open-ended collection;
- broad crawler expansion;
- private-message access;
- account/profile graph capture;
- landing-page or redirect-chain capture;
- embedding/model training;
- production detection;
- legal fraud determination;
- automated enforcement;
- public release;
- raw evidence in git.

## Proposed Caps

| Cap | Proposed value |
|---|---:|
| Surfaced candidates | 300 |
| Human-reviewed candidates | 150 |
| Accepted strict-valid records | 75 |
| Intake window | 14 calendar days |
| Reviewer time cap | average <= 12 minutes per reviewed candidate |
| Second-review rate target | <= 40% |
| Second-review rate concern threshold | > 55% |
| Duplicate rate cap | <= 25% |
| Duplicate rate stop/concern threshold | > 35% |
| Insufficient-evidence rate cap | <= 30% |
| Insufficient-evidence stop/concern threshold | > 40% |
| Hard-negative false-positive pressure cap | <= 15% |
| Hard-negative false-positive stop/concern threshold | > 20% |
| Raw evidence leakage tolerance | 0 |
| Production or enforcement use | 0 |

These caps are provisional and must be approved, reduced, or revised before execution.

## Proposed Source Arms

| Source arm | Candidate cap | Purpose |
|---|---:|---|
| Existing checkpoint-derived seed replay | 50 | Test whether checkpoint 0081 signal families can replay known useful candidate-discovery patterns without raw-evidence expansion. |
| Reviewer-supplied candidates | 50 | Compare reviewer intuition against signal-family-driven candidate discovery. |
| Approved browser-session risk-probe matrix | 100 | Test whether signal-family discovery produces review-worthy investment-scam candidates under an approved session/source boundary. |
| Reply/comment funnel cue candidates | 50 | Test thread-level and comment-layer risk discovery, especially contact migration and coordinated reassurance cues. |
| OCR/image-cue candidates | 50 | Test whether profit-proof, image text, and visual contact cues improve candidate yield. |

Each source arm must record:

- source family;
- candidate count;
- reviewed count;
- review-worthy count;
- high-risk count;
- final scam count;
- duplicate count;
- insufficient-evidence count;
- hard-negative count;
- average review time.

## Candidate Discovery Workflow

```text
candidate surfaced
-> repo-safe candidate note
-> dedupe check
-> evidence completeness check
-> primary human review
-> second review if triggered
-> label / risk assignment
-> hard-negative check
-> strict validation
-> aggregate-only reporting
-> stop-rule check
```

The following steps are mandatory in any future execution approval:

- dedupe check;
- evidence completeness check;
- hard-negative check;
- stop-rule check.

## Required Method-Test Schema Draft

Any future execution record must include repo-safe fields sufficient to audit source-arm yield, dedupe, evidence completeness, reviewer burden, hard-negative pressure, and stop-rule outcomes.

Minimum repo-safe fields:

```text
candidate_id
candidate_unit
source_family
source_arm
candidate_surface_date_bucket
candidate_provenance_class
signal_families_triggered
signal_combination_strength
primary_signal_family
secondary_signal_families
evidence_surfaces_available
top_level_post_available
reply_context_available
reply_context_required
ocr_needed
ocr_decisive
ocr_quality
profile_context_used
profile_context_boundary
external_contact_category
private_channel_migration_visible
dedupe_status
duplicate_cluster_id
near_duplicate_reason
evidence_completeness_score
primary_reviewer_role
review_time_minutes
initial_label
initial_risk
second_review_required
second_review_reason
second_reviewer_role
reviewer_disagreement_type
final_label
final_risk
hard_negative_flag
hard_negative_type
uncertain_reason
insufficient_evidence_reason
false_positive_pressure
false_negative_pressure
stop_rule_triggered
stop_rule_type
repo_safe_notes
```

These fields must not contain raw URLs, handles, screenshots, raw post text, raw reply text, contact IDs, stock names, stock codes, price values, credentials, browser/session artifacts, exact controlled-store paths, stakeholder case IDs, or private recipient details.

## Signal Combination Rule

High-priority candidates should require at least two signal families unless the single signal is a clearly visible:

- private-channel migration cue;
- OCR-derived contact cue;
- OCR-derived profit cue tied to conversion behavior;
- thread-level funnel cue.

Weak signals must not independently create high-priority candidates:

- investment vocabulary only;
- profile looks like finance creator;
- public link only;
- anti-scam language only;
- no-fee language only;
- teacher/advisor wording only;
- ordinary group/community language only.

These weak signals may support low-priority candidate selection or hard-negative review only when context justifies review.

## Priority Scoring Draft

This draft proposes a reviewer triage rubric, not a production score.

| Signal | Points |
|---|---:|
| Private-channel migration | +2 |
| Reply/comment funnel cue | +2 |
| OCR-derived contact/profit cue | +2 |
| Group invitation tied to individualized help | +2 |
| Profit-proof tied to contact/group movement | +2 |
| Teacher/advisor framing | +1 |
| Testimonial/witness cue | +1 |
| Repeated profile-context pattern | +1 |
| Genuine anti-scam warning | -2 |
| Ordinary investment discussion | -2 |
| Non-directed financial education | -2 |
| Public contact information without funnel | -1 |
| Market commentary only | -1 |

Priority interpretation:

| Score | Priority |
|---:|---|
| 0 or below | hard-negative / low priority |
| 1-2 | low-priority candidate |
| 3-4 | medium-priority candidate |
| 5+ | high-priority candidate |

## Metrics and Provisional Thresholds

| Metric | Success threshold | Stop / concern threshold |
|---|---:|---:|
| Review-worthy yield | >= 40% | < 25% |
| High-risk yield | >= 20% | < 10% |
| Final scam-label yield | >= 15% | < 8% |
| Duplicate rate | <= 25% | > 35% |
| Average review time | <= 12 min | > 18 min |
| Second-review rate | <= 40% | > 55% |
| Reviewer disagreement rate | <= 20% | > 30% |
| Hard-negative false-positive pressure | <= 15% | > 20% |
| Insufficient-evidence rate | <= 30% | > 40% |
| Thread-context dependency | measured | no automatic stop |
| OCR dependency | measured | no automatic stop |
| Private-channel migration rate | measured | no automatic stop |
| Raw evidence leak | 0 | any occurrence |
| Baseline misuse as enforcement | 0 | any occurrence |

Precision and recall may be reported as smoke-test context only. They are insufficient by themselves for scaling decisions.

## Hard-Negative Protection

Hard-negative protection is a primary method-test metric, not an appendix.

Protected hard-negative classes:

- genuine anti-scam warning;
- ordinary investment discussion;
- financial education;
- general market commentary;
- personal investment journaling;
- legitimate finance creator content;
- educational charts/screenshots;
- public website/contact without investment funnel;
- news discussion;
- risk warning content.

Mandatory second-review triggers:

- anti-scam language plus possible funnel cue;
- teacher/advisor framing without contact or proof;
- profit-proof without conversion path;
- public contact information without investment funnel;
- profile-context pattern as main evidence;
- OCR-dependent candidate;
- investment vocabulary only;
- ordinary group/community discussion.

## Stop Rules

| Stop event | Required action |
|---|---|
| Raw evidence leak | immediate stop, incident note, no further intake |
| Hard-negative false-positive cluster | pause affected source arm |
| Duplicate rate > 35% | pause source arm and revise dedupe method |
| Reviewer burden > 18 minutes average | pause intake |
| Second-review rate > 55% | pause and revise rubric |
| Disagreement rate > 30% | pause and recalibrate reviewers |
| Insufficient-evidence rate > 40% | pause source method |
| Private-message boundary pressure | stop affected candidate path |
| Legal/privacy uncertainty for required execution surface | no execution |
| Baseline described as enforcement tool | pause reporting and correct wording |
| Source cap pressure | stop at cap; no overflow queue |
| UI or evidence-surface changes | pause and revalidate capture assumptions |

Each stop event must record:

```text
stop_rule_owner
incident_note_id
affected_source_family
affected_signal_family
pause_required
resume_condition
```

## Legal/Privacy Execution Gate

Legal/privacy review is required before execution, not before drafting this decision.

Before execution, legal/privacy reviewers must answer:

- Can reviewer-supplied candidates be used?
- Can approved browser-session candidates be used?
- Can OCR-derived text be processed?
- Can profile-context category be recorded?
- Can external-link/contact category be recorded?
- What must remain controlled-store-only?
- What is the retention period?
- What is the redaction standard?
- Who owns deletion or incident handling?
- Can aggregate outputs be shared beyond CIB/internal?

If any required legal/privacy answer is unresolved, execution remains blocked.

## Controlled-Store and Redaction Boundary

Tracked repo artifacts may include:

- repo-safe candidate IDs;
- source-family names;
- source-arm names;
- signal-family labels;
- evidence-surface presence flags;
- category-level contact or external-link indicators;
- dedupe status;
- review time;
- labels and risk tiers;
- aggregate metrics;
- redacted reviewer notes.

Controlled-store-only material includes:

- raw Threads URLs;
- raw handles;
- screenshots;
- raw post text;
- raw reply/comment text;
- contact IDs;
- stock names or stock codes when sensitive to the case context;
- price values when sensitive to the case context;
- browser/session artifacts;
- credentials, tokens, cookies, HAR files, or storage state;
- exact controlled-store paths;
- stakeholder case IDs;
- private recipient details.

## Aggregate Reporting Template

Any future execution report must include:

- source-arm candidate count;
- source-arm reviewed count;
- review-worthy yield;
- high-risk yield;
- final scam-label yield;
- duplicate rate;
- insufficient-evidence rate;
- hard-negative count;
- hard-negative false-positive pressure;
- average review time;
- second-review rate;
- disagreement rate;
- stop-rule incidents;
- legal/privacy gate status;
- strict validation status;
- non-authorization statement.

Reports must avoid raw evidence, operational enforcement recommendations, public warning lists, and legal fraud determinations.

## Required Execution Gates

Execution requires all of the following before any method-test candidate discovery begins:

- final approval of this decision;
- legal/privacy status recorded;
- reviewer roles assigned;
- source-family caps approved;
- surfaced-candidate cap approved;
- human-review cap approved;
- accepted-record cap approved;
- intake window approved;
- controlled-store handling recorded;
- retention and redaction rules recorded;
- strict validation command recorded;
- dedupe method recorded;
- hard-negative second-review triggers recorded;
- stop-rule owner assigned;
- aggregate reporting template recorded;
- no production, enforcement, or legal-determination language.

## Future Go / No-Go Criteria

Future execution may be approved only if the final decision contains:

- fixed candidate cap;
- fixed accepted-record cap;
- fixed intake window;
- source-family caps;
- reviewer role assignment;
- legal/privacy status;
- controlled-store handling;
- redaction rule;
- strict validation command;
- dedupe method;
- hard-negative second-review triggers;
- stop-rule owner;
- aggregate reporting template;
- explicit non-authorizations.

Missing any one of these means no execution.

## Non-Authorizations

This draft does not authorize:

- execution;
- item `0082`;
- new evidence collection;
- open-ended collection;
- broad crawler/browser expansion;
- confirmed-pointer intake;
- account/profile graph capture;
- private-message access;
- landing-page or redirect-chain capture;
- embedding/model training;
- production detector claims;
- legal fraud determinations;
- automated enforcement;
- public release;
- raw evidence in git.

## Next Step

Send this draft for technical/governance and legal/privacy review. Reviewers should decide whether to:

- approve the draft for final capped execution decision preparation;
- approve with conditions;
- request revision before execution decision;
- block the method-test design.
