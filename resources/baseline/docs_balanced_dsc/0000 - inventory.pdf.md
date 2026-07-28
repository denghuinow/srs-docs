# **Software Requirements Specification (SRS)**
## **Unified University Inventory System (UUIS)**

**Document Version:** 1.0
**Date:** October 26, 2023
**Status:** Draft for Review
**Project Sponsor:** IUfA University Administration

---

### **Revision History**

| Version | Date       | Author/Editor          | Description of Change          |
| :------ | :--------- | :--------------------- | :----------------------------- |
| 1.0     | 2023-10-26 | SRS Author             | Initial Draft Creation         |

---

## **1. Introduction**

### **1.1 Purpose**
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Unified University Inventory System (UUIS). It serves as a comprehensive agreement between the stakeholders (university administration, faculty, IT, and end-users) and the development team. This document will be used to guide the design, development, testing, and deployment phases of the project.

### **1.2 Scope**
The UUIS is a web-based application designed to integrate and centralize the disparate inventory databases of three university faculties. Its primary purpose is to provide a secure, unified interface for managing all university assets, including equipment, materials, and reservable spaces.

**In-Scope:**
*   Centralized web interface for inventory management.
*   Role-based access control for all system functions.
*   Asset lifecycle management (search, request, approve, transfer, modify, return).
*   Reporting capabilities for auditing and oversight.
*   Management of the university's hierarchical structure (University > Faculty > Department).
*   Integration of existing faculty inventory data sources.

**Out-of-Scope:**
*   Financial management or procurement of new assets.
*   Real-time GPS tracking of physical assets.
*   Predictive maintenance scheduling for assets.
*   Direct integration with external financial or HR systems (though user data may be imported).
*   Mobile-native application development (system will be browser-responsive).

### **1.3 Definitions, Acronyms, and Abbreviations**
*   **UUIS:** Unified University Inventory System.
*   **Asset:** Any physical item (e.g., laptop, projector, lab equipment) or reservable space managed by the university.
*   **Stakeholder:** Any individual or group with an interest in the system (see Section 2).
*   **Administrator:** An umbrella term for users with managerial permissions (University, Faculty, Department, Inventory Admin).
*   **SRS:** Software Requirements Specification.
*   **UAT:** User Acceptance Testing.

### **1.4 References**
*   IUfA IT Infrastructure and Security Policy v4.2
*   Preliminary Stakeholder Interviews and Workshop Notes
*   Legacy Faculty Inventory Database Schemas (Faculties A, B, C)

### **1.5 Overview**
The remainder of this document is structured as follows: Section 2 describes the overall product perspective, stakeholders, and user characteristics. Section 3 details specific functional requirements. Section 4 outlines non-functional requirements. Section 5 provides supplementary information on data models, milestones, risks, and open issues.

---

## **2. Overall Description**

### **2.1 Product Perspective**
The UUIS is a new, self-contained web application. It will interact with the following external entities:
*   **Users:** Access the system via a web browser.
*   **Legacy Databases:** The system will migrate and/or synchronize data from three existing faculty inventory databases.
*   **University Authentication Service:** The system will integrate with the central LDAP/Active Directory for user authentication (Single Sign-On preferred).
*   **Email Server:** To send notifications for request updates, approvals, and system alerts.

### **2.2 Stakeholders and User Characteristics**

| Stakeholder Category          | Key Responsibilities & Interests                                                                                                                                 | Expected Expertise                                                                 |
| :---------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------- |
| **University Administrator**  | Oversight of all university assets. Approval of inter-faculty transfers. Delegation of high-level permissions.                                                   | High-level administrative, understands university-wide policy.                     |
| **Faculty Administrator**     | Management of all assets within their faculty. Approval of intra-faculty requests. Generation of faculty-wide reports.                                            | Administrative, understands faculty-specific needs and procedures.                 |
| **Department Administrator**  | Management of assets within their department. First-level approval/rejection of asset requests.                                                                  | Familiar with department-level inventory and daily operations.                     |
| **Inventory Administrator**   | Perform day-to-day inventory tasks as delegated (e.g., updating asset status, processing returns).                                                                | Trained on specific UUIS procedures, detail-oriented.                              |
| **User (Student/Professor)**  | Search for available assets/spaces. Create and track borrowing/reservation requests.                                                                              | Basic computer literacy, familiar with web forms. Primary goal is ease of request. |
| **IT Administrator**          | System maintenance, user account and permission management, handling technical exception requests (e.g., new location types).                                      | Strong technical expertise in system administration and databases.                 |

### **2.3 Operating Environment**
*   **Software:** The application will be a web-based system accessible via standard browsers (see Portability, Section 4.2.3). The backend will run on a standard LAMP (Linux, Apache, MySQL, PHP) or equivalent stack (e.g., Java/.NET with SQL Server).
*   **Hardware:** Hosted on university-managed servers with appropriate specifications to handle concurrent user load.
*   **Network:** Accessible via the university's internal network and VPN for remote administrative access.

### **2.4 Design and Implementation Constraints**
1.  Must comply with the university's IT security and data privacy policies.
2.  Must use the existing university authentication system for user credentials.
3.  Must be developed within a 3-month timeline, necessitating a phased or MVP approach.
4.  Data migration must account for inconsistencies between the three legacy faculty databases.

### **2.5 User Stories (Summary)**
1.  **US-1:** As a **User**, I want to create a request to borrow an asset so that I can use it for my work or studies.
2.  **US-2:** As a **Department Administrator**, I want to approve or reject asset transfer requests within my department so that inventory is properly managed.
3.  **US-3:** As a **Faculty Administrator**, I want to generate an asset report by location so that I can audit inventory across departments.
4.  **US-4:** As an **Inventory Administrator**, I want to edit asset properties so that the inventory records remain accurate.
5.  **US-5:** As a **University Administrator**, I want to delegate permission to edit assets to another user so that tasks can be distributed.
6.  **US-6:** As an **IT Administrator**, I want to create a new space/location in the system so that the floor structure can be updated when needed.

### **2.6 Assumptions and Dependencies**
*   **Assumption:** University working hours are defined as 8:00 AM to 6:00 PM, Monday to Friday.
*   **Assumption:** All users will have reliable access to the internet and a compatible web browser.
*   **Dependency:** Successful data extraction and mapping from legacy faculty databases.
*   **Dependency:** Availability of the university's central authentication service API.
*   **Dependency:** IT infrastructure team will provision and maintain the required server environment.

---

## **3. System Features and Requirements**

### **3.1 Functional Requirements**

#### **3.1.1 Authentication & Authorization (FR-1)**
*   **FR-1.1:** The system shall require all users to authenticate using university credentials.
*   **FR-1.2:** The system shall determine the user's role(s) and permissions upon login.
*   **FR-1.3:** The system shall display only the menu options and functionalities permitted for the user's role.
*   **FR-1.4:** The system shall allow University and Faculty Administrators to delegate specific permissions to other users (Inventory Administrators) within their scope of authority.

#### **3.1.2 Asset Management (FR-2)**
*   **FR-2.1:** The system shall allow authorized administrators to add, modify, and decommission assets.
*   **FR-2.2:** The system shall store, at a minimum, the following asset properties: `Asset_ID`, `Type`, `Serial_Number`, `Location`, `Status` (e.g., Available, Checked-Out, Under Maintenance, Decommissioned), `Owner` (linked to University Structure).
*   **FR-2.3:** The system shall allow Inventory Administrators to update an asset's status to "Returned" upon physical return.

#### **3.1.3 Search Functionality (FR-3)**
*   **FR-3.1:** The system shall provide a simple search interface with a free-text field to search across asset name, type, and serial number.
*   **FR-3.2:** The system shall provide an advanced search interface allowing filtering by criteria such as Asset Type, Location (Building/Room), Status, Faculty, and Department.
*   **FR-3.3:** All search results shall respect the user's permission scope (e.g., a Department Admin cannot see assets from other faculties unless explicitly permitted).

#### **3.1.4 Request & Approval Workflow (FR-4)**
*   **FR-4.1:** The system shall allow Users to create a request for a single asset or space, specifying desired dates/times for borrowing/reservation.
*   **FR-4.2:** The system shall automatically route the request to the appropriate Department Administrator for approval.
*   **FR-4.3:** The system shall allow the designated administrator to approve or reject the request, optionally providing a reason.
*   **FR-4.4:** The system shall notify the requester via email and dashboard update upon approval or rejection.
*   **FR-4.5:** For inter-departmental or inter-faculty requests, the system shall escalate the request through the hierarchical approval chain (Dept -> Faculty -> University Admin as needed).

#### **3.1.5 Reporting (FR-5)**
*   **FR-5.1:** The system shall allow authorized administrators to generate pre-defined reports.
*   **FR-5.2:** Reports shall include, but not be limited to:
    *   Asset List by Location (Building/Department/Faculty).
    *   Asset Status Summary (Counts of Available, Checked-Out, etc.).
    *   Request History and Approval Statistics.
    *   Permission Delegation Audit Log.

#### **3.1.6 System Administration (FR-6)**
*   **FR-6.1:** The system shall allow IT Administrators to create and modify locations/spaces within the university hierarchy.
*   **FR-6.2:** The system shall provide an interface for IT Administrators to manage user-system roles and resolve exception requests flagged by the workflow.

### **3.2 Use Case Models (Key Processes)**
*   **UC-1: Authenticate User** (Trigger: Application Start)
*   **UC-2: Search for Asset** (Trigger: User Initiates Search)
*   **UC-3: Create Asset/Space Request** (Trigger: User Needs Asset/Space)
*   **UC-4: Approve/Reject Request** (Trigger: Pending Request Exists)
*   **UC-5: Modify Asset Properties** (Trigger: Asset Information Changes)
*   **UC-6: Process Asset Return** (Trigger: Asset is Physically Returned)
*   **UC-7: Generate Report** (Trigger: User Needs Report)

*(Detailed use case specifications with actors, pre/post-conditions, and basic flow should be developed in a separate or appendix document.)*

---

## **4. Non-Functional Requirements**

### **4.1 Usability**
*   **UF-1:** The web interface shall be intuitive enough for a user with basic internet and office software experience to learn core functions (search, create request) within **2 hours** and administrative functions within **4 hours** of guided use.
*   **UF-2:** The system shall provide contextual help tooltips and a searchable user manual.

### **4.2 Performance**
*   **PF-1:** The system shall support concurrent access by at least 100 users.
*   **PF-2:** Page load times for standard functions (login, search results, request form) shall be under **3 seconds** under normal load.
*   **PF-3:** **Database queries initiated by any user action shall be automatically terminated by the system if they exceed 60 seconds** to prevent system degradation.

### **4.3 Portability**
*   **PO-1:** The client-side web application shall be fully functional on the latest stable versions of the following browsers: **Google Chrome, Mozilla Firefox, Microsoft Edge, and Apple Safari**.

### **4.4 Security**
*   **SE-1:** All communication between the client browser and server shall be encrypted using TLS 1.2 or higher.
*   **SE-2:** Access to the application database server shall be restricted to the application server and the IT administration team only.
*   **SE-3:** The system shall implement role-based access control (RBAC). Permissions denied at a higher scope (e.g., Faculty) cannot be granted at a lower scope (e.g., Department).
*   **SE-4:** All user actions that modify data (add, edit, delete, approve) shall be logged in an audit trail with timestamp and user ID.

### **4.5 Availability & Maintainability**
*   **AV-1:** The system shall achieve **99% availability during defined university working hours (8:00 AM - 6:00 PM, Mon-Fri)**. Scheduled maintenance shall be conducted outside these hours with at least 48 hours notice.
*   **MA-1:** The system shall be designed with a modular architecture to facilitate future enhancements, such as adding new asset categories or report types.
*   **MA-2:** The codebase shall be documented according to agreed-upon internal standards.

---

## **5. Other Requirements**

### **5.1 Data Model (Preliminary)**
Core entity-relationship based on provided domain elements:
```sql
-- Simplified Core Tables --
User (User_ID PK, Name, Role, Department_FK, Auth_ID)
University_Structure (Unit_ID PK, Name, Type, Parent_Unit_ID FK) -- Represents University, Faculty, Department hierarchy
Asset (Asset_ID PK, Type, Serial_Number, Status, Location_FK, Owner_Unit_ID FK)
Location (Location_ID PK, Building, Room_Number, Owning_Unit_ID FK)
Request (Request_ID PK, Requester_ID FK, Asset_ID FK, Type, Status, Creation_Date, Approved_By_ID FK, Approval_Date)
Permission (Permission_ID PK, Granter_User_ID FK, Grantee_User_ID FK, Action_Type, Scope_Unit_ID FK, Expiry_Date)
```

### **5.2 Milestones and Dependencies**
1.  **M1:** SRS Finalization & Approval (Prerequisite for all development).
2.  **M2:** Core Architecture & Database Design Sign-off (Dependent on M1).
3.  **M3:** Completion of Phase 1 Development (Auth, Asset CRUD, Basic Search/Request).
4.  **M4:** User Acceptance Testing (UAT) Completion (Dependent on M3, requires stakeholder availability).
5.  **M5:** System Deployment & Go-Live (Dependent on successful UAT and IT infrastructure readiness).

### **5.3 Risks and Mitigation**
| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| Data inconsistency during migration from legacy systems | High | High | Conduct a thorough data audit and cleansing pre-migration. Use a staged, validated migration approach with rollback plans. |
| Aggressive project timeline leads to quality compromise | Medium | High | Adopt a phased delivery model (MVP). Prioritize core inventory/request features. Use agile methodologies for flexibility. |
| Complex permission model causes user confusion or errors | Medium | Medium | Develop a clear, visual permission management interface. Implement comprehensive logging and provide detailed training for administrators. |
| Low user adoption due to poor usability | Medium | Medium | Involve end-users in iterative UI/UX prototyping and testing. Develop clear, concise training materials and quick-start guides. |

### **5.4 Undecided Issues (To Be Resolved)**
1.  **UI-1:** Detailed schema for asset subtypes (e.g., technical specifications for IT equipment vs. furniture).
2.  **UI-2:** Definitive approval matrix for multi-asset, cross-faculty requests.
3.  **UI-3:** Specification for notification system (email templates, push notifications in UI, SMS).
4.  **UI-4:** Formal backup and disaster recovery plan (RTO/RPO).
5.  **UI-5:** Detailed filter set and UI design for the "Advanced Search" feature.
6.  **UI-6:** Standard Operating Procedure (SOP) for IT Admins to handle exception requests for unclassified assets/locations.

---
**END OF DOCUMENT**