**Purpose & Scope**  
Solves online store setup for new e-commerce users via a plug-and-play USB device. Manages customer accounts, inventory, shopping carts, and order confirmation. Excludes customer order analysis, advanced inventory beyond 20,000 items, and telephonic order processing.  

**Product Background / Positioning**  
New standalone e-commerce system designed for non-technical users. Operates as a self-contained USB appliance with no software installation. Not integrated with existing enterprise systems; relies on Yoggie Corporation’s hardware and OS.  

**Core Functional Overview**  
- Customer account management (creation, login, profile updates).  
- Product inventory management (add, delete, update categories/products).  
- Shopping cart functionality (add/remove items, view totals).  
- Order processing (checkout, payment, confirmation email).  
- System administration (user management, plug-in installation).  
- Plug-in API for future feature extensions.  

**Key Users & Usage Scenarios**  
- **System Admin**: Manages users, products, and plug-ins; requires login.  
- **Sales Personnel**: Updates inventory, product details, and pricing; requires login.  
- **Customers**: Browses products, adds to cart, checks out, and views order status; requires login.  

**Major External Interfaces**  
Web browser interface (limited to legacy browsers: IE 6/7, Netscape 4/5). USB hardware interface (Yoggie-provided). Email communications (order confirmations, admin alerts). Plug-in API for third-party extensions.  

**Key Non-functional Requirements**  
- Availability: 99.99%.  
- Performance: 1,000 concurrent users; <2ms shopping cart updates; <1s product search.  
- Security: SSL encryption, credit card fraud validation, IP attack blocking.  
- Reliability: 20,000-item inventory minimum; automatic backups.  

**Constraints, Assumptions & Dependencies**  
- Must deploy via USB key; no software installation.  
- Browser compatibility limited to IE 6/7 and Netscape 4/5.  
- Relies on Yoggie Corporation’s USB hardware and OS baseline.  
- No support for telephonic orders or order analysis.  

**Priorities & Acceptance Approach**  
High priority: Account management, product management, payment processing, plug-in API.  
Acceptance: Meets all performance metrics (e.g., 99.99% availability), security requirements, and core functional capabilities (e.g., order confirmation flow).