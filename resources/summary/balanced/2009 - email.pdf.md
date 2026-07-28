# Balanced Summary: Enterprise E-mail Functional Requirements Specification

## Goals and Scope
The project aims to establish a statewide e-mail, messaging, and calendaring service for all executive branch agencies to reduce operational costs and meet statutory requirements. The scope includes delivering a proposed plan by December 31, 2009, analyzing sourcing options, conducting cost-benefit analyses, and creating a migration schedule from July 2010 to June 2013. The plan must address functionality, security, privacy, and the reuse of existing infrastructure.

## Stakeholders and User Stories
*   **AEIT (Agency for Enterprise Information Technology):** Leads the project and coordinates requirements gathering to develop the statewide e-mail system plan.
*   **Executive Branch Agencies:** Are the end-user organizations whose needs the system must meet and who will migrate from their existing systems.
*   **Data Center Administrators:** Manage core system operations, including security, backup, and infrastructure.
*   **Agency Administrators:** Handle user account provisioning, distribution lists, and agency-specific configurations within their organization.
*   **End Users:** State employees who utilize e-mail, calendar, and contact services for daily communication and scheduling.
*   **Legal/Compliance Personnel (e.g., OIG):** Require access to archiving and discovery tools to fulfill legal and public records requests.

**User Stories:**
1.  As an **end user**, I want to send, receive, and organize e-mail with attachments so that I can communicate effectively.
2.  As an **agency administrator**, I want to create and manage distribution lists integrated with directory services so that communication within my agency is efficient.
3.  As a **data center administrator**, I want to implement pre-emptive virus scanning and content filtering so that the e-mail system is secure from threats.
4.  As an **end user**, I want to access my e-mail and calendar remotely via a secure web client or mobile device so that I can work flexibly.
5.  As an **agency administrator**, I want to archive, search, and retrieve e-mails based on policy so that the agency can comply with legal retention requirements.
6.  As a **legal/compliance officer**, I want to review and mark e-mails from discovery search results so that I can respond to litigation or investigations.

## Key Processes
1.  **Requirements Elicitation:** Triggered by project initiation; the workgroup gathers functional needs via surveys and historical data.
2.  **Requirements Categorization:** Triggered by survey completion; requirements are analyzed and classified as Basic or Extended based on agency usage and legal necessity.
3.  **Plan Development:** Triggered by requirements approval; the project team creates the proposed plan, including sourcing and migration analysis.
4.  **Stakeholder Review & Approval:** Triggered by draft plan completion; the plan is submitted to key stakeholders and governing bodies for feedback and sign-off.
5.  **Vendor Engagement (Potential):** Triggered by plan approval; functional requirements may be used in RFIs/RFPs for sourcing solutions.
6.  **System Migration:** Triggered by final solution selection; agencies are migrated from old systems to the new enterprise system according to schedule.
7.  **Decommissioning:** Triggered by successful migration; legacy agency e-mail systems are retired.

## Domain Data Elements
*   **User Account:** (Primary Key: User ID). Fields: Email Address, Display Name, Agency Affiliation, Account Status, Mailbox Quota.
*   **Email Message:** (Primary Key: Message ID). Fields: Sender, Recipient(s), Subject, Body, Sent Timestamp, Attachment References.
*   **Distribution List:** (Primary Key: List ID). Fields: List Name, Owner, Member List (User IDs), Query Criteria (for dynamic lists).
*   **Calendar Entry:** (Primary Key: Entry ID). Fields: Organizer, Attendees, Start Time, End Time, Location, Subject.
*   **Archive Record:** (Primary Key: Archive ID). Fields: Source Message ID, Retention Policy, Archive Date, Storage Location, Legal Hold Status.
*   **System Log:** (Primary Key: Log Entry ID). Fields: Event Timestamp, Event Type (e.g., Backup, Security Scan), Actor (Admin/System), Target, Outcome.

## Non-functional Requirements
1.  The system must ensure confidentiality, privacy, and security in compliance with federal and state regulations.
2.  The system must be designed to reduce the current cost of operation and support for the state.
3.  The archiving solution must support long-term retention separate from the active e-mail system.
4.  Disaster recovery capabilities must allow for business continuity during various severity levels of disruption.
5.  Remote access must be provided over secure (encrypted) connections.
6.  The solution must be technically and financially feasible for statewide implementation.

## Milestones and External Dependencies
1.  Complete functional requirements specification (Completed by workgroup).
2.  Submit proposed plan to Governor and Legislature by December 31, 2009.
3.  Begin agency migration to the new system by July 1, 2010.
4.  Complete full migration and decommission all legacy agency systems by June 30, 2013.
5.  Dependency on agency inventory and financial surveys for cost analysis.

## Risks and Mitigation Strategies
1.  **Risk:** Inability to meet diverse agency functional needs within a single system.
    *   **Mitigation:** Categorize requirements as Basic (mandatory) and Extended (optional/cost-add), and conduct thorough feasibility analysis.
2.  **Risk:** Complex migration disrupting agency operations.
    *   **Mitigation:** Develop a detailed, phased migration schedule over three years and identify reusable existing infrastructure.
3.  **Risk:** Failure to comply with legal and records retention mandates.
    *   **Mitigation:** Prioritize archiving, retention, and discovery features in Basic requirements and validate against regulations.
4.  **Risk:** Cost savings objectives not achieved.
    *   **Mitigation:** Perform detailed cost-benefit analysis comparing sourcing options against current agency spends.
5.  **Risk:** Agency-specific constraints (contracts, application dependencies) hindering transition.
    *   **Mitigation:** Compile agency risks/issues into a FAQ and address them during planning.

## Undecided Issues
1.  Final sourcing model (in-house, externally sourced, or hybrid).
2.  Specific technical and financial feasibility of each functional requirement.
3.  Standardized format for state e-mail addresses.
4.  Exact cost allocation model for agencies.
5.  Selection of specific vendor products or platforms.
6.  Detailed technical architecture for disaster recovery and archiving tiers.