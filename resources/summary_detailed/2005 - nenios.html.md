# Detailed Summary

## Background and Scope
The Neñios Child Care Management (NCCM) system is a web-based software solution designed to automate operational workflows for child care centers. It aims to improve efficiency by managing child enrollment, attendance tracking, billing, immunization monitoring, and reporting functions. The system will centralize data management and provide role-based access to employees. Non-goals include handling federal/state compliance requirements and providing parent-facing portals.

## Role Matrix and Use Cases
- **Administrator**: Full system access including account management, reporting, and billing
- **Teacher**: Can document child behavior and view assigned classroom information
- **Assistant**: Records child arrival/departure times and manages daily attendance

Main scenarios include: child enrollment process, daily attendance tracking, billing generation, and reminder management. Exception scenarios include: handling late pickups and managing waiting lists when classrooms are full.

## Business Process
**Main Enrollment Process** (trigger: parent inquiry):
1. Check classroom availability
2. Place on waiting list if full
3. Create/edit customer account
4. Assign to classroom
5. Record authorized pickups
6. Set up billing information

**Key Branch - Late Pickup** (trigger: child departure after hours):
1. Record actual departure time
2. Calculate late fee duration
3. Apply $10/hour charge
4. Update invoice

## Domain Model
- **Employee**: user_id (unique), password, role (required)
- **Parent**: name, address, phone (required), email, emergency_contact
- **Child**: name, birth_date (required), classroom, immunization_dates
- **Classroom**: name (unique), capacity (max:20), teacher, assistant
- **Invoice**: invoice_date, amount_due, late_fees, account_history
- **Reminder**: reminder_date, message, user_id (reference)
- **WaitingList**: child_name, parent_phone, date_added
- **Immunization**: type, due_date, received_date

## Interfaces and Integrations
- **Web Browser Interface**: Inbound, user interaction, supports IE/Netscape, SLA: 20s response time
- **Database System**: Internal, data persistence, stores all entity records, ensures data integrity
- **Reporting Module**: Internal, document generation, produces formatted reports and invoices

## Acceptance Criteria
- **Given** a teacher logs in, **when** they access their classroom, **then** they can view current student attendance
- **Given** an administrator processes end-of-month billing, **when** multiple children are enrolled, **then** appropriate discounts are applied
- **Given** a child is due for immunization, **when** the teacher logs in, **then** a notification is displayed

## Non-functional Metrics
- **Performance**: All user requests respond within 20 seconds
- **Security**: Role-based access control with password authentication (6-8 alphanumeric characters)
- **Reliability**: System maintains data integrity during concurrent user access

## Milestones and Release Strategy
1. Core authentication and role management
2. Child/parent account management
3. Attendance tracking system
4. Billing and invoicing module
5. Reporting functionality
6. Reminder system implementation

## Risk List and Mitigation Strategies
- **Technology dependency**: ASP.NET requirement limits hosting options
- **User adoption**: Provide comprehensive training for non-technical staff
- **Data security**: Implement password policies and session timeouts
- **System performance**: Optimize database queries for large datasets

## Undecided Issues and Responsible Parties
- Immunization schedule management approach (Not mentioned)
- Backup and recovery procedures (Not mentioned)
- System scalability for multiple locations (Not mentioned)
- Integration with payment processing systems (Not mentioned)