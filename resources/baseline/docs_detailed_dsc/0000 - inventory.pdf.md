# Software Requirements Specification (SRS)
## Unified University Inventory System (UUIS)

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft for Review  
**Authors:** UUIS Requirements Team

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Unified University Inventory System (UUIS). It serves as a comprehensive guide for developers, testers, project managers, and stakeholders to understand the system's intended capabilities, constraints, and behavior. The primary audience includes the development team, quality assurance, and university administration.

#### 1.2 Scope
The UUIS is a web-based application designed to centralize and streamline inventory management across three university faculties: Arts & Science, Computer Science, and Engineering. The system will manage physical assets, software licenses, and reservable spaces/rooms through a unified request and approval workflow, supported by a hierarchical permission model.

**In-Scope:**
*   Centralized web interface for inventory management.
*   Hierarchical user roles and permission delegation.
*   Asset borrowing and space reservation request workflows.
*   Integration with existing faculty legacy databases.
*   Reporting and audit logging.
*   Bulk asset import functionality.

**Out of Scope (Non-Goals):**
*   Replacement of existing faculty-specific inventory databases.
*   Development of a native mobile application.
*   Implementation of real-time asset tracking sensors (e.g., RFID, IoT).
*   Financial management or procurement modules.
*   Direct integration with university HR or student information systems for user population (initial phase).

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **UUIS:** Unified University Inventory System.
*   **SLA:** Service Level Agreement.
*   **CRUD:** Create, Read, Update, Delete.
*   **UAT:** User Acceptance Testing.
*   **API:** Application Programming Interface.
*   **SMTP:** Simple Mail Transfer Protocol.
*   **Asset:** Any item managed by the system (e.g., laptop, projector, software license, laboratory room).

#### 1.4 References
*   University IT Security Policy v4.2
*   Faculty of Engineering Asset Management Guidelines
*   Project Charter: UUIS-2023-01

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product and its operating environment. Section 3 details specific system requirements in a structured format. Appendices may contain supplementary diagrams or data models.

---

### 2. Overall Description

#### 2.1 Product Perspective
The UUIS is a new, self-contained web application that will interact with several external systems:
*   **Authentication System:** For user login.
*   **Legacy Faculty Databases (3):** For data integration.
*   **University Email Server:** For notifications.

It is designed to be the primary interface for all university inventory operations, sitting above but not replacing existing faculty data stores.

#### 2.2 User Classes and Characteristics
| User Class | Level | Key Characteristics | Key Responsibilities |
| :--- | :--- | :--- | :--- |
| **IT/Security Administrator** | 4 | Technical staff, small group. | System maintenance, group permissions, exception handling. |
| **University Administrator** | 3 | Central admin staff, ~5-10 users. | Oversight of all inventory, approves inter-faculty/outside transfers. |
| **Faculty Administrator** | 2 | Faculty-level staff, ~3 per faculty. | Manages faculty inventory, approves inter-departmental transfers. |
| **Department Administrator** | 1 | Department-level staff, multiple per dept. | Controls department inventory, approves internal transfers. |
| **Inventory Administrator (Delegated)** | N/A | Staff or students delegated specific tasks. | Performs specific CRUD operations as permitted by a higher-level admin. |
| **User (Student/Professor)** | 0 | All students and faculty, ~1000s. | Browses inventory, creates borrow/reserve requests. |

#### 2.3 Operating Environment
*   **Software:** Modern web browsers (Chrome, Firefox, Safari, Edge). Application hosted on university Linux servers.
*   **Hardware:** Standard university desktop/laptop for users; dedicated application and database servers.
*   **Network:** Accessible via university intranet and VPN for secure external access.

#### 2.4 Design and Implementation Constraints
1.  Must use the university's central authentication service.
2.  Database must be compatible with the university's standard RDBMS (PostgreSQL 12+).
3.  Frontend must not require browser plugins (e.g., Flash, Java applets).
4.  Must comply with university accessibility guidelines (WCAG 2.1 AA).

#### 2.5 Assumptions and Dependencies
*   Legacy faculty databases will remain operational and provide a stable interface (API or direct DB access) for integration.
*   User information (name, email, faculty/department affiliation) will be provisioned to the system.
*   University "working hours" for system availability will be formally defined by administration.

---

### 3. System Requirements

#### 3.1 Functional Requirements

##### 3.1.1 User Authentication and Authorization
*   **FR-1:** The system shall authenticate all users via the central university username and password service.
*   **FR-2:** The system shall assign users a default role (Level 0-4) based on data from the provisioning source.
*   **FR-3:** The system shall allow higher-level administrators (Level 1-4) to delegate specific permissions (`asset:edit`, `request:approve`, etc.) to other users, adhering to the rule that a user cannot delegate a permission they do not possess.
*   **FR-4:** The system shall enforce role and permission checks on all actions, returning an "Insufficient Privilege" error when violated.

##### 3.1.2 Asset Management
*   **FR-5:** The system shall allow authorized administrators to add, view, modify, and deactivate assets.
*   **FR-6:** Each asset shall have a mandatory type, status (e.g., Available, Checked-Out, Damaged, In Maintenance), current location, and owning department.
*   **FR-7:** The system shall provide a bulk upload feature to add/update multiple assets from a structured file (format TBD).
*   **FR-8:** When an administrator attempts to add an asset with a non-existent type, the system shall create an exception request for the IT Administrator.
*   **FR-9:** The system shall integrate with legacy faculty databases to synchronize asset data according to a defined mechanism (frequency TBD).

##### 3.1.3 Request Workflow
*   **FR-10:** A Level 0 User shall be able to create a borrow request for an asset or a reserve request for a space.
*   **FR-11:** The system shall automatically route a request to the correct approval queue based on:
    *   The asset's owning department/faculty.
    *   The requester's department/faculty.
    *   The request type (intra-department, inter-department, inter-faculty).
*   **FR-12:** Authorized administrators shall have a queue interface to view, approve, or reject pending requests.
*   **FR-13:** Upon request approval, the system shall automatically update the asset's status to "Checked-Out" or "Reserved".
*   **FR-14:** The system shall send an email notification to the requester upon request approval, rejection, or system cancellation.

##### 3.1.4 Reporting and Auditing
*   **FR-15:** The system shall generate reports on assets (by location, type, status, department) and request history.
*   **FR-16:** The system shall maintain an immutable audit log of all significant actions, including: asset modifications, permission changes, request state transitions, and user authentication attempts (success/failure).

##### 3.1.5 University Structure and Location Management
*   **FR-17:** The system shall model the university hierarchy (University > Faculty > Department).
*   **FR-18:** The system shall allow IT Administrators to create and manage locations/rooms, assigning them to a specific faculty.

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance
*   **NFR-1:** All web pages shall load within 3 seconds under normal load conditions.
*   **NFR-2:** Standard reports on datasets of up to 10,000 assets shall generate within 30 seconds.
*   **NFR-3:** The authentication service response time shall be under 2 seconds.
*   **NFR-4:** Queries to legacy databases shall timeout after 1 minute.

##### 3.2.2 Reliability & Availability
*   **NFR-5:** The system shall be available 99% of the time during formally defined university working hours.
*   **NFR-6:** Automated full database backups shall be performed nightly with a retention period of 7 days.

##### 3.2.3 Security
*   **NFR-7:** All user sessions shall timeout after 30 minutes of inactivity.
*   **NFR-8:** All database queries shall be parameterized to prevent SQL injection attacks.
*   **NFR-9:** Audit logs shall be retained for a minimum of 7 years for compliance.

##### 3.2.4 Usability
*   **NFR-10:** A new Level 0 User shall be able to successfully create a borrow request with less than 4 hours of training or guided exploration.
*   **NFR-11:** Approval queues for administrators shall be filterable by request type, date, department, and asset.

#### 3.3 External Interface Requirements

##### 3.3.1 User Interfaces
*   **UI-1:** The system shall provide a responsive web interface compatible with recent versions of Chrome, Firefox, Safari, and Edge.

##### 3.3.2 Hardware Interfaces
*   **HI-1:** None specified.

##### 3.3.3 Software Interfaces
*   **SI-1:** **Authentication System Interface:** The system shall call the university's LDAP/Active Directory service to validate credentials.
*   **SI-2:** **Legacy Database Interface:** The system shall connect to three distinct faculty databases (mechanism TBD) to read and synchronize asset data.
*   **SI-3:** **Email Interface:** The system shall connect to the university SMTP server to send notification emails, with delivery initiation within 5 minutes of the triggering event.

##### 3.3.4 Communications Interfaces
*   **CI-1:** All external communications with legacy systems and email shall use the university's secure internal network or VPN.

#### 3.4 Acceptance Criteria (Selected Key Examples)
*   **AC-1 (FR-10):** Given a Level 0 User is authenticated, when they submit a basic borrow request for an available asset, then the request is created with a "Pending" status.
*   **AC-2 (FR-4):** Given a Department Administrator is authenticated, when they attempt to approve an inter-faculty transfer request, then the system displays an "Insufficient Privilege" error.
*   **AC-3 (FR-5, FR-16):** Given an Inventory Administrator with `asset:edit` permission is viewing an asset, when they modify the asset's status to "Damaged" and save, then the inventory record is updated and an entry is created in the AuditLog.
*   **AC-4 (FR-7):** Given a Faculty Administrator, when they use the bulk upload feature to add 50 new software licenses, then all licenses are added and owned by the respective departments under that faculty.

---

### 4. Appendices

#### 4.1 Domain Model (Summary)
```yaml
User:
  - userID: PK, Unique
  - name: String
  - role: String (Level 0-4)
  - departmentID: FK > UniversityStructure
  - facultyID: FK > UniversityStructure

Asset:
  - assetID: PK, Unique
  - serialNumber: String
  - type: String (Required)
  - status: Enum (Available, Checked-Out, etc.)
  - currentLocationID: FK > Location
  - ownerDepartmentID: FK > UniversityStructure

Request:
  - requestID: PK, Unique
  - requesterUserID: FK > User
  - assetID: FK > Asset
  - type: Enum (Borrow, Reserve)
  - status: Enum (Pending, Approved, Rejected, etc.)
  - approvalLevelRequired: Integer

UniversityStructure:
  - nodeID: PK, Unique
  - name: String
  - type: Enum (University, Faculty, Department)
  - parentNodeID: FK > UniversityStructure (Self-Referencing)
```

#### 4.2 Business Process Flow (Key)
**Main Process: Asset Borrowing**
1.  User authenticates.
2.  User creates request (Asset, Duration).
3.  System routes to approval queue (Dept/Faculty/Uni Admin).
4.  Admin approves/rejects.
5.  System updates asset status, sends email.
6.  Upon physical return, admin updates asset status.

#### 4.3 Risk Management
| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| Legacy DB Integration Complexity | High | High | Early prototyping; phased integration. |
| Permission Delegation Gaps | Medium | High | Implement strict "no delegation without possession" rule. |
| High Request Volume | Medium | Medium | Design filterable queues; monitor during pilot. |
| Poor User Adoption | Medium | Medium | Involve end-users in design; create guides. |

#### 4.4 Open Issues and Decisions Pending
1.  **Decision:** Frequency/Mechanism of legacy database sync. *Owners: Technical Lead, Faculty IT.*
2.  **Decision:** Bulk upload file format (CSV/XML) and validation rules. *Owners: Business Analyst, Lead Developer.*
3.  **Decision:** Formal definition of "working hours" for SLA. *Owners: Product Owner, University Admin.*
4.  **Decision:** Priority order for integrating the three legacy databases. *Owners: Project Sponsor, Technical Lead.*

---
*Document End*