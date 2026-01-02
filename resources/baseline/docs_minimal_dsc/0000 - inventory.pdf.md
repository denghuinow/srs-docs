# Software Requirements Specification (SRS)
## Unified University Asset Management System (UUAMS)

**Document Version:** 1.0  
**Date:** [Current Date]  
**Authors:** [System Analysts/Project Team]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Unified University Asset Management System (UUAMS). The primary purpose of this document is to provide a detailed description of the system's capabilities, interfaces, and performance characteristics. It serves as a contractual agreement between the stakeholders (university administration) and the development team, and will be the foundation for system design, implementation, and testing.

#### 1.2 Scope
The UUAMS will integrate disparate inventory databases from three distinct university faculties (e.g., Engineering, Sciences, Humanities) into a single, cohesive web-based application. The system's scope encompasses the complete lifecycle management of university assets, including but not limited to:
*   Physical assets (e.g., lab equipment, furniture, AV gear)
*   Spaces (e.g., classrooms, meeting rooms, labs)
*   Digital assets (e.g., software licenses)

Core in-scope functionalities include centralized tracking, inter-departmental transfer workflows, reservation/borrowing processes, and hierarchical permission management. The system will **not** handle financial procurement, payroll, human resource management, or student academic records.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **UUAMS** | Unified University Asset Management System |
| **Asset** | Any university-owned item, space, or license tracked by the system. |
| **Reservation** | A time-bound booking of a space or asset for future use. |
| **Borrow Request** | A request to take temporary custody of a portable asset. |
| **Transfer** | The formal change of custody or responsibility for an asset between organizational units. |
| **Administrator** | A user with elevated permissions (University, Faculty, Dept., IT). |
| **General User** | An end-user (student, professor) with basic privileges. |
| **Organizational Hierarchy** | The defined structure: University > Faculty > Department. |

#### 1.4 References
*   University IT Infrastructure Policy v3.1
*   ISO/IEC/IEEE 29148:2018 - Systems and software engineering — Life cycle processes — Requirements engineering
*   Legacy Faculty Inventory Database Schemas (Faculties A, B, C)

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its users, and operating environment. Section 3 details the specific functional requirements. Section 4 outlines all non-functional requirements, including performance, security, and constraints.

---

### 2. Overall Description

#### 2.1 Product Perspective
The UUAMS is a new, self-contained web application. It will act as a middleware layer and front-end, replacing the need for users to interact directly with three separate legacy database systems. It will interface with these existing faculty databases (via secure APIs or connectors) for data synchronization and with the university's central Active Directory/LDAP service for user authentication.

#### 2.2 Product Functions (High-Level)
1.  **Asset Management:** Provide a unified interface to Add, View, Edit, Modify status, and Transfer assets.
2.  **Request Management:** Enable users to create requests to borrow assets or reserve spaces, and allow authorized administrators to approve or deny these requests.
3.  **Permission Management:** Allow IT and University Administrators to define and modify user roles and permissions based on the university's organizational hierarchy.
4.  **Reporting & Dashboard:** Generate consolidated views, availability calendars, and audit logs.
5.  **System Administration:** Manage system configuration, data integration jobs, and user authentication.

#### 2.3 User Characteristics
| User Class | Skill Level | Key Responsibilities |
| :--- | :--- | :--- |
| **General User** (Student, Professor) | Basic computer literacy. Familiar with web browsers. | Browse available assets/spaces; create reservation/borrow requests; view own request history. |
| **Department Administrator** | Proficient with data entry and basic administrative tools. | Manage assets within their department; approve/reject requests from department members; initiate internal transfers. |
| **Faculty Administrator** | Advanced administrative skills. Understands faculty-level policy. | Oversee all departments within the faculty; approve cross-departmental transfers; generate faculty-level reports. |
| **University Administrator** | Strategic, system-wide oversight capability. | Configure university-wide policies; manage the organizational hierarchy; access all system data and reports. |
| **IT Administrator** | High technical expertise. | Manage system integration, user roles/authentication, system performance, backups, and platform constraints. |

#### 2.4 Constraints
1.  **Platform Compatibility:** The system must be deployable and fully functional on both Microsoft Windows Server and Unix-based (e.g., Linux) server platforms.
2.  **Availability:** System must maintain **99% availability during standard university working hours (07:00 - 19:00, Monday-Friday)**. Planned maintenance outside these hours is acceptable.
3.  **Security:** All users, without exception, must be authenticated via the university's central directory service before accessing any system functionality.
4.  **Performance:** Any database query generated by the system must be automatically terminated by the application layer if its execution time exceeds **60 seconds**, to prevent system resource exhaustion.
5.  **Legacy System Integration:** The design must accommodate the existing data models and limitations of the three faculty inventory databases without requiring major modifications to those systems.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** The university's central authentication service (e.g., Active Directory) will be available and provide necessary user attributes (e.g., group membership, department).
*   **Assumption:** Read/Write API access or database connectivity to the three legacy faculty systems is feasible and will be provided.
*   **Dependency:** The project timeline is dependent on receiving finalized data mapping specifications from each faculty.
*   **Dependency:** System deployment requires a supported Java/.NET/Python runtime environment and a relational database (e.g., PostgreSQL, SQL Server) as the unified master repository.

---

### 3. Specific Requirements

#### 3.1 External Interface Requirements
**3.1.1 User Interfaces**
*   **UI-01:** The system shall provide a responsive, role-based web interface accessible via modern browsers (Chrome, Firefox, Edge, Safari - last 2 major versions).
*   **UI-02:** The interface shall include distinct dashboard views tailored for each user class (General User, Dept. Admin, etc.).

**3.1.2 Hardware Interfaces**
*   **HW-01:** The system shall operate on standard university server hardware meeting the minimum specifications for the chosen application server and database.

**3.1.3 Software Interfaces**
*   **SI-01:** The system shall authenticate users via the university's **LDAP v3** or **Active Directory** service.
*   **SI-02:** The system shall connect to the three legacy faculty inventory databases (**Oracle 12c**, **MySQL 5.7**, **SQL Server 2019**) via secure, read/write connectors.
*   **SI-03:** The system shall use the university's standard SMTP server for sending notification emails.

**3.1.4 Communications Interfaces**
*   **CI-01:** All client-server communication shall use **HTTPS (TLS 1.2 or higher)**.
*   **CI-02:** Internal system components shall communicate via RESTful APIs or secure message queues.

#### 3.2 Functional Requirements
**3.2.1 Asset Management**
*   **FR-01: Add Asset**
    *   The system shall allow authorized administrators (Dept., Faculty, University) to add a new asset to the inventory.
    *   Inputs shall include: Asset ID (auto-generated), Name, Description, Category, Location, Custodian (default: requester), Status (Available, Checked-Out, Maintenance), and associated Faculty/Department.
*   **FR-02: Modify Asset**
    *   The system shall allow authorized administrators to edit the details of an existing asset within their scope of authority.
*   **FR-03: Transfer Asset**
    *   The system shall allow an administrator to initiate a transfer of an asset to a different department or faculty.
    *   The system shall require approval from an administrator in the *receiving* organizational unit before the transfer is finalized and custody is updated.
*   **FR-04: View Assets**
    *   The system shall provide search and filter capabilities for all users to browse assets based on category, location, status, and faculty/department.

**3.2.2 Request Management**
*   **FR-05: Create Request**
    *   Any authenticated user shall be able to create a request to either **borrow a portable asset** or **reserve a space**.
    *   For reservations, the user must specify a start and end date/time.
*   **FR-06: Approve/Deny Request**
    *   The system shall route a request for approval to the appropriate administrator (e.g., Dept. Admin for intra-department requests).
    *   The administrator shall be able to approve or deny the request with an optional reason.
    *   The requester shall be notified via email of the decision.
*   **FR-07: Track Request Status**
    *   Users shall be able to view the current status (Pending, Approved, Denied, Completed) of all requests they have submitted.

**3.2.3 Permission & Role Management**
*   **FR-08: Manage Roles**
    *   IT and University Administrators shall be able to create, modify, and delete system roles (e.g., "Physics Dept. Admin").
*   **FR-09: Assign Permissions**
    *   The system shall allow the assignment of granular permissions (e.g., "Can approve requests in Dept. X", "Can edit assets in Faculty Y") to roles, based on the organizational hierarchy.
*   **FR-10: Assign Users to Roles**
    *   Administrators shall be able to assign individual users (retrieved from the central directory) to one or more system roles.

#### 3.3 Non-Functional Requirements

**3.3.1 Performance Requirements**
*   **PER-01:** The system shall support up to **500 concurrent users**.
*   **PER-02:** The web interface shall load any dashboard page within **3 seconds** under normal load (100 concurrent users).
*   **PER-03:** Search operations returning <100 results shall complete within **2 seconds**.
*   **PER-04:** As specified in Constraints (Section 2.4), the system shall automatically terminate any database query exceeding **60 seconds** of execution time.

**3.3.2 Safety Requirements**
*   *Not applicable for this business system.*

**3.3.3 Security Requirements**
*   **SEC-01:** All access shall be subject to authentication (via central LDAP/AD).
*   **SEC-02:** All user actions shall be authorized based on their assigned roles and hierarchical scope.
*   **SEC-03:** The system shall log all security-critical events (failed logins, permission denials, asset transfers, approval actions) in an immutable audit trail.
*   **SEC-04:** All passwords shall be managed by the central directory service; the UUAMS shall not store user passwords.

**3.3.4 Software Quality Attributes**
*   **RELI-01:** The system shall meet the **99% availability** requirement during working hours as defined in Section 2.4.
*   **USAB-01:** The system shall be designed to be intuitive for General Users, requiring no formal training for basic request creation.
*   **MAIN-01:** The system shall be modular to allow for updates to the integration layer for one faculty without impacting connections to the others.
*   **PORT-01:** The system shall be platform-independent, meeting the constraint in Section 2.4 to run on both Windows and Unix servers.

---

### 4. Appendices

#### Appendix A: Data Flow Diagrams (To be developed)
*   Context Diagram
*   Level-1 DFD for Request Process

#### Appendix B: Entity-Relationship Model (To be developed)
*   Conceptual ERD for the unified UUAMS database.

#### Appendix C: Change Management
This SRS document may be updated as the project evolves. All changes must be approved by the project steering committee and recorded in a version history log.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead System Analyst | | | |
| IT Director | | | |