# Software Requirements Specification (SRS)
## Policy Analysis & Goal Management (PAGM) Tool

**Document Version:** 1.0  
**Date:** [Current Date]  
**Authors:** [Project Team]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the **Policy Analysis & Goal Management (PAGM) Tool**. The primary purpose of this system is to assist security and privacy analysts in the systematic mining, reconciliation, and management of goals and scenarios extracted from privacy and security policy documents. This document is intended for use by the project stakeholders, development team, quality assurance team, and project managers.

#### 1.2 Scope
The PAGM Tool will be a web-based application that provides a centralized repository for goals and scenarios derived from policy analysis. Its core capabilities include user and role management, structured data entry and classification, and support for the specification and analysis of access control policies using the RACAF (Role-based Access Control Analysis Framework) methodology. The system will enforce strict security and auditability constraints, including comprehensive access logging and secure credential handling.

**Out-of-Scope:**
*   Automated natural language processing for initial policy document ingestion.
*   Integration with external identity providers (e.g., Active Directory, LDAP) in the initial release.
*   Advanced data visualization or reporting dashboards beyond basic list views and logs.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **SRS:** Software Requirements Specification.
*   **RACAF:** Role-based Access Control Analysis Framework. A methodology for specifying and analyzing access control policies.
*   **Goal:** A high-level objective or requirement extracted from a policy document (e.g., "Ensure patient data confidentiality").
*   **Scenario:** A specific use case, process, or situation described in a policy that operationalizes a goal.
*   **Analyst:** A primary user role responsible for entering and managing policy artifacts.
*   **PAGM Tool:** The system being specified in this document.

#### 1.4 References
*   [List any relevant project charter, standards, or prior documents here]
*   *Example: IETF RFC 6238 - TOTP: Time-Based One-Time Password Algorithm*

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a high-level description of the product. Section 3 details specific functional requirements. Section 4 outlines non-functional requirements, including performance, security, and auditability. Appendices may contain supplementary information.

---

### 2. Overall Description

#### 2.1 Product Perspective
The PAGM Tool is a new, self-contained web application. It will interact with a backend relational database for persistent storage. The system architecture follows a standard three-tier model: Presentation Layer (Web UI), Application Logic Layer, and Data Storage Layer.

#### 2.2 Product Functions (Summary)
1.  **User Access & Role Management:** Secure authentication and authorization for four distinct user roles.
2.  **Goal & Scenario Repository Management:** Create, read, update, delete, search, and classify policy artifacts (goals and scenarios).
3.  **RACAF Policy Support:** Facilitate the definition and basic analysis of access control policies within the RACAF framework.
4.  **Audit Logging:** Automatically record all significant user actions for security and compliance.
5.  **System Administration:** Configuration and maintenance functions accessible to administrators.

#### 2.3 User Characteristics
| Role | Description | Key Activities |
| :--- | :--- | :--- |
| **Administrator** | Manages system users and overall configuration. | Create user accounts, assign roles, configure system settings, view system logs. |
| **Project Manager** | Oversees projects containing policy artifacts. | Create/manage projects, assign analysts to projects, view consolidated project reports and logs. |
| **Analyst** | Primary contributor of policy analysis data. | Within assigned projects: Add, classify, edit, and delete goals and scenarios; perform RACAF analysis. |
| **Guest** | Read-only access to view published content. | Browse and search public goals, scenarios, and policy analyses. Cannot modify any data. |

#### 2.4 Constraints
1.  **Security:** All user passwords MUST be stored using a strong, adaptive, and salted hashing algorithm (e.g., Argon2id, bcrypt, scrypt). Plain-text or weakly hashed password storage is prohibited.
2.  **Auditability:** The system MUST automatically generate an immutable access log entry for every successful and attempted "Add," "Delete," and "Edit" action performed on any entity within the system (e.g., User, Goal, Scenario, Project). Logs must be viewable only by authorized roles (Admin, Project Manager).
3.  **Authentication:** User login sessions MUST be secure, employing industry-standard practices (e.g., HTTPS/TLS, protection against brute-force attacks, secure session management).
4.  **Technical:** The system shall be developed as a web application accessible via modern browsers (Chrome, Firefox, Safari, Edge - last two major versions).

#### 2.5 Assumptions and Dependencies
*   **Assumption:** Users will have a modern web browser with JavaScript enabled.
*   **Assumption:** Analysts are trained in the RACAF methodology.
*   **Dependency:** Availability of a supported relational database management system (e.g., PostgreSQL, MySQL).
*   **Dependency:** Deployment on a server with a valid TLS/SSL certificate to ensure secure communication.

---

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 User Management Module
*   **FR-UM-01: User Authentication**
    *   The system shall allow users to log in by providing a unique username and password.
    *   The system shall securely validate credentials against the hashed values in the database.
    *   The system shall enforce a configurable account lockout policy after `N` consecutive failed login attempts.
*   **FR-UM-02: Role-Based Authorization**
    *   The system shall enforce access controls based on the four defined roles (Administrator, Project Manager, Analyst, Guest).
    *   The system's user interface shall present only the functions and data permissible for the logged-in user's role.
*   **FR-UM-03: User Account Management (Admin)**
    *   The system shall allow Administrators to create, view, update (e.g., reset password, change role), and deactivate user accounts.
    *   The system shall require Administrator confirmation for critical actions like account deletion.

##### 3.1.2 Goal & Scenario Repository Module
*   **FR-GS-01: Create Artifact**
    *   The system shall allow Analysts to create new Goal and Scenario records within an assigned project.
    *   Each artifact shall require mandatory fields: `Title`, `Description`, `Classification` (from a predefined list), `Project` association, and `Created By` (auto-populated).
*   **FR-GS-02: Retrieve & View Artifacts**
    *   The system shall allow all authorized users to view, search, and filter Goals and Scenarios based on attributes like title, description, classification, project, and date.
    *   Guests shall only view artifacts marked as "Public" or within public projects.
*   **FR-GS-03: Modify Artifact**
    *   The system shall allow Analysts (and potentially Project Managers) to edit the details of existing Goals and Scenarios they own or are authorized to modify.
    *   Each edit shall create a new version or preserve a history log of the change.
*   **FR-GS-04: Delete Artifact**
    *   The system shall allow Analysts and Project Managers to delete artifacts, with a confirmation dialog to prevent accidental deletion.
*   **FR-GS-05: Classify & Relate Artifacts**
    *   The system shall allow users to classify artifacts using a system-defined taxonomy (e.g., Confidentiality, Integrity, Availability, Privacy).
    *   The system shall allow users to define relationships between artifacts (e.g., "Scenario S1 operationalizes Goal G1").

##### 3.1.3 RACAF Policy Module
*   **FR-RACAF-01: Policy Specification**
    *   The system shall provide a structured interface for Analysts to define RACAF policy elements (Roles, Permissions, Constraints) linked to specific Scenarios and Goals.
*   **FR-RACAF-02: Basic Policy Analysis**
    *   The system shall be able to check for basic consistency within a defined RACAF policy (e.g., identify roles with conflicting permissions within a given scenario).
    *   The system shall generate a simple report of the analysis findings.

##### 3.1.4 Audit Logging Module
*   **FR-AUDIT-01: Log Generation**
    *   The system shall automatically generate a log entry for every Add, Edit, and Delete action on core entities (User, Project, Goal, Scenario, RACAF Policy).
    *   Each log entry shall include: Timestamp (UTC), User ID, Action Type (`CREATE`, `UPDATE`, `DELETE`), Entity Type, Entity ID, and a summary of changes (e.g., `"Field 'Title' changed from 'Old' to 'New'"`).
*   **FR-AUDIT-02: Log Viewing**
    *   The system shall provide a dedicated interface for Administrators and Project Managers to view, search, and filter the access logs.
    *   Project Managers shall only see logs for actions taken within their managed projects.

#### 3.2 Non-Functional Requirements

##### 3.2.1 Security Requirements
*   **NF-SEC-01:** All authentication shall occur over an encrypted channel (HTTPS/TLS 1.2+).
*   **NF-SEC-02:** Passwords shall be stored using a strong, salted, and adaptive hashing function (e.g., Argon2id with appropriate work factors). The implementation shall follow OWASP recommendations.
*   **NF-SEC-03:** Session management shall be secure, using random session identifiers, with timeouts after a period of inactivity (configurable, default 30 minutes).
*   **NF-SEC-04:** The system shall be protected against common web vulnerabilities (e.g., SQL Injection, Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF)) as per OWASP Top 10 guidelines.

##### 3.2.2 Auditability & Compliance
*   **NF-AUD-01:** Access logs shall be stored in a durable, tamper-evident manner (e.g., write-once storage or database with restricted write permissions). Logs shall be retained for a minimum of 7 years to support compliance.
*   **NF-AUD-02:** Log entries shall be immutable once written. No user, including Administrators, shall be able to modify or delete audit log entries through the application interface.

##### 3.2.3 Performance Requirements
*   **NF-PER-01:** The system shall support concurrent login and usage by at least 50 users.
*   **NF-PER-02:** Page load times for standard views (list of goals, scenarios) shall be less than 3 seconds under normal load (95th percentile).

##### 3.2.4 Usability Requirements
*   **NF-USA-01:** The user interface shall be intuitive and require minimal training for Analysts familiar with the RACAF methodology.
*   **NF-USA-02:** The system shall provide clear feedback for all user actions (success, error, warning messages).

##### 3.2.5 Data Management Requirements
*   **NF-DATA-01:** The system shall support regular, automated backups of the entire database, including audit logs.
*   **NF-DATA-02:** A data export function (e.g., CSV, JSON) shall be available for Goals, Scenarios, and associated RACAF data for authorized users (Project Manager, Admin).

---

### 4. Appendices

#### Appendix A: Data Models (Preliminary)
*Entity-Relationship diagrams or simple schema descriptions can be placed here.*

#### Appendix B: Use Case Diagrams
*Graphical representations of key use cases (User Login, Manage Goal, Perform RACAF Analysis, View Audit Log) can be placed here.*

#### Appendix C: Sample Audit Log Schema
```sql
-- Example table structure for audit logs
CREATE TABLE audit_log (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    timestamp DATETIME NOT NULL DEFAULT UTC_TIMESTAMP(),
    user_id VARCHAR(50) NOT NULL, -- Reference to users table
    ip_address VARCHAR(45),
    action_type ENUM('CREATE', 'UPDATE', 'DELETE', 'LOGIN_ATTEMPT', 'LOGIN') NOT NULL,
    entity_type VARCHAR(50) NOT NULL, -- e.g., 'GOAL', 'SCENARIO', 'USER'
    entity_id VARCHAR(255), -- ID of the affected entity
    change_description TEXT, -- Human-readable summary of changes
    -- Additional fields for before/after snapshots could be added
    INDEX idx_timestamp (timestamp),
    INDEX idx_user_entity (user_id, entity_type)
);
```

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| Quality Assurance Lead | | | |