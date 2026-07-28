# Detailed Summary: Supply Chain Management (SCM) System

## Background and Scope
This document specifies the requirements for a web-based Supply Chain Management (SCM) system for Ejada company. The system aims to manage the flow of products and services, including IT products, business consultation, and other IT services, by coordinating between customers, suppliers, and an internal coordinator role. It focuses on core SCM functions like customer service management, procurement, product development, manufacturing flow, and performance measurement. The system is constrained to use .NET technologies (ASP.NET, C#) and MS SQL Server, and must integrate with Ejada's existing framework. Non-goals include integration with external systems like CRM or HR in the initial release, and the system is not intended for use outside of Ejada.

## Stakeholders Matrix and Use Cases
*   **Coordinator (Ejada Employee):** Manages customers, suppliers, items, resource locations, and requests; acts as the central orchestrator between customers and suppliers.
*   **Customer:** Submits and manages product/service requests, and views request status.
*   **Supplier:** Views supply requests from the coordinator, submits feedback on feasibility and delivery timelines, and manages their profile.

**Main Scenarios:**
1.  Coordinator logs in and manages (adds, views, edits, deletes) customer, supplier, item, or location records.
2.  Customer logs in, creates a new request, and submits it to the coordinator.
3.  Supplier logs in, views pending supply requests, and submits feedback on a specific request.
4.  Coordinator creates a new supply request and sends it to a supplier.
5.  Coordinator views details of a customer request or a supplier's feedback.
6.  Customer or Supplier edits their own profile information.

**Exception Scenarios:**
1.  User provides incorrect login credentials and is shown an error page.
2.  Coordinator attempts to send a request but no suppliers are available in the system.
3.  Supplier submits invalid data in a feedback form, triggering an error.

## Business Process
**Main Process: Fulfill Customer Request**
1.  **Trigger:** Customer submits a new product/service request.
2.  Coordinator reviews the incoming customer request.
3.  Coordinator identifies required items and checks internal inventory.
4.  If items are unavailable, coordinator creates and sends a supply request to a supplier.
5.  Supplier reviews the request and submits feedback (ability to supply, timeline).
6.  Coordinator reviews supplier feedback and updates the customer request status.
7.  Coordinator manages the procurement and fulfillment process.
8.  **Output:** Customer request is fulfilled (or status is communicated).

**Key Branch A: Supplier Feedback Loop (Steps 5-6)**
1.  Supplier indicates they cannot fully supply the request.
2.  Coordinator may edit the original request based on partial availability.
3.  Coordinator may send the revised request to another supplier.
4.  Process iterates until supply is secured or request is cancelled.

**Key Branch B: Direct Item Fulfillment (Step 3)**
1.  Required items are available in internal inventory.
2.  Coordinator allocates items from stock to the customer request.
3.  Process skips to fulfillment (Step 7).
4.  Inventory levels are updated.

## Domain Model
Core entities and their key fields:
*   **User** (Parent class): UserID (required, unique), Password (required), Domain (required: Coordinator/Customer/Supplier).
*   **Customer** (extends User): Name (required), Address, ContactPerson, Email.
*   **Supplier** (extends User): Name (required), Address, ContactPerson, Email.
*   **Coordinator** (extends User): (Inherits fields; may have role-specific attributes).
*   **Request:** RequestID (required, unique), Description, Status, CustomerID (reference), CoordinatorID (reference).
*   **Item:** ItemID (required, unique), Name, Description, Quantity.
*   **ResourceLocation:** LocationID (required, unique), Name, Address.
*   **Feedback:** FeedbackID (required, unique), Content, RequestID (reference), SupplierID (reference).

## Interfaces and Integrations
*   **User Interface (Web Browser):** Direction: Bidirectional. Theme: Role-based web portal with login and navigation menus. Input: User credentials, form data. Output: HTML pages, success/error messages. SLA: Page load < 3 seconds.
*   **Database (MS SQL Server):** Direction: System to DB. Interaction: All data persistence. Input: CRUD operations. Output: Query results, transaction confirmation. SLA: 90% of transactions < 1 second.
*   **Ejada .NET Framework:** Direction: System integrated with. Theme: Shared libraries and integration points for future modules. Input/Output: Defined by framework APIs. SLA: Must comply with framework's runtime constraints.
*   **Web Server (Microsoft IIS):** Direction: System hosted on. Theme: Application deployment and HTTP request handling. Input: HTTP requests. Output: HTTP responses. SLA: Supports 100 concurrent users.

## Acceptance Criteria
**Capability: Customer Request Submission**
*   Given a customer is logged in, when they fill and submit a new request form, then the request is saved with a "Pending" status and the coordinator is notified.
*   Given a customer submits a request with invalid data, when they click submit, then an error message is shown and the request is not saved.

**Capability: Supplier Feedback**
*   Given a supplier is viewing a supply request's details, when they enter and submit feedback, then the feedback is saved and associated with the request, and the coordinator is notified.
*   Given a supplier submits empty feedback, when they click submit, then an error message is shown.

**Capability: Coordinator Management**
*   Given a coordinator is authenticated, when they delete a customer record, then the system prompts for confirmation before removal and logs the action.

## Non-functional Metrics
*   **Performance:** Support at least 100 concurrent users; 90% of transactions complete in under 1 second.
*   **Reliability:** Implement daily automated database backups; system must rollback transactions on failure.
*   **Security:** Enforce role-based access control (Coordinator, Customer, Supplier) via login authentication.
*   **Compliance:** Adhere to Ejada's internal programming standards and .NET framework constraints.
*   **Observability:** System must detect and provide understandable error messages to users for operational failures.

## Milestones and Release Strategy
1.  Finalize SRS (v2.0) and obtain stakeholder sign-off.
2.  Complete core database schema and authentication module.
3.  Implement Coordinator management functions (CRUD for Customers, Suppliers, Items).
4.  Implement Customer request lifecycle (Create, View, Edit, Delete).
5.  Implement Supplier feedback module.
6.  Release 1.0 with all core functional requirements integrated and tested within the Ejada framework.

## Risk List and Mitigation Strategies
1.  **Risk:** Scope creep from future integration with CRM/HR modules. **Mitigation:** Clearly define and freeze scope for Release 1.0; document interfaces for future expansion.
2.  **Risk:** Performance degradation with 100+ concurrent users. **Mitigation:** Implement query optimization, caching strategies, and load testing early.
3.  **Risk:** Dependency on specific versions of .NET Framework/IIS. **Mitigation:** Document exact version requirements and conduct compatibility testing in the staging environment.
4.  **Risk:** Data loss or corruption. **Mitigation:** Implement robust, automated backup procedures and transaction rollback mechanisms.
5.  **Risk:** Security breach via weak authentication. **Mitigation:** Enforce strong password policies and secure session management.
6.  **Risk:** Failure to meet Ejada's programming standards. **Mitigation:** Conduct regular code reviews against the provided standards.
7.  **Risk:** Supplier or customer inability to use the web interface effectively. **Mitigation:** Design a simple, intuitive UI and provide basic guidance/help.
8.  **Risk:** Project delays due to waterfall model rigidity. **Mitigation:** Maintain detailed documentation and strict phase gate reviews.

## Undecided Issues and Responsible Parties
1.  **Issue:** Specific format and channel for notifications (email, in-system alert) to users. **Responsible:** Product Owner / Business Analyst.
2.  **Issue:** Detailed validation rules for all data input fields (e.g., email format, phone number). **Responsible:** Development Team Lead.
3.  **Issue:** Criteria for archiving or purging old requests and data. **Responsible:** System Architect & Ejada IT.
4.  **Issue:** Final decision on whether customers/suppliers should be notified on every edit/deletion by the coordinator. **Responsible:** Product Owner.
5.  **Issue:** Recovery procedure and SLA for restoring from backups. **Responsible:** DevOps / System Administrator.
6.  **Issue:** Browser compatibility testing matrix beyond IE and Firefox. **Responsible:** QA Team Lead.
7.  **Issue:** Definition of "concurrent user" for performance testing (active session vs. simultaneous transaction). **Responsible:** Performance Test Engineer.
8.  **Issue:** Process for handling a request when all contacted suppliers decline. **Responsible:** Business Process Owner (Coordinator role).