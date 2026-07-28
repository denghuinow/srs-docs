# Short Summary: GAMMA-J Web Store

## Background and objectives
The GAMMA-J Web Store is a plug-and-play USB-based e-commerce system designed to enable new online store owners to quickly set up and manage sales. Its primary objective is to provide a self-contained, easy-to-deploy solution with core online retail functionalities, expandable via plug-ins.

## In scope
- Customer account management (registration, login, profile editing).
- Inventory management with multi-tiered product categorization.
- Shopping cart functionality for item selection and modification.
- Order confirmation with email notifications and payment processing.
- A plug-in API for future custom enhancements.

## Out of scope
- Telephonic order integration and transition handling.
- Built-in transportation/tracking number generation (relies on external services like FedEx).
- Customer order analysis and reporting features.
- Support for web browsers other than specified versions of Internet Explorer and Netscape.
- Direct responsibility for the underlying Yoggie-provided USB hardware and operating system.

## Stakeholders and core use cases
**Stakeholders:**
- **System Administrator:** Manages system maintenance, user privileges, and plug-ins.
- **Sales Personnel:** Updates inventory, product descriptions, prices, and availability.
- **Customer:** Browses products, makes purchases, and manages their account.
- **Development Team:** Implements and designs the system based on requirements.
- **Test and Verification Team:** Ensures requirements are met through testing.
- **Tech Writer:** Creates user documentation and manuals.

**Core use cases:**
1. As a customer, I want to register an account so that I can make purchases and save my information.
2. As a customer, I want to add items to a shopping cart so that I can review them before checkout.
3. As a salesperson, I want to update product attributes so that inventory details are accurate.
4. As a system administrator, I want to install plug-ins so that I can extend system functionality.
5. As a customer, I want to confirm an order so that I receive a confirmation email with details.
6. As a system administrator, I want to manage user accounts so that I can control access and privileges.

## Success metrics
- System deploys and becomes operational in less than 1 minute after USB plug-in.
- Handles 1000 concurrent customer logins without performance degradation.
- Achieves 99.99% system availability for uninterrupted store operations.

## Major constraints
- Must use an SQL-based database for data storage and compatibility.
- Only verified for compatibility with Microsoft Internet Explorer versions 6/7 and Netscape Communicator versions 4/5.
- Operates on a specific Yoggie-provided USB hardware with Slackware Linux 2.6 and Apache.
- Initial inventory supports a minimum of 20,000 items, expandable via unique codes.
- All sensitive data must be encrypted via HTTPS and in the database.

## Undecided issues
- Strategy for transitioning telephonic orders to the online system without business loss.
- Future development of an internal module for tracking number generation and transportation.
- Implementation of customer order analysis capabilities.
- Full compatibility assurance with browsers like Mozilla or Firefox.
- Long-term coordination with Yoggie on hardware enhancements and features.