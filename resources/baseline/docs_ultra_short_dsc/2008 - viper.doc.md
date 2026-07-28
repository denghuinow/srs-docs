# Software Requirements Specification (SRS)
## Supply Chain Management (SCM) System
### For Ejada Company

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft for Review  
**Prepared for:** Ejada Company  
**Prepared by:** [Your Name/Team Name]

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the Ejada Supply Chain Management (SCM) System. It serves as a formal agreement between the development team, stakeholders, and end-users regarding the system's capabilities, constraints, and behavior. The intended audience includes project managers, developers, testers, and Ejada's business representatives.

### 1.2 Scope
The SCM System is a custom, web-based application designed to manage the internal supply chain operations of Ejada Company. Its core purpose is to streamline the flow of customer requests, items, and supplier interactions to facilitate the efficient delivery of products and services.

**In-Scope:**
*   Management of customer and supplier master data.
*   Management of an internal item catalog.
*   Management of resource and storage locations.
*   End-to-end lifecycle management of customer requests.
*   Role-based access for Coordinators, Customers, and Suppliers.
*   Web-based user interface compatible with specified browsers.
*   Integration with a Microsoft SQL Server database.

**Out-of-Scope:**
*   Integration with external enterprise systems (e.g., CRM, HR, ERP). *(Noted for future consideration)*
*   Financial modules (e.g., invoicing, payment processing).
*   Advanced reporting and business intelligence analytics beyond basic status views.
*   Mobile-specific application development.

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **SCM** | Supply Chain Management |
| **Coordinator** | An Ejada employee with full administrative rights within the system. |
| **Customer** | An external entity that requests products or services from Ejada. |
| **Supplier** | An external entity that provides products or services to Ejada. |
| **Request** | A formal record of a Customer's need for a product or service. |
| **ASP.NET** | A web application framework developed by Microsoft. |
| **DBMS** | Database Management System |

### 1.4 References
*   Ejada .NET Framework Standards Document
*   Ejada Programming Standards Guide
*   Project Charter - Ejada SCM System

### 1.5 Overview
The remainder of this document is structured as follows:
*   **Section 2:** Provides a general description of the product, its users, and operating environment.
*   **Section 3:** Details all specific functional requirements.
*   **Section 4:** Details all non-functional requirements (performance, security, etc.).
*   **Appendix A:** May contain supplementary diagrams or data models.

## 2. Overall Description

### 2.1 Product Perspective
The SCM System is a new, self-contained module within Ejada's internal software framework. It is positioned as a tailored alternative to large-scale, generic solutions (e.g., Oracle, SAP). While initially standalone, its architecture anticipates future integration with two other planned modules within the same framework. The system interfaces directly with a Microsoft SQL Server database and is accessed by users via standard web browsers.

### 2.2 Product Functions (High-Level)
1.  **Identity and Access Management:** Secure login and role-based authorization.
2.  **Master Data Management:** CRUD (Create, Read, Update, Delete) operations for Customers, Suppliers, Items, and Locations.
3.  **Request Lifecycle Management:** Full lifecycle support for customer requests, from creation by a Customer, through coordination by a Coordinator, to feedback from Suppliers.
4.  **Supplier Portal:** Allows Suppliers to view relevant requests and submit fulfillment feedback.
5.  **Customer Portal:** Allows Customers to create and track their own requests and manage their profile.

### 2.3 User Characteristics
| User Class | Description | Technical Proficiency | Key Goals |
| :--- | :--- | :--- | :--- |
| **Coordinator** | Ejada internal staff. Primary system administrator and workflow manager. | High. Comfortable with complex data entry and management interfaces. | Efficiently match customer requests with supplier capabilities, maintain accurate system data, monitor overall supply chain status. |
| **Customer** | External client of Ejada. Uses the system to request services. | Medium. Assumed to be proficient with standard web browsing and form submission. | Easily submit new requests, clearly see the status of existing requests, maintain own contact information. |
| **Supplier** | External vendor for Ejada. Uses the system to receive business opportunities. | Medium. Assumed to be proficient with standard web browsing and form submission. | Quickly view new requests relevant to their business, understand request details, communicate ability to fulfill. |

### 2.4 Constraints
1.  **Technical:** The system must be developed using ASP.NET and C# on the .NET Framework.
2.  **Database:** Must use Microsoft SQL Server as the DBMS.
3.  **Architectural:** Must comply with Ejada's established programming standards and internal .NET framework.
4.  **Client-Side:** Must support Internet Explorer (versions 6 & 7) and Mozilla Firefox (versions 2 & 3).

### 2.5 Assumptions and Dependencies
*   **Assumptions:**
    *   A suitable Microsoft server operating system with a reliable internet connection will be provided for hosting.
    *   Users will have access to one of the supported web browsers.
*   **Dependencies:**
    *   The successful development and stability of the Ejada .NET framework.
    *   Future integration is dependent on the development of the two other planned Ejada modules.

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 User Interfaces
*   The system shall provide a professional, intuitive web-based interface.
*   The interface layout and navigation shall adapt based on the user's role (Coordinator, Customer, Supplier).
*   All data entry forms shall include appropriate validation and user feedback.

#### 3.1.2 Software Interfaces
*   **Database:** The system shall interface with **Microsoft SQL Server [Version to be specified]** using standard .NET data providers (e.g., ADO.NET, Entity Framework).
*   **Framework:** The application shall be built upon and integrate with the **Ejada .NET Framework**.

#### 3.1.3 Communication Interfaces
*   The system shall communicate over standard **TCP/IP** protocols via HTTP/HTTPS.
*   Client-server communication shall occur over the internet/company network.

### 3.2 Functional Requirements

#### 3.2.1 Authentication & Authorization (AUTH)
*   **AUTH-1:** The system shall require users to authenticate with a unique username and password.
*   **AUTH-2:** The system shall assign one of three distinct roles upon login: Coordinator, Customer, or Supplier.
*   **AUTH-3:** The system shall present a role-specific homepage and menu structure after successful login.

#### 3.2.2 Customer Management (CUST)
*   **CUST-1:** *Coordinator* shall be able to add a new Customer record, capturing at minimum: Company Name, Contact Person, Email, Phone, Address.
*   **CUST-2:** *Coordinator* shall be able to view, search, and filter the list of all Customers.
*   **CUST-3:** *Coordinator* shall be able to edit the details of any Customer.
*   **CUST-4:** *Coordinator* shall be able to deactivate/archive a Customer record (soft delete).
*   **CUST-5:** *Customer* shall be able to view and edit their own profile information.

#### 3.2.3 Supplier Management (SUPP)
*   **SUPP-1:** *Coordinator* shall be able to add a new Supplier record, capturing at minimum: Company Name, Contact Person, Email, Phone, Address, and Supplied Item Categories.
*   **SUPP-2:** *Coordinator* shall be able to view, search, and filter the list of all Suppliers.
*   **SUPP-3:** *Coordinator* shall be able to edit the details of any Supplier.
*   **SUPP-4:** *Coordinator* shall be able to deactivate/archive a Supplier record (soft delete).

#### 3.2.4 Item Catalog Management (ITEM)
*   **ITEM-1:** *Coordinator* shall be able to add a new Item to the catalog, capturing at minimum: Item Code, Description, Category, and Unit of Measure.
*   **ITEM-2:** *Coordinator* shall be able to view, search, and filter the list of all Items.
*   **ITEM-3:** *Coordinator* shall be able to edit the details of any Item.
*   **ITEM-4:** *Coordinator* shall be able to mark an Item as inactive in the catalog.

#### 3.2.5 Location Management (LOC)
*   **LOC-1:** *Coordinator* shall be able to define a new storage/resource Location, capturing at minimum: Location Code, Name, and Type (e.g., Warehouse, Office).
*   **LOC-2:** *Coordinator* shall be able to view, search, and filter the list of all Locations.
*   **LOC-3:** *Coordinator* shall be able to edit the details of any Location.
*   **LOC-4:** *Coordinator* shall be able to mark a Location as inactive.

#### 3.2.6 Request Management (REQ)
*   **REQ-1:** *Customer* shall be able to create a new Request, specifying required Items, quantities, and desired timeframe.
*   **REQ-2:** *Customer* shall be able to view a list of all Requests they have created, along with their current status (e.g., New, In Review, Sent to Supplier, Closed).
*   **REQ-3:** *Coordinator* shall be able to view, search, and filter all Requests from all Customers.
*   **REQ-4:** *Coordinator* shall be able to edit a Request (e.g., add internal notes, update priority, assign to a Supplier).
*   **REQ-5:** *Coordinator* shall be able to send a specific Request to one or more selected Suppliers for feedback.
*   **REQ-6:** *Supplier* shall, upon login, see a list of Requests that have been sent to them by the Coordinator and are pending feedback.
*   **REQ-7:** *Supplier* shall be able to view the full details of a Request sent to them.
*   **REQ-8:** *Supplier* shall be able to submit feedback for a Request, indicating their ability to fulfill (e.g., "Can Supply," "Cannot Supply") and optionally providing a quote or notes.
*   **REQ-9:** *Coordinator* shall be able to view all feedback submitted by Suppliers for a given Request.

### 3.3 Non-Functional Requirements

#### 3.3.1 Performance Requirements
*   **PERF-1:** The system shall support a minimum of **100 concurrent users** without significant degradation in response time.
*   **PERF-2:** For 90% of standard transactions (page loads, form submissions, searches), the system response time shall be **less than 1 second** under normal load conditions.

#### 3.3.2 Availability & Reliability
*   **AVAIL-1:** The system shall be designed for **100% operational availability**. Scheduled maintenance windows must be communicated in advance.
*   **RELI-1:** All system data shall be backed up automatically on a **daily** basis.
*   **RELI-2:** The system shall implement database transactions to ensure data integrity. Incomplete transactions due to system errors shall be automatically rolled back.

#### 3.3.3 Security Requirements
*   **SEC-1:** User passwords shall be stored in the database using industry-standard hashing algorithms (e.g., salted hash).
*   **SEC-2:** All user sessions shall timeout after a period of inactivity (e.g., 30 minutes).
*   **SEC-3:** The system shall enforce role-based access control (RBAC) as defined in Section 3.2.1, preventing users from accessing functionality or data outside their permissions.

#### 3.3.4 Maintainability & Supportability
*   **MAIN-1:** The system shall be developed in discrete, loosely-coupled modules (e.g., Authentication Module, Data Management Module, Request Module) to facilitate independent testing, debugging, and updating.

## 4. Appendices

### 4.1 Priority and Acceptance
All functional requirements specified in Section 3.2 are classified as **High Priority** and are required for the first release (Release 1.0). The non-functional requirements related to Performance (PERF-1, PERF-2), Availability (AVAIL-1), and Security (SEC-1, SEC-2, SEC-3) are **Critical Acceptance Criteria**. The system will be deemed acceptable only if it demonstrably meets these criteria during User Acceptance Testing (UAT).

### 4.2 Development Model
This project will follow a **Waterfall** process model, with sequential phases for Requirements, Design, Implementation, Verification, and Maintenance. This SRS document serves as the definitive requirements baseline for the Design phase.