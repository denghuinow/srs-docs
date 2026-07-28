# Software Requirements Specification (SRS)
## Statewide Enterprise Email, Messaging, and Calendaring Service

**Document Version:** 1.0  
**Date:** [Date of SRS Creation]  
**Prepared for:** Agency for Enterprise Information Technology (AEIT)  
**Prepared by:** [Name of Workgroup/Author]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the proposed statewide Enterprise Email, Messaging, and Calendaring Service. It serves as the foundation for the development of the project plan, sourcing analysis, and eventual system implementation. The primary audience includes project stakeholders, technical planners, solution architects, and potential vendors.

#### 1.2 Project Scope
The scope of this project encompasses the planning, analysis, and eventual deployment of a unified, secure, and cost-effective electronic communication and collaboration service for all executive branch agencies. This SRS details the requirements that the final solution must satisfy.

**In-Scope:**
*   Definition of core and extended functional capabilities for email, calendaring, and contacts.
*   Specification of security, privacy, archiving, and compliance requirements.
*   Analysis of sourcing options (in-house, cloud, hybrid) and associated cost-benefit.
*   Development of a high-level migration and decommissioning schedule (July 2010 - June 2013).
*   Consideration for reusing existing state IT infrastructure where feasible.

**Out-of-Scope:**
*   Implementation of the final technical solution (this is a planning document).
*   Management of non-executive branch agencies (e.g., legislative, judicial).
*   Real-time messaging/chat services beyond standard email.
*   Detailed low-level system design or vendor product selection.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **AEIT:** Agency for Enterprise Information Technology
*   **OIG:** Office of Inspector General
*   **RFP:** Request for Proposal
*   **RFI:** Request for Information
*   **SLA:** Service Level Agreement
*   **DR:** Disaster Recovery
*   **Basic Requirements:** Mandatory features necessary for legal compliance and fundamental operation.
*   **Extended Requirements:** Desirable features that enhance functionality but are not legally mandatory; may involve additional cost.

#### 1.4 References
*   State statutes governing public records, data privacy, and IT consolidation.
*   Agency survey results and historical system inventories.
*   Federal regulations (e.g., pertaining to data security and retention).

#### 1.5 Document Overview
This document is structured to present a complete view of the system requirements. Following this introduction, it details overall description, specific requirements categorized by feature, and supporting information regarding constraints, assumptions, and appendices.

### 2. Overall Description

#### 2.1 Product Perspective
This system will be a new, statewide enterprise service intended to replace disparate, agency-specific email and calendaring systems. It must integrate with existing state directory services (e.g., LDAP/Active Directory) for authentication and user management. The system will interact with external mail servers for internet email exchange and must provide secure remote access channels.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **End User** (~50,000+ state employees) | Varying technical proficiency. Primary need is reliable daily communication. | Send/receive email with attachments, manage calendar, access from office/remotely. |
| **Agency Administrator** (Per Agency IT) | Technically proficient in user/group management. Understands agency structure. | Provision users, manage distribution lists, apply agency-specific policies, run basic reports. |
| **Data Center Administrator** (Central AEIT/Operations) | Highly skilled in system infrastructure, security, and high-availability operations. | Ensure system availability, perform backups, manage security (virus/SPAM), monitor performance. |
| **Legal/Compliance Officer** (e.g., OIG, Agency Counsel) | Knowledgeable in records retention laws and e-discovery procedures. | Perform legal holds, search archives comprehensively, export records for investigations. |
| **AEIT Project/Plan Management** | Manages the planning, sourcing, and migration process. | Requirements traceability, cost-benefit analysis, vendor evaluation criteria. |

#### 2.3 Operating Environment
*   **Network:** Must operate over the state's wide area network (WAN) with secure remote access via the internet.
*   **Client Access:** Must support standard email clients (e.g., Outlook, Thunderbird) via protocols (SMTP, IMAP/POP3, CalDAV), a secure web client, and synchronize with mobile devices.
*   **Server Environment:** To be determined based on sourcing analysis (state data center, cloud provider, or hybrid).
*   **Directory Services:** Must integrate with the state's enterprise directory for user identity and authentication.

#### 2.4 Design and Implementation Constraints
1.  **Regulatory:** Must comply with [List relevant state and federal statutes for records retention, privacy (e.g., PII), and accessibility].
2.  **Financial:** The total cost of ownership (TCO) must demonstrate a reduction compared to the aggregate current agency costs.
3.  **Temporal:** The migration plan must be completed by June 30, 2013, as per the project mandate.
4.  **Technical:** Must support the reuse of qualified existing state infrastructure to minimize capital expenditure.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** Executive branch agencies will participate in the requirements gathering and migration process.
*   **Assumption:** Adequate funding will be approved based on the proposed plan.
*   **Dependency:** Accurate and complete inventory and financial data from all agencies is required for a valid cost-benefit analysis.
*   **Dependency:** The state's network infrastructure can support the consolidated system's bandwidth and latency requirements.

### 3. System Features and Requirements

Requirements are categorized as **Basic (B)** or **Extended (E)**.

#### 3.1 Email Core Functionality
*   **FR-1.1 (B):** The system shall allow users to send and receive email messages to internal and external recipients.
*   **FR-1.2 (B):** The system shall support sending and receiving email attachments of common file types.
*   **FR-1.3 (B):** The system shall provide users with the ability to organize messages into folders, flag messages, and mark messages as read/unread.
*   **FR-1.4 (E):** The system may provide advanced email management features such as rules/filters, out-of-office auto-replies, and search within mailbox.

#### 3.2 Calendaring and Scheduling
*   **FR-2.1 (B):** The system shall allow users to create, view, edit, and delete calendar appointments and events.
*   **FR-2.2 (B):** The system shall support inviting attendees to meetings and managing attendee responses (Accept, Tentative, Decline).
*   **FR-2.3 (B):** The system shall provide free/busy lookup for internal users to facilitate scheduling.
*   **FR-2.4 (E):** The system may support resource scheduling (e.g., conference rooms, vehicles) and shared calendars.

#### 3.3 Directory and User Management
*   **FR-3.1 (B):** The system shall synchronize with the central state directory service for user authentication and core identity information (name, email address).
*   **FR-3.2 (B):** The system shall allow Agency Administrators to create, modify, enable, and disable user mailboxes and calendars within their agency.
*   **FR-3.3 (B):** The system shall allow Agency Administrators to create and manage static and dynamic distribution lists.
*   **FR-3.4 (E):** The system may provide a global address list (GAL) that is searchable by all users across all executive branch agencies.

#### 3.4 Security and Protection
*   **FR-4.1 (B):** The system shall scan all inbound and outbound email for viruses and malware pre-emptively.
*   **FR-4.2 (B):** The system shall filter unsolicited commercial email (SPAM) based on configurable policies.
*   **FR-4.3 (B):** All remote access (web client, mobile sync) shall require secure, encrypted connections (TLS/SSL).
*   **FR-4.4 (B):** The system shall enforce password policies and account lockout thresholds defined by the state.
*   **FR-4.5 (E):** The system may support content filtering based on data loss prevention (DLP) policies for sensitive information.

#### 3.5 Archiving, Retention, and e-Discovery
*   **FR-5.1 (B):** The system shall provide a mechanism to archive all sent and received email messages based on configurable retention policies (e.g., 7 years).
*   **FR-5.2 (B):** The archive shall be stored separately from the active email system for integrity and long-term preservation.
*   **FR-5.3 (B):** Authorized Legal/Compliance personnel shall be able to perform advanced, cross-mailbox searches on the archived data based on criteria (sender, recipient, date, keywords).
*   **FR-5.4 (B):** The system shall allow Legal/Compliance personnel to place mailboxes or specific messages on "legal hold," preventing their deletion from the archive.
*   **FR-5.5 (B):** Search results from the archive shall be exportable in a standard, forensically sound format.

#### 3.6 Administration and Monitoring
*   **FR-6.1 (B):** The system shall provide Data Center Administrators with tools to monitor system health, performance, and capacity.
*   **FR-6.2 (B):** The system shall generate audit logs for administrative actions (user provisioning, policy changes) and security events.
*   **FR-6.3 (B):** The system shall support regular, automated backups of system data and configuration.

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
*   **NR-1:** System availability shall be 99.9% or higher during standard business hours, excluding scheduled maintenance.
*   **NR-2:** Email delivery latency (internal to internal) shall be less than 30 seconds, 95% of the time.
*   **NR-3:** The web client shall render and be usable within 5 seconds under standard load.

#### 4.2 Safety and Security Requirements
*   **NR-4:** The system shall comply with all applicable state IT security standards and federal regulations (e.g., for data protection).
*   **NR-5:** All data in transit shall be encrypted. Data at rest in the archive shall be encrypted.
*   **NR-6:** Access to administrative functions and archived data shall be strictly controlled based on the principle of least privilege and logged for audit.

#### 4.3 Software Quality Attributes
*   **NR-7 (Reliability):** The system shall include disaster recovery capabilities to meet defined Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) for various disruption levels.
*   **NR-8 (Scalability):** The system shall be designed to support a 20% increase in user count without major architectural changes.
*   **NR-9 (Maintainability):** The system shall allow for patches and updates to be applied with minimal service disruption.
*   **NR-10 (Usability):** The web client interface shall be intuitive and require minimal training for standard End Users familiar with email.

### 5. Data Model
The following core entities and their key attributes define the system's domain data.

```yaml
UserAccount:
  primary_key: UserID
  attributes:
    - EmailAddress
    - DisplayName
    - AgencyAffiliation
    - AccountStatus (Active, Suspended, Terminated)
    - MailboxQuota

EmailMessage:
  primary_key: MessageID
  attributes:
    - Sender (FK: UserAccount)
    - Recipients (List of FK: UserAccount or external addresses)
    - Subject
    - Body
    - SentTimestamp
    - Attachments (List of file references)

DistributionList:
  primary_key: ListID
  attributes:
    - ListName
    - Owner (FK: UserAccount)
    - Members (List of FK: UserAccount)
    - QueryCriteria (for dynamic lists)

CalendarEntry:
  primary_key: EntryID
  attributes:
    - Organizer (FK: UserAccount)
    - Attendees (List of FK: UserAccount)
    - StartTime
    - EndTime
    - Location
    - Subject

ArchiveRecord:
  primary_key: ArchiveID
  attributes:
    - SourceMessageID (FK: EmailMessage)
    - RetentionPolicy
    - ArchiveDate
    - StorageLocation
    - LegalHoldStatus (Active, Released)

SystemLog:
  primary_key: LogEntryID
  attributes:
    - EventTimestamp
    - EventType (e.g., "UserLogin", "AdminPolicyChange", "BackupCompleted")
    - Actor (UserID or "System")
    - Target
    - Outcome (Success, Failure)
```

### 6. Other Requirements

#### 6.1 Migration Requirements
*   The solution must include tools and processes to migrate user mailboxes, calendars, and contacts from legacy agency systems with minimal data loss.
*   The migration must allow for a phased approach by agency or user group.

#### 6.2 Compliance and Legal
*   The system and its operational procedures must satisfy the state's public records act requirements for retention, accessibility, and disclosure.

### 7. Appendices

#### Appendix A: User Stories to Requirements Traceability
| User Story | Related Functional Requirements (FR) |
| :--- | :--- |
| As an **end user**, I want to send, receive, and organize e-mail... | FR-1.1, FR-1.2, FR-1.3 |
| As an **agency administrator**, I want to create and manage distribution lists... | FR-3.3 |
| As a **data center administrator**, I want to implement pre-emptive virus scanning... | FR-4.1 |
| As an **end user**, I want to access my e-mail and calendar remotely... | FR-4.3 |
| As an **agency administrator**, I want to archive, search, and retrieve e-mails... | FR-5.1, FR-5.2 |
| As a **legal/compliance officer**, I want to review and mark e-mails... | FR-5.3, FR-5.4, FR-5.5 |

#### Appendix B: Open Issues and Decisions Pending
1.  **Sourcing Model:** Final decision on in-house, cloud, or hybrid hosting.
2.  **Technical Feasibility:** Detailed assessment of each Extended (E) requirement's technical complexity and cost impact.
3.  **Email Address Standard:** Format for state email addresses (e.g., `first.last@state.xx.gov`).
4.  **Cost Allocation:** Model for charging back costs to individual agencies.
5.  **Product/Platform Selection:** Specific vendor or software solution to be chosen via subsequent RFP process.
6.  **DR/Archive Architecture:** Detailed technical design for disaster recovery tiers and archive storage infrastructure.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| AEIT Project Lead | | | |
| Workgroup Chair | | | |
| Stakeholder Representative | | | |