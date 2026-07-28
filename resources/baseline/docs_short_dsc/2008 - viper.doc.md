# Software Requirements Specification (SRS)
## Supply Chain Management (SCM) System
**For Ejada Company**
**Document Version:** 1.0
**Date:** [Current Date]

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Ejada Supply Chain Management (SCM) System. It serves as a formal agreement between the project stakeholders and the development team, providing a comprehensive description of the system's intended capabilities, constraints, and external interfaces. The primary audience includes project managers, developers, testers, and end-users.

#### 1.2 Document Conventions
This SRS follows the IEEE 830-1998 standard for Software Requirements Specifications. Requirements are uniquely identified with tags (e.g., `FR-001`, `NFR-001`). Markdown formatting is used for structure, with code blocks for technical specifications.

#### 1.3 Project Scope
The SCM system is a web-based application designed to streamline the management of customer requests, supplier interactions, and internal resource coordination within Ejada. It centralizes the request lifecycle, from submission by a customer to fulfillment by a supplier, managed by an internal coordinator.

**In-Scope Features:**
*   User role management for Coordinators, Customers, and Suppliers.
*   Full CRUD (Create, Read, Update, Delete) operations for managing Customers, Suppliers, Items, and Resource Locations.
*   End-to-end Request Lifecycle Management (creation, assignment, tracking, feedback, closure).
*   Role-based access control (RBAC) via a web interface.
*   Development on the Microsoft technology stack (ASP.NET, C#, MS SQL Server).
*   Integration with two specified existing .NET modules within Ejada's framework.

**Out-of-Scope Features:**
*   Hardware interfaces or device drivers.
*   Direct, real-time integration with external enterprise systems (e.g., CRM, ERP, HR).
*   Non-web client interfaces (e.g., desktop applications, mobile apps, offline functionality).
*   Advanced business intelligence, predictive analytics, or complex reporting.
*   Automated procurement, payment processing, or inventory control systems.

#### 1.4 References
*   Ejada Corporate .NET Framework Standards Document
*   Project Charter: SCM System for Ejada
*   IEEE Std 830-1998, IEEE Recommended Practice for Software Requirements Specifications

### 2. Overall Description

#### 2.1 Product Perspective
The SCM System is a new, self-contained web application that will reside within Ejada's existing IT ecosystem. It will be hosted on internal servers and must integrate with two pre-existing .NET modules (to be specified during design). The system does not replace but complements existing operational workflows.

**System Interfaces:**
*   **Software Interfaces:** Must integrate with two designated legacy .NET modules via defined APIs or service layers.
*   **User Interfaces:** Web-based GUI accessible via specified browsers.
*   **Communication Interfaces:** Internal network communication via HTTP/HTTPS. Notification channels (email/SMS) are TBD.
*   **Database:** Microsoft SQL Server.

#### 2.2 Product Functions (High-Level Feature List)
1.  **User Management:** Secure authentication and authorization for three distinct roles.
2.  **Customer Management:** Coordinators can register, view, edit, and deactivate customer accounts.
3.  **Supplier Management:** Coordinators can register, view, edit, and deactivate supplier accounts.
4.  **Catalog Management:** Coordinators can manage a list of Items and Resource Locations.
5.  **Request Lifecycle Management:**
    *   Customers can create, view, and track their requests.
    *   Coordinators can view, assign, monitor, and close all requests.
    *   Suppliers can view requests assigned to them and submit feedback.
6.  **Reporting & Views:** Filtered views and basic performance dashboards per user role.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Responsibilities |
| :--- | :--- | :--- |
| **Coordinator** | Internal Ejada employee. Technically proficient. Primary system administrator. | Manage all master data (customers, suppliers, items, locations). Assign customer requests to suppliers. Monitor request status and supplier feedback. Resolve issues. |
| **Customer** | External client. Varying technical skill. Accesses system to request services/products. | Submit new requests. View and track the status of their own requests. Update their own profile information. |
| **Supplier** | External vendor. Varying technical skill. Accesses system to receive work orders. | View requests assigned to them by the coordinator. Submit feedback (e.g., accept, decline, propose changes) on requests. Update their own profile information. |

#### 2.4 Operating Environment
*   **Server:** Microsoft Windows Server OS, Internet Information Services (IIS) 6.0+, .NET Framework 3.5.
*   **Database:** Microsoft SQL Server 2005+.
*   **Client Browsers:** Internet Explorer (v6, v7), Mozilla Firefox (v2, v3).
*   **Network:** Corporate LAN/Intranet; external users access via secure VPN or designated access point.

#### 2.5 Design and Implementation Constraints
1.  **Architectural:** Must be developed as a web application using ASP.NET WebForms or MVC (as per framework) with C#.
2.  **Database:** Must use MS SQL Server for all persistent data storage.
3.  **Process:** Development must follow the Waterfall methodology.
4.  **Design:** System must be designed using object-oriented principles and patterns.
5.  **Integration:** Must comply with Ejada's internal .NET framework and integrate seamlessly with two existing modules.
6.  **Browser Compatibility:** Must fully support the listed browser versions.

#### 2.6 Assumptions and Dependencies
*   Assumes stable network connectivity for all users.
*   Depends on the existing Ejada user directory or authentication service for initial coordinator login (or will implement its own).
*   Success metrics are dependent on adequate server hardware provisioning, which is the responsibility of the Ejada IT department.

### 3. System Features and Requirements

#### 3.1 Feature 1: User Authentication and Role-Based Access
**Description:** The system shall provide secure login and enforce access controls based on user roles (Coordinator, Customer, Supplier).

**Functional Requirements:**
*   `FR-001`: The system shall present a login page requiring a username and password.
*   `FR-002`: The system shall authenticate credentials against the system database.
*   `FR-003`: Upon successful login, the system shall redirect the user to a dashboard specific to their role.
*   `FR-004`: The system shall enforce authorization rules, displaying only menu options and data permissible for the user's role.
*   `FR-005`: The system shall provide a secure logout mechanism that terminates the user session.

#### 3.2 Feature 2: Coordinator Management Console
**Description:** Provides the coordinator with tools to manage all core entities within the system.

**Sub-feature 2.1: Manage Customers**
*   `FR-010`: The coordinator shall be able to add a new customer, capturing at least: Company Name, Contact Person, Email, Phone, Address.
*   `FR-011`: The coordinator shall be able to view a list of all customers.
*   `FR-012`: The coordinator shall be able to edit the details of any existing customer.
*   `FR-013`: The coordinator shall be able to deactivate (soft delete) a customer account, preventing new requests but preserving history.

**Sub-feature 2.2: Manage Suppliers**
*   `FR-020`: The coordinator shall be able to add a new supplier, capturing at least: Company Name, Contact Person, Email, Phone, Address, and Supplied Items/Categories.
*   `FR-021`: The coordinator shall be able to view a list of all suppliers.
*   `FR-022`: The coordinator shall be able to edit the details of any existing supplier.
*   `FR-023`: The coordinator shall be able to deactivate a supplier account.

**Sub-feature 2.3: Manage Catalog (Items & Locations)**
*   `FR-030`: The coordinator shall be able to create, view, edit, and deactivate Items in the system catalog (e.g., Product ID, Name, Description).
*   `FR-031`: The coordinator shall be able to create, view, edit, and deactivate Resource Locations (e.g., Warehouse ID, Name, Address).

**Sub-feature 2.4: Manage Requests**
*   `FR-040`: The coordinator shall be able to view all requests in the system with filter options (e.g., by status, customer, date).
*   `FR-041`: The coordinator shall be able to assign a pending customer request to one or more suppliers.
*   `FR-042`: The coordinator shall be able to view feedback submitted by suppliers on assigned requests.
*   `FR-043`: The coordinator shall be able to update the status of a request (e.g., "In Progress", "Completed", "Cancelled") based on supplier feedback and customer communication.

#### 3.3 Feature 3: Customer Portal
**Description:** Allows customers to submit and monitor their service/product requests.

*   `FR-050`: The customer shall be able to submit a new request, specifying at least: Required Item(s), Quantity, Required Date, Preferred Location, and Special Instructions.
*   `FR-051`: The customer shall be able to view a list of all their submitted requests.
*   `FR-052`: The customer shall be able to view the detailed status of any of their requests (e.g., "Submitted", "Assigned to Supplier", "Supplier Feedback Received", "Completed").
*   `FR-053`: The customer shall be able to edit their own profile information (Contact, Phone, etc.).
*   `FR-054`: A customer shall only see and interact with requests they own.

#### 3.4 Feature 4: Supplier Portal
**Description:** Allows suppliers to view assigned requests and communicate feedback.

*   `FR-060`: The supplier shall be able to view a list of requests assigned to them, filtered by status (e.g., "New", "Pending Feedback").
*   `FR-061`: The supplier shall be able to view the full details of an assigned request.
*   `FR-062`: The supplier shall be able to submit feedback on an assigned request. Feedback shall include a status (e.g., "Accepted", "Declined", "Need More Info") and a comment field.
*   `FR-063`: The supplier shall be able to edit their own profile information.
*   `FR-064`: A supplier shall only see requests explicitly assigned to them by a coordinator.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   The UI shall be clean, professional, and consistent with Ejada's web standards.
*   All data entry forms shall include clear validation and user-friendly error messages.
*   The main navigation shall be role-specific, displayed as a menu or dashboard upon login.
*   List views shall support basic sorting and filtering.

#### 4.2 Software Interfaces (Integration)
*   `SI-001`: The system shall interface with **Module A** (TBD) for [Purpose TBD, e.g., fetching employee data].
*   `SI-002`: The system shall interface with **Module B** (TBD) for [Purpose TBD, e.g., logging financial events].
*   Integration shall be achieved via .NET assemblies, web services (ASMX), or direct database calls as dictated by the existing modules' APIs.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-001`: The system shall support a minimum of **100 concurrent users** without significant degradation in performance.
*   `NFR-002`: **90% of all standard transactions** (page loads, form submissions, list views) shall complete in **under 1 second** under normal load conditions.
*   `NFR-003`: Database queries for primary list views shall return results in under 3 seconds.

#### 5.2 Safety & Security Requirements
*   `NFR-010`: All passwords shall be stored using strong, irreversible hashing algorithms (e.g., SHA-256 with salt).
*   `NFR-011`: All user sessions shall timeout after a period of inactivity (15 minutes recommended).
*   `NFR-012`: The system shall be protected against common web vulnerabilities (SQL Injection, Cross-Site Scripting).
*   `NFR-013`: Direct database access shall be restricted to the application service account.

#### 5.3 Software Quality Attributes
*   **Availability:** `NFR-020`: The system shall target **100% availability** during core business hours (e.g., 8:00 AM - 6:00 PM). Scheduled maintenance must be communicated in advance.
*   **Reliability:** `NFR-021`: The system shall provide clear, understandable, and actionable error messages to the user, avoiding technical codes.
*   **Maintainability:** `NFR-022`: The code shall be developed with object-oriented design, follow .NET best practices, and include inline comments to facilitate future maintenance.
*   **Usability:** `NFR-023`: The system shall be intuitive enough for a novice user to perform core tasks (submit a request, view status) with minimal training.

### 6. Other Requirements

#### 6.1 Success Metrics
The project will be deemed successful if the following metrics are validated during User Acceptance Testing (UAT):
1.  The system meets all Functional Requirements (`FR-001` through `FR-064`).
2.  Performance tests confirm support for 100+ concurrent users (`NFR-001`).
3.  Performance tests show 90% of transactions under 1-second response time (`NFR-002`).
4.  End-users (Coordinators, Customers, Suppliers) confirm the workflow is logical and efficient.

#### 6.2 Undecided (TBD) Issues
The following items require stakeholder resolution prior to or during the design phase:
1.  The specific communication channels for system notifications (e.g., in-app only, email, SMS).
2.  Whether a customer can edit a request after it has been acknowledged or assigned by a coordinator.
3.  The exact filter and search criteria for customer and supplier list views.
4.  The business rule for handling request deletions or cancellations when a supplier is unavailable.
5.  The detailed backup schedule, recovery time objective (RTO), and recovery point objective (RPO) for disaster recovery.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| Quality Assurance Lead | | | |