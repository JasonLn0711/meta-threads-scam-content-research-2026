# Pilot Launch Records

This folder contains non-sensitive launch records for the first approved Threads 50-item pilot.

Do not place raw Threads content, screenshots, URLs, handles, stakeholder case IDs, credentials, browser exports, or investigative material here.

## Current Launch Packet

| File | Purpose |
|---|---|
| `threads_pilot_v1_2026-05_source_intake.md` | Non-sensitive approved source-category intake. |
| `threads_pilot_v1_2026-05_sampling_frame.csv` | Diagnostic 50-item pilot sampling frame. |
| `threads_pilot_v1_2026-05_authorization_decision.md` | Stakeholder authorization decision record. |
| `threads_pilot_v1_2026-05_data_authorization.md` | Field, storage, retention, and sharing authorization summary. |
| `threads_pilot_v1_2026-05_controlled_launch_record.md` | Non-sensitive controlled launch record, including CIB API and automation authorization. |
| `threads_pilot_v1_2026-05_go_no_go.md` | Go/no-go decision record. |
| `threads_pilot_v1_2026-05_controlled_rehearsal_work_order.md` | Execution sheet for the first 1-2 controlled real rehearsal items. |
| `threads_pilot_v1_2026-05_controlled_crawler_run_record_0001.md` | Non-sensitive tracked run record for the first controlled low-speed crawler rehearsal. |
| `threads_pilot_v1_2026-05_controlled_crawler_run_record_0002.md` | Non-sensitive tracked run record for the next one-item browser-rendered or API/session-aware rehearsal. |
| `threads_pilot_v1_2026-05_checkpoint_browser_run_record_0003.md` | Non-sensitive tracked run record for collecting local records 0002-0010 for the first 10-item checkpoint. |
| `threads_pilot_v1_2026-05_limited_extension_run_record_0004.md` | Non-sensitive tracked run record for the item 11-15 limited extension after the first checkpoint decision. |
| `threads_pilot_v1_2026-05_risk_probe_run_record_0005.md` | Non-sensitive tracked run record for the first multi-term high-risk case-finding probe before item 16. |
| `threads_pilot_v1_2026-05_risk_probe_run_record_0006.md` | Non-sensitive tracked run record for the normalized no-space risk-probe retry before item 16. |
| `threads_pilot_v1_2026-05_access_path_review_run_record_0007.md` | Non-sensitive tracked run record for the approved session/API access-path review before item 16. |
| `threads_pilot_v1_2026-05_browser_session_execution_run_record_0009.md` | Non-sensitive tracked run record for the first approved browser-session item 0016 attempt. |
| `threads_pilot_v1_2026-05_browser_session_limited_extension_run_record_0010.md` | Non-sensitive tracked run record for the item 0017-0020 limited browser-session extension with negation filtering. |
| `threads_pilot_v1_2026-05_method_revision_run_record_0011.md` | Non-sensitive tracked run record for the item 0017 method-revision diagnostic design after run 0010 produced no selected item. |
| `threads_pilot_v1_2026-05_evidence_path_design_run_record_0012.md` | Non-sensitive tracked run record defining scoped evidence-path boundaries before any further item 0017 attempt. |
| `threads_pilot_v1_2026-05_scoped_evidence_execution_run_record_0013.md` | Non-sensitive tracked run record for a future single item 0017 scoped evidence execution attempt. |
| `threads_pilot_v1_2026-05_evidence_scope_review_gate_0014.md` | Non-sensitive stakeholder evidence-scope review gate required before any item 0017 retry, item 0018 attempt, or evidence-expansion run. |
| `threads_pilot_v1_2026-05_evidence_expansion_run_record_0015.md` | Non-sensitive tracked run record for the first bounded item 0018-to-0027 evidence-expansion tranche after gate 0014 approval. |
| `threads_pilot_v1_2026-05_work_order.md` | Pilot batch work order. |
| `threads_pilot_v1_2026-05_readiness_review.md` | Real-pilot readiness review. |
| `threads_pilot_v1_2026-05_guideline_revision_log.md` | Accepted calibration-driven guideline revisions for the first governed rehearsal and pilot batch. |
| `../../docs/40-pilot-preflight-verification.md` | Repo and local workspace preflight before item 1. |
| `../../templates/manual_collection_rehearsal_checklist.md` | Checklist for the first 1-2 controlled real rehearsal items. |
| `../../templates/controlled_rehearsal_review.md` | Aggregate-only review template for turning the 1-2 item rehearsal into a decision. |
| `../../templates/annotation_qa_checklist.md` | Annotation and calibration QA checklist for the first pilot batch. |
| `../../docs/38-first-pilot-checkpoint-protocol.md` | Required first 10-15 item checkpoint protocol. |
| `../../templates/pilot_checkpoint_review.md` | Checkpoint review template. |
| `../../decision-log/0017-record-integrated-synthetic-launch-rehearsal.md` | Decision record preserving the controlled-launch gate after the synthetic rehearsal. |
| `../../decision-log/0018-record-cib-api-and-automation-authorization.md` | Decision record for CIB-authorized API access and automation. |
| `../../experiments/evaluation-notes/0008-phase1-synthetic-launch-rehearsal.md` | Synthetic-only launch rehearsal results. |
| `../../experiments/evaluation-notes/0012-synthetic-calibration-guideline-revision.md` | Calibration-driven guideline and answer-key revision note. |
| `../../experiments/evaluation-notes/0013-controlled-rehearsal-boundary-watchlist.md` | Watchlist for the first 1-2 controlled real rehearsal items. |
| `../../experiments/evaluation-notes/0014-controlled-rehearsal-review-protocol.md` | Repo-safe decision protocol after the first 1-2 controlled real rehearsal items. |

## Launch Status

Status: `go_with_limits`.

Meaning:

- The stakeholder outcome has been recorded as approved.
- The project owner explicitly approved the requirement that exact source, storage, access, retention, and redaction limits be written into the launch record before collection.
- The pilot remains limited to the first 50 Threads items before the decision memo, unless a later work order expands it.
- CIB explicitly authorizes API access and all research-required automation under the controlled launch record.
- Production scoring, public accusation, and legal fraud determinations are not approved.
- Raw evidence must stay outside git.
- Exact raw storage location, API credentials, automation logs, access list, and any sensitive source identifiers must be held in the approved controlled location, not in this repository.
- The item-1 preflight must pass after local workspace initialization.
- The calibration-driven guideline revision log should be reviewed before the first governed rehearsal item.
- The pilot must pause after the first 10-15 collected or annotated rows for checkpoint review.
- The integrated synthetic launch rehearsal is tooling evidence only; it does not authorize item 1.

No raw Threads evidence has been collected or committed in this folder. As of `2026-04-24`, the first 15 controlled local records have been collected under ignored local files and summarized only in repo-safe aggregate notes. Risk-probe runs 0005 and 0006 did not produce extractable item content, and access-path review run 0007 did not attempt collection, so item 0016 remains uncreated.

As of `2026-04-25`, access-path preparation run 0008 has prepared the repo-safe browser/API access tooling. The next execution run still must wait for a real approved browser storage-state/session artifact in controlled storage or real approved API probe inputs in the controlled env file. Templates, manifests, query echoes, and UI text cannot become item 0016.

Later on `2026-04-25`, the approved browser storage-state artifact was exported into the outside-git controlled store and passed shape validation. Run 0009 is now opened as the next single-item browser-session execution run for item 0016. It allows at most one selected item and at most 5 candidates for the selected probe seed.

Run 0009 then selected one item 0016 candidate and built a strict-valid local record under ignored `data/interim/`. Second review changed item 0016 from preliminary `uncertain` / `medium` to final `non_scam` / `low`; it is now treated as a false-positive pressure example. Run 0010 attempted all five planned item 0017 risk-probe seeds under the approved browser-session path. Each seed reviewed 5 candidates, no safe redacted item was selected, and no `manual_entry_0017.json` was created. Decision 0026 required method revision before another item 0017 attempt or any move toward item 0018. Run 0011 executed the revised diagnostic design and built a local item 0017 trace, but second review excluded it because the retained visible text was only a query echo. The query-echo filter has now been patched, all four revised seeds have been attempted, and no reviewable candidate remains. Decision 0027 pauses the text-only item 0017 extension. Decision 0028 selects a scoped evidence-path study for run 0012 using domain-only link/redirect-category evidence plus narrow reply-context feasibility. Run 0012 design has been reviewed and accepted. Run 0013 executed one scoped item 0017 attempt; no reviewable candidate was found and no item was built. Decision 0029 stops the item 0017 extension for the current pilot tranche. Decision 0030 opens evidence-scope review gate 0014. Decision 0031 records stakeholder approval for all proposed evidence families with run-level limits: at most 20 candidates reviewed and at most 10 selected items. Run 0015 then reviewed 20 candidates, built local items 0018-0023, and completed second review. The checkpoint now has 23 strict-valid local records: 22 non-excluded records and 1 excluded method-review trace.
