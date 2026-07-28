**Purpose & Scope**
The system is a "plug and play" web store application for new online store owners, enabling core e-commerce sales. It manages customer accounts, inventory, shopping carts, and order confirmations. It does not handle telephonic order integration, customer order analysis, or its own shipping/tracking number generation.

**Product Background / Positioning**
This is a new, self-contained system designed for users new to e-commerce. It runs on a dedicated USB key appliance with its own CPU and OS (Yoggie/Slackware Linux/Apache). It interfaces with an external payment system (WebOrder) for billing and inventory updates.

**Core Functional Overview**
*   Customer account management (registration, login, profile/payment info storage).
*   Product inventory management within multi-tiered categories.
*   Product search and browsing.
*   Shopping cart management (add/remove items, view totals).
*   Checkout and order confirmation with email notification.
*   System administration for user and privilege management.
*   A plug-in API for future functional extensions.

**Key Users & Usage Scenarios**
*   **Customer**: Browses/search for products, manages account, adds items to cart, checks out.
*   **Sales Personnel**: Manages product inventory (add, update, delete product details).
*   **System Administrator**: Manages user accounts and privileges, installs system patches and plug-ins.

**Major External Interfaces**
*   User Interface: Web browser (IE 6/7, Netscape 4/5).
*   Hardware Interface: Specific USB key appliance from Yoggie.
*   Software Interface: Programmatic interface to external "WebOrder" system for billing and inventory updates.
*   Communications Interface: Outbound email to customers (order confirmations) and administrators (queries).

**Key Non-functional Requirements**
*   **Performance**: Handle 1000 concurrent users; product search in <1 second; add to cart in <2ms.
*   **Security**: Encrypt all sensitive data via HTTPS and in the database; auto-detect and block IP DOS attacks.
*   **Availability**: 99.99% availability.
*   **Deployment**: System must be operational within 1 minute of plugging in the USB key.

**Constraints, Assumptions & Dependencies**
*   Must use a SQL database (MySQL specified).
*   Browser compatibility is only guaranteed for IE 6/7 and Netscape 4/5.
*   Dependent on Yoggie for the USB hardware, OS, drivers, and their stable baseline.
*   Assumes delivery of Yoggie development/test samples.

**Priorities & Acceptance Approach**
High-priority features are customer accounts, product management, purchasing/payment, and the plug-in API. Acceptance will involve verifying core e-commerce workflows (browse, cart, checkout), meeting the stated performance/availability metrics, and confirming operation within the defined constraints (browser, hardware).