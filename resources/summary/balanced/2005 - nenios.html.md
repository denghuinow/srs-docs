# Balanced Summary: Neñios Child Care Center Management (NCCM) Software

## Goals and Scope
The NCCM software is a web-based system designed to automate the operational workflow of a child care center, improving efficiency in administrative tasks and child care management. Its primary objectives are to assist in managing child enrollments, tracking immunizations and attendance, processing billing, and generating reports, allowing staff to focus more on child care. The scope includes user access control, daily operations logging, customer account management, and automated billing and reporting features.

## Stakeholders and User Stories
*   **Administrator:** Responsible for full system access, managing customer accounts, enrollments, waiting lists, billing, and reports.
*   **Teacher:** Responsible for supervising children, documenting behavior and comments for parent-teacher conferences.
*   **Teaching Assistant:** Responsible for recording child arrival/departure times and verifying authorized pickups.
*   **Parent/Customer:** The guardian of a child enrolled at the center, who is billed for services and receives notifications.
*   **Code Works (Developer):** The software development team responsible for building and delivering the web-based application.

**User Stories:**
1.  As an **Administrator**, I want to check classroom availability and manage a waiting list so that I can efficiently handle new enrollment requests.
2.  As a **Teaching Assistant**, I want to record child arrival and departure times so that attendance is tracked and late pickups can be billed.
3.  As a **Teacher**, I want to add and edit behavioral comments for children so that I have documented information for parent-teacher conferences.
4.  As an **Administrator**, I want to generate and print monthly invoices with immunization notices so that billing is accurate and parents are informed.
5.  As an **Employee**, I want to set and receive daily reminder pop-ups so that I don't miss important events or tasks.
6.  As an **Administrator**, I want to run preformatted reports (e.g., Customer Directory, Immunization Due) so that I can access summarized center information.

## Key Processes
1.  **User Authentication:** (Trigger: Employee access attempt) An employee must log in with a username and password, which determines their access privileges within the system.
2.  **Child Enrollment:** (Trigger: Parent inquiry) An administrator checks classroom capacity, places the child on a waiting list if full, or creates/updates a customer account.
3.  **Daily Attendance Logging:** (Trigger: Child arrival/departure) A teaching assistant records a child's check-in and check-out times, which triggers late fee calculations.
4.  **Behavior Documentation:** (Trigger: Teacher observation) A teacher enters or edits notes regarding a child's behavior into the child's record.
5.  **Billing Cycle:** (Trigger: End of month) The system calculates monthly fees based on the number of enrolled children and any accrued late fees, generating invoices.
6.  **Report Generation:** (Trigger: Administrator request) An administrator selects and prints a preformatted report (e.g., enrollment, immunization status).
7.  **Reminder Management:** (Trigger: Employee action or login) An employee creates a reminder; the system displays it as a pop-up when the employee logs in on the specified date.

## Domain Data Elements
*   **Employee:** (PK: EmployeeID) Username, Password, Role (Admin/Teacher/Assistant), FirstName, LastName.
*   **Customer/Parent:** (PK: CustomerID) LastName, FirstName, Address, HomePhone, EmergencyContact.
*   **Child:** (PK: ChildID) FirstName, DateOfBirth, ClassroomID, [FK: CustomerID], Photo.
*   **Classroom:** (PK: ClassroomID) Name, Capacity (max 20), AssignedTeacherID, AssistantID.
*   **Immunization Record:** (PK: RecordID) [FK: ChildID], ImmunizationType, DateAdministered, DueDate.
*   **Invoice:** (PK: InvoiceID) [FK: CustomerID], InvoiceDate, TotalAmount, LateFeeDetails, Status.

## Non-Functional Requirements
1.  **Accessibility:** The system shall have a web-based interface compatible with Internet Explorer and Netscape Navigator.
2.  **Performance:** The system shall respond to all user requests within 20 seconds.
3.  **Usability:** The background color of all application windows shall be blue.
4.  **Security:** Users shall be authenticated via unique username and a 6-8 character alphanumeric password.
5.  **Reliability:** The system shall support the entry, storage, and updating of parent, child, and billing information.
6.  **Capacity:** The waiting list shall support up to 100 potential customers.

## Milestones and External Dependencies
1.  Finalization and agreement on this Software Requirements Specification (SRS).
2.  Completion of core module development (User Management, Enrollment, Attendance).
3.  Integration of billing and reporting modules.
4.  User Acceptance Testing (UAT) with center staff.
4.  Dependency: Availability of a web server supporting Microsoft ASP.NET technology.

## Risks and Mitigation Strategies
1.  **Risk:** Scope creep from numerous medium/low-priority requirements threatening the delivery schedule.
    *   **Mitigation:** Strictly prioritize implementation based on "High" priority requirements first; defer medium/low items.
2.  **Risk:** Performance degradation with a full database of children, parents, and historical records.
    *   **Mitigation:** Implement efficient database indexing and query optimization during design.
3.  **Risk:** Security vulnerability from simple password rules or lack of account lockout.
    *   **Mitigation:** Enforce password complexity and implement account lockout after failed attempts (Req. R11).
4.  **Risk:** User resistance from staff unfamiliar with a web-based system.
    *   **Mitigation:** Provide comprehensive training and ensure the UI is intuitive and meets usability requirements.
5.  **Risk:** Incorrect billing calculations, leading to financial loss or customer disputes.
    *   **Mitigation:** Rigorous testing of all billing rules and scenarios, including discounts and late fees.

## Undecided Issues
1.  The final implementation plan for the "pop-up" daily reminder feature (R17).
2.  Whether to automate the process for resetting forgotten passwords (R12) or keep it manual.
3.  The specific calendar control to be used for selecting reminder dates (R15).
4.  The exact method for administrators to define and manage immunization schedules (R21).
5.  The design and format of the audit trail for account edits (R39).
6.  Handling of the session timeout feature (R13) and its impact on user workflow.