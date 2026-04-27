# Checkpoint 0081 Shadow Pilot Readiness Gap Analysis

## Purpose

Assess what is still required before checkpoint `threads_pilot_v1_0081` can be considered for a shadow-only operational pilot design that tests the investment-scam candidate-discovery method.

This document does not authorize:

- item `0082`;
- new evidence collection;
- browser or crawler expansion;
- confirmed-pointer intake;
- account/profile graph capture;
- private-message access;
- landing-page or redirect-chain capture;
- embedding or model training;
- production detection;
- legal fraud determination;
- external sharing;
- public release;
- raw evidence in git.

The purpose is to identify gates, SOPs, metrics, reviewer workflow requirements, legal/privacy boundaries, and stop rules required before any shadow-only pilot can be considered. The underlying first-principle goal remains scalable, stable, and reviewable discovery of Threads investment-scam candidates.

## Current Status

| Field | Status |
|---|---|
| Checkpoint | `threads_pilot_v1_0081` |
| Current records | 78 strict-valid records |
| Label distribution | 36 `scam`, 24 `non_scam`, 13 `uncertain`, 5 `insufficient_evidence` |
| Risk distribution | 36 `high`, 11 `medium`, 31 `low` |
| Strict validation | 0 errors, 0 warnings |
| Baseline smoke result | precision 0.829, recall 0.944, F1 0.883 |
| Baseline error profile | 7 false positives, 2 false negatives |
| Current adoption state | CIB/internal `accepted_with_conditions` |
| Current authorized use | internal research checkpoint, evidence-system review, annotation-rule calibration, governance review, report/package handoff, future research planning |
| Current collection state | no prospective tranche open |

Checkpoint 0081 is ready for internal research use. It is not ready for production use, automated enforcement, broad deployment, public release, or legal fraud determination.

## What Is Already Ready

- 78 strict-valid records.
- CIB-approved research checkpoint framing.
- CIB/internal adoption recorded as `accepted_with_conditions`.
- Annotation schema and thread item schema.
- Labeling guideline with hard-negative boundaries.
- Second-review practice for ambiguous and medium-risk records.
- Confirmed-pointer intake method for controlled future evidence, if separately authorized.
- Full-text and reply controlled-capture method as a governance pattern.
- Baseline smoke evaluation with explicit caveats.
- Package QA, checksum, and leakage-scan workflow.
- Redaction boundary for tracked repo artifacts.
- Recipient adoption tracker and dispatch workflow.
- First-principle investment-scam discovery-method guidance in `docs/56-first-principle-investment-scam-discovery-method.md`.

## What Is Not Yet Ready

- Technical/governance recipient adoption is still not recorded as accepted.
- Legal/privacy clearance for broader external sharing is not recorded.
- No operational reviewer SOP exists for a real workflow.
- No approved shadow-pilot candidate intake rule exists.
- No reviewer burden measurement template exists.
- No operational escalation rule exists for ambiguous, insufficient, or disagreement cases.
- No stop/no-go threshold has been adopted.
- No retention and audit workflow exists for shadow-pilot outputs.
- No role responsibility matrix exists for CIB reviewer, technical reviewer, governance owner, and legal/privacy reviewer.
- No separate decision authorizes a shadow pilot.
- No capped candidate-discovery method-test decision exists yet.

## Readiness Gates

### Gate 1: Recipient Adoption

| Question | Current Answer | Required Before Shadow Pilot |
|---|---|---|
| Who accepts checkpoint 0081? | CIB/internal reviewer accepted with conditions | Record technical/governance adoption and any legal/privacy constraints required for the intended recipient boundary |
| Accepted for what? | Internal research checkpoint use | Keep use limited to review, calibration, governance, and planning unless a later decision expands scope |
| Is broader sharing allowed? | No, not yet | Record legal/privacy status before external sharing |
| Is public release allowed? | No | Keep public release blocked unless a later explicit decision authorizes it |

### Gate 2: Technical And Governance Review

Technical/governance review should verify:

- schema contracts are sufficient for shadow-pilot review records;
- validation can distinguish schema validity from evidence approval;
- baseline caveats are visible wherever metrics appear;
- redaction and raw-evidence boundaries are enforceable;
- package manifests and checksums are reproducible;
- reviewer workflow fields can be captured without adding sensitive raw evidence to git.

### Gate 3: Legal And Privacy Boundary

Before any broader sharing or shadow operational workflow, legal/privacy status must decide:

- who may view the package;
- whether any controlled evidence may be referenced outside the current boundary;
- retention rules for review outputs;
- whether reviewer notes can include sensitive investigative details;
- what must stay out of git and out of any exported package;
- whether aggregate-only reporting is required;
- whether additional consent, authorization, or platform-policy review is required.

### Gate 4: Shadow Pilot SOP

A future SOP must define the operational loop before any shadow-only pilot begins:

1. Candidate received through an approved source.
2. Candidate assigned a repo-safe candidate ID.
3. Evidence surfaces reviewed under the approved boundary.
4. Primary reviewer records initial label, risk, evidence surfaces, reason codes, and review time.
5. Second review occurs when risk, uncertainty, or disagreement rules require it.
6. Final adjudication records final label, final risk, disagreement type, and unresolved caveats.
7. Aggregate report records counts, error patterns, reviewer burden, and stop-rule status.
8. No automated action is taken against users, posts, accounts, or external sites.

### Gate 5: Metrics And Error Adjudication

Shadow pilot metrics should not be limited to precision and recall.

| Metric | Why It Matters |
|---|---|
| reviewer time per candidate | Tests whether the workflow is operationally sustainable |
| second-review rate | Measures how often the rules are not decisive enough for one reviewer |
| disagreement rate | Measures annotation clarity and reviewer alignment |
| hard-negative protection rate | Tests protection for anti-scam warnings and ordinary investment discussion |
| uncertain rate | Reveals how often evidence is still too thin |
| insufficient-evidence rate | Reveals capture-boundary weakness |
| false-positive pressure | Measures legal, governance, and trust risk |
| false-negative pressure | Measures risk of missing high-risk funnel behavior |
| rule-family coverage | Shows whether rule families cover actual reviewer reasoning |
| evidence-surface coverage | Shows whether post, reply, OCR, link, profile-context, and controlled notes are being used correctly |
| escalation clarity | Tests whether reviewers know when to escalate or stop |
| discovery-yield quality | Shows whether the method finds enough review-worthy investment-scam candidates to justify scaling |

Recommended repo-safe review fields:

```text
candidate_id
reviewer_role
review_round
initial_label
final_label
initial_risk
final_risk
rule_family_triggered
evidence_surface_used
review_time_minutes
needs_second_review
disagreement_type
false_positive_pressure
false_negative_pressure
hard_negative_flag
uncertain_reason
insufficient_evidence_reason
escalation_required
stop_rule_triggered
repo_safe_notes
```

### Gate 6: Stop Rules

A future shadow-only pilot should stop or pause if any of these occur:

- raw evidence leakage risk appears;
- reviewer disagreement exceeds the threshold set by the pilot decision;
- hard-negative false positives cluster around ordinary investment discussion, anti-scam warnings, or non-directed financial education;
- false negatives cluster around private-channel migration, comment-layer contact hijack, or trust-building stories;
- private-message access becomes necessary to make core judgments;
- legal/privacy status remains unresolved for required sharing;
- baseline output is misunderstood as an enforcement recommendation;
- candidate intake pressure exceeds the approved cap;
- platform UI or evidence surfaces change enough to invalidate capture assumptions;
- reviewer burden exceeds the approved time budget;
- controlled-store or redaction workflow cannot be verified.

## Proposed Shadow Pilot Boundary

Any future shadow pilot should be:

- shadow-only;
- human-review only;
- no automated action;
- no platform enforcement;
- no account targeting;
- no public warning list;
- no case referral automation;
- no production claim;
- no legal fraud determination;
- no public release;
- no raw evidence in git;
- fixed candidate cap only after a separate decision;
- repo-safe aggregate reporting only;
- strict-validation required;
- second-review required for specified conditions;
- legal/privacy-gated before broader sharing.

## Allowed Design Use Cases

The readiness work may prepare for these possible use cases:

- reviewer calibration;
- rule-family stress test;
- false-positive pressure review;
- uncertain and insufficient-evidence handling;
- reviewer burden measurement;
- handoff workflow rehearsal;
- governance boundary testing;
- hard-negative protection review.
- investment-scam candidate-discovery method stress testing.

It must not prepare an unapproved operational detector, enforcement queue, account list, public warning list, model-training dataset, or legal fraud determination process.

## Evidence Intake Boundary For Any Future Pilot

Candidate intake for any future shadow pilot must require a separate capped decision record.

Preferred future sources, if separately authorized:

- CIB-supplied confirmed pointers;
- reviewer-supplied candidates;
- existing redacted checkpoint materials;
- strictly capped calibration candidates.

Not authorized by this analysis:

- open-ended crawler;
- broad keyword search;
- account/profile graph capture;
- private-message capture;
- landing-page or redirect-chain capture;
- automatic ingestion from public search or browser sessions.

## Key Risks

| Risk | Why It Matters | Control Needed |
|---|---|---|
| False positives against legitimate investment discussion | Can harm lawful speech and reduce reviewer trust | Hard-negative rules and second review |
| Anti-scam warning misclassification | Warning content may use scam vocabulary without being scam | Context-aware hard-negative policy |
| Missing reply/comment context | Scam funnel cues may appear outside top-level post | Full-thread/reply readiness gate |
| Private-channel migration invisibility | The highest-risk step may happen after DM migration | Preserve uncertainty and do not infer beyond evidence |
| Reviewer burden | Manual review may not scale | Time-per-candidate metric and cap |
| Baseline overinterpretation | Smoke metrics may be mistaken for production performance | Baseline caveat in every package and report |
| Governance drift | Design work may be mistaken for collection or deployment approval | Decision-log non-authorizations and stop rules |
| Redaction failure | Sensitive evidence could leak into repo-safe artifacts | Leakage scan, manifest review, controlled-store boundary |

## Recommended Next Decision

Open a design-only shadow pilot charter draft only after this gap analysis is reviewed. The draft should frame any future pilot as a capped investment-scam candidate-discovery method test, not as deployment.

No pilot execution should begin until a separate capped decision records:

- source boundary;
- candidate cap;
- selected item cap, if any;
- reviewer roles;
- legal/privacy status;
- evidence surfaces allowed;
- controlled-store handling;
- redaction rules;
- validation commands;
- second-review conditions;
- metrics;
- stop rules;
- reporting format;
- explicit non-authorizations.
- discovery-yield and reviewer-burden success criteria.

## Bottom Line

Checkpoint 0081 is strong enough for internal research adoption and readiness planning.

It is not yet strong enough for real-world deployment. The next real progress is not more data by default. The next real progress is proving that the investment-scam candidate-discovery method, review workflow, evidence boundary, reviewer burden, legal/privacy gate, metrics, and stop rules can survive a shadow-only operational design review.
