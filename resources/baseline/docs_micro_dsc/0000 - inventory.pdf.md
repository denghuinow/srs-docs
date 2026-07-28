# Software Requirements Specification (SRS)
## University Asset and Space Management System (UASMS)

**Document Version:** 1.0  
**Date:** [Current Date]  
**Authors:** [Project Team/Author Name]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the University Asset and Space Management System (UASMS). The primary purpose of this document is to provide a detailed description of the system's capabilities, interfaces, and performance characteristics. It is intended for use by the project stakeholders, including university administration, faculty representatives, development teams, and quality assurance personnel.

#### 1.2 Scope
The UASMS is a secure, web-based system designed to integrate and manage inventory assets (e.g., lab equipment, AV gear, furniture) and reservable spaces (e.g., meeting rooms, labs) across three distinct university faculties. The system will centralize tracking, facilitate controlled transfers between departments and faculties, and manage the request-approval workflow for borrowing assets or reserving spaces. It will also provide reporting capabilities for inventory and request audits. Access to the system is restricted to authorized university staff during institutional working hours.

**In-Scope:**
*   User management and role-based access control for three faculties.
*   Cataloging and lifecycle tracking of inventory assets.
*   Management of reservable space listings.
*   Workflow for submitting, reviewing, and approving/denying asset borrow and space reservation requests.
*   Process for initiating and recording inter-faculty and intra-faculty asset transfers.
*   Generation of standard inventory, transaction, and request history reports.
*   Web-based user interface accessible via standard browsers.

**Out-of-Scope:**
*   Financial management or procurement of new assets.
*   Integration with campus card access systems for physical spaces.
*   Real-time GPS tracking of mobile assets.
*   Mobile-native applications (system is web-responsive only).
*   Maintenance scheduling or calibration tracking for equipment.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **Asset** | Any physical inventory item (e.g., projector, microscope, laptop cart) tracked by the system. |
| **Space** | A reservable physical location (e.g., conference room, laboratory). |
| **Faculty** | One of the three primary organizational units (e.g., Faculty of Science, Faculty of Engineering). |
| **Transfer** | The formal process of changing the custodial responsibility of an asset from one organizational level to another. |
| **Requester** | A user with privileges to submit borrow/reservation requests. |
| **Approver** | A user with privileges to review and approve/deny requests for their organizational unit. |
| **Administrator** | A super-user with privileges to manage system data and users. |
| **UASMS** | University Asset and Space Management System. |
| **SLA** | Service Level Agreement. |

#### 1.4 References
*   University IT Security Policy v3.1
*   Institutional Data Classification Standard
*   Project Charter: UASMS, Version 1.2

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its users, and operating environment. Section 3 details the specific functional requirements. Section 4 outlines all non-functional requirements, including performance, security, and usability.

### 2. Overall Description

#### 2.1 Product Perspective
The UASMS is a new, self-contained system. It will operate within the university's existing IT infrastructure, utilizing central authentication services (e.g., LDAP/Active Directory) for user login. It will require a dedicated database server. Future considerations may include APIs for integration with the university's central finance or facilities systems, but these are not part of the current project.

#### 2.2 Product Functions
The core functions of the UASMS are:
1.  **Asset & Space Management:** Maintain a centralized repository of all trackable assets and reservable spaces, including details like description, location, condition, and responsible faculty/department.
2.  **Transfer Management:** Enable authorized users to initiate, approve, and record the transfer of assets between different organizational levels (e.g., department to department, faculty to faculty).
3.  **Request & Approval Workflow:** Provide a structured process for users to request to borrow assets or reserve spaces, and for approvers to review and decide on these requests. Notifications will be sent at key workflow stages.
4.  **Reporting:** Generate and export predefined reports detailing inventory status, request history, approval timelines, and transfer logs.

#### 2.3 User Characteristics
| User Class | Description | Key Skills & Assumptions |
| :--- | :--- | :--- |
| **End-User / Requester** | Staff members who need to borrow assets or reserve spaces. | Basic computer literacy, web browsing. Understands their own departmental structure. |
| **Approver / Manager** | Department heads or designated staff responsible for assets/spaces. | Same as above, with authority to make allocation decisions. |
| **Faculty Administrator** | Power users within each faculty responsible for overseeing transfers and catalog accuracy. | Higher technical comfort. Understands faculty-level organizational hierarchy. |
| **System Administrator** | IT staff responsible for system health, user role management, and backups. | Proficient in system administration and database management. |

#### 2.4 Constraints
1.  **Availability Constraint:** The system must be operational and available for access during standard university working hours (defined as 8:00 AM to 6:00 PM, Monday through Friday, excluding official holidays). Planned maintenance outside these hours is acceptable.
2.  **Learnability Constraint:** A new user who is computer-literate and familiar with basic web applications must be able to perform their core tasks (e.g., submit a request, approve a request) without assistance after a maximum of **4 hours** of total engagement, including any formal training and independent exploration.
3.  **Performance Constraint:** All database queries executed by the system's standard functions (searches, report generation, loading lists) must complete and return results within **1 minute** under normal operational load.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** All users will have reliable access to a modern web browser and the university network.
*   **Assumption:** A definitive, agreed-upon list of assets and spaces to be migrated into the system will be provided by the faculties.
*   **Dependency:** The project depends on the university's IT department to provision suitable application and database server hosting.
*   **Dependency:** User authentication is dependent on the stability and availability of the university's central directory service.

### 3. Specific Requirements

#### 3.1 Functional Requirements

**3.1.1 User Management & Authentication (UM)**
*   **UM-1:** The system shall authenticate users via the university's central directory service.
*   **UM-2:** The system shall assign users to one or more of the following roles: Requester, Approver, Faculty Administrator, System Administrator.
*   **UM-3:** A System Administrator shall be able to create, modify, and disable user accounts and role assignments.

**3.1.2 Asset & Space Catalog Management (CM)**
*   **CM-1:** The system shall allow Faculty Administrators to add, edit (mark as damaged/lost), and decommission assets and spaces within their faculty's purview.
*   **CM-2:** Each asset record shall store: Unique ID, Description, Category, Serial Number, Faculty/Department, Current Location, Status (Available, Checked-Out, In Repair, Lost), Purchase Date, and Value.
*   **CM-3:** Each space record shall store: Unique ID, Name, Location, Capacity, Faculty/Department, Associated Assets (e.g., built-in projector), and Availability Schedule.

**3.1.3 Asset Transfer Management (TR)**
*   **TR-1:** A Faculty Administrator shall be able to initiate a transfer request for an asset from one organizational unit (e.g., Department A in Faculty 1) to another (e.g., Department B in Faculty 2).
*   **TR-2:** The system shall require approval from an Approver in the *receiving* organizational unit before a transfer is finalized.
*   **TR-3:** Upon approval, the system shall automatically update the asset's recorded responsible faculty/department and log the complete transaction (who, what, when, from/to).

**3.1.4 Borrowing & Reservation Workflow (BR)**
*   **BR-1:** A Requester shall be able to search for available assets or spaces and submit a request specifying desired item, dates, and times.
*   **BR-2:** The system shall automatically route the submitted request to the appropriate Approver(s) based on the asset's/space's responsible organizational unit.
*   **BR-3:** An Approver shall be able to view pending requests, and approve or deny them with an optional reason.
*   **BR-4:** The Requester and Approver shall receive email notifications upon request submission, approval, or denial.
*   **BR-5:** Upon approval, the system shall mark the asset/space as "Reserved" or "Checked-Out" for the specified period.

**3.1.5 Reporting (RE)**
*   **RE-1:** The system shall generate a pre-defined "Inventory Summary Report" listing all assets by faculty, department, and status. Report shall be exportable to PDF and CSV.
*   **RE-2:** The system shall generate a pre-defined "Request History Report" filterable by date range, faculty, requester, and status (approved/denied/pending). Report shall be exportable to PDF and CSV.
*   **RE-3:** The system shall generate a pre-defined "Transfer Log Report" detailing all asset transfers within a specified date range.

#### 3.2 Non-Functional Requirements

**3.2.1 Performance Requirements**
*   **PER-1:** As per Key Constraint 3, all user-initiated database queries shall return results within **60 seconds**, with a target of under 5 seconds for common searches and list views.
*   **PER-2:** The system shall support a concurrent user load of up to 100 users without significant degradation in response time.

**3.2.2 Usability Requirements**
*   **USB-1:** As per Key Constraint 2, a new user shall achieve proficiency in core tasks applicable to their role within **4 hours** of initial use.
*   **USB-2:** The user interface shall be consistent with WCAG 2.1 Level AA guidelines for accessibility.
*   **USB-3:** All error messages shall be clear, instruct the user on corrective action, and avoid technical jargon.

**3.2.3 Reliability & Availability**
*   **AVL-1:** As per Key Constraint 1, the system shall maintain **99% availability** during published working hours (8:00 AM - 6:00 PM, Mon-Fri).
*   **AVL-2:** Scheduled maintenance requiring downtime shall be communicated at least 48 hours in advance and performed outside working hours.

**3.2.4 Security Requirements**
*   **SEC-1:** All user sessions shall timeout after 15 minutes of inactivity.
*   **SEC-2:** All web communications shall be encrypted using TLS 1.2 or higher.
*   **SEC-3:** Users shall only see and act upon data (assets, spaces, requests) for which their role and organizational permissions are valid (e.g., a Faculty 1 Approver cannot see requests for Faculty 2 assets).
*   **SEC-4:** All user actions (logins, approvals, transfers, edits) shall be recorded in an immutable audit log.

**3.2.5 Data Management**
*   **DATA-1:** The system shall perform a full database backup automatically every 24 hours.
*   **DATA-2:** Asset transaction history and request records shall be retained for a minimum of 7 years to meet audit requirements.

### 4. Appendices

#### 4.1 Use Case Diagrams
*(Placeholder for diagrams illustrating the core interactions: Submit Request, Approve Request, Initiate Transfer, Generate Report)*

#### 4.2 Data Schema Overview
*(Placeholder for a high-level Entity-Relationship diagram or table listing core entities: User, Asset, Space, Request, TransferLog, AuditLog)*

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| Quality Assurance Lead | | | |