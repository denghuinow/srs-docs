# Balanced Summary

## Goals and Scope
The Unified University Inventory System (UUIS) aims to integrate three faculty databases into a single web-based inventory management platform. It provides secure access for authorized users to manage university assets and spaces during working hours. The system covers core operations like asset transfers, request management, and inventory reporting across the university hierarchy.

## Roles and User Stories
- **As a Student/Professor**, I want to create borrowing requests so that I can access needed assets
- **As a Department Administrator**, I want to approve internal requests so that assets stay within departmental control
- **As a Faculty Administrator**, I want to manage faculty-wide assets so that resources are properly allocated
- **As an Inventory Administrator**, I want to modify asset properties so that inventory records remain accurate
- **As an IT Administrator**, I want to assign permissions so that users have appropriate system access

## Key Processes
1. **Authentication** (trigger: user accesses system)
2. **Asset Search** (trigger: user needs to locate items)
3. **Request Creation** (trigger: user needs to borrow assets)
4. **Request Approval** (trigger: pending requests require action)
5. **Asset Transfer** (trigger: approved inter-department requests)
6. **Inventory Update** (trigger: assets are returned or modified)
7. **Report Generation** (trigger: management needs inventory data)

## Domain Data Elements
- **Asset** (asset_id, type, location, status, owner)
- **User** (user_id, role, permissions, department, email)
- **Request** (request_id, requester, assets, status, approval_level)
- **Location** (location_id, type, capacity, department, floor)
- **Permission** (permission_id, role, actions, scope, level)
- **Report** (report_id, type, filters, generated_date, content)

## Non-functional Requirements
- System available during working hours with maintenance after hours
- Maximum 2-4 hour learning curve for new users
- Support for major browsers (IE, Firefox, Chrome, Safari, Opera)
- User authentication via username/password with role-based permissions
- Query timeout after 1 minute to ensure performance
- Portable across Microsoft and Unix platforms

## Milestones and External Dependencies
- Integration with three existing faculty databases
- Authentication system implementation
- Permission hierarchy setup across university levels
- Bulk asset import capability development
- Report generation module completion

## Risks and Mitigation Strategies
- **Complex permission delegation**: Implement predefined permission groups by administrative level
- **Database integration challenges**: Use technology-independent business terminology
- **User adoption**: Ensure intuitive web interface with consistent terminology
- **System performance**: Implement query timeouts and periodic maintenance
- **Security breaches**: Restrict local database access to IT team only

## Undecided Issues
- Specific backup frequency and procedures
- Detailed exception handling for all error scenarios
- Exact maintenance window scheduling
- Comprehensive audit trail implementation details
- Performance benchmarks beyond query timeouts
- Not mentioned