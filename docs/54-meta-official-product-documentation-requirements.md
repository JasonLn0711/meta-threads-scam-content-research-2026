# Meta Official Product Documentation Requirements Record

## Purpose

This record captures the repo-safe operational requirements from Meta's official
product documentation for:

- Meta Content Library and API
- Meta Secure Research Environment

It is a structured compliance and planning note, not a copy of Meta's full
website. The official pages remain the source of truth and should be checked
again before submission, onboarding, API use, publication, or any controlled
data run.

## Source Snapshot

- Snapshot date: 2026-05-21
- Primary sources:
  - `https://developers.facebook.com/docs/content-library-and-api`
  - `https://developers.facebook.com/docs/content-library-and-api/get-access`
  - `https://developers.facebook.com/docs/content-library-and-api/content-library`
  - `https://developers.facebook.com/docs/content-library-and-api/content-library-api`
  - `https://developers.facebook.com/docs/content-library-api/overview`
  - `https://developers.facebook.com/docs/content-library-api/quick-start`
  - `https://developers.facebook.com/docs/content-library-api/guides`
  - `https://developers.facebook.com/docs/content-library-and-api/appendix`
  - `https://developers.facebook.com/docs/content-library-and-api/support`
  - `https://developers.facebook.com/docs/content-library-and-api/disclosures-disclaimers`
  - `https://developers.facebook.com/docs/content-library-and-api/citations`
  - `https://developers.facebook.com/docs/content-library-and-api/changelog`
  - `https://developers.facebook.com/docs/secure-research-environment`
  - `https://developers.facebook.com/docs/secure-research-environment/overview`
  - `https://developers.facebook.com/docs/researcher-platform/secure-browser`
  - `https://developers.facebook.com/docs/researcher-platform/features`
  - `https://developers.facebook.com/docs/researcher-platform/support`
  - `https://developers.facebook.com/docs/researcher-platform/changelog`
- Screenshot source: user-provided Research Tools Manager screenshot showing
  research-tool selections, secure-computing-platform selection, and required
  confirmations.

## Product Model

Meta Content Library and API are controlled-access research products.

| Product | Official role | Repo interpretation |
|---|---|---|
| Meta Content Library | Web-based research tool for exploring and searching publicly accessible content across supported Meta technologies. | Primary route for Threads public-content discovery when the approved account exposes Threads. |
| Meta Content Library API | Programmatic API for querying and analyzing the public content archive in Python or R inside Meta Secure Research Environment or an approved third-party cleanroom. | Programmatic route only inside the approved cleanroom; do not assume local export or full Threads parity with the web UI. |
| Meta Secure Research Environment | Virtual data cleanroom based on a modified Jupyter environment in Amazon WorkSpaces Secure Browser. | Approved computation environment, not a local collection or download path. |

## Current Application Selections

The user-provided screenshot confirms this application draft state:

| Form area | Current selection |
|---|---|
| Meta Content Library web-based tool | Selected |
| Meta Content Library API via secure computing platform | Selected |
| Secure computing platform | `Meta Secure Research Environment` selected |
| Alternative secure platform | `SOMAR Virtual Data Enclave` not selected |
| Product-documentation / API-field confirmation | Checked |
| Scientific-discipline / public-interest confirmation | Checked |

Operational meaning:

- The project is asking for both the web-based research interface and API access.
- API work should be assumed to happen only inside Meta Secure Research Environment unless the application is later changed and approved for a different secure platform.
- The checked documentation confirmation should be treated as a real attestation: the team should understand the relevant fields, data types, endpoints, and export restrictions before submission.

## Terms And Conditions Application Gate

Later user-provided screenshots of the live Research Tools Manager application
show the `Terms and Conditions` page after personal information, organization,
research details, and collaborators were completed.

Repo-safe record:

- [../notes/2026-05-21-meta-research-tools-manager-terms-and-conditions-page.md](../notes/2026-05-21-meta-research-tools-manager-terms-and-conditions-page.md)

Recorded visible state:

- Image 1: required application/terms confirmation unchecked, marketing-consent
  checkbox unchecked, and `Agree & submit application` disabled.
- Image 2: both checkboxes checked and `Agree & submit application` enabled.
- Visible linked materials include the Data Processing Agreement, Terms of
  Service, and Privacy Policy.

Terms-driven operational requirements for this repo:

- Use Research Tools only for the Approved Purpose.
- Do not scrape, crawl, harvest, or perform unauthorized text/data mining of
  Research Tools.
- Do not re-identify, profile, track, or accuse individual users.
- Do not export, download, combine, sell, commercially exploit, or benchmark
  Meta Data outside what the terms and official environment allow.
- Do not share access; collaborators need their own approved path.
- Protect, separate, retain, and delete Meta Data according to the approved
  purpose and Meta's requirements.
- Notify Meta promptly, and within the terms-stated two-day window, for
  relevant authority/data-subject requests, investigations, complaints, or
  inability to comply.
- Publish only permitted Research Outputs, cite the correct Meta
  product/version, preserve limitations, and avoid implying Meta endorsement.

This record summarizes the user-provided terms excerpt for project governance.
It is not legal advice and does not replace live review of the official terms
before submission or use.

## Submitted Application Status

A later Research Tools Manager status screenshot shows the application has been
submitted and is under independent review:

- submitted date shown by UI: 2026-05-21
- current status: `Application under independent review`
- current stage: CASD review
- typical CASD review time shown by UI: `2-3 weeks`
- later stages shown but not reached: Meta processing and Approval
- lead researcher access: pending
- requested access shown: Meta Content Library and Meta Content Library API

Repo-safe record:

- [../notes/2026-05-21-meta-research-tools-manager-submission-review-status-page.md](../notes/2026-05-21-meta-research-tools-manager-submission-review-status-page.md)

Operational meaning:

- Approval has not been granted.
- Tool access has not been activated.
- No official run should begin until approval, access details, environment
  availability, storage, retention, redaction, and run-record boundaries are
  confirmed.

## Eligibility Requirements

Access is application-based and reviewed through Research Tools Manager.

Eligibility constraints recorded from the official documentation:

- Applicants must be affiliated with a qualified academic institution or a
  qualified research institution.
- Academic institutions must be education/research oriented, accredited or able
  to document equivalent qualification, degree-granting, and not-for-profit.
- Non-academic institutions must be not-for-profit, with scientific or
  public-interest research as a primary purpose or core activity.
- Applicants can be from different disciplinary or professional backgrounds.
- Global users may apply, but access and use must comply with applicable laws,
  rules, and regulations.
- The researcher, affiliated organization, and affiliated institution must not
  be in a jurisdiction targeted by sanctions from the United States, United
  Kingdom, European Union, or United Nations.

## Application And Access Workflow

The official workflow is:

1. Review application requirements, the application guide, and product documentation.
2. The lead researcher submits the research program, organization, and collaborator details through Research Tools Manager.
3. CASD independently reviews eligibility for Meta Content Library access.
4. CASD review can take 2 to 3 weeks.
5. Meta processing typically takes another 2 to 3 weeks after application review.
6. If approved, access details arrive by email and access status appears in Research Tools Manager.
7. Lead researchers can invite collaborators from the Research Tools Manager dashboard.

Important workflow requirements:

- Research Tools Manager is desktop/laptop oriented; the official page says the current version does not work on mobile devices.
- Collaborators should be invited by the lead researcher and their collaborator applications are reviewed only after the lead researcher is approved.
- A substantially changed research agenda requires a new application.
- Lead researchers who change institutions need a new application and should notify Meta.
- Collaborators who change institutions need a new organizational email invitation, a new application, and notification to Meta.

## Costs And Access Environment

For Meta Secure Research Environment:

- Official documentation says there are no fees for access or computation for
  Meta Content Library web UI or Content Library API on Meta Secure Research
  Environment.
- Secure Research Environment compute is described as free.
- Third-party cleanrooms may have their own interface, procedures, and terms
  outside Meta's SRE documentation.

## Content Library Data Scope

### Facebook

Public Content Library data includes:

- posts to Pages, groups, events, verified public profiles, and public profiles
  with 100 or more followers;
- public Marketplace listings from eligible Pages or profiles, subject to
  exclusions such as older sold listings, stale listings, hidden-from-friends
  settings, and some job listings;
- public fundraisers and fundraisers attached to public posts;
- public Facebook channels meeting audience and creator eligibility criteria,
  plus channel messages within public channels.

Downloadable Facebook subset is narrower than view-only access and requires
application approval plus consent to the applicable Meta Research Tools terms.

### Instagram

Public Content Library data includes:

- posts from business and creator accounts;
- posts from public personal accounts that are verified or have 100 or more
  followers;
- public Instagram fundraisers;
- public Instagram channels that satisfy audience and creator eligibility
  criteria, plus channel messages.

Downloadable Instagram subset is narrower than view-only access and requires
approval and applicable terms consent.

### Threads

Public Content Library data includes:

- posts shared by public Threads profiles with 100 or more followers.

Important limitation:

- Threads content is not available for download while the dataset is in
  development, because data quality may have significant variation.
- The web-based tool and API may not have identical Threads behavior; this repo
  must verify Threads availability in the approved environment before relying
  on any API workflow.

### WhatsApp Channels

Public Content Library data includes:

- WhatsApp channels that are verified or have at least 100 followers;
- channel updates within eligible channels from the last 30 days.

Private WhatsApp chats are not included.

## Geographic, Audience, And Language Scope

Official documentation excludes public data/content from:

- China
- North Korea
- South Korea
- Togo

Operational interpretation:

- Eligible public surfaces generally require an admin, owner, account, profile,
  channel, or relevant producer country/region to be in a non-excluded location.
- Only posts or messages from non-excluded countries/territories are in scope
  once the surface itself qualifies.
- Multimedia from Illinois and Texas is excluded from data downloads where
  downloads are available.
- Age-restricted content may not be surfaced because it is not treated as
  publicly accessible.
- Location-restricted content can be unavailable depending on the viewer,
  cleanroom location, platform, and legal/local restriction.
- Search results include all languages unless a language filter is applied and
  the relevant data type supports that filter.

## Threads-Relevant Visible Data Classes

For Threads posts, the Content Library documentation describes data classes such
as:

- likes;
- replies, including replies to previous replies;
- reply browsing in pages of up to 50 loaded replies at a time;
- text search, sorting, and date range filtering within loaded replies;
- reposts;
- views, subject to visibility thresholds and refresh timing;
- post owner;
- post date;
- text-only media state;
- photo media;
- video media.

Repo rule:

- Treat these as potential approved fields only after the actual account and
  approved environment expose them.
- Do not store post owner, handles, permalinks, raw reply text, screenshots, or
  URLs in git unless a later governance record explicitly approves a redacted
  representation.

## Content Library API Scope

The current API documentation snapshot describes version `v6.0`.

Recorded API scope:

- programmatic analysis in Python or R;
- approved use inside Meta Secure Research Environment or an approved
  third-party cleanroom;
- access to public Facebook, Instagram, and WhatsApp data classes listed in
  the official API overview;
- no local API download path;
- up to 100,000 results per query where supported;
- more than 100 data fields across supported endpoints;
- asynchronous search support;
- endpoint guides for supported Facebook, Instagram, WhatsApp, comments,
  fundraisers, channels, and ID-based retrieval.

Endpoint-family documentation includes:

- Facebook Pages, groups, events, profiles, posts, Marketplace listings,
  fundraisers, channels, channel messages, donations, and comments;
- Instagram accounts, posts, fundraisers, channels, channel messages, and
  comments;
- WhatsApp channels and channel updates;
- bulk comments;
- ID-based retrieval;
- search, advanced search, rate limiting/query budgeting, and data deletion.

Conservative Threads reading:

- The web-based Content Library documentation explicitly includes Threads.
- The current API overview enumerates Facebook, Instagram, and WhatsApp data
  families and does not establish that all Threads UI functionality is
  available through the API.
- Therefore, this repo must not claim Threads API parity until the approved
  environment confirms it.

## API Download And Export Boundary

Key official restriction:

- Downloading Facebook, Instagram, Threads, or WhatsApp data from the Content
  Library API is not permitted by any means, whether using Meta Secure Research
  Environment or an approved third-party cleanroom.

Content Library UI download boundary:

- Downloading a public-data subset is available only in the web UI, not the API.
- UI download is available only after ICPSR or CASD approval and consent to the
  appropriate terms, including Meta Research Tools Terms and Conditions and/or
  an Information Sharing Agreement.
- Threads content is not downloadable while its dataset is marked in
  development.

Repo rule:

- API access is analysis access, not an export channel.
- Raw query outputs, exports, screenshots, URLs, handles, and cleanroom files
  stay outside git.

## Secure Research Environment Requirements

SRE is described as:

- a secure access route for qualified users;
- privacy-protected and controlled by data access policies;
- penetration-tested by internal and external security professionals;
- a modified Jupyter/JupyterHub/JupyterLab environment inside Amazon
  WorkSpaces Secure Browser;
- capable of Python, R, SQL, and standard statistical packages;
- a private research environment with free compute for qualified academics.

Hardware support described in the official documentation includes:

- memory guarantee of 50 GB and limit of 64 GB;
- 32 GB EBS storage, with no current S3 storage limit stated in the snapshot;
- 16 CPU cores;
- optional GPU server with G4dn.4xlarge class, 64 GiB memory, 16 GiB GPU
  memory, 125 GB instance storage, and up to 25 Gbps network performance.

## WorkSpaces Secure Browser Requirements

The SRE access route uses Amazon WorkSpaces Secure Browser.

Recorded requirements and constraints:

- WorkSpaces Secure Browser is mandatory as of 2025-02-27; OpenVPN access is no
  longer supported.
- The optional Chrome extension is recommended because it can reduce repeated
  Facebook login prompts.
- Users should pick the portal closest to their location for performance.
- Users should avoid unnecessary VPNs and disable browser extensions that
  interfere with keyboard shortcuts.
- The WorkSpaces toolbar can be minimized for performance and full-screen mode
  can be used for workspace efficiency.

Cleanroom restrictions:

- Only SRE and Facebook login URLs are accessible from inside WorkSpaces Secure Browser.
- Other internet sites are not accessible from inside the secure browser.
- Text can be copied into a Jupyter notebook.
- Text cannot be copied from the notebook out to the local environment.
- Notebook export is the approved alternative when supported.

Some environments permit upload/download through a temporary WorkSpaces shared
folder, but support depends on the specific research environment and product.

## SRE Feature Boundaries

Feature families described by official SRE documentation:

- CPU or GPU server selection, with switching possible by stopping and
  restarting the server.
- GPU dashboards are available only on GPU servers.
- Asynchronous queries are available for Python and are rate limited per user.
- Jupyter notebooks can be exported in a scrubbed format where outputs and raw
  cell data are removed according to privacy rules.
- Python packages can be installed through Meta's `Pip` wrapper; users should
  avoid upgrading or uninstalling system packages.
- R packages can be installed through Meta's Conda or CRAN wrappers; users
  should avoid removing system-level packages.
- Approved Hugging Face text models can be downloaded through Meta-provided
  utilities.
- Requests for additional Hugging Face models require a support ticket, a model
  link, and a use-case explanation tied to the approved research agenda.
- Newly approved models become available to all researchers, not only the
  requester.
- S3 bucket upload is supported for the Ad Targeting and URL Shares datasets,
  but the official SRE page states it is not supported for Meta Content
  Library.
- Notebook sharing is supported for collaborators in some environments through
  R workflows, not Python.

## Export, Publication, And Citation Requirements

Publication:

- Research outputs such as tables, graphs, and analysis may be published,
  subject to the Meta Research Tools Terms and Conditions.
- For publications based solely on Meta Content Library and/or API, Meta does
  not ask to review manuscripts before publication.
- Meta asks researchers to follow attribution/citation guidance and provide
  notice upon publishing.

Current citation records in the official docs:

- Meta Content Library API version `v6.0` DOI:
  `https://doi.org/10.48680/meta.metacontentlibraryapi.6.0`
- Meta Content Library version `v6.0` DOI:
  `https://doi.org/10.48680/meta.metacontentlibrary.6.0`

Repo rule:

- Any paper, report, or external handoff using MCL/API-derived results must cite
  the appropriate product/version and include the documented limitations.

## Support And Status

Official support routes:

- Meta Support Community / Direct Support for product support and troubleshooting.
- Get access page for access and eligibility questions.
- Data Transparency Status Page for disruptions or outages affecting Meta
  Content Library, Content Library API, or Secure Research Environment.
- Official docs recommend subscribing to the status page RSS feed.

Repo rule:

- Outages, disrupted queries, and platform issues should be recorded as run
  limitations, not silently retried with scraping or unofficial tooling.

## Disclosures, Disclaimers, And Data-Quality Boundary

Official documentation records these important limitations:

- Data governance and search-quality source details can change.
- Metrics can be affected by logging issues, fluctuating data quality, and
  incompleteness.
- Researchers are responsible for standard, thorough data cleaning.
- Researchers are responsible for analysis accuracy.
- Meta encourages users to report data quality, validity, or fidelity issues.
- Historical data and retention limits may prevent identified issues from being
  fixed.
- Post searches return posts by original producers, not collaborators.
- Meta does not warrant that the data will meet all research needs or
  expectations.
- Data may contain nonconformities, defects, or errors.
- Use may not be uninterrupted.
- Errors may not be corrected.

Repo rule:

- All results must preserve uncertainty and platform limitations.
- No report should claim full-platform coverage, perfect recall, legal fraud
  determination, or production-grade detection from MCL/API data alone.

## Changelog Items Relevant To This Project

Current official update history relevant to this repo:

- 2026-04-30: WhatsApp channels and channel updates are available for Content
  Library and API.
- 2026-03-12: Facebook channels and channel messages are available for Content
  Library and API.
- 2025-11-10: Content Library/API `v6.0` updates include threshold decrease to
  100 followers for certain Facebook profiles, Instagram personal accounts, and
  Threads public profiles; REST/OpenAPI updates; async jobs tooling.
- 2025-07-15: synchronous search result limit reduced from 500 to 100.
- 2025-02-27: WorkSpaces Secure Browser became mandatory; VPN access is no
  longer supported.
- 2025-02-06: search text in images extended to approximately 180 days for
  Facebook and Instagram posts, and bulk comments retrieval was added.
- 2024-11-11: `v5.0` introduced broader public-profile/personal-account access
  thresholds and API search ID sharing; older default sorting changed.
- 2026-05-21 local note: official docs should be checked again immediately
  before submission because access rules, product coverage, and API fields can
  change.

## Project-Specific Compliance Checklist

Before submitting or using MCL/API access:

- [ ] The Research Tools Manager application text matches the approved research
      agenda.
- [ ] The applicant and institution satisfy eligibility and sanctions checks.
- [ ] CASD/Meta approval is received before any MCL/API data use.
- [ ] All collaborators are invited through Research Tools Manager and approved
      before access.
- [ ] The team has reviewed product documentation, fields, data types,
      endpoints, export limits, and disclaimers.
- [ ] The selected secure platform is still Meta Secure Research Environment.
- [ ] Threads availability is checked in the approved environment.
- [ ] API coverage is verified before assuming Threads API parity.
- [ ] No API download/export is attempted.
- [ ] UI download is used only if explicitly approved, contractually allowed,
      and relevant to a downloadable dataset.
- [ ] Threads content is not downloaded while official docs mark it as
      non-downloadable.
- [ ] Raw outputs, screenshots, handles, URLs, access emails, environment
      details, and credentials stay outside git.
- [ ] Notebook exports are reviewed because scrubbed exports retain code,
      Markdown, and images.
- [ ] Support tickets and status-page incidents are logged as research
      limitations.
- [ ] Publications cite the correct product/version DOI and include
      limitations/disclaimers.

## First-Principle Reading

The scarce resource remains trust.

The official documentation makes the project boundary clearer:

- Official access is governed access, not a scraping substitute.
- API access is cleanroom analysis, not local data acquisition.
- SRE provides computation under privacy controls, not freedom to export raw
  platform data.
- Threads public data exists in the web tool subject to follower and download
  limits; API parity must be verified.
- Publications can use aggregate outputs, but they must cite the product and
  preserve limitations.
- The correct project claim is reviewer-support research under controlled
  public-content access, not legal adjudication or enforcement.
