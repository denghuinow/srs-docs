# Software Requirements Specification (SRS)
## Laboratory Information System (LIS) Rewrite & Enhancement
**Document Version:** 1.0
**Date:** October 26, 2023
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the software requirements for the rewrite and enhancement of the core Laboratory Information System (LIS). It is intended for use by the project stakeholders, including development teams, quality assurance, project management, and the Technical Owner, to ensure a common understanding of the system's functionality, constraints, and quality attributes.

#### 1.2 Document Conventions
*   **Requirements:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Priority:** (H) High, (M) Medium, (L) Low.
*   **Keywords:** `MUST`, `SHALL`, `WILL` indicate mandatory requirements. `SHOULD` indicates a recommendation.

#### 1.3 Project Scope
The scope of this project is a targeted rewrite of the core LIS to achieve improved performance, ensure system reliability, and maintain/achieve regulatory compliance. The effort is scoped to:
*   Implement validated critical defects and enhancements.
*   Implement new, validated functional requirements gathered in specific requirement sessions.
*   Modify existing core functionalities **only** when necessary to implement a new requirement.
*   **Out of Scope:** A ground-up, feature-for-feature reimplementation of all existing LIS functionality.

#### 1.4 References
*   Company Active Directory Schema
*   HIPAA Security and Privacy Rules
*   .NET Framework 3.5 Documentation
*   SQL Server 2008 Documentation
*   Validated Requirements Session Notes (Attached)

### 2. Overall Description

#### 2.1 Product Perspective
This system is a rewrite and enhancement of an existing, mission-critical Laboratory Information System. It is a core business application within the company's IT ecosystem. The system is a standalone application but has critical dependencies on external systems as outlined in Section 2.4.

#### 2.2 Product Functions
The core functions of the system include:
*   User account administration (creation, role/division assignment).
*   Integrated authentication and authorization via company Active Directory.
*   Provision of context-sensitive online help.
*   Comprehensive system logging.
*   Email notification for critical system events.
*   Management of laboratory data with full HIPAA compliance.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Responsibilities |
| :--- | :--- | :--- |
| **Laboratory User** | Medical/technical staff. Uses the LIS for daily operational tasks (e.g., sample processing, result entry). Has varying levels of access based on role. | Perform laboratory workflows, view patient/results data. |
| **System Administrator** | IT or lab supervisory staff. Technically proficient. | Create and manage user accounts, assign roles/divisions/locations, monitor system health via logs. |
| **Technical Owner** | Senior IT management. Has authority over production deployments. | Provide final sign-off for any production release. |

#### 2.4 Operating Environment
*   **Software Platform:** Microsoft .NET Framework 3.5.
*   **Database:** Microsoft SQL Server 2008 (single instance).
*   **Directory Services:** Company Microsoft Active Directory.
*   **Email System:** Corporate SMTP server for notifications.

#### 2.5 Design and Implementation Constraints
1.  The application **MUST** be developed using the .NET Framework 3.5.
2.  Data persistence **MUST** use the single, specified SQL Server 2008 database instance.
3.  User authentication **MUST** be integrated with the company's Active Directory.
4.  Established, reputable open-source frameworks (e.g., for logging, ORM) **SHOULD** be used where appropriate to reduce development time and increase reliability.
5.  All new and modified code **MUST** maintain HIPAA compliance for data security and privacy.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** Development and deployment will proceed in a modular fashion based on validated requirement sets.
*   **Assumption:** The company's Active Directory service will be available and accessible during system operation.
*   **Dependency:** The system is dependent on the corporate Active Directory for real-time user validation and authentication.
*   **Dependency:** A formal sign-off from the designated Technical Owner is a hard dependency for any production deployment.

### 3. External Interface Requirements

#### 3.1 User Interfaces
The user interface will be a Windows-based desktop application or a web application (to be specified in design docs). Every screen **SHALL** contain a clearly marked link or button to access context-sensitive help (`FR-030`).

#### 3.2 Hardware Interfaces
None specified. (Standard client-server architecture is assumed).

#### 3.3 Software Interfaces
*   **SI-001: Active Directory**
    *   **Purpose:** User authentication and status verification.
    *   **Protocol/Method:** LDAP/LDAPS.
    *   **Data:** Validate user principal name (UPN) or sAMAccountName; retrieve user groups for role mapping.

*   **SI-002: SQL Server 2008 Database**
    *   **Purpose:** Primary data storage for all application data.
    *   **Protocol/Method:** ADO.NET, T-SQL.
    *   **Data:** All LIS transactional data, user permissions, system configuration.

*   **SI-003: Corporate SMTP Server**
    *   **Purpose:** Sending error notification emails.
    *   **Protocol/Method:** SMTP.
    *   **Data:** Email recipient list (distribution list), error subject, and body.

#### 3.4 Communications Interfaces
Standard HTTP/HTTPS for any web services and TCP/IP for database connectivity.

### 4. System Features

#### 4.1 User Account Administration
**Description:** This feature allows System Administrators to manage user access within the LIS.

**Priority:** High (H)

**Requirements:**
*   `FR-010`: The system **SHALL** allow an administrator to create a new LIS user account.
*   `FR-011`: During user creation, the system **SHALL** validate the entered username against the company Active Directory to confirm it is a valid domain account.
*   `FR-012`: The system **SHALL** prevent the creation of a user if the username already exists in the LIS database.
*   `FR-013`: The system **SHALL** allow the administrator to associate the user with one or more pre-defined system roles (e.g., "Technician," "Pathologist," "Admin").
*   `FR-014`: The system **SHALL** allow the administrator to associate the user with one or more organizational divisions and locations.
*   `FR-015`: The system **SHALL** allow administrators to disable, enable, or modify role/division assignments for existing users.

**Usage Scenario: Adding a New Lab User**
1.  Administrator navigates to User Management screen.
2.  Administrator clicks "Add New User."
3.  Administrator enters the new user's Active Directory username.
4.  System queries Active Directory.
    *   *If invalid:* System displays error: "User not found in Active Directory."
    *   *If valid:* System checks LIS database for duplicate.
        *   *If duplicate:* System displays error: "User already exists in LIS."
        *   *If unique:* System proceeds.
5.  Administrator selects appropriate roles, divisions, and locations from lists.
6.  Administrator saves. System creates the user record with associations.

#### 4.2 System Logging & Notification
**Description:** This feature ensures all system events are recorded and critical errors are proactively communicated.

**Priority:** High (H)

**Requirements:**
*   `FR-020`: The system **SHALL** log all unhandled exceptions (errors) with timestamp, severity, source, and detailed message to an external, configurable log file.
*   `FR-021`: The system **SHALL** log warning and informational messages (e.g., user login, configuration changes) as defined by the application.
*   `FR-022`: The system **SHALL** send an email notification to a pre-configured distribution list when a logged error is of "Critical" severity.
*   `FR-023`: The format and location of the log file **SHALL** be configurable via an application configuration file.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-001`: User authentication (including AD validation) **SHALL** complete in under 3 seconds for 99% of requests under normal load.

#### 5.2 Safety & Compliance Requirements
*   `NFR-010`: The system **MUST** maintain full compliance with HIPAA Security and Privacy Rules in all new and modified functionality. This includes but is not limited to: access controls, audit logging of PHI access, and data encryption at rest and in transit as per company policy.

#### 5.3 Security Requirements
*   `NFR-020`: All user authentication **SHALL** be performed against the company Active Directory. The LIS **SHALL NOT** store independent user passwords.
*   `NFR-021`: User authorization (access to functions/data) **SHALL** be enforced based on roles and divisions assigned within the LIS.

#### 5.4 Software Quality Attributes
*   **Reliability:** The core user administration and authentication modules **SHALL** have an availability target of 99.5% during business hours.
*   **Maintainability:** `NFR-030`: All application code **SHALL** be accompanied by technical documentation detailing module purpose and key logic flows.
*   **Supportability:** `NFR-040`: Log files **SHALL** be formatted in a human-readable manner and be easily accessible for troubleshooting.

#### 5.5 Operational & Deployment Requirements
*   `NFR-050`: Updates to the production system **CAN ONLY** be deployed during the approved weekly maintenance window (e.g., Tuesday 7:00 PM to Wednesday 7:00 AM).
*   `NFR-051`: A full, automated backup of the LIS database **MUST** be verified as successful immediately prior to any production deployment.

### 6. Acceptance & Verification

#### 6.1 Priority Framework
Implementation priority **SHALL** be given in the following order:
1.  Critical defects impacting system stability or data integrity.
2.  Enhancements that alleviate significant user burden or operational inefficiency.
3.  Enhancements that facilitate scalable and efficient system growth.
4.  Minor defects and cosmetic improvements.

#### 6.2 Acceptance Approach
Formal acceptance of the system for production deployment requires the following:
1.  **Regression Testing:** All builds **MUST** pass a full regression test suite covering core LIS functionality.
2.  **User Acceptance Testing (UAT):** A formal UAT cycle **MUST** be conducted by designated end-users against the validated requirements. All critical and major issues from UAT **MUST** be resolved.
3.  **Sign-Off:** Final approval for production deployment **REQUIRES** formal written sign-off from the designated Technical Owner, confirming that requirements 6.2.1 and 6.2.2 have been met.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner | | | |
| Technical Owner | | | |
| Lead Developer | | | |
| QA Manager | | | |