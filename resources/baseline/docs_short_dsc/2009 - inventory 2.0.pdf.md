# Software Requirements Specification (SRS)
## Inventory Management System (IMS)
### For Construction Junction

**Document Version:** 1.0  
**Date:** [Current Date]  
**Author:** [Author/Team Name]  
**Status:** Draft for Review

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Inventory Management System (IMS) to be developed for Construction Junction. The intended audience includes stakeholders, project managers, software developers, testers, and system integrators.

### 1.2 Project Scope
The IMS is a web-based application designed to manage the complete lifecycle of donated construction and building materials, from acquisition through to point-of-sale. Its primary objectives are to streamline inventory tracking, accelerate donation processing, ensure inventory accuracy, and integrate seamlessly with the existing QuickBooks Point-of-Sale (POS) and Salesforce Customer Relationship Management (CRM) systems.

### 1.3 Definitions, Acronyms, and Abbreviations
*   **IMS:** Inventory Management System
*   **POS:** Point of Sale
*   **CRM:** Customer Relationship Management
*   **QB POS:** QuickBooks Point of Sale
*   **Decon:** Deconstruction (the process of carefully dismantling structures to salvage materials)
*   **SKU:** Stock Keeping Unit
*   **UI:** User Interface
*   **UX:** User Experience
*   **API:** Application Programming Interface

### 1.4 References
*   QuickBooks POS API Documentation
*   Salesforce CRM API Documentation
*   Construction Junction Operational Procedures

### 1.5 Document Overview
This document is structured to present an overall description of the product, followed by specific functional and non-functional requirements, external interface requirements, and other supporting information.

## 2. Overall Description

### 2.1 Product Perspective
The IMS is a new, self-contained web application that will interface with two critical existing systems:
1.  **QuickBooks POS:** For finalizing sales transactions and synchronizing inventory deductions.
2.  **Salesforce CRM:** For managing donor/buyer constituent data and history.

The system will replace or augment manual and disparate inventory tracking processes.

### 2.2 Product Functions (High-Level)
*   Manage a hierarchical inventory categorization system (Department > Category > Subcategory).
*   Process donations via three intake channels: Drop-off, Scheduled Pickup, and Deconstruction.
*   Manage the full item lifecycle (Add, Tag, Price, Modify, Split, Transfer, Mark as Sold/Donated).
*   Generate barcode labels for inventory items.
*   Provide role-based dashboards and workflows for different staff members.
*   Synchronize item and customer data bi-directionally with QB POS and Salesforce.
*   Generate basic operational reports.

### 2.3 User Characteristics

| Role | Primary Responsibilities | Technical Proficiency |
| :--- | :--- | :--- |
| **Administrator** | System configuration, category management, user role assignment. | High. Comfortable with system settings. |
| **Director** | User management, oversight reports, managerial overrides. | Medium-High. |
| **Manager** | Adjusting item pricing, properties, and inventory levels; approving exceptions. | Medium. |
| **Receiving Associate** | Initial data entry and tagging of donations at the receiving dock. | Medium-Low. Requires touch-screen, scan-centric UI. |
| **Customer Service Rep** | Looking up donor history, processing returns/credits. | Medium. |
| **Pickup/Decon Associate** | Entering preliminary donation details on a mobile device in the field. | Low-Medium. Requires simple, robust mobile web UI. |
| **Sales Associate** | Processing sales at POS (primarily in QB POS, impacted by IMS data). | Low. Uses QB POS interface directly. |
| **Donor/Buyer** | External entity providing or purchasing goods. No direct system access. | N/A |

### 2.4 Constraints
1.  **Integration Constraint:** Must use existing APIs for QuickBooks POS and Salesforce CRM.
2.  **Interface Constraint:** Must provide a touch-screen optimized interface for dock workstations.
3.  **Hardware Constraint:** Must support standard USB barcode scanners and label printers.
4.  **Architectural Constraint:** Must be a web-based application for cross-platform (Windows, iOS) compatibility.
5.  **Performance Constraint:** Data synchronization between IMS, QB POS, and Salesforce must occur in near real-time (latency < 5 minutes for critical updates).

### 2.5 Assumptions and Dependencies
*   Assumes stable network connectivity at the warehouse, store, and for mobile units.
*   Depends on the continued availability and support of the QB POS and Salesforce APIs.
*   Assumes hardware (scanners, printers, tablets) will be procured separately and are compatible with web technologies.

## 3. System Features and Requirements

### 3.1 Functional Requirements

#### 3.1.1 Inventory Categorization Management (FR-1)
*   **FR-1.1:** The system shall allow Administrators to create, read, update, and deactivate a hierarchical structure of **Departments**, **Categories**, and **Subcategories**.
*   **FR-1.2:** The system shall enforce that all inventory items are assigned to a terminal node (Subcategory or Category) in the hierarchy.
*   **FR-1.3:** The category hierarchy shall be displayable in a matrix or tree view for management purposes.

#### 3.1.2 Donation Acquisition Processing (FR-2)
*   **FR-2.1:** The system shall support creating a **Donation Record** linked to a Constituent (donor) in Salesforce.
*   **FR-2.2:** The system shall support three intake types:
    *   **FR-2.2.1:** **Drop-off:** Immediate processing at the dock.
    *   **FR-2.2.2:** **Pickup:** Scheduled pickup with preliminary data entry on a mobile device.
    *   **FR-2.2.3:** **Deconstruction:** Project-based intake with multiple items.
*   **FR-2.3:** For each donation, the system shall generate a printable or emailable receipt for the donor.
*   **FR-2.4:** Pickup/Decon Associates shall be able to enter item descriptions, quantities, and preliminary categories using a mobile-optimized web interface.

#### 3.1.3 Inventory Item Lifecycle Management (FR-3)
*   **FR-3.1:** Upon receiving an item, a Receiving Associate shall be able to create an **Inventory Item Record** with: SKU (auto-generated), description, category, condition, location, estimated value/price, donor info, and notes.
*   **FR-3.2:** The system shall generate and print a unique barcode label for each inventoried item or lot.
*   **FR-3.3:** Managers shall be able to **modify** item properties (price, description, condition, location).
*   **FR-3.4:** The system shall allow authorized users to **split** a multi-quantity lot into individual item records.
*   **FR-3.5:** The system shall maintain a complete audit **history** (who, what, when) for all changes to an item record.
*   **FR-3.6:** When an item is sold in QB POS, the IMS shall be notified via integration and automatically update the item's status to **Sold**, adjusting available inventory.

#### 3.1.4 Integration Requirements (FR-4)
*   **FR-4.1:** The system shall synchronize new and updated **Constituent** (donor/buyer) information bi-directionally with Salesforce CRM.
*   **FR-4.2:** The system shall push new **Inventory Item** data (SKU, Description, Price, Category) to QuickBooks POS.
*   **FR-4.3:** The system shall receive **Sale Transaction** notifications from QuickBooks POS to update item status and inventory levels.
*   **FR-4.4:** All integrations shall operate in near real-time.

#### 3.1.5 Reporting (FR-5)
*   **FR-5.1:** The system shall provide a basic dashboard showing: total active inventory, recent donations, recently sold items.
*   **FR-5.2:** The system shall generate standard reports including:
    *   Donation Summary Report (by date, donor, type)
    *   Inventory Valuation Report (by category, location)
    *   Price Change History Report
    *   Items Sold Report (linked to POS data)

#### 3.1.6 User Management & Security (FR-6)
*   **FR-6.1:** The system shall implement role-based access control (RBAC) aligned with the user characteristics in section 2.3.
*   **FR-6.2:** All user actions shall be authenticated via a secure login mechanism.
*   **FR-6.3:** Directors and Administrators shall be able to create and manage system user accounts and assign roles.

### 3.2 Non-Functional Requirements

#### 3.2.1 Usability
*   **NF-UR-1:** The interface for Receiving Dock workstations shall be optimized for touch interaction (buttons/targets >= 48x48 pixels).
*   **NF-UR-2:** Common tasks (e.g., entering a drop-off donation) shall be achievable in 3 clicks/touches or less from the role-specific home screen.
*   **NF-UR-3:** The mobile web interface for pickup associates shall be fully functional on screens as small as 5 inches.

#### 3.2.2 Performance
*   **NF-PR-1:** Page load times for core workflows shall be under 2 seconds on the local network.
*   **NF-PR-2:** Barcode scan-to-item lookup shall return results in less than 1 second.
*   **NF-PR-3:** The system shall support at least 20 concurrent users without significant degradation.

#### 3.2.3 Reliability & Availability
*   **NF-RA-1:** The system shall have an uptime availability of 99.5% during core business hours (8 AM - 6 PM).
*   **NF-RA-2:** Critical data entry shall be preserved in the browser in case of a network interruption and submitted upon reconnection.

#### 3.2.4 Supportability
*   **NF-SR-1:** The system shall log all errors and significant user actions for troubleshooting and audit purposes.
*   **NF-SR-2:** Configuration settings (e.g., default printer, category matrix view) shall be manageable through the admin UI.

## 4. External Interface Requirements

### 4.1 User Interfaces
*   The primary UI will be a responsive web application.
*   **Touch Interface:** A distinct, simplified UI profile will be served to devices identified as dock workstations.
*   **Mobile Interface:** A responsive layout for use on tablets and smartphones in the field.
*   **Desktop Interface:** A full-featured interface for managerial and administrative tasks.

### 4.2 Hardware Interfaces
*   The system shall interface with standard USB HID barcode scanners (input).
*   The system shall support printing to standard label printers (e.g., Zebra, DYMO) via browser print APIs or dedicated driver integration.

### 4.3 Software Interfaces
*   **Salesforce CRM:** Bi-directional REST API integration for Constituent data.
    *   `POST /services/data/vXX.0/sobjects/Contact` - Create/Update Donor
    *   `GET /services/data/vXX.0/sobjects/Contact/{Id}` - Retrieve Donor
*   **QuickBooks POS:** Integration via QB POS API or intermediary database.
    *   Push: `Add/Update Item` function.
    *   Pull/Listen: `Sale Event` notification to update IMS inventory.

### 4.4 Communication Interfaces
*   The application will use HTTPS (TLS 1.2+) for all client-server communication.
*   API calls to external systems (Salesforce, QB POS) will use secure, authenticated connections (OAuth 2.0 recommended).

## 5. Other Non-Functional Requirements

### 5.1 Security
*   All passwords shall be stored using strong, salted, hashing algorithms (e.g., bcrypt).
*   The system shall be protected against common web vulnerabilities (OWASP Top 10).
*   Session management shall be secure, with timeouts after 30 minutes of inactivity.

### 5.2 Data Integrity
*   The system shall prevent the deletion of inventory items that have associated historical transactions (sale, donation). A "deactivate" or "archive" status shall be used instead.
*   Referential integrity between donations, items, and constituents shall be enforced at the database level.

## 6. Appendices

### 6.1 Success Metrics
*   **Processing Time:** Achieve a 30% reduction in average time from donation arrival to receipt generation and item tagging.
*   **Inventory Accuracy:** Maintain a perpetual inventory accuracy rate of 95% or higher, as measured by regular cycle counts.
*   **Integration Success:** Achieve >99% successful synchronization rate between IMS, QB POS, and Salesforce over a 30-day period post-launch.

### 6.2 Undecided Issues (To Be Resolved)
1.  The final design and dimensions of the category matrix display in the management UI.
2.  Specific make/model specifications for mobile tablets and rugged cases for pickup associates.
3.  Detailed disaster recovery procedures and Recovery Time Objective (RTO).
4.  The technical implementation approach for integrating inventory availability with the Construction Junction public website.
5.  The complete, finalized list of standard report formats and their parameters.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| Quality Assurance | | | |