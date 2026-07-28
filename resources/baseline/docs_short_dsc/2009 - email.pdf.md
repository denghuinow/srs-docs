# **Software Requirements Specification (SRS)**
**For the Florida Statewide Enterprise E-mail System Plan**

**Document Version:** 1.0
**Prepared for:** Agency for Enterprise Information Technology (AEIT)
**Prepared by:** [Your Name/Team Name]
**Date:** [Date of Creation]

---

## **1. Introduction**

### **1.1 Purpose**
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the proposed statewide enterprise e-mail system mandated by Florida Statute 282.34. Its primary purpose is to serve as the foundation for the comprehensive plan to be submitted by December 31, 2009, detailing sourcing options, cost-benefit analysis, and migration strategy. This document is intended for use by the AEIT Project Team, stakeholders, potential solution providers, and state leadership.

### **1.2 Document Conventions**
*   **Requirements:** Functional requirements are labeled as `FR-XXX`. Non-functional requirements are labeled as `NFR-XXX`.
*   **Priority:** Requirements are categorized as (H)igh, (M)edium, or (L)ow based on their criticality for the core plan and eventual system.
*   **Keywords:** The terms "MUST," "SHALL," "REQUIRED," "WILL," and "SHOULD" are used as described in IETF RFC 2119.

### **1.3 Project Scope**
This project encompasses the definition, planning, and high-level design of a consolidated e-mail service for all executive branch agencies of the State of Florida. The focus is on specifying the required capabilities to reduce operational costs, improve security, ensure compliance, and meet user needs.

#### **1.3.1 In Scope**
*   Specification of core end-user functionalities: e-mail, calendar, and contacts.
*   Definition of archiving, retention, and e-discovery capabilities for legal compliance.
*   Specification of security features including anti-virus, anti-spam, content filtering, and encryption.
*   Requirements for remote access via web and mobile devices.
*   Definition of basic administrative functions for agency and system-level administrators.
*   Development of a migration framework and schedule (2010-2013).

#### **1.3.2 Out of Scope**
*   Detailed design, technical implementation, or data structure specifications.
*   Collaboration tools such as instant messaging, shared workspaces, or document workflows.
*   Collection of detailed agency inventory and financial data (a parallel activity).
*   Final vendor selection, procurement, or contract negotiations.
*   Modification or integration with agency-specific line-of-business applications not dependent on core e-mail protocols.

### **1.4 References**
*   **Florida Statute 282.34:** State Data Center System; powers and duties.
*   **Florida Statute 282.0041:** Agency for State Technology; powers and duties.
*   **IETF RFC 2119:** Key words for use in RFCs to Indicate Requirement Levels.
*   **State of Florida Security and Privacy Standards:** Relevant policies for data handling.

## **2. Overall Description**

### **2.1 Product Perspective**
The proposed enterprise e-mail system is a strategic initiative to replace disparate agency e-mail systems with a single, managed service. It will interact with existing agency directory services (e.g., Active Directory), network infrastructure, and must be architected to allow for future integration. The system is a component of the broader State Data Center System.

### **2.2 User Classes and Characteristics**
| User Class | Description | Key Characteristics |
| :--- | :--- | :--- |
| **End-User** | An employee of an executive branch agency. | Varying technical proficiency. Primary need is reliable communication and scheduling. Requires access from office, home, and mobile. |
| **Agency Administrator** | IT staff within a specific agency. | Technically proficient. Manages user lifecycle and agency-specific configurations. Liaison between agency and system administrators. |
| **Data Center Administrator (SSRC Admin)** | Technical staff managing the statewide system infrastructure. | Highly technically proficient. Responsible for system health, security, backups, patching, and global policies. |
| **Legal/Compliance Personnel** | Staff from offices like the OIG or agency legal departments. | Not necessarily technical. Requires powerful, auditable search and hold capabilities for e-discovery and public records requests. |
| **AEIT Project Team** | Central team managing the planning and oversight. | Manages requirements, vendor relations, migration coordination, and project governance. |

### **2.3 Operating Environment**
*   **Logical Environment:** Must support access from the state network, trusted external networks, and the public internet (via secure methods).
*   **Client Devices:** Must be accessible from Windows and macOS computers, state-issued mobile devices (iOS, Android, Windows Mobile), and common web browsers.
*   **Integration Points:** Must interface with existing statewide or agency directory services for authentication and user provisioning.

### **2.4 Design and Implementation Constraints**
1.  **Legal Constraints:** The system MUST comply with all applicable Florida Statutes, including FS 282.34 and 282.0041, and federal/state regulations for data privacy (e.g., CJIS, HIPAA where applicable) and public records retention.
2.  **Schedule Constraint:** The functional requirements specification phase MUST be completed within 30 business days.
3.  **Security Constraints:** The solution MUST meet or exceed state security standards for data confidentiality, integrity, and availability.
4.  **Financial Constraint:** All proposed functionalities are subject to a cost-benefit analysis and must demonstrate a reduction in total cost of ownership compared to the decentralized model.
5.  **Technical Constraint:** The plan MUST assess and consider existing agency e-mail infrastructure (hardware, software, licenses) for potential reuse or migration.

### **2.5 Assumptions and Dependencies**
*   **Assumption:** Agencies will provide necessary inventory and user data to support planning and migration.
*   **Assumption:** Adequate network bandwidth and reliability will be available statewide to support the consolidated service.
*   **Dependency:** The final sourcing model (in-house, cloud, hybrid) will determine specific technical architectures.
*   **Dependency:** Cooperation from all executive branch agencies is required for successful migration.

## **3. System Features and Requirements**

### **3.1 Core End-User Functionality**
**Description:** This feature set covers the essential communication and productivity tools required by every end-user.

**Priority:** (H)

**Requirements:**
*   `FR-101`: The system SHALL allow users to send and receive e-mail messages with internal and external recipients. (H)
*   `FR-102`: The system SHALL support sending and receiving file attachments, with configurable size limits set by administrators. (H)
*   `FR-103`: The system SHALL provide a personal calendar for scheduling appointments, meetings, and all-day events. (H)
*   `FR-104`: The system SHALL allow users to create and manage personal contact lists. (M)
*   `FR-105`: The system SHALL provide folder-based organization for e-mails (e.g., Inbox, Sent, Drafts, custom folders). (H)
*   `FR-106`: The system SHALL include standard e-mail features: reply, reply-all, forward, and carbon copy (CC)/blind carbon copy (BCC). (H)

### **3.2 Remote and Mobile Access**
**Description:** This feature ensures users can access services securely from outside the office network using various clients.

**Priority:** (H)

**Requirements:**
*   `FR-201`: The system SHALL provide a secure web-based client (OWA/Webmail) accessible from standard browsers over HTTPS. (H)
*   `FR-202`: The system SHALL support synchronization with mobile devices (e.g., smartphones, tablets) using standard protocols (ActiveSync, IMAP, etc.). (H)
*   `NFR-201`: Mobile access SHALL enforce device security policies (e.g., PIN lock, remote wipe capability). (H)

### **3.3 Administration and Management**
**Description:** Capabilities for Agency and Data Center Administrators to manage users, groups, and system settings.

**Priority:** (H)

**Requirements:**
*   `FR-301`: The system SHALL allow Agency Administrators to provision, disable, and delete user mailboxes. (H)
*   `FR-302`: The system SHALL allow Agency Administrators to create, modify, and delete distribution lists, with support for nested groups. (M)
*   `FR-303`: The system SHALL integrate with a central directory service (e.g., LDAP, Active Directory) to synchronize user identities and attributes. (H)
*   `FR-304`: The system SHALL provide Data Center Administrators with tools for system monitoring, performance management, and alerting. (H)
*   `FR-305`: The system SHALL provide a role-based access control (RBAC) model to separate duties between Agency and Data Center Administrators. (M)

### **3.4 Security and Threat Protection**
**Description:** Features to protect the system infrastructure and user data from malicious software, spam, and data loss.

**Priority:** (H)

**Requirements:**
*   `FR-401`: The system SHALL perform pre-emptive virus and malware scanning on all inbound, outbound, and internal e-mail messages and attachments. (H)
*   `FR-402`: The system SHALL include configurable content filtering to block spam and phishing attempts. (H)
*   `FR-403`: The system SHALL support transport-level encryption (TLS) for e-mail in transit between servers and to external domains. (H)
*   `FR-404`: The system SHALL support encryption of e-mail at rest, based on policy or user action. (M)
*   `NFR-401`: The system SHALL maintain audit logs for all administrative actions and security-related events. (H)

### **3.5 Archiving, Retention, and E-Discovery**
**Description:** Capabilities to meet public records laws, legal holds, and compliance investigations.

**Priority:** (H)

**Requirements:**
*   `FR-501`: The system SHALL provide a centralized, tamper-evident archive for all sent and received e-mails, separate from user mailboxes. (H)
*   `FR-502`: The system SHALL enforce configurable retention policies based on content, sender/recipient, or other metadata. (H)
*   `FR-503`: The system SHALL provide Legal/Compliance Personnel with a search interface to query the archive across all user mailboxes based on complex criteria (keywords, date ranges, users, etc.). (H)
*   `FR-504`: The system SHALL allow authorized personnel to place search results or entire mailboxes on "legal hold," preventing alteration or deletion regardless of retention policies. (H)
*   `FR-505`: The system SHALL provide tools for authorized reviewers to redact sensitive information from e-mails exported for disclosure. (M)

## **4. Non-Functional Requirements**

### **4.1 Performance Requirements**
*   `NFR-P01`: The web client SHOULD render a usable inbox within 3 seconds for 95% of requests under expected load.
*   `NFR-P02`: E-mail delivery between internal users SHOULD occur within 60 seconds 99% of the time.

### **4.2 Safety and Security Requirements**
*   `NFR-S01`: The system SHALL be designed and operated in compliance with state data security standards and undergo regular security assessments.
*   `NFR-S02`: All authentication SHALL use secure, state-approved methods (e.g., integrated Windows auth, multi-factor for admin access).

### **4.3 Business Rules**
*   `BR-01`: E-mail addresses SHALL follow a standardized format for the state (e.g., `firstname.lastname@agency.state.fl.us`). The exact format is TBD.
*   `BR-02`: Default mailbox size quotas SHALL be established uniformly but MAY be adjustable by agency or role.

### **4.4 Data Migration Requirements**
*   `FR-601`: The migration plan MUST include a method for migrating existing user e-mail, calendar, and contact data from legacy agency systems to the new enterprise system with minimal data loss.

## **5. Appendices**

### **5.1 Glossary**
*   **AEIT:** Agency for Enterprise Information Technology.
*   **E-Discovery:** The electronic aspect of identifying, collecting, and producing electronically stored information in response to a legal request.
*   **Legal Hold:** A process to preserve all relevant information when litigation is reasonably anticipated.
*   **OWA:** Outlook Web App (a common term for webmail).
*   **SSRC:** Statewide Data Center (assumed from context).

### **5.2 Undecided Issues (To Be Resolved in Plan)**
1.  Final sourcing model (State-operated, Vendor-hosted, Hybrid).
2.  Technical and financial feasibility analysis of each functional requirement.
3.  Standardized format for state e-mail addresses.
4.  Detailed cost estimates and projected savings per sourcing option.
5.  Specific technical protocols and APIs for directory and application integration.

### **5.3 Success Metrics**
*   Successful submission of a complete proposed plan to state leadership by **December 31, 2009**.
*   The plan demonstrates a clear path to **reduced operational costs** compared to the aggregate of existing agency systems.
*   The plan includes a **feasible, phased migration schedule** to transition all executive branch agencies between **July 2010 and June 2013**.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| AEIT Project Lead | | | |
| Technical Lead | | | |
| Stakeholder Representative | | | |