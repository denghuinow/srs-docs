# Software Requirements Specification (SRS)
## Laboratory Information System (LIS) Rewrite Project
**Document Version:** 1.0  
**Date:** [Current Date]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the rewrite of the core Laboratory Information System (LIS). The primary purpose is to serve as a definitive guide for the development team, project managers, and stakeholders, ensuring a common understanding of the system to be built. It will be used as the basis for design, development, testing, and project verification.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Keywords:** "Shall" indicates a mandatory requirement. "Should" indicates a desirable but not mandatory feature.
*   **Formatting:** Code and database elements are presented in `inline code` blocks. Important notes are called out in **bold**.

#### 1.3 Intended Audience and Reading Suggestions
*   **Project Sponsors & Stakeholders:** Focus on Sections 1 (Introduction), 2 (Overall Description), and 5 (Key Constraints).
*   **Project Managers:** The entire document, with emphasis on scope, features, and constraints.
*   **Development & QA Teams:** The entire document, with detailed focus on Sections 3 (System Features) and 4 (External Interface Requirements).
*   **System Administrators & DBAs:** Focus on Sections 4.2 (Hardware Interfaces), 4.3 (Software Interfaces), and 5 (Non-Functional Requirements).

#### 1.4 Project Scope
The project entails a full rewrite of the core LIS application layer. The scope includes:
*   Re-architecting and re-coding the application logic to improve performance and maintainability.
*   Implementing new workflow automation and decision-support logic.
*   Maintaining 100% of the existing business functionality and data model as presented to the end-user.
*   Developing new administrative modules for user/role management and context-sensitive help.
*   Ensuring the new system interfaces exclusively with the **existing SQL Server 2008 database**.
*   Guaranteeing full compliance with HIPAA security and privacy standards.

**Out of Scope:**
*   Modifying the underlying SQL Server 2008 database schema or version.
*   Creating new external system interfaces (HL7, instruments, etc.) beyond what currently exists.
*   Changes to the physical server infrastructure (though performance improvements may influence future recommendations).

#### 1.5 References
*   HIPAA Security Rule (45 CFR Part 160 and Subparts A and C of Part 164)
*   HIPAA Privacy Rule (45 CFR Part 160 and Subparts A and E of Part 164)
*   Existing LIS Functional Specification Documents
*   SQL Server 2008 Database Schema Documentation

### 2. Overall Description

#### 2.1 Product Perspective
The new LIS is a standalone, client-server application that replaces the legacy LIS front-end and application layer. It is a component within the larger laboratory ecosystem, interacting with the persistent SQL Server 2008 database and, indirectly through existing interfaces, with laboratory instruments and hospital information systems (HIS).

#### 2.2 Product Functions
The core functions of the product are:
1.  Provide a high-performance, secure user interface for all laboratory workflows (accessioning, testing, review, reporting).
2.  Automate laboratory decisions and streamline manual processes through configurable business rules.
3.  Administer system users, roles, and permissions centrally.
4.  Deliver integrated, context-sensitive help to users.
5.  Maintain all legacy functionality for order management, result entry, quality control, and reporting.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Requirements |
| :--- | :--- | :--- |
| **Laboratory Technologist** | Primary end-user. Performs testing, reviews results. Needs efficient, task-oriented screens. | Performance, intuitive workflow, context-sensitive help. |
| **Pathologist/Lab Director** | Reviews and verifies complex results. Makes diagnostic decisions. | Advanced data visualization, audit trails, decision support alerts. |
| **Laboratory Administrator** | Manages users, configures test catalogs, runs operational reports. | Administrative tools, role-based security. |
| **System Administrator** | Installs software, manages application servers, monitors logs. | Deployment support, diagnostic tools. |
| **Patient** (Indirect) | Subject of data. No direct system access. | Privacy and security of Protected Health Information (PHI). |

#### 2.4 Operating Environment
*   **Application Server:** Windows Server 2012 R2 or later.
*   **Database Server:** Microsoft SQL Server 2008 (Existing instance).
*   **Client Workstation:** Windows 10/11 with a modern web browser (Chrome, Edge, Firefox) or a dedicated .NET client (to be determined).
*   **Network:** Secure hospital intranet, 1 Gbps LAN recommended.

#### 2.5 Design and Implementation Constraints
1.  **Database Constraint:** The application **must** operate with the existing SQL Server 2008 database. Schema changes are prohibited.
2.  **Regulatory Constraint:** The system **shall** be designed and implemented in full compliance with HIPAA regulations.
3.  **Deployment Constraint:** All updates to the production environment **must** be deployable within the scheduled Tuesday maintenance windows.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** The existing SQL Server 2008 database will remain stable and supported for the lifespan of the rewritten application.
*   **Assumption:** Sufficient server hardware is available to host the new application layer.
*   **Dependency:** Successful deployment depends on coordination with the IT department for maintenance window access.

### 3. System Features

#### 3.1 Feature: User and Role Administration
**Description:** A centralized module for creating, modifying, disabling, and deleting user accounts and assigning system roles/permissions.

**Sub-Features & Requirements:**
*   `FR-101`: The system shall allow administrators to create user accounts with at least the following attributes: Username, Full Name, Email, Department, and Status (Active/Inactive).
*   `FR-102`: The system shall provide a role-based access control (RBAC) model. Permissions shall be assigned to roles, and roles shall be assigned to users.
*   `FR-103`: The system shall include pre-defined roles (e.g., Technologist, Pathologist, Admin) with configurable permission sets.
*   `FR-104`: The system shall maintain a complete audit log of all user account and role modifications (who, what, when).

#### 3.2 Feature: Context-Sensitive Online Help
**Description:** Integrated help system that provides relevant documentation based on the user's current page or selected UI element.

**Sub-Features & Requirements:**
*   `FR-201`: The system shall provide a persistent "Help" button or icon within the application interface.
*   `FR-202`: When the Help function is activated, the system shall display documentation relevant to the current active window, screen, or data field.
*   `FR-203`: The system shall include a searchable knowledge base of help articles.
*   `FR-204`: Help content shall be maintainable without requiring a full code deployment.

#### 3.3 Feature: Core Laboratory Workflow Engine
**Description:** The rewritten core system that performs all existing LIS functions with improved performance and automated workflows.

**Sub-Features & Requirements:**
*   `FR-301`: The system shall provide all order entry, specimen tracking, result entry, and reporting functions present in the legacy system.
*   `FR-302`: The system shall implement configurable business rules to automate tasks such as reflex testing, critical value alerting, and delta checking.
*   `FR-303`: The system shall streamline manual data entry through features like default values, pick-lists, and auto-completion.
*   `FR-304`: All screen response times for core transactions shall meet the performance criteria defined in `NFR-401`.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   The primary UI shall be a modern, web-based interface compatible with specified browsers.
*   The UI shall be responsive and accessible, following WCAG 2.1 Level AA guidelines.
*   All data entry forms shall maintain functional parity with the legacy system.

#### 4.2 Hardware Interfaces
*   The application shall support standard laboratory peripherals (barcode scanners, label printers) via standard Windows drivers and emulation.

#### 4.3 Software Interfaces
*   **Database:** The system shall connect to the existing `LIS_PROD` SQL Server 2008 instance using a trusted Windows authentication or SQL authentication connection string.
    ```tns
    Server=sql08-lis.prod.hospital.org;Database=LIS_PROD;Trusted_Connection=True;
    ```
*   **Legacy Interfaces:** The system shall not disrupt existing interface engines (e.g., HL7 listeners, instrument middleware) that read from/write to the database.

#### 4.4 Communications Interfaces
*   All client-server communication shall occur over HTTPS/TLS 1.2 or higher within the hospital network.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-401`: **Screen Load Time:** 95% of all interactive screens shall load in less than 2 seconds under normal load.
*   `NFR-402`: **Transaction Response Time:** 95% of database transactions (e.g., save result, search order) shall complete in less than 1 second.
*   `NFR-403`: **Concurrent Users:** The system shall support up to 250 concurrent active users without significant degradation in performance.

#### 5.2 Safety & Security Requirements
*   `NFR-501`: **HIPAA Compliance:** The system shall enforce access controls, maintain audit trails of all PHI access/modification, and ensure data integrity and confidentiality per HIPAA regulations.
*   `NFR-502`: **Authentication:** All users shall be required to authenticate with a unique username and password (meeting organizational complexity standards).
*   `NFR-503`: **Session Management:** Inactive sessions shall timeout after a maximum of 15 minutes, requiring re-authentication.
*   `NFR-504`: **Data Encryption:** PHI shall be encrypted in transit (TLS) and at rest within the application (e.g., sensitive fields, audit logs).

#### 5.3 Software Quality Attributes
*   **Maintainability:** The codebase shall be modular, well-documented, and developed using standard design patterns to facilitate future updates.
*   **Reliability:** The system shall achieve 99.5% uptime during scheduled operational hours, excluding planned maintenance.
*   **Availability:** Deployment and rollback procedures must be designed to fit within the Tuesday maintenance window constraint (`NFR-601`).

#### 5.4 Operational & Deployment Constraints
*   `NFR-601`: **Deployment Window:** The entire process for deploying an update to production—including final backup, deployment, verification, and rollback preparation—must be designed to complete within a 4-hour scheduled Tuesday maintenance window.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| QA Manager | | | |
| System Owner | | | |