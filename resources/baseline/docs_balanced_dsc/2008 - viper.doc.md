# Software Requirements Specification (SRS)
## Ejada Supply Chain Management (SCM) System
**Version:** 2.0  
**Date:** [Date of Document Creation]  
**Status:** Draft for Review

---

### **1. Introduction**

#### **1.1 Purpose**
This document defines the functional and non-functional requirements for the Ejada Supply Chain Management (SCM) System. It serves as a formal agreement between the development team, project stakeholders, and management, providing a comprehensive blueprint for system design, development, and testing. The intended audience includes project managers, software architects, developers, testers, and system administrators.

#### **1.2 Document Conventions**
*   **Bold text** is used for emphasis and key terms.
*   *Italic text* may be used for notes or references.
*   Requirements are uniquely identified as `FR-XXX` (Functional) or `NFR-XXX` (Non-Functional).
*   Code and database elements are presented in `inline code` blocks.

#### **1.3 Project Scope**
The SCM System is a web-based application designed to streamline Ejada's internal supply chain operations. Its core purpose is to digitize and centralize the management of requests, items, customers, and suppliers, thereby improving coordination, visibility, and efficiency.

**In-Scope:**
*   A secure, role-based web portal for Coordinators, Customers, and Suppliers.
*   Management of master data (Customers, Suppliers, Items, Resource Locations).
*   End-to-end lifecycle management of supply `Requests` (creation, assignment, feedback, tracking).
*   User profile management.
*   Basic reporting and list views.

**Out-of-Scope:**
*   Financial transactions, invoicing, or payment processing.
*   Advanced analytics or predictive forecasting.
*   Real-time GPS tracking of shipments.
*   Mobile-native applications (system is browser-based).
*   Direct integration with external third-party logistics (3PL) systems (beyond supplier feedback via the portal).

#### **1.4 References**
*   Ejada Corporate IT Standards & .NET Framework Guidelines
*   Initial Project Charter: "Balanced Summary: Supply Chain Management (SCM) System"

---

### **2. Overall Description**

#### **2.1 Product Perspective**
The SCM System is a new, self-contained module within the Ejada enterprise ecosystem. It will initially operate as a standalone web application but is architected for future integration with other corporate systems (e.g., CRM, HR). It depends on Ejada's central .NET framework and authentication standards.

#### **2.2 User Classes and Characteristics**
| User Class | Characteristics | Key Responsibilities |
| :--- | :--- | :--- |
| **Coordinator** (Internal User) | Ejada employee. Technically proficient. Requires full system control. Manages the supply chain workflow. | Create/manage `Requests`. Manage `Customer`, `Supplier`, `Item`, and `ResourceLocation` master data. Oversee request status. |
| **Customer** (External User) | Business client of Ejada. Varying technical skill. Needs simple, clear interface. | Submit and track personal `Requests`. Update own `Customer` profile information. |
| **Supplier** (External User) | Vendor/partner of Ejada. Needs timely information to fulfill demands. | View assigned/pending `Requests`. Submit feedback on capability and timelines. |

#### **2.3 Operating Environment**
*   **Server:** Microsoft Windows Server with Internet Information Services (IIS) and the required .NET Framework.
*   **Database:** Microsoft SQL Server.
*   **Client:** Web browsers: Mozilla Firefox (latest stable version) and Microsoft Internet Explorer (version as per Ejada IT policy).
*   **Development:** ASP.NET (Web Forms or MVC), C#.

#### **2.4 Design and Implementation Constraints**
1.  The system **must** be developed using ASP.NET, C#, and MS SQL Server (`NFR-005`).
2.  The system **must** adhere to Ejada's internal .NET programming standards and framework for integration (`NFR-005`).
3.  The user interface **must** be compatible with specified browsers (`NFR-006`).

#### **2.5 Assumptions and Dependencies**
*   **Assumption:** Users will have reliable internet access.
*   **Assumption:** Coordinators will be trained on system procedures.
*   **Dependency:** Availability of the Ejada .NET framework and approved development environment.
*   **Dependency:** Server infrastructure meeting the specified OS and software requirements.

---

### **3. System Features and Requirements**

#### **3.1 Feature: User Authentication and Role-Based Access**
**Description:** Secure login and session management directing users to domain-specific functionality.

**3.1.1 Functional Requirements:**
*   `FR-101`: The system shall present a login page requesting Username, Password, and User Domain (Coordinator, Customer, Supplier).
*   `FR-102`: The system shall validate credentials against the `Coordinator`, `Customer`, and `Supplier` tables.
*   `FR-103`: Upon successful authentication, the system shall redirect the user to a dashboard tailored to their domain.
*   `FR-104`: The system shall provide a secure logout mechanism that terminates the user session.

#### **3.2 Feature: Coordinator Dashboard & Master Data Management**
**Description:** Central interface for Coordinators to oversee and manage all core supply chain entities.

**3.2.1 Functional Requirements:**
*   `FR-201`: The system shall allow a Coordinator to create, read, update, and delete (CRUD) records in the `Customer` table.
*   `FR-202`: The system shall allow a Coordinator to create, read, update, and delete (CRUD) records in the `Supplier` table.
*   `FR-203`: The system shall allow a Coordinator to create, read, update, and delete (CRUD) records in the `Item` table.
*   `FR-204`: The system shall allow a Coordinator to create, read, update, and delete (CRUD) records in the `ResourceLocation` table.
*   `FR-205`: The system shall provide a "View All Customers" list, displaying `CustomerID`, Name, ContactPerson, and Email.
*   `FR-206`: The system shall allow a Coordinator to assign a `Request` to a `Supplier`.

#### **3.3 Feature: Request Lifecycle Management**
**Description:** End-to-end process for creating, tracking, and fulfilling supply requests.

**3.3.1 Functional Requirements:**
*   `FR-301`: The system shall allow a Coordinator to create a new `Request` on behalf of a `Customer`, linking it to a `Supplier` and describing required `Items`. *(Supports User Story #1)*
*   `FR-302`: The system shall allow a Customer to create a new `Request`, providing a Description and linking it to their own `CustomerID`. *(Supports User Story #3)*
*   `FR-303`: Each `Request` shall have a `Status` (e.g., "New", "Assigned", "Supplier Feedback Received", "In Fulfillment", "Closed").
*   `FR-304`: The system shall allow a Supplier to view a list of `Requests` where `SupplierID` matches their ID and `Status` is "Assigned" or similar. *(Supports User Story #5)*
*   `FR-305`: The system shall allow a Supplier to submit feedback (e.g., text comment, proposed delivery date) on a `Request`, which updates the request's `Status` and records the feedback. *(Supports User Story #6)*
*   `FR-306`: The system shall allow a Coordinator to view the status and history of all `Requests`.

#### **3.4 Feature: User Self-Service Profile Management**
**Description:** Allows Customers and Suppliers to manage their own contact information.

**3.4.1 Functional Requirements:**
*   `FR-401`: The system shall allow a Customer to view and edit their own record in the `Customer` table (Name, Address, ContactPerson, Email). *(Supports User Story #4)*
*   `FR-402`: The system shall allow a Supplier to view and edit their own record in the `Supplier` table (Name, Address, ContactPerson, Email).

---

### **4. External Interface Requirements**

#### **4.1 User Interfaces**
*   The UI shall be clean, professional, and intuitive, using Ejada's corporate color scheme and branding.
*   All data entry forms shall include clear validation and error messages.
*   Navigation shall be consistent, with a main menu relevant to the user's domain.

#### **4.2 Hardware Interfaces**
*   None specified. Standard web server and client hardware are assumed.

#### **4.3 Software Interfaces**
*   **Database:** The application shall interface with a single MS SQL Server database.
*   **Framework:** The application shall be built upon and integrate with the existing Ejada .NET framework.

#### **4.4 Communications Interfaces**
*   The application shall use HTTP/HTTPS protocols for web communication.
*   *Undecided Issue #1:* Specific notification channels (email/SMS/in-app alerts) are TBD.

---

### **5. Non-Functional Requirements**

#### **5.1 Performance Requirements**
*   `NFR-001`: The system shall support at least **100 concurrent users** without significant degradation in performance.
*   `NFR-002`: **90% of all transactional operations** (e.g., login, saving a request, updating a profile) shall complete in **less than 1 second** under normal load.

#### **5.2 Safety and Security Requirements**
*   User passwords shall be stored using industry-standard hashing algorithms (e.g., bcrypt).
*   All user sessions shall timeout after a period of inactivity (e.g., 30 minutes).
*   Role-based access control (RBAC) shall be strictly enforced; a Customer shall not access Supplier or Coordinator functions.

#### **5.3 Software Quality Attributes**
*   **Availability (`NFR-003`):** The system shall target 100% operational uptime during business hours. Any errors must provide clear, user-friendly feedback to the user and log details for administrators.
*   **Reliability:** Database transactions shall be atomic, consistent, isolated, and durable (ACID). Rollback mechanisms shall be in place for failed operations.
*   **Maintainability:** Code shall be well-documented and follow Ejada's coding standards.
*   **Scalability:** The architecture shall be designed to allow for scaling to meet `NFR-001`.

#### **5.4 Business Rules**
*   A `Request` must be associated with one `Customer`.
*   A `Request` can be associated with one `Supplier` (optional at creation, mandatory for fulfillment).
*   A `Customer` or `Supplier` can only modify their own profile record.

---

### **6. Data Model**
The system will implement the following core entities and relationships, based on the provided domain elements.

```sql
-- Simplified Schema Representation
CREATE TABLE Coordinator (
    CoordinatorID INT PRIMARY KEY IDENTITY,
    Username NVARCHAR(50) UNIQUE NOT NULL,
    PasswordHash NVARCHAR(255) NOT NULL,
    Domain NVARCHAR(20) NOT NULL CHECK (Domain IN ('Coordinator'))
);

CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY IDENTITY,
    Name NVARCHAR(100) NOT NULL,
    Address NVARCHAR(255),
    ContactPerson NVARCHAR(100),
    Email NVARCHAR(100)
);

CREATE TABLE Supplier (
    SupplierID INT PRIMARY KEY IDENTITY,
    Name NVARCHAR(100) NOT NULL,
    Address NVARCHAR(255),
    ContactPerson NVARCHAR(100),
    Email NVARCHAR(100)
);

CREATE TABLE Item (
    ItemID INT PRIMARY KEY IDENTITY,
    Name NVARCHAR(100) NOT NULL,
    Description NVARCHAR(MAX),
    Category NVARCHAR(50)
);

CREATE TABLE ResourceLocation (
    LocationID INT PRIMARY KEY IDENTITY,
    Name NVARCHAR(100) NOT NULL,
    Address NVARCHAR(255),
    Type NVARCHAR(50) -- e.g., 'Warehouse', 'Factory'
);

CREATE TABLE Request (
    RequestID INT PRIMARY KEY IDENTITY,
    Description NVARCHAR(MAX) NOT NULL,
    Status NVARCHAR(50) NOT NULL DEFAULT 'New',
    CustomerID INT NOT NULL FOREIGN KEY REFERENCES Customer(CustomerID),
    SupplierID INT NULL FOREIGN KEY REFERENCES Supplier(SupplierID),
    DateCreated DATETIME NOT NULL DEFAULT GETDATE(),
    FeedbackText NVARCHAR(MAX) NULL
    -- Note: A more robust design might link Items to Requests via a junction table.
);
```

---

### **7. Appendices**

#### **Appendix A: Glossary**
*   **SCM:** Supply Chain Management.
*   **CRUD:** Create, Read, Update, Delete.
*   **PK:** Primary Key.
*   **FK:** Foreign Key.
*   **ACID:** Atomicity, Consistency, Isolation, Durability (database transaction properties).

#### **Appendix B: Analysis Models**
*   *Use Case Diagrams, Activity Diagrams, or Wireframes would be included here in a full SRS.*

#### **Appendix C: Issues List (Undecided/TBD)**
1.  **Notification Channels:** The specific medium (email, in-app alert, SMS) for system notifications needs to be determined.
2.  **List Filtering:** Advanced filtering and sorting capabilities for list views (e.g., Requests by date range, Items by Category) require detailed specification.
3.  **Request Edit Locking:** Business rule needed: Should a Customer be able to edit a `Request` after a Coordinator has acknowledged or acted upon it?
4.  **Profile Change Notification:** Process for alerting relevant users (e.g., Coordinator) when a Customer or Supplier edits their profile.
5.  **No-Supplier Scenario:** Define the system workflow when a `Request` cannot be assigned to an available `Supplier`.
6.  **QA Procedures:** Detailed test plans, including performance/load testing and user acceptance testing (UAT) criteria, need to be developed.