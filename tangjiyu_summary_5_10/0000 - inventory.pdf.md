# Unified University Inventory System (UUIS) - Software Requirements Specification

## System Overview
The Unified University Inventory System (UUIS) is designed to integrate three faculty databases and provide a web interface that allows users to access and manage the integrated inventory. The system guarantees secure access to data from outside the university at any time during working hours.

## System Scope
The UUIS application provides the following core operations:
- Transferring assets between departments, faculties, and external entities
- Editing and modifying existing assets
- Adding new inventory assets
- Creating requests to borrow assets or reserve spaces
- Processing asset returns
- Creating new spaces/locations
- Approving user requests
- User authentication and authorization
- Search functionality
- Permission management
- Report generation

## System Description

### Inventory Assets
Assets are classified into three types:
1. Rooms and spaces
2. Software licenses
3. All other assets

Assets can be grouped (e.g., computer parts).

### University Structure
The organizational hierarchy consists of:
- University level (Level 3)
- Faculty level (Level 2)
- Department level (Level 1)
- User level (Level 0) - Can place inventory requests
- IT and security level (Level 4) - System maintenance

### User Roles
1. University administrators
2. Faculty administrators
3. Department administrators
4. Inventory administrators (delegated users with varying permissions)
5. Regular users (students and professors)
6. IT team system administrators

## Functional Requirements

### Asset Management
- **Asset Transfer**: Direct updates within same department; approval required for inter-department, inter-faculty, and external transfers
- **Asset Editing**: Administrative users can edit assets within their permission scope
- **Asset Modification**: All asset fields (except IDs) can be modified; bulk entry support available
- **Asset Addition**: Users at different administrative levels can add assets within their scope; bulk entry supported

### Request Management
- **Request Creation**: Authorized users can create requests to borrow assets or reserve spaces
- **Request Approval**: Administrative users can approve/reject requests within their permission level
- **Notification System**: Email notifications sent upon request processing
- **Execution Tracking**: Approved requests added to execution waiting list

### Space Management
- **Location Creation**: IT team members can create new spaces and modify floor structures
- **Space Reservation**: Users can request space reservations through request system

### User Management
- **Authentication**: Username/password authentication for all users
- **Authorization**: Role-based permission system with five administrative levels
- **Permission Delegation**: Administrative users can delegate permissions to other users
- **Permission Groups**: Predefined permissions by role:
  * Request-related permissions (create, list, show, edit, approve/reject)
  * Asset-related permissions (create, list, show, edit/modify)
  * Location-related permissions (create, list, show, edit, delete)
  * University structure permissions (create, list, show, edit, delete)
  * Search permissions (simple, advanced)
  * Report permissions (list, show)
  * User action permissions (list, show, edit, change permissions)
  * Audit permissions (list, show)

### Reporting
- Asset reports by location
- Request reports
- User permission reports

## Non-Functional Requirements

### Usability
- Learning time: Maximum 2-4 hours (considering many tasks are delegated to student workers)
- Clear and consistent web interface terminology
- Intuitive design for users with basic internet and office experience

### Availability
- System available during all working hours
- Maintenance and backup operations conducted outside working hours

### Portability
- Cross-platform compatibility (Microsoft and Unix systems)
- Browser compatibility (IE, Firefox, Chrome, Opera, Safari)

### Security
- Username/password authentication for all users
- Role-based permission assignment
- Local database server access restricted to IT team
- Query timeout after 1 minute
- Periodic backup operations

### Maintainability
- System designed for future evolution and ease of maintenance

## Core Use Cases

### Asset Modification
- Authenticated inventory administrators can search, edit, and modify asset properties
- Error handling for insufficient privileges or non-existent assets

### Request Processing
- Users create requests for asset borrowing or space reservation
- Multiple request types: basic, advanced, and exception requests
- Administrative approval workflow with notifications

### Permission Management
- Administrative users can delegate permissions to other users
- Validation to prevent users from assigning permissions beyond their own level

### Reporting
- Generation of asset reports by location
- Request history reports
- User permission reports

## Technical Constraints
- Database query timeout: 1 minute maximum
- Administrative permission hierarchy with delegation capability
- IT team exclusive access to database servers
- Support for bulk asset entry operations

## Cost Estimation
- Project duration: 3 months (14 weeks)
- Team size: 8 people
- Total effort: 1,120 hours (7 person-months)
- Estimated cost: $22,400.00 (at $20/hour)

## Quality Attributes
- Role-based access control with five administrative levels
- Comprehensive audit trail through request and permission tracking
- Cross-platform compatibility
- Responsive web interface
- Secure authentication and authorization
- Scalable permission delegation system
