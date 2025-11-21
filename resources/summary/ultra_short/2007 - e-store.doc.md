Purpose & Scope  
The system enables online sales of electronics and home entertainment products for Marvel Electronics, supporting product configuration, purchasing, and post-purchase services. It excludes physical store operations, inventory management, and in-person customer support.  

Product Background / Positioning  
The E-Store integrates with existing CRM, payment, shipping, and tax systems to replace manual sales processes, enabling scalable online distribution and marketing for Marvel Electronics.  

Core Functional Overview  
- Online product purchase with order confirmation  
- Shopping cart for adding/removing items  
- Multiple payment method processing  
- Real-time shipment tracking  
- Personalized customer profiles with order history  
- Automated tax calculation for orders  
- Product reviews and ratings submission  

Key Users & Usage Scenarios  
Primary users are customers conducting online purchases. Customers create profiles, browse products, place orders, track shipments, and provide reviews. No role-based permissions are specified.  

Major External Interfaces  
Interfaces with CRM (support), payment systems (billPay), shipping systems, tax calculation services, and content management for product data. All use HTTP/IPv4 protocols.  

Key Non-functional Requirements  
- 99.999% internet availability via ISP contract  
- Secure data transfer using SSL for confidential transactions  
- Credit card numbers displayed only as last four digits  
- Database encryption and password masking  
- System load time ≤5 minutes under standard internet conditions  

Constraints, Assumptions & Dependencies  
Must operate via standard web browsers (IE, Mozilla). Requires VeriSign-like third-party security. Depends on external CRM, payment, shipping, and tax systems.  

Priorities & Acceptance Approach  
Critical: Core purchase flow, security, and availability. Acceptance requires successful order completion, secure transaction handling, and 99.999% uptime. Non-functional metrics must be verifiable.