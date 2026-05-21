# Meta Research Tools Manager Terms And Conditions Page Snapshot

- Date recorded: 2026-05-21
- Source: user-provided screenshots of the Meta Research Tools Manager application draft and user-provided Terms and Conditions excerpt
- Page section: `Terms and Conditions`
- URL / application identifier: intentionally omitted from git
- Screenshot files: not stored in git
- Repo-safe privacy note: this note records the terms-page field states and compliance implications only. It does not record the visible application ID, logged-in account identity, screenshots, access credentials, raw Threads evidence, handles, URLs, cleanroom exports, collaborator emails, invitation links, or item-level controlled artifacts.

## Visible Page State

- Visible application title at the top: `Metadata-Driven Public Scam Pattern Analysis and Reviewer Su`
- Left application list item: truncated application title with `Draft` status
- Left application stepper state:
  - `Personal information`: completed
  - `Organization`: completed
  - `Research details`: completed
  - `Collaborators`: completed
  - `Terms and Conditions`: active
- Main panel title: `Terms and Conditions`
- Bordered terms viewer title: `Meta Research Tools Terms and Conditions`
- Bottom controls visible: `Back` and `Agree & submit application`
- No `Save` or `Next` button is visible on this page in the screenshots.

## Checkbox And Submit-State Record

| Screenshot state | First confirmation checkbox | Marketing consent checkbox | Submit button state | Repo interpretation |
|---|---|---|---|---|
| Image 1 | Unchecked | Unchecked | Visible but disabled | Application cannot be submitted until at least the required terms confirmation is checked. |
| Image 2 | Checked | Checked | Visible and enabled | The UI permits submission after the visible confirmations are checked. |

The first checkbox is the legally important application and terms confirmation. It covers that the submitted information is the applicant's information, the Facebook profile is the applicant's own personal profile and not shared, the applicant has read and understood the Research Tools terms including linked data-processing and service terms, and application information may be used for eligibility review, partner support, and Research Tools improvement under Meta's privacy policy.

The second checkbox is marketing consent. It covers receiving marketing messages from Meta and notes that consent can be withdrawn or unsubscribed later. This is separate from the research-access terms confirmation.

Visible links in the checkbox area:

- Data Processing Agreement
- Terms of Service
- Privacy Policy

## Terms Source Handling

The user provided a long Terms and Conditions excerpt. This note records a complete section-by-section operational summary rather than copying the full legal text into the repo. The official Meta page remains the source of truth and should be reviewed again immediately before submission, access use, publication, export, or any controlled data run.

This record is not legal advice. It is an internal research-governance checklist for this repo.

## Section-By-Section Terms Record

### 1. Applicable Research Tools

The terms apply to the Meta Content Library user interface, Meta Content Library API, and Ads Transparency and Targeting Dataset. Meta may add other Research Tools at its discretion.

Project implication:

- Treat both the web-based Meta Content Library and Content Library API selections as governed Research Tools.
- Do not assume the same rights or export permissions across different Meta research products.

### 2. Definitions

The excerpt defines key terms including application, applicable law, approved purpose, confidential information, combined data, data-protection requirements, DPA, institution, Meta, Meta data, Meta TOS, personal data, publication, research, research outputs, research tools, Research Tools Manager, and the applicant.

Operational definitions that matter most for this repo:

- `Approved Purpose`: access is only for the research purpose authorized by Meta. Any other purpose requires prior written consent from Meta.
- `Meta Data`: any data or information made available by Meta or accessed through the Research Tools, including confidential information or personal data.
- `Combined Data`: data or output created by combining Meta Data with uploaded external data; it remains restricted like Meta Data unless it qualifies as a permitted Research Output.
- `Research`: non-commercial science or public-interest research.
- `Research Outputs`: permitted findings or results such as tables, charts, code, graphs, figures, and statistics, subject to restrictions on confidential information and personal data.
- `Research Tools Manager`: the portal for applications, status review, and collaborator management.

Project implication:

- The repo must separate Meta Data, Combined Data, and Research Outputs.
- Repo-visible files should contain only aggregate, redacted, or otherwise permitted Research Outputs.
- The approved research purpose must remain the control boundary for any MCL/API activity.

### 3. Access

Access requires a formal application through a Meta-approved channel. Application information is used to evaluate eligibility and support/improve the Research Tools. Meta may later require reconfirmation of affiliation, approved purpose, or related information; inability to confirm may terminate access. Optional testing or feedback may be governed by separate beta-testing terms.

Project implication:

- Treat application status and access status as governed state, not credentials.
- Notify Meta if the applicant's affiliation, research agenda, or access need changes.
- Do not treat approval as permanent or transferable.

### 4. Import And Export Policies

The Meta Research Tools Import and Export Policy is incorporated by reference and controls import/export matters if there is a conflict.

Project implication:

- Do not import outside data into the secure environment or export outputs unless the official import/export policy allows it.
- Do not use API access as a local download path.
- Review export permission before publishing tables, figures, code, examples, or notebook outputs.

### 5. Data Use

#### Obligations

The researcher must use Research Tools only for the Approved Purpose, comply with the terms and applicable Meta policies, process Research Outputs and Combined Data according to privacy/security requirements, comply with applicable law and data-protection requirements, disclose conflicts of interest, and notify Meta if affiliation, research topic, or access need changes.

Project implication:

- Every run must map back to the approved public-interest research purpose.
- Conflict-of-interest and agenda-change handling belongs in governance notes, not ad hoc messages.
- Changing from research to enforcement, product benchmarking, or production detection would require a new approval path.

#### Prohibited Practices

The excerpt prohibits attempts to bypass privacy/security protections, re-identify individuals, export or download Meta Data outside approved environments unless allowed, combine Meta Data with other data unless allowed, use Meta Data or derivatives in unauthorized research/services/products, sell or commercially exploit Meta Data/Combined Data/Research Outputs, crawl or scrape Research Tools, perform text/data mining on Research Tools, develop competing products or benchmark with Research Tools or Meta Data, misuse institutional policies/assets, or seek patent protection for inventions arising from research under these terms or against Meta/products/services.

Project implication:

- No scraping, crawling, browser harvesting, or unofficial workaround.
- No de-anonymization or identity linking.
- No local raw-data download or export unless explicitly approved.
- No commercial exploitation or product benchmarking.
- No patent-claim strategy should be built on Meta Data or Research Tools outputs.

#### Publication

The researcher may publish permitted Research Outputs according to the import/export policy and terms. Confidential information and personal data cannot be disclosed except where expressly permitted and tied to the Approved Purpose. For publications based solely on Meta Data, Meta asks for publication notice by email. Attribution/citation requirements must be followed. Meta's name, trademarks, logos, or endorsement cannot be implied beyond required attribution.

Project implication:

- External reports should publish aggregate findings, not raw posts, handles, source URLs, or confidential cleanroom details.
- Cite the correct Meta Content Library / API version and include limitations.
- Notify Meta upon relevant publication where required or requested.

#### Open Access

The excerpt asks researchers to make efforts to publish findings in open-access outlets consistent with Open Science.

Project implication:

- Prefer open-access publication routes for final academic outputs when feasible.

### 6. Data Protection

The researcher must protect Meta Data from loss, alteration, unauthorized disclosure, and unauthorized access; store Meta Data separately unless authorized; keep Research Tool access limited to the approved individual; delete Meta Data when it is no longer necessary, on expiration/termination, or at Meta's request; act as an independent controller under applicable data-protection requirements; and comply with Meta system/site policies if granted access.

The excerpt also requires prompt written notice to Meta, without undue delay and within two days, for relevant authority/data-subject investigations or complaints, authority requests for personal-data disclosure/access, or inability to comply with the terms. The DPA is incorporated. For European-region personal-data requirements, the researcher is treated as a third party or controller. The transfer details describe users/visitors of Meta products as data subjects, public user-generated content as the personal-data category, continuous transfer frequency, research for the Approved Purpose as the purpose, and retention only as needed for that purpose or as otherwise described.

Project implication:

- No shared logins, shared browser sessions, or credential sharing.
- No Meta Data in git.
- Store controlled data separately from other data unless authorization says otherwise.
- Deletion and retention rules must be written before any controlled run.
- Build a two-day incident/authority-request notification rule into governance runbooks.

### 7. Confidentiality

Meta Data, Research Tools, and information contained in them are treated as confidential information. Use is limited to what is necessary for the Approved Purpose. Disclosure is limited to parties with a need to know and appropriate confidentiality obligations. Upon expiration or termination, Meta's confidential information must be returned or destroyed as requested. Feedback given to Meta may be used by Meta without royalties or other consideration.

Project implication:

- Do not commit screenshots, UI internals, cleanroom details, or Meta Data.
- Do not share Research Tool output with collaborators unless their access and confidentiality status allow it.
- Treat support tickets, environment details, and exports as controlled material.

### 8. Publicity

The researcher may not use Meta's name, logo, trademarks, or issue public announcements or press releases about Meta or the terms except as allowed under the publication section.

Project implication:

- Research outputs should cite Meta products as required without implying Meta endorsement, partnership, approval of conclusions, or operational support.

### 9. Indemnification

The excerpt requires the researcher to defend and indemnify Meta and related parties for claims arising from breaches, intellectual-property issues, negligent or wrongful acts, fraud or dishonesty, and certain injuries or damages. Settlements require Meta's prior written consent.

Project implication:

- This is a high-stakes legal section. Obtain institutional or legal review if the research team is uncertain about signing authority, liability, or institutional coverage.

### 10. Limitation Of Liability

The excerpt limits liability for many categories of damages but carves out intellectual-property infringement, data-protection breaches, confidentiality breaches, indemnity obligations, and compliance-with-law breaches. It also states an aggregate liability cap tied to amounts paid by Meta or a stated USD threshold.

Project implication:

- Data protection, confidentiality, and compliance are not soft process concerns; they are high-risk contractual obligations.

### 11. Disclaimer Of Warranties

Meta disclaims warranties. Meta Data, Research Tools, and Meta properties are provided as-is. Data may contain defects or errors. Meta does not guarantee that the data or tools will meet research needs, be uninterrupted, or have all defects corrected.

Project implication:

- All reports must preserve uncertainty, data-quality limitations, missingness, and official-source constraints.
- Do not claim complete coverage, perfect recall, production-grade reliability, or legal proof from MCL/API output.

### 12. Termination

Meta may terminate the terms at any time, for any or no reason, upon notice. Certain obligations survive expiration or termination.

Project implication:

- Do not build the project as if access is guaranteed indefinitely.
- Keep reproducible aggregate research outputs and repo-safe methods, not dependence on permanent raw access.

### 13. General

The excerpt applies California law and venue in San Mateo County, California. It requires compliance with applicable laws, Meta policies, anti-corruption laws, export controls, and trade sanctions. It includes waiver/severability provisions and allows Meta to change the terms at any time with or without notice; continued use constitutes acceptance.

Project implication:

- Check terms and official documentation again before submission and before material use.
- Treat sanctions/export-control compliance and institutional eligibility as part of access readiness.

## Operational Compliance Checklist For This Project

Before submitting or using access:

- [ ] Confirm the application text still matches the exact Approved Purpose.
- [ ] Confirm the research remains non-commercial, scientific, and public-interest oriented.
- [ ] Confirm the project will not perform scraping, crawling, browser harvesting, or unofficial data mining of Research Tools.
- [ ] Confirm no attempt will be made to re-identify, profile, track, or accuse individual users.
- [ ] Confirm no local export/download of Meta Data will be attempted unless explicitly allowed.
- [ ] Confirm any imported external data or Combined Data plan is explicitly authorized.
- [ ] Confirm raw Meta Data, screenshots, handles, URLs, access emails, cleanroom exports, and controlled artifacts stay outside git.
- [ ] Confirm Research Tool access is not shared with collaborators or third parties.
- [ ] Confirm collaborator access, if any, goes through Research Tools Manager and approval.
- [ ] Confirm storage separation, retention, deletion, and incident notification rules exist before data use.
- [ ] Confirm the two-day notification rule is understood for relevant authority/data-subject requests or inability to comply.
- [ ] Confirm publications use Research Outputs only, cite the correct Meta product/version, preserve limitations, and avoid implying Meta endorsement.
- [ ] Confirm the team understands Meta can update terms or terminate access.
- [ ] Confirm the marketing-consent checkbox is intentionally selected or unselected before final submission.

## First-Principle Reading

The terms page turns the application from a form-filling task into a legal and governance commitment.

The scarce resource remains trust:

- Meta and CASD must trust that access will be used only for the approved public-interest purpose.
- The institution must trust that data protection, confidentiality, and liability boundaries are understood.
- The research team must trust that outputs remain publishable without exposing Meta Data or personal data.
- Future reviewers must be able to see why the project stayed with human-review routing and aggregate research outputs instead of scraping, production enforcement, or individual accusation.

For this repo, the correct operating conclusion is:

> Do not click `Agree & submit application` until the research purpose, title, collaborator decision, IRB/ethics position, storage/deletion plan, publication boundary, and terms obligations have been reviewed outside git by the responsible human team.
