# Balanced Summary

**Goals and scope**
GAMMA-J Web Store is a plug-and-play USB-based e-commerce system designed for new online store owners to quickly set up and manage sales. It provides core functionality for customer accounts, inventory management, and shopping cart operations while supporting future enhancements via plug-ins. The system targets small businesses with initial inventory capacity of 100 items, expandable to 20,000 items.

**Roles and user stories**
- As a Customer, I want to register and manage my account so that I can store my profile and purchase history
- As a Customer, I want to add items to a shopping cart so that I can reserve products for purchase
- As a Customer, I want to checkout and confirm orders so that I can complete my purchases
- As a Sales Person, I want to manage product inventory so that I can keep product information current
- As a System Administrator, I want to manage user accounts and privileges so that I can control system access
- As a System Administrator, I want to install plug-ins so that I can extend system functionality

**Key processes**
1. Customer registration (triggered by customer clicking "Register")
2. User login (triggered by clicking "Login")
3. Product search and browsing (triggered by customer navigation)
4. Shopping cart management (triggered by adding/removing items)
5. Order checkout and confirmation (triggered by clicking "Checkout")
6. Inventory updates (triggered by sales personnel actions)
7. System administration (triggered by administrator requests)

**Domain data elements**
- User (User ID, Password, Email, Privileges, Address)
- Product (Product ID, Name, Description, Price, Inventory Quantity)
- Order (Order Number, Order Date, Total Amount, Status, Tracking Number)
- Shopping Cart (Session ID, Product ID, Quantity, Added Date)
- Category (Category ID, Name, Parent Category, Description)
- Payment (Credit Card Number, Expiry Date, Billing Address)

**Non-functional requirements**
- 99.99% system availability requirement
- Support for 1000 concurrent users
- Response time under 1 second for product searches
- SSL encryption for all sensitive data
- Compatibility with major web browsers
- Plug-and-play deployment via USB key

**Milestones and external dependencies**
- Delivery of USB system samples from Yoggie Corporation
- Freeze of USB system baseline by Yoggie
- Integration with FedEx for shipping and tracking
- Support for future plug-in development
- Transition from telephonic to online ordering system

**Risks and mitigation strategies**
- Browser compatibility issues (mitigated by testing specified versions)
- USB hardware dependencies (mitigated by coordination with Yoggie)
- Order transition from telephone to online (mitigated by phased implementation)
- Shipping system limitations (mitigated by FedEx integration)
- Customer adoption challenges (mitigated by user-friendly interface design)

**Undecided issues**
- Customer order analysis capabilities
- Internal transportation system module
- Complete transition strategy from telephonic orders
- Enhanced tracking number generation
- Competitor response to business transition
- Long-term plug-in ecosystem development