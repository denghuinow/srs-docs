# Detailed Summary: Inventory Management System for Construction Junction

## Background and Scope
This document defines the requirements for an Inventory Management System for Construction Junction (CJ), a nonprofit retail outlet for used building materials. The system will manage a categorized inventory, facilitate donation processing (drop-off, pickup, deconstruction), integrate with QuickBooks POS and CJ's website, and provide reporting capabilities. It will support unique items (individually priced), stock items (standard price), and under-$5 items (not tracked). Non-goals include implementing all medium/low-priority features (e.g., e-commerce, mobile units) in the initial release and replacing existing CRM (Salesforce) or POS systems.

## Stakeholders Matrix and Use Cases
*   **Administrator**: Manages inventory structure (departments/categories), attributes, details, and all inventory functions.
*   **Director**: Performs manager functions plus user management.
*   **Manager**: Performs receiving associate functions plus item property changes.
*   **Receiving Associate**: Receives donations at the dock, enters items into inventory, and generates donation receipts.
*   **Customer Service Representative**: Manages constituent data, processes returns, and creates drop-off acquisitions.
*   **Pickup Associate**: Picks up donated items and initiates receiving process but cannot finalize additions to inventory.
*   **Decon Associate**: Executes deconstruction jobs and initiates receiving process but cannot finalize additions to inventory.
*   **Sales Associate**: Processes customer purchases via QuickBooks POS.
*   **Donor/Primary Contact**: Donates items and receives a tax receipt.
*   **Buyer**: Purchases items from inventory.

**Main Scenarios**: View categorized inventory; Add item (during donation or maintenance); Receive acquisition (process donation); Sell item (via POS integration); Generate reports.
**Exception Scenarios**: Adjust item quantity (with reason); Split an item into multiple items; Move/merge categories; Handle invalid data during management operations.

## Business Process
**Main Process: Receive Donation & Add to Inventory**
1.  **Trigger**: Donor arrives with acquisition number or for unscheduled drop-off.
2.  Receiving Associate locates or creates (CRM) the acquisition record.
3.  Associate navigates inventory matrix to select item category.
4.  Associate enters item details (quantity, condition, price, attributes).
5.  System validates data and suggests price (for unique items).
6.  Associate prints donation receipt for donor.
7.  Associate prints item tag (for unique/stock items) and attaches it.
8.  System adds item to inventory and syncs with QuickBooks POS.
**Key Branch A: Unscheduled Drop-off**
    1. Create new Drop-Off acquisition in CRM.
    2. Proceed to main process step 3.
**Key Branch B: Item Requires Further Processing**
    1. Print temporary label with acquisition info.
    2. Leave acquisition as "Partially Received".
    3. Complete processing later via main process.

## Domain Model
*   **Department** (Name: required, unique; POS Department Code: required; Unique Tag: required, unique)
*   **Category** (Name: required, unique; Unique Tag: required, unique; Type: required [Unique, Stock, Under $5]; Price: required for Stock)
*   **Inventory Item** (Item Number: system-generated, unique; Quantity: required; Condition: required for Unique; Price: required for Unique; Description: required for generic/Under $5; Category: reference)
*   **Attribute** (Name: required, unique; Type: required [Material, Finish, Color, Features])
*   **Detail** (Name: required, unique; Type: required [Number, Text, Selection]; Options: required if Selection)
*   **Acquisition** (Acquisition Number: unique; Type: required [Drop-Off, Pick Up, Decon]; Status: required [Expected, Partially Received, Completed]; Donor: reference)
*   **Donor/Primary Contact** (Name; Contact Info - managed in CRM)
*   **Item History** (Action: required; Date/Time: required; User: reference; Item: reference)

## Interfaces and Integrations
1.  **QuickBooks POS** (Bidirectional)
    *   **Theme**: Inventory and sales synchronization.
    *   **Input**: New/updated items, quantity changes from Inventory System.
    *   **Output**: Sale transactions, updated quantities to Inventory System.
    *   **SLA**: Near real-time updates for sales; prompt updates for inventory changes.
2.  **Salesforce CRM** (Bidirectional)
    *   **Theme**: Donor and acquisition data management.
    *   **Input**: Acquisition records, donor info from CRM.
    *   **Output**: Updated acquisition status, added item details to CRM.
    *   **SLA**: Immediate visibility of changes in both systems.
3.  **Construction Junction Website** (Outbound from Inventory)
    *   **Theme**: Inventory display and online functionality.
    *   **Input**: Categorized inventory data, item availability.
    *   **Output**: Website displays inventory for browsing, wish lists, and (future) e-commerce.
    *   **SLA**: Regular data feed; website reflects inventory changes.
4.  **Vertical Response/ExactTarget** (Outbound from Inventory)
    *   **Theme**: E-blast marketing integration.
    *   **Input**: "Blastworthy" flagged items from Inventory System.
    *   **Output**: Item data for email campaigns.
    *   **SLA**: Data available for weekly e-blast generation.
5.  **Hardware Interfaces** (Input/Output)
    *   **Theme**: Operational support.
    *   **Interaction**: Touch screens, barcode scanners, label printers.
    *   **Key Points**: UI designed for touch; support for scanning item tags and member cards.

## Acceptance Criteria
**Capability: Process a Drop-Off Donation**
*   **Given** a donor arrives without an appointment and a Receiving Associate is logged in,
*   **When** the associate creates a new Drop-Off acquisition in CRM and completes the item receipt process,
*   **Then** a donation receipt is printed, the item is added to inventory, and the acquisition status is "Completed".
**Capability: Sell a Unique Inventory Item**
*   **Given** a unique item exists in inventory and is tagged,
*   **When** a Sales Associate scans its tag and completes the sale in QuickBooks POS,
*   **Then** the item's quantity is decremented in the Inventory System and the sale is recorded in its history.

## Non-functional Metrics
*   **Performance**: System response times must be consistently low to not impede dock or sales floor operations. The inventory matrix must support at least 30 tiles per level.
*   **Reliability**: No specific requirements stated, but availability is required during and beyond business hours for different user groups.
*   **Security**: Role-based access control (8 defined roles); audit logging for sensitive operations (price changes, deletions).
*   **Compliance**: Must generate tax receipts for donors.
*   **Observability**: System must record processing time per acquisition and maintain full item history.

## Milestones and Release Strategy
1.  Core Inventory Management (View/Manage departments/categories/items).
2.  Donation Processing Integration (Acquisition receipt, basic CRM/QuickBooks POS sync).
3.  Reporting Module (Basic inventory and acquisition reports).
4.  Website Integration (Inventory display).
5.  Enhanced Features (E-blast flagging, price suggestions, membership program).
6.  Advanced Features (E-commerce, mobile handheld units).

## Risk List and Mitigation Strategies
1.  **Risk**: Complex integration with QuickBooks POS and Salesforce.
    *   **Mitigation**: Use middleware; define clear, phased sync requirements.
2.  **Risk**: Data migration from legacy POS for constituents/history.
    *   **Mitigation**: Utilize purchased tools (Demand Tools); extensive testing.
3.  **Risk**: Usability challenges for touch-screen dock operations.
    *   **Mitigation**: Design UI with large buttons/spacing; involve users in prototype testing.
4.  **Risk**: Overly complex inventory categorization hindering staff use.
    *   **Mitigation**: Provide training; implement intuitive matrix navigation with shortcuts.
5.  **Risk**: Performance degradation with large inventory volume.
    *   **Mitigation**: Architect for scalability; optimize database queries and matrix loading.
6.  **Risk**: Inaccurate price suggestions leading to revenue loss.
    *   **Mitigation**: Algorithm tuning with historical data; keep price entry as a manual override.
7.  **Risk**: Scope creep from numerous medium/low-priority requirements.
    *   **Mitigation**: Strict prioritization and phased release strategy.
8.  **Risk**: Lack of disaster recovery/business continuity plan.
    *   **Mitigation**: Develop and document procedures as part of implementation.

## Undecided Issues and Responsible Parties
1.  Final dimensions of the inventory matrix tiles. *(System Architect)*
2.  Selection of middleware for QuickBooks POS/Salesforce integration. *(Technical Sponsor)*
3.  Decision to proceed with VerticalResponse or migrate to ExactTarget for e-blasts. *(Business Sponsor)*
4.  Specification of RFID vs. standard barcode for item tags. *(Operations & Technical Sponsor)*
5.  Definition of "regular data transfer" frequency for website inventory updates. *(System Architect)*
6.  Approval of specific hardware models for touch screens, scanners, and printers. *(Operations)*
7.  Development of detailed disaster recovery and backup procedures. *(Technical Sponsor)*
8.  Resolution of potential Google Apps migration and its impact on integrations. *(Business Sponsor)*