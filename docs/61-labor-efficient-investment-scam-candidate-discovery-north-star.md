# Labor-Efficient Investment Scam Candidate Discovery North Star

## 1. Updated North-Star Statement

From this point forward, the repo's core goal is:

```text
Build a scalable, stable, reviewable, and labor-efficient method for discovering enough review-worthy Threads investment-scam candidates with as little human review burden as possible.
```

The operational goal is not merely to find scam posts. The operational goal is to use a small amount of human labor to find enough candidates worth reviewing.

This repo remains a documentation-first research scaffold. It does not become a production detector, legal fraud determination system, enforcement system, public warning channel, broad crawler, or raw-evidence store.

## 2. Why "Finding Scams" Is Not Enough

"Find scam posts" is too weak as a research objective because it hides the actual bottleneck: reviewer labor.

A method can surface many suspicious-looking Threads items and still fail operationally if reviewers must manually read long threads, inspect replies, parse OCR text, copy fields, summarize evidence, identify signal families, check hard negatives, and write repo-safe notes for every candidate.

A scalable scam-discovery method must reduce human labor by design. If the method requires reviewers to manually read, interpret, copy, summarize, and structure every candidate, it is not scalable even if its detection yield looks promising.

The project should therefore evaluate whether a method produces review-worthy candidates at usable volume with an acceptable review burden, not whether it can simply label more items as suspicious.

## 3. The Coupled Relationship Between Discovery Yield And Reviewer Burden

Scalable discovery and labor reduction are coupled success conditions.

A method that finds many candidates but requires excessive manual reading, sorting, and schema filling is not operationally scalable.

A method that saves reviewer time but fails to surface enough review-worthy candidates is not useful.

The research should optimize the joint outcome:

- high review-worthy candidate yield;
- acceptable reviewer burden;
- controlled false-positive pressure;
- hard-negative protection;
- governance-safe evidence handling.

Labor reduction is not a secondary convenience. It is an operational feasibility constraint and a core research success condition.

## 4. The Real Operational Unit: Review-Worthy Candidate, Not Legal Fraud Determination

The real unit of work is the review-worthy candidate.

A review-worthy candidate is a Threads item, thread, funnel clue, or bounded account-context trace that has enough repo-safe, source-linked, evidence-preserving context to justify human review under the current authorization boundary.

A review-worthy candidate may ultimately be labeled `scam`, `non_scam`, `uncertain`, or `insufficient_evidence`. Review-worthy does not mean legally fraudulent. It means the candidate is worth spending scarce reviewer time on.

The repo should preserve the distinction between:

- candidate discovery;
- risk triage;
- evidence sufficiency;
- human label decision;
- second review or adjudication;
- legal, policy, or enforcement decisions outside this repo's authority.

## 5. What AI/System Support May Do

AI and system support may reduce the most time-consuming human tasks when authorized and repo-safe.

Allowed support includes:

- reading long threads and preparing concise reviewer-oriented summaries;
- summarizing posts, replies, comments, and OCR content;
- extracting visible investment-scam signal families;
- pre-filling schema fields from already authorized evidence;
- ranking candidate priority for human review;
- identifying possible hard-negative risk;
- highlighting missing evidence and uncertainty;
- deduplicating or linking candidate sources;
- preparing repo-safe reviewer notes;
- measuring reviewer burden and candidate yield;
- producing aggregate reports without raw evidence in git.

All such outputs must preserve evidence references, uncertainty, and reviewer override.

## 6. What AI/System Support Must Not Do

AI and system support must not:

- make final legal fraud determinations;
- make final scam-label decisions without human review;
- recommend enforcement, takedown, account action, or public warning;
- claim production detector status;
- infer private-message content that was not observed;
- expand into private-message access;
- capture account/profile graphs without separate authorization;
- perform landing-page or redirect-chain capture unless separately authorized;
- conduct broad crawler/browser expansion unless separately authorized;
- train models unless separately authorized;
- commit raw evidence, credentials, browser exports, screenshots with unnecessary personal data, or sensitive investigative material to git.

## 7. Human Role After Automation

Human reviewers remain responsible for:

- final label decisions;
- final risk-level decisions;
- evidence sufficiency judgments;
- uncertainty handling;
- hard-negative acceptance;
- second review and adjudication;
- exception escalation;
- governance boundary interpretation;
- deciding whether a method is useful enough to continue, revise, pause, or stop.

Automation should make those decisions faster and better supported. It should not remove human accountability.

## 8. Success Metrics

Future experiments and reports should measure both yield and labor.

| Metric | Why it matters |
|---|---|
| average review time per candidate | Mean reviewer labor burden |
| median review time | Typical reviewer burden without outlier distortion |
| p95 review time | Worst-tail burden and scaling risk |
| candidates reviewed per hour | Practical throughput |
| percentage of fields auto-filled | Degree of schema-filling assistance |
| percentage of fields manually corrected | Quality cost of automation |
| summary usefulness rating | Whether summaries reduce reading burden |
| percentage of candidates requiring full original-thread reading | Residual manual-reading burden |
| second-review rate | Complexity and review-stability pressure |
| reviewer disagreement rate | Label clarity and guidance pressure |
| hard-negative false-positive pressure | Risk of overflagging ordinary or warning content |
| insufficient-evidence rate | Capture or evidence-completeness pressure |
| review-worthy yield per source arm | Source-arm discovery usefulness |
| high-risk yield per reviewer hour | Joint yield and labor-efficiency outcome |

Precision, recall, and F1 can remain useful for controlled slices, but they are not enough to judge whether a discovery method is operationally feasible.

## 9. Failure Modes

Important failure modes include:

- high candidate volume but too much manual reading per candidate;
- fast review flow but too few review-worthy candidates;
- schema prefill that creates hidden correction burden;
- summaries that omit decisive reply, OCR, or hard-negative context;
- ranking that over-prioritizes investment vocabulary without funnel evidence;
- hard-negative false positives against ordinary investment discussion or anti-scam warnings;
- excessive second-review load;
- high insufficient-evidence rate from context-thin captures;
- duplicate or source-linkage failure that wastes reviewer time;
- governance drift into raw-evidence handling, private-message inference, crawler expansion, model training, enforcement claims, or production-detector claims;
- UI/API/schema demo work being mistaken for the research output.

## 10. How This Changes Future Repo Work

From this point forward, future repo work should ask:

```text
Does this change improve labor-efficient discovery of review-worthy Threads investment-scam candidates?
```

Current Track B work should be interpreted as testing:

1. candidate discovery yield;
2. reviewer burden;
3. hard-negative false-positive pressure;
4. feasibility of AI/system-assisted reviewer workflow.

The next research layer after Track B should include:

- reviewer assist layer design;
- schema prefill evaluation;
- summary-assisted review evaluation;
- priority-ranking evaluation;
- labor-savings measurement;
- decision-support UI/API demonstration.

UI, API, schema, and package demos are demonstration surfaces. The research output is the validated method and workflow: what source arms work, what evidence is needed, how much reviewer labor is required, what automation can safely reduce, and where humans must remain in control.

Do not open item `0082`, open-ended collection, broad crawler/browser expansion, private-message access, account/profile graph capture, landing-page or redirect-chain capture, model training, production detector claims, legal fraud determinations, automated enforcement, public release, or raw evidence in git unless a separate decision explicitly authorizes that scope.

## 11. What Historical Materials Remain Unchanged

Historical checkpoint records, prior reports, Track A/Track B history, decision logs, experiment notes, package QA records, and reviewer-delivery artifacts remain unchanged unless a later task explicitly asks to update a forward-looking routing note.

This document does not rewrite prior history. It sets the forward-looking interpretation of repo work from this point onward.

