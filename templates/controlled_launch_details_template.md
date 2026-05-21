# Controlled Launch Details Template

This is the canonical structure for the exact controlled details required before real Threads pilot work begins.

Important: the filled version may contain sensitive source, storage, access, or investigative details. Keep the filled record in the approved controlled location outside git unless it is fully non-sensitive and explicitly approved for commit. The repo may reference that this record exists, but it must not store sensitive controlled details if disallowed.

Collection remains paused if any required section below is incomplete, unresolved, or contradicted by the non-sensitive launch packet.

## Launch Identity

| Field | Value |
|---|---|
| Controlled details ID |  |
| Dataset or batch ID | `threads_pilot_v1_2026-05` |
| Date completed |  |
| Completion owner |  |
| Governance reviewer |  |
| Related non-sensitive launch packet | `governance/pilot-launch/` |
| Current launch status | `not_ready` / `ready_for_rehearsal` / `ready_for_first_10_15_items` / `paused` |

## Source Or Source Category

| Field | Value |
|---|---|
| Exact approved source or source category |  |
| Source owner or approving stakeholder |  |
| Source type | stakeholder_provided / manual_public / other_approved |
| Approved source window |  |
| Approved source exclusions |  |
| Approved source access path |  |
| Sensitive source identifiers present? | yes / no |
| Where sensitive source identifiers are stored |  |
| Source categories explicitly not approved |  |

## Raw And Working Storage

| Storage item | Exact controlled value |
|---|---|
| Raw evidence storage location |  |
| Redacted working file location |  |
| Local pilot workspace path |  |
| Backup or archival location, if any |  |
| Encryption or access-control expectation |  |
| Who confirms raw files stay out of git |  |
| What must be deleted after pilot decision |  |

## Access List

| Role | Approved person or ID | Raw evidence access? | Redacted file access? | Notes |
|---|---|---|---|---|
| Project owner |  | yes / no | yes / no |  |
| Governance reviewer |  | yes / no | yes / no |  |
| Collector |  | yes / no | yes / no |  |
| Annotator 1 |  | yes / no | yes / no |  |
| Annotator 2 |  | yes / no | yes / no |  |
| Reviewer |  | yes / no | yes / no |  |
| Adjudicator |  | yes / no | yes / no |  |
| Research engineer |  | yes / no | yes / no |  |

## Approved Pilot IDs

| ID type | Approved IDs |
|---|---|
| Collector IDs |  |
| Annotator IDs |  |
| Reviewer IDs |  |
| Adjudicator IDs |  |
| Research engineer IDs |  |
| IDs not approved for this pilot |  |

## Retention And Deletion Rule

| Evidence type | Retention limit | Deletion/archive owner | Review date | Notes |
|---|---|---|---|---|
| Raw screenshots |  |  |  |  |
| Raw source references |  |  |  |  |
| Stakeholder case packets |  |  |  |  |
| Redacted screenshots |  |  |  |  |
| Local annotation CSVs |  |  |  |  |
| Processed JSONL |  |  |  |  |
| Audit, agreement, baseline, and packet outputs |  |  |  |  |
| Aggregate summaries and decision memos |  |  |  |  |

## Permitted Fields

List only fields approved for this pilot. Use the least sensitive approved representation.

| Field or evidence type | Approved? | Exact allowed representation | Notes |
|---|---|---|---|
| `post_text` | yes / no | full visible / redacted excerpt / blank |  |
| `reply_texts` | yes / no | selected relevant redacted replies / blank |  |
| `image_paths` | yes / no | redacted local reference only / blank |  |
| `ocr_text` | yes / no | risk-relevant excerpt / blank |  |
| `external_links` | yes / no | domain-only / redacted / blank |  |
| `visible_contact_handles` | yes / no | category only / redacted handle / blank |  |
| `visible_platform_redirects` | yes / no | schema categories only |  |
| `poster_threads_id_ref` | yes / no | controlled-store reference / salted hash / redacted handle / blank | Top-level poster only; not ordinary commenters. |
| `poster_profile_context_status` | yes / no | schema status only | Use `captured_redacted` for repo-safe records when raw ID/profile stays controlled. |
| `poster_profile_signals` | yes / no | schema categories only | Context for dedupe/repeat-source review, not a standalone label. |
| `poster_profile_notes` | yes / no | redacted context note only | No raw profile URL, profile photo, follower/following list, or unrelated personal data in git. |
| account cadence metadata | yes / no | aggregate counts/time buckets only | No continuous monitoring; no raw profile history in git. |
| `source_url_if_stored` | yes / no | omitted / redacted reference / normalized URL |  |
| `metadata_notes` | yes / no | non-sensitive operational note only |  |
| `privacy_redaction_notes` | yes / no | required when redaction occurs |  |

## Forbidden Fields And Context

| Field or context | Forbidden unless later approved? | Notes |
|---|---|---|
| Raw personal data unrelated to risk evidence | yes |  |
| Raw ordinary user handles | yes |  |
| Full contact handles, phone numbers, emails, payment details, or referral codes | yes |  |
| Profile history, follower/following lists, or broad account metadata | yes | Narrow top-level poster ID/profile-context capture is allowed only when a run record explicitly approves it. |
| Landing-page content or redirect-chain evidence | yes |  |
| Browser exports, cookies, tokens, credentials, profiles, or HAR files | yes |  |
| Bulk exports or automated collection outputs | yes |  |
| Legal fraud determinations or accusation language | yes |  |

## Redaction Rules

| Evidence type | Exact approved handling | Required notes |
|---|---|---|
| Ordinary user handles |  |  |
| Top-level poster Threads ID | controlled-store raw; repo-safe salted hash, redacted handle, or controlled reference only |  |
| Poster profile context | narrow risk-relevant categories only |  |
| Contact handles |  |  |
| Personal names, faces, profile photos |  |  |
| Source URLs |  |  |
| Visible external links |  |  |
| Replies/comments |  |  |
| Stakeholder case references |  |  |
| Payment, credential, or referral details |  |  |

## Screenshot Policy

| Question | Decision |
|---|---|
| Are screenshots allowed at all? | yes / no |
| Are full screenshots allowed? | yes / no |
| Are redacted screenshots allowed? | yes / no |
| Where are screenshots stored? |  |
| Who performs redaction QA? |  |
| Which screenshot statuses are allowed? | `not_applicable` / `not_captured` / `captured_redacted` / `captured_full_approved` / `unavailable` |
| What requires exclusion instead of screenshot retention? |  |

## OCR Policy

| Question | Decision |
|---|---|
| Is OCR allowed? | yes / no |
| Source images allowed for OCR | approved local redacted image / stakeholder-provided image / other |
| OCR storage limit | risk-relevant excerpt only / full OCR approved / not allowed |
| OCR redaction reviewer |  |
| Low-quality OCR handling | blank `ocr_text` plus `ocr_missing_or_low_quality` / other |
| What requires exclusion instead of OCR retention? |  |

## Source URL And Link Policy

| Evidence type | Decision |
|---|---|
| Source URL storage | omitted / redacted reference / normalized URL / full approved |
| Visible external link storage | domain-only / redacted / full approved / not allowed |
| Link snapshot status allowed | `not_applicable` / `not_captured` / `captured_redacted` / `captured_full_approved` / `unavailable` |
| Redirect expansion allowed? | no unless later approved |
| Landing-page capture allowed? | no unless later approved |
| What requires pausing? |  |

## Handle And Contact Info Policy

| Evidence type | Decision |
|---|---|
| Ordinary user handles | omit / redact / approved exception |
| Contact handles | category only / redacted handle / full approved / not allowed |
| Phone, email, payment, referral details | omit / redact / approved exception |
| Platform redirect categories allowed | line / whatsapp / telegram / messenger / instagram_dm / threads_dm / external_site / private_group / phone / email / other / none |
| What requires pausing? |  |

## Rehearsal, Calibration, And Checkpoint Gates

| Gate | Required before collection continues? | Owner | Status |
|---|---|---|---|
| 1-2 item manual collection rehearsal | yes |  | not_started / passed / blocked |
| 5-item annotator calibration | yes |  | not_started / passed / blocked |
| First 10-15 item checkpoint | yes before 50 items |  | not_started / passed / blocked |
| 50-item pilot decision memo | yes before expansion |  | not_started / passed / blocked |

## Unresolved Uncertainties

| Uncertainty | Owner | Blocking? | Resolution required before |
|---|---|---|---|
|  |  | yes / no | item 1 / 10-15 checkpoint / 50-item pilot / expansion |

## Pre-Collection Signoff

| Check | Status | Owner | Notes |
|---|---|---|---|
| Exact source or source category approved |  |  |  |
| Exact raw storage approved |  |  |  |
| Exact access list approved |  |  |  |
| Exact retention/deletion rule approved |  |  |  |
| Exact redaction rules approved |  |  |  |
| Screenshot policy approved |  |  |  |
| OCR policy approved |  |  |  |
| Source URL/link policy approved |  |  |  |
| Handle/contact info policy approved |  |  |  |
| Approved IDs assigned |  |  |  |
| Permitted and forbidden fields reviewed |  |  |  |
| No raw evidence will enter git |  |  |  |
| First 10-15 item checkpoint scheduled |  |  |  |

## Final Controlled Detail Decision

- Decision: `ready_for_rehearsal` / `ready_for_first_10_15_items` / `needs_revision` / `paused`
- Decision owner:
- Governance reviewer:
- Decision date:
- Conditions:
- Location of filled controlled record:

If the decision is not `ready_for_rehearsal` or `ready_for_first_10_15_items`, do not initialize real pilot work or collect real items.
