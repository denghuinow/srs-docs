# Balanced Summary: E-Store Project

## Goals and Scope
The project aims to develop an E-Store for Marvel Electronics and Home Entertainment to enable online sales, distribution, and marketing of electronics. The scope includes comprehensive product management, customer profile handling, and a full online purchasing process with support for configuration, multiple payment methods, and order tracking.

## Stakeholders and User Stories
*   **Customer:** An end-user who browses, configures, and purchases products online.
*   **System Administrator:** Responsible for maintaining back-end systems, databases, and ensuring high availability.
*   **Shipping Department:** Manages shipping options, logistics, and provides tracking data.
*   **Sales System:** Handles order management and lifecycle.
*   **CRM System:** Provides customer support and relationship management.
*   **External Tax System:** Calculates applicable taxes for orders.

**User Stories:**
1.  As a Customer, I want to search and view detailed product information so that I can make an informed purchase decision.
2.  As a Customer, I want to configure a product by selecting components so that I can order a customized item.
3.  As a Customer, I want to manage a shopping cart and checkout using multiple payment methods so that I can complete purchases conveniently.
4.  As a Customer, I want to track my order and view my profile history so that I can manage my purchases.
5.  As a System Administrator, I want the database to be stored on redundant, RAID 5 systems so that data reliability and availability are ensured.
6.  As a Customer, I want to receive email confirmations and view secure, detailed invoices so that I have a record of my transaction.

## Key Processes
1.  **Product Browsing & Search:** (Trigger: Customer visits site) The system allows users to browse categorized products or use a search facility to find items.
2.  **Product Configuration:** (Trigger: Customer selects a configurable product) The system displays available components and allows the user to build a custom configuration, checking for conflicts.
3.  **Shopping Cart Management:** (Trigger: Customer adds an item) The system provides a cart where users can add or remove products before purchase.
4.  **Checkout & Payment:** (Trigger: Customer proceeds to checkout) The system calculates tax and shipping, presents payment options, and processes the secured transaction.
5.  **Order Confirmation & Fulfillment:** (Trigger: Payment is confirmed) The system sends an email confirmation, generates an invoice, and interfaces with sales and shipping systems.
6.  **Post-Purchase Support:** (Trigger: Customer views profile or seeks help) The system allows order tracking, changes/cancellations (if eligible), and provides customer support via FAQs and contact options.
7.  **Profile Management:** (Trigger: Customer creates or logs into an account) The system maintains and authenticates customer profiles, storing order history and preferences.

## Domain Data Elements
*   **Product:** (PK: Product ID) Name, Description, Category, Price, Image URL.
*   **Customer:** (PK: Customer ID) Name, Email Address, Shipping Address, Hashed Password.
*   **Order:** (PK: Order ID) Customer ID, Order Date, Total Amount, Status, Shipping Method.
*   **Order Line Item:** (PK: Line Item ID) Order ID, Product ID, Quantity, Unit Price.
*   **Shopping Cart:** (PK: Cart ID / Session ID) Customer ID, Product ID, Quantity.
*   **Payment Transaction:** (PK: Transaction ID) Order ID, Payment Method, Amount, Status, Date.

## Non-Functional Requirements
1.  **Usability:** Provide a uniform, accessible GUI with multi-language support and handicap access.
2.  **Reliability/Availability:** Ensure 99.999%+ uptime via ISP agreements and use redundant, RAID 5 back-end storage with off-site replication.
3.  **Security:** Use secure sockets (SSL) for confidential data, encrypt stored data, and never display passwords or full credit card numbers.
4.  **Performance:** The web-based application must have a load time under five minutes under normal internet conditions.
5.  **Supportability:** Maintain all source code in a configuration management tool.
6.  **Design Constraints:** Develop using standard web tools conforming to IBM CUA or Microsoft GUI standards.

## Milestones and External Dependencies
1.  Finalization and sign-off on Software Requirements Specification (SRS).
2.  Selection and contractual agreement with a high-availability Internet Service Provider (ISP).
3.  Integration with external systems (Tax, Credit Management, Export Regulation).
4.  Procurement and setup of redundant server hardware and RAID storage.
5.  Completion of user acceptance testing (UAT) with stakeholders.

## Risks and Mitigation Strategies
1.  **Risk:** Failure to meet high availability (99.999%) targets.
    *   **Mitigation:** Establish strict SLAs with the ISP and implement robust internal redundancy with automatic failover.
2.  **Risk:** Security breach exposing customer payment data.
    *   **Mitigation:** Enforce end-to-end encryption (SSL), never store full card details, and follow secure coding practices.
3.  **Risk:** Poor performance or long load times degrading user experience.
    *   **Mitigation:** Optimize web assets, implement caching, and conduct performance testing under load.
4.  **Risk:** Complex product configurator causing user confusion or errors.
    *   **Mitigation:** Implement clear conflict detection/notification and provide guided configuration steps.
5.  **Risk:** Integration failures with external software systems (e.g., Tax, CRM).
    *   **Mitigation:** Define clear, stable APIs for external interfaces and conduct early integration testing.

## Undecided Issues
1.  Specific choice of web development tool/framework (e.g., Java Applet, EJB, MS Front Page).
2.  Selection of the third-party secure transaction software (e.g., Verisign equivalent).
3.  Detailed specification of multi-language support implementation.
4.  Exact criteria and time limits for eligible order changes/cancellations.
5.  Specific structure and management process for online promotions and rewards.
6.  Detailed design of the online help system and FAQ content.