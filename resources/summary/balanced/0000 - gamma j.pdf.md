# Balanced Summary: GAMMA-J Web Store

## Goals and Scope
The GAMMA-J Web Store is a plug-and-play e-commerce system designed for new online store owners, providing core sales and business management capabilities over the internet. Version 1 will be implemented on a portable USB key, featuring account management, inventory control, shopping cart functionality, and order processing. The system aims for high availability (99.999%) and includes a plug-in API for future enhancements.

## Stakeholders and User Stories
*   **System Administrator**: Manages system maintenance, user privileges, and overall system configuration.
*   **Sales Personnel**: Updates inventory, product descriptions, and manages the product line for customer purchase.
*   **Customer**: Browses products, makes purchases, and manages their account on the web store.
*   **Development Team**: Uses the SRS for guidance on system design and implementation.
*   **Test and Verification Team**: References the SRS to ensure requirements are met.
*   **Technical Writer**: Uses the SRS to assist in creating user documentation.

**User Stories:**
1.  As a **Customer**, I want to register an account so that I can store my profile and make purchases.
2.  As a **Customer**, I want to add items to a shopping cart so that I can review them before checkout.
3.  As a **Customer**, I want to confirm my order and receive an email summary so that I have a record of my purchase.
4.  As a **Sales Personnel**, I want to add, update, and remove products from the inventory so that the store catalog is accurate.
5.  As a **System Administrator**, I want to manage user accounts and privileges so that I can control system access.
6.  As a **System Administrator**, I want to install and manage plug-ins so that I can extend system functionality.

## Key Processes
1.  **Customer Registration**: Triggered by a customer clicking "Register," leading to account creation and session initiation.
2.  **Product Browsing/Search**: Triggered by customer navigation or search input, returning relevant product listings.
3.  **Shopping Cart Management**: Triggered by adding an item, allowing customers to reserve products temporarily.
4.  **Checkout & Payment**: Triggered by proceeding to checkout, involving order calculation, payment processing, and confirmation.
5.  **Order Confirmation & Notification**: Triggered by successful payment, resulting in order storage and email dispatch to the customer.
6.  **Inventory Management**: Triggered by sales personnel actions to add, update, or delete product information.
7.  **System Administration**: Triggered by administrator login, enabling user, privilege, and plug-in management.

## Domain Data Elements
*   **User Account** (Primary Key: UserID): Email, Password, Name, Address, PrivilegeLevel.
*   **Product** (Primary Key: ProductID): Name, Description, Price, Category, InventoryQuantity.
*   **Order** (Primary Key: OrderID): CustomerID, OrderDate, TotalAmount, Status, ShippingAddress.
*   **Order Item** (Composite Key: OrderID, ProductID): Quantity, UnitPrice.
*   **Shopping Cart** (Linked to User Session): SessionID, ProductID, Quantity.
*   **Category** (Primary Key: CategoryID): Name, ParentCategoryID, Description.

## Non-Functional Requirements
1.  **Performance**: System must handle 1000 concurrent users and retrieve 200 products per second.
2.  **Security**: All sensitive data must be encrypted via HTTPS, and the system must detect/block fraudulent activities.
3.  **Availability**: Target system availability is 99.99%.
4.  **Usability**: Interface must be intuitive, easy to learn, and consistent across specified web browsers.
5.  **Portability**: The core system is delivered on a portable USB key for plug-and-play deployment.
6.  **Maintainability**: System supports interchangeable plug-ins and easy updates for fixes and patches.

## Milestones and External Dependencies
1.  Delivery of USB hardware development samples from Yoggie Corporation.
2.  Freezing of the USB system baseline by Yoggie post-delivery.
3.  Compatibility testing with specified web browsers (Internet Explorer 6/7, Netscape 4/5).
4.  Integration with external payment gateway for credit card validation.
5.  Setup of email service for sending order confirmations and notifications.

## Risks and Mitigation Strategies
1.  **Risk**: Loss of business during transition from telephonic to online orders.
    *   **Mitigation**: Plan for a phased transition and parallel run of systems, with customer support and training.
2.  **Risk**: Dependence on FedEx for shipping and tracking; no integrated module in V1.
    *   **Mitigation**: Manual process for tracking number entry initially; plan plug-in or module for future version.
3.  **Risk**: Browser compatibility limited to older versions, excluding modern browsers.
    *   **Mitigation**: Clearly communicate supported environments; prioritize testing for stated browsers.
4.  **Risk**: Security vulnerabilities from external attacks (e.g., DDoS, fraud).
    *   **Mitigation**: Implement stated security measures (firewall, encryption, fraud detection, login attempt monitoring).
5.  **Risk**: System performance degradation under high load.
    *   **Mitigation**: Adhere to performance requirements during design and conduct load testing.

## Undecided Issues
1.  Detailed strategy for migrating existing telephonic order customers to the new online system.
2.  Specific implementation plan for the optional mirror site for reliability and backups.
3.  Final list and specification of initial plug-ins to be developed or provided.
4.  Resolution path for handling customer order analysis, which is currently unsupported.
5.  Detailed disaster recovery procedures beyond periodic backups.
6.  Long-term roadmap for hardware evolution beyond the USB key form factor.