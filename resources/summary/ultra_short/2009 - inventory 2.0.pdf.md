**Purpose & Scope**: The system manages categorized inventory for Construction Junction, enabling tracking of donated items from donation through sale. It handles unique and stock items but does not track Under $5 items (only for donation receipt purposes). It integrates with QuickBooks POS and the organization's website but does not handle shipping or physical item movement.

**Product Background / Positioning**: This system replaces manual inventory tracking with a digital solution integrated into Construction Junction's existing retail and donation management ecosystem. It connects with QuickBooks POS for sales processing and Salesforce CRM for donor acquisition data, supporting the organization's mission of receiving and reselling donated items.

**Core Functional Overview**: 
- View inventory in hierarchical department-category-item structure
- Manage inventory structure (departments, categories, attributes)
- Add items to inventory during donation processing or routine maintenance
- Receive acquisitions (process donated items via drop-off, pick-up, deconstruction)
- Sell items through QuickBooks POS with automatic inventory updates
- Suggest item pricing based on historical data
- Generate reports on inventory, acquisitions, and donor activity
- Track item history and pricing adjustments

**Key Users & Usage Scenarios**: Administrators, Directors, and Managers have full inventory access. Receiving Associates process donations and print receipts. Pickup/Decon Associates initiate receiving but cannot complete inventory additions. Sales Associates process sales via POS. Customer Service Representatives handle donor inquiries and wish lists. Donors and Buyers interact with the system indirectly through staff.

**Major External Interfaces**: QuickBooks POS (for inventory synchronization and sales), Salesforce CRM (for donor acquisition data), Construction Junction website (for online inventory browsing and e-commerce), and Vertical Response/ExactTarget (for email marketing). Hardware interfaces include touch screens, barcode readers, and Zebra printers.

**Key Non-functional Requirements**: Must support touch screen interface with intuitive navigation. Available during normal business hours for operations, and beyond hours for website use. Requires low response times for critical operations. Uses role-based access control with audit trails for sensitive operations. Maintains inventory data integrity through synchronization with QuickBooks POS.

**Constraints, Assumptions & Dependencies**: Must integrate with existing QuickBooks POS and Salesforce CRM systems. Uses matrix-based inventory navigation with minimum 30 slots per level. Under $5 items are not tracked in inventory (only for donation receipt purposes). Requires QuickBooks POS to handle item pricing and sales data.

**Priorities & Acceptance Approach**: Medium-priority features include website integration, e-blast flagging, e-commerce, and membership program. Low-priority features include mobile handheld units and inventory item story/history. Acceptance requires successful integration with QuickBooks POS, accurate inventory tracking, and functional reporting capabilities.