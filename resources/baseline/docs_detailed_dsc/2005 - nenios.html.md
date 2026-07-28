# Software Requirements Specification (SRS)
## For Neñios Child Care Management (NCCM) System
**Version:** 1.0  
**Date:** October 26, 2023  
**Prepared for:** Neñios Child Care Center  
**Prepared by:** Code Works Development Team

---

### **1. Introduction**

#### **1.1 Purpose**
This document defines the functional and non-functional requirements for the Neñios Child Care Management (NCCM) system. It serves as a formal agreement between the stakeholders (Neñios Child Care Center) and the developers (Code Works) regarding the system's capabilities, constraints, and features. The intended audience includes project managers, developers, testers, and end-users.

#### **1.2 Scope**
The NCCM is a comprehensive, web-based software solution designed to automate and streamline the administrative and operational workflows of a child care center. Its core functionalities include:
*   Child enrollment and classroom management.
*   Daily attendance tracking with late pick-up fee calculation.
*   Billing and invoice generation with support for family discounts.
*   Immunization record management and reminder notifications.
*   Role-based access for administrators, teachers, and teaching assistants.
*   Reporting and data management.

**Out of Scope:**
*   The system will **not** enforce or guarantee compliance with Federal, State, or Local child care licensing regulations. Compliance remains the responsibility of the facility management.
*   Direct parent portal access for real-time monitoring or payment processing is not included in this initial release.
*   Payroll management for center employees.
*   Meal planning or nutritional tracking.

#### **1.3 Definitions, Acronyms, and Abbreviations**
*   **NCCM:** Neñios Child Care Management System.
*   **CRUD:** Create, Read, Update, Delete.
*   **SLA:** Service Level Agreement.
*   **UAT:** User Acceptance Testing.
*   **UI:** User Interface.

#### **1.4 References**
*   Project Charter and Initial Statement of Work.
*   Stakeholder Interview Notes.

#### **1.5 Overview**
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its users, and constraints. Section 3 details the specific functional requirements. Appendices contain supplementary information such as data models and open issues.

---

### **2. Overall Description**

#### **2.1 Product Perspective**
The NCCM is a new, self-contained web application. It will interact with a central database server and be accessed by users via standard web browsers (e.g., Internet Explorer, Netscape Navigator). It is designed to replace manual, paper-based processes.

#### **2.2 User Classes and Characteristics**
| User Class | Key Characteristics | Primary Responsibilities |
| :--- | :--- | :--- |
| **Administrator** | Full system access. Manages center operations. | Manage all accounts (customer, child, employee). Assign classrooms. Manage waiting lists. Generate invoices and reports. Reset passwords. |
| **Teacher** | Access limited to assigned classroom(s). | Document child behavior and daily comments. View immunization reminders for children in their class. |
| **Teaching Assistant** | Access limited to check-in/out functions. | Record child arrival and departure times. Verify identity of authorized pick-up persons. |
| **Parent/Customer** | External stakeholder; receives outputs. | Provides child/enrollment information. Receives invoices and notifications (via system-generated outputs). |
| **System Developer** | Technical expert. | Implements, maintains, and supports the software application. |

#### **2.3 Operating Environment**
*   **Software:** The application will be developed using ASP.NET and will require a compatible web server (e.g., IIS) and a relational database server (e.g., Microsoft SQL Server).
*   **Hardware:** Standard web server and database server hardware capable of supporting the expected user load.
*   **Browsers:** The web-based UI must be compatible with Internet Explorer and Netscape Navigator.

#### **2.4 Design and Implementation Constraints**
1.  Must be a web-based application accessible via browser.
2.  Must use a relational database for data persistence.
3.  Must implement role-based security.
4.  Must adhere to the performance metric of <20 seconds for all user requests.

#### **2.5 Assumptions and Dependencies**
*   The child care center has stable internet connectivity.
*   Users have basic computer literacy.
*   The facility's official opening and closing times are configured and maintained within the system by an Administrator.
*   Pricing schedules (base rate, multi-child discount, late fee) are configurable by an Administrator.

---

### **3. System Features and Requirements**

#### **3.1 Functional Requirements**

##### **3.1.1 User Authentication and Authorization (UA)**
*   **UA-1:** The system shall require a unique UserID and password for employee access.
*   **UA-2:** Passwords shall be 6-8 alphanumeric characters.
*   **UA-3:** The system shall present a login screen as the initial point of entry.
*   **UA-4:** Upon successful authentication, the system shall grant access to functions and data based on the user's role (Administrator, Teacher, Assistant).
*   **UA-5:** After three consecutive failed login attempts, the system shall lock the user account.
*   **UA-6:** Only an Administrator shall be able to reset a locked or forgotten password.
*   **UA-7:** The system shall automatically log out a user after 10 minutes of inactivity.

##### **3.1.2 Customer and Child Management (CC)**
*   **CC-1:** The system shall allow an Administrator to create, read, update, and deactivate Customer (Parent) records (Name, Address, Phone, Email, Emergency Contact).
*   **CC-2:** The system shall allow an Administrator to create, read, update, and deactivate Child records (Name, Date of Birth, Gender, Photo, Special Needs).
*   **CC-3:** The system shall link a Child record to a primary Customer (Parent) record.
*   **CC-4:** The system shall allow an Administrator to assign a Child to a specific Classroom based on age group and capacity.

##### **3.1.3 Classroom and Waiting List Management (CL)**
*   **CL-1:** The system shall allow an Administrator to define Classrooms (Name, Assigned Teacher, Assigned Assistant, Maximum Capacity).
*   **CL-2:** The system shall enforce classroom capacity. An Administrator shall not be able to assign a child to a classroom that is at maximum capacity.
*   **CL-3:** If a classroom is full, the system shall allow an Administrator to place a child on a waiting list for that specific classroom (Child Name, Parent Contact, Date Added).
*   **CL-4:** The system shall provide a view for the Administrator to see the waiting list, ordered by date added.
*   **CL-5:** When a spot becomes available, the system shall allow the Administrator to move a child from the waiting list into the classroom, updating occupancy.

##### **3.1.4 Daily Attendance and Operations (AT)**
*   **AT-1:** A Teaching Assistant shall be able to record a child's arrival (Time In) for the current day.
*   **AT-2:** A Teaching Assistant shall be able to record a child's departure (Time Out) for the current day.
*   **AT-3:** The system shall calculate the duration between the recorded Time Out and the center's official closing time.
*   **AT-4:** If the departure is after closing, the system shall automatically calculate a late fee ($10 per hour or partial hour) and associate it with the child's account.
*   **AT-5:** A Teacher shall be able to add behavioral notes/comments to a Child's record for the current day.

##### **3.1.5 Immunization Management (IM)**
*   **IM-1:** The system shall allow an Administrator to record a child's immunizations (Type, Date Received).
*   **IM-2:** The system shall allow an Administrator to define a schedule for when the next immunization is due.
*   **IM-3:** The system shall display a pop-up notification to a Teacher upon login if any child in their assigned classroom has an immunization due within the next two weeks.
*   **IM-4:** When generating a monthly invoice, the system shall include a notice for any immunizations due for the customer's children.

##### **3.1.6 Billing and Invoicing (BI)**
*   **BI-1:** The system shall automatically generate monthly invoices for all active customers.
*   **BI-2:** The invoice shall include a base rate per child.
*   **BI-3:** The system shall apply a 25% discount to the base rate for the third and any subsequent child from the same family.
*   **BI-4:** The invoice shall include any accumulated late fees for the billing period.
*   **BI-5:** The invoice shall include immunization due notices (see IM-4).
*   **BI-6:** The system shall allow an Administrator to mark an invoice as Paid, Pending, or Overdue.

##### **3.1.7 Reporting (RE)**
*   **RE-1:** The system shall generate a Classroom Roster report.
*   **RE-2:** The system shall generate an Attendance Report for a selected date range and child/classroom.
*   **RE-3:** The system shall generate a Billing Summary report.
*   **RE-4:** The system shall generate an Immunization Due report.
*   **RE-5:** All reports shall be viewable on-screen and printable via a standard system print dialog.

##### **3.1.8 System Utilities (SU)**
*   **SU-1:** Any employee shall be able to set a daily pop-up reminder for themselves.
*   **SU-2:** The system shall log (User ID, Date, Time, Action Description) for all create, update, or delete operations on Customer, Child, and Employee accounts.

#### **3.2 Non-Functional Requirements**

##### **3.2.1 Performance**
*   The system shall respond to any user interaction (page load, form submission, report generation) within 20 seconds under normal operating conditions.
*   The system shall support concurrent use by all employees of the center (estimated 10-15 users).

##### **3.2.2 Reliability**
*   The system shall maintain data integrity, ensuring relationships between records (e.g., Child to Classroom) are preserved.
*   The database shall support daily backup procedures executed by the system administrator.

##### **3.2.3 Security**
*   Access shall be controlled via role-based authentication (UA-4).
*   Passwords shall be stored in an encrypted format.
*   User sessions shall timeout after 10 minutes of inactivity (UA-7).

##### **3.2.4 Observability**
*   All critical account modifications shall be audited (SU-2).
*   System errors shall be logged with a timestamp and user context for technical support.

---

### **4. External Interface Requirements**

#### **4.1 User Interfaces**
The primary UI will be a web-based interface consisting of HTML forms, tables, and reports. It will include:
*   A login screen.
*   Role-specific dashboards/menus.
*   Data entry forms for all entities (Child, Customer, Attendance, etc.).
*   Report display screens.
*   Pop-up notification dialogs for reminders and immunization alerts.

#### **4.2 Hardware Interfaces**
*   **Printer:** The system will generate standard print commands to be handled by the client's operating system and printer drivers.

#### **4.3 Software Interfaces**
*   **Database:** The application will interface with a relational database management system (RDBMS) via SQL queries and commands for all persistent data storage and retrieval.

#### **4.4 Communications Interfaces**
*   The system will use HTTP/HTTPS protocols for communication between client browsers and the web server.

---

### **5. Acceptance Criteria**
*   **Authentication Test:** Verify that a Teaching Assistant cannot access the billing report generation screen.
*   **Attendance & Billing Test:** Record a departure 1 hour 5 minutes after closing. Confirm a $20 late fee is added to the child's account and appears on the next invoice.
*   **Immunization Test:** Set a child's immunization due date to 13 days in the future. Log in as that child's Teacher and confirm a pop-up reminder appears.
*   **Multi-Child Discount Test:** For a customer with three children enrolled (base rate $90/child), generate an invoice. Confirm the total is ($90 + $90) + ($90 * 0.75) = $157.50 + $67.50 = $225.00.
*   **Waiting List Test:** Attempt to assign a child to a full classroom. Confirm the system prevents the assignment and allows the child to be added to the waiting list.

---

### **Appendix A: Domain Model / Data Dictionary**
Based on the provided domain model, key entities include:
*   **Employee:** `UserID(PK), Name, Role, Password`
*   **Customer:** `CustomerID(PK), Name, Address, Phone, Email, EmergencyContact`
*   **Child:** `ChildID(PK), Name, DateOfBirth, Gender, ClassroomID(FK), Photo, SpecialNeeds, CustomerID(FK)`
*   **Classroom:** `ClassroomID(PK), Name, TeacherID(FK), AssistantID(FK), MaxCapacity, CurrentOccupancy`
*   **ImmunizationRecord:** `RecordID(PK), ChildID(FK), ImmunizationType, DateReceived, NextDueDate`
*   **AttendanceRecord:** `RecordID(PK), ChildID(FK), Date, TimeIn, TimeOut, LateFeeApplied`
*   **Invoice:** `InvoiceID(PK), CustomerID(FK), Month, Year, BaseAmount, DiscountAmount, LateFees, TotalAmount, Status`
*   **WaitingListEntry:** `EntryID(PK), ChildName, ParentContact, ClassroomID(FK), DateAdded`

---

### **Appendix B: Open Issues and Pending Decisions**
| # | Issue / Decision Point | Responsible Party |
| :--- | :--- | :--- |
| 1. | Specific algorithm for generating initial employee usernames. | Code Works |
| 2. | Technical implementation details for the 10-minute inactivity auto-logoff. | Code Works |
| 3. | Final format (modal, sidebar) and delivery mechanism for daily pop-up reminders. | Code Works |
| 4. | UI design and workflow for entering and managing immunization schedules. | Code Works & Administrator |
| 5. | Exact column layout, sorting, and filtering for all standard reports (R30-R38). | Administrator |
| 6. | Process and UI for handling general "customer log notes" (separate from behavioral notes). | Administrator |
| 7. | Formal protocol for verifying authorized pick-ups (e.g., check ID, PIN). | Teaching Assistant & Administrator |
| 8. | Detailed disaster recovery plan for database server failure. | Code Works & Center Management |