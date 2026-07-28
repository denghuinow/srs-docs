# Detailed Summary: Neñios Child Care Management (NCCM) Software

## Background and Scope
This document specifies requirements for a web-based Neñios Child Care Management (NCCM) system to automate administrative and operational workflows for a child care center. The system will manage child enrollment, attendance tracking, billing, immunization records, and reporting through a centralized database accessible via standard web browsers. Non-goals include handling compliance with Federal, State, and Local licensing regulations, which are assumed to be managed separately by the facility.

## Stakeholders Matrix and Use Cases
*   **Administrator**: Manages customer accounts, classroom assignments, waiting lists, billing, and reports; has full system access.
*   **Teacher**: Documents child behavior and comments, views immunization reminders for their classroom.
*   **Teaching Assistant**: Records child arrival/departure times and verifies authorized pick-ups.
*   **Parent/Customer**: Enrolls children, provides emergency and pick-up contacts, receives invoices and notifications.
*   **System Developer (Code Works)**: Implements and maintains the software application.

**Main Scenarios**: 1) New child enrollment with classroom availability check. 2) Daily child check-in/out with late pick-up tracking. 3) Teacher adding behavioral notes. 4) Administrator generating monthly invoices with late fees and immunization notices. 5) Any employee setting and receiving a daily reminder.
**Exception Scenarios**: 1) Classroom is full, child is placed on a waiting list. 2) Unauthorized person attempts to pick up a child. 3) User fails login after three attempts and is locked out.

## Business Process
**Main Process: Child Enrollment & Daily Operations**
1.  **Trigger**: Parent contacts center to enroll a child.
2.  Administrator checks classroom capacity for child's age group.
3.  If space exists, Administrator creates/updates customer and child records.
4.  If no space, Administrator adds child to classroom waiting list.
5.  Daily: Assistant records child arrival time.
6.  Teacher may add behavioral comments during the day.
7.  Daily: Assistant records child departure time; system calculates late fees if applicable.
8.  End of Month: System generates invoices, applies discounts for multiple children, and adds immunization due notices.

**Key Branch A: Waiting List Management (Trigger: Classroom opening)**
1.  Administrator identifies next child on the waiting list.
2.  Contacts parent to offer placement.
3.  Upon acceptance, moves child from waiting list to active enrollment.
4.  Updates classroom occupancy.

**Key Branch B: Late Pick-up Handling (Trigger: Child departure after official closing time)**
1.  System records actual departure time.
2.  Calculates late duration.
3.  Applies hourly late fee to the child's account.
4.  Includes fee in the next monthly invoice.

## Domain Model
*   **Employee** (UserID (unique, required), Name, Role, Password)
*   **Customer (Parent)** (CustomerID (unique, required), Name, Address, Phone, Email, EmergencyContact)
*   **Child** (ChildID (unique, required), Name, DateOfBirth, Gender, ClassroomID (reference), Photo, SpecialNeeds)
*   **Classroom** (ClassroomID (unique, required), Name, TeacherID (reference), AssistantID (reference), MaxCapacity)
*   **ImmunizationRecord** (RecordID (unique, required), ChildID (reference, required), ImmunizationType, DateReceived)
*   **AttendanceRecord** (RecordID (unique, required), ChildID (reference, required), Date, TimeIn, TimeOut)
*   **Invoice** (InvoiceID (unique, required), CustomerID (reference, required), Month, AmountDue, LateFees, Status)
*   **WaitingListEntry** (EntryID (unique, required), ChildName, ParentContact, ClassroomID (reference), DateAdded)

## Interfaces and Integrations
*   **Web Browser Client**: Direction: User to System. Interaction: Web-based UI. Input: User credentials, form data. Output: HTML pages, reports, pop-up reminders. SLA: Response time <20 seconds.
*   **Database Server**: Direction: System to System (internal). Interaction: Central data persistence. Input: CRUD operations from application logic. Output: Query results. SLA: High availability during business hours.
*   **Printer (Logical)**: Direction: System to Peripheral. Interaction: Report/Invoice generation. Input: Print command and data. Output: Physical documents. SLA: Support for standard print drivers.

## Acceptance Criteria
**Capability: User Authentication**
*   Given an employee with valid credentials, when they log into the system, then they are granted access according to their role (Admin/Teacher/Assistant).
*   Given a user who enters an incorrect password three times, when they attempt to log in again, then their account is locked until an Administrator resets the password.

**Capability: Attendance Tracking & Billing**
*   Given a child is picked up after the center's closing time, when the Assistant records the departure, then the system calculates a $10/hour late fee and associates it with the child's account for invoicing.
*   Given a customer with three enrolled children, when the monthly invoice is generated, then the total is calculated as $157.50 (for two children) + $45 (for the third child).

**Capability: Immunization Management**
*   Given a child's immunization is due within two weeks, when their Teacher logs in, then a notification is displayed.
*   Given a child is due for an immunization, when the monthly invoice is generated for their parent, then a notice is included on the invoice.

## Non-functional Metrics
*   **Performance**: All user requests shall respond within 20 seconds. The system shall support concurrent access by all center employees.
*   **Reliability**: The database shall maintain data integrity and support daily backup procedures.
*   **Security**: Access requires unique username and password (6-8 alphanumeric chars). Passwords shall be reset-able by Administrators.
*   **Compliance**: The software context assumes facility compliance with external regulations; the system itself does not enforce them.
*   **Observability**: System shall log user ID, date, time, and description for all account edits.

## Milestones and Release Strategy
1.  Finalize and sign off on SRS.
2.  Complete core database and authentication module.
3.  Implement child/parent account management and classroom/waiting list features.
4.  Develop daily operations modules (attendance, comments, reminders).
5.  Implement billing engine and reporting suite.
6.  User Acceptance Testing (UAT) and deployment of the web-based application.

## Risk List and Mitigation Strategies
1.  **Scope Creep**: Adhere strictly to prioritized requirements; defer Low/Medium priority items to future phases.
2.  **Performance Issues**: Conduct load testing with simulated typical user activity to ensure <20s response time.
3.  **Data Security**: Implement password policies and access control lists per role; sanitize database inputs.
4.  **User Adoption**: Involve key stakeholders (Administrators, Teachers) in design reviews and UAT.
5.  **Browser Compatibility**: Test UI extensively with specified browsers (Internet Explorer, Netscape Navigator).
6.  **Inaccurate Billing**: Thoroughly unit test billing logic, especially for multiple-child discounts and late fees.
7.  **Server Downtime**: Choose a reliable ASP.NET hosting provider with adequate support and backup.
8.  **Unclear Requirements**: Maintain an open issues list (Appendix B) and assign responsible parties for clarification.

## Undecided Issues and Responsible Parties
1.  Specific algorithm for generating usernames (R8) - Code Works.
2.  Implementation details for the 10-minute inactivity auto-logoff (R13) - Code Works.
3.  Format and delivery mechanism for pop-up daily reminders (R17) - Code Works.
4.  User interface design and workflow for entering immunization schedules (R21) - Code Works & Administrator.
5.  Exact format and fields for all required reports (R30-R38) - Administrator.
6.  Process for handling and logging "customer log notes" (R43) - Administrator.
7.  Protocol for verifying authorized pick-ups during check-out (implied by R40) - Teaching Assistant & Administrator.
8.  Disaster recovery plan for database failure - Code Works & Center Management.