# Software Requirements Specification (SRS)
## Supply Chain Management System (SCMS) - Ejada
**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Ejada Supply Chain Management System (SCMS). It is intended for use by the project stakeholders, including Ejada management, development team, quality assurance, and system integrators, to ensure a common understanding of the system to be developed.

#### 1.2 Document Conventions
*   **Requirements IDs:** Follow the format `FR-XXX` for Functional Requirements and `NFR-XXX` for Non-Functional Requirements.
*   **Priority:** (H) High, (M) Medium, (L) Low.
*   **Keywords:** `MUST`, `SHALL`, `WILL` indicate mandatory requirements. `SHOULD`, `COULD`, `MAY` indicate desirable but not mandatory features.

#### 1.3 Project Scope
The SCMS is a web-based application designed to centralize and streamline the coordination of product and service delivery between Ejada's internal coordinators, external customers, and suppliers. The system will manage the lifecycle of requests, maintain critical master data, and facilitate communication and feedback within the supply chain.

**In-Scope:**
*   Web-based user interfaces for Coordinators, Customers, and Suppliers.
*   Management of Customer and Supplier Requests (CRUD operations).
*   Management of master data entities (Customers, Suppliers, Items, Resource Locations).
*   Supplier portal for viewing requests and submitting feedback.
*   Integration with two specified existing Ejada .NET modules.
*   Hosting on Ejada's approved infrastructure.

**Out-of-Scope:**
*   Mobile-native applications (responsive web design is in-scope).
*   Financial processing, invoicing, or payment gateways.
*   Advanced Business Intelligence (BI) or predictive analytics.
*   Real-time GPS tracking of shipments.
*   Development of the two existing modules to be integrated with.

#### 1.4 References
*   Ejada Enterprise Architecture Guidelines v4.2
*   .NET Framework Integration Standards
*   MS SQL Server 2019+ Deployment Handbook

---

### 2. Overall Description

#### 2.1 Product Perspective
The SCMS is a new module that will integrate into Ejada's existing .NET-based enterprise ecosystem. It will interact with two other modules (e.g., a User Directory/Authentication module and an Inventory module, to be specified during design). The system will be a self-contained web application with a dedicated MS SQL Server database.

#### 2.2 User Classes and Characteristics
| User Class | Description | Key Characteristics |
| :--- | :--- | :--- |
| **System Administrator** | IT staff managing system configuration, users, and roles. | Technical expertise, low user volume. |
| **Coordinator (Ejada Staff)** | Primary internal user. Creates requests, manages master data, oversees fulfillment. | High daily usage, requires efficient workflows. |
| **Customer** | External entity requesting products/services. | Variable usage, needs simple, clear interface. |
| **Supplier** | External entity fulfilling requests. | Needs clear view of relevant requests and easy feedback mechanism. |

#### 2.3 Operating Environment
*   **Server:** Windows Server 2019/2022, IIS 10+, .NET Framework 4.8 or .NET 6+ (as per Ejada standard).
*   **Database:** Microsoft SQL Server 2019 or later.
*   **Client:** Modern web browsers (Chrome 90+, Edge 90+, Firefox 88+, Safari 14+) with JavaScript enabled.
*   **Network:** Accessible via Ejada's corporate intranet and a secured extranet for customers/suppliers.

#### 2.4 Design and Implementation Constraints
1.  **C-1:** The application **MUST** be developed using ASP.NET (Web Forms or MVC) and C#.
2.  **C-2:** The data persistence layer **MUST** use Microsoft SQL Server.
3.  **C-3:** The system **MUST** integrate seamlessly with Ejada's existing .NET framework and two other specified .NET modules via defined APIs or shared libraries.
4.  **C-4:** The user interface **MUST** be consistent with Ejada's corporate web application style guide.

#### 2.5 Assumptions and Dependencies
*   **AS-1:** Ejada's network and security infrastructure will provide secure access for external users (customers/suppliers).
*   **AS-2:** The teams responsible for the two existing modules will provide stable integration points and documentation.
*   **DE-1:** Successful deployment depends on the availability of the approved staging and production server environments.

---

### 3. System Features and Requirements

#### 3.1 User Authentication and Authorization
*   **FR-1:** The system **SHALL** integrate with Ejada's existing user directory for authentication. (Priority: H)
*   **FR-2:** The system **SHALL** support role-based access control (RBAC) with at least the following roles: Administrator, Coordinator, Customer, Supplier. (Priority: H)

#### 3.2 Master Data Management
*   **FR-10:** The system **SHALL** allow authorized users (Coordinators, Admins) to Create, Read, Update, and Deactivate records for **Customers**. (Priority: H)
    *   *Fields: Customer ID (auto), Name, Contact Info, Address, Status, etc.*
*   **FR-11:** The system **SHALL** allow authorized users to perform CRUD operations on **Supplier** records. (Priority: H)
*   **FR-12:** The system **SHALL** allow authorized users to manage an **Item** catalog (Products/Services). (Priority: H)
*   **FR-13:** The system **SHALL** allow authorized users to manage **Resource Locations** (e.g., warehouses, offices). (Priority: M)

#### 3.3 Request Management
*   **FR-20:** A Coordinator **SHALL** be able to create a new request, linking it to a Customer, Supplier, Item(s), and Locations. (Priority: H)
*   **FR-21:** The system **SHALL** provide a dashboard for Coordinators to view, filter, and search all requests. (Priority: H)
*   **FR-22:** A Coordinator **SHALL** be able to edit or cancel (soft delete) requests within a permitted status window. (Priority: H)
*   **FR-23:** A Customer **SHALL** be able to view the status of requests linked to their account. (Priority: M)
*   **FR-24:** A Supplier **SHALL** be able to view a list of requests assigned to them. (Priority: H)

#### 3.4 Supplier Feedback Module
*   **FR-30:** On the supplier request view, the system **SHALL** display a form for the supplier to submit feedback. (Priority: H)
*   **FR-31:** Supplier feedback **SHALL** include fields for status update (e.g., "Acknowledged", "In Progress", "Shipped"), estimated completion date, and notes. (Priority: H)
*   **FR-32:** The system **SHALL** notify the relevant Coordinator via the dashboard or internal alert when a supplier submits feedback. (Priority: M)

#### 3.5 Integration
*   **FR-40:** The system **SHALL** expose or consume APIs/web services to exchange data with the two specified existing Ejada modules. (Priority: H)
    *   *Integration specifics (data points, frequency, format) to be defined in a separate Interface Control Document (ICD).*

---

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
*   **NFR-1:** The system **MUST** support at least **100 concurrent users** without significant degradation in performance (<2 sec response time for core transactions). (Priority: H)
*   **NFR-2:** Page load times for the main dashboard **SHALL** be under 3 seconds under normal load (50 concurrent users). (Priority: M)

#### 4.2 Security Requirements
*   **NFR-10:** All authentication **MUST** occur over HTTPS/TLS 1.2+. (Priority: H)
*   **NFR-11:** The system **SHALL** prevent SQL injection and Cross-Site Scripting (XSS) vulnerabilities. (Priority: H)
*   **NFR-12:** Customer and Supplier users **SHALL** only have access to data explicitly linked to their accounts. (Priority: H)

#### 4.3 Reliability & Availability
*   **NFR-20:** The system **SHALL** have an operational uptime of 99.5% during core business hours (08:00 - 18:00 GMT+3). (Priority: M)
*   **NFR-21:** Database transactions **SHALL** follow ACID properties to ensure data integrity. (Priority: H)

#### 4.4 Usability
*   **NFR-30:** The user interface for Customers and Suppliers **SHALL** be intuitive and require minimal training (<30 mins of guided exploration). (Priority: M)
*   **NFR-31:** The application **SHALL** be fully navigable via keyboard. (Priority: L)

#### 4.5 Maintainability & Support
*   **NFR-40:** The C# source code **SHALL** be documented following Ejada's internal commenting standards. (Priority: M)
*   **NFR-41:** Database schema scripts (CREATE, ALTER) **SHALL** be version-controlled. (Priority: H)

---

### 5. Appendices

#### 5.1 Glossary
| Term | Definition |
| :--- | :--- |
| **CRUD** | Create, Read, Update, Delete - the four basic data operations. |
| **Master Data** | The core, non-transactional data entities critical to business operations (e.g., Customer, Supplier). |
| **Request** | A transaction representing a demand for a product or service from a customer, to be fulfilled by a supplier. |
| **Coordinator** | An Ejada employee who manages the flow of requests between customers and suppliers. |

#### 5.2 Data Model (Preliminary)
A high-level entity-relationship diagram will be developed during the design phase. Core entities include:
*   **User** (linked to directory)
*   **Customer**
*   **Supplier**
*   **Item**
*   **ResourceLocation**
*   **Request** (with foreign keys to Customer, Supplier, Item, Location, and status history)
*   **Feedback** (linked to Request and Supplier)

#### 5.3 Open Issues
*   The specific two .NET modules for integration are to be formally identified.
*   The exact API contract and authentication method for external users (Customers/Suppliers) needs final security review.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner | *[To be filled]* | | |
| Lead Architect | *[To be filled]* | | |
| Project Manager | *[To be filled]* | | |