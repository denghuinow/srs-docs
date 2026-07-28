# Software Requirements Specification (SRS)
## Unified University Inventory System (UUIS)

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Unified University Inventory System (UUIS). The intended audience includes project stakeholders, software developers, testers, project managers, and system administrators. This document serves as the definitive source of requirements for the system's design, implementation, and verification.

#### 1.2 Scope
The UUIS is a web-based application designed to integrate three separate faculty inventory databases into a single, centralized system. It will manage university inventory assets (including physical spaces, software licenses, and other equipment), facilitate the request workflow for borrowing or reserving these assets, and enforce role-based access control aligned with the university's organizational hierarchy.

**In-Scope:**
*   Centralized management of all inventory assets.
*   User request creation, submission, approval, and fulfillment workflows.
*   Role-based access control and permission delegation.
*   Integration with three existing faculty inventory databases.
*   Search functionality and standard reporting.
*   User authentication and notification via email.

**Out-of-Scope:**
*   Financial transactions, billing, or invoicing.
*   Payroll or human resources management.
*   Student academic records or grading systems.
*   Development of the underlying university credential system (integration only).

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **UUIS** | Unified University Inventory System |
| **Asset** | Any item managed by the system (e.g., projector, lab space, software license). |
| **Organizational Scope** | The hierarchical boundary of a user's authority (Department, Faculty, University). |
| **RBAC** | Role-Based Access Control |
| **Administrator (Levels 1-3)** | Department, Faculty, or University-level administrative users with asset and request management privileges. |
| **Inventory Administrator** | A user delegated specific asset management permissions by a higher-level Administrator. |
| **IT Administrator (Level 4)** | System-wide administrator with full control over infrastructure and permission models. |

#### 1.4 References
*   University Organizational Hierarchy Policy
*   Faculty Inventory Database Schemas (x3)
*   University IT Security Policy

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements. Appendices may contain supplementary information.

---

### 2. Overall Description

#### 2.1 Product Perspective
The UUIS is a new, self-contained system that will replace the functionality of three legacy faculty inventory systems. It operates within the university's IT ecosystem, interfacing with external databases for initial data migration and ongoing synchronization, and with the university email system for notifications.

**System Interfaces:**
*   **Legacy Database Interface:** The system shall connect to three distinct faculty inventory databases to extract, transform, and load (ETL) existing asset and user data.
*   **Email System Interface (SMTP):** The system shall connect to the university's SMTP server to send request status notifications (e.g., approval, rejection, fulfillment) to users.

**User Interfaces:** The primary interface shall be a responsive web application compatible with modern browsers (Microsoft Edge, Mozilla Firefox, Google Chrome, Opera, Safari).

#### 2.2 Product Functions
The core functions of UUIS are:
1.  **User Authentication & Authorization:** Secure login and enforcement of permissions based on role and organizational scope.
2.  **Asset Lifecycle Management:** Full CRUD (Create, Read, Update, Delete/Return) operations for inventory assets, scoped to user authority.
3.  **Request Workflow Management:** End-to-end process for creating, submitting, approving/rejecting, and fulfilling requests to borrow or reserve assets.
4.  **Delegation Management:** Allows administrators to grant specific permissions to other users (Inventory Administrators).
5.  **Search & Discovery:** Simple and advanced search capabilities across the unified inventory.
6.  **Reporting:** Generation of predefined reports on asset status, request history, and user permissions.

#### 2.3 User Characteristics
| User Class | Skill Level | Key Responsibilities |
| :--- | :--- | :--- |
| **Student/Professor (Level 0)** | Novice to Advanced | Browse inventory, create and track personal requests. |
| **Department Admin (Level 1)** | Intermediate | Manage assets and approve requests within their department. Delegate permissions. |
| **Faculty Admin (Level 2)** | Intermediate | Manage assets and approve requests within their faculty. Delegate permissions. |
| **University Admin (Level 3)** | Intermediate | Broad oversight and management. Delegate permissions. |
| **Inventory Administrator** | Intermediate | Perform specific asset management tasks as delegated (e.g., updating status, processing returns). |
| **IT Administrator (Level 4)** | Expert | System configuration, user/role management, database maintenance, and infrastructure oversight. |

#### 2.4 Constraints
*   The system design must strictly adhere to the defined university organizational hierarchy (University > Faculty > Department).
*   The system must be installable and operable on both Microsoft Windows Server and Unix-based (e.g., Linux) server platforms.
*   All database servers hosting the UUIS database shall only be accessible from within the university's local network by the authorized IT team.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** Administrative users (Levels 1-3) will understand their organizational scope and delegate permissions responsibly.
*   **Dependency:** Successful integration is dependent on stable, documented access to the three legacy faculty inventory databases.
*   **Dependency:** User authentication will depend on the existing university credential system (e.g., LDAP/Active Directory), which provides username/password validation.
*   **Assumption:** University working hours are defined as 8:00 AM to 6:00 PM, Monday through Friday, excluding official holidays.

---

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Authentication & Authorization (AUTH)
*   **AUTH-01:** The system shall require users to authenticate with a username and password validated against the university credential system.
*   **AUTH-02:** The system shall enforce access permissions based on a combination of the user's role (Level 0-4) and their assigned organizational scope.
*   **AUTH-03:** An Administrator (Levels 1-3) shall be able to delegate a subset of their asset management permissions to another user, creating an Inventory Administrator role for a specified scope and time period.

##### 3.1.2 Asset Management (AM)
*   **AM-01:** Authorized users shall be able to add new inventory assets, specifying type, description, location, status (available, checked-out, under maintenance), and organizational owner.
*   **AM-02:** Users shall be able to modify attributes of assets within their management scope.
*   **AM-03:** The system shall allow authorized users to update an asset's status to "Returned" or "Available" upon its physical return.
*   **AM-04:** Any user shall be able to view details of assets for which they have read permissions, based on their role and scope.

##### 3.1.3 Request Workflow (RW)
*   **RW-01:** Students and Professors (Level 0) shall be able to create a request to borrow a reservable asset or reserve a space.
*   **RW-02:** The request shall include asset ID, requested dates/times, and purpose.
*   **RW-03:** The system shall route the request to the appropriate Administrator (Level 1-3) based on the asset's organizational scope.
*   **RW-04:** The responsible Administrator shall be able to approve or reject the pending request, optionally providing a reason.
*   **RW-05:** Upon approval, the system shall notify the requesting user and any assigned Inventory Administrator. The asset status shall be updated accordingly.
*   **RW-06:** Upon rejection, the system shall notify the requesting user with the reason.

##### 3.1.4 Search & Reporting (SR)
*   **SR-01:** The system shall provide a simple search interface with a single text box for searching asset names and descriptions.
*   **SR-02:** The system shall provide an advanced search interface allowing filtering by asset type, location, status, and organizational scope.
*   **SR-03:** The system shall generate a standard "Assets by Location" report.
*   **SR-04:** The system shall generate a standard "Request History" report filterable by date range and scope.
*   **SR-05:** Administrators shall be able to generate a "User Permissions" report for their organizational scope.

##### 3.1.5 System Administration (SYS)
*   **SYS-01:** IT Administrators (Level 4) shall have full access to all system data and functions.
*   **SYS-02:** IT Administrators shall be able to define new system-wide permission groups or roles.

#### 3.2 External Interface Requirements

##### 3.2.1 User Interfaces
*   The web interface shall be usable on the latest stable versions of Chrome, Firefox, Edge, Safari, and Opera.
*   All data entry forms shall provide clear validation messages.

##### 3.2.2 Hardware Interfaces
*   None specified beyond standard server hardware.

##### 3.2.3 Software Interfaces
*   **SI-01:** The system shall interface with the three legacy faculty inventory databases via provided connectors/APIs to perform initial data migration.
*   **SI-02:** The system shall connect to the university's central SMTP server to send email notifications.

##### 3.2.4 Communications Interfaces
*   Communication between the web client and application server shall use HTTPS.
*   Email notifications shall be sent via SMTP.

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance Requirements
*   **PER-01:** The system shall support concurrent access by at least 500 users.
*   **PER-02:** Page load times for standard user interactions (search, view asset) shall be under 3 seconds under normal load.
*   **PER-03:** Any database query initiated by a user action that takes longer than 60 seconds shall be automatically terminated by the system, and an appropriate error message shall be displayed to the user.

##### 3.3.2 Safety Requirements
*   Not applicable.

##### 3.3.3 Security Requirements
*   **SEC-01:** All user sessions shall be conducted over encrypted connections (TLS 1.2 or higher).
*   **SEC-02:** Passwords shall be hashed and salted in the database.
*   **SEC-03:** Direct access to the application database shall be restricted to the local network and authorized IT administrative accounts only.
*   **SEC-04:** The system shall prevent privilege escalation; a user cannot modify their own role or organizational scope.

##### 3.3.4 Software Quality Attributes
*   **AVAILABILITY:** The system shall achieve 99.5% availability during defined university working hours (8:00 AM - 6:00 PM, Mon-Fri). Scheduled maintenance shall only occur outside these hours.
*   **MAINTAINABILITY:** The system shall be designed with modular components and well-documented APIs to facilitate future enhancements and corrections. The mean time to repair (MTTR) for critical bugs shall be less than 4 hours.
*   **PORTABILITY:** The application server component shall be deployable on both Microsoft Windows Server 2019+ and a mainstream Linux distribution (e.g., Ubuntu LTS, RHEL).

---

### 4. Supporting Information

#### 4.1 Priority & Acceptance
*   **Priority 1 (Critical):** Requirements AUTH-01, AUTH-02, AM-01, AM-02, RW-01 to RW-06. These constitute the core workflow.
*   **Acceptance Criteria:** The system will be accepted upon successful demonstration of:
    1.  Correct enforcement of the hierarchical permission model.
    2.  End-to-end processing of all request types (borrow, reserve).
    3.  System availability meeting the specified target during a 2-week observation period.

#### 4.2 Appendix A: Use Case Scenarios
**Scenario: Professor Requests a Projector**
1.  Professor Logs in (AUTH-01).
2.  Professor searches for "portable projector" and finds one in their department (SR-01).
3.  Professor creates a borrow request for next Tuesday (RW-01, RW-02).
4.  System routes request to the Professor's Department Administrator (RW-03).
5.  Department Administrator reviews and approves the request (RW-04).
6.  System emails Professor (confirmation) and the department's Inventory Administrator (task assignment) (SI-02).
7.  Inventory Administrator prepares the projector and updates its status in UUIS (AM-02).
8.  After the event, the Professor returns the projector, and the Inventory Administrator marks it as available (AM-03).