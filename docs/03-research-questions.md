# Research Questions

## Broad Research Questions

1. What types of scam-like content are most common in Threads-related reports?
2. Which observable signals are most useful for human triage?
3. How much value do comments, OCR text, and link signals add beyond post text?
4. Can simple baselines provide defensible triage support before heavier models are considered?
5. What evidence must be preserved for investigators, policy reviewers, or domain experts?
6. Where does the project need platform cooperation or stakeholder-provided samples?

## Narrowed Phase-1 Questions

1. Can a text-only baseline separate obvious high-risk items from obvious low-risk items?
2. Does OCR improve recall for image-heavy or screenshot-heavy scam lures?
3. Do replies and comments contain decisive redirection signals that the original post lacks?
4. Are link and private-channel signals useful enough to justify structured extraction?
5. Is risk triage more useful than binary scam/non-scam classification for ambiguous content?
6. Can reviewers consistently apply the initial taxonomy and uncertainty labels?

## What Must Be Answered First

- What is the minimum dataset schema needed to preserve evidence and uncertainty?
- Which labels can annotators apply consistently?
- What sample size is enough for a first baseline comparison?
- Which signals are high-value and cheap enough for phase 1?
- What content should be excluded to protect budget and focus?

## What Can Wait

- Production deployment design.
- Cross-platform Meta integration.
- Full account or network analysis.
- Long video and deepfake pipelines.
- Large-scale model training.
- Automated collection beyond approved access.
