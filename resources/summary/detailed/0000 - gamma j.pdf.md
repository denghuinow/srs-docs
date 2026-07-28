# Detailed Summary: GAMMA-J Web Store

## Background and Scope
The GAMMA-J Web Store is a plug-and-play e-commerce solution designed for new online store owners, enabling quick setup and core business operations over the internet. Version 1 is implemented on a USB key with its own CPU and operating system, requiring no software installation. Key capabilities include customer account management, inventory management, shopping cart functionality, order confirmation, and a browser-based interface with SSL security. Non-goals include telephonic order integration, in-house transportation/tracking systems, and customer order analysis features.

## Stakeholders Matrix and Use Cases
*   **Customer**: An individual purchasing inventory; can register, log in, browse, manage a cart, and place orders.
*   **Sales Personnel**: The store owner or staff responsible for updating inventory, product descriptions, prices, and availability.
*   **System Administrator**: The owner or designated person responsible for system maintenance, user privilege assignment, and plug-in management.
*   **Development Team**: Uses the SRS for system design and implementation guidance.
*   **Test & Verification Team**: References the SRS to validate that requirements are met.
*   **Technical Writer**: Uses the SRS to assist in creating user documentation.
*   **Yoggie Corporation**: Provides the USB key hardware, base operating system, and drivers.

**Main Scenarios**: Customer registers, logs in, browses/search products, adds items to cart, checks out, and confirms order. Sales Personnel logs in and manages product catalog. System Administrator logs in and manages user accounts and plug-ins.
**Exception Scenarios**: Failed login attempts trigger password recovery via email. Browser session termination during checkout allows order resumption via session cookies.

## Business Process
**Main Process: Customer Purchase**
1.  **Trigger**: Customer accesses store URL via browser.
2.  Customer browses or searches product catalog.
3.  Customer adds selected item(s) and quantity to shopping cart.
4.  Customer proceeds to checkout.
5.  System presents order summary and prompts for payment/shipping confirmation.
6.  Customer confirms order details and payment.
7.  System processes order, stores details, and sends confirmation email.
8.  **Output**: Order confirmation with details to customer and system.

**Key Branch A: User Account Management**
1.  **Trigger**: New user selects "Register".
2.  User provides required profile and contact information.
3.  System validates and creates account.
4.  **Output**: New user account is created and user is logged in.

**Key Branch B: Product Catalog Management (Sales Personnel)**
1.  **Trigger**: Sales Personnel logs in and selects product management.
2.  Personnel adds, updates, or removes product information and inventory counts.
3.  System validates changes and updates catalog.
4.  **Output**: Updated product catalog is available for customers.

## Domain Model
*   **User** (required: UserID/unique, Password, Email/unique; reference: Role)
*   **Product** (required: ProductID/unique, Name, Price; reference: Category)
*   **Category** (required: CategoryID/unique, Name; reference: ParentCategory)
*   **ShoppingCart** (required: CartID/unique; reference: User, list of CartItem)
*   **CartItem** (required: ItemID/unique; reference: Product, ShoppingCart, Quantity)
*   **Order** (required: OrderID/unique, Status, Total; reference: User, list of OrderItem)
*   **OrderItem** (required: OrderItemID/unique; reference: Order, Product, Quantity, Price)
*   **Payment** (required: PaymentID/unique, Amount, Method; reference: Order)

## Interfaces and Integrations
*   **Customer Web Browser**: Direction: Bidirectional. Interaction: HTTPS. Input: User actions (clicks, form data). Output: Rendered web pages (product listings, cart, forms). SLA: Compatibility with IE 6/7, Netscape 4/5.
*   **Email Service**: Direction: Outbound. Interaction: SMTP. Input: Order details, recipient address. Output: Order confirmation email. SLA: Send email within 1 second.
*   **Credit Card Processor**: Direction: Outbound. Interaction: API call. Input: Card details, amount. Output: Authorization status. SLA: Validate within 2 seconds.
*   **Shipping Charge Calculator**: Direction: Outbound. Interaction: API call. Input: Destination, package details. Output: Shipping cost. SLA: Acquire charges within 2 seconds.
*   **Plug-in API**: Direction: Bidirectional. Interaction: Programmatic interface. Input: API calls from plug-in. Output: System data/events to plug-in. SLA: Documented specification for developers.
*   **USB Hardware (Yoggie)**: Direction: System dependency. Interaction: Hardware interface. Input: Power, network. Output: System operation. SLA: USB key delivers required compute/storage.

## Acceptance Criteria
*   **Account Registration**: Given a new user is on the registration page, when they submit valid details, then a new account is created and they are logged in.
*   **Product Search**: Given a customer enters search criteria, when they execute the search, then matching products are displayed in less than 1 second.
*   **Add to Cart**: Given a customer is viewing a product, when they click "Add to Cart", then the item is added to their cart in less than 2ms and the cart total updates.
*   **Checkout Process**: Given a customer with items in their cart proceeds to checkout, when they confirm payment and shipping, then an order is created and a confirmation email is sent.

## Non-functional Metrics
*   **Performance**: System must handle 1000 concurrent users; product search results in <1 second.
*   **Reliability/Availability**: System availability of 99.99%; supports periodic automated backups.
*   **Security**: All sensitive data encrypted via HTTPS; system auto-detects and blocks IP DOS attacks.
*   **Compliance**: Uses SSL for secure transactions; adheres to SQL database standard.
*   **Observability**: System creates logs of all changes and updates; can run in a debug mode.

## Milestones and Release Strategy
1.  Finalize SRS and obtain stakeholder sign-off.
2.  Complete core system development (account, catalog, cart, order modules).
3.  Integrate with external services (payment, email).
4.  Internal alpha testing on target USB hardware environment.
5.  Beta testing with a limited user group.
6.  Release of Version 1.0 on USB key.

## Risk List and Mitigation Strategies
1.  **Risk**: Transition from telephonic orders may lose business.
    **Mitigation**: Develop a phased transition plan and customer communication strategy.
2.  **Risk**: Dependency on Yoggie for stable USB hardware/OS baseline.
    **Mitigation**: Formalize agreement on baseline freeze and delivery schedule.
3.  **Risk**: Browser compatibility limited to specific versions.
    **Mitigation**: Clearly document supported browsers and test rigorously against them.
4.  **Risk**: Performance targets (e.g., 1000 concurrent users) not met.
    **Mitigation**: Conduct early load testing and performance profiling.
5.  **Risk**: Credit card fraud or security breach.
    **Mitigation**: Implement encryption, fraud validation, and monitor failed login attempts.
6.  **Risk**: Plug-in API may be unstable or poorly adopted.
    **Mitigation**: Provide comprehensive, clear documentation and sample plug-ins.
7.  **Risk**: Inventory expansion via purchased codes may have scaling issues.
    **Mitigation**: Design database and catalog structure to scale beyond 20,000 items.
8.  **Risk**: Shipping cost calculation API failures during checkout.
    **Mitigation**: Implement graceful fallback (e.g., flat rate) and async processing.

## Undecided Issues and Responsible Parties
1.  **Resolution path for telephonic order transition**. (Responsible: GAMMA-J Management)
2.  **Future module for generating tracking numbers/transportation system**. (Responsible: Product Manager)
3.  **Feasibility and scope of customer order analysis feature**. (Responsible: Product Manager)
4.  **Support and compatibility for browsers other than IE and Netscape (e.g., Firefox, Safari)**. (Responsible: Development Lead)
5.  **Detailed disaster recovery process for the optional mirror site**. (Responsible: System Architect)
6.  **Certification process and security review for third-party plug-ins**. (Responsible: Security Lead)
7.  **Pricing and licensing model for inventory expansion codes**. (Responsible: GAMMA-J Management)
8.  **Long-term support and patch delivery mechanism from Yoggie**. (Responsible: Project Manager)