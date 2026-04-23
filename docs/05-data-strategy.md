# Data Strategy

## Principle

Collect the minimum evidence needed to answer phase-1 research questions while preserving auditability, privacy, and uncertainty.

Operational collection and redaction steps are defined in `docs/23-collection-and-redaction-sop.md`.

## Candidate Data Sources

| Source | Use | Caution |
|---|---|---|
| Manually collected public examples | Early taxonomy testing and baseline development | Avoid unnecessary personal data; document collection method. |
| Stakeholder-provided examples | Operational relevance and report-aligned sampling | Confirm legal sharing, redaction, and retention rules. |
| Researcher-created negative examples | Calibration for non-scam and benign marketing | Do not overrepresent artificial negatives. |
| Public benign Threads content | Non-scam comparison set | Avoid broad automated collection without approval. |
| Historical report summaries | Pattern discovery if available | May be sensitive or incomplete. |

## Manual Public Example Workflow

1. Confirm the source and collection method are permitted.
2. Record only the fields needed for `data-contracts/thread_item_schema_v1.json`.
3. Avoid unnecessary account identifiers.
4. Redact personal information where possible.
5. Capture `screenshot_snapshot_status` and `link_snapshot_status`.
6. Store raw screenshots outside git unless explicitly approved and redacted.
7. Record collection decisions in `templates/collection_log_template.csv`.

## Stakeholder-Provided Examples

Before using stakeholder samples, confirm:

- Who is authorized to share them.
- Whether they contain personal or investigative data.
- What redaction is required.
- Whether examples can be retained.
- Whether they can be used in publications or only internal analysis.
- Whether any legal or platform restrictions apply.

## Internal Annotation Workflow

1. Assign each item an `item_id`.
2. Capture text, reply text, image references, OCR text, and visible links.
3. Annotator labels scam status and scam type.
4. Annotator records `signal_tags` and explanation.
5. A second reviewer checks uncertain and high-risk cases.
6. Disagreements are logged and used to revise the guideline.

## Evidence Fields To Preserve

- Source type
- Post text
- Reply text
- Image paths or redacted references
- OCR text
- External links or normalized link evidence
- Signal tags
- Scam label
- Scam type
- Annotation confidence
- Annotation notes
- Review status
- Screenshot and link snapshot status
- Collection timestamp

## Privacy And Ethical Cautions

- Do not collect more than needed.
- Do not store credentials, cookies, or browser profiles.
- Do not expose ordinary users in research artifacts.
- Avoid public accusations.
- Distinguish suspicious content from confirmed illegal scam.
- Treat false positives as serious harms.

## Legal And Platform Cautions

No automated Threads or Meta collection is approved at repo initialization. Any crawler, scraper, browser automation, or bulk download must be authorized and recorded in `governance/data-governance.md`.

## Sampling Plan

Start with a 50-item pilot, then expand to 100-200 items after guideline and schema review. If annotation capacity is limited, prefer 100-150 high-quality items over a larger weakly reviewed batch.

Pilot:

| Bucket | Target count | Purpose |
|---|---:|---|
| Likely scam or high-risk scam-like | 15 | Learn positive signals. |
| Likely non-scam | 15 | Calibrate false positives. |
| Uncertain | 10 | Stress-test ambiguity handling. |
| Insufficient evidence | 10 | Test evidence status rules. |

First usable batch:

| Bucket | Target count | Purpose |
|---|---:|---|
| Likely scam-like | 40 to 60 | Learn high-risk signals. |
| Likely non-scam | 40 to 60 | Calibrate false positives. |
| Uncertain | 20 to 40 | Stress-test ambiguity handling. |
| Insufficient evidence | 10 to 20 | Test evidence status rules. |

Include a mixture of:

- Text-only posts
- Text plus image posts
- Posts with replies/comments
- OCR-heavy images
- Visible redirection or links

## Balancing Strategy

Do not use natural prevalence estimates in the first sample. Phase 1 needs signal discovery and guideline testing, so a balanced diagnostic sample is more useful than a prevalence sample.

After the guideline stabilizes, create a second sample that better reflects incoming report distribution.

## Deduplication Strategy

Deduplicate by:

- Exact repeated text
- Near-duplicate post text
- Reused OCR claims
- Repeated links or handles
- Identical screenshot assets

Keep duplicate clusters if repetition itself is a relevant campaign signal, but mark the cluster relationship.

## Weak Labeling Ideas

Weak labels can help triage review, but should not replace annotation. Candidate weak signals:

- Guaranteed profit terms
- Private-channel redirection
- Suspicious link patterns
- Fake endorsement language
- Urgency terms
- OCR-detected contact handles

All weak labels must be stored as `signal_tags` or notes, not final truth.

## Dataset Versioning

Use versions such as:

- `threads_sample_v0_2026-04`: exploratory notes, not analysis-ready.
- `threads_sample_v1_2026-05`: first annotated phase-1 sample.
- `threads_sample_v1_1_2026-05`: corrected labels or schema-compatible updates.

Each dataset version should include a manifest, schema version, annotation guideline version, and known limitations.
