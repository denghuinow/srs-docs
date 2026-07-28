# Software Requirements Specification (SRS)
## Laboratory Information System (LIS) Rewrite
**Document Version:** 1.0  
**Date:** [Date of Creation]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the rewrite of the core Laboratory Information System (LIS). It serves as a formal agreement between stakeholders and the development team, providing a comprehensive blueprint for the project's scope, features, constraints, and interfaces.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Keywords:** "Shall" indicates a mandatory requirement. "Should" indicates a desirable but not mandatory feature.
*   **Formatting:** User interface elements are denoted in *italics*. System actions or responses are in **bold**.

#### 1.3 Project Scope
This project involves a strategic rewrite of the core LIS application to achieve the following objectives:
*   **Improve Performance:** Address latency and sluggishness in user-facing operations and batch processes.
*   **Ensure System Integrity:** Resolve critical defects that compromise data accuracy or workflow stability.
*   **Streamline Workflows:** Implement targeted enhancements to reduce user burden and improve efficiency.
*   **Modernize Architecture:** Implement a sustainable technical foundation to support future business growth and integration needs.

**In-Scope:**
*   Rewrite of core application modules, starting with the Admin module.
*   Implementation of validated critical defect fixes and enhancements.
*   Architectural improvements for performance, security, and maintainability.
*   Maintenance of all existing, validated core functionalities.

**Out-of-Scope (Non-Goals):**
*   Implementation of new, undocumented features or requirements.
*   Modification of functionalities not directly related to validated critical issues.
*   Complete overhaul of all legacy interfaces in the initial phase.

#### 1.4 References
*   Project Charter: LIS Rewrite Initiative
*   Existing LIS System Documentation
*   HIPAA Security and Privacy Rules

### 2. Overall Description

#### 2.1 Product Perspective
The new LIS is a standalone, web-based application that will replace the existing legacy system. It will integrate with several external systems to form a complete laboratory ecosystem.

#### 2.2 User Classes and Characteristics
| User Class | Description | Key Characteristics |
| :--- | :--- | :--- |
| **System Administrator** | Manages system configuration, user accounts, and security. | Technical proficiency, requires full system access. |
| **Laboratory Manager** | Oversees lab operations, reviews reports, manages workflows. | Needs comprehensive data access and reporting tools. |
| **Lab Technician** | Performs primary data entry, sample processing, and result validation. | Requires efficient, task-oriented interfaces. |
| **Pathologist/Reviewer** | Reviews and approves sensitive results (e.g., histology, cytology). | Needs specialized workflows and high-resolution image viewing. |
| **Client Services** | Handles client inquiries and provides result status updates. | Requires read-only access to client-specific data. |

#### 2.3 Operating Environment
*   **Software:** Windows Server OS, Microsoft SQL Server, .NET Core Runtime, IIS Web Server.
*   **Hardware:** Standard enterprise server infrastructure with load balancing capabilities.
*   **Client:** Modern web browsers (Chrome, Edge, Firefox latest stable versions).

#### 2.4 Design and Implementation Constraints
1.  The system must maintain backward compatibility with existing data schemas during migration.
2.  All new code must adhere to the organization's defined security and coding standards.
3.  The user interface must be responsive and accessible according to WCAG 2.1 Level AA guidelines.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** Active Directory will remain the primary source of user identity.
*   **Dependency:** Successful integration with the existing SQL Server database is critical.
*   **Assumption:** Business stakeholders will be available for timely User Acceptance Testing (UAT).

### 3. System Features and Requirements

#### 3.1 Admin Module: User Management
**3.1.1 Description**
This feature allows authorized administrators to create, modify, and manage user accounts within the LIS, associating them with appropriate roles, divisions, and lab locations.

**3.1.2 Functional Requirements**
*   `FR-101`: The system shall provide a *User Management* page within the Admin module.
*   `FR-102`: The system shall allow an admin to initiate a new user creation via an *Add User* button.
*   `FR-103`: Upon initiation, the system shall display a user creation form with the following required fields: *User Name*, *Display Name*.
*   `FR-104`: The system shall provide selection controls for assigning at least one **Role**, one **Division**, and one **Lab Location** to the new user.
*   `FR-105`: Before saving, the system shall validate that the provided *User Name* does not already exist as an active record in the LIS database.
*   `FR-106`: Before saving, the system shall validate that the provided *User Name* corresponds to an active account in the integrated Active Directory service.
*   `FR-107`: If validation fails (duplicate user or inactive in AD), the system shall display a clear error message and prevent the save operation.
*   `FR-108`: Upon successful validation and save, the system shall persist the new User record and all associated Role, Division, and Location mappings to the database.
*   `FR-109`: Upon successful save, the system shall display a confirmation message to the admin.
*   `FR-110`: The admin shall be able to cancel the operation at any point during data entry using a *Cancel* button, which clears the form and returns to the main User Management page.
*   `FR-111`: The system shall allow an admin to create a user from a pre-defined template, auto-populating the form with default roles and settings from that template.

**3.1.3 Business Process Flow**
```
1.  Admin navigates to Admin Module -> User Management.
2.  Admin clicks 'Add User'.
3.  System displays blank user form.
4.  Admin enters User Name, Display Name.
5.  Admin selects Role(s), Division(s), Lab Location(s).
6.  Admin clicks 'Save'.
7.  System validates against LIS DB (no duplicate) and AD (is active).
    a. If validation FAILS: Show error. Return to Step 4.
    b. If validation PASSES: Proceed to Step 8.
8.  System saves user and associations.
9.  System displays success confirmation.
```

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   The application shall present a modern, consistent, and intuitive web-based interface.
*   All data entry forms shall provide clear validation messages inline or upon submission.
*   A context-sensitive online help system shall be accessible via a `(?)` icon on every screen.

#### 4.2 Hardware Interfaces
None specified beyond standard server-client web interaction.

#### 4.3 Software Interfaces
| Interface Name | Direction | Purpose | Data Format | SLA / Performance Requirement |
| :--- | :--- | :--- | :--- | :--- |
| **Active Directory** | Outbound | User authentication and status verification. | LDAP queries / responses. | Response time < 2 seconds per validation. |
| **SQL Server Database** | Bi-directional | Primary data persistence for all system entities. | T-SQL / Result sets. | 99.9% availability during business hours (8 AM - 6 PM). |
| **Corporate Email System (SMTP)** | Outbound | Notification of system errors to support staff. | SMTP protocol. | Email dispatched within 5 minutes of error event. |
| **Online Help System** | Integrated | Serve context-sensitive help content. | Internal API call / HTML content. | Help page load time < 3 seconds. |

#### 4.4 Communications Interfaces
*   The application shall use HTTPS (TLS 1.2 or higher) for all client-server communication.
*   Internal service-to-service communication (e.g., to database) shall occur over secure channels.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-201`: Critical user-facing web pages (like User Management) shall have a response time of under 3 seconds for 95% of transactions under normal load.
*   `NFR-202`: Batch processes (e.g., nightly reports) must complete within their defined time windows.

#### 5.2 Safety Requirements
Not applicable for this software system.

#### 5.3 Security & Compliance Requirements
*   `NFR-301`: The system shall maintain full compliance with HIPAA regulations for electronic Protected Health Information (ePHI) concerning data security, privacy, and confidentiality.
*   `NFR-302`: All user access shall be controlled via role-based permissions.
*   `NFR-303`: All authentication events and critical data modifications (create, update, delete of user records) shall be logged in an audit trail.

#### 5.4 Software Quality Attributes
*   **Reliability:** `NFR-401`: The system shall have a target operational availability of 99.5%. Scheduled maintenance is confined to pre-defined windows (e.g., Tuesdays, 7:00 PM to 7:00 AM).
*   **Observability:** `NFR-402`: All application errors, warnings, and informational messages shall be logged to an external, centralized application log file with appropriate severity levels (Error, Warning, Info).
*   **Maintainability:** The codebase shall be structured with clear separation of concerns to facilitate future updates and bug fixes.

### 6. Data Model
The core entities and their relationships for the User Management feature are defined below. This is a subset of the complete system domain model.

```yaml
User:
  attributes:
    UserID: integer, required, unique, primary key
    UserName: string, required, unique (maps to AD)
    DisplayName: string, required
    Status: enum (Active, Inactive)

Role:
  attributes:
    RoleID: integer, required, unique, primary key
    RoleName: string, required
    Permissions: collection

Division:
  attributes:
    DivisionID: integer, required, unique, primary key
    DivisionName: string, required

LabLocation:
  attributes:
    LocationID: integer, required, unique, primary key
    LocationCode: string, required
    Address: string

# Association Entities
UserRole:
  attributes:
    UserID: integer, foreign key to User.UserID
    RoleID: integer, foreign key to Role.RoleID

UserDivision:
  attributes:
    UserID: integer, foreign key to User.UserID
    DivisionID: integer, foreign key to Division.DivisionID
```

### 7. Acceptance Criteria
The following scenarios must be successfully demonstrated for the User Management feature to be accepted.

**AC-1: Successful User Creation**
*   **Given** an authenticated user with Administrator privileges,
*   **When** they navigate to the User Management page, complete the *Add User* form with valid and unique data, assign at least one Role, Division, and Lab Location, and click *Save*,
*   **Then** a new user record is created in the database with all associated mappings, and a success message is displayed.

**AC-2: Duplicate User Validation**
*   **Given** an admin is creating a new user with a *User Name* that already exists in the LIS,
*   **When** they attempt to save the form,
*   **Then** the system displays a clear error message (e.g., "User '[UserName]' already exists.") and does not save the record.

**AC-3: Mandatory Field Validation**
*   **Given** an admin is creating a new user and has left a required field (e.g., *Display Name*) blank,
*   **When** they attempt to save the record,
*   **Then** the system highlights the missing field(s) with an error message and prevents the save operation until all required fields are completed.

**AC-4: Create User from Template**
*   **Given** an admin user and a pre-defined user template "Standard Technician" with specific role and setting defaults,
*   **When** the admin selects "Create from Template > Standard Technician",
*   **Then** the new user form is auto-populated with the default roles and settings from that template.

### 8. Project Management Appendices

#### 8.1 Stakeholder Matrix
| Role | Name/Title | Responsibility |
| :--- | :--- | :--- |
| **CIO / Business & Technical Owner** | [To be assigned] | Final approver; overall business and technical ownership. |
| **IT Manager (QA/QC & Implementation)** | [To be assigned] | Oversees QA, QC, and implementation activities. |
| **Programmer Analyst / Project Manager** | [To be assigned] | Manages project development; provides SME guidance. |
| **Sr. Business Systems Analyst** | [To be assigned] | Leads requirements analysis, documentation, and validation. |
| **QA Analyst** | [To be assigned] | Executes test plans (functional, regression, UAT support). |
| **Technical Writer** | [To be assigned] | Creates user manuals and online help content. |

#### 8.2 Milestones and Release Strategy
1.  **M1:** SRS Sign-off & Requirements Baseline Frozen.
2.  **M2:** Admin Module Development & Internal QA Complete.
3.  **M3:** Successful UAT for Release Bundle 1 (Admin + Critical Fixes).
4.  **M4:** Technical/Production Deployment Sign-off.
5.  **M5:** **Release 1.0 to Production** (Admin Module & Priority Fixes).
6.  **M6-Mx:** Iterative development, testing, and release of remaining modules.

#### 8.3 Risk Register
| Risk | Probability | Impact | Mitigation Strategy | Owner |
| :--- | :--- | :--- | :--- | :--- |
| Scope Creep | Medium | High | Strict change control process. All changes require formal CR and stakeholder approval. | Project Manager |
| Active Directory Integration Issues | Medium | High | Early prototyping and testing of the AD interface during the design phase. | Technical Lead |
| Insufficient UAT Time | High | Medium | Involve business UAT representatives early; allocate a dedicated, protected UAT period in the schedule. | IT Manager |
| Performance Degradation | Medium | High | Establish performance benchmarks early; integrate load/stress testing into the QA cycle. | QA Manager / Tech Lead |

#### 8.4 Open Issues / TBD
| Issue | Description | Responsible Party | Due Date |
| :--- | :--- | :--- | :--- |
| **TBD-01** | Final list of all application modules to be included in the rewrite. | CIO / Project Manager | [Date] |
| **TBD-02** | Detailed definition of "Critical" severity for defects/enhancements. | Business Owner / Sr. BA | [Date] |
| **TBD-03** | Specific performance benchmarks (load, concurrent users) for each module. | Technical Lead / QA Manager | [Date] |
| **TBD-04** | Complete inventory and specification of all legacy system interfaces. | Technical Lead / Dev Team | [Date] |

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Business Owner | | | |
| Technical Owner | | | |
| Project Manager | | | |
| Sr. Business Analyst | | | |