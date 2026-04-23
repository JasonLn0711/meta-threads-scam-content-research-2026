# Dataset Decisions

## Why One `thread_item`

The first dataset centers one `thread_item` because phase 1 needs a practical annotation unit. A Threads scam-like item may be a post, a reply, a text plus image post, or a post context with OCR and visible redirection. Keeping one unit avoids premature account, campaign, graph, or enforcement modeling.

This design lets the team collect and annotate immediately while preserving enough evidence for first baselines.

## Why Text, Replies, OCR, Links, And Redirection Are First-Class

Threads-first scam-content reports are likely to include lightweight evidence:

- post text that carries the lure
- replies/comments that reveal private-channel migration
- OCR text from screenshot-style images
- visible external links
- contact handles or platform redirects

These fields are cheap to collect manually, practical for annotation, and directly useful for first baselines. They also let the project compare text-only, OCR-augmented, reply-context, and link/redirection signals without building a heavy system.

## What Is Deferred

The v1 schema intentionally defers:

- long video and heavy video understanding
- deepfake detection as a core pipeline
- account graph or campaign attribution
- broad cross-platform integration
- automated Threads or Meta collection
- landing-page crawling or redirect-chain capture without approval
- VLM-heavy scoring for every item
- production dashboards, monitoring, or enforcement workflows

These may become future studies only after data access, legal review, budget, and stakeholder value are clear.

## Likely Revisions After 50 Items

Review these after the 50-item pilot:

- whether `uncertain` is too broad
- whether `insufficient_evidence` is being confused with low-confidence uncertainty
- whether scam subtypes are too overlapping
- whether `signal_tags` need merging or splitting
- whether source skew makes the pilot misleading
- whether screenshot-heavy items require a stronger OCR quality rule
- whether reply-only lures should be annotated as whole-thread risk or separated
- whether annotation time per item is realistic
- whether external link and contact-handle redaction rules are clear enough

The first revision should simplify the package if annotators struggle. Do not add fields unless they solve a repeated, concrete annotation or baseline problem.
