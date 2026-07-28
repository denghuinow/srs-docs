# Software Requirements Specification (SRS)
## WebStore-in-a-USB Plug-and-Play E-commerce System

**Document Version:** 1.0
**Date:** October 26, 2023
**Status:** Approved for Development

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the "WebStore-in-a-USB" system. This document is intended to be used by the project development team, quality assurance team, project managers, and stakeholders to ensure a common understanding of the system to be developed. The primary purpose is to provide a complete, web-based e-commerce solution that operates entirely from a dedicated USB hardware device, enabling new online retailers to deploy a fully functional store with minimal technical expertise.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Keywords:** The terms `MUST`, `SHALL`, `WILL`, `SHOULD`, `MAY`, and `MUST NOT` are used as defined in IETF RFC 2119.
*   **Priority:** (H) High, (M) Medium, (L) Low.

#### 1.3 Project Scope
The "WebStore-in-a-USB" system is a self-contained, plug-and-play e-commerce platform. The scope includes:
*   A web server, application logic, and SQL database running on a specified USB hardware device.
*   A public-facing website for customer browsing, account management, and purchasing.
*   An administrative interface for the retailer to manage products, inventory, and orders.
*   Core e-commerce functions: customer accounts, product catalog, shopping cart, and order processing.

**Out of Scope:**
*   Payment gateway integration (assumed to be handled by a third-party service redirected from the order page).
*   Advanced marketing tools (e.g., email campaigns, loyalty programs).
*   Custom web design or theme development services.
*   Physical shipping carrier integration or label printing.

#### 1.4 References
*   Project Charter: "WebStore-in-a-USB" – Initial Proposal
*   Hardware Specification: Yoggie USB System Datasheet
*   IETF RFC 2119: Key words for use in RFCs to Indicate Requirement Levels

### 2. Overall Description

#### 2.1 Product Perspective
The system is a standalone, embedded product. It connects to a host machine (retailer's computer) via USB but operates independently on its own specified hardware and Linux-based OS stack. The host machine only provides network access and power via the USB connection. The system presents two primary web interfaces: one for customers and one for the store administrator.

#### 2.2 Product Functions
The high-level functions of the system are:
1.  **Storefront Presentation:** Display product information, categories, and prices to customers.
2.  **Customer Self-Service:** Allow customers to create accounts, manage their profiles, and view order history.
3.  **Shopping Cart Management:** Enable customers to add, update, and remove items from a persistent cart.
4.  **Checkout Process:** Guide customers through a structured checkout flow culminating in order submission.
5.  **Inventory Management:** Allow the administrator to add, edit, deactivate, and categorize products, and track stock levels.
6.  **Order Management:** Allow the administrator to view, process, and update the status of customer orders.
7.  **System Administration:** Provide basic controls for the store administrator (e.g., store name, contact information).

#### 2.3 User Classes and Characteristics
*   **Customer:** An end-user browsing and purchasing products. May be a guest or a registered account holder. Assumed to have basic web browsing competency.
*   **Store Administrator (Retailer):** The primary user of the system. Manages all aspects of the store. Assumed to have minimal technical server administration skills but can follow web-based instructions.
*   **System Administrator (Implied):** Responsible for the initial plug-and-play setup of the USB device. Interaction with the system is limited to hardware connection and basic network configuration.

#### 2.4 Operating Environment
*   **Hardware:** The application MUST operate exclusively on the specified Intel-based Linux hardware provided within the Yoggie USB system form factor.
*   **Software Runtime:** A LAMP (Linux, Apache, MySQL, PHP) or equivalent stack (e.g., Linux, Nginx, MySQL, Python) pre-installed on the USB device's internal storage.
*   **Client Browsers:** The web interface MUST be compatible **only** with the following browser versions:
    *   Microsoft Internet Explorer 6.0 & 7.0
    *   Netscape Navigator 4.0 & 5.0
*   **Network:** The device must obtain a local IP address via DHCP from the host network. The host network must allow HTTP (port 80) traffic to the device.

#### 2.5 Design and Implementation Constraints
1.  `NFR-CON-001` (H): The entire software system MUST reside and execute from the read-only and/or persistent storage of the specified Yoggie USB hardware device.
2.  `NFR-CON-002` (H): The system MUST use an SQL-based relational database (MySQL/MariaDB) for all persistent data storage.
3.  `NFR-CON-003` (H): All front-end HTML, CSS, and JavaScript MUST be developed to ensure functional compatibility with IE 6/7 and Netscape 4/5 as specified in section 2.4.
4.  `NFR-CON-004` (M): The system must be designed for low disk I/O and memory footprint due to the constraints of the USB hardware environment.

#### 2.6 Assumptions and Dependencies
*   The retailer has a Windows or Linux computer with a USB port and a network connection.
*   The retailer's network firewall allows inbound HTTP connections to the USB device's IP address.
*   The retailer will handle domain name registration and DNS configuration separately if a custom domain is desired; otherwise, the store is accessed via the device's IP address.
*   The SQL database server is bundled and configured within the USB device's software stack.

### 3. System Features and Requirements

#### 3.1 Customer Account Management
**Description:** This feature allows users to create personal accounts and manage their profile information.

**Functional Requirements:**
*   `FR-ACC-001` (H): The system SHALL allow a visitor to register for a new customer account by providing a unique email address, password, and basic personal information (name, shipping address).
*   `FR-ACC-002` (H): The system SHALL allow a registered customer to authenticate (log in) using their email address and password.
*   `FR-ACC-003` (M): The system SHALL allow an authenticated customer to view and update their personal profile information (e.g., password, shipping address, phone number).
*   `FR-ACC-004` (M): The system SHALL associate a customer's shopping cart contents with their account, persisting the cart between sessions.
*   `FR-ACC-005` (L): The system SHALL provide a "Forgot Password" function to reset credentials via email.

#### 3.2 Product Inventory Management
**Description:** This feature allows the Store Administrator to manage the product catalog and inventory levels.

**Functional Requirements:**
*   `FR-INV-001` (H): The system SHALL allow the Administrator to add new products, specifying name, description, price, SKU, category, and initial stock quantity.
*   `FR-INV-002` (H): The system SHALL allow the Administrator to edit or deactivate existing products.
*   `FR-INV-003` (H): The system SHALL automatically decrement product stock levels when an order is confirmed and prevent the sale of out-of-stock items.
*   `FR-INV-004` (M): The system SHALL allow the Administrator to organize products into hierarchical categories and subcategories.
*   `FR-INV-005` (M): The system SHALL provide a basic search and filter interface for the Administrator to view the product list.

#### 3.3 Shopping Cart and Order Processing
**Description:** This feature allows customers to select products and complete purchases, and allows the Administrator to manage the resulting orders.

**Functional Requirements:**
*   `FR-ORD-001` (H): The system SHALL allow a customer (guest or registered) to add products to a shopping cart, specifying quantity.
*   `FR-ORD-002` (H): The system SHALL allow a customer to view their cart, modify item quantities, and remove items.
*   `FR-ORD-003` (H): The system SHALL guide a customer through a checkout process: reviewing cart, confirming shipping address, and viewing a final order total.
*   `FR-ORD-004` (H): The system SHALL generate a unique, persistent order number and record the final order details (items, prices, customer info, timestamp) upon customer confirmation.
*   `FR-ORD-005` (H): The system SHALL provide an order management interface for the Administrator to view a list of all orders, filter by status, and view order details.
*   `FR-ORD-006` (M): The system SHALL allow the Administrator to update the status of an order (e.g., "Processing," "Shipped," "Cancelled").

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Customer Storefront:** A clean, template-based HTML interface for browsing products, viewing cart, and managing accounts. Must comply with browser constraints in 2.4.
*   **Administrator Panel:** A password-protected web interface with a menu-driven navigation for managing products, categories, and orders. Must comply with browser constraints in 2.4.

#### 4.2 Hardware Interfaces
*   **USB Connection:** The device interfaces with the host computer solely via a USB 2.0 (or higher) port for power and network bridging. The application software has no direct interface with the host OS.

#### 4.3 Software Interfaces
*   **SQL Database:** The application SHALL interface with a MySQL (or compatible) database using standard SQL queries via a persistent connection (e.g., PDO, mysqli).
*   **Web Server:** The application SHALL run as a server-side script (e.g., PHP, Python) within the Apache or Nginx web server environment on the device.

#### 4.4 Communications Interfaces
*   **HTTP/HTTPS:** The system SHALL communicate with client browsers using the HTTP/1.1 protocol. HTTPS is recommended but not mandated in the initial scope.
*   **SMTP (Outbound):** The system SHALL be capable of connecting to an external SMTP server (configured by the Administrator) to send transactional emails (e.g., registration confirmations, order confirmations).

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-PER-001`: The storefront homepage SHALL load in under 3 seconds on a local area network (LAN) connection when tested with IE 7.
*   `NFR-PER-002`: The system SHALL support a minimum of 10 concurrent user sessions without significant degradation in response time.

#### 5.2 Safety Requirements
*   Not applicable for this software system.

#### 5.3 Security Requirements
*   `NFR-SEC-001` (H): All administrator access SHALL require authentication.
*   `NFR-SEC-002` (H): Customer passwords SHALL be stored in the database using a strong, irreversible hashing algorithm (e.g., bcrypt).
*   `NFR-SEC-003` (M): The system SHALL be resilient to common web attacks (e.g., SQL Injection, Cross-Site Scripting) through parameterized queries and output encoding.

#### 5.4 Software Quality Attributes
*   **Usability:** The Administrator interface SHOULD be usable by a non-technical person with less than one hour of training.
*   **Reliability:** The system SHOULD achieve 99% uptime during operating hours, excluding network outages outside the USB device.
*   **Portability:** The software is NOT portable. It is tightly constrained to the hardware and software stack specified in sections 2.4 and 2.5.
*   **Maintainability:** The source code SHALL be modular and include inline comments to facilitate future updates by the development team.

---
**Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| QA Manager | | | |