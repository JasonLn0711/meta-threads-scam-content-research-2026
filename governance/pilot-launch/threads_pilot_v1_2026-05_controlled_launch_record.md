# Controlled Launch Record: Threads Pilot v1

This is the non-sensitive repository copy of the controlled launch record for the CIB-authorized Threads scam-content research pilot.

Sensitive source identifiers, exact CIB contacts, raw evidence paths, credential details, API tokens, browser session material, case identifiers, handles, URLs, screenshots, and raw investigative details must remain outside git in the controlled location named below.

## Launch Identity

| Field | Value |
|---|---|
| Controlled details ID | `CTRL-THREADS-PILOT-V1-CIB-2026-04-23` |
| Dataset or batch ID | `threads_pilot_v1_2026-05` |
| Date completed | `2026-04-23` |
| Completion owner | `PROJECT-OWNER-01` |
| Governance reviewer | `GOV-REVIEWER-01` |
| Stakeholder authorization authority | CIB Criminal Investigation Bureau |
| Related non-sensitive launch packet | `governance/pilot-launch/` |
| Related decision record | `decision-log/0018-record-cib-api-and-automation-authorization.md` |
| Current launch status | `ready_for_rehearsal` |
| Next gate | local workspace initialization, item-1 preflight, then 1-2 item controlled rehearsal |

## CIB Authorization Scope

| Scope area | Decision |
|---|---|
| Research case authorization | CIB authorizes the research team to perform the research activities needed for this Threads scam-content research case under this controlled launch record. |
| API authorization | CIB explicitly authorizes API-based collection and processing for this research case, subject to approved platform access conditions, credential controls, audit logging, field limits, and storage limits. |
| Automation authorization | CIB explicitly authorizes all automation required for this research case, including collection, retrieval, parsing, OCR, normalization, deduplication, redaction support, validation, audit, baseline scoring, packet generation, and reporting automation under this record. |
| Browser or workflow automation | Authorized only for research collection and evidence-handling tasks covered by this record; credentials, browser profiles, cookies, tokens, HAR files, and session artifacts must not enter git. |
| Link and redirect automation | Authorized for research-required link parsing, redirect-chain capture, and landing-page evidence capture when needed for this case; raw outputs stay outside git and redacted derived fields are used for annotation. |
| Profile/account context automation | Authorized only when necessary for the CIB-approved research question and only for approved fields; avoid broad graph capture unless specifically needed and logged. |
| Production scoring or enforcement | Not authorized by this record. Any automated score is a research triage output only and cannot be used as a legal fraud determination or platform enforcement action. |
| Expansion beyond the first pilot | Not automatic. Larger batches require a work order or decision memo that references this controlled record and states item count, source, fields, retention, and review gates. |

## Source Or Source Category

| Field | Value |
|---|---|
| Exact approved source or source category | CIB-authorized Threads scam or scam-like content research examples, including stakeholder-provided cases, manually identified public Threads examples, API-authorized samples, and automation-collected examples needed for the approved research case. |
| Source owner or approving stakeholder | CIB Criminal Investigation Bureau; exact contacts held outside git. |
| Source type | `stakeholder_provided`, `manual_public`, `api_authorized`, `other_approved` |
| Approved source window | From controlled launch signoff on `2026-04-23` through `2026-05-31`, unless CIB issues a narrower or extended written window. |
| Approved source exclusions | Production enforcement, public accusation workflows, unlogged credential/session capture, unmanaged raw-data sharing, and any activity outside CIB-approved research purpose. |
| Approved source access path | CIB-approved manual handoff, CIB-approved API access path, and CIB-approved automation path. Exact channels, accounts, credentials, and access details are stored outside git. |
| Sensitive source identifiers present? | yes |
| Where sensitive source identifiers are stored | `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-RAW` and `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-GOVERNANCE`, outside git. |
| Source categories explicitly not approved | Non-research production enforcement, unrelated Meta surfaces, unrelated private accounts, unrelated personal-data enrichment, and publication-ready examples without later sharing approval. |

## Raw And Working Storage

| Storage item | Exact controlled value |
|---|---|
| Raw evidence storage location | `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-RAW`, outside git; exact filesystem/cloud path is held in the CIB-controlled access record. |
| Redacted working file location | local-only ignored workspace: `data/interim/` in this repo working tree. |
| Local pilot workspace path | `/home/jnclaw/every_on_git_jnclaw/phd-life-system/meta-threads-scam-content-research-2026/data/interim/` |
| Processed local output path | `/home/jnclaw/every_on_git_jnclaw/phd-life-system/meta-threads-scam-content-research-2026/data/processed/`, ignored by git. |
| Automation log location | `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-AUTOMATION-LOGS`, outside git; non-sensitive aggregate run summaries may be recorded in repo docs. |
| API credential location | `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-CREDENTIALS`, outside git. |
| Browser/session artifact location | `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-SESSION-ARTIFACTS`, outside git, if browser automation is used. |
| Backup or archival location, if any | `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-ARCHIVE`, only if CIB approves archive after pilot decision memo. |
| Encryption or access-control expectation | CIB-controlled access; raw evidence, credentials, API tokens, browser profiles, and session material are not synced to public repos or unmanaged storage. |
| Who confirms raw files stay out of git | `PROJECT-OWNER-01`, `GOV-REVIEWER-01`, and `ENG-01` |
| What must be deleted after pilot decision | Raw screenshots, raw source references, stakeholder case packets, unredacted OCR, temporary automation outputs, temporary review packets, and local item-level outputs not approved for retention. |

## Access List

| Role | Approved person or ID | Raw evidence access? | Redacted file access? | API/automation access? | Notes |
|---|---|---|---|---|---|
| Project owner | `PROJECT-OWNER-01` | yes | yes | approve/run oversight | Owns launch, pause, and continue decisions. |
| Governance reviewer | `GOV-REVIEWER-01` | yes | yes | audit oversight | Confirms privacy, redaction, retention, and sharing limits. |
| CIB stakeholder owner | `CIB-STK-01` | yes | yes | approve/audit | Exact identity outside git. |
| Collector | `COLLECTOR-01` | yes | yes | approved runs only | Manual, API, and automation collection under this record. |
| Automation operator | `AUTO-OP-01` | yes if needed | yes | yes | Runs approved API or automation jobs and records audit logs. |
| Annotator 1 | `ANN-01` | no by default | yes | no | Redacted evidence only. |
| Annotator 2 | `ANN-02` | no by default | yes | no | Redacted evidence only. |
| Reviewer | `REVIEWER-01` | yes, if needed | yes | no by default | Reviews high-risk, uncertain, low-confidence, partial-evidence cases. |
| Adjudicator | `ADJ-01` | yes, if needed | yes | no by default | Resolves disagreements without legal determinations. |
| Research engineer | `ENG-01` | no by default | yes | tooling and validation | Runs validation, audit, conversion, baseline, and reporting on redacted/local files. |

## Approved Pilot IDs

| ID type | Approved IDs |
|---|---|
| Collector IDs | `COLLECTOR-01` |
| Automation operator IDs | `AUTO-OP-01` |
| Annotator IDs | `ANN-01`, `ANN-02` |
| Reviewer IDs | `REVIEWER-01` |
| Adjudicator IDs | `ADJ-01` |
| Research engineer IDs | `ENG-01` |
| IDs not approved for this pilot | Anyone not listed above |

## API And Automation Run Rules

Every API or automation run must have a local or controlled run record with:

| Required run field | Required value |
|---|---|
| Run ID | Unique ID such as `AUTO-RUN-YYYYMMDD-###` |
| Operator ID | One approved ID from this record |
| Purpose | Research purpose tied to Threads scam-content triage |
| Source category | Approved source category from this record |
| Collection method | `api_authorized`, `browser_automation`, `link_capture`, `ocr_pipeline`, `redaction_pipeline`, `baseline_pipeline`, or other approved method |
| Item or batch limit | Stated before run starts |
| Fields collected | Stated before run starts |
| Raw output path | Controlled path outside git |
| Redacted output path | Ignored local path or controlled redacted path |
| Credential/session handling | Credentials, tokens, cookies, profiles, and HAR files outside git only |
| Redaction status | `pending`, `reviewed`, `passed`, or `blocked` |
| Stop condition review | Recorded after run |

Pause automation immediately if a run collects fields outside this record, stores raw data in git, exposes credentials/session artifacts, bypasses access controls, or shifts toward production scoring.

## Retention And Deletion Rule

| Evidence type | Retention limit | Deletion/archive owner | Review date | Notes |
|---|---|---|---|---|
| Raw screenshots | Retain only until pilot decision memo or `2026-06-30`, whichever comes first. | `GOV-REVIEWER-01` | `2026-06-30` | Delete unless CIB approves archive. |
| Raw source references | Retain only until pilot decision memo or `2026-06-30`. | `PROJECT-OWNER-01` | `2026-06-30` | Keep outside git only. |
| Stakeholder case packets | CIB-controlled retention only. | `CIB-STK-01` | `2026-06-30` | Do not copy into repo. |
| API raw responses | Retain only until pilot decision memo or `2026-06-30`. | `AUTO-OP-01` / `GOV-REVIEWER-01` | `2026-06-30` | Store outside git; redact before annotation. |
| Browser/session artifacts | Delete as soon as audit no longer requires them, no later than `2026-06-30`. | `AUTO-OP-01` | `2026-06-30` | Credentials, cookies, profiles, and HAR files never enter git. |
| Redirect-chain and landing-page captures | Retain only if needed for audit, no later than `2026-06-30` without archive approval. | `GOV-REVIEWER-01` | `2026-06-30` | Redact before annotation. |
| Redacted screenshots | Retain through checkpoint and pilot decision memo. | `GOV-REVIEWER-01` | `2026-06-30` | Internal review only. |
| Local annotation CSVs | Retain through pilot analysis and decision memo. | `ENG-01` | `2026-07-15` | Ignored by git. |
| Processed JSONL | Retain through pilot analysis and decision memo. | `ENG-01` | `2026-07-15` | Local-only unless later approved as fully non-sensitive. |
| Audit, agreement, baseline, and packet outputs | Retain through pilot analysis. | `ENG-01` | `2026-07-15` | Item-level outputs stay outside git. |
| Aggregate summaries and decision memos | May be retained if non-sensitive. | `PROJECT-OWNER-01` | after pilot memo | Git-safe only if no raw/source-sensitive details. |

## Permitted Fields

| Field or evidence type | Approved? | Exact allowed representation | Notes |
|---|---|---|---|
| `post_text` | yes | redacted visible text or risk-relevant excerpt | Remove unrelated personal data. |
| `reply_texts` | yes | selected relevant redacted replies only | Broader reply capture allowed only when the run record explains why it is needed. |
| `image_paths` | yes | redacted local reference only | No raw screenshots in git. |
| `ocr_text` | yes | risk-relevant excerpt or full OCR only if approved in the run record | Privacy review before annotation. |
| `external_links` | yes | domain-only, redacted visible-link reference, or controlled raw value outside git | Link automation allowed under run record. |
| `visible_contact_handles` | yes | category only, redacted handle, or controlled raw value outside git if needed | No raw handles in repo-visible files. |
| `visible_platform_redirects` | yes | schema categories only | Example: `line`, `telegram`, `whatsapp`, `external_site`, `phone`, `email`, `none`. |
| `source_url_if_stored` | yes with limits | omitted or redacted reference in repo-visible files; controlled raw URL outside git | Full source URLs stay outside git. |
| `metadata_notes` | yes | non-sensitive operational note only | No accusation or legal conclusion. |
| `privacy_redaction_notes` | yes | required when redaction occurs | Must explain screenshot/OCR/link/handle/reply handling. |
| API metadata | yes with limits | run-level or item-level controlled metadata outside git; redacted derived values in annotations | Do not commit API tokens, raw IDs, or sensitive response payloads. |
| Automation logs | yes with limits | non-sensitive aggregate in git; raw run logs outside git | Must include operator, purpose, source, fields, and output path. |

## Forbidden Fields And Context

| Field or context | Forbidden unless later approved? | Notes |
|---|---|---|
| Raw personal data unrelated to risk evidence | yes | Exclude or redact. |
| Raw ordinary user handles in git | yes | Use omitted/redacted/category representation. |
| Full contact handles, phone numbers, emails, payment details, referral codes in git | yes | Store only category/redacted form in repo-visible files. |
| Credentials, tokens, cookies, session files, browser profiles, HAR files in git | yes | Store only in controlled credential/session location. |
| Unmanaged bulk exports | yes | Bulk outputs require a run record and controlled storage. |
| Legal fraud determinations or accusation language | yes | Use research labels only: `scam`, `non_scam`, `uncertain`, `insufficient_evidence`. |
| Production enforcement decisions | yes | This record supports research triage only. |

## Redaction Rules

| Evidence type | Exact approved handling | Required notes |
|---|---|---|
| Ordinary user handles | Omit or replace with `[ordinary_user_handle_redacted]` in repo-visible files. | Note if removed from post/reply context. |
| Contact handles | Store category only, such as `line_contact`, `telegram_contact`, `phone_contact`, or `email_contact`; raw or redacted handle only in controlled storage if needed for audit. | Required in `privacy_redaction_notes`. |
| Personal names, faces, profile photos | Redact or exclude from repo-visible files unless directly approved by CIB and necessary for audit. | Required if any visual evidence is retained. |
| Source URLs | Omit from repo-visible files or use `source_ref_redacted_###`. | Exact URL outside git only. |
| Visible external links | Store domain-only or redacted reference in repo-visible files. | Raw/expanded values outside git only. |
| Replies/comments | Keep selected relevant redacted replies in annotations; broader captures outside git only if run record justifies them. | No raw handles in annotation notes. |
| Stakeholder case references | Replace with controlled reference ID, e.g. `CIB_CASE_REF_###`. | Exact case mapping outside git only. |
| Payment, credential, or referral details | Redact to category, e.g. `payment_detail_redacted`, `credential_request`, `referral_code_redacted`. | Required if such evidence drives label reasoning. |
| API responses | Redact IDs, handles, URLs, and unrelated personal fields before annotation. | Raw responses outside git. |
| Automation logs | Keep raw logs outside git; commit only non-sensitive run summaries if needed. | Include run ID and controlled output location. |

## Screenshot Policy

| Question | Decision |
|---|---|
| Are screenshots allowed at all? | yes, with CIB-controlled storage and redaction limits |
| Are full screenshots allowed? | yes only in controlled raw storage when needed for audit |
| Are redacted screenshots allowed? | yes |
| Is automated screenshot capture allowed? | yes, under API/automation run rules |
| Where are screenshots stored? | Raw: `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-RAW`; redacted local references may be used in ignored local workspace only. |
| Who performs redaction QA? | `GOV-REVIEWER-01` |
| Which screenshot statuses are allowed? | `not_applicable`, `not_captured`, `captured_redacted`, `captured_full_approved`, `unavailable` |
| What requires exclusion instead of screenshot retention? | Unrelated personal data, minors, private messages, credentials, payment details, private group context, or content outside the CIB-approved research purpose. |

## OCR Policy

| Question | Decision |
|---|---|
| Is OCR allowed? | yes |
| Is automated OCR allowed? | yes, under API/automation run rules |
| Source images allowed for OCR | approved local image, redacted image, CIB stakeholder-provided image, or CIB-authorized automated screenshot only |
| OCR storage limit | risk-relevant excerpt in annotation files; full OCR outside git only if needed for audit |
| OCR redaction reviewer | `GOV-REVIEWER-01` |
| Low-quality OCR handling | blank `ocr_text` plus signal tag `ocr_missing_or_low_quality` |
| What requires exclusion instead of OCR retention? | OCR containing unrelated personal details, private contact details, credentials, private messages, or information outside the approved research purpose. |

## Source URL And Link Policy

| Evidence type | Decision |
|---|---|
| Source URL storage | redacted reference in repo-visible files; exact URL outside git if retained. |
| Visible external link storage | domain-only or redacted reference in repo-visible files; raw value outside git if needed. |
| Link snapshot status allowed | `not_applicable`, `not_captured`, `captured_redacted`, `captured_full_approved`, `unavailable` |
| Redirect expansion allowed? | yes, if needed for the CIB-approved research case and logged in the automation run record |
| Landing-page capture allowed? | yes, if needed for the CIB-approved research case and stored outside git with redacted derived fields only |
| What requires pausing? | Automation captures credentials/session artifacts into repo paths, collects unrelated personal data at scale, exceeds the run record, or produces outputs that cannot be redacted. |

## Handle And Contact Info Policy

| Evidence type | Decision |
|---|---|
| Ordinary user handles | omit or redact in repo-visible files; raw values outside git only if needed for audit |
| Contact handles | category only or redacted handle in annotation files; raw controlled value outside git only if needed |
| Phone, email, payment, referral details | omit or redact to category in repo-visible files |
| Platform redirect categories allowed | `line`, `whatsapp`, `telegram`, `messenger`, `instagram_dm`, `threads_dm`, `external_site`, `private_group`, `phone`, `email`, `other`, `none` |
| Automated extraction allowed? | yes, under API/automation run rules |
| What requires pausing? | Raw handles/contact details appear in git, annotation notes depend on unredacted identity, or automation collects unrelated identity fields beyond the run record. |

## Reply And Comment Policy

| Question | Decision |
|---|---|
| Are replies/comments allowed? | yes |
| Automated reply/comment collection allowed? | yes, under API/automation run rules |
| Broad thread capture allowed? | yes only when justified in the run record for the CIB-approved research question; otherwise selected relevant replies/comments are preferred. |
| Reply author handles retained? | redacted or controlled outside git |
| Reply text retained? | risk-relevant redacted excerpt in annotation files; raw controlled copy outside git only if needed |
| What requires pausing? | Automation captures unrelated private discussion, identity context, or broad comment history beyond the stated run record. |

## Rehearsal, Calibration, And Checkpoint Gates

| Gate | Required before collection continues? | Owner | Status |
|---|---|---|---|
| 1-2 item controlled manual/API/automation rehearsal | yes | `COLLECTOR-01` / `AUTO-OP-01` / `GOV-REVIEWER-01` | `not_started` |
| 5-item annotator calibration | yes before annotation expansion | `ANN-01`, `ANN-02`, `REVIEWER-01` | `not_started` |
| First 10-15 item checkpoint | yes before 50 items | `PROJECT-OWNER-01` | `not_started` |
| 50-item pilot decision memo | yes before expansion | `PROJECT-OWNER-01` / `ENG-01` | `not_started` |
| Automation scale-up review | yes before any larger automated batch | `PROJECT-OWNER-01` / `GOV-REVIEWER-01` / `AUTO-OP-01` | `not_started` |

## Unresolved Uncertainties

| Uncertainty | Owner | Blocking? | Resolution required before |
|---|---|---|---|
| Whether first 10-15 item mix will contain enough non-scam comparators | `PROJECT-OWNER-01` | no | 10-15 checkpoint |
| Whether OCR and screenshot automation burden is acceptable | `GOV-REVIEWER-01` | no | 10-15 checkpoint |
| Whether API or browser automation produces source skew | `AUTO-OP-01` | no | 10-15 checkpoint |
| Whether annotators distinguish `uncertain` from `insufficient_evidence` consistently | `REVIEWER-01` | no | annotation checkpoint |
| Whether larger API/automation batches should proceed | `PROJECT-OWNER-01` | yes for expansion only | 50-item decision memo |

## Pre-Collection Signoff

| Check | Status | Owner | Notes |
|---|---|---|---|
| Exact source or source category approved | complete | `CIB-STK-01` | CIB-authorized stakeholder-provided, manual public, API-authorized, and automation-collected Threads scam-like content research examples. |
| API authorization approved | complete | `CIB-STK-01` | CIB explicitly requested API authorization in this record. |
| Automation authorization approved | complete | `CIB-STK-01` | CIB explicitly requested authorization for all automation needed for this research case. |
| Exact raw storage approved | complete | `PROJECT-OWNER-01` | `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-RAW`, exact path outside git. |
| Exact API credential storage approved | complete | `GOV-REVIEWER-01` | `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-CREDENTIALS`, outside git. |
| Exact automation log storage approved | complete | `GOV-REVIEWER-01` | `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-AUTOMATION-LOGS`, outside git. |
| Exact access list approved | complete | `GOV-REVIEWER-01` | IDs listed above. |
| Exact retention/deletion rule approved | complete | `GOV-REVIEWER-01` | Review no later than `2026-06-30` for raw evidence and automation artifacts. |
| Exact redaction rules approved | complete | `GOV-REVIEWER-01` | Redaction rules listed above. |
| Screenshot policy approved | complete | `GOV-REVIEWER-01` | Raw outside git, redacted derived fields for annotation. |
| OCR policy approved | complete | `GOV-REVIEWER-01` | Automated OCR allowed; annotation files use redacted/risk-relevant text. |
| Source URL/link policy approved | complete | `GOV-REVIEWER-01` | Redirect and landing-page automation allowed under run records; raw outputs outside git. |
| Handle/contact info policy approved | complete | `GOV-REVIEWER-01` | Category/redacted in repo-visible files. |
| Reply/comment policy approved | complete | `GOV-REVIEWER-01` | Automated collection allowed under run records. |
| Approved IDs assigned | complete | `PROJECT-OWNER-01` | Pseudonymous role IDs listed above. |
| Permitted and forbidden fields reviewed | complete | `PROJECT-OWNER-01` | Research triage only; no legal determination. |
| No raw evidence will enter git | complete | `ENG-01` | `data/interim/` and `data/processed/` remain ignored/local-only. |
| First 10-15 item checkpoint scheduled | required next | `PROJECT-OWNER-01` | Schedule after controlled rehearsal passes. |

## Final Controlled Detail Decision

- Decision: `ready_for_rehearsal`
- Decision owner: `PROJECT-OWNER-01`
- Governance reviewer: `GOV-REVIEWER-01`
- Stakeholder authorization authority: CIB Criminal Investigation Bureau
- Decision date: `2026-04-23`
- Conditions:
  - Run local workspace initialization before item 1.
  - Run item-1 preflight and require `ERROR: 0`.
  - Complete 1-2 item controlled rehearsal before the first real batch; rehearsal may use manual, API, or automation flow.
  - Proceed only to the first 10-15 item checkpoint before completing 50 items.
  - API access and all research-required automation are authorized by CIB under this record, but every run must have a run record, field limits, controlled output path, redaction status, and stop-condition review.
  - Keep raw evidence, credentials, tokens, browser/session artifacts, exact sensitive source/storage/access details, and item-level sensitive outputs outside git.
  - Automated outputs are research triage artifacts only, not production enforcement, public accusation, or legal fraud determinations.
- Location of filled controlled record:
  - `CIB-CONTROLLED-STORE-THREADS-PILOT-V1-GOVERNANCE/CTRL-THREADS-PILOT-V1-CIB-2026-04-23.md`
