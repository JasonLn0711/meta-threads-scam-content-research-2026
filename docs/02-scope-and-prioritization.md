# Scope And Prioritization

## Phase-1 Recommendation

Start with a focused investment-scam candidate-discovery method on Threads. From this point forward, the method must be scalable, stable, reviewable, and labor-efficient: it should discover enough review-worthy investment-scam candidates with as little human review burden as possible.

Use text, images, comments/replies, OCR, visible redirection signals, and CIB-authorized API/automation support only when they directly improve the joint outcome: review-worthy yield, acceptable reviewer burden, controlled false-positive pressure, hard-negative protection, and governance-safe evidence handling.

Defer video-heavy, deepfake-heavy, cross-family expansion, and production-enforcement work until the investment-scam discovery method shows useful yield, acceptable reviewer burden, hard-negative protection, and measured labor efficiency.

## Labor-Efficient Discovery Boundary

Do not frame the scope as "detect investment scams first, reduce labor second." Discovery yield and reviewer burden are coupled success conditions.

- A method that finds many candidates but requires excessive manual reading, sorting, summarization, copying, schema filling, and second review is not operationally scalable.
- A method that saves reviewer time but fails to surface enough review-worthy candidates is not useful.
- AI/system support may assist with long-thread reading, OCR/post/reply summarization, signal-family extraction, schema prefill, priority ranking, hard-negative risk identification, and repo-safe reviewer notes.
- AI/system support must not make final labels, legal fraud determinations, enforcement recommendations, public warnings, automated takedowns, production detector claims, or scope-expansion decisions.

## Scope Matrix

| Content surface | Investigative value | Technical feasibility | Annotation burden | Compute cost | False positive risk | Phase recommendation | Include now |
|---|---:|---:|---:|---:|---:|---|---|
| Text posts | High | High | Low to medium | Low | Medium | Core phase 1 | Yes |
| Text plus image posts | High | Medium | Medium | Low to medium | Medium | Core phase 1 with OCR | Yes |
| Comments / replies | High | Medium | Medium to high | Low | Medium | Core phase 1 sample | Yes |
| OCR from images | High | Medium | Medium | Low to medium | Medium | Add after text baseline | Yes |
| External links | High | Medium | Medium | Low | High | Capture visible, API, redirect, and landing signals only under CIB run records | Yes |
| API and automation support | High | Medium | Medium | Low to medium | High | Include as governed CIB-authorized collection and processing support | Yes, controlled |
| Screenshot-heavy posts | Medium to high | Medium | High | Low to medium | Medium | Include selectively with privacy controls | Yes, selective |
| Short video | Medium | Low to medium | High | Medium to high | High | Later study only if sample demands it | Later |
| Long video | Low to medium | Low | Very high | High | High | Defer | No |
| Deepfake-related signals | Future risk value | Low | Very high | High | Very high | Defer to future risk note | No |

## Required Forward-Looking Metrics

Future scope, experiment, and continuation decisions should include:

- average review time per candidate;
- median review time;
- p95 review time;
- candidates reviewed per hour;
- percentage of fields auto-filled;
- percentage of fields manually corrected;
- summary usefulness rating;
- percentage of candidates requiring full original-thread reading;
- second-review rate;
- reviewer disagreement rate;
- hard-negative false-positive pressure;
- insufficient-evidence rate;
- review-worthy yield per source arm;
- high-risk yield per reviewer hour.

## Detailed Research Judgment

### 0. Investment Scam Candidate Discovery

Prioritize now.

- Technical cost: manageable if the method stays bounded and review-centered.
- Operational cost: medium. Full-thread/reply review and hard-negative protection require reviewer time.
- Evidence value: high. Investment-scam patterns expose repeated signal families such as teacher/advisor framing, profit proof, group conversion, private-channel migration, comment-layer reassurance, and external-link/contact cues.
- Budget fit: strong if the repo measures discovery yield and reviewer burden together before expanding.
- Expansion logic: later scam families should be added only after the investment-scam method is useful enough to adapt.

### 1. Text Posts

Include now.

- Technical cost: low. Keyword, pattern, and rule baselines can all operate on text.
- Operational cost: low to medium. Reviewers can annotate posts quickly if guidance is clear.
- Evidence value: high. Scam lures often expose promises, urgency, fake authority, and redirection.
- Budget fit: strong. This is the cheapest defensible starting point.

### 2. Text Plus Image Posts

Include now, but process images through lightweight OCR first.

- Technical cost: medium. Needs image storage discipline, OCR, and text normalization.
- Operational cost: medium. Reviewers must inspect both post text and extracted image text.
- Evidence value: high. Scam claims, testimonials, fake checks, charts, and contact details may be embedded in images.
- Budget fit: strong if limited to OCR and human review, weak if it expands into heavy vision modeling.

### 3. Comments / Replies

Include now as a sampled workstream.

- Technical cost: low to medium. Text processing is simple, but thread structure must be represented.
- Operational cost: medium to high. More text increases reviewer time.
- Evidence value: high. Scam actors may keep the original post vague and place redirection in replies.
- Budget fit: good if sampled and compared against post-only baselines.

### 4. OCR Text From Images

Include now after the first text baseline.

- Technical cost: medium. OCR errors and multilingual text require normalization.
- Operational cost: medium. Annotators need to verify whether OCR captured the relevant image claim.
- Evidence value: high. OCR can expose claims hidden from text-only analysis.
- Budget fit: strong for a lightweight pipeline and ablation study.

### 5. External Links

Include visible link and redirection signals now, but do not crawl without approval.

- Technical cost: low for visible URL parsing, medium if domain normalization is added.
- Operational cost: medium. Reviewers need rules for suspicious versus legitimate links.
- Evidence value: high. Redirection to private channels or suspicious domains is often operationally important.
- Budget fit: strong for metadata and visible-link features, poor for unauthorized crawling.

### 6. Screenshot-Heavy Posts

Include selectively.

- Technical cost: medium. Screenshots require OCR and careful path management.
- Operational cost: high. Screenshots may contain irrelevant personal information and require redaction.
- Evidence value: medium to high. Screenshots can carry fake endorsements, testimonials, or proof-of-profit claims.
- Budget fit: acceptable only with privacy minimization and sample limits.

### 7. API And Automation Support

Include now under the CIB controlled launch record.

- Technical cost: medium. Automation reduces collection and normalization friction but introduces credential, logging, and redaction duties.
- Operational cost: medium. Every run needs purpose, operator, source, field, output, retention, and stop-condition records.
- Evidence value: high. API and automation can make source capture more complete, reproducible, and auditable.
- Budget fit: good if limited to governed collection, OCR, parsing, validation, audit, and baseline automation; poor if it expands into production monitoring or enforcement.

### 8. Short Video

Defer unless stakeholders show that short videos dominate the report queue.

- Technical cost: medium to high. Requires frame sampling, transcription, and media handling.
- Operational cost: high. Annotation takes longer and evidence is harder to quote.
- Evidence value: uncertain for phase 1.
- Budget fit: weak for the first 4 weeks, possible as a later narrow study.

### 9. Long Video

Defer.

- Technical cost: high.
- Operational cost: very high.
- Evidence value: uncertain relative to cost.
- Budget fit: poor under NTD 1.8 million for phase 1.

### 10. Deepfake Indicators

Do not include as a mainline phase-1 workstream.

- Technical cost: high and specialized.
- Operational cost: very high due to expert review and false positive sensitivity.
- Evidence value: future risk value, but not the fastest path to Threads scam-content triage.
- Budget fit: poor for phase 1. Mention as deferred risk only.
