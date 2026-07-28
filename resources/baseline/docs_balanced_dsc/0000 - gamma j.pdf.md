# Software Requirements Specification (SRS)
## GAMMA-J Web Store
### Version 1.0

**Document Version:** 1.0  
**Date:** [Date of Creation]  
**Status:** Draft for Review  
**Distribution:** Development Team, Test Team, Project Stakeholders

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the GAMMA-J Web Store, Version 1.0. It serves as the authoritative source for the development, testing, and verification teams, and provides a foundation for user documentation. The intended audience includes project managers, software developers, testers, system administrators, and other stakeholders.

### 1.2 Project Scope
The GAMMA-J Web Store is a plug-and-play e-commerce system designed for new online store owners. Its primary objective is to provide core sales and business management capabilities over the internet. Version 1.0 will be delivered on a portable USB key, enabling easy deployment. The system will facilitate online product sales, customer account management, inventory control, and order processing. It is architected for high availability and future extensibility via a plug-in API.

**In-Scope for Version 1.0:**
*   Customer registration, authentication, and profile management.
*   Product catalog browsing and searching.
*   Shopping cart functionality.
*   Checkout process with integration to an external payment gateway.
*   Basic inventory management for sales personnel.
*   System administration for user and privilege management.
*   Deployment and execution from a portable USB key.
*   Plug-in API framework (implementation of specific plug-ins is future work).

**Out-of-Scope for Version 1.0:**
*   Advanced customer analytics and reporting.
*   Integrated shipping carrier (e.g., FedEx) tracking module.
*   Support for web browsers other than those explicitly listed in Section 3.
*   Migration tools for legacy telephonic order systems.
*   Implementation of a mirror site for disaster recovery.

### 1.3 Definitions, Acronyms, and Abbreviations
*   **API:** Application Programming Interface
*   **DDoS:** Distributed Denial of Service
*   **HTTPS:** Hypertext Transfer Protocol Secure
*   **SRS:** Software Requirements Specification
*   **UI:** User Interface
*   **USB:** Universal Serial Bus

### 1.4 References
*   Project Charter: GAMMA-J Web Store
*   [List any other relevant documents, e.g., UI Mockups, API Contracts]

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details specific functional and non-functional requirements. Section 4 outlines external interfaces. Section 5 covers other non-functional attributes. Appendices may include data models, use case diagrams, or glossary expansions.

## 2. Overall Description

### 2.1 Product Perspective
The GAMMA-J Web Store is a self-contained, client-server web application. The server component and its runtime environment are packaged on a portable USB key. Users interact with the system via a web browser. The system interfaces with external services for payment processing and email notifications.

### 2.2 Product Functions (Summary)
1.  **User Account Management:** Registration, login, profile viewing/editing.
2.  **Product Catalog Management:** Browsing, searching, and viewing product details.
3.  **Shopping Cart Management:** Adding, updating quantities, and removing items from a cart.
4.  **Order Processing:** Calculating totals, processing payments, creating orders.
5.  **Inventory Management:** CRUD (Create, Read, Update, Delete) operations on products and categories by authorized personnel.
6.  **System Administration:** Management of user accounts, privileges, and system plug-ins.
7.  **Notification Service:** Sending order confirmation emails to customers.

### 2.3 User Characteristics
| Actor | Description | Key Skills/Assumptions |
| :--- | :--- | :--- |
| **Customer** | End-user who browses and purchases products. | Basic web browsing literacy. Has a valid email address and payment method. |
| **Sales Personnel** | Store staff responsible for maintaining the product catalog. | Granted administrative access to inventory functions. Understands product details. |
| **System Administrator** | Technical staff responsible for system health, security, and user management. | IT proficient. Understands user role-based security concepts. |
| **Development/Test Team** | Internal users of this SRS for building and verifying the system. | Expert technical knowledge. |

### 2.4 Constraints
1.  **Deployment:** Must run from a specified USB key hardware platform provided by Yoggie Corporation.
2.  **Browser Compatibility:** Must support Internet Explorer 6, Internet Explorer 7, Netscape Navigator 4, and Netscape Navigator 5.
3.  **Dependencies:** Relies on external payment gateway API and an SMTP server for email.
4.  **Performance:** Must be designed to meet concurrent user and data retrieval targets on the specified USB hardware.

### 2.5 Assumptions and Dependencies
*   The USB hardware from Yoggie Corporation will meet minimum performance specifications.
*   The store owner will have a stable internet connection to host the web store from the USB key.
*   An external payment gateway service (e.g., Authorize.net, PayPal API) will be available and integrated.
*   A functional SMTP server will be configured for sending emails.
*   The system will not be required to support real-time inventory synchronization across multiple physical locations in V1.0.

## 3. Specific Requirements

### 3.1 Functional Requirements

#### 3.1.1 User Account Management
*   **FR-UC-01: Customer Registration**
    *   **Description:** A visitor shall be able to create a new customer account.
    *   **Input:** Email address, password, full name, and shipping address.
    *   **Processing:** System shall validate email format and check for uniqueness. Password shall be stored using strong hashing (e.g., bcrypt).
    *   **Output:** New user account created with `PrivilegeLevel = "Customer"`. User is logged in and redirected to the home page.

*   **FR-UC-02: User Login**
    *   **Description:** A registered user shall be able to log in to the system.
    *   **Input:** Email address and password.
    *   **Processing:** System shall verify credentials against stored hash.
    *   **Output:** Successful login initiates a secure session. Failed attempts shall be logged and subject to security policies (see NFR-SEC-02).

*   **FR-UC-03: Profile Management**
    *   **Description:** A logged-in customer shall be able to view and edit their own profile information (name, address).
    *   **Precondition:** User is authenticated.

#### 3.1.2 Product Catalog & Browsing
*   **FR-CAT-01: Browse Product List**
    *   **Description:** A user shall be able to view a paginated list of products, optionally filtered by category.
*   **FR-CAT-02: Search Products**
    *   **Description:** A user shall be able to search for products by name or description keywords.
*   **FR-CAT-03: View Product Details**
    *   **Description:** A user shall be able to view detailed information for a single product, including name, description, price, category, and available inventory.

#### 3.1.3 Shopping Cart
*   **FR-CART-01: Add Item to Cart**
    *   **Description:** A user shall be able to add a product to their shopping cart, specifying a quantity.
    *   **Constraint:** Quantity shall not exceed `Product.InventoryQuantity`.
*   **FR-CART-02: View Cart**
    *   **Description:** A user shall be able to view the contents of their current shopping cart, including items, quantities, unit prices, and subtotal.
*   **FR-CART-03: Modify Cart**
    *   **Description:** A user shall be able to update the quantity of an item in the cart or remove an item entirely.

#### 3.1.4 Checkout and Order Processing
*   **FR-ORD-01: Initiate Checkout**
    *   **Description:** A customer shall be able to proceed from their cart to the checkout process.
    *   **Precondition:** User is logged in and cart is not empty.
*   **FR-ORD-02: Process Payment**
    *   **Description:** The system shall collect shipping address (defaults to profile) and payment information, then submit a transaction request to the external payment gateway via a secure HTTPS connection.
    *   **Input:** Credit card details (number, expiry, CVV), shipping address confirmation.
    *   **Processing:** Calculate final total (including tax if applicable). Validate payment via external gateway.
    *   **Output:** On success, create an `Order` and associated `Order Items`, reduce inventory, clear the cart, and trigger FR-NOT-01. On failure, display appropriate error message.
*   **FR-ORD-03: Order History**
    *   **Description:** A logged-in customer shall be able to view a list of their past orders and the details of each order.

#### 3.1.5 Inventory Management (Sales Personnel)
*   **FR-INV-01: Add Product**
    *   **Description:** Authorized sales personnel shall be able to add a new product to the catalog.
    *   **Input:** Product name, description, price, category, initial inventory quantity.
*   **FR-INV-02: Update Product**
    *   **Description:** Authorized sales personnel shall be able to modify the details of an existing product.
*   **FR-INV-03: Delete Product**
    *   **Description:** Authorized sales personnel shall be able to remove a product from the catalog (soft-delete or archive recommended).
    *   **Constraint:** Product cannot be deleted if it is part of any existing, non-cancelled order.

#### 3.1.6 System Administration
*   **FR-ADM-01: Manage User Accounts**
    *   **Description:** System Administrator shall be able to view, enable, disable, or delete user accounts.
*   **FR-ADM-02: Manage Privileges**
    *   **Description:** System Administrator shall be able to assign or revoke roles (e.g., "Sales Personnel", "Administrator") to/from users.
*   **FR-ADM-03: Plug-in Management**
    *   **Description:** System Administrator shall be able to view a list of installed plug-ins, install new plug-ins (via provided API-compatible package), and disable/enable existing plug-ins.

### 3.2 Non-Functional Requirements

#### 3.2.1 Performance
*   **NFR-PER-01:** The system shall support **1,000 concurrent users** with a response time of less than 3 seconds for 95% of page requests under normal load.
*   **NFR-PER-02:** Product search and listing operations shall be capable of retrieving and displaying **200 product records per second**.

#### 3.2.2 Security
*   **NFR-SEC-01:** All communication between the client browser and the server shall be encrypted using **HTTPS (TLS 1.2 or higher)**.
*   **NFR-SEC-02:** The system shall monitor login attempts and implement a temporary account lockout after **5 consecutive failed attempts** from the same IP address/username.
*   **NFR-SEC-03:** Passwords shall be stored using a strong, salted, one-way hashing algorithm.
*   **NFR-SEC-04:** The system shall implement measures to detect and block fraudulent activities (e.g., bulk card testing, anomalous purchase patterns). *[Specific logic TBD during design phase].*

#### 3.2.3 Availability & Reliability
*   **NFR-AVL-01:** The target operational availability for the core e-commerce functions (browse, cart, checkout) shall be **99.99%** (approximately 52 minutes of downtime per year).
*   **NFR-AVL-02:** The system shall perform automated daily backups of all transactional data (Orders, Users, Products) to a location external to the USB key.

#### 3.2.4 Usability
*   **NFR-USA-01:** A new customer shall be able to complete the registration process in **less than 2 minutes** without training.
*   **NFR-USA-02:** The user interface shall have a consistent layout, navigation, and terminology across all pages.
*   **NFR-USA-03:** The system shall be fully operable and render correctly on the following browsers: **Internet Explorer 6, Internet Explorer 7, Netscape Navigator 4, Netscape Navigator 5.**

#### 3.2.5 Portability & Maintainability
*   **NFR-PRT-01:** The entire system (application server, database, runtime) shall be packaged to run from a **portable USB key** without requiring installation on the host machine's primary storage.
*   **NFR-MNT-01:** The system shall expose a well-documented **Plug-in API** to allow for the development and integration of additional functional modules without modifying the core system code.
*   **NFR-MNT-02:** The system shall provide a mechanism for applying software patches and updates to the core application.

## 4. External Interface Requirements

### 4.1 User Interfaces
The primary UI is a web interface. Wireframes/mockups are referenced separately. Key interface elements include:
*   Public-facing: Home page, Product List/Detail pages, Shopping Cart, Checkout pages, Login/Registration pages.
*   Admin-facing: Dashboard, User Management, Product Management, Plug-in Management consoles.

### 4.2 Hardware Interfaces
*   **USB Key:** The system must interface with the Yoggie-provided USB hardware to host the web server and database. The application must be optimized for the I/O and processing constraints of this medium.

### 4.3 Software Interfaces
*   **Payment Gateway:** Interface via HTTPS POST/GET requests using the gateway's specified API (e.g., REST, SOAP) for authorizing and capturing payments.
*   **Email Service (SMTP):** Interface with an SMTP server to send transactional emails (order confirmations). Configuration (server, port, credentials) shall be manageable by the System Administrator.

### 4.4 Communications Interfaces
*   **HTTP/HTTPS:** Primary protocol for web communication (Ports 80/443).
*   **SMTP:** For outgoing email (typically Port 25, 465, or 587).

## 5. Other Non-Functional Requirements

### 5.1 Business Rules
*   **BR-01:** Product price is defined at the `Product` level and is immutable for a given order once the order is placed.
*   **BR-02:** An order can have the following statuses: `Pending Payment`, `Processing`, `Shipped`, `Cancelled`, `Completed`.
*   **BR-03:** A user's `PrivilegeLevel` determines access to administrative functions (`Customer`, `Sales`, `Administrator`).

### 5.2 Data Requirements & Domain Model
The core data entities and their key attributes are defined below. This logical model shall guide physical database design.

```sql
-- Simplified Logical Data Model
Entity User {
    UserID (PK): Integer
    Email: String, Unique
    PasswordHash: String
    FullName: String
    Address: Text
    PrivilegeLevel: Enum('Customer', 'Sales', 'Administrator')
}

Entity Product {
    ProductID (PK): Integer
    Name: String
    Description: Text
    Price: Decimal
    CategoryID (FK): Integer
    InventoryQuantity: Integer
    IsActive: Boolean
}

Entity Category {
    CategoryID (PK): Integer
    Name: String
    ParentCategoryID (FK): Integer, Nullable
    Description: Text
}

Entity Order {
    OrderID (PK): Integer
    CustomerID (FK): Integer
    OrderDate: DateTime
    TotalAmount: Decimal
    Status: Enum('Pending Payment', 'Processing', 'Shipped', 'Cancelled', 'Completed')
    ShippingAddress: Text
}

Entity OrderItem {
    OrderID (PK, FK): Integer
    ProductID (PK, FK): Integer
    Quantity: Integer
    UnitPriceAtTimeOfOrder: Decimal
}

Entity ShoppingCart {
    SessionID: String
    ProductID (FK): Integer
    Quantity: Integer
    AddedDate: DateTime
}
```

## Appendix A: Open Issues / TBD
1.  **Customer Migration Strategy:** Detailed plan for migrating existing telephonic customers (data import, communication, incentive) is pending.
2.  **Mirror Site Implementation:** The feasibility and design for an optional mirror site for enhanced reliability are deferred.
3.  **Initial Plug-in Specifications:** The final list, scope, and design of the first-party plug-ins to be developed post-V1.0 are not defined.
4.  **Disaster Recovery Plan:** Detailed procedures for system restoration beyond daily backups are required as a separate operational document.
5.  **Future Hardware Roadmap:** Evolution path for the hardware form factor beyond the USB key is a strategic business decision.

## Appendix B: Risk Log (Summary)
| Risk | Probability | Impact | Mitigation Strategy (from SRS) |
| :--- | :--- | :--- | :--- |
| Business loss during transition | Medium | High | Phased transition with parallel system run. |
| Dependence on manual shipping tracking | High | Medium | Manual entry process in V1; plan automated plug-in for future. |
| Browser compatibility limitations | High | Medium | Explicitly define and test against supported browser list. |
| Security vulnerabilities | Medium | High | Implement HTTPS, fraud detection, login monitoring, and regular security reviews. |
| Performance under load | Medium | High | Design to performance targets; conduct rigorous load testing on target USB hardware. |

---
*This document is considered the baseline for the GAMMA-J Web Store Version 1.0 project upon sign-off by the authorized stakeholders.*