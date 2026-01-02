# Software Requirements Specification (SRS)
## Ejada Supply Chain Management (SCM) System

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft for Review  
**Prepared for:** Ejada Stakeholders  
**Prepared by:** [Your Name/Department]

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the Ejada Supply Chain Management (SCM) System. It serves as a formal agreement between stakeholders, project managers, and the development team regarding the system's capabilities, constraints, and intended behavior. The primary audience includes project sponsors, business analysts, software architects, developers, and quality assurance teams.

### 1.2 Scope
The Ejada SCM System is a web-based application designed to manage the end-to-end supply chain processes internal to Ejada's operations. The system's scope is explicitly limited to:
*   Managing product and service requests from external customers.
*   Managing procurement requests to external suppliers.
*   Maintaining a centralized catalog of supply items (products and services).
*   Managing master data for customer and supplier entities.
*   Providing role-based interfaces for Coordinators, Customers, and Suppliers.

**Out of Scope:**
*   Financial accounting, invoicing, or payment processing.
*   Advanced logistics, warehousing, or inventory management.
*   Manufacturing or production planning modules.
*   Integration with external, non-Ejada SCM or ERP platforms.

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **SCM** | Supply Chain Management |
| **Coordinator** | An authorized Ejada employee who manages requests and entity data within the system. |
| **Request** | A formal demand for products or services, either from a Customer (Customer Request) or to a Supplier (Supplier/Procurement Request). |
| **Item** | A product or service available for supply within Ejada's catalog. |
| **Entity** | A business partner, either a Customer (receives goods/services) or a Supplier (provides goods/services). |
| **ASP.NET** | A web application framework developed by Microsoft. |
| **MS SQL Server** | Microsoft SQL Server, a relational database management system. |

### 1.4 References
*   Ejada Corporate IT Standards and Framework Documentation
*   Microsoft .NET Development Guidelines
*   Project Charter: Ejada SCM System

### 1.5 Overview
The remainder of this document is structured as follows:
*   **Section 2:** Provides a high-level description of the overall system and its operating environment.
*   **Section 3:** Details specific functional requirements organized by features and user roles.
*   **Section 4:** Specifies external interface requirements (UI, hardware, software, communications).
*   **Section 5:** Lists non-functional requirements (performance, security, quality attributes).
*   **Section 6:** Outlines other requirements such as compliance, documentation, and licensing.

## 2. Overall Description

### 2.1 Product Perspective
The Ejada SCM System is a new, self-contained web application. It must integrate with Ejada's existing corporate framework (e.g., authentication services, design system, logging libraries). It is not a module of a larger ERP system but will serve as the primary system for managing supply chain requests and partner data for its defined scope.

### 2.2 Product Functions
The core high-level functions of the system are:
1.  **Request Management:** Create, view, track, update, and close requests from customers and to suppliers.
2.  **Item Catalog Management:** Maintain a centralized list of all products and services offered, including descriptions, codes, and statuses.
3.  **Entity Management:** Maintain master records for all Customers and Suppliers, including contact and contractual information.
4.  **User & Role Management:** Provide distinct interfaces and permissions for Coordinators, Customers, and Suppliers.

### 2.3 User Characteristics
| User Class | Description | Technical Proficiency | Key Goals |
| :--- | :--- | :--- | :--- |
| **Coordinator (Ejada Employee)** | Primary system operator. Manages the flow of requests and data. | High. Comfortable with business web applications. | Efficiently process requests, maintain accurate item and entity data, generate reports. |
| **Customer** | External client who submits requests for products/services. | Medium. Can use standard web forms and portals. | Easily submit and track the status of their requests. |
| **Supplier** | External vendor who receives procurement requests from Ejada. | Medium. Can use standard web forms and portals. | View and respond to requests sent by Ejada coordinators. |

### 2.4 Constraints
1.  **Technical:** The system must be developed as a web application using the Microsoft .NET technology stack, specifically ASP.NET (Core or MVC) with C# and MS SQL Server as the backend database.
2.  **Integration:** The application must comply with and integrate into Ejada's existing corporate IT framework (e.g., single sign-on, UI component library, network security policies).
3.  **Operational:** The system is for Ejada's internal and direct partner use only. It shall not be marketed as a commercial, off-the-shelf product.

### 2.5 Assumptions and Dependencies
*   It is assumed that users will have access to a modern web browser (Chrome, Edge, Firefox, Safari).
*   The project depends on the availability of Ejada's existing framework APIs and documentation for successful integration.
*   It is assumed that clear business processes for request approval and supplier communication are defined outside the system.

## 3. Specific Requirements

### 3.1 Functional Requirements

#### 3.1.1 User Authentication & Authorization (UAA)
*   **UAA-1:** The system shall integrate with Ejada's corporate authentication system (e.g., Active Directory) for Coordinator login.
*   **UAA-2:** The system shall provide a separate, secure login mechanism for external Customers and Suppliers using username/password.
*   **UAA-3:** The system shall implement role-based access control (RBAC) with at least the following roles: `Coordinator`, `Customer`, `Supplier`.
*   **UAA-4:** A user with the `Coordinator` role shall have access to all system functions.

#### 3.1.2 Customer & Supplier Entity Management
*   **ENT-1:** The system shall allow a `Coordinator` to create, read, update, and deactivate Customer and Supplier records.
*   **ENT-2:** Each Entity record shall store: Unique ID, Name, Type (Customer/Supplier), Primary Contact Info, Address, Status (Active/Inactive), and Date Created.
*   **ENT-3:** The system shall prevent the deletion of an Entity that has associated historical Requests.
*   **ENT-4:** `Customers` and `Suppliers` shall only be able to view their own entity profile.

#### 3.1.3 Item Catalog Management
*   **ITEM-1:** The system shall allow a `Coordinator` to manage a catalog of supply Items.
*   **ITEM-2:** Each Item record shall store: Item Code (unique), Description, Category, Unit of Measure, Status (Available/Discontinued), and Cost Price (optional).
*   **ITEM-3:** The system shall prevent the assignment of a discontinued Item to a new Request.
*   **ITEM-4:** `Customers` shall be able to browse the catalog of available Items when creating a request.

#### 3.1.4 Request Management
*   **REQ-1:** The system shall allow a `Customer` user to create a new Customer Request.
*   **REQ-2:** A Customer Request shall include: Request ID (auto-generated), Customer, Request Date, Required Items (with quantities), Status (e.g., Submitted, Under Review, Approved, Fulfilled, Cancelled), and Comments.
*   **REQ-3:** The system shall allow a `Coordinator` to create a Supplier (Procurement) Request.
*   **REQ-4:** A Supplier Request shall include: Request ID, Supplier, Request Date, Requested Items, Status (e.g., Draft, Sent to Supplier, Quote Received, Ordered, Received), Coordinator Comments, and Supplier Response field.
*   **REQ-5:** The system shall allow a `Coordinator` to view, search, filter, and update the status of all Requests (Customer and Supplier).
*   **REQ-6:** The system shall allow a `Supplier` user to view Supplier Requests sent to them and update the status and provide a response (e.g., quote).
*   **REQ-7:** The system shall log all status changes for a Request with a timestamp and the user who made the change.
*   **REQ-8:** The system shall send email notifications to relevant users upon key status changes (e.g., Customer notified when request is fulfilled, Supplier notified when a new request is sent).

### 3.2 External Interface Requirements

#### 3.2.1 User Interfaces
*   The UI shall be a responsive web application compatible with major browsers.
*   The visual design shall adhere to Ejada's corporate UI/UX standards and component library.
*   Key pages shall include: Dashboard, Entity List/Detail, Item Catalog, Request List/Detail, and User Profile.

#### 3.2.2 Hardware Interfaces
*   None specified. The application is hosted server-side.

#### 3.2.3 Software Interfaces
*   **SI-1:** The system shall interface with Ejada's corporate **Active Directory** or **Identity Provider** for Coordinator authentication.
*   **SI-2:** The system shall interface with Ejada's corporate **SMTP server** for sending email notifications.
*   **SI-3:** The system shall be hosted on Ejada-approved **IIS web servers**.

#### 3.2.4 Communications Interfaces
*   The system shall use **HTTPS (TLS 1.2+)** for all client-server communications.
*   Communication with the database shall use secure, encrypted connections.

### 3.3 Non-Functional Requirements

#### 3.3.1 Performance Requirements
*   **PER-1:** The system shall support up to 100 concurrent users.
*   **PER-2:** 95% of all web page loads shall complete in less than 3 seconds under normal load.
*   **PER-3:** Search operations on primary lists (Entities, Items, Requests) shall return results in less than 2 seconds.

#### 3.3.2 Safety Requirements
*   Not applicable. This is a business management system with no physical safety implications.

#### 3.3.3 Security Requirements
*   **SEC-1:** All passwords shall be stored using strong, salted hashing algorithms.
*   **SEC-2:** The system shall be protected against common OWASP Top 10 vulnerabilities (e.g., SQL Injection, XSS, CSRF).
*   **SEC-3:** User sessions shall timeout after 30 minutes of inactivity.
*   **SEC-4:** All actions shall be logged for audit purposes (user, action, timestamp, entity ID).

#### 3.3.4 Software Quality Attributes
*   **AVAILABILITY:** The system shall have an operational uptime of 99.5% during core business hours (8:00 AM - 6:00 PM, Sunday-Thursday).
*   **MAINTAINABILITY:** The code shall be written following .NET best practices and include XML documentation for all public APIs and complex methods.
*   **USABILITY:** The system shall be intuitive for `Coordinators` to learn core functions within 2 hours of training. The external user (`Customer`/`Supplier`) interface shall require no formal training.
*   **RELIABILITY:** The system shall have a mean time between failures (MTBF) of no less than 720 hours in production.

## 4. Other Requirements

### 4.1 Documentation Requirements
*   **User Manual:** Online help system and PDF guide for Coordinators.
*   **External User Guide:** Brief guide for Customers and Suppliers on how to submit and track requests.
*   **Technical Documentation:** Solution architecture, database schema, and API documentation.
*   **Deployment & Operations Guide:** Instructions for IT staff to install, configure, and backup the system.

### 4.2 Licensing and Legal Requirements
*   The system shall be developed using properly licensed versions of all software (Visual Studio, .NET, SQL Server).
*   The application must comply with Ejada's internal data governance and privacy policies.

### 4.3 Standards Compliance
*   The application code shall comply with Ejada's internal .NET coding standards.
*   Database design shall follow Ejada's SQL Server naming conventions and design patterns.

---
**APPROVALS**

| Name | Role | Signature | Date |
| :--- | :--- | :--- | :--- |
| | Project Sponsor | | |
| | Lead Business Analyst | | |
| | Lead Software Architect | | |