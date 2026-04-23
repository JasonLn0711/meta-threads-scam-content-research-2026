# First Pilot Checkpoint Protocol

## Purpose

Use this protocol after the first 10-15 real Threads pilot items are collected or annotated.

The checkpoint exists to catch problems early while they are still cheap to fix:

- redaction failures
- raw evidence entering the wrong location
- unapproved fields creeping into the dataset
- source skew
- too many low-context items
- annotation label drift
- `uncertain` becoming a catch-all
- screenshot/OCR/link handling becoming too burdensome

This protocol does not authorize new collection methods, additional sources, automation, link crawling, profile review, or expansion beyond the approved 50-item pilot.

This checkpoint is a hard gate. Do not complete the 50-item pilot until the first 10-15 item checkpoint is reviewed and the project owner records `continue_to_50` or `continue_with_limits`.

## Preconditions

Do not start the first checkpoint until:

- controlled launch details are completed outside git
- exact source, storage, access, retention, and redaction limits are recorded in the controlled location
- local-only files under ignored `data/interim/` exist, preferably initialized with `scripts/init_pilot_workspace.py`
- item-1 preflight has passed with `scripts/check_pilot_preflight.py --before-item-1 --ack-controlled-details`
- collector and reviewer IDs are assigned
- raw evidence storage is outside git
- the collector understands screenshot, URL, handle, OCR, and reply/comment limits

The non-sensitive launch record is [37-approved-pilot-launch-plan.md](37-approved-pilot-launch-plan.md). Local workspace instructions are in [39-local-pilot-workspace.md](39-local-pilot-workspace.md). Preflight instructions are in [40-pilot-preflight-verification.md](40-pilot-preflight-verification.md). Use `templates/controlled_launch_details_template.md` only as a blank structure for the controlled, non-git copy.

## Checkpoint Timing

Run two small checkpoints before completing all 50 pilot items.

| Checkpoint | Timing | Main question |
|---|---|---|
| Collection checkpoint | after 10-15 candidate items are collected and redacted | Are evidence capture and redaction safe enough to continue? |
| Annotation checkpoint | after 10-15 items have first-pass labels | Are labels, evidence notes, and review routing stable enough to continue? |

If the same 10-15 items support both checks, the team may review them together. If collection moves faster than annotation, run the collection checkpoint first.

## Expected Early Composition

The first 10-15 items do not need to perfectly match the final 15/15/10/10 target, but they should not all come from one easy bucket.

Recommended early mix:

| Bucket | Suggested count in first 10-15 |
|---|---:|
| likely scam or high-risk scam-like | 3-5 |
| likely non-scam comparator | 3-5 |
| uncertain or ambiguous | 2-3 |
| insufficient-evidence or low-context | 1-3 |

Try to include at least some variation across:

- text-only
- text plus image or screenshot-style item
- reply/comment context
- OCR-relevant content
- visible link or redirection signal

Do not force this mix if doing so would require unapproved evidence.

Content coverage targets for the first checkpoint:

| Content form | Target in first 10-15 | Notes |
|---|---:|---|
| text-only | at least 2 | Include suspicious and benign if available. |
| text plus image | at least 2 if approved | Use redacted image references only. |
| reply/comment context | at least 1-2 if approved | Selected relevant replies only. |
| OCR-heavy or screenshot-style | at least 1 if approved | OCR must be privacy-reviewed. |
| visible link, handle, or redirect signal | at least 2 if approved | Visible signals only; no crawling or redirect expansion. |

If a coverage target cannot be met under the controlled launch limits, record that as a checkpoint finding rather than expanding the source or context.

## Collection Checkpoint

Use `templates/pilot_checkpoint_review.md`.

Review the local-only collection log and annotation sheet draft. Do not copy raw evidence into the checkpoint summary.

Required checks:

- no raw screenshots, browser exports, source case packets, credentials, or personal data in git
- every item has `collection_batch_id`
- every item has `authorization_status`
- every item has source type and collection method
- screenshot status is filled where images/screenshots are involved
- link status is filled where visible links are involved
- redaction notes exist for screenshots, URLs, handles, OCR, or stakeholder-provided context
- source references are omitted, normalized, or redacted according to the controlled launch record
- no item requires profile/account/landing-page context
- duplicates are marked rather than silently removed

Review dimensions:

- governance compliance
- redaction quality
- collection burden
- evidence sufficiency
- OCR quality
- reply/comment usefulness
- visible link/handle handling
- whether any item implicitly required unapproved context

Pause immediately if:

- any raw evidence entered git
- the collector needs unapproved fields
- screenshots or URLs cannot be redacted consistently
- the source is not the one approved in the controlled launch record
- collection drifts toward automation
- more than 30 percent of the first checkpoint items are not ready for annotation because of missing or unsafe evidence

## Annotation Checkpoint

Run after first-pass labels exist for 10-15 items.

Required checks:

- no blank primary labels
- no blank evidence sufficiency values
- no blank annotation confidence values
- `signal_tags` uses `none` when no signal applies
- high-risk `scam` items are routed to second review
- all `uncertain` items are routed to second review
- low-confidence and partial-evidence cases are routed to second review
- notes are evidence-based and avoid legal conclusions
- notes do not include raw personal data
- `uncertain` and `insufficient_evidence` are not being used interchangeably

Review dimensions:

- annotation consistency
- evidence-based notes
- second-review routing
- dangerous label drift
- whether the guideline is clear enough to continue

Warning thresholds for 10-15 items:

| Finding | Warning threshold | Action |
|---|---:|---|
| `uncertain` | above 40 percent | Review whether source is too ambiguous or guideline boundary is unclear. |
| `insufficient_evidence` | above 30 percent | Review collection quality and evidence requirements. |
| missing required annotation fields | any repeated pattern | Fix sheet/process before continuing. |
| unapproved context needed | any item | Pause and revise authorization or exclude the item. |
| repeated same disagreement | two or more items | Add guidance or examples before continuing. |
| raw identifiers in notes | any item | Redact immediately and retrain note-writing. |

## Decision Outcomes

Choose one checkpoint decision:

| Decision | Meaning |
|---|---|
| `continue_to_50` | Collection and annotation can proceed under current limits. |
| `continue_with_limits` | Continue, but with stricter source, field, redaction, or routing limits. |
| `pause_for_redaction_fix` | Stop collection until redaction/storage handling is corrected. |
| `pause_for_collection_fix` | Stop collection until source mix, evidence capture, or missing fields are corrected. |
| `pause_for_guideline_fix` | Stop annotation until label or evidence rules are clarified. |
| `pause_for_authorization_review` | Stop because the team needs unapproved evidence or collection methods. |
| `stop_pilot` | Stop the pilot because privacy, source, or operational risk is too high. |

Do not choose `continue_to_50` if the team cannot explain why each warning is acceptable.

Decision evidence:

| Practical decision | Checkpoint decision value | Evidence needed |
|---|---|---|
| continue | `continue_to_50` | Zero blocking governance/privacy findings; redaction consistent; annotation fields usable; no repeated dangerous label drift. |
| continue with limits | `continue_with_limits` | Issues are bounded by source, field, content-form, redaction, or review constraints that can be enforced immediately. |
| pause | `pause_for_redaction_fix`, `pause_for_collection_fix`, `pause_for_authorization_review`, or `stop_pilot` | Raw-data, authorization, evidence quality, burden, or unapproved-context issue blocks safe continuation. |
| revise guideline first | `pause_for_guideline_fix` | Repeated label-boundary, evidence-sufficiency, confidence, or signal-tag disagreement would make the next 35-40 items unreliable. |
| revise schema first | `pause_for_collection_fix` plus schema follow-up | Required fields are missing, confusing, too sensitive, too burdensome, or cannot represent approved evidence. |
| narrow sources | `continue_with_limits` or `pause_for_collection_fix` | Source mix causes low-context, privacy-heavy, or unreviewable items that would distort the 50-item pilot. |

## Minimum Checkpoint Output

The checkpoint summary should include:

- checkpoint ID
- date
- item count reviewed
- bucket counts
- content-form counts
- redaction findings
- missing-field findings
- label distribution if labels exist
- second-review routing count
- unresolved blockers
- decision
- owner and next review date

Use `templates/pilot_checkpoint_review.md`.

## Local Commands

When the first local annotation CSV exists:

```bash
python scripts/validate_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv --strict
python scripts/audit_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv \
  > data/processed/threads_pilot_v1_checkpoint_audit.md
```

If only the collection log exists, do a manual collection checkpoint first and wait to run schema validation until the annotation CSV has the required schema fields.

Do not commit the local CSV, JSONL, raw evidence, or generated processed outputs unless they are explicitly approved and fully non-sensitive.

## After The Checkpoint

If the decision is `continue_to_50` or `continue_with_limits`:

1. Record the decision in a non-sensitive note.
2. Continue collection up to 50 items.
3. Maintain second-review routing.
4. Keep raw evidence outside git.

If the decision is any pause or stop:

1. Stop collection.
2. Record the blocker without raw evidence.
3. Update the controlled launch record if source, storage, access, retention, or redaction limits changed.
4. Update the annotation guideline, collection SOP, or work order if needed.
5. Resume only after the project owner records a new decision.
