# Software Requirements Specification (SRS)
## Childcare Center Management System (CCMS)
**Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Childcare Center Management System (CCMS). It is intended to serve as a complete description of the system's behavior for stakeholders, including project managers, developers, testers, and end-users. This SRS will be the basis for design, implementation, verification, and project management.

#### 1.2 Scope
The CCMS is a comprehensive web-based application designed to automate the core administrative and operational tasks of a childcare center. The system will manage child and family information, streamline enrollment and classroom assignments, track daily attendance, automate billing based on attendance and late pickups, and generate essential reports. It aims to replace manual, paper-based processes, thereby improving accuracy, efficiency, and workflow for administrators and teaching staff.

**In-Scope:**
*   Web-based user interface for all functions.
*   Management of child, family, and employee records.
*   Enrollment process, including waiting list management.
*   Daily check-in/check-out with late pickup tracking.
*   Automated monthly invoice generation.
*   Generation of predefined operational reports.
*   A daily task reminder system for employees.
*   Role-based access control for Administrators and Teachers/Assistants.

**Out-of-Scope:**
*   Mobile-native applications (though the web interface must be functional on specified browsers).
*   Payroll processing for employees.
*   Advanced accounting or general ledger integration.
*   Meal planning or nutritional tracking.
*   Real-time video monitoring or parent communication portals.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **CCMS:** Childcare Center Management System.
*   **Admin/Administrator:** A user role with full system access and privileges.
*   **Teacher/Assistant:** A user role with limited access, primarily for data entry related to children.
*   **ASP.NET:** The web application framework specified for system development.
*   **UI:** User Interface.

#### 1.4 References
*   Project Charter – Childcare Center Management System.
*   Stakeholder Interview Summaries.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements, including performance, security, and constraints.

---

### 2. Overall Description

#### 2.1 Product Perspective
The CCMS is a new, standalone web application. It must interface with a backend database (to be specified during design) and be hosted on a web server compatible with the ASP.NET framework. The primary users will interact with the system via their web browsers.

#### 2.2 Product Functions
The high-level functions of the CCMS are:
1.  **Enrollment & Classroom Management:** Manage child registrations, assign children to classrooms adhering to capacity rules, and maintain a prioritized waiting list.
2.  **Daily Operations:** Record and timestamp child arrivals and departures, automatically flag and calculate fees for late pickups.
3.  **Record Keeping:** Maintain secure, detailed records for children (including immunizations, allergies, and teacher notes) and their families.
4.  **Billing & Financials:** Automatically generate monthly invoices based on attendance records, late fees, and enrollment plans.
5.  **Reporting:** Generate standard reports (e.g., attendance summaries, immunization reports, revenue reports).
6.  **Staff Tools:** Provide a daily dashboard or list of reminders for employees (e.g., immunizations due, children absent).
7.  **User & Security Management:** Authenticate users and enforce role-based permissions.

#### 2.3 User Characteristics
| User Class | Skill Level | Key Responsibilities |
| :--- | :--- | :--- |
| **Administrator** | High computer literacy. Understands center operations, billing, and reporting. | Full system configuration. Manage all records (children, families, staff). Process enrollments and waiting lists. Generate all reports and invoices. Override system actions if necessary. |
| **Teacher / Assistant** | Basic computer literacy. Primary focus is child care. | Record daily child arrival/departure times. Enter basic observational notes or comments for children in their classroom. View daily reminders. Cannot access financial or sensitive administrative data. |

#### 2.4 Constraints
1.  **Technical:** The system must be developed using the **ASP.NET** framework.
2.  **Infrastructure:** The system requires a compatible Microsoft Internet Information Services (IIS) web server for deployment.
3.  **Client-Side:** The web-based user interface must be compatible with **Internet Explorer** and **Netscape Navigator** browsers.
4.  **Business Rule:** Each classroom has a strict **maximum capacity of 20 children**. The system must enforce this constraint during enrollment and classroom assignment.
5.  **Performance:** The system must respond to any user request within **20 seconds** under normal operational load.

#### 2.5 Assumptions and Dependencies
*   Users will have reliable internet access and a compatible browser installed.
*   A suitable server and database environment will be provisioned for hosting the application.
*   Initial data migration from existing paper or simple digital records will be performed manually.

---

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 User Authentication and Authorization (UAA)
*   **UAA-1:** The system shall require username and password authentication for all access.
*   **UAA-2:** The system shall provide two distinct user roles: Administrator and Teacher/Assistant.
*   **UAA-3:** Administrators shall have access to all system functions and data.
*   **UAA-4:** Teachers/Assistants shall only be able to:
    *   View children assigned to their classroom.
    *   Record arrival/departure times for these children.
    *   Add/view teacher comments for these children.
    *   View their own daily reminders.

##### 3.1.2 Child and Family Management (CFM)
*   **CFM-1:** The system shall allow Administrators to create, read, update, and deactivate child records.
*   **CFM-2:** A child record shall include: Full name, date of birth, address, primary guardian contacts, emergency contacts, authorized pick-up list, immunization history, allergy information, and physician details.
*   **CFM-3:** The system shall allow Administrators to create, read, update, and deactivate family records, linking one or more children to a family.
*   **CFM-4:** The system shall maintain a history of teacher comments/notes for each child, timestamped and linked to the staff member who entered them.

##### 3.1.3 Enrollment and Classroom Management (ECM)
*   **ECM-1:** The system shall manage an enrollment process for new children, capturing all required data from CFM-2.
*   **ECM-2:** The system shall allow Administrators to assign a child to a specific classroom.
*   **ECM-3:** The system shall prevent an assignment that would cause a classroom to exceed its maximum capacity of **20 children**. An error message must be displayed.
*   **ECM-4:** The system shall maintain a waiting list for enrollment when all appropriate classrooms are at capacity.
*   **ECM-5:** The system shall allow an Administrator to manage the waiting list (add, remove, re-prioritize) and enroll a child from the list when a spot becomes available.

##### 3.1.4 Daily Attendance and Tracking (DAT)
*   **DAT-1:** The system shall allow authorized staff (Teachers/Assistants and Admins) to record a child's arrival time (check-in).
*   **DAT-2:** The system shall allow authorized staff to record a child's departure time (check-out).
*   **DAT-3:** The system shall automatically calculate if a pick-up is late based on a configurable center closing time (e.g., 6:00 PM).
*   **DAT-4:** The system shall flag late pickups and record the duration of lateness in 15-minute increments.

##### 3.1.5 Billing and Invoicing (BIN)
*   **BIN-1:** The system shall automatically generate a monthly invoice for each family.
*   **BIN-2:** The invoice shall be based on:
    *   The child's enrollment plan (flat monthly rate).
    *   Recorded attendance for the month.
    *   Calculated late pickup fees (configurable fee per increment).
*   **BIN-3:** The system shall allow Administrators to view, print, and mark invoices as paid.
*   **BIN-4:** The system shall maintain a payment history for each family.

##### 3.1.6 Reporting (REP)
*   **REP-1:** The system shall generate a predefined **Attendance Summary Report** (daily/weekly/monthly).
*   **REP-2:** The system shall generate a predefined **Immunization Report** listing children with upcoming or overdue immunizations.
*   **REP-3:** The system shall generate a predefined **Class Roster Report** for each classroom.
*   **REP-4:** The system shall generate a predefined **Billing Summary Report** for a given period.
*   **REP-5:** All reports shall be filterable by date range and exportable to PDF or CSV format.

##### 3.1.7 Reminder System (REM)
*   **REM-1:** The system shall provide a daily dashboard or list view for employees upon login.
*   **REM-2:** Reminders shall include, but not be limited to:
    *   Children in the employee's classroom with immunizations due soon.
    *   Children absent without prior notification.
    *   Upcoming center events or deadlines (entered by Administrators).

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance Requirements
*   **PER-1:** The system shall respond to **95% of user interactions** (page loads, form submissions, report generation) within **20 seconds** under expected concurrent user load (approx. 10-15 users).
*   **PER-2:** The daily check-in/check-out process for a single child shall be completable in less than 5 seconds.

##### 3.2.2 Usability Requirements
*   **USB-1:** The user interface shall be intuitive and require minimal training for Teachers/Assistants with basic computer skills.
*   **USB-2:** Common tasks (check-in/check-out) shall be accessible in three clicks or fewer from the main dashboard.
*   **USB-3:** The system shall provide clear confirmation messages for successful actions and descriptive error messages for failures.

##### 3.2.3 Reliability & Availability
*   **REL-1:** The system shall be available for use during core business hours (6:00 AM to 8:00 PM, weekdays) with uptime of 99%.
*   **REL-2:** The system shall perform automatic daily backups of all data.

##### 3.2.4 Security Requirements
*   **SEC-1:** All passwords shall be stored in the database using industry-standard hashing (e.g., bcrypt).
*   **SEC-2:** The system shall implement measures to prevent SQL injection and cross-site scripting (XSS) attacks.
*   **SEC-3:** All web sessions shall timeout after 30 minutes of inactivity.

##### 3.2.5 Design Constraints
*   **CON-1:** The system shall be implemented as a web application using the **ASP.NET** framework.
*   **CON-2:** The client-side interface shall be fully functional and render correctly in **Internet Explorer 6+** and **Netscape Navigator 7+**.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| Quality Assurance Lead | | | |