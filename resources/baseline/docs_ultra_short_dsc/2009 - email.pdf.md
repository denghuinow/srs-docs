# Software Requirements Specification (SRS)
## Statewide Enterprise Email, Messaging, and Calendaring Service

**Document Version:** 1.0  
**Date:** [Date of Generation]  
**Status:** Draft for Plan Development  
**Project Code:** SEE-CS-2009

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for a proposed statewide enterprise email, messaging, and calendaring service. The primary purpose of this document is to serve as the foundation for a comprehensive sourcing plan that will analyze in-house, external, and hybrid delivery options. It is intended for use by project stakeholders, solution architects, procurement officers, and vendor partners.

#### 1.2 Document Conventions
*   **Priority:** Requirements are categorized as **Basic** (mandatory minimal solution) or **Extended** (optional capabilities).
*   **Formatting:** Functional requirements are uniquely identified (e.g., `FR-EMAIL-001`). Non-functional requirements are identified as `NFR-xxx`.
*   **References:** All external regulations and laws are cited for traceability.

#### 1.3 Project Scope
The system shall be a centralized enterprise service providing email, messaging, and calendaring functionality to all executive branch agencies within the state. The core objectives are to reduce operational costs and consolidate disparate agency systems.

**In-Scope:**
*   Email, calendaring, and contact management.
*   Centralized administration, security, and archiving.
*   Integration with existing agency directories and applications.
*   Remote and mobile access.
*   Development of a sourcing plan (the immediate project deliverable).

**Out-of-Scope:**
*   Collaboration services such as shared document repositories, instant messaging, or discussion forums.
*   The actual implementation, deployment, or migration activities (these are subjects of the future plan).
*   Services for legislative or judicial branch agencies (unless later expanded).

#### 1.4 References
*   Sarbanes-Oxley Act (SOX)
*   Health Insurance Portability and Accountability Act (HIPAA)
*   Florida Public Records Law (Chapter 119, F.S.) *[Note: Replace with applicable state law]*
*   State IT Security Standards and Policies

### 2. Overall Description

#### 2.1 Product Perspective
This system is a mandated, statewide enterprise service intended to replace existing heterogeneous email systems. It will operate as a centralized service, likely interfacing with multiple legacy agency directory services (e.g., LDAP) and applications. The system exists within a broader state IT ecosystem and must exchange email with the public internet.

#### 2.2 Product Functions (Summary)
The core functions of the proposed system include:
1.  **Email Management:** Sending, receiving, storing, and organizing email with attachments.
2.  **Calendaring & Contacts:** Managing personal/group calendars, contacts, and distribution lists.
3.  **Archiving & Compliance:** Providing server-based archiving, retention policy enforcement, and legal discovery tools.
4.  **Security & Protection:** Implementing anti-virus, anti-spam, content filtering, and data security controls.
5.  **Accessibility:** Enabling access via web clients and mobile devices (e.g., BlackBerry, other smartphones).
6.  **Data Management:** Performing backup and restore operations at granular and system levels.
7.  **Administration:** Providing tools for agency and system-level administrators to manage users, resources, and configurations.
8.  **Integration:** Supporting standard protocols for integration with other agency software.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Agency Employee (End-User)** | ~50,000+ users statewide. Varying levels of technical skill. Primary role is communication and scheduling. | Reliable send/receive of email with attachments. Intuitive calendar and contact management. Secure remote access from multiple devices. |
| **Agency Administrator** | IT staff within each agency. Manages user population for their agency. | Provision/de-provision user accounts. Manage agency-specific distribution lists. Perform searches for internal legal/compliance needs. Apply agency-specific policies. |
| **System Administrator (Data Center/SSRC)** | Central IT operations staff. Manages the entire enterprise service. | System-wide monitoring, security, and patch management. Configuration of global routing, filtering, and retention policies. Execution of disaster recovery procedures. Management of server-level backups. |

#### 2.4 Operating Environment
*   **Logical Environment:** Must operate within the state's secure network perimeter and potentially a private cloud or state data center.
*   **Client Access:** Must support modern web browsers, BlackBerry Enterprise Server (BES) or equivalent, and ActiveSync/EWS for other mobile devices.
*   **Server Environment:** To be determined by the sourcing analysis (e.g., Windows Server/Linux, VMware/Hyper-V, specific mail platform software).

#### 2.5 Design and Implementation Constraints
1.  **Plan Deadline:** The final sourcing and implementation plan must be submitted by **December 31, 2009**.
2.  **Migration Deadline:** The plan must schedule a complete migration of all agencies by **June 30, 2013**.
3.  **Directory Integration:** The solution must reuse or integrate with existing agency LDAP-like directory services for identity management.
4.  **Application Integration:** Must maintain support for existing integrations with agency line-of-business applications.
5.  **Feasibility:** All stated requirements are subject to technical and financial feasibility analysis within the sourcing plan.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** Agencies will provide necessary contact and requirements information during the planning phase.
*   **Assumption:** Sufficient budget and political support will exist to execute the chosen plan.
*   **Dependency:** The sourcing plan is dependent on accurate inventory and assessment of current agency systems and directory schemas.
*   **Dependency:** The final solution's architecture depends on the selected sourcing model (in-house, cloud, hybrid).

### 3. System Features and Requirements

#### 3.1 Email Management
**Priority: Basic**
*   `FR-EMAIL-001`: The system shall allow users to send and receive email messages to/from internal and external (internet) addresses.
*   `FR-EMAIL-002`: The system shall support sending and receiving email attachments up to a configurable size limit (e.g., 25MB).
*   `FR-EMAIL-003`: The system shall provide folder-based organization of email (Inbox, Sent, Drafts, Deleted, Custom).
*   `FR-EMAIL-004`: The system shall provide robust search capabilities across the user's mailbox based on sender, recipient, subject, date, and content.

#### 3.2 Calendaring and Contact Management
**Priority: Basic**
*   `FR-CAL-001`: The system shall allow users to create, view, edit, and delete calendar appointments and meetings.
*   `FR-CAL-002`: The system shall support sending and receiving meeting invitations, with support for acceptance, tentative, and decline responses.
*   `FR-CAL-003`: The system shall allow users to manage a personal address book (contacts).
*   `FR-CAL-004`: The system shall support the creation and management of distribution lists.

#### 3.3 Archiving, Retention, and eDiscovery
**Priority: Basic**
*   `FR-ARCH-001`: The system shall provide a server-based archiving system to capture all sent and received email.
*   `FR-ARCH-002`: The system shall allow administrators to define and apply retention policies based on content, sender/recipient, or other metadata.
*   `FR-ARCH-003`: The system shall provide a legal discovery "hold" function to preserve email for specific users or keywords, preventing deletion.
*   `FR-ARCH-004`: The system shall provide authorized administrators with tools to search the archive across all mailboxes based on complex queries and export results for legal proceedings.

#### 3.4 Security and Content Management
**Priority: Basic**
*   `FR-SEC-001`: The system shall integrate enterprise-grade anti-virus scanning for all inbound, outbound, and internal email.
*   `FR-SEC-002`: The system shall implement anti-spam and content filtering based on configurable policies.
*   `FR-SEC-003`: The system shall encrypt email transmission between servers and clients using standards such as TLS.
*   `FR-SEC-004`: The system shall authenticate all user access via integration with the central agency directory service.

#### 3.5 Access and Availability
**Priority: Basic**
*   `FR-ACC-001`: The system shall provide a fully functional web-based client (OWA-like) accessible from standard browsers.
*   `FR-ACC-002`: The system shall support secure synchronizations with mobile devices, including BlackBerry and other devices supporting ActiveSync or comparable protocols.
*   `FR-ACC-003`: The system shall provide a disaster recovery capability, with a defined Recovery Time Objective (RTO) and Recovery Point Objective (RPO) to be detailed in the plan.
*   `FR-ACC-004`: The system shall perform regular backups at multiple levels: individual messages (via archiving), individual mailboxes, and full server/system state.

#### 3.6 Administration and Management
**Priority: Basic**
*   `FR-ADMIN-001`: The system shall provide agency administrators with a delegated administration portal to create, disable, and manage user accounts within their agency.
*   `FR-ADMIN-002`: The system shall provide system administrators with a central management console for system-wide configuration, monitoring, and security policy management.
*   `FR-ADMIN-003`: The system shall generate audit logs for administrative actions, security events, and access.

#### 3.7 Integration Interfaces
**Priority: Basic**
*   `FR-INT-001`: The system shall interface with existing agency directory services (LDAPv3 or similar) for user authentication and provisioning.
*   `FR-INT-002`: The system shall support standard email protocols (SMTP, POP3, IMAP4) to allow integration with other agency software applications.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Web Client:** A clean, intuitive, and accessible web interface for all email, calendar, and contact tasks.
*   **Mobile Interfaces:** Native or optimized experiences for BlackBerry and other mobile devices.
*   **Administration Consoles:** Web-based or thick-client consoles for agency and system administrators.

#### 4.2 Hardware Interfaces
*   The system must be compatible with standard server hardware platforms used in the state data center. Specifics will be determined by the sourcing plan.

#### 4.3 Software Interfaces
*   **Directory Service:** Must interface via LDAPv3 with existing agency directories (e.g., Active Directory, Sun Directory Server).
*   **Public Internet:** Must communicate via SMTP, DNS, and TLS with external mail servers.
*   **Backup System:** Must integrate with enterprise backup software (e.g., NetBackup, Commvault).

#### 4.4 Communications Interfaces
*   Must support secure communication protocols: TLS 1.2+ for SMTP, IMAP, POP; HTTPS for web access; and encrypted tunnels for mobile device synchronization.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-PERF-001`: System availability shall be 99.9% or higher, excluding scheduled maintenance.
*   `NFR-PERF-002`: Email delivery latency (internal-to-internal) shall be less than 30 seconds, 95% of the time.
*   `NFR-PERF-003`: The web client shall render and be interactive within 3 seconds for a standard mailbox, under normal load.

#### 5.2 Safety and Security Requirements
*   `NFR-SEC-001`: The system shall comply with all applicable federal (e.g., FISMA, HIPAA, SOX) and state IT security standards for data confidentiality and integrity.
*   `NFR-SEC-002`: The system shall protect personally identifiable information (PII) in accordance with state privacy laws.
*   `NFR-SEC-003`: The system shall undergo regular third-party security penetration testing and vulnerability assessments.

#### 5.3 Compliance Requirements
*   `NFR-COMP-001`: The archiving and retention system shall be configurable to comply with the Florida Public Records Law and other relevant retention schedules.
*   `NFR-COMP-002`: The system shall maintain audit trails sufficient to demonstrate compliance with relevant regulations (SOX, HIPAA).

#### 5.4 Scalability and Capacity
*   `NFR-SCAL-001`: The system architecture shall be scalable to support a minimum of 50,000 concurrent users and a total mailbox storage capacity in the petabyte range, as projected for the 2013 horizon.

### 6. Acceptance Approach
The deliverable of the current project phase is a **proposed sourcing plan**. Acceptance of this plan will be based on the following criteria:
1.  The plan comprehensively addresses all **Basic** functional and non-functional requirements outlined in this SRS.
2.  The plan includes a detailed cost-benefit analysis (CBA) comparing at least three sourcing options: In-House development/managed, Externally provisioned (Cloud/SaaS), and a Hybrid model.
3.  The plan presents a viable, high-level migration strategy and timeline concluding by June 30, 2013.
4.  The plan identifies key risks, dependencies, and assumptions for each sourcing option.
5.  The plan is submitted by the deadline of December 31, 2009.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Chief Architect | | | |
| SRS Author | | | |