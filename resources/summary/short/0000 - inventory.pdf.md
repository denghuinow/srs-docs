# Short Summary: Unified University Inventory System (UUIS)

## Background and Objectives
The Unified University Inventory System (UUIS) aims to integrate three separate faculty databases into a single web-based platform, enabling centralized management and access to university inventory assets. Its primary goal is to provide secure, anytime access during working hours for authorized users to manage inventory operations efficiently.

## In Scope
- Web-based interface for inventory management accessible during working hours.
- Management of three asset types: rooms/spaces, software licenses, and other physical assets.
- Inventory operations including transfers, edits, additions, and returns.
- Request system for borrowing assets or reserving spaces with approval workflows.
- User authentication and role-based permission management.

## Out of Scope
- Integration with external systems beyond the three specified faculty databases.
- Real-time inventory tracking or IoT-based asset monitoring.
- Mobile application development (web interface only).
- Financial management or billing for asset usage.
- Advanced analytics or predictive maintenance features.

## Stakeholders and Core Use Cases
**Stakeholders:**
- University Administrators: Manage entire university inventory and permissions.
- Faculty Administrators: Oversee faculty-level inventory and operations.
- Department Administrators: Control department-specific inventory assets.
- Inventory Administrators: Execute delegated inventory management tasks.
- Users (Students/Professors): Request and borrow inventory assets.
- IT Team: Maintain system infrastructure and security.

**Core Use Cases:**
1. As a user, I want to create borrowing requests so that I can access needed assets.
2. As a department administrator, I want to approve internal transfer requests so that assets move efficiently within my department.
3. As an inventory administrator, I want to modify asset properties so that inventory records remain accurate.
4. As a faculty administrator, I want to generate asset reports by location so that I can track inventory distribution.
5. As an IT administrator, I want to assign user permissions so that access control aligns with organizational roles.
6. As a university administrator, I want to approve inter-faculty transfers so that assets are allocated appropriately across the university.

## Success Metrics
- System availability during 100% of working hours with maintenance conducted outside these periods.
- User training completed within 2-4 hours for users with basic internet and office experience.
- Successful integration of three separate faculty databases into a unified inventory system.

## Major Constraints
- Must run on both Microsoft and Unix platforms with browser compatibility (IE, Firefox, Chrome, Opera, Safari).
- Authentication limited to username/password without multi-factor options.
- Query execution timeout set to 1 minute maximum.
- Permission delegation cannot exceed the delegator's own permission level.
- Asset transfers outside university require university-level approval.

## Undecided Issues
- Specific backup frequency and disaster recovery procedures.
- Detailed audit trail implementation requirements.
- Exact criteria for "exception requests" requiring IT intervention.
- Performance benchmarks beyond basic availability requirements.
- Interface design specifics and user experience validation methods.