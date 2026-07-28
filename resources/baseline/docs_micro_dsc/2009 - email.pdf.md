# **Software Requirements Specification (SRS)**
## **Statewide Unified Messaging & Collaboration Service (SUMCS)**
**Document Version:** 1.0
**Date:** [Date of Draft]
**Status:** Draft for Proposal

---

### **1. Introduction**

#### **1.1 Purpose**
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the proposed Statewide Unified Messaging & Collaboration Service (SUMCS). The primary purpose of this document is to provide a detailed description of the system to be developed, serving as a basis for the proposed plan due December 31, 2009, and as a foundation for subsequent design, development, and procurement activities. This SRS is intended for use by state executives, project stakeholders, system architects, developers, and agency IT managers.

#### **1.2 Document Conventions**
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Keywords:** "Shall" indicates a mandatory requirement. "Should" indicates a desirable but not mandatory feature. "Will" indicates a statement of fact or future intent.
*   **Formatting:** Technical terms and references to system components are `highlighted`.

#### **1.3 Project Scope**
The SUMCS project aims to design, procure, and implement a centralized, secure, and cost-effective email, calendaring, and contact management service for all executive branch agencies of the state. The system will replace disparate, agency-specific solutions, achieving economies of scale and standardized governance.

**In-Scope:**
*   Centralized provisioning and management of user accounts (mailbox, calendar, contacts).
*   Core user functionality for sending, receiving, and managing email, calendars, and contacts via standard clients (e.g., Outlook, web browser, mobile ActiveSync).
*   Centralized administrative console for system management.
*   Integrated security services including anti-virus, anti-spam, and message filtering.
*   System-wide archiving, retention, and legal discovery (e-discovery) capabilities.
*   Migration of all executive branch agency users from legacy systems to the new SUMCS platform.
*   Compliance with relevant federal and state security, privacy, and records management mandates.

**Out-of-Scope:**
*   Non-executive branch agencies (e.g., legislative, judicial) unless a future expansion is agreed upon.
*   Replacement of internal agency line-of-business applications that use email protocols.
*   Development of custom email client software.
*   Long-term storage of archival data beyond the configured retention periods (assumes integration with state archives).

#### **1.4 References**
*   State IT Security Policy & Standards Manual
*   Federal Information Security Management Act (FISMA) guidelines
*   State Records Retention and Disposition Schedules
*   Relevant privacy acts (e.g., State Privacy Act, HIPAA if applicable)

---

### **2. Overall Description**

#### **2.1 Product Perspective**
The SUMCS is envisioned as a new, mission-critical enterprise system. It will interface with:
*   **State Identity & Access Management (IAM) System:** For user authentication and authoritative identity source.
*   **State Network Backbone:** For connectivity to all agency offices and remote users.
*   **Agency Active Directory/LDAP Servers (Optional):** For possible directory synchronization.
*   **State Archival Storage System:** For long-term retention of records.
*   **External Internet Mail Servers:** For sending/receiving internet email.

#### **2.2 Product Functions**
The high-level functions of SUMCS are:
1.  **User Collaboration:** Provide reliable email, shared calendaring, and contact management.
2.  **Unified Administration:** Offer a single pane of glass for managing the entire tenant.
3.  **Security & Protection:** Actively defend against malware, spam, and data loss.
4.  **Compliance & Governance:** Automatically enforce retention policies and enable efficient legal discovery.
5.  **Agency Migration:** Provide tools and processes for seamless migration from legacy systems.

#### **2.3 User Classes and Characteristics**
| User Class | Characteristics | Estimated Population |
| :--- | :--- | :--- |
| **End-User** | Executive branch employees. Varied technical skill. Requires intuitive access via desktop, web, and mobile. | Tens of thousands |
| **Agency Administrator** | Agency IT staff. Manages agency-specific distribution lists, resource mailboxes, and user support. | Hundreds |
| **System Administrator** | Central IT team operating the service. Responsible for core infrastructure, global policies, and security. | Dozens |
| **Compliance Officer** | Legal & records management staff. Requires powerful search and export for e-discovery and audits. | Scores |
| **Help Desk Staff** | Provides first-line support. Requires tools to reset passwords, diagnose delivery issues, and manage quotas. | Hundreds |

#### **2.4 Operating Environment**
*   **Network:** Must operate within the state's secure intranet and through designated DMZs for internet mail flow.
*   **Client Access:** Must support Microsoft Outlook (MAPI/HTTP), web browsers (HTTPS), and mobile devices (ActiveSync, IMAP).
*   **Operating System:** To be determined by solution architecture (e.g., Windows Server, Linux, or cloud SaaS platform).
*   **Database:** Robust backend database for user information, messages, and calendar data.

#### **2.5 Design and Implementation Constraints**
1.  **`CON-001`** – The proposed system architecture and implementation plan **shall** be finalized and submitted by **December 31, 2009**.
2.  **`CON-002`** – The complete migration of all executive branch agency users to the new system **shall** be completed by **June 30, 2013**.
3.  **`CON-003`** – The system **shall** be designed and operated in full compliance with all applicable federal (e.g., FISMA) and state regulations for information confidentiality, integrity, availability, and privacy.

#### **2.6 Assumptions and Dependencies**
*   **Assumption:** Adequate state budget and resources will be allocated for the procurement, implementation, and migration phases.
*   **Assumption:** Agencies will provide necessary subject matter experts and cooperate with the migration schedule.
*   **Dependency:** Successful integration with the State IAM system is critical for user provisioning and authentication.
*   **Dependency:** The state network infrastructure will provide sufficient bandwidth and reliability for the service.

---

### **3. System Features**

#### **3.1 Feature 1: Core User Messaging & Collaboration**
**3.1.1 Description**
Provide a reliable, intuitive interface for users to perform day-to-day email, calendaring, and contact management tasks.
**3.1.2 Requirements**
*   `FR-101` – The system **shall** allow users to send and receive internal and external email messages with attachments.
*   `FR-102` – The system **shall** provide a personal calendaring system supporting appointment scheduling, reminders, and recurrence.
*   `FR-103` – The system **shall** support shared calendars, with configurable permissions for viewing and editing.
*   `FR-104` – The system **shall** provide a global address list (GAL) containing all SUMCS users and groups.
*   `FR-105` – The system **shall** allow users to manage personal contact lists.
*   `FR-106` – The system **shall** be accessible via a standards-based web client (e.g., HTTPS) from within the state network.

#### **3.2 Feature 2: Administrative Management**
**3.2.1 Description**
Provide a centralized, role-based administrative platform for managing the entire service lifecycle.
**3.2.2 Requirements**
*   `FR-201` – The system **shall** provide tools for bulk provisioning, modification, and de-provisioning of user accounts, synchronized with the state IAM system where possible.
*   `FR-202` – The system **shall** allow for the creation and management of distribution lists and shared mailboxes.
*   `FR-203` – The system **shall** provide role-based access control (RBAC), differentiating between System, Agency, and Help Desk admin roles.
*   `FR-204` – The system **shall** include monitoring dashboards showing system health, performance, and capacity metrics.

#### **3.3 Feature 3: Security, Anti-Virus, and Filtering**
**3.3.1 Description**
Integrate multi-layered security controls to protect the system from threats and unauthorized access.
**3.3.2 Requirements**
*   `FR-301` – The system **shall** scan all inbound, outbound, and internal email messages for viruses and malware, quarantining or cleansing infected content.
*   `FR-302` – The system **shall** employ configurable anti-spam filtering to block unsolicited commercial email.
*   `FR-303` – The system **shall** support transport rules (policy-based filtering) for data loss prevention (DLP), such as blocking messages containing specific sensitive data patterns.
*   `NFR-304` – All data in transit **shall** be encrypted using TLS 1.2 or higher. Data at rest **shall** be encrypted using FIPS 140-2 validated cryptographic modules.

#### **3.4 Feature 4: Archiving, Retention, and Legal Discovery**
**3.4.1 Description**
Implement a unified policy framework for email retention and provide efficient tools for legal and compliance searches.
**3.4.2 Requirements**
*   `FR-401` – The system **shall** provide a centralized, immutable archive for all email messages sent or received by the service.
*   `FR-402` – The system **shall** allow administrators to define and apply retention policies based on state records schedules (e.g., delete after 7 years).
*   `FR-403` – The system **shall** include a legal hold functionality to preserve all data related to specified custodians, suspending retention policies.
*   `FR-404` – The system **shall** provide a search interface for compliance officers to perform granular, cross-mailbox searches based on keywords, dates, sender/recipient, etc., with the ability to export results in a legally defensible format.

#### **3.5 Feature 5: Migration Framework**
**3.5.1 Description**
Provide the tools, documentation, and processes to migrate all agencies from their legacy email systems with minimal user disruption.
**3.5.2 Requirements**
*   `FR-501` – The system **shall** support migration from common legacy platforms (e.g., IBM Notes, Novell GroupWise, various POP/IMAP systems).
*   `FR-502` – The system **shall** provide tools to migrate user mailbox data (email, calendar, contacts) preserving folder structure and metadata.
*   `FR-503` – The system **shall** support staged, agency-by-agency migration, allowing for coexistence (e.g., directory synchronization, mail routing) during the transition period.

---

### **4. Non-Functional Requirements**

#### **4.1 Performance Requirements**
*   `NFR-601` – System availability **shall** be 99.9% or higher during core business hours (7:00 AM - 7:00 PM, Monday-Friday).
*   `NFR-602` – Email delivery latency (internal-to-internal) **shall** be less than 30 seconds, 95% of the time under normal load.
*   `NFR-603` – The web client **shall** render and be interactive within 3 seconds for 95% of page loads.

#### **4.2 Safety and Security Requirements**
*   `NFR-701` – The system **shall** require strong authentication (minimum: username/password with account lockout; desired: multi-factor authentication).
*   `NFR-702` – The system **shall** maintain detailed audit logs of all administrative actions and access to compliance search tools. Logs **shall** be retained for a minimum of one year.
*   `NFR-703` – The system design **shall** undergo a formal Security Risk Assessment and Authorization to Operate (ATO) process prior to production launch.

#### **4.3 Software Quality Attributes**
*   **Scalability:** The architecture **shall** be able to scale to support a 20% increase in users and a 30% annual increase in data volume without major re-architecture.
*   **Maintainability:** System software **shall** be supported by the vendor with regular security patches and updates. Administrative tasks **shall** be automatable via scripting/APIs.
*   **Usability:** The web client interface **shall** comply with Section 508 accessibility standards.

---

### **5. Project Timeline & Milestones (High-Level)**
*   **Milestone 1:** SRS Finalized & Proposal Submitted – **December 31, 2009**
*   **Milestone 2:** Vendor Selection/RFP Award – Q2 2010
*   **Milestone 3:** Core System Deployed & Pilot Agency Migration – Q4 2011
*   **Milestone 4:** Phased Agency Migrations – 2012 - Q2 2013
*   **Milestone 5:** Full Operational Capability & Legacy System Decommission – **June 30, 2013**

---
**Document Approval:**

| Name | Title | Signature | Date |
| :--- | :--- | :--- | :--- |
| | Chief Information Officer (State) | | |
| | SUMCS Project Director | | |
| | Lead System Architect | | |