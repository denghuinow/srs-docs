# Detailed Summary: Enterprise E-mail Functional Requirements Specification

## Background and Scope
This project aims to establish a statewide enterprise email, messaging, and calendaring service for all executive branch agencies in Florida, as mandated by Florida Statute 282.34. The primary goal is to reduce operational costs while meeting agency needs. The immediate deliverable is a proposed plan, due by December 31, 2009, which must include sourcing options, cost-benefit analyses, and a migration schedule. Non-goals include implementing collaboration services like shared documents, instant messaging, and discussion forums, which are explicitly out of scope.

## Stakeholders Matrix and Use Cases
*   **AEIT (Agency for Enterprise Information Technology):** Leads the project and is responsible for submitting the final plan to government leadership.
*   **Executive Branch Agencies:** The end-user organizations whose needs the system must meet and who will migrate from their existing systems.
*   **End Users:** Individual state employees who will use the email, calendar, and contact services daily.
*   **Agency Administrators:** IT staff within each agency responsible for provisioning accounts, managing distribution lists, and handling archiving/discovery tasks.
*   **Data Center/SSRC Administrators:** Personnel responsible for system-wide operations, including security, backup/restore, and infrastructure management.
*   **Legal/Compliance Personnel (e.g., OIG):** Users who require the ability to review, mark, and manage emails for legal discovery and compliance.
*   **Project Workgroup Team:** Compiled the functional requirements specification through surveys and analysis.
*   **Vendors/Service Providers:** Potential bidders who will respond to RFIs/RFPs based on these requirements.

**Main Scenarios:** 1) User sends and receives email with attachments. 2) User manages calendar and schedules resources. 3) Agency admin provisions a new user account. 4) Agency admin performs a legal discovery search on the email archive. 5) Data center admin performs a mailbox-level restore from backup. 6) System filters inbound email for viruses and spam. 7) User accesses email remotely via a secure web client or mobile device. 8) User archives old emails to comply with retention policies.
**Exception Scenarios:** 1) Recovery from a full data center disaster. 2) Handling a large-scale, complex legal e-discovery request.

## Business Process
**Main Process: User Email Management**
1.  **Trigger:** User needs to communicate or check for messages.
2.  User logs into the email client (desktop, web, or mobile).
3.  User composes, reads, replies to, or forwards messages (with formatting and spell check).
4.  User organizes messages into personal folders or applies rules (e.g., auto-reply).
5.  User manages calendar entries, tasks, and contact lists.
6.  User may search their mailbox or archive based on various criteria.
7.  User may flag emails for deletion per retention policy or flag to exclude from archiving.
8.  **Output:** Sent/received messages, updated calendar, organized contacts.

**Key Branch A: Account Provisioning & Administration (Trigger: New hire or role change)**
1.  Agency admin creates a new email account, integrating with directory services.
2.  Admin assigns the account to distribution lists and applies standard conventions.
3.  Admin may create or manage shared resources like public folders or generic addresses.
4.  **Output:** A fully provisioned and configured user mailbox.

**Key Branch B: Legal E-Discovery & Archiving (Trigger: Legal/compliance request)**
1.  Agency admin captures and archives all relevant sent/received emails based on policy.
2.  Admin performs a complex search (Boolean, full-text) on the archive using criteria like sender, date, content.
3.  Admin places responsive results on legal hold to suspend deletion.
4.  Legal personnel review, mark, and certify the results for production.
5.  **Output:** A certified, redacted set of emails fulfilling the legal production request.

## Domain Model
*   **User Account:** (Fields: UserID [unique], DisplayName, EmailAddress [unique/required], Department, AccountStatus [required])
*   **Email Message:** (Fields: MessageID [unique], Sender [reference User], Recipients [list], Subject, Body, SentDateTime [required], Attachments [list])
*   **Mailbox:** (Fields: MailboxID [unique], Owner [reference User/required], StorageQuota, FolderList [list])
*   **Distribution List:** (Fields: ListID [unique], ListName [required], Members [list of User references], QueryCriteria)
*   **Calendar Entry:** (Fields: EntryID [unique], Organizer [reference User/required], StartTime [required], EndTime, Location, Attendees [list])
*   **Archive Record:** (Fields: RecordID [unique], SourceMessage [reference Email], ArchivedDate [required], RetentionPolicy [required], LegalHoldFlag)
*   **Discovery Case:** (Fields: CaseID [unique], CaseName [required], Custodian [reference User], SearchCriteria, Status)
*   **System Log:** (Fields: LogID [unique], EventType [required], Timestamp [required], User/Actor, Details)

## Interfaces and Integrations
*   **LDAP/Active Directory (Inbound):** For user authentication, account provisioning, and populating distribution lists. Input: User credentials, group membership. Output: Authenticated session, synchronized user attributes. SLA: High availability for authentication.
*   **SMTP Gateways (Inbound/Outbound):** For sending and receiving external email. Input: Inbound messages from the internet. Output: Filtered messages to internal servers or outbound to recipients. SLA: 99.9% uptime, <5-minute message delay.
*   **Mobile Device Services (Outbound):** For syncing email, calendar, contacts to BlackBerry and other mobile devices (ActiveSync). Input: Device registration requests. Output: Synchronized mailbox data. SLA: Support for major device protocols.
*   **Archiving/Compliance System (Bidirectional):** For capturing messages and enabling discovery. Input: Messages to archive from live system. Output: Search results and records for legal hold. SLA: Must meet state and federal retention requirements.
*   **Backup System (Outbound):** For regular data protection. Input: Mailbox and system data. Output: Backup sets for restore. SLA: Defined Recovery Time and Point Objectives (RTO/RPO).
*   **Agency Applications (Inbound):** For workflow applications to send/receive email via an SMTP bridgehead. Input: Application-generated messages. Output: Messages delivered to the mail system. SLA: Reliable, low-latency connection.
*   **Web Client (Outbound):** For user access via browser. Input: User HTTP/HTTPS requests. Output: Rendered mailbox interface. SLA: Secure (encrypted) connection, responsive UI.
*   **Anti-Virus/Content Filtering Service (Inbound):** For scanning messages pre-delivery. Input: Raw incoming messages. Output: Cleaned or quarantined messages. SLA: Real-time scanning with minimal latency.

## Acceptance Criteria
**Capability: Core Email Functionality**
*   Given a user has a valid account, when they compose and send an email with an attachment, then the recipient receives the message with the attachment intact.
*   Given a user sets an "Out of Office" rule, when an email is sent to them, then the sender automatically receives the configured reply.

**Capability: Administrative Account Management**
*   Given an agency admin has appropriate permissions, when they request to create a new user account integrated with LDAP, then the account is provisioned and appears in the global address list within one business day.
*   Given an admin creates a query-based distribution list, when a user's LDAP attributes change to meet the criteria, then the user is automatically added to the distribution list.

**Capability: Legal Discovery**
*   Given a legal hold is placed on a set of emails for a specific case, when the system's standard retention policy would delete them, then those emails are preserved until the hold is released.
*   Given an agency admin performs a full-text search of the archive for a specific keyword, then the system returns all emails containing that keyword in the body or attachments.

## Non-functional Metrics
*   **Performance:** System must support concurrent access for all state executive branch users with sub-second response time for core operations (send, open). Archive search operations for large datasets must complete within defined, agency-agreed timeframes.
*   **Reliability/Availability:** The core email and calendaring service must have 99.9% uptime. Backup systems must enable restoration of an individual mailbox within 4 hours.
*   **Security/Compliance:** The system must encrypt data in transit and at rest, and comply with confidentiality, privacy, and security requirements of Florida statutes and federal regulations (e.g., HIPAA, SOX where applicable). All access must be audited.
*   **Observability:** Comprehensive logging of administrative actions (provisioning, archiving, discovery searches) and system events (failures, performance degradation) must be available for monitoring and troubleshooting.

## Milestones and Release Strategy
1.  Finalize and approve Functional Requirements Specification (Completed with v1.5).
2.  Complete agency inventory and financial analysis surveys (Technical team ongoing).
3.  Develop and issue Request for Information (RFI) to potential vendors.
4.  Evaluate sourcing options (in-house, external, hybrid) and complete cost-benefit analysis.
5.  Submit the final proposed plan to the Governor, Senate President, and House Speaker by Dec 31, 2009.
6.  Execute migration plan: Begin agency migrations by July 1, 2010, and complete by June 30, 2013.

## Risk List and Mitigation Strategies
1.  **Risk:** Vendor lock-in or inability to meet all functional requirements cost-effectively.
    *   **Mitigation:** Conduct thorough RFI/RFP process, evaluate multiple sourcing models, and prioritize "basic" requirements.
2.  **Risk:** Agency resistance to change or inability to migrate due to application dependencies.
    *   **Mitigation:** Engage agencies early, compile a FAQ of constraints, and develop a phased, supported migration schedule over three years.
3.  **Risk:** Inability to meet complex legal archiving and discovery requirements.
    *   **Mitigation:** Include legal/compliance personnel in requirements validation and select/design a solution with robust, proven archiving features.
4.  **Risk:** Budget overruns during implementation or ongoing operation.
    *   **Mitigation:** Perform detailed cost-benefit analysis, include all recurring and non-recurring costs, and compare against current agency spend.
5.  **Risk:** Security breaches or failure to meet state/federal security standards.
    *   **Mitigation:** Make security a primary evaluation criterion, require encryption, and design with defense-in-depth principles.
6.  **Risk:** Inadequate performance or scalability for the entire state user base.
    *   **Mitigation:** Define clear performance metrics in SLAs and conduct load testing during the proof-of-concept phase.
7.  **Risk:** Data loss during migration from legacy systems.
    *   **Mitigation:** Develop detailed migration tools and procedures, conduct pilot migrations, and ensure comprehensive backup before migration.
8.  **Risk:** Project delays missing the legislative deadline for the plan (Dec 31, 2009).
    *   **Mitigation:** Adhere to the strict 6-week timeline for requirements gathering and maintain strong project management oversight.

## Undecided Issues and Responsible Parties
1.  Final selection of sourcing model (in-house, outsourced, hybrid). **Responsible: AEIT/Project Lead.**
2.  Specific technical and financial feasibility of each "basic" and "extended" requirement. **Responsible: Technical and Financial Workgroups.**
3.  Exact cost allocation model for agencies. **Responsible: AEIT/Financial Workgroup.**
4.  Detailed technical architecture and specific software/hardware solutions. **Responsible: To be determined post-RFI/RFP.**
5.  Prioritization and potential phasing of "extended" requirements. **Responsible: AEIT in consultation with agencies.**
6.  Standardized format for state email addresses. **Responsible: AEIT/Project Lead (per plan requirement).**
7.  Definitive list of existing email infrastructure to be reused. **Responsible: Technical Workgroup (via inventory survey).**
8.  Specific disaster recovery (DR) and backup RTO/RPO service levels. **Responsible: AEIT/Technical Workgroup in consultation with agencies.**