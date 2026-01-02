# Software Requirements Specification (SRS)
## Laboratory Information System (LIS) Core Rewrite
**Document Version:** 1.0
**Date:** [Current Date]
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the rewrite of the core Laboratory Information System (LIS). The primary purpose of this project is to improve system performance, ensure long-term integrity, and remediate critical defects, while preserving all existing core functionalities. This document serves as a comprehensive guide for stakeholders, developers, testers, and project managers throughout the system development lifecycle.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are prefixed with `FR`, non-functional with `NFR`, and constraints with `CON`.
*   **Priority:** `(H)` High, `(M)` Medium, `(L)` Low.
*   **Keywords:** `MUST`, `SHALL`, `WILL` indicate mandatory requirements. `SHOULD`, `MAY` indicate desirable but optional features.

#### 1.3 Project Scope
The scope of this project is strictly limited to the foundational rewrite of the LIS core and the implementation of three specified new core functions. All existing business logic for laboratory operations (e.g., test ordering, specimen tracking, result entry, reporting) **MUST** be retained and integrated into the new architecture. The project **SHALL NOT** introduce new laboratory workflows or business features beyond those explicitly listed in this document.

**In-Scope:**
*   Refactoring of the existing application codebase into a new .NET 3.5 architecture.
*   Implementation of a new user and role administration module.
*   Implementation of a centralized application logging framework.
*   Implementation of a context-sensitive online help system.
*   Performance optimization of database interactions and key user interfaces.
*   Remediation of all critical and high-priority defects from the legacy system.
*   Ensuring HIPAA compliance in the new codebase.

**Out-of-Scope:**
*   Development of new laboratory workflow features.
*   Modifications to the underlying business rules of the retained functionalities.
*   Upgrades to newer versions of the .NET framework or SQL Server.
*   Creation of mobile applications or external APIs.

#### 1.4 References
*   HIPAA Security Rule (45 CFR Part 160 and Part 164, Subparts A and C)
*   Legacy LIS Functional Specification
*   Legacy LIS Defect Log

### 2. Overall Description

#### 2.1 Product Perspective
The rewritten LIS is a standalone, client-server application. It will replace the existing LIS module-for-module. It interfaces with a single SQL Server 2008 database, which contains all laboratory and system data. The system must operate within the existing IT infrastructure of the laboratory.

#### 2.2 Product Functions (Summary)
1.  **Retained Functions:** All core LIS functions for managing patients, orders, specimens, tests, results, and reports.
2.  **New Core Functions:**
    *   System User and Role Administration.
    *   Application-wide logging to external files.
    *   Integrated, screen-specific online help.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Requirements |
| :--- | :--- | :--- |
| **System Administrator** | Technical staff, manages system access. | `FR-010`, `FR-011`, `FR-012`. Must have full control over user lifecycle and role permissions. |
| **Laboratory Manager/Supervisor** | Administrative staff, oversees lab operations. | May have elevated privileges for data review and audit functions within retained modules. |
| **General Laboratory User** (Technologist, Phlebotomist, Clerk) | Primary end-users, perform daily LIS tasks. | Access to all retained workflow modules. Requires intuitive UI and accessible help (`FR-030`). |

#### 2.4 Operating Environment
*   **Software Platform:** Microsoft .NET Framework 3.5
*   **Database:** Microsoft SQL Server 2008
*   **Client OS:** Windows 7/10/11 (as supported by .NET 3.5)
*   **Server OS:** Windows Server 2008 R2 or later

#### 2.5 Design and Implementation Constraints
*   `CON-001`: The application **MUST** be developed using the .NET Framework 3.5.
*   `CON-002`: The application **MUST** use a single SQL Server 2008 database instance.
*   `CON-003`: The system **MUST** be fully compliant with HIPAA standards for data security, privacy, and auditability.
*   `CON-004`: All updates to the production environment **MUST** be scheduled for Tuesdays between 19:00 (7pm) and 07:00 (7am) local server time.

#### 2.6 Assumptions and Dependencies
*   The existing SQL Server 2008 database schema will remain largely unchanged, with modifications only for new core functions.
*   The legacy system's data will be fully migratable to the new system.
*   Client workstations meet the minimum hardware requirements for running a .NET 3.5 Windows Forms or WPF application.

### 3. System Features and Requirements

#### 3.1 User and Role Administration
**Description:** This module allows authorized administrators to manage system access by creating users and assigning security roles.

**Priority:** High (H)

**Functional Requirements:**
*   `FR-010`: The system **SHALL** provide a secure interface, accessible only to users with the 'System Administrator' role, for managing user accounts.
*   `FR-011`: An administrator **SHALL** be able to create a new user account by providing at minimum: Username, Full Name, and initial Password. The password **MUST** adhere to a configurable complexity policy.
*   `FR-012`: An administrator **SHALL** be able to assign one or more pre-defined security roles (e.g., 'Technologist', 'Supervisor', 'Clerk', 'Administrator') to a user account. The permissions associated with each role are defined by the retained modules.
*   `FR-013`: The system **SHALL** log all user administration activities (create, modify, role assignment, deactivation) per `FR-020`.

#### 3.2 Application Logging
**Description:** A centralized service to record system events for monitoring, debugging, and audit purposes.

**Priority:** High (H)

**Functional Requirements:**
*   `FR-020`: The system **SHALL** log events to an external text-based file (e.g., .log, .txt). The log file location **SHALL** be configurable.
*   `FR-021`: Each log entry **SHALL** include: Timestamp, Log Level (Error, Warning, Info), Source Module/Class, User ID (if applicable), and a descriptive Message.
*   `FR-022`: The system **SHALL** support three primary log levels:
    *   **Error:** For system failures, exceptions, and critical issues.
    *   **Warning:** For unexpected but non-critical events.
    *   **Info:** For significant system actions (user login/logout, transaction completion).
*   `FR-023`: Logging calls **SHALL** be implemented in all major components, including the new administration module and all retained core modules.

#### 3.3 Online Help System
**Description:** Context-sensitive help accessible from any screen within the application.

**Priority:** Medium (M)

**Functional Requirements:**
*   `FR-030`: Every user screen (form) **SHALL** have a standardized 'Help' button or menu option (e.g., F1 key support).
*   `FR-031`: Activating help **SHALL** open a help viewer window displaying content specific to the active screen and, if possible, the focused control.
*   `FR-032`: Help content **SHALL** be stored externally (e.g., compiled HTML Help .chm file) to allow updates without code recompilation.

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
*   `NFR-001`: The system **SHALL** demonstrate a measurable improvement in performance over the legacy system. Key transaction screens (e.g., Result Entry, Order Search) **MUST** load within 2 seconds under typical load (50 concurrent users).
*   `NFR-002`: Database query performance for high-use transactions **SHALL** be optimized as part of the rewrite.

#### 4.2 Security and Compliance Requirements
*   `NFR-010`: The system **MUST** comply with all relevant HIPAA regulations. This includes:
    *   Access Controls (Unique user identification, role-based access, automatic logoff).
    *   Audit Controls (`FR-020`, `FR-023`).
    *   Integrity Controls (Protection against unauthorized data alteration).
    *   Transmission Security (if applicable).
*   `NFR-011`: All Protected Health Information (PHI) **MUST** be encrypted at rest in the database and in any log files.
*   `NFR-012`: User passwords **SHALL** be stored using strong, salted hashing algorithms.

#### 4.3 Reliability and Maintainability
*   `NFR-020`: The system **SHALL** achieve 99.5% uptime during core business hours (6:00 - 20:00).
*   `NFR-021`: The codebase **SHALL** be structured with clear separation of concerns to facilitate future maintenance.

#### 4.4 Deployment Constraints
*   `NFR-030`: The deployment process **MUST** respect `CON-004`. All installation/update packages **MUST** be designed for execution within the defined Tuesday maintenance window.

---
**Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| Quality Assurance Lead | | | |