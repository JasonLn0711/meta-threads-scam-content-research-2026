# Problem Framing

## Working Definition

In this project, "Threads scam content" means Threads-related posts, replies, comments, image text, or redirection signals that plausibly attempt to lure users into deception, financial loss, identity compromise, unsafe off-platform contact, or other fraud-like risk.

This is a research label. It does not mean the author has committed a crime, and it does not replace legal or platform policy review.

## Included Content

Phase 1 includes:

- Text posts with scam-like claims or offers.
- Text plus image posts where the image may contain key claims.
- Replies and comments that amplify, redirect, or complete the lure.
- OCR text from images or screenshots.
- External links, handles, messaging-channel references, and other visible redirection signals.
- Screenshot-heavy posts when privacy can be minimized.

## Excluded Or Deferred Content

Phase 1 does not prioritize:

- Long video analysis.
- Heavy multimodal video pipelines.
- Deepfake detection as a mainline workstream.
- Full cross-platform Meta integration.
- Automated production enforcement.

## Why Text, Image Text, Comments, And Redirection First

These surfaces are prioritized because they are:

- High signal: scam lures often use repeated promises, urgency, testimonials, fake endorsements, or contact instructions.
- Lower cost: text and OCR are cheaper to process than video.
- Reviewable: human annotators can inspect the evidence and explain decisions.
- Experiment-friendly: they support clear ablation tests such as post-only versus post-plus-comments.
- Budget-fit: they can produce actionable learning under NTD 1.8 million.

## Likely Threads Scam Patterns

Expected phase-1 patterns include:

- Investment lures using guaranteed returns or low-risk profit language.
- Fake endorsement or celebrity-adjacent promotion.
- Redirect-to-private-channel behavior, such as messaging app handles or private groups.
- Impersonation or pseudo-official language.
- High-pressure urgency, limited-time opportunity, or fear of missing out.
- Suspicious testimonials or fabricated success stories.
- Crypto, stock, side-income, loan, medical, or job lures with weak evidence.
- Link-shortener or suspicious domain redirection.

## Operational Framing

The project should produce risk triage, not absolute truth judgment.

Useful output should say:

- Which signals were observed.
- Why the item was ranked as higher or lower risk.
- What evidence is missing.
- Whether the case needs human review.
- How confident the reviewer or baseline is.

It should not say:

- "This is definitely fraud."
- "This account should be removed."
- "This system detects all scams."
- "This model is production-ready."
