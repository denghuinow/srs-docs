# Balanced Summary

## Goals and Scope
This SRS defines requirements for a web-based Supply Chain Management (SCM) system for Ejada company. The system aims to manage procurement, manufacturing flow, and customer relationships while coordinating between customers, suppliers, and coordinators. The scope is limited to Ejada's specific requirements and will integrate with other modules in their .NET framework.

## Roles and User Stories
- **Coordinator**: I want to manage customer requests so that I can efficiently process and forward them to suppliers
- **Coordinator**: I want to manage supplier information so that I can maintain accurate partner records
- **Customer**: I want to submit and track requests so that I can receive timely products and services
- **Supplier**: I want to view pending requests so that I can provide timely feedback on supply availability
- **Supplier**: I want to edit my profile information so that my contact details remain current

## Key Processes
1. **Trigger: User login** → System authenticates and directs to role-specific dashboard
2. **Trigger: Customer creates request** → System records request and notifies coordinator
3. **Trigger: Coordinator processes request** → System forwards request to appropriate suppliers
4. **Trigger: Supplier reviews request** → System enables feedback submission
5. **Trigger: Coordinator manages items** → System maintains product catalog and inventory
6. **Trigger: User edits profile** → System updates user information in database
7. **Trigger: Coordinator manages resources** → System tracks storage locations and availability

## Domain Data Elements
- **Customer**: CustomerID (PK), Name, Address, ContactPerson, Email
- **Supplier**: SupplierID (PK), Name, Address, ContactPerson, Email
- **Request**: RequestID (PK), Description, Status, CustomerID, SupplierID
- **Item**: ItemID (PK), Name, Description, Category, Price
- **Resource Location**: LocationID (PK), Name, Address, Capacity, Type
- **Coordinator**: CoordinatorID (PK), Username, Password, Domain

## Non-functional Requirements
- Support 100 concurrent users with 90% of transactions completing in <1 second
- Maintain 100% system availability with understandable error feedback
- Implement role-based authentication for secure access
- Use ASP.NET, C#, and MS SQL with .NET Framework 3.5
- Daily automated data backup with manual backup capability
- Operate on Microsoft OS with IIS and latest .NET framework

## Milestones and External Dependencies
- Release 1.0 delivery including all specified requirements
- Integration with Ejada's existing .NET framework
- Dependence on Microsoft SQL Server database
- Compatibility with Internet Explorer and Firefox browsers
- Future integration with CRM and HR systems

## Risks and Mitigation Strategies
- **Login failures**: Implement robust authentication with clear error messages
- **Supplier unavailability**: Provide alternative communication channels (phone)
- **Data corruption**: Daily automated backups and transaction rollback capability
- **System errors**: Modular design for easier error detection and maintenance
- **Integration issues**: Object-oriented design for future compatibility

## Undecided Issues
- Specific communication channels to actors
- Criteria for request refinement and filtering
- Notification preferences for profile changes
- Handling of acknowledged request modifications
- Performance measurement methodologies
- Quality assurance implementation details