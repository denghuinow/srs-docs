# Short Summary: Neñios Child Care Center Management Software

## Background and Objectives
The Neñios Child Care Management (NCCM) software is a web-based system designed to automate operational workflows in a child care center, enabling staff to spend more time caring for children. Its primary objectives are to manage child enrollment, track immunizations and attendance, handle billing, and generate reports through a centralized, browser-accessible platform.

## In Scope
- User authentication with role-based access (administrators, teachers, assistants).
- Management of child and parent accounts, including immunizations, attendance, and authorized pickups.
- Billing and invoicing with support for late fees and multi-child discounts.
- Generation of predefined reports (e.g., customer directory, immunization due lists).
- Daily reminders for employees and immunization notifications.

## Out of Scope
- Compliance with Federal, State, and Local daycare licensing guidelines.
- Direct parent/guardian access to the system (e.g., for viewing reports or invoices).
- Integration with external financial or accounting software.
- Mobile application or offline functionality.
- Advanced data analytics or predictive features for business growth.

## Stakeholders and Core Use Cases
**Stakeholders:**
- **Administrators:** Manage all system data, customer accounts, billing, and reports.
- **Teachers:** Document child behavior and comments for parent-teacher conferences.
- **Teaching Assistants:** Record child arrival/departure times and track late pickups.
- **Parents/Customers:** Enroll children, provide emergency contacts, and receive invoices.
- **Code Works (Development Team):** Design, develop, and maintain the NCCM software.
- **Care Center Management:** Oversee operations and utilize reports for decision-making.

**Core Use Cases:**
1. As an administrator, I want to check classroom availability and manage waiting lists so that I can efficiently enroll new children.
2. As a teaching assistant, I want to record child arrival and departure times so that late pickups can be accurately billed.
3. As a teacher, I want to add or edit behavior comments for children so that I can prepare for parent-teacher conferences.
4. As an administrator, I want to generate and print monthly invoices with immunization notices so that billing is timely and compliant.
5. As any employee, I want to set daily reminders for myself so that I can stay organized with important tasks.
6. As an administrator, I want to view immunization due reports so that I can ensure children meet health requirements.

## Success Metrics
- System responds to user requests within 20 seconds for all operations.
- Reduction in administrative time spent on manual tasks (e.g., billing, report generation).
- Successful generation and accuracy of all required reports and invoices.

## Major Constraints
- The system must be web-based and compatible with Internet Explorer and Netscape Navigator.
- Development must use Microsoft ASP.NET, requiring a compatible web server.
- Each classroom has a maximum capacity of 20 children.
- Passwords must be 6–8 alphanumeric characters, with security measures for failed attempts.
- User interface must have a blue background for all windows.

## Undecided Issues
- Implementation of low-priority requirements (e.g., automatic logoff after 10 minutes of inactivity).
- Specific design of the calendar picker for daily reminders.
- Configuration options for immunization types and schedules by administrators.
- Handling of parent referrals and associated discounts beyond multi-child pricing.
- Detailed workflow for resetting forgotten passwords.