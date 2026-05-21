# Changelog

This file tracks repository operating versions for the Threads scam-content research scaffold. It is separate from dataset versions, schema versions, annotation guideline versions, and experiment run names.

Do not record raw Threads evidence, source URLs, account handles, credentials, session artifacts, screenshots, or sensitive controlled-run details here. Record only repo-safe change summaries, affected paths, verification, and decision references.

## v1.3.8 - 2026-05-21

- Type: patch
- Previous version: v1.3.7
- Categories: application-status;governance;data-access;planning
- Summary: Record Research Tools submitted review status

### Detailed Changes

- Recorded the submitted Research Tools Manager status page: application under independent review, submitted on May 21, 2026, Submission completed, CASD review active, Meta processing and Approval pending, and typical CASD review time of 2-3 weeks.
- Captured requested tool-access visibility for Meta Content Library and Meta Content Library API, lead access pending state, collaborator invitation availability, and the operational boundary that visible tool controls do not authorize MCL UI/API use before approval and controlled activation.

### Affected Paths

- `notes/2026-05-21-meta-research-tools-manager-submission-review-status-page.md`
- `notes/2026-05-21-meta-research-tools-manager-application-flow.md`
- `templates/meta_research_tools_application_prep.md`
- `docs/51-meta-content-library-api-access.md`
- `docs/53-first-principle-meta-research-tools-application-strategy.md`
- `docs/54-meta-official-product-documentation-requirements.md`

### Verification

- `git diff --check`
- `python3 scripts/validate_thread_dataset.py data/samples/thread_item_sample_batch.csv`
- `python3 -m py_compile scripts/record_version_update.py`

### Sources

- User-provided Research Tools Manager submitted application review-status screenshot

### Sensitive Data Check

- Repo-visible files omit application ID, logged-in account identity, screenshots, personal legal identity, credentials, raw Threads evidence, handles, source URLs from controlled data, cleanroom exports, collaborator email addresses, invitation links, and item-level controlled artifacts. The lead researcher row is recorded only as role/status, not personal identity.

## v1.3.7 - 2026-05-21

- Type: patch
- Previous version: v1.3.6
- Categories: application-prep;governance;legal-boundary;privacy
- Summary: Record Research Tools terms and conditions page status

### Detailed Changes

- Recorded the Terms and Conditions page state, including unchecked and checked checkbox states, enabled/disabled submit button states, visible controls, and section-by-section terms implications from the user-provided terms excerpt.
- Captured operational compliance boundaries: Approved Purpose only, no scraping/crawling/TDM, no unauthorized export/download/combination/commercial use, no shared access, publication/citation/notice requirements, data-protection/deletion/notification duties, confidentiality, termination, and warranty/liability boundaries.

### Affected Paths

- `notes/2026-05-21-meta-research-tools-manager-terms-and-conditions-page.md`
- `notes/2026-05-21-meta-research-tools-manager-application-flow.md`
- `templates/meta_research_tools_application_prep.md`
- `docs/51-meta-content-library-api-access.md`
- `docs/53-first-principle-meta-research-tools-application-strategy.md`
- `docs/54-meta-official-product-documentation-requirements.md`

### Verification

- `git diff --check`
- `python3 scripts/validate_thread_dataset.py data/samples/thread_item_sample_batch.csv`
- `python3 -m py_compile scripts/record_version_update.py`

### Sources

- User-provided Research Tools Manager Terms and Conditions screenshots and pasted terms excerpt

### Sensitive Data Check

- Repo-visible files omit application ID, logged-in account identity, screenshots, access credentials, raw Threads evidence, handles, source URLs from controlled data, cleanroom exports, collaborator email addresses, invitation links, and item-level controlled artifacts. Long legal text is recorded as structured summary rather than full reproduced terms.

## v1.3.6 - 2026-05-21

- Type: patch
- Previous version: v1.3.5
- Categories: application-prep;governance;privacy
- Summary: Record Research Tools collaborators page status

### Detailed Changes

- Recorded the optional Collaborators page state, including completed prior sections, active collaborators step, blank collaborator email field, unused Add another control, and enabled Next button.
- Clarified that collaborator emails, invitation links, collaborator application status, and collaborator personal details must stay outside git.

### Affected Paths

- `notes/2026-05-21-meta-research-tools-manager-collaborators-page.md`
- `notes/2026-05-21-meta-research-tools-manager-application-flow.md`
- `templates/meta_research_tools_application_prep.md`
- `docs/51-meta-content-library-api-access.md`
- `docs/53-first-principle-meta-research-tools-application-strategy.md`

### Verification

- `git diff --check`
- `python3 scripts/validate_thread_dataset.py data/samples/thread_item_sample_batch.csv`
- `python3 -m py_compile scripts/record_version_update.py`

### Sources

- User-provided Research Tools Manager Collaborators screenshot

### Sensitive Data Check

- Repo-visible files omit application ID, logged-in account identity, screenshots, collaborator email addresses, invitation links, private access details, raw Threads evidence, handles, source URLs from controlled data, credentials, cleanroom exports, and item-level controlled artifacts.

## v1.3.5 - 2026-05-21

- Type: patch
- Previous version: v1.3.4
- Categories: application-prep;governance;data-access;secure-environment
- Summary: Record Meta official product documentation requirements

### Detailed Changes

- Added a structured requirements record for Meta Content Library/API and Meta Secure Research Environment official documentation, including eligibility, application flow, data scope, API/export restrictions, SRE cleanroom restrictions, support/status, citations, disclaimers, and changelog implications.
- Recorded the latest Research Tools Manager bottom-section screenshot state: web tool and API selected, Meta Secure Research Environment selected, SOMAR not selected, and both confirmations checked.

### Affected Paths

- `docs/54-meta-official-product-documentation-requirements.md`
- `docs/51-meta-content-library-api-access.md`
- `docs/53-first-principle-meta-research-tools-application-strategy.md`
- `notes/2026-05-21-meta-research-tools-manager-research-details-page.md`
- `templates/meta_research_tools_application_prep.md`

### Verification

- `git diff --check`
- `python3 scripts/validate_thread_dataset.py data/samples/thread_item_sample_batch.csv`
- `python3 -m py_compile scripts/record_version_update.py`

### Sources

- Meta official Content Library/API documentation
- Meta official Secure Research Environment documentation
- User-provided Research Tools Manager bottom-section screenshot

### Sensitive Data Check

- Repo-visible files omit application ID, logged-in account identity, screenshots, private access details, raw Threads evidence, handles, source URLs from controlled data, credentials, cleanroom exports, and item-level controlled artifacts. Official public documentation URLs and paraphrased requirements were recorded.

## v1.3.4 - 2026-05-21

- Type: patch
- Previous version: v1.3.3
- Categories: application-prep;governance;data-access
- Summary: Record Research Tools research details page status

### Detailed Changes

- Recorded the Research details page fields, full drafted application text, EU systemic-risk selection, selected research tools, secure-computing platform, and required confirmations.
- Noted that the research title is at the 60-character limit and appears to end mid-word before submission.

### Affected Paths

- `notes/2026-05-21-meta-research-tools-manager-research-details-page.md`
- `notes/2026-05-21-meta-research-tools-manager-application-flow.md`
- `templates/meta_research_tools_application_prep.md`
- `docs/51-meta-content-library-api-access.md`
- `docs/53-first-principle-meta-research-tools-application-strategy.md`

### Verification

- `git diff --check`
- `python3 scripts/validate_thread_dataset.py data/samples/thread_item_sample_batch.csv`
- `python3 -m py_compile scripts/record_version_update.py`

### Sources

- User-provided Research Tools Manager Research details screenshots

### Sensitive Data Check

- Repo-visible files omit application ID, logged-in account identity, screenshots, private access details, raw Threads evidence, handles, source URLs, credentials, and item-level controlled artifacts. The recorded research text contains application content but no raw evidence or private personal-information values.

## v1.3.3 - 2026-05-21

- Type: patch
- Previous version: v1.3.2
- Categories: application-prep;governance;privacy
- Summary: Record Research Tools organization page status

### Detailed Changes

- Recorded the Organization page fields, repo-safe filled status, institutional verification guidance, and direct-affiliation redaction boundary.
- Stored complete observed organization values only in ignored local private storage under data/private/.

### Affected Paths

- `notes/2026-05-21-meta-research-tools-manager-organization-page.md`
- `templates/meta_research_tools_application_prep.md`
- `docs/53-first-principle-meta-research-tools-application-strategy.md`

### Verification

- `git diff --check`

### Sources

- User-provided Research Tools Manager Organization screenshot

### Sensitive Data Check

- Repo-visible files retain public institution-level values but redact department-level affiliation, role, applicant-verification URL, application ID, logged-in identity, and any private application details. Actual values were stored only in ignored local private storage under data/private/.

## v1.3.2 - 2026-05-21

- Type: patch
- Previous version: v1.3.1
- Categories: application-prep;privacy
- Summary: Record filled Research Tools personal information status

### Detailed Changes

- Recorded the filled-state status of the Research Tools Manager personal-information page with identity-bearing values redacted from git.
- Noted that the city field is still blank and is the likely blocker for the disabled Next button.

### Affected Paths

- `notes/2026-05-21-meta-research-tools-manager-personal-information-page.md`
- `templates/meta_research_tools_application_prep.md`

### Verification

- `git diff --check`

### Sources

- User-provided filled Research Tools Manager personal-information screenshot

### Sensitive Data Check

- Repo-visible files redact legal name, email, ORCID, CV file name, application ID, and uploaded file details. Actual values were stored only in ignored local private storage under data/private/.

## v1.3.1 - 2026-05-21

- Type: patch
- Previous version: v1.3.0
- Categories: application-prep;governance
- Summary: Record Research Tools personal information page guidance

### Detailed Changes

- Added a repo-safe transcription of the Research Tools Manager personal-information page and field-level filling guidance for legal name, location, institutional email, discipline, ORCID, and CV upload.
- Updated the application prep template so final personal values stay outside git while form strategy is reusable.

### Affected Paths

- `notes/2026-05-21-meta-research-tools-manager-personal-information-page.md`
- `templates/meta_research_tools_application_prep.md`
- `docs/53-first-principle-meta-research-tools-application-strategy.md`

### Verification

- `git diff --check`

### Sources

- User-provided Research Tools Manager personal-information screenshot

### Sensitive Data Check

- No legal name, organizational email, ORCID, CV file, application ID, access email, screenshot file, raw Threads evidence, handles, URLs, credentials, or item-level controlled artifacts added.

## v1.3.0 - 2026-05-21

- Type: minor
- Previous version: v1.2.9
- Categories: governance;data-access;research-design;application-prep
- Summary: Add first-principle Meta Research Tools application strategy

### Detailed Changes

- Added a first-principle Research Tools Manager application strategy that frames trust, governance, data minimization, and reviewer support as the scarce-resource problem.
- Recorded Decision 0160 so the application is not framed as app-building, scraping, platform policing, or autonomous scam detection.
- Updated README, recommended path, and Meta Content Library/API access notes to route future application prep through the new strategy document.

### Affected Paths

- `docs/53-first-principle-meta-research-tools-application-strategy.md`
- `decision-log/0160-record-first-principle-meta-research-tools-application-strategy.md`
- `decision-log/README.md`
- `README.md`
- `docs/18-recommended-path-v1.md`
- `docs/51-meta-content-library-api-access.md`

### Decision References

- `decision-log/0160-record-first-principle-meta-research-tools-application-strategy.md`

### Verification

- `git diff --check`
- `python3 scripts/validate_thread_dataset.py data/samples/thread_item_sample_batch.csv`

### Sources

- User request to apply FIRST PRINCIPLE to Meta Research Tools Manager application planning

### Sensitive Data Check

- No raw Threads evidence, credentials, tokens, screenshots, source URLs, account handles, browser exports, or item-level controlled artifacts added.

## v1.2.9 - 2026-05-21

- Type: patch
- Previous version: v1.2.8
- Categories: governance;data-access;application-prep
- Summary: Record Research Tools Manager application framing notes

### Detailed Changes

- Expanded the Research Tools Manager screenshot note with application framing, CASD review interpretation, project advantages, public-interest language, governance boundaries, ethics questions, and minimal viable research architecture.
- Added a Meta Research Tools application prep template for research purpose, official-access necessity, data governance, human-review routing, and IRB/privacy planning.
- Updated the Meta Content Library/API access record and data authorization request template so future applications avoid app-builder, policing, scraping, or autonomous-enforcement framing.

### Affected Paths

- `notes/2026-05-21-meta-research-tools-manager-application-flow.md`
- `templates/meta_research_tools_application_prep.md`
- `docs/51-meta-content-library-api-access.md`
- `templates/data_authorization_request.md`

### Decision References

- `decision-log/0158-require-meta-content-library-api-route.md`

### Verification

- `git diff --check`
- `python3 scripts/validate_thread_dataset.py data/samples/thread_item_sample_batch.csv`

### Sources

- User-provided Meta Research Tools Manager screenshot and application-framing notes

### Sensitive Data Check

- No raw Threads evidence, credentials, tokens, screenshots, source URLs, account handles, browser exports, or item-level controlled artifacts added.

## v1.2.8 - 2026-05-21

- Type: patch
- Previous version: v1.2.7
- Categories: governance;data-access;research-design
- Summary: Record Meta Content Library research-scale platform notes

### Detailed Changes

- Added a repo-safe conceptual note explaining Meta Content Library / API as official research-scale social data infrastructure rather than a normal app API.
- Updated the Meta Content Library/API access record with scam-research fit, keyword diffusion, producer-list, trend-analysis, and human-review routing implications.
- Preserved key boundaries: Threads coverage is public-profile and follower-threshold limited; UI/API/export availability must be checked per approved environment; missing official coverage is not permission to scrape.

### Affected Paths

- `notes/2026-05-21-meta-content-library-research-scale-platform.md`
- `docs/51-meta-content-library-api-access.md`

### Decision References

- `decision-log/0158-require-meta-content-library-api-route.md`

### Verification

- `git diff --check`
- `python3 scripts/validate_thread_dataset.py data/samples/thread_item_sample_batch.csv`

### Sources

- User-provided Meta Content Library / API research-scale platform notes
- Meta Content Library / API official documentation links already recorded in docs/51-meta-content-library-api-access.md

### Sensitive Data Check

- No raw Threads evidence, credentials, tokens, screenshots, source URLs, account handles, browser exports, or item-level controlled artifacts added.

## v1.2.7 - 2026-05-21

- Type: patch
- Previous version: v1.2.6
- Categories: governance;data-access
- Summary: Record Meta Research Tools Manager application flow screenshot

### Detailed Changes

- Added a repo-safe transcription of the Research Tools Manager access-application workflow from the user-provided screenshot.
- Updated Meta Content Library/API access notes with the four-step application path, expected review and processing windows, and privacy boundaries for access emails and account identity.
- Extended the data authorization request template with Research Tools Manager, CASD review, Meta processing, and access-email status fields.

### Affected Paths

- `notes/2026-05-21-meta-research-tools-manager-application-flow.md`
- `docs/51-meta-content-library-api-access.md`
- `templates/data_authorization_request.md`

### Decision References

- `decision-log/0158-require-meta-content-library-api-route.md`

### Verification

- `git diff --check`
- `python3 scripts/validate_thread_dataset.py data/samples/thread_item_sample_batch.csv`

### Sources

- User-provided Meta Research Tools Manager screenshot

### Sensitive Data Check

- No raw Threads evidence, credentials, tokens, screenshots, source URLs, account handles, browser exports, or item-level controlled artifacts added.

## v1.2.6 - 2026-05-21

- Type: initial repository operating baseline
- Previous version: none
- Categories: governance; data-access; model-candidate; tooling
- Summary: Initialize repo-level versioning after Breeze Guard 26 and Meta Content Library/API route records.

### Detailed Changes

- Added Breeze Guard 26 as a deferred Taiwan-localized safety-classifier candidate, not a current Phase 1 launch dependency and not a final scam, legal, financial, or medical adjudicator.
- Added Meta Content Library / API as the preferred official research access route for the CIB/165 Threads case, with regular Threads API keyword search treated as a scoped supplement only when a controlled run record approves it.
- Preserved the existing design direction: a governed, human-review-oriented research scaffold rather than a production detector, full-platform OSINT monitor, or scraping system.
- Added an automated repo-version logging mechanism so future changes can bump `vMAJOR.MINOR.PATCH`, update `VERSION`, and append both Markdown and CSV logs.
- Clarified that repo versions are separate from dataset manifests, schema IDs, guideline versions, baseline run names, and controlled run records.

### Affected Paths

- `VERSION`
- `CHANGELOG.md`
- `versioning/README.md`
- `versioning/version_log.csv`
- `scripts/record_version_update.py`
- `scripts/README.md`
- `docs/52-automated-versioning-and-change-log.md`
- `docs/05-data-strategy.md`
- `docs/18-recommended-path-v1.md`
- `docs/19-codex-workflow.md`
- `README.md`
- `AGENTS.md`
- `decision-log/0157-record-breeze-guard-26-as-deferred-candidate.md`
- `decision-log/0158-require-meta-content-library-api-route.md`
- `decision-log/0159-add-automated-versioning-and-change-log.md`
- `decision-log/README.md`

### Verification

- `git diff --check`
- `python3 scripts/validate_thread_dataset.py data/samples/thread_item_sample_batch.csv`
- `python3 scripts/record_version_update.py --dry-run --bump patch --summary "Dry-run versioning smoke test" --category tooling --detail "Verify the script can compute the next patch version without writing files." --path scripts/record_version_update.py --verification "dry-run only"`

### Sensitive Data Check

- No raw Threads evidence, credentials, tokens, screenshots, source URLs, account handles, browser exports, or item-level controlled artifacts were added to the version log.
