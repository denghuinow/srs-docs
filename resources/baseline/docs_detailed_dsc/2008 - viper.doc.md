# Software Requirements Specification (SRS)
## Supply Chain Management (SCM) System
**For Ejada Company**
**Version:** 2.0
**Date:** October 26, 2023
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Ejada Supply Chain Management (SCM) System. It serves as a formal agreement between the project stakeholders, developers, and quality assurance teams, detailing what the system will do and the constraints under which it must operate. The intended audience includes project managers, business analysts, software architects, developers, testers, and system administrators.

#### 1.2 Scope
The SCM System is a web-based application designed to manage the flow of Ejada's products and services (IT products, business consultation, and other IT services). It facilitates coordination between Customers, Suppliers, and an internal Coordinator role to manage requests, procurement, and fulfillment.

**In-Scope (Release 1.0):**
*   User authentication and role-based access control (Coordinator, Customer, Supplier).
*   Management of master data (Customers, Suppliers, Items, Resource Locations).
*   End-to-end lifecycle management of Customer Requests.
*   Creation and management of Supply Requests sent to Suppliers.
*   Submission and management of Supplier Feedback.
*   Integration with the existing Ejada .NET Framework.
*   Deployment on Microsoft IIS with an MS SQL Server backend.

**Out-of-Scope:**
*   Integration with external enterprise systems (e.g., CRM, HR, Accounting).
*   Use by entities outside of Ejada and its designated partners.
*   Advanced reporting and business intelligence analytics.
*   Mobile-native applications.
*   Real-time inventory tracking with barcode/RFID.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **SCM:** Supply Chain Management.
*   **CRUD:** Create, Read, Update, Delete.
*   **RBAC:** Role-Based Access Control.
*   **IIS:** Internet Information Services.
*   **SLA:** Service Level Agreement.
*   **UI:** User Interface.
*   **API:** Application Programming Interface.

#### 1.4 References
*   Ejada Internal Development Standards Document.
*   Ejada .NET Framework Integration Guide.
*   Project Charter - SCM System.

#### 1.5 Overview
The remainder of this document is structured as follows:
*   **Section 2:** Overall description of the product, its users, and operating environment.
*   **Section 3:** Specific system requirements, including functional, interface, and non-functional requirements.

### 2. Overall Description

#### 2.1 Product Perspective
The SCM System is a new, self-contained module that will integrate with Ejada's existing .NET technology stack. It will operate within the corporate network, accessible via a web browser.

**System Interfaces:**
*   **Users:** Interact via a web browser (Chrome, Firefox, Edge).
*   **Database:** MS SQL Server for all persistent data storage.
*   **Application Server:** Hosted on Microsoft IIS.
*   **Framework:** Built upon and integrated with the Ejada .NET Framework.

#### 2.2 Product Functions (Summary)
1.  **User Management:** Secure login and profile management for three distinct roles.
2.  **Master Data Management:** CRUD operations for Customer, Supplier, Item, and Resource Location entities (Coordinator role).
3.  **Request Management:**
    *   Customers can create, view, and track requests.
    *   Coordinators can review, assign, and manage the status of all requests.
4.  **Supply Chain Coordination:**
    *   Coordinators can create Supply Requests from Customer Requests.
    *   Suppliers can view Supply Requests and submit Feedback (feasibility, timeline).
5.  **Notification System:** Alert relevant users about key state changes (e.g., new request, new feedback).

#### 2.3 User Characteristics
| Role | Skill Level | Key Responsibilities | Frequency of Use |
| :--- | :--- | :--- | :--- |
| **Coordinator** (Ejada Employee) | High computer literacy. Understands SCM processes. | System administration, orchestrating requests, managing suppliers and inventory. | Daily |
| **Customer** (Ejada Client) | Basic web navigation skills. | Submitting and tracking service/product requests. | Weekly/Monthly |
| **Supplier** (Vendor/Partner) | Basic web navigation skills. | Responding to supply requests and managing profile. | As requests are received |

#### 2.4 Constraints
1.  **Technical:** Must be developed using ASP.NET (C#) and MS SQL Server.
2.  **Architectural:** Must comply with and integrate into the existing Ejada .NET Framework.
3.  **Business:** Initial release scope is frozen; no CRM/HR integration.
4.  **Regulatory:** Must adhere to Ejada's internal data security and coding standards.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** Users will have access to a compatible modern web browser.
*   **Assumption:** The Ejada .NET Framework will be stable and supported for the project duration.
*   **Dependency:** Availability of the MS SQL Server database environment.
*   **Dependency:** Network infrastructure to support web access for external Suppliers and Customers.

### 3. Specific Requirements

#### 3.1 Functional Requirements

**3.1.1 User Authentication & Authorization (FUN-AUTH)**
*   **FUN-AUTH-001:** The system shall present a login page to all unauthenticated users.
*   **FUN-AUTH-002:** The system shall authenticate users against credentials stored in the database.
*   **FUN-AUTH-003:** The system shall enforce Role-Based Access Control (RBAC), redirecting users to a role-specific homepage upon successful login (Coordinator, Customer, or Supplier dashboard).
*   **FUN-AUTH-004:** The system shall terminate a user session after a period of inactivity (timeout to be configured).
*   **FUN-AUTH-005:** The system shall allow users to log out, terminating their session.

**3.1.2 Coordinator Management Functions (FUN-COORD)**
*   **FUN-COORD-010:** The Coordinator shall be able to Create, Read, Update, and Delete (CRUD) Customer records.
*   **FUN-COORD-011:** The Coordinator shall be able to CRUD Supplier records.
*   **FUN-COORD-012:** The Coordinator shall be able to CRUD Item records (including Quantity for inventory).
*   **FUN-COORD-013:** The Coordinator shall be able to CRUD Resource Location records.
*   **FUN-COORD-014:** The system shall display a list of all pending Customer Requests to the Coordinator.
*   **FUN-COORD-015:** The Coordinator shall be able to view the full details of any Customer Request.
*   **FUN-COORD-016:** The Coordinator shall be able to update the Status of a Customer Request (e.g., Pending, In Review, Sourced, In Fulfillment, Completed, Cancelled).
*   **FUN-COORD-017:** From a Customer Request detail view, the Coordinator shall be able to create a new Supply Request to be sent to a selected Supplier.
*   **FUN-COORD-018:** The Coordinator shall be able to view all Feedback submitted by Suppliers.
*   **FUN-COORD-019:** The system shall log all delete actions performed by a Coordinator (entity and user who performed it).

**3.1.3 Customer Functions (FUN-CUST)**
*   **FUN-CUST-020:** The Customer shall be able to view and edit their own profile information (Name, Contact, Email, etc.).
*   **FUN-CUST-021:** The Customer shall be able to create a new Request by filling a form with at least a Description field.
*   **FUN-CUST-022:** Upon submission, the Customer Request shall be saved with a "Pending" status and the assigned Coordinator shall be notified.
*   **FUN-CUST-023:** The Customer shall be able to view a list of their own submitted Requests.
*   **FUN-CUST-024:** The Customer shall be able to view the details and current Status of their own Requests.

**3.1.4 Supplier Functions (FUN-SUPP)**
*   **FUN-SUPP-030:** The Supplier shall be able to view and edit their own profile information.
*   **FUN-SUPP-031:** The Supplier shall be able to view a list of Supply Requests assigned to them by the Coordinator.
*   **FUN-SUPP-032:** The Supplier shall be able to view the details of a specific Supply Request.
*   **FUN-SUPP-033:** On a Supply Request detail page, the Supplier shall be able to submit Feedback, including textual content regarding feasibility and estimated timeline.
*   **FUN-SUPP-034:** Upon submission, the Feedback shall be saved and linked to the Request, and the responsible Coordinator shall be notified.

**3.1.5 Data Validation (FUN-VAL)**
*   **FUN-VAL-040:** The system shall validate all user input on the client and server side.
*   **FUN-VAL-041:** The system shall prevent the submission of forms with required fields left blank.
*   **FUN-VAL-042:** The system shall display clear, user-friendly error messages next to the problematic field(s).

#### 3.2 External Interface Requirements

**3.2.1 User Interfaces (UI)**
*   **UI-001:** The system shall provide a responsive, role-based web interface compatible with major browsers (Chrome, Firefox, Edge).
*   **UI-002:** Each role shall have a distinct navigation menu providing access to their permitted functions.
*   **UI-003:** All data entry shall be done through clearly labeled forms.
*   **UI-004:** Lists of entities (e.g., Requests, Customers) shall be paginated if they exceed 25 items.

**3.2.2 Hardware Interfaces**
*   None specified. Standard web server and database server hardware is assumed.

**3.2.3 Software Interfaces (SI)**
*   **SI-001: Database:** The system shall interface with MS SQL Server 2019 or later via ADO.NET or Entity Framework.
*   **SI-002: Application Server:** The system shall be deployed as an ASP.NET application on Microsoft IIS 10 or later.
*   **SI-003: Framework:** The system shall reference and utilize shared libraries from the Ejada .NET Framework as specified in the integration guide.

**3.2.4 Communications Interfaces**
*   The system shall use HTTP/HTTPS protocols for all browser communication.

#### 3.3 Non-Functional Requirements

**3.3.1 Performance Requirements (PERF)**
*   **PERF-001:** The system shall support at least 100 concurrent users.
*   **PERF-002:** 90% of all database transactions shall complete in under 1 second.
*   **PERF-003:** 95% of web page loads shall complete in under 3 seconds under normal load.

**3.3.2 Reliability Requirements (REL)**
*   **REL-001:** The system shall have an operational uptime of 99.5% during business hours (8 AM - 6 PM, Sunday-Thursday).
*   **REL-002:** The system shall implement atomic database transactions to ensure data integrity. Failed transactions shall be rolled back completely.
*   **REL-003:** Automated daily full backups of the database shall be performed.

**3.3.3 Security Requirements (SEC)**
*   **SEC-001:** All passwords shall be hashed and salted before storage in the database.
*   **SEC-002:** All user sessions shall be managed via secure, HTTP-only session cookies.
*   **SEC-003:** Direct access to role-specific pages shall be blocked if the user's role does not permit it (e.g., a Customer trying to access a Coordinator management page).
*   **SEC-004:** All system errors shall be logged for administrative review but shall not reveal stack traces or database details to end-users.

**3.3.4 Compliance Requirements**
*   The source code shall adhere to Ejada's internal C# coding standards and .NET design guidelines.

### 4. System Models (Appendices)

#### 4.1 Use Case Diagrams & Descriptions
*(A textual representation based on provided scenarios)*

**Use Case UC-01: Manage Master Data**
*   **Actor:** Coordinator
*   **Description:** Coordinator performs CRUD operations on Customer, Supplier, Item, and Location records.
*   **Precondition:** Coordinator is logged in.
*   **Postcondition:** The master data is updated in the system.
*   **Exception:** If deletion is attempted, a confirmation prompt is shown and the action is logged.

**Use Case UC-02: Submit Customer Request**
*   **Actor:** Customer
*   **Description:** Customer creates and submits a new product/service request.
*   **Precondition:** Customer is logged in.
*   **Postcondition:** A new Request with "Pending" status is created and the Coordinator is notified.
*   **Exception:** Invalid form data prevents submission and shows errors.

**Use Case UC-03: Provide Supplier Feedback**
*   **Actor:** Supplier
*   **Description:** Supplier submits feedback on a Supply Request assigned to them.
*   **Precondition:** Supplier is logged in and has pending requests.
*   **Postcondition:** Feedback is saved and linked to the request; Coordinator is notified.
*   **Exception:** Empty feedback submission is rejected.

#### 4.2 Domain Model / Data Dictionary
```csharp
// Core Entity Overview
public class User {
    int UserID; // PK, Required, Unique
    string Password; // Required, Hashed
    string Domain; // Required: "Coordinator", "Customer", "Supplier"
}
public class Customer : User {
    string Name; // Required
    string Address;
    string ContactPerson;
    string Email;
}
public class Supplier : User {
    string Name; // Required
    string Address;
    string ContactPerson;
    string Email;
}
public class Coordinator : User { }

public class Request {
    int RequestID; // PK, Required, Unique
    string Description;
    string Status; // e.g., "Pending", "In Review", etc.
    int CustomerID; // FK to Customer
    int CoordinatorID; // FK to Coordinator (assigned)
    DateTime CreatedDate;
}
public class Item {
    int ItemID; // PK, Required, Unique
    string Name;
    string Description;
    int Quantity; // Inventory level
}
public class ResourceLocation {
    int LocationID; // PK, Required, Unique
    string Name;
    string Address;
}
public class Feedback {
    int FeedbackID; // PK, Required, Unique
    string Content; // Required
    DateTime SubmissionDate;
    int RequestID; // FK to Request
    int SupplierID; // FK to Supplier
}
```

#### 4.3 Business Process Flow
**Primary Flow: Fulfill Customer Request**
1.  Customer submits request (UC-02).
2.  System notifies Coordinator.
3.  Coordinator reviews request (UC-01 variant).
4.  **Decision Point:** Items in inventory?
    *   **Yes (Branch B):** Allocate items, update inventory, proceed to step 7.
    *   **No:** Proceed to step 5.
5.  Coordinator creates and sends Supply Request to a Supplier.
6.  Supplier provides Feedback (UC-03). System notifies Coordinator.
    *   **Loop:** If feedback is negative/partial, Coordinator may revise request and send to another supplier (back to step 5).
7.  Coordinator updates Customer Request status and manages fulfillment.
8.  Process ends with request status "Fulfilled" or "Cancelled".

### 5. Acceptance Criteria (Key Examples)
*   **AC-01 (Customer Submission):** Given a valid customer session, when the customer completes the "New Request" form and clicks submit, then a new record appears in the `Request` table with `Status='Pending'` and the assigned coordinator can see it in their pending requests list.
*   **AC-02 (Supplier Feedback):** Given a supplier viewing a specific supply request, when they enter "Can supply within 14 days" in the feedback box and submit, then a new record appears in the `Feedback` table linked to that request and supplier, and the request's coordinator receives a notification.
*   **AC-03 (Coordinator Deletion):** Given a coordinator on the customer management page, when they click "Delete" for a customer, then a modal dialog asks "Are you sure you want to delete [Customer Name]?" and upon confirmation, the customer record is marked inactive (or deleted) and an entry is made in an audit log.

### 6. Undecided Issues & Risks
*   Refer to the separate "Undecided Issues and Responsible Parties" and "Risk List and Mitigation Strategies" sections from the input summary. These are integral to project planning and must be resolved per the assigned responsibilities.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner | | | |
| Project Manager | | | |
| System Architect | | | |
| QA Lead | | | |