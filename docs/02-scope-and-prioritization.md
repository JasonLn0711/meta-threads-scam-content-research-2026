# Scope And Prioritization

## Phase-1 Recommendation

Start with text, images, comments, OCR, and visible redirection signals. Defer video-heavy and deepfake-heavy work until the first dataset and baseline comparison show that these signals are insufficient.

## Scope Matrix

| Content surface | Investigative value | Technical feasibility | Annotation burden | Compute cost | False positive risk | Phase recommendation | Include now |
|---|---:|---:|---:|---:|---:|---|---|
| Text posts | High | High | Low to medium | Low | Medium | Core phase 1 | Yes |
| Text plus image posts | High | Medium | Medium | Low to medium | Medium | Core phase 1 with OCR | Yes |
| Comments / replies | High | Medium | Medium to high | Low | Medium | Core phase 1 sample | Yes |
| OCR from images | High | Medium | Medium | Low to medium | Medium | Add after text baseline | Yes |
| External links | High | Medium | Medium | Low | High | Capture visible signals, avoid unauthorized crawling | Yes |
| Screenshot-heavy posts | Medium to high | Medium | High | Low to medium | Medium | Include selectively with privacy controls | Yes, selective |
| Short video | Medium | Low to medium | High | Medium to high | High | Later study only if sample demands it | Later |
| Long video | Low to medium | Low | Very high | High | High | Defer | No |
| Deepfake-related signals | Future risk value | Low | Very high | High | Very high | Defer to future risk note | No |

## Detailed Research Judgment

### 1. Text Posts

Include now.

- Technical cost: low. Keyword, pattern, classifier, and LLM-assisted baselines can all operate on text.
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

### 7. Short Video

Defer unless stakeholders show that short videos dominate the report queue.

- Technical cost: medium to high. Requires frame sampling, transcription, and media handling.
- Operational cost: high. Annotation takes longer and evidence is harder to quote.
- Evidence value: uncertain for phase 1.
- Budget fit: weak for the first 4 weeks, possible as a later narrow study.

### 8. Long Video

Defer.

- Technical cost: high.
- Operational cost: very high.
- Evidence value: uncertain relative to cost.
- Budget fit: poor under NTD 1.8 million for phase 1.

### 9. Deepfake Indicators

Do not include as a mainline phase-1 workstream.

- Technical cost: high and specialized.
- Operational cost: very high due to expert review and false positive sensitivity.
- Evidence value: future risk value, but not the fastest path to Threads scam-content triage.
- Budget fit: poor for phase 1. Mention as deferred risk only.
