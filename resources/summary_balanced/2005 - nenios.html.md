# Balanced Summary

## Goals and Scope
The Neñios Child Care Management (NCCM) software aims to automate operational workflows in a child care center through a web-based system. It will manage child enrollment, attendance tracking, billing, immunizations, and reporting to reduce administrative burden. The system focuses on improving information sharing among employees while maintaining secure access controls.

## Roles and User Stories
- **Administrator**: I want to manage customer accounts and classroom availability so that enrollment processes are efficient
- **Administrator**: I want to generate invoices and reports so that billing and documentation are accurate
- **Teacher**: I want to document child behavior and comments so that parent-teacher conferences are informative
- **Teaching Assistant**: I want to record child arrival/departure times so that attendance and late pickups are tracked
- **Parent/Guardian**: I want authorized pickups to be verified so that child safety is maintained

## Key Processes
1. **User Authentication** (trigger: system access) - Employees log in with username and password for system access
2. **Child Enrollment** (trigger: new registration) - Administrators check classroom availability and create/update accounts
3. **Attendance Tracking** (trigger: child arrival/departure) - Assistants record arrival and departure times
4. **Behavior Documentation** (trigger: observation) - Teachers add/edit child behavior comments
5. **Billing Generation** (trigger: end of month) - System calculates fees and generates invoices
6. **Report Generation** (trigger: administrative request) - Administrators generate various operational reports
7. **Reminder Management** (trigger: scheduled date) - System displays daily reminders to employees

## Domain Data Elements
- **Employee**: EmployeeID, Name, Role, AccessLevel, Password
- **Child**: ChildID, Name, DateOfBirth, Classroom, ImmunizationDates
- **Parent**: ParentID, Name, Address, Phone, EmergencyContact
- **Classroom**: ClassroomID, Name, Capacity, Teacher, Assistant
- **Invoice**: InvoiceID, AccountID, Amount, DueDate, LateFees
- **WaitingList**: WaitlistID, ChildName, ParentPhone, RequestDate

## Non-functional Requirements
- Web-based interface compatible with Internet Explorer and Netscape Navigator
- System response time within 20 seconds for all user requests
- Password security with 6-8 alphanumeric characters
- Blue background color for all windows
- Centralized database accessible via internet
- Support for multiple computer platforms through HTML standardization

## Milestones and External Dependencies
- Initial draft completion (10/17/05)
- ASP.NET technology dependency for web server implementation
- Microsoft technology stack requirement
- Browser compatibility testing
- Database deployment and configuration

## Risks and Mitigation Strategies
- Schedule delays: Prioritize requirements (High/Medium/Low) for potential scope reduction
- Security breaches: Implement password policies and automatic logout after inactivity
- System performance: Ensure 20-second response time requirement is met
- User adoption: Provide intuitive web interface familiar to users
- Data integrity: Maintain audit trails for account changes

## Undecided Issues
- Unique password requirement implementation
- Automatic logout timeout configuration
- Immunization type and schedule management
- Calendar interface for reminder dates
- Parent referral discount implementation
- Photo storage and management approach