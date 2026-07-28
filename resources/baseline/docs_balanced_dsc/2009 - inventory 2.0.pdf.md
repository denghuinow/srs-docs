# Software Requirements Specification (SRS)
## Construction Junction Inventory Management System (IMS)

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft for Review  
**Prepared for:** Construction Junction  
**Prepared by:** [Your Company/Team Name]

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Construction Junction Inventory Management System (IMS). The intended audience includes project stakeholders, developers, testers, and project managers. This document serves as the foundation for system design, implementation, and verification.

#### 1.2 Project Scope
The IMS is a comprehensive software solution designed to digitize and streamline the inventory lifecycle for Construction Junction, a non-profit building material reuse center. The system will enable staff to create, maintain, and view categorized inventory contents and value. Core functionalities include processing donations (acquisitions), managing inventory hierarchy (departments/categories), integrating with QuickBooks Point of Sale (POS) for sales, synchronizing with Salesforce CRM for donor management, and providing data to the organization's website for online viewing. The scope is bounded by the specific user stories and key processes outlined by the Construction Junction team.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **IMS:** Inventory Management System
*   **POS:** Point of Sale
*   **CRM:** Customer Relationship Management
*   **UI:** User Interface
*   **RBAC:** Role-Based Access Control
*   **API:** Application Programming Interface
*   **Acquisition:** A transaction representing the receipt of items into inventory, typically via donation, consignment, or vendor purchase.
*   **Decon:** Deconstruction

#### 1.4 References
*   Construction Junction Business Process Documentation
*   QuickBooks POS API Documentation
*   Salesforce CRM API Documentation

#### 1.5 Document Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product. Section 3 details specific system requirements. Appendices may contain supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
The IMS is a new, self-contained web application that will interface with several existing external systems:
*   **QuickBooks POS:** For real-time sales processing and inventory quantity updates.
*   **Salesforce CRM:** As the system of record for Donor and Acquisition data.
*   **Construction Junction Website:** To display available inventory and facilitate online purchases.
*   **E-Blast Service (Vertical Response/ExactTarget):** For marketing communications.

The system will replace and enhance manual or QuickBooks-limited inventory tracking processes.

#### 2.2 User Classes and Characteristics
| User Class | Primary Responsibilities | Key Characteristics |
| :--- | :--- | :--- |
| **Administrator** | System configuration, defining inventory structure (departments/categories). | Technical proficiency, understands business taxonomy. |
| **Director** | Managerial oversight, user account management. | Strategic view, requires summary data and controls. |
| **Manager** | Modifying item properties, prices, overseeing daily operations. | Tactical decision-making, needs edit permissions. |
| **Receiving Associate** | Processing scheduled donations, entering item details. | On-site, needs efficient, touch-optimized data entry. |
| **Customer Service Rep** | Handling walk-in donations (drop-offs), constituent management. | Front-desk, must handle unplanned acquisitions. |
| **Pickup/Decon Associate** | Initiating acquisitions for items collected off-site. | Mobile/field role, may need offline capability. |
| **Sales Associate** | Finalizing customer purchases at POS. | Relies on POS integration; does not directly use IMS UI for sales. |
| **Donor/Consigner/Vendor** | Providing items to inventory. | External actor, interacts via receipt generation or CRM. |
| **Buyer** | Purchasing inventory items. | External actor, interacts via POS or website. |

#### 2.3 Operating Environment
*   **Software:** Modern web browser (Chrome, Firefox, Edge). Backend built on approved technology stack (e.g., .NET/Java, SQL Server/PostgreSQL).
*   **Hardware:** Standard desktop PCs, touch-screen kiosks, and mobile handheld units (specific model TBD) for warehouse use.
*   **Network:** Secure internal LAN with controlled external access for integrations.

#### 2.4 Design and Implementation Constraints
1.  Must integrate via API with existing QuickBooks POS and Salesforce CRM systems.
2.  UI must be designed for touch-screen interaction with large, tappable elements.
3.  Must adhere to Construction Junction's data security and privacy policies.
4.  Architecture must be maintainable using in-house technical skills.

#### 2.5 Assumptions and Dependencies
*   **Assumptions:** Stable internet connectivity is available at the main facility. External systems (QuickBooks, Salesforce) will maintain stable APIs.
*   **Dependencies:**
    1.  Successful data migration from QuickBooks POS to Salesforce CRM.
    2.  Availability of API documentation and support for QuickBooks POS and Salesforce.
    3.  Final selection of e-blast service provider (Vertical Response or ExactTarget).

### 3. System Requirements

#### 3.1 Functional Requirements

**3.1.1 Inventory Hierarchy Management**
*   **FR-1:** The system shall allow users with the 'Administrator' role to create, read, update, and deactivate **Department** records (Department ID, Name, POS Department Code, Unique Tag, Status).
*   **FR-2:** The system shall allow users with the 'Administrator' role to create, read, update, and deactivate **Category** records (Category ID, Name, Unique Tag, Type [Unique/Stock/Under $5], Default Price, Parent Department).
*   **FR-3:** The system shall display the inventory hierarchy on the primary dashboard as a matrix of Departments (dimensions TBD).

**3.1.2 Acquisition & Donor Management**
*   **FR-4:** The system shall allow 'Receiving Associates' to locate an existing Acquisition record by Acquisition Number (linked from Salesforce CRM).
*   **FR-5:** The system shall allow 'Receiving Associates' and 'Customer Service Reps' to create new 'Drop-off' Acquisition records for unscheduled donations.
*   **FR-6:** Upon saving an Acquisition, the system shall generate a printable donor receipt suitable for tax deduction purposes.

**3.1.3 Inventory Item Lifecycle**
*   **FR-7:** The system shall allow authorized users ('Receiving Associate', 'Manager') to **Add Items** to inventory by selecting a Category and entering details (Description, Condition, Quantity, Price, Attributes).
*   **FR-8:** The system shall provide a **Price Suggestion** for new items based on historical data of similar items in the same category.
*   **FR-9:** The system shall allow users with the 'Manager' role to **Modify Item** properties, including Price, Condition, and Description.
*   **FR-10:** When a sale is processed in **QuickBooks POS**, the system shall automatically decrement the quantity of the sold item in the IMS database via real-time integration.

**3.1.4 Reporting**
*   **FR-11:** The system shall generate an **Inventory Valuation Report** showing total value by Department/Category.
*   **FR-12:** The system shall generate an **Acquisition Summary Report** filtered by date range and donor type.
*   **FR-13:** The system shall generate a **Donor Contribution Report** for tax season.

**3.1.5 System Administration**
*   **FR-14:** The system shall implement **Role-Based Access Control (RBAC)** to enforce permissions based on user roles defined in Section 2.2.
*   **FR-15:** The system shall maintain an **Audit Trail** logging all create, update, and delete operations on Inventory Items, Prices, and Acquisition records.

#### 3.2 Non-Functional Requirements

**3.2.1 Usability**
*   **NFR-1:** The user interface shall be optimized for touch-screen interaction (minimum touch target size of 44x44 pixels).
*   **NFR-2:** Common data entry workflows (e.g., adding an item) shall be achievable with minimal keyboard use, utilizing dropdowns, checkboxes, and large buttons.

**3.2.2 Performance**
*   **NFR-3:** The system shall have a maximum page load time of 3 seconds for 95% of page requests under normal load.
*   **NFR-4:** Data entry operations (saving an item, completing an acquisition) shall have a response time of less than 2 seconds.

**3.2.3 Reliability & Availability**
*   **NFR-5:** The system shall be available for internal staff from 7:00 AM to 8:00 PM, Monday through Saturday (99.5% uptime).
*   **NFR-6:** The website integration feed shall have an availability of 99% during extended hours (6:00 AM to 11:00 PM daily).

**3.2.4 Security**
*   **NFR-7:** All user authentication shall be managed via integration with the organization's central directory (e.g., Active Directory).
*   **NFR-8:** Sensitive operations (price changes, user role changes) shall require re-authentication if the session is idle for more than 5 minutes.
*   **NFR-9:** All data in transit shall be encrypted using TLS 1.2 or higher.

**3.2.5 Interoperability**
*   **NFR-10:** The system shall synchronize inventory quantity and status with **QuickBooks POS** in near real-time (latency < 30 seconds).
*   **NFR-11:** The system shall use **Salesforce CRM** as the master source for Donor and Acquisition header information (Type, Donor ID, Status, Dates).
*   **NFR-12:** The system shall provide a secure API feed to the **Construction Junction website** for publishing inventory items, categories, and prices.

#### 3.3 Data Requirements
The system shall maintain the following core entities with the specified attributes:

```sql
-- Core Domain Entities
ENTITY Department {
    DepartmentID: PK, Integer
    Name: String
    POS_Department_Code: String
    Unique_Tag: String
    Status: Enum(Active, Inactive)
}

ENTITY Category {
    CategoryID: PK, Integer
    Name: String
    Unique_Tag: String
    Type: Enum(Unique, Stock, Under5)
    Default_Price: Decimal
    Parent_Department: FK -> Department
}

ENTITY InventoryItem {
    ItemNumber: PK, String/Integer
    Description: Text
    Condition: Enum(New, Like-New, Good, Fair, As-Is)
    Quantity: Integer
    Price: Decimal
    Category: FK -> Category
    AcquisitionID: FK -> Acquisition
    Date_Added: DateTime
}

ENTITY Acquisition {
    AcquisitionNumber: PK, String (from Salesforce)
    Type: Enum(Scheduled Pickup, Drop-off, Decon, Vendor, Consignment)
    DonorID: FK -> Donor (in Salesforce)
    Status: Enum(Scheduled, In Progress, Received, Cancelled)
    Start_Date: DateTime
    End_Date: DateTime
}
-- Note: Donor entity is mastered in Salesforce CRM.
```

### 4. Appendices

#### 4.1 User Story Mapping to Requirements
| User Story | Mapped Functional Requirements |
| :--- | :--- |
| As a Receiving Associate, I want to enter donated items... | FR-4, FR-7 |
| As a Manager, I want to modify item properties and prices... | FR-9, FR-15 |
| As a Sales Associate, I want to process item sales... | FR-10, NFR-10 |
| As an Administrator, I want to define inventory departments... | FR-1, FR-2 |
| As a Customer Service Rep, I want to create drop-off acquisitions... | FR-5, FR-6 |
| As a Donor, I want to receive a donation receipt... | FR-6 |

#### 4.2 Open Issues / TBD Items
1.  **UI-1:** Final matrix dimensions (e.g., 4x4, 5x5) for the department/category display on the main dashboard.
2.  **HW-1:** Specific model and OS for mobile handheld units used by Pickup/Decon associates.
3.  **INT-1:** Decision on depth of integration with Google Apps vs. Microsoft Office (e.g., report export).
4.  **INT-2:** Final selection and API details for the e-Blast service provider (Vertical Response vs. ExactTarget).
5.  **FUT-1:** Implementation details for customer wish list notification functionality.
6.  **OUT-1:** Specific format and template for automated inventory item signage generation.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| Quality Assurance | | | |