# Software Requirements Specification (SRS)
## Categorized Inventory Management System (CIMS)
### For Construction Junction

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft for Review  
**Prepared for:** Construction Junction Stakeholders  
**Prepared by:** [Your Name/Team]

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Categorized Inventory Management System (CIMS). The primary purpose of this document is to provide a detailed description of the system's capabilities, interfaces, and performance characteristics to serve as a basis for design, development, testing, and stakeholder agreement.

### 1.2 Document Conventions
This document follows standard SRS conventions. Requirements are uniquely identified with tags (e.g., `FR-001`, `NF-002`). Markdown is used for formatting, with headers, lists, and code blocks to enhance readability.

### 1.3 Project Scope
The Categorized Inventory Management System (CIMS) is a software application designed to manage the complete lifecycle of donated construction and building materials for Construction Junction, from donor acquisition through point-of-sale. The system will provide a centralized, categorized inventory database, streamline donor receipting, manage stock levels, and integrate seamlessly with existing business systems (QuickBooks Point of Sale and Salesforce CRM). The system will be deployed on touch-screen workstations and utilize barcode scanners for efficient operations in warehouse and sales environments.

**In-Scope:**
*   Management of a hierarchical inventory categorization system.
*   Processing of donor acquisitions and generation of donation receipts.
*   Real-time inventory updates based on sales and internal adjustments.
*   User interfaces optimized for touch and barcode scanner input.
*   Bi-directional integration with QuickBooks Point of Sale (QBPOS) for sales data.
*   Integration with Salesforce CRM for donor/customer information.
*   User role-based access control for Construction Junction staff.

**Out-of-Scope:**
*   Development of the QBPOS or Salesforce CRM systems.
*   Financial accounting beyond inventory valuation.
*   Direct e-commerce sales functionality on the public website (integration only).
*   Mobile applications for field operations (e.g., pickup associates).
*   Payroll or human resources management.

### 1.4 References
*   Construction Junction Business Process Documentation
*   QuickBooks Point of Sale SDK/API Documentation
*   Salesforce CRM API Documentation
*   Internal Style Guide & Branding Standards

## 2. Overall Description

### 2.1 Product Perspective
CIMS is a new, self-contained software system that will replace and enhance existing manual and disparate inventory tracking methods. It will act as the "system of record" for inventory, interfacing with two critical external systems:
1.  **QuickBooks Point of Sale (QBPOS):** CIMS will send item master data (category, description, cost) to QBPOS. QBPOS will send sales transaction data back to CIMS to decrement inventory.
2.  **Salesforce CRM:** CIMS will query and update donor/customer records within Salesforce, linking donations and purchases to constituent profiles.

### 2.2 Product Functions
The core high-level functions of CIMS are:
1.  **Inventory Hierarchy Management:** Create, navigate, and maintain a multi-level categorized tree of inventory items (e.g., Building Materials > Lumber > Hardwood > Oak).
2.  **Donor Acquisition Processing:** Record donor information, item descriptions, quantities, and values to add new stock to inventory, and generate IRS-compliant donation receipts.
3.  **Inventory Lifecycle Management:** Adjust item attributes, quantities (for breakage, loss, bundling), and split lots into separate sellable units.
4.  **Sales Synchronization:** Receive sales data from QBPOS and automatically update on-hand quantities and statuses.
5.  **Reporting & Search:** Provide real-time views of inventory levels, donation history, and item details through search and filtered lists.

### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key System Interactions |
| :--- | :--- | :--- |
| **Administrator** | Full system access. IT proficient. | Configure system settings, manage user roles, oversee integrations, generate advanced reports. |
| **Director/Manager** | Decision-makers. Need summary data. | View high-level dashboards, run inventory valuation reports, adjust pricing strategies. |
| **Receiving Associate** | Warehouse staff. Primary data entry. | Process donor acquisitions, print receipts, apply barcodes, perform initial item categorization. |
| **Sales Associate** | Floor staff. Fast-paced environment. | Look up item details/availability, check inventory levels, process holds (via integration). |
| **Pickup/Decon Associate** | Field & warehouse staff. | Update item status (e.g., "received," "in deconstruction"), adjust quantities post-processing. |
| **Customer Service Rep** | Office staff. Donor/Buyer facing. | Look up donation/purchase history, assist with receipts, manage customer issues related to inventory. |
| **Donor** | External user. Interacts via receipt. | Provides donation info. Receives printed receipt. No direct system login. |
| **Buyer** | External customer. | Views inventory on integrated website. No direct CIMS login. |

### 2.4 Operating Environment
*   **Hardware:** Touch-screen enabled workstations (minimum 15"), barcode scanners (USB/HID), receipt printers in receiving area, network infrastructure.
*   **Software:** Windows 10/11 operating system, .NET Framework or equivalent runtime, QBPOS (version specified), Salesforce CRM instance.
*   **Network:** Secure local area network (LAN) with reliable internet connection for cloud integrations.

### 2.5 Design and Implementation Constraints
1.  **Integration Constraint:** Must utilize published APIs or SDKs for QuickBooks Point of Sale and Salesforce. Customization of these core platforms is not allowed.
2.  **Usability Constraint:** All core transactional interfaces (receiving, inventory adjustment) must be fully operable via touch screen (large buttons, minimal typing) and barcode scanner.
3.  **Data Model Constraint:** The inventory categorization hierarchy must support at least four levels of depth to accommodate detailed item classification.

### 2.6 Assumptions and Dependencies
*   **Assumption:** QBPOS and Salesforce systems will be available and responsive during normal business hours.
*   **Assumption:** Staff will be trained on the new system and procedures.
*   **Dependency:** Successful integration is dependent on the stability and continued support of QBPOS and Salesforce APIs.
*   **Dependency:** Project timeline is dependent on timely access to subject matter experts (SMEs) from Construction Junction staff.

## 3. System Features

### 3.1 Feature 1: Hierarchical Inventory Navigation & Viewing
**Description:** Users shall be able to browse and search the inventory through a visual, hierarchical category tree and detailed list views.

**Requirements:**
*   `FR-001`: The system shall display a navigable tree view of inventory categories and subcategories.
*   `FR-002`: Selecting a category in the tree shall display a list of all inventory items within that category and its subcategories.
*   `FR-003`: The list view shall display columns for Item ID, Description, Category, Quantity On Hand, Location, Status, and Value.
*   `FR-004`: The system shall provide a global search function that searches item ID, description, and donor name.

### 3.2 Feature 2: Donor Acquisition Processing
**Description:** Receiving Associates shall record new donations, add items to inventory, and generate donor receipts.

**Requirements:**
*   `FR-010`: The system shall allow lookup or creation of a donor profile by entering name/email, synchronized with Salesforce.
*   `FR-011`: For each donated item, the user shall select a category, enter description, quantity, condition, estimated fair market value, and optional notes.
*   `FR-012`: The system shall automatically generate a unique, sequential Donation Receipt ID and Item ID/Barcode for each distinct item or lot.
*   `FR-013`: Upon finalizing the acquisition, the system shall print an IRS-compliant donation receipt listing all items, values, and donor information.
*   `FR-014`: All items from the acquisition shall be immediately added to inventory with a status of "Received."

### 3.3 Feature 3: Inventory Management Operations
**Description:** Authorized staff shall modify, adjust, and manage existing inventory items.

**Requirements:**
*   `FR-020`: The system shall allow modification of an item's description, category, condition, value, and notes.
*   `FR-021`: The system shall allow adjustment of an item's quantity (e.g., due to breakage, discovery) with a required reason code.
*   `FR-022`: The system shall allow a "Split" function to divide a multi-quantity lot into separate, individually trackable items, each receiving a new unique ID/barcode.
*   `FR-023`: All management actions shall be logged with user ID, timestamp, and details of the change.

### 3.4 Feature 4: Sales Integration & Inventory Update
**Description:** The system shall automatically reflect inventory changes due to sales made in QBPOS.

**Requirements:**
*   `FR-030`: The system shall provide a secure interface (API/Service) to receive sales transaction data from QBPOS in near real-time.
*   `FR-031`: Upon receiving a sale confirmation for an item, the system shall decrement the quantity on hand for that specific item ID.
*   `FR-032`: If an item's quantity reaches zero, its status shall change to "Sold Out."
*   `FR-033`: The system shall log all sales synchronizations and flag any discrepancies (e.g., item sold in QBPOS not found in CIMS).

### 3.5 Feature 5: Integration with External Systems
**Description:** The system shall exchange data with QBPOS and Salesforce CRM.

**Requirements:**
*   `FR-040`: The system shall push new item master data (ID, Description, Category, Cost) to QBPOS upon item creation in CIMS.
*   `FR-041`: The system shall query Salesforce to retrieve donor information during acquisition processing using donor name or ID.
*   `FR-042`: The system shall create or update the donor's record in Salesforce with a summary of the donation (Receipt ID, Total Value, Date).
*   `FR-043`: All integration failures shall be logged in a system alert queue for administrator review.

## 4. External Interface Requirements

### 4.1 User Interfaces
*   **UI-01:** Touch-Optimized Receiving Interface: Large form fields, button-based category selection, and barcode scan input focus.
*   **UI-02:** Inventory Management Dashboard: Combines category tree, list view, and search panel in a single responsive window.
*   **UI-03:** Administrative Console: Standard desktop application interface for configuration and user management.

### 4.2 Hardware Interfaces
*   **HI-01:** The system shall interface with standard USB HID barcode scanners. A scanned barcode shall be interpreted as direct data entry into the focused field.
*   **HI-02:** The system shall support standard Windows-compatible receipt printers for generating donation receipts.

### 4.3 Software Interfaces
*   **SI-01: QuickBooks Point of Sale Interface**
    *   **Method:** QBPOS SDK or REST API.
    *   **Data to QBPOS:** Item Add/Update (Item Name, SKU (CIMS ID), Price, Category).
    *   **Data from QBPOS:** Sales Transaction Data (SKU, Quantity Sold, Timestamp).
*   **SI-02: Salesforce CRM Interface**
    *   **Method:** Salesforce REST API (OAuth 2.0).
    *   **Data to/from Salesforce:** Donor/Customer Object (Name, Address, Email, Phone, Donation History).

### 4.4 Communications Interfaces
*   **CI-01:** HTTP/S over LAN/WAN for integration with cloud-based Salesforce services.
*   **CI-02:** Local TCP/IP or SDK-based communication with QBPOS on the same network.

## 5. Non-Functional Requirements

### 5.1 Performance Requirements
*   `NF-001`: The system shall load the main inventory list view in less than 2 seconds for a category with up to 500 items.
*   `NF-002`: Barcode scan to item lookup response time shall be less than 1 second under normal load.
*   `NF-003`: Synchronization of a sales batch from QBPOS shall complete within 30 seconds.

### 5.2 Safety Requirements
*   Not applicable beyond standard electrical safety for hardware.

### 5.3 Security Requirements
*   `NF-010`: The system shall implement role-based access control (RBAC) as defined in Section 2.3.
*   `NF-011`: All user authentication shall be managed via integration with the organization's Active Directory.
*   `NF-012`: All data transmitted to external systems (Salesforce) shall be encrypted in transit using TLS 1.2 or higher.
*   `NF-013`: Audit logs for inventory adjustments and donor data access shall be maintained and non-erasable by standard users.

### 5.4 Software Quality Attributes
*   **Usability:** Core workflows for Receiving Associates shall be completable with fewer than 3 mouse/touch clicks or focused field changes per donated item.
*   **Reliability:** The system shall achieve 99.5% uptime during business hours (8 AM - 6 PM, Mon-Sat).
*   **Maintainability:** The system shall be designed with modular components, allowing for independent updates to the integration modules without affecting core inventory logic.
*   **Portability:** The application shall be compatible with any Windows 10/11 workstation meeting minimum hardware specifications.

---
**Appendices**

*Appendix A: Glossary*
*   **Item ID/SKU:** Unique identifier and barcode for a single sellable unit or lot.
*   **Donation Receipt ID:** Unique identifier for a donor's transaction containing one or more items.
*   **Acquisition:** The process and record of receiving items from a donor.
*   **QBPOS:** QuickBooks Point of Sale.

*Appendix B: To Be Determined (TBD)*
*   Specific field mappings for Salesforce donor object.
*   Branding and logo specifications for printed receipts.
*   Detailed report mockups for management dashboards.