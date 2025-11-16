# GAMMA-J Web Store - Software Requirements Specification

## System Overview
The GAMMA-J Web Store is a software solution designed for new online store owners to quickly and easily set up and operate an e-commerce business over the internet. The system is planned for implementation on a "plug and play" USB Key, with future versions based on other network appliances. The initial inventory capacity is 100 items, expandable to a minimum of 20,000 items with unique codes.

## Core Functional Features

### Customer Accounts (High Priority)
- Customer registration and account creation
- Login/logout functionality
- Profile management with contact information and purchase history
- Order confirmation and tracking
- Secure storage of payment information (credit card details)
- SSL encryption for account security

### Product Management (High Priority)
- Multi-tiered product categorization system
- Sales personnel ability to add, delete, and update product descriptions
- Product information management including pictures, prices, and availability
- Inventory management with unique product codes

### Shopping Cart (Medium Priority)
- Temporary storage for customer-selected items
- Real-time display of item count and total cost
- Ability to add or remove products before checkout
- Session-based cart persistence

### Purchasing and Payment (High Priority)
- Order review and confirmation process
- Secure payment processing
- Credit card validation and fraud detection
- Order confirmation email generation
- Integration with shipping systems

### Search Engine (Medium Priority)
- Product search functionality with multiple criteria
- Category-based browsing
- Search result filtering and sorting

### Plug-in API (High Priority)
- Application programming interface for custom plug-in development
- Extensibility framework for future enhancements
- Well-documented API specifications for developers

## User Classes

### System Administrator
- System maintenance and configuration
- User privilege management
- Account administration
- Plug-in installation and management
- System patching and updates

### Sales Personnel
- Product inventory management
- Product information updates
- Category management
- Inventory level monitoring

### Customer
- Account registration and management
- Product browsing and searching
- Shopping cart operations
- Order placement and payment
- Order status tracking

## Technical Requirements

### Operating Environment
- Compatible with Microsoft Internet Explorer versions 6 and 7
- Compatible with Netscape Communicator versions 4 and 5
- Intel-based system with Slackware Linux 2.6 and Apache Web Server
- SQL-based database for inventory storage
- USB interface provided by Yoggie Corporation

### Security Requirements
- Secure Socket Layer (SSL) encryption for all communications
- Credit card validation and fraud detection
- Database encryption for sensitive customer data
- Automatic IP-based DoS attack detection and blocking
- Consecutive failed login attempt detection
- Firestarter open-source firewall protection

### Performance Requirements
- System deployment and operation in less than 1 minute after USB connection
- Support for 1000 concurrent logged-in customers
- Product retrieval rate of 200 products per second
- Shopping cart addition in less than 2ms
- Product search completion in less than 1 second
- Email transmission in less than 1 second
- Credit card validation in less than 2 seconds
- Shipping charge acquisition in less than 2 seconds
- Data restoration rate of 1000 records per second

### Availability Requirements
- System availability of 99.99%
- Optional mirror site for reliability and backups
- Periodic automated backups via internet connection

### Usability Requirements
- Intuitive web-based interface compatible with major browsers
- Unambiguous navigation and product browsing
- Context-sensitive help system
- Easy-to-locate buttons and controls
- Clear error messages
- Consistent symbols and colors for notifications

### Portability Requirements
- High portability via USB drive implementation
- Easy migration and backup via additional USB drives

### Maintainability Requirements
- Interchangeable plug-in architecture
- Easy update mechanisms for fixes and patches
- Comprehensive change logging
- Simple upgrade procedures

## Interface Requirements

### User Interfaces
- Login screens for customers and administrators
- Product management screens for system administrators
- Customer account screens
- Shopping cart interface
- Order summary and confirmation screens
- System administration maintenance screens

### Hardware Interfaces
- USB key hardware from Yoggie Corporation

### Software Interfaces
- WebOrder browser interface
- Programmatic interfaces for billing operations
- Inventory management system communication
- Plug-in interface system

### Communications Interfaces
- Email confirmation system for customers with tracking numbers
- Technical query notifications to system administrators

## Quality Attributes

### Performance Efficiency
- Dijkstra's shortest path algorithm for searches
- On-demand asynchronous page loading
- Image compression for large files
- Email address validation

### Reliability
- High availability (99.99%)
- Backup and recovery mechanisms
- Error detection and handling

### Security
- End-to-end encryption
- Access control and authentication
- Intrusion detection and prevention

### Maintainability
- Modular design with plug-in architecture
- Comprehensive logging and monitoring
- Easy update and patch management

### Portability
- Platform independence via USB deployment
- Standard web browser compatibility

## System Constraints
- Must use SQL-based database
- Limited browser compatibility (IE 6/7, Netscape 4/5)
- Hardware requirements: 4GB Flash RAM, 128MB SDRAM, Intel XScale PXA270 520-MHz chipset
- OS: Apache web server
- Database: MySQL

## Future Considerations
- Transition support for telephone orders to online system
- Integration with transportation and tracking systems
- Customer order analysis capabilities
