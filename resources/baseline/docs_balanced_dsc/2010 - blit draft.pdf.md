# Software Requirements Specification (SRS)
## Laboratory Information System (LIS) Core Rewrite
**Document Version:** 1.0
**Date:** [Date of Creation]
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the rewrite of the core Laboratory Information System (LIS). The primary purpose is to establish a clear, comprehensive, and agreed-upon foundation for system development, ensuring the final product improves performance, ensures integrity, complies with regulations, and addresses critical user burdens.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Priority:** Implied by the project's focus on critical enhancements. All listed requirements are considered high priority unless otherwise noted in future revisions.
*   **Keywords:** **Shall** indicates a mandatory requirement. **Should** indicates a desirable but not mandatory feature.

#### 1.3 Project Scope
This project encompasses the architectural redesign and targeted enhancement of the existing LIS core. The scope is explicitly limited to:
*   **In-Scope:**
    *   Performance improvements to the core application and database.
    *   Architectural refactoring for improved maintainability and scalability.
    *   Implementation of a comprehensive, context-sensitive help system.
    *   Enhancement of user management, including templated user creation.
    *   Enforcement of coding standards, logging frameworks, and code review processes.
    *   Ensuring all new and modified functionality complies with HIPAA and FDA regulations.
    *   Maintaining all existing core LIS functionalities (e.g., sample tracking, test result management, reporting).
*   **Out-of-Scope:**
    *   Addition of major new laboratory testing modules not in the current system.
    *   Complete UI overhaul beyond necessary changes for new features and usability fixes.
    *   Any requirement not explicitly documented in this SRS or a subsequent, approved change request.

#### 1.4 References
*   Project Charter: "Balanced Summary - LIS Core Rewrite"
*   HIPAA Security and Privacy Rules
*   Relevant FDA 21 CFR Part 11 Guidance (if applicable)
*   Company Active Directory Schema Documentation

### 2. Overall Description

#### 2.1 Product Perspective
The new LIS is a successor to the existing system. It will operate within the same ecosystem, integrating with:
*   **Active Directory (External System):** For user authentication and status validation.
*   **Legacy Database:** Data migration from the existing LIS database is implied.
*   **Laboratory Instruments (Implicit):** The core system must maintain existing interfaces.

#### 2.2 User Classes and Characteristics
| User Class | Description | Key Characteristics |
| :--- | :--- | :--- |
| **System Administrator** | Manages system users, roles, and templates. | High technical proficiency, understands organizational roles and security policies. |
| **General System User** | All other LIS users (Lab Technicians, Pathologists, etc.). | Varied computer literacy, primary focus is on laboratory workflow tasks. |
| **Development Team** | Software engineers and programmer analysts building the system. | Technical experts in the chosen stack, require clear standards and processes. |
| **QA/QC Team** | Quality Assurance and Quality Control analysts. | Focus on test procedures, regression testing, and validation. |
| **Technical Lead** | Oversees code quality and architecture. | Responsible for technical decisions and code review. |
| **Project Stakeholders** | CIO, IT Manager, Sr. Business Analyst. | Provide business direction, approve features, and review usability. |
| **Technical Writer** | Creates user-facing documentation and help content. | Requires access to the system and clear specifications for help topics. |

#### 2.3 Operating Environment
*   **Software:** Windows Server environment, .NET Framework (or similar, TBD), relational database (e.g., SQL Server).
*   **Hardware:** To be determined based on performance requirements and new architecture.
*   **Network:** Must operate securely on the company intranet, with access to Active Directory services.

#### 2.4 Design and Implementation Constraints
1.  **Regulatory:** Must comply with HIPAA security and privacy standards. FDA compliance (21 CFR Part 11) must be retained for relevant functions.
2.  **Technical:** Must integrate with the company's Active Directory for user validation.
3.  **Process:** All production deployments must occur during scheduled weekly maintenance windows.
4.  **Procedural:** All code must adhere to defined coding standards and undergo review before commit.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** The existing core LIS functionality is well-understood and can be successfully replicated in the new architecture.
*   **Assumption:** "Reasonable time" for UI adjustments and UAT will be defined during the project planning phase.
*   **Dependency:** User validation is dependent on the availability and schema of the corporate Active Directory.
*   **Dependency:** The selection of specific open-source frameworks (logging, UI, etc.) will be made during the design phase and documented in a separate Technical Design Document.

### 3. System Features and Requirements

#### 3.1 User Management Module
**3.1.1 Description**
This module allows authorized administrators to create, manage, and validate system users by leveraging role-based access control (RBAC) and user templates for efficiency.

**3.1.2 Functional Requirements**
*   `FR-101`: The system shall allow an Administrator to create a new user account by manually entering UserName, DisplayName, and selecting Division and one or more Roles.
*   `FR-102`: The system shall allow an Administrator to create a new user account by selecting a pre-defined **User Template**, which automatically applies a set of predefined Roles and DefaultSettings.
*   `FR-103`: Upon entry of a new UserName, the system shall check for duplicates against existing users in the LIS database and prevent creation if a duplicate exists.
*   `FR-104`: Upon entry of a new UserName, the system shall verify the user's active status against the corporate Active Directory. Creation shall be prevented if the user is not found or is inactive in AD.
*   `FR-105`: The system shall persist all validated user information, including Role and Division associations, to the system database upon administrator confirmation.
*   `FR-106`: The system shall provide an interface for Administrators to create, modify, and delete User Templates, defining their TemplateName, PredefinedRoles, and DefaultSettings.

#### 3.2 Help System Module
**3.2.1 Description**
An integrated, context-sensitive help system accessible from any screen within the LIS application.

**3.2.2 Functional Requirements**
*   `FR-201`: Every screen in the LIS application shall display a consistent "Help" link or button.
*   `FR-202`: When a user activates the Help control, the system shall open a help window.
*   `FR-203`: The help window shall provide navigation features (Table of Contents, Index).
*   `FR-204`: The help window shall provide a full-text search capability across help content.
*   `FR-205`: The help window shall include a glossary of key terms used within the LIS.
*   `FR-206`: The help system content shall be maintainable by the Technical Writer via a defined process without requiring code deployment.

#### 3.3 Development Process & System Management
**3.3.1 Description**
Requirements governing the internal development lifecycle, code quality, and system operations.

**3.3.2 Functional Requirements**
*   `FR-301`: The development team shall write all code according to a formally defined and documented set of coding standards.
*   `FR-302`: All code changes shall be reviewed and approved by the Technical Lead (or designee) before being committed to the main source control branch.
*   `FR-303`: The system shall integrate with an external logging framework (e.g., log4net, NLog).
*   `FR-304`: The system shall log all errors, warnings, and significant informational events (e.g., user login, critical data changes) to an external log file or system. Each log entry shall include Timestamp, Severity, Message, and associated UserID (if applicable).
*   `FR-305`: The development team shall produce integrated builds and deploy them to a Staging environment on a weekly schedule.
*   `FR-306`: The QA/QC team shall perform full regression testing on each build deployed to the Staging environment.
*   `FR-307`: The QA/QC team shall perform User Acceptance Testing (UAT) on release candidates prior to production deployment.
*   `FR-308`: Production deployments shall only occur after formal sign-off by the Technical Owner and must be executed during the scheduled weekly maintenance window.
*   `FR-309`: Project stakeholders shall be presented with UI mockups for new or modified interfaces early in the development cycle for feedback.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   The UI shall be consistent with the existing LIS look-and-feel unless modified for new features.
*   UI mockups for new features shall be created and reviewed as per `FR-309`.
*   All screens shall include access to the context-sensitive help system as per `FR-201`.

#### 4.2 Hardware Interfaces
*   (To be detailed during design phase. Assumes standard server-client architecture.)

#### 4.3 Software Interfaces
*   **Active Directory:** The system shall interface via LDAP or a similar protocol to validate user status (see `FR-104`).
*   **Logging Framework:** The system shall integrate with a chosen external logging framework (see `FR-303`).

#### 4.4 Communications Interfaces
*   Standard HTTP/HTTPS for web-based client communication (assumed).
*   Secure, authenticated protocols for any inter-service communication within the new architecture.

### 5. Non-Functional Requirements

#### 5.1 Usability
*   `NFR-501`: UI changes and new screens shall be demonstrated to stakeholders during the development phase, with a planned, reasonable allowance for adjustment based on feedback.

#### 5.2 Reliability
*   `NFR-502`: Updates to the production system shall be restricted to scheduled weekly maintenance windows to minimize operational disruption.

#### 5.3 Maintainability
*   `NFR-503`: All application errors and significant system events shall be logged externally as per `FR-304`.
*   `NFR-504`: The codebase shall be developed following defined coding standards (`FR-301`) to ensure consistency and ease of future maintenance.

#### 5.4 Supportability
*   `NFR-505`: Development shall utilize an external, configurable logging framework (`FR-303`).

#### 5.5 Compliance
*   `NFR-506`: The system shall retain all existing HIPAA compliance capabilities. All new and modified functionality shall be designed and implemented to extend HIPAA compliance (e.g., audit logging, access controls, data integrity).

#### 5.6 Performance
*   `NFR-507`: Appropriate performance testing shall be conducted. User Acceptance Testing (`FR-307`) must be successfully completed before any production release.

### 6. Data Model
Key domain entities and their attributes, as identified:
```plaintext
User
  PK UserID: int
  UserName: varchar (Unique, ties to AD)
  DisplayName: varchar
  Status: enum (Active/Inactive)
  RoleAssociations: collection(Role)
  Division: Division

Role
  PK RoleID: int
  RoleName: varchar
  Permissions: collection(Permission)
  Description: text

Division
  PK DivisionID: int
  DivisionName: varchar
  Code: varchar
  LabLocation: varchar

UserTemplate
  PK TemplateID: int
  TemplateName: varchar
  PredefinedRoles: collection(Role)
  DefaultSettings: key-value pairs

SystemLog
  PK LogID: bigint
  Timestamp: datetime
  Severity: enum (Error, Warning, Info)
  Message: text
  UserID: int (FK, nullable)

HelpTopic
  PK TopicID: int
  Title: varchar
  Content: text (or HTML)
  Keywords: collection(varchar)
  Category: varchar
```
*(Note: This is a conceptual model. A detailed physical data model will be created during the design phase.)*

### 7. Appendices

#### Appendix A: Glossary
*   **LIS:** Laboratory Information System.
*   **HIPAA:** Health Insurance Portability and Accountability Act.
*   **UAT:** User Acceptance Testing.
*   **FRS:** Functional Requirements Specification (this document).
*   **SME:** Subject Matter Expert.
*   **RBAC:** Role-Based Access Control.

#### Appendix B: Undecided Issues (TBD)
1.  Specific list and severity of critical functional issues from the legacy system to be addressed.
2.  Detailed module breakdown and development sequence/priority.
3.  Finalized schedule for Requirements Gathering and Validation sessions.
4.  Exact definition of "reasonable time" for UI adjustments and UAT.
5.  Specific open-source frameworks to be utilized (logging, UI components, etc.).
6.  Detailed content and structure of the help system glossary.

#### Appendix C: Risks and Mitigation
| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| Scope creep from undocumented requests. | Medium | High | Adhere strictly to this SRS; all undocumented requests require a formal change control process. |
| Integration issues during weekly builds. | Medium | Medium | Implement a disciplined source control branching, labeling, and automated build process. |
| Insufficient time for UAT. | Medium | High | Explicitly plan and allocate time for UAT in the project schedule; treat it as a non-negotiable milestone. |
| New code breaks existing functionality. | High | High | Mandate comprehensive regression testing (`FR-306`) for all scheduled builds. |
| Non-compliance with HIPAA regulations. | Low | Critical | Involve compliance experts in design reviews; conduct security-specific testing. |

---
**Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Business & Technical Owner (CIO) | | | |
| Sr. Business Systems Analyst | | | |
| IT Manager (QA/QC & Implementation) | | | |
| Technical Lead | | | |