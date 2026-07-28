# Software Requirements Specification (SRS)
## Unified University Inventory System (UUIS)

**Document Version:** 1.0  
**Date:** [Current Date]  
**Status:** Draft for Review  
**Prepared for:** University Stakeholders  
**Prepared by:** [Your Name/Team]

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Unified University Inventory System (UUIS). The primary audience includes stakeholders, project managers, developers, testers, and system administrators. This document serves as the foundation for system design, implementation, testing, and project validation.

#### 1.2 Scope
The UUIS is a web-based application designed to consolidate three separate faculty inventory databases into a single, centralized platform. The system will manage university assets—including rooms/spaces, software licenses, and physical assets—through a secure, role-based interface accessible during standard working hours. Core functionalities include asset lifecycle management (add, edit, transfer, return), a request/approval workflow for borrowing/reservations, and comprehensive user permission management.

**In-Scope Items:**
*   Centralized web interface for inventory management.
*   Management of three defined asset types.
*   Inventory operations (transfer, edit, add, return).
*   Request and approval workflow system.
*   User authentication and role-based access control (RBAC).

**Out-of-Scope Items:**
*   Integration with external, non-faculty systems.
*   Real-time tracking (e.g., IoT, GPS).
*   Native mobile applications.
*   Financial processing, billing, or invoicing.
*   Advanced data analytics, machine learning, or predictive maintenance modules.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **UUIS** | Unified University Inventory System |
| **Asset** | Any inventory item managed by the system (Room, Software License, Physical Asset) |
| **RBAC** | Role-Based Access Control |
| **Faculty** | A major academic division within the university (e.g., Faculty of Engineering) |
| **Department** | A sub-division within a Faculty |
| **Approval Workflow** | The defined process a request must follow for authorization |

#### 1.4 References
*   University IT Security Policy v3.1
*   Initial Project Charter: UUIS, [Date]
*   Legacy Faculty Database Schemas (Faculties A, B, C)

#### 1.5 Document Overview
This SRS is structured to present an overall description of the product, followed by specific external interface, functional, and non-functional requirements.

### 2. Overall Description

#### 2.1 Product Perspective
The UUIS is a new, self-contained system that will replace three legacy, isolated faculty inventory databases. It will interface with existing university user directories for authentication. The system does not initiate connections to other external enterprise systems.

#### 2.2 Product Functions (High-Level)
1.  Provide a secure, web-based user interface.
2.  Authenticate users and enforce role-based permissions.
3.  Manage the lifecycle of inventory assets (Create, Read, Update, Transfer, Archive).
4.  Facilitate user requests to borrow assets or reserve spaces.
5.  Route requests through configurable approval workflows based on asset type, value, and transfer scope.
6.  Generate standard reports on inventory status, location, and history.
7.  Administer user roles and permissions.

#### 2.3 User Characteristics and Stakeholders
| Stakeholder | Role & Responsibilities | Key System Interactions |
| :--- | :--- | :--- |
| **University Administrator** | Oversees entire university inventory, sets top-level policy, approves inter-faculty transfers. | Manage global settings, approve high-level transfers, view university-wide reports. |
| **Faculty Administrator** | Manages inventory within a specific faculty, approves inter-departmental transfers. | Oversee faculty inventory, generate faculty-level reports, approve departmental transfers. |
| **Department Administrator** | Manages inventory for a specific department, approves internal transfer requests. | Manage department assets, approve internal requests, delegate tasks to Inventory Administrators. |
| **Inventory Administrator** | Performs day-to-day inventory tasks as delegated by a Department or Faculty Administrator. | Add/edit asset details, process returns, execute approved transfers. |
| **User (Student/Professor)** | Needs to borrow physical assets or reserve rooms/software for academic use. | Browse available inventory, submit borrowing/reservation requests, view request status. |
| **IT Administrator** | Maintains system infrastructure, manages user accounts and security groups. | Assign system permissions, monitor system health, perform backups. |

#### 2.4 Operating Environment
*   **Server:** Must be deployable on both Microsoft Windows Server and Unix-based (e.g., Linux) platforms.
*   **Client:** Web browser (Internet Explorer 11+, Mozilla Firefox, Google Chrome, Opera, Safari - latest stable versions).
*   **Network:** Accessible via university intranet; external access requires VPN.
*   **Availability:** Required during university working hours (e.g., 7:00 AM - 7:00 PM, Monday-Friday). Scheduled maintenance will occur outside this window.

#### 2.5 Design and Implementation Constraints
1.  **Platform Compatibility:** The application must be browser-based and compatible with the listed browsers.
2.  **Authentication:** Limited to username/password credentials validated against the university directory. Multi-factor authentication is not required.
3.  **Performance:** All database queries must be optimized to complete within a maximum timeout of **1 minute**.
4.  **Security Model:** The principle of least privilege and delegation limits shall apply. A user can only delegate permissions that are a subset of their own.
5.  **Business Rule:** Any request for an asset transfer to an entity outside the university **must** be routed for University Administrator approval.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** Users possess basic computer literacy and internet browsing skills.
*   **Assumption:** Accurate initial data will be provided from the three legacy faculty databases.
*   **Dependency:** The system depends on the university's central Active Directory/LDAP service for user authentication.
*   **Dependency:** Successful completion of user acceptance testing (UAT) by stakeholder representatives is required for go-live.

### 3. System Features and Requirements

#### 3.1 Functional Requirements

**3.1.1 User Authentication and Authorization (FR-AUTH)**
*   **FR-AUTH-01:** The system shall authenticate users via university username and password.
*   **FR-AUTH-02:** The system shall implement RBAC with the following predefined roles: User, Inventory Administrator, Department Administrator, Faculty Administrator, University Administrator, IT Administrator.
*   **FR-AUTH-03:** A user with administrative privileges shall be able to assign roles to other users, provided the assigned role does not exceed the assigner's own privilege level.

**3.1.2 Asset Management (FR-AM)**
*   **FR-AM-01:** The system shall allow authorized users to add new assets to the inventory, classifying them as: Room/Space, Software License, or Physical Asset.
*   **FR-AM-02:** For each asset, the system shall store at minimum: Unique ID, Name, Description, Type, Current Location (Faculty/Department), Status (Available, Checked-Out, Under Maintenance), Acquisition Date, and Custodian.
*   **FR-AM-03:** Authorized users (Inventory Admin and above) shall be able to modify the properties of assets within their scope of authority.
*   **FR-AM-04:** The system shall track the complete history of all changes (transfers, edits) made to any asset.

**3.1.3 Request and Approval Workflow (FR-REQ)**
*   **FR-REQ-01:** Any authenticated User shall be able to submit a request to borrow a physical asset or reserve a room/software license.
*   **FR-REQ-02:** The system shall automatically route requests based on configurable rules:
    *   Internal department transfers → Department Administrator.
    *   Inter-department, intra-faculty transfers → Faculty Administrator.
    *   Inter-faculty transfers → University Administrator.
    *   Transfers outside university → University Administrator.
*   **FR-REQ-03:** Approvers shall receive notification of pending requests and shall be able to approve or reject them with an optional comment.
*   **FR-REQ-04:** The requestor shall be able to view the real-time status (Pending, Approved, Rejected, Fulfilled) of their requests.

**3.1.4 Transfer and Return Processing (FR-TR)**
*   **FR-TR-01:** Upon approval, the system shall generate a transfer order and update the asset's status and location.
*   **FR-TR-02:** Inventory Administrators shall be able to record the physical handoff/checkout of an asset to a requestor.
*   **FR-TR-03:** The system shall allow Inventory Administrators to process the return of an asset, updating its status back to "Available."

**3.1.5 Reporting (FR-REP)**
*   **FR-REP-01:** The system shall allow Faculty Administrators and above to generate a standard report listing all assets filtered by location (Faculty/Department).
*   **FR-REP-02:** The system shall provide a report of all pending requests for the logged-in administrator's scope.

#### 3.2 Non-Functional Requirements

**3.2.1 Usability (NF-US)**
*   **NF-US-01:** A user with basic internet and office software experience shall be able to perform core functions (browse, request) after a maximum of **2-4 hours** of training.
*   **NF-US-02:** The system shall provide clear error messages and confirmations for user actions.

**3.2.2 Reliability (NF-REL)**
*   **NF-REL-01:** The system shall maintain **100% availability** during defined university working hours.
*   **NF-REL-02:** All data transactions shall be atomic, consistent, isolated, and durable (ACID properties).

**3.2.3 Performance (NF-PER)**
*   **NF-PER-01:** The system shall support concurrent access by a minimum of 200 users.
*   **NF-PER-02:** Page load times for standard views (asset list, request form) shall be under **3 seconds** under normal load.
*   **NF-PER-03:** As per constraint, no single database query shall execute for longer than **60 seconds**; the system shall timeout and return a user-friendly message.

**3.2.4 Security (NF-SEC)**
*   **NF-SEC-01:** All authentication shall occur over encrypted channels (HTTPS).
*   **NF-SEC-02:** User passwords shall be stored using strong, salted hashing algorithms.
*   **NF-SEC-03:** The system shall prevent privilege escalation via the delegation function.
*   **NF-SEC-04:** User sessions shall expire after **15 minutes** of inactivity.

**3.2.5 Supportability (NF-SUP)**
*   **NF-SUP-01:** The system shall log all user authentication attempts (success/failure).
*   **NF-SUP-02:** The system shall log all critical actions (asset creation, modification, transfer approval).

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   The interface shall be a responsive web application.
*   It shall feature a main navigation menu based on the user's role.
*   Standard forms shall include: Login, Asset Search/View, Request Form, Approval Dashboard, Administration Panel.

#### 4.2 Hardware Interfaces
*   None specified. Standard server-client architecture over TCP/IP is assumed.

#### 4.3 Software Interfaces
*   **University Directory Service:** The system shall interface with the university's LDAP/Active Directory service for user authentication.
*   **Legacy Databases:** The system shall have a one-time data migration interface to import data from the three legacy faculty databases.

#### 4.4 Communication Interfaces
*   The system shall use HTTP/HTTPS protocols for client-server communication.

### 5. Other Non-Functional Requirements

#### 5.1 Success Metrics
1.  **Integration:** Successful migration and consolidation of data from three distinct faculty databases without data loss.
2.  **Availability:** Achievement of 100% scheduled uptime during working hours for the first quarter post-launch.
3.  **Training:** 90% of trained users report confidence in performing their assigned tasks within the 2-4 hour training window.

### 6. Appendices

#### 6.1 Undecided Issues / Open Questions
1.  The specific frequency (e.g., daily, weekly) and methodology for system backups and disaster recovery procedures.
2.  The depth and retention period for audit trails (e.g., are all read operations logged, or only writes?).
3.  The precise definition and handling process for "exception requests" that fall outside normal workflows and require IT intervention.
4.  Detailed performance benchmarks for peak usage periods (e.g., start of semester).
5.  The process for formal User Experience (UX) validation and user acceptance testing criteria for the interface design.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| Quality Assurance | | | |