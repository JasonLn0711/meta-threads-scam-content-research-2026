# Checkpoint 0081 Investment-Scam Discovery Method Test Charter Draft

## Status

Draft only.

This document does not authorize execution.

This document does not authorize:

- item `0082`;
- new evidence collection;
- browser or crawler expansion;
- confirmed-pointer intake;
- account/profile graph capture;
- private-message access;
- landing-page or redirect-chain capture;
- embedding or model training;
- production detector claims;
- legal fraud determination;
- public release;
- automated enforcement;
- raw evidence in git.

Any future candidate-discovery method test requires a separate capped decision record before execution.

## First-Principle Goal

Develop a scalable, stable, and reviewable method for discovering Threads investment-scam candidates.

The method is designed to discover review-worthy investment-scam candidates at scale. It is not designed to automatically determine fraud, guilt, takedown eligibility, enforcement priority, or legal liability.

## Discovery Target

Investment-scam risk is not always post-level. The method should reason across four candidate units:

| Candidate unit | Meaning | Why it matters |
|---|---|---|
| post candidate | A single top-level post contains visible investment-scam risk signals | Useful when the lure is explicit in the main post |
| thread candidate | The top-level post plus replies/comments form the risk pattern | Many funnels are hidden in comments or reply coordination |
| account-context candidate | Profile text, repeated behavior, or account-level posting pattern strengthens the candidate | Investment scam accounts may use repeated multi-style posts and profile-level trust framing |
| funnel candidate | Threads content points toward DM, LINE, Telegram, WhatsApp, group, external site, or other conversion path | The risky step may happen after platform migration |

The test should measure which unit level produces the best review-worthy yield without overflagging hard negatives.

## Candidate Discovery Hypotheses

The draft method test should evaluate these hypotheses:

| Hypothesis | Reason To Test |
|---|---|
| Reply/comment funnel cues reveal risk missed by top-level post review | Scam posts often keep the main post vague and put contact or group movement in replies |
| Private-channel migration cues improve high-risk yield | DM, add-friend, group, LINE, Telegram, WhatsApp, and similar movement are common conversion steps |
| OCR/image-derived proof claims improve discovery | Profit proof, screenshots, testimonials, and financial claims may be image-only |
| Teacher/advisor framing improves candidate quality | Investment-scam funnels often rely on authority, assistant, teacher, mentor, or expert roles |
| Hard-negative contrast is required to control false positives | Anti-scam warnings and ordinary investment discussion share vocabulary with scams |
| Account-context signals may improve prioritization when bounded | Repetition and profile framing can help, but graph capture and broad profile review remain out of scope unless separately authorized |

## Signal Families

The method should use signal families, not single keywords.

| Signal family | Example surface | Discovery value | False-positive risk | Needs reply? | Needs OCR? | Hard-negative contrast |
|---|---|---:|---:|---:|---:|---|
| investment domain seed | stocks, investing, wealth management, crypto, options, funds | medium | high | no | no | ordinary investment discussion |
| private-channel migration | DM, add friend, LINE, Telegram, WhatsApp, Messenger, group movement | high | medium | sometimes | no | normal contact info without investment funnel |
| reply/comment funnel cue | comment-layer contact cue, safe-contact claim, reply coordination | high | medium | yes | no | ordinary Q&A or warning comments |
| profit-proof | earnings sheet, return screenshot, success proof, gain claims | high | medium | no | often | normal portfolio/performance discussion |
| teacher/advisor framing | teacher, assistant, analyst, mentor, expert, helper | high | medium | sometimes | no | financial education without funnel |
| group invitation | stock group, daily watchlist, holdings clinic, join community | high | medium | sometimes | no | ordinary community discussion |
| testimonial/witness cue | other accounts praise results or claim joining helped | medium-high | medium | yes | sometimes | real user feedback without conversion path |
| reassurance/no-fee/safety language | not charging, just sharing, anti-scam, safe channel | medium | high | sometimes | no | genuine anti-scam warning |
| external-link/contact signal | visible link/contact type/domain category | high | medium-high | sometimes | no | legitimate public website or official profile |
| OCR-derived financial claim | image-only returns, stock names, group QR, testimonial, contact text | high | medium | no | yes | educational chart or ordinary screenshot |
| profile-context pattern | repeated investment persona, repeated calls to group/DM, multi-style funnel | medium-high | high | no | no | ordinary finance creator profile |
| hard-negative boundary | anti-scam warning, general market commentary, non-directed education | protective | n/a | sometimes | sometimes | n/a |

The companion matrix is maintained in [../docs/57-investment-scam-discovery-signal-family-matrix.md](../docs/57-investment-scam-discovery-signal-family-matrix.md).

## Candidate Source Boundary

No source is authorized by this draft.

A future capped decision must specify:

- source type;
- candidate cap;
- accepted-record cap, if any;
- intake window;
- reviewer roles;
- evidence boundary;
- redaction rule;
- controlled-store handling;
- stop rules;
- validation commands;
- reporting format.

Potential source families to compare only after separate approval:

- CIB/stakeholder confirmed pointers;
- reviewer-supplied candidates;
- approved browser-session candidates under explicit caps;
- diversified risk-probe seed matrices;
- existing checkpoint records and hard negatives.

Not authorized by this draft:

- open-ended crawler;
- broad keyword scrape;
- graph capture;
- private-message access;
- landing-page or redirect-chain capture;
- automatic ingestion from public search or browser sessions.

## Discovery Workflow

Future execution, if separately authorized, should follow this shape:

```text
candidate surfaced
→ repo-safe candidate triage note
→ dedupe and source-linkage check
→ full-thread/reply-readiness check
→ human primary review
→ second review if triggered
→ final label and risk assignment
→ strict validation
→ aggregate-only reporting
```

No automated action should be taken against users, posts, accounts, links, groups, or external sites.

## Metrics

The test should be judged by discovery usefulness, not only label-level precision/recall.

| Metric | Question Answered |
|---|---|
| candidate yield | Per 100 candidates, how many are worth reviewer attention? |
| high-risk yield | Per 100 candidates, how many become `high` risk after review? |
| scam-label yield | Per 100 candidates, how many become final `scam` after review? |
| duplicate rate | Is the method repeatedly finding the same or near-same content? |
| reviewer time per candidate | Is the workflow humanly sustainable? |
| second-review rate | Are the rules stable enough for primary review? |
| disagreement rate | Do reviewers interpret signals consistently? |
| hard-negative false-positive pressure | Is the method overflagging ordinary investment discussion or anti-scam warnings? |
| false-negative pressure | Are high-risk funnel signals still being missed? |
| insufficient-evidence rate | Is the method surfacing too many context-thin candidates? |
| thread-context dependency | How often is reply/comment context needed for the decision? |
| OCR dependency | How often is image-derived text decisive? |
| private-channel migration rate | How often do candidates contain DM/add-friend/group/contact movement? |
| profile-context dependency | How often is bounded account/profile context useful? |

## Review Fields

A future method-test record or review sheet should include repo-safe versions of:

```text
candidate_id
candidate_unit
source_family
signal_families_triggered
evidence_surfaces_available
dedupe_status
full_thread_ready
ocr_needed
profile_context_needed
primary_reviewer_role
review_time_minutes
initial_label
initial_risk
second_review_required
second_review_reason
final_label
final_risk
hard_negative_flag
uncertain_reason
insufficient_evidence_reason
false_positive_pressure
false_negative_pressure
stop_rule_triggered
repo_safe_notes
```

Raw URLs, handles, screenshots, raw post text, raw reply text, contact IDs, stock codes, credentials, browser/session artifacts, controlled-store paths, and stakeholder case IDs must stay out of tracked repo artifacts unless a later decision explicitly changes the boundary.

## Hard-Negative Protection

The method must protect:

- genuine anti-scam warnings;
- ordinary investment discussion;
- non-directed financial education;
- general market commentary;
- personal investment journaling without contact, proof, or conversion cues;
- legitimate public contact information without investment funnel behavior;
- educational charts or screenshots without deceptive conversion path.

Hard-negative review should be explicit because investment scam discovery will share vocabulary with legitimate finance content.

## Stop Rules

Stop or pause any future method test if:

- raw evidence leakage risk appears;
- false-positive clusters emerge;
- hard-negative protection fails;
- reviewer burden exceeds the approved cap;
- private-message boundary pressure appears;
- legal/privacy status is unresolved for the intended sharing boundary;
- candidate intake pressure exceeds the approved cap;
- baseline output is treated as enforcement recommendation;
- platform UI or evidence surfaces invalidate capture assumptions;
- dedupe/source-linkage failure creates repeated review load;
- controlled-store or redaction workflow cannot be verified.

## Expansion Criteria

Only consider expanding beyond investment scams if:

- investment-scam candidate yield is meaningful;
- final scam/high yield justifies reviewer burden;
- duplicate rate is manageable;
- hard-negative false positives are controlled;
- thread/reply and OCR dependencies are understood;
- signal families are stable enough to transfer;
- legal/privacy status is recorded;
- technical/governance review accepts the method.

Likely later scam families include romance/fake-friendship openings, escort/adult-service scam openings, loan or debt-relief scams, job scams, shopping/fake seller scams, pseudo-official service scams, and charity/recovery/public-good trust scams.

## Required Decision Before Execution

This draft can be reviewed and revised without new evidence.

Execution requires a later capped decision that records:

- source boundary;
- candidate cap;
- accepted-record cap, if any;
- evidence surfaces;
- reviewer roles;
- legal/privacy status;
- retention/redaction boundary;
- controlled-store handling;
- validation command;
- second-review triggers;
- metrics;
- stop rules;
- reporting format;
- explicit non-authorizations.

## Recommended Next Review

Ask technical/governance reviewers whether this charter has enough structure to support a safe capped method-test decision later.

Do not execute the method test from this draft alone.
