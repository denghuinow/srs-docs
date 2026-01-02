# Software Requirements Specification (SRS)
## Statewide Enterprise Messaging & Collaboration System (SEMCS)

**Document Version:** 1.0  
**Date:** [Date of Draft]  
**Status:** Draft for Review  
**Plan Submission Deadline:** December 31, 2009

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Statewide Enterprise Messaging & Collaboration System (SEMCS). The primary purpose of this document is to provide a detailed description of the system's capabilities, interfaces, and performance characteristics. It serves as a contractual agreement between the state's project stakeholders and the development/implementation team, and will be the foundation for system design, development, testing, and deployment.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Keywords:** The terms "MUST," "MUST NOT," "SHALL," "SHALL NOT," "SHOULD," and "MAY" are used as defined in IETF RFC 2119.
*   **Priority:** (H) High, (M) Medium, (L) Low.

#### 1.3 Project Scope
The SEMCS is a statewide, centralized enterprise service providing email, calendaring, scheduling, and contact management to all executive branch agencies. The system will replace existing disparate agency-level systems, consolidating infrastructure and operations to achieve significant cost reduction. The scope includes:
*   Core messaging and collaboration services for all authorized users.
*   Administrative tools for agency and system management.
*   Security, compliance archiving, and e-discovery functions.
*   Support for remote and mobile access.
*   Integration with existing state directory services (e.g., LDAP/Active Directory).

**Out of Scope:**
*   Replacement of non-executive branch agency systems (e.g., judicial, legislative).
*   Public-facing email services (e.g., citizen contact forms).
*   Real-time instant messaging or chat services.
*   Development of new, unrelated office productivity software.

#### 1.4 References
*   State IT Security Policy Framework
*   Relevant Federal Regulations (e.g., FOIA, State-specific records retention laws)
*   Project Charter: Statewide Email Consolidation Initiative

### 2. Overall Description

#### 2.1 Product Perspective
The SEMCS is a new, self-contained system that will replace legacy email systems. It must interface with several existing state enterprise systems:
*   **Identity & Access Management (IAM) System:** For user authentication and provisioning.
*   **State Network Infrastructure:** For connectivity to all agency offices and remote users.
*   **Backup and Disaster Recovery Systems:** For system resilience.

#### 2.2 Product Functions
The high-level functions of the SEMCS are:
1.  **Electronic Messaging:** Send, receive, store, and manage email with file attachments.
2.  **Collaboration & Scheduling:** Manage personal and shared calendars, schedule meetings, and manage contacts.
3.  **Compliance & Governance:** Automatically archive all messages, enforce retention policies, and facilitate legal e-discovery.
4.  **Security & Protection:** Provide antivirus scanning, anti-spam filtering, and data loss prevention.
5.  **Accessibility:** Provide secure access via standard clients, web browsers, and mobile devices.
6.  **Administration:** Enable user/group management, resource provisioning, and system monitoring by different administrative roles.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **End-User** | 50,000+ employees across all executive agencies. Varying technical skill. | Reliable, intuitive email/calendar; access from office, home, and mobile devices. |
| **Agency Administrator** | 100-200 IT staff delegated by each agency. Technical proficiency. | Manage user accounts, distribution lists, and resource mailboxes for their agency; generate basic usage reports. |
| **Data Center/System Administrator** | 10-20 central state IT staff. High technical expertise. | Install, configure, monitor, and maintain the entire system; set global policies; manage security and compliance features. |
| **Legal/Compliance Officer** | Small team. Knowledge of records laws. | Perform targeted searches on archived mail for e-discovery and audits. |

#### 2.4 Operating Environment
*   **Physical:** Hosted in primary and secondary state data centers.
*   **Software:** Must support access via:
    *   Web browsers (IE, Firefox, Chrome - current versions).
    *   Mobile OS (iOS, Android, Windows Mobile).
    *   Desktop clients (Outlook, IMAP-compatible clients).
*   **Networks:** Must operate over the state's private WAN and be accessible via secure remote access (VPN) for external users.

#### 2.5 Design and Implementation Constraints
1.  **Schedule Constraint:** A complete system implementation plan MUST be submitted by **December 31, 2009**.
2.  **Cost Constraint:** The selected solution and operational model MUST demonstrate a reduction in total cost of ownership compared to the aggregate cost of existing agency systems.
3.  **Regulatory Constraint:** The system MUST comply with all applicable state and federal regulations regarding data confidentiality (e.g., PII), privacy, and security (e.g., FISMA, NIST standards).
4.  **Integration Constraint:** The system MUST integrate with the state's existing centralized IAM/LDAP service for user authentication.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** Adequate bandwidth exists between agency offices and the central data centers.
*   **Assumption:** Agencies will agree to migrate from their legacy systems according to the state's migration schedule.
*   **Dependency:** The project is dependent on the continued operation and support of the state's central IAM service.

### 3. System Features and Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Email Management
*   `FR-101 (H)`: The system SHALL allow users to send and receive email messages with one or more file attachments.
*   `FR-102 (H)`: The system SHALL provide a folder-based interface for organizing emails (Inbox, Sent, Drafts, Custom Folders).
*   `FR-103 (M)`: The system SHALL support distribution lists managed by Agency Administrators.

##### 3.1.2 Calendaring & Scheduling
*   `FR-201 (H)`: The system SHALL allow users to create, view, edit, and delete calendar appointments and events.
*   `FR-202 (H)`: The system SHALL allow users to schedule meetings by checking the availability of other users and resources (e.g., conference rooms).
*   `FR-203 (M)`: The system SHALL support sharing calendars with other users with configurable permission levels (view-only, edit).

##### 3.1.3 Compliance Archiving & e-Discovery
*   `FR-301 (H)`: The system SHALL automatically archive a copy of all inbound, outbound, and internal email messages in a secure, immutable repository.
*   `FR-302 (H)`: The system SHALL enforce configurable retention policies based on message metadata (e.g., sender, date, keywords).
*   `FR-303 (H)`: The system SHALL provide a search interface for authorized Legal/Compliance Officers to perform granular e-discovery searches across the archive without end-user knowledge.

##### 3.1.4 Security & Content Filtering
*   `FR-401 (H)`: The system SHALL scan all inbound and outbound email attachments for viruses and malware.
*   `FR-402 (H)`: The system SHALL provide configurable content filtering to block spam and emails based on policy rules (e.g., keywords, file types).
*   `FR-403 (M)`: The system SHALL provide optional encryption for sensitive outbound emails.

##### 3.1.5 Remote & Mobile Access
*   `FR-501 (H)`: The system SHALL provide a fully functional web client accessible from standard browsers over HTTPS.
*   `FR-502 (H)`: The system SHALL support synchronization of email, calendar, and contacts with mobile devices using ActiveSync or similar standard protocol.
*   `FR-503 (M)`: Mobile access SHALL enforce device-level security policies (e.g., PIN lock, remote wipe capability).

##### 3.1.6 Administration
*   `FR-601 (H)`: The system SHALL provide a role-based administration model, delegating specific privileges to Agency Administrators and System Administrators.
*   `FR-602 (H)`: Agency Administrators SHALL be able to create, disable, and delete user accounts and manage distribution lists within their agency's organizational unit.
*   `FR-603 (H)`: System Administrators SHALL have a dashboard to monitor system health, performance, and storage utilization.

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance Requirements
*   `NFR-101`: System availability SHALL be 99.9% (excluding scheduled maintenance) during business hours (7 AM - 7 PM, Mon-Fri).
*   `NFR-102`: Email delivery latency (internal-to-internal) SHALL be less than 30 seconds, 95% of the time under normal load.
*   `NFR-103`: The web client interface SHALL render and be usable within 3 seconds for 95% of page loads.

##### 3.2.2 Security Requirements
*   `NFR-201`: All user authentication SHALL integrate with the state's central IAM system (e.g., via LDAP or SAML).
*   `NFR-202`: All data in transit SHALL be encrypted using TLS 1.2 or higher.
*   `NFR-203`: The system SHALL maintain audit logs for all administrative actions and access to compliance archives. Logs SHALL be tamper-evident.
*   `NFR-204`: The system SHALL be designed and operated in compliance with NIST SP 800-53 security controls as specified by the state CISO.

##### 3.2.3 Usability Requirements
*   `NFR-301`: The web client interface SHALL be consistent with common webmail paradigms (e.g., Gmail, Outlook Web App) to minimize training needs.
*   `NFR-302`: The system SHALL provide context-sensitive help and user documentation.

##### 3.2.4 Compliance & Regulatory Requirements
*   `NFR-401`: The archiving solution SHALL meet the state's defined records retention schedules for electronic communications.
*   `NFR-402`: The system SHALL support legal holds, preventing the deletion of relevant messages during litigation.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   A primary web-based interface accessible via HTTPS.
*   Support for desktop mail client interfaces (MAPI/IMAP/SMTP).
*   Mobile-optimized web view or dedicated mobile app experience.
*   Separate, secure administrative web portals for Agency and System Administrators.

#### 4.2 Hardware Interfaces
*   The system software shall run on standard commercial off-the-shelf (COTS) server hardware in the state data center.

#### 4.3 Software Interfaces
*   **IAM Interface:** LDAP v3 or SAML 2.0 for authentication and group membership.
*   **Logging Interface:** Syslog or API for forwarding audit logs to the state's Security Information and Event Management (SIEM) system.

#### 4.4 Communications Interfaces
*   **Email:** SMTP, IMAP4, POP3 (optional).
*   **Calendaring:** iCal, CalDAV.
*   **Mobile:** Exchange ActiveSync, CalDAV/CardDAV.

### 5. Other Non-Functional Requirements

#### 5.1 Scalability
The system architecture SHALL be scalable to support a 20% increase in user count and a 30% annual increase in data storage without major architectural changes.

#### 5.2 Reliability
The system SHALL implement redundancy at all critical layers (servers, storage, network) to avoid single points of failure. A full disaster recovery plan with an RTO (Recovery Time Objective) of < 8 hours and an RPO (Recovery Point Objective) of < 1 hour is required.

#### 5.3 Portability & Cloud Consideration
The solution SHOULD be evaluated for potential deployment in a state-approved cloud (IaaS/PaaS) or hybrid model, provided it meets all security (`NFR-201` to `NFR-204`) and compliance (`NFR-401`, `NFR-402`) requirements.

---
**Approvals**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| State Chief Information Officer (CIO) | | | |
| Lead System Architect | | | |