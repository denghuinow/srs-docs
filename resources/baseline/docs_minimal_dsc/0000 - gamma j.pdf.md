# Software Requirements Specification (SRS)
## Portable Web Store System

**Document Version:** 1.0  
**Date:** [Current Date]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the **Portable Web Store System**. This system is a self-contained, plug-and-play e-commerce solution designed to operate entirely from a provided USB key. The primary purpose is to enable rapid deployment of a fully-featured online store for sales, with integrated customer, inventory, and order management. This document is intended for use by the project stakeholders, development team, quality assurance team, and project management.

#### 1.2 Scope
The scope of this project is the development of a portable web store application that includes:
*   A complete web-based storefront for customer product browsing and purchasing.
*   Backend administrative interfaces for system, inventory, and sales management.
*   A self-contained runtime environment on a specified USB key hardware device.
*   Core e-commerce functionality including user accounts, shopping cart, checkout, and order confirmation.
*   A documented API to allow for future functional extensions via plug-ins.

**Out of Scope:**
*   Development of physical USB key hardware.
*   Integration with third-party payment gateways (initial version will simulate/record payment).
*   Advanced reporting and business intelligence analytics.
*   Multi-language or multi-currency support.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **SRS:** Software Requirements Specification
*   **API:** Application Programming Interface
*   **SQL:** Structured Query Language
*   **UI:** User Interface
*   **HTTP:** Hypertext Transfer Protocol
*   **SSL:** Secure Sockets Layer (implied for security, though not explicitly stated in constraints)
*   **Inventory Item:** A unique product or service offered for sale in the system.

#### 1.4 References
*   Project Charter – Portable Web Store, Version 1.0
*   Yoggie Corporation USB Key Hardware Specifications, Document #HW-USB-2.0

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its users, and constraints. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements including performance, security, and technical constraints.

---

### 2. Overall Description

#### 2.1 Product Perspective
The Portable Web Store System is a standalone, encapsulated web application. It is not a module of a larger system but operates independently. It interfaces with:
*   **Users:** Via a web browser over HTTP/HTTPS.
*   **Persistent Storage:** Via an integrated SQL database running on the same USB key.
*   **Host Environment:** The Yoggie USB key hardware, which provides the processing, memory, and web server (Apache) environment.

#### 2.2 Product Functions
The high-level functions of the system are:
1.  **Customer Account Management:** Secure creation, authentication, and profile management for end customers.
2.  **Product Inventory Management:** Full CRUD (Create, Read, Update, Delete) operations on products, including categorization.
3.  **Shopping & Order Processing:** Management of a session-based shopping cart, a checkout process, payment handling, and order confirmation generation.
4.  **Product Discovery:** A public-facing web interface allowing customers to browse, search, and view product details.
5.  **Extensibility:** Provision of a stable, documented API for developing plug-ins to add new features.

#### 2.3 User Characteristics
| User Class | Description | Technical Proficiency | Key Goals |
| :--- | :--- | :--- | :--- |
| **System Administrator** | Responsible for initial deployment, user management, system monitoring, and backup. | High. Familiar with web servers and basic Linux administration. | Ensure system availability, manage user access, perform maintenance. |
| **Sales Personnel** | Manages the product catalog, views orders, and handles basic customer inquiries. | Medium. Comfortable with web-based administrative interfaces. | Accurately maintain product information and pricing; process orders. |
| **Customer** | Browses and purchases products from the store. | Variable. Assumed to be competent with basic web browsing. | Find desired products easily, complete purchases securely and efficiently. |

#### 2.4 Constraints
1.  **Browser Compatibility:** The web interface must be fully functional on:
    *   Microsoft Internet Explorer versions 6 and 7.
    *   Netscape Communicator versions 4 and 5.
2.  **Database:** The system must utilize an SQL-based relational database (e.g., SQLite, MySQL) for all persistent data storage.
3.  **Operating Environment:** The software stack must run on the specific provided environment:
    *   **OS:** Slackware Linux, Kernel 2.6.
    *   **Web Server:** Apache.
    *   **Hardware:** Specified Intel-based system using the provided Yoggie Corporation USB key.
4.  **Portability:** The entire application, including runtime, database, and web server configuration, must be contained and operable from the USB key without requiring installation on the host machine.

#### 2.5 Assumptions and Dependencies
*   The provided Yoggie USB key meets all minimum hardware requirements (CPU, RAM, storage).
*   The host machine (Intel-based system) can boot from or execute programs from the USB key.
*   Network connectivity (TCP/IP) is available for client browsers to access the web server on the USB key.
*   Initial system setup and network configuration on the USB key environment will be performed by a qualified system administrator.

---

### 3. Specific Requirements

#### 3.1 External Interface Requirements
**3.1.1 User Interfaces**
*   The storefront shall have a clean, professional design compatible with the browsers listed in Section 2.4.
*   The administrative interface shall be separate from the storefront, requiring authentication.
*   All forms shall provide clear validation messages.

**3.1.2 Hardware Interfaces**
*   The application shall interact solely with the hardware resources provided by the Yoggie USB key (storage, processor, memory, network interface).

**3.1.3 Software Interfaces**
*   **Database:** The application shall interface with an SQL database via standard SQL queries or an ORM layer.
*   **Web Server:** The application shall be developed in a language (e.g., PHP, Python) compatible with Apache on Slackware Linux 2.6.
*   **Plug-in API:** The system shall expose a documented, versioned HTTP or internal function-based API for plug-in development.

**3.1.4 Communications Interfaces**
*   The system shall communicate with client browsers via HTTP (port 80) and optionally HTTPS (port 443).
*   All sensitive data transmission (e.g., login, checkout) should use HTTPS (implied security best practice).

#### 3.2 Functional Requirements
**3.2.1 Customer Account Management (FR-UC)**
*   **FR-UC-01:** The system shall allow a new visitor to create a customer account by providing a unique email, password, and basic personal information.
*   **FR-UC-02:** The system shall authenticate registered customers via email and password.
*   **FR-UC-03:** The system shall allow an authenticated customer to view and update their profile (shipping address, contact info).
*   **FR-UC-04:** The system shall maintain a secure, hashed storage of customer passwords.

**3.2.2 Product Inventory Management (FR-INV)**
*   **FR-INV-01:** Authorized Sales Personnel shall be able to add new products to the inventory, specifying name, description, category, price, and initial stock quantity.
*   **FR-INV-02:** The system shall support a hierarchical product categorization (e.g., Electronics > Computers > Laptops).
*   **FR-INV-03:** Sales Personnel shall be able to modify product details or delete discontinued products.
*   **FR-INV-04:** The system shall track stock levels, decrementing upon successful order completion.
*   **FR-INV-05:** The inventory database shall be designed to hold a minimum of 100 items and be scalable to hold at least 20,000 items without structural changes.

**3.2.3 Shopping & Order Processing (FR-ORD)**
*   **FR-ORD-01:** The system shall provide a persistent shopping cart for both guests and logged-in customers.
*   **FR-ORD-02:** A customer shall be able to add/remove items and change quantities in their cart.
*   **FR-ORD-03:** The system shall guide the customer through a checkout process (review cart, enter shipping/billing, confirm order).
*   **FR-ORD-04:** The system shall generate a unique order confirmation number and display/email a summary upon checkout completion.
*   **FR-ORD-05:** The system shall record all order details (items, prices, customer, timestamp) permanently.

**3.2.4 Product Discovery (FR-BRW)**
*   **FR-BRW-01:** The public storefront shall display products organized by category.
*   **FR-BRW-02:** Customers shall be able to search for products by name or description keywords.
*   **FR-BRW-03:** Customers shall be able to view a detailed page for each product, showing all relevant information and an "Add to Cart" option.

**3.2.5 Administrative Functions (FR-ADMIN)**
*   **FR-ADMIN-01:** The System Administrator shall be able to create, disable, and delete accounts for Sales Personnel.
*   **FR-ADMIN-02:** Sales Personnel shall have a dashboard to view recent orders and basic sales metrics.
*   **FR-ADMIN-03:** The system shall provide a log of administrative actions.

**3.2.6 Extensibility (FR-API)**
*   **FR-API-01:** The system shall provide a documented API that allows third-party plug-ins to add new payment methods, shipping calculators, or UI widgets.
*   **FR-API-02:** The plug-in architecture shall not require modification of the core system code.

#### 3.3 Non-Functional Requirements

**3.3.1 Performance Requirements**
*   The storefront homepage shall load in under 3 seconds on the specified hardware with a database of 1000 products.
*   Product search queries shall return results in under 2 seconds.
*   The system shall support a minimum of 10 concurrent user sessions without significant degradation.

**3.3.2 Safety & Security Requirements**
*   All user passwords shall be hashed using a strong, salted algorithm (e.g., bcrypt).
*   Administrative and user login sessions shall timeout after a period of inactivity (e.g., 30 minutes).
*   The system shall be resistant to common web vulnerabilities (e.g., SQL Injection, Cross-Site Scripting).
*   Customer data shall be stored securely on the encrypted volume of the USB key (implied by hardware spec).

**3.3.3 Technical Requirements**
*   As defined in **Section 2.4 Constraints**.

**3.3.4 Data Requirements**
*   The initial database schema shall support 100 inventory items.
*   The schema design shall be normalized to efficiently support scaling to 20,000 items.
*   Regular automated backups of the database shall be configurable by the System Administrator.

**3.3.5 Portability Requirement**
*   The entire software package must be capable of being transferred to a new, identical Yoggie USB key and function without code modification.

---
**End of Document**