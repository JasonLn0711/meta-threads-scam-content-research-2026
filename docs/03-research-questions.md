# Research Questions

## Broad Research Questions

1. What bounded method can discover enough review-worthy Threads investment-scam candidates while remaining reviewable, governed, and labor-efficient?
2. Which investment-scam signal families produce the highest review-worthy yield?
3. How much value do comments, OCR text, profile-context signals, and link/contact cues add beyond post text?
4. What hard-negative controls protect ordinary investment discussion, financial education, and anti-scam warnings?
5. Can simple baselines provide defensible triage support before heavier models are considered?
6. What evidence must be preserved for investigators, policy reviewers, or domain experts?
7. Which AI/system-assisted steps can safely reduce reading, summarization, signal extraction, schema filling, triage, hard-negative review, and reporting burden without making final scam determinations?
8. Where does the project need platform cooperation or stakeholder-provided samples?

## Narrowed Phase-1 Questions

1. Which bounded source path produces the best investment-scam candidate quality: confirmed pointers, reviewer-supplied candidates, approved browser-session candidates, diversified seed matrices, or existing checkpoint materials?
2. Can a text-only baseline separate obvious high-risk investment-scam items from obvious low-risk items?
3. Does OCR improve recall for image-heavy or screenshot-heavy investment-scam lures?
4. Do replies and comments contain decisive redirection or private-channel migration signals that the original post lacks?
5. Are link/contact and private-channel signals useful enough to justify structured extraction?
6. Is risk triage more useful than binary scam/non-scam classification for ambiguous content?
7. Can reviewers consistently apply the initial taxonomy and uncertainty labels?
8. What discovery-yield and reviewer-burden metrics determine whether the method is worth scaling?
9. Can schema prefill, summary-assisted review, and priority ranking improve high-risk yield per reviewer hour without increasing hard-negative false-positive pressure?

## What Must Be Answered First

- What is the minimum dataset schema needed to preserve evidence and uncertainty?
- Which labels can annotators apply consistently?
- What sample size is enough for a first baseline comparison?
- Which signals are high-value and cheap enough for phase 1?
- What content should be excluded to protect budget and focus?
- What candidate-discovery method should be tested first, and under what cap?
- What are the average, median, and p95 review times per candidate?
- How many candidates can reviewers process per hour?
- What percentage of fields can be auto-filled, and what percentage need manual correction?
- How often do reviewers still need to read the full original thread?
- What are the second-review rate, reviewer disagreement rate, hard-negative false-positive pressure, insufficient-evidence rate, review-worthy yield per source arm, and high-risk yield per reviewer hour?

## What Can Wait

- Production deployment design.
- Cross-platform Meta integration.
- Full account or network analysis.
- Long video and deepfake pipelines.
- Large-scale model training.
- Automated collection beyond approved access.
- Expansion to other scam families before the investment-scam method is useful.
- AI/system outputs that make final labels, legal fraud determinations, enforcement recommendations, public warnings, automated takedowns, or production detector claims.
