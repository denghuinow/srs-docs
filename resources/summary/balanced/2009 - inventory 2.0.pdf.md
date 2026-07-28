# Balanced Summary: Construction Junction Inventory Management System

## Goals and Scope
The Inventory Management System is designed to allow Construction Junction staff to create, maintain, and view categorized inventory contents and value. It facilitates receiving items via donation processes and integrates with QuickBooks POS and the organization's website. The scope includes creating a categorized inventory system with functionality identified by the Construction Junction team, with implementation based on project planning estimates.

## Stakeholders and User Stories
**Stakeholders:**
- **Administrator:** Manages all inventory functions and system configuration.
- **Director:** Performs managerial functions and manages user accounts.
- **Manager:** Changes item properties and oversees inventory operations.
- **Receiving Associate:** Receives donated items and performs initial inventory entry.
- **Customer Service Representative:** Handles constituent management, returns, and drop-off acquisitions.
- **Pickup Associate:** Picks up donated items for processing.
- **Decon Associate:** Executes deconstruction jobs and brings items for processing.
- **Sales Associate:** Processes customer purchases.
- **Donor:** Donates items and receives tax deductions.
- **Buyer:** Purchases items from inventory.
- **Primary Contact:** Acts as main contact for donations.
- **Vendor:** Sells items to be added to inventory.
- **Consigner:** Donates items under consignment.

**User Stories:**
1. As a Receiving Associate, I want to enter donated items into the system so that donors receive receipts and items are tracked.
2. As a Manager, I want to modify item properties and prices so that inventory remains accurate and properly valued.
3. As a Sales Associate, I want to process item sales through QuickBooks POS so that inventory quantities are automatically updated.
4. As an Administrator, I want to define inventory departments and categories so that items are organized systematically.
5. As a Customer Service Representative, I want to create drop-off acquisitions so that unexpected donations can be processed.
6. As a Donor, I want to receive a donation receipt so that I can claim tax deductions.

## Key Processes
1. **View Inventory:** User accesses main screen displaying departments in matrix format (trigger: user login).
2. **Add Item to Inventory:** User drills down to category and enters item information (trigger: donation processing or inventory maintenance).
3. **Receive Acquisition:** Receiving Associate locates donation request and enters item details (trigger: donor arrival with acquisition number).
4. **Sell Item:** Sales associate scans item tags and processes sale in QuickBooks POS (trigger: customer purchase).
5. **Manage Departments/Categories:** Administrator defines or modifies inventory structure (trigger: organizational need).
6. **Suggest Item Price:** System provides pricing recommendations based on historical data (trigger: item entry or modification).
7. **Generate Reports:** System produces inventory, acquisition, and donor reports (trigger: user request).

## Domain Data Elements
1. **Department:** Primary Key: Department ID; Fields: Name, POS Department Code, Unique Tag, Status
2. **Category:** Primary Key: Category ID; Fields: Name, Unique Tag, Type (Unique/Stock/Under $5), Price, Parent Department
3. **Inventory Item:** Primary Key: Item Number; Fields: Description, Condition, Quantity, Price, Category
4. **Acquisition:** Primary Key: Acquisition Number; Fields: Type, Donor ID, Status, Start Date, End Date
5. **Donor:** Primary Key: Donor ID; Fields: Name, Contact Information, Donor Type, Location
6. **Attribute/Detail:** Primary Key: Attribute ID; Fields: Name, Type, Assigned Departments/Categories, Status

## Non-functional Requirements
1. **Usability:** Interface must be touch-screen optimized with minimal keyboard use.
2. **Availability:** System must be available during normal operating hours for internal users and extended hours for website access.
3. **Security:** Role-based access control with audit trails for sensitive operations.
4. **Performance:** Consistently low response times to avoid impacting business operations.
5. **Interoperability:** Integration with QuickBooks POS, Salesforce CRM, and website.
6. **Maintainability:** Built using approved technologies and industry best practices.

## Milestones and External Dependencies
1. Data migration from QuickBooks POS to Salesforce CRM.
2. Integration with QuickBooks POS for inventory synchronization.
3. Integration with Salesforce CRM for donor and acquisition data.
4. Website integration for online inventory viewing and purchasing.
5. Implementation of e-Blast functionality with Vertical Response/ExactTarget.

## Risks and Mitigation Strategies
1. **Integration Complexity:** Use middleware for system interfaces and thorough testing.
2. **Data Migration Issues:** Utilize CRM Fusion tools and validate migrated data.
3. **Performance Degradation:** Design for scalability and monitor system performance.
4. **User Adoption Resistance:** Provide comprehensive training and user-friendly interfaces.
5. **Vendor Product Changes:** Maintain flexible architecture and monitor vendor roadmaps.

## Undecided Issues
1. Final matrix dimensions for department/category display.
2. Specific hardware selection for mobile handheld units.
3. Decision on Google Apps vs. Microsoft Office integration.
4. Final e-Blast service provider (Vertical Response vs. ExactTarget).
5. Implementation details for customer wish list notifications.
6. Specific formats for inventory item signage generation.