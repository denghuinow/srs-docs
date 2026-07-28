**Purpose & Scope**
The system is an inventory management application for Construction Junction (CJ) to create, maintain, and view its categorized inventory. It facilitates receiving donated items and traces them from donation through sale. It does not replace the existing POS or CRM systems but integrates with them.

**Product Background / Positioning**
The system is a new application for CJ staff. It integrates with the existing QuickBooks Point of Sale (POS) system for sales processing and the Salesforce CRM system for donor and acquisition data. It also interfaces with CJ's public website.

**Core Functional Overview**
1.  View and navigate a categorized inventory hierarchy (departments, categories, items).
2.  Manage the inventory structure (add/edit/delete/move departments and categories).
3.  Receive donated items into inventory via acquisitions (Drop-Off, Pickup, Deconstruction).
4.  Add, modify, split, and adjust the quantity of inventory items.
5.  Generate and print donation receipts and item tags.
6.  Synchronize item data and sales with QuickBooks POS.
7.  Generate reports on inventory status, changes, and acquisitions.

**Key Users & Usage Scenarios**
*   **Administrator/Director:** Full system access, including user management and inventory structure configuration.
*   **Manager:** Can change item properties and prices.
*   **Receiving Associate:** Receives donations at the dock, enters items, prints receipts and tags.
*   **Pickup/Decon Associate:** Can initiate receiving processes off-site but cannot finalize them.
*   **Sales Associate:** Processes sales via QuickBooks POS, triggering inventory updates.
*   **Customer Service Representative:** Manages constituents and can create drop-off acquisitions.
*   **Donor/Buyer:** External actors who donate or purchase items.

**Major External Interfaces**
*   **Software:** Integration with QuickBooks POS (bi-directional sync of items and sales) and Salesforce CRM (acquisition and donor data).
*   **Hardware:** Support for touch screens, barcode scanners, and label printers.
*   **Website:** Provides inventory data for online viewing and potential e-commerce.

**Key Non-functional Requirements**
*   **Availability:** Must be available during all CJ operating hours for sales and donation processing; extended hours for inventory management and website.
*   **Security:** Role-based access control. System must record the user and time for sensitive operations (e.g., price changes, deletions).
*   **Performance:** Must perform with consistently low response times to avoid impacting business operations.
*   **Usability:** Interface must be optimized for touch screen workstations to minimize keyboard use and errors during acquisition processing.

**Constraints, Assumptions & Dependencies**
*   **Dependencies:** Successful operation is dependent on integration with QuickBooks POS and Salesforce CRM.
*   **Constraints:** The system must use CJ-approved technologies and be supportable by planned staffing levels.
*   **Assumption:** All acquisitions are created in the CRM system first.

**Priorities & Acceptance Approach**
Core functions for inventory management, donation receiving, and POS integration are the highest priority. Medium-priority features include website integration, e-blast flagging, and a membership program. Acceptance will be based on the system correctly performing the defined functional flows, meeting the stated non-functional metrics (e.g., availability), and successfully interfacing with the specified external systems.