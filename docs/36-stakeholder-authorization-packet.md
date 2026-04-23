# Stakeholder Authorization Packet

## Purpose

Use this packet to request and record approval for the first real Threads pilot source.

This packet is the source-authorization reference for the research project. The repo has the schema, annotation workflow, synthetic dry run, QA gates, readiness review, and a bounded `go_with_limits` launch packet. The remaining blocker before item 1 is not broad approval language; it is the exact controlled launch record outside git.

This packet helps the project owner run a concrete approval meeting and leave with one of four decisions:

- `approved`
- `approved_with_limits`
- `revise_request`
- `rejected_or_paused`

For a new source, default status remains `not_approved`. For the current approved pilot, use this packet as the source/field/storage checklist and then complete `templates/controlled_launch_details_template.md` in the approved controlled location before item 1.

## Non-Negotiable Boundaries

This packet does not authorize:

- automated Threads or Meta collection
- scraping, crawling, browser automation, or bulk export
- landing-page crawling or redirect-chain capture
- profile/account review beyond approved item-level evidence
- storage of raw screenshots in git
- storage of credentials, cookies, browser profiles, or sensitive investigative material
- public accusation, enforcement action, or legal fraud determination

"Approved without limitations" is not a valid outcome. Every approval must define source, collection method, field set, storage, access, retention, redaction, and sharing limits.

## Packet Contents

Prepare these artifacts before the approval meeting. Use completed copies; do not paste raw evidence into the packet.

| Artifact | Required? | Purpose |
|---|---:|---|
| `reports/threads-scam-content-research-v0-executive-brief.md` | yes | Gives stakeholders the short research rationale. |
| `reports/threads-scam-content-research-v0.md` | yes | Gives the full report context and limits. |
| `docs/25-stakeholder-pilot-kickoff.md` | yes | Summarizes the pilot request. |
| `templates/stakeholder_pilot_request_email.md` | optional | Email wrapper for requesting the meeting or written decision. |
| `templates/source_candidate_intake.md` | yes | Describes the proposed source and source risk. |
| `templates/source_sampling_frame_template.csv` | yes | Shows how the 50-item diagnostic sample will be composed. |
| `templates/data_authorization_request.md` | yes | Records approved fields, storage, retention, and access. |
| `templates/stakeholder_authorization_decision_record.md` | yes | Records the meeting outcome and decision owner. |
| `docs/26-pilot-go-no-go-checklist.md` | after approval | Confirms operational gates after source approval. |
| `templates/pilot_batch_work_order.md` | after approval | Defines the exact pilot batch, roles, and stop conditions. |
| `templates/real_pilot_readiness_review.md` | final gate | Final launch review before real collection starts. |
| `templates/controlled_launch_details_template.md` | before item 1 | Exact controlled source, storage, access, retention, redaction, screenshot, OCR, URL/link, handle/contact, role-ID, permitted-field, forbidden-field, uncertainty, and signoff details. Filled sensitive copy stays outside git. |
| `templates/manual_collection_rehearsal_checklist.md` | before real volume | Rehearsal checklist for 1-2 manually prepared records. |
| `templates/annotator_calibration_packet_template.md` | before real annotation volume | Calibration packet for five items. |
| `templates/pilot_checkpoint_review.md` | after first 10-15 items | Checkpoint worksheet before completing 50 items. |

## Approval Meeting Agenda

Recommended length: 45-60 minutes.

| Segment | Time | Outcome |
|---|---:|---|
| Research scope recap | 5 min | Stakeholders confirm this is research, not enforcement or production detection. |
| Source proposal | 10 min | Candidate source and collection method are understood. |
| Field and evidence review | 10 min | Approved, denied, and pending fields are recorded. |
| Privacy and storage review | 10 min | Raw storage, access, retention, and redaction rules are recorded. |
| Sampling and annotation review | 10 min | 50-item diagnostic composition and second-review rules are accepted or revised. |
| Controlled launch and checkpoint review | 10 min | Outside-git controlled launch details and the first 10-15 item gate are understood. |
| Decision and owner assignment | 5-15 min | Decision, limits, blockers, and next owners are recorded. |

## Decision Questions

The meeting must answer these questions explicitly.

### Source And Method

| Question | Required answer |
|---|---|
| Which source type is approved? | stakeholder-provided cases / manual public examples / API-authorized examples / other approved source |
| Is collection manual only? | yes / no / limited |
| Is any automation approved? | no by default; yes only with written scope |
| What is the approved sample size? | number and batch ID |
| What date range or source window is allowed? | explicit range or not applicable |

### Field Approval

| Field | Decision needed |
|---|---|
| `post_text` | approved / approved_with_redaction / denied / pending |
| `reply_texts` | approved / approved_with_redaction / denied / pending |
| `ocr_text` | approved / approved_with_redaction / denied / pending |
| `image_paths` or screenshot references | approved / approved_redacted_only / denied / pending |
| `external_links` | full URL approved / normalized domain only / redacted reference only / denied |
| `visible_contact_handles` | full handle approved / redacted handle only / category only / denied |
| `visible_platform_redirects` | approved / approved_with_redaction / denied / pending |
| `source_url_if_stored` | full URL approved / redacted reference only / not stored |
| `metadata_notes` | approved / limited / denied |

### Evidence Handling

| Question | Required answer |
|---|---|
| Where is raw evidence stored outside git? | named location category or controlled system |
| Who may access raw evidence? | named people or roles |
| Who may access redacted annotation files? | named people or roles |
| How long is raw evidence retained? | period and deletion owner |
| How long are redacted derived files retained? | period and deletion owner |
| Are screenshots allowed? | no / redacted only / full approved |
| Are source URLs allowed? | no / redacted only / full approved |
| Is OCR allowed? | no / redacted only / approved |
| Are aggregate metrics shareable? | internal only / external allowed / not allowed |
| Are redacted examples shareable? | internal only / external allowed / not allowed |

### Controlled Launch Details

| Question | Required answer |
|---|---|
| Where will the filled controlled launch record live outside git? | exact controlled location |
| Who owns final signoff before item 1? | named person or role |
| Which collector IDs are approved? | IDs |
| Which annotator IDs are approved? | IDs |
| Which reviewer/adjudicator IDs are approved? | IDs |
| Which fields are explicitly forbidden? | field/context list |
| Which uncertainties block item 1? | blocker list |
| What decision allows the first 10-15 items? | `ready_for_first_10_15_items` or equivalent |
| What decision allows continuation to 50? | `continue_to_50` or `continue_with_limits` after checkpoint |

## Decision Outcomes

| Outcome | Meaning | Next action |
|---|---|---|
| `approved` | Source, method, field set, storage, access, retention, redaction, and sharing are clear. | Record decision, run go/no-go, then readiness review. |
| `approved_with_limits` | Approval exists but is constrained. | Record every limit; convert unresolved issues into explicit pilot limits. |
| `revise_request` | Stakeholders need changes before approval. | Revise packet and request another review. |
| `rejected_or_paused` | Source or method is not approved. | Do not collect. Use only synthetic/redacted work. |

## Minimum Approval Required To Start Real Pilot Work

The first real pilot workflow can start only if all of these are true:

- `templates/stakeholder_authorization_decision_record.md` is completed.
- `templates/data_authorization_request.md` is completed.
- `governance/pilot-authorization-register.md` is updated.
- `governance/source-intake-register.md` is updated.
- `docs/26-pilot-go-no-go-checklist.md` is completed with `go` or `go_with_limits`.
- `templates/pilot_batch_work_order.md` is completed.
- `templates/real_pilot_readiness_review.md` is completed with `go` or `go_with_limits`.
- controlled launch details are completed outside git.
- local workspace initialization and item-1 preflight are ready.
- 1-2 item rehearsal and 5-item calibration are planned.
- first 10-15 item checkpoint is scheduled before completing 50.
- raw evidence storage is outside git.
- redaction, access, retention, and sharing limits are written down.

If any item is missing, the project remains synthetic-only.

Do not complete all 50 items until the first 10-15 item checkpoint records `continue_to_50` or `continue_with_limits`.

## How To Record The Decision

After the meeting:

1. Complete `templates/stakeholder_authorization_decision_record.md`.
2. Complete or update `templates/data_authorization_request.md`.
3. Add the source decision to `governance/source-intake-register.md`.
4. Add the authorization decision to `governance/pilot-authorization-register.md`.
5. Update `docs/16-open-questions-for-stakeholders.md` by removing answered questions and adding unresolved blockers.
6. Add a meeting note under `notes/` with no raw evidence or sensitive details.
7. If approved, continue with `docs/26-pilot-go-no-go-checklist.md`.
8. Before item 1, complete the controlled launch record outside git.

## Owner Checklist

Before sending the packet:

- [ ] The report and executive brief are current.
- [ ] Source candidate intake is filled without sensitive raw evidence.
- [ ] Sampling frame shows the 15/15/10/10 pilot composition.
- [ ] Authorization request lists each field separately.
- [ ] Storage outside git is identified.
- [ ] Access, retention, and redaction questions are ready.
- [ ] Meeting owner can explain why 50 items is a pilot, not a prevalence claim.
- [ ] Meeting owner can explain why the first 10-15 items are a checkpoint before completing 50.
- [ ] Meeting owner can explain why 500 items is a later governed expansion.
- [ ] Decision-record template is ready to fill immediately.

After the meeting:

- [ ] Decision record completed.
- [ ] Registers updated.
- [ ] Go/no-go checklist updated.
- [ ] Pilot batch work order updated if approved.
- [ ] Real-pilot readiness review updated if approved.
- [ ] Controlled launch record completed outside git before item 1.
- [ ] First 10-15 item checkpoint owner assigned.
- [ ] Meeting note added without raw evidence.

## Practical Recommendation

For the first real source, prefer the lowest-risk approval that can still test the workflow:

- one source category
- 50 items maximum
- manual or stakeholder-provided examples only
- redacted screenshots only, or no screenshots if storage remains unclear
- normalized/redacted links unless full URLs are explicitly approved
- redacted contact handles unless full handles are explicitly approved
- internal aggregate reporting only

That level of approval is enough to learn whether annotation, evidence fields, OCR, replies, and link/redirection signals are useful without prematurely turning the project into a data-collection operation.
