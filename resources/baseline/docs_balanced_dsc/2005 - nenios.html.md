# Software Requirements Specification (SRS)
## For
# Neñios Child Care Center Management (NCCM) Software

**Document Version:** 1.0  
**Date:** [Date of Creation]  
**Authors:** Code Works Development Team  
**Status:** Draft for Review

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the Neñios Child Care Center Management (NCCM) Software. It serves as a formal agreement between the stakeholders (Neñios Child Care Center) and the developers (Code Works) regarding the system's capabilities, constraints, and features. The intended audience includes project managers, developers, testers, and end-users.

### 1.2 Project Scope
The NCCM is a comprehensive, web-based management system designed to automate and streamline the operational workflow of a child care center. Its primary goal is to improve administrative efficiency in child enrollment, attendance tracking, immunization management, billing, and reporting, thereby allowing staff to dedicate more time to child care. The system will provide role-based access for Administrators, Teachers, and Teaching Assistants, and will manage data related to Customers (Parents), Children, Classrooms, and Financial transactions.

**In-Scope:**
*   User authentication and role-based authorization.
*   Management of child enrollments, waiting lists, and classroom capacity.
*   Daily logging of child attendance (check-in/check-out).
*   Documentation of child behavioral notes.
*   Management of child immunization records.
*   Automated monthly billing and invoice generation.
*   Generation of preformatted operational reports.
*   A personal reminder system for employees.

**Out-of-Scope:**
*   A public-facing portal for parents to access records or make payments.
*   Payroll management for center employees.
*   Inventory management for supplies.
*   Meal planning or nutritional tracking.
*   Real-time video monitoring integration.

### 1.3 Definitions, Acronyms, and Abbreviations
*   **NCCM:** Neñios Child Care Center Management Software.
*   **PK:** Primary Key (Database).
*   **FK:** Foreign Key (Database).
*   **UI:** User Interface.
*   **UAT:** User Acceptance Testing.
*   **Admin/Administrator:** A system user with full administrative privileges.
*   **Customer:** The parent or legal guardian of a child enrolled at the center.

### 1.4 References
*   Project Charter and Initial Statement of Work.
*   Stakeholder Interview Notes.
*   [List any other relevant documents]

### 1.5 Document Overview
The remainder of this document details the overall description of the product, specific functional and non-functional requirements, and supporting appendix information.

## 2. Overall Description

### 2.1 Product Perspective
The NCCM is a new, self-contained web application. It will operate in a client-server model where users access the system via a web browser (Internet Explorer, Netscape Navigator). The system will rely on a backend database server (technology TBD, but compatible with ASP.NET) and a web server hosting the ASP.NET application.

### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Responsibilities |
| :--- | :--- | :--- |
| **Administrator** | Center manager or lead administrative staff. Computer literate but not necessarily technical experts. Requires full control over all data and processes. | Manage all system data (employees, customers, children, classrooms). Process enrollments and waiting lists. Generate invoices and reports. Oversee system configuration. |
| **Teacher** | Child care professional. Primary interaction is with child records, not financial data. Needs simple, efficient data entry. | Document child behavior and developmental notes. View classroom rosters and child profiles. |
| **Teaching Assistant** | Supports Teachers in daily operations. Tasks are repetitive and time-sensitive (e.g., check-in). | Record child arrival and departure times. Verify authorized pick-up persons. |
| **Customer/Parent** | *Indirect User*. They are the subject of data (billing, contact info) but do not directly interact with the system in Version 1.0. | Provide data for their and their child's record. Receive generated invoices and notices. |

### 2.3 Operating Environment
*   **Software:** The application shall be developed using Microsoft ASP.NET technology. It shall be compatible with Internet Explorer and Netscape Navigator web browsers.
*   **Hardware:** A dedicated web server and database server capable of supporting the expected user load and data storage requirements.
*   **Network:** A standard TCP/IP network connection (LAN/Internet) for client-server communication.

### 2.4 Design and Implementation Constraints
1.  The system must be implemented as a web application.
2.  The backend must be compatible with Microsoft ASP.NET hosting environments.
3.  The database schema must be normalized to at least 3rd Normal Form (3NF) to ensure data integrity.
4.  The user interface must have a blue background color for all application windows as per stakeholder request.

### 2.5 Assumptions and Dependencies
*   **Assumption:** Center staff will have reliable access to computers with compatible web browsers.
*   **Assumption:** A system administrator will be available to perform initial user account setup and basic troubleshooting.
*   **Dependency:** The project is dependent on the availability of a suitable ASP.NET web server for deployment.
*   **Dependency:** Final requirements are dependent on stakeholder sign-off of this SRS.

## 3. System Features and Requirements

### 3.1 Functional Requirements

#### 3.1.1 User Authentication and Authorization (FUN-AUTH)
*   **FUN-AUTH-01:** The system shall require users to enter a unique username and a 6-8 character alphanumeric password to gain access.
*   **FUN-AUTH-02:** The system shall validate credentials against the `Employee` table and grant access only upon a successful match.
*   **FUN-AUTH-03:** The system shall determine the user's role (Admin, Teacher, Assistant) upon login and present a menu and functionalities appropriate to that role.
*   **FUN-AUTH-04:** The system shall implement an account lockout mechanism after 5 consecutive failed login attempts to mitigate brute-force attacks.
*   **FUN-AUTH-05:** The system shall provide a "Forgot Password" function. *[Undecided: Process may be manual (admin reset) or automated (email reset)].*
*   **FUN-AUTH-06:** The system shall implement a session timeout after a period of inactivity (e.g., 30 minutes). *[Undecided: Exact duration and user workflow impact to be determined].*

#### 3.1.2 Customer and Child Management (FUN-CCM)
*   **FUN-CCM-01:** An Administrator shall be able to create, read, update, and deactivate records in the `Customer` table.
*   **FUN-CCM-02:** An Administrator shall be able to create, read, update, and deactivate records in the `Child` table, linking each child to a primary `Customer`.
*   **FUN-CCM-03:** The system shall allow the upload and storage of a child's photograph linked to their `Child` record.
*   **FUN-CCM-04:** The system shall maintain a complete audit trail log for all edits made to Customer and Child account information. *[Undecided: Format and design of audit trail].*

#### 3.1.3 Enrollment and Classroom Management (FUN-ENRL)
*   **FUN-ENRL-01:** An Administrator shall be able to view a list of all `Classrooms`, including their `Name`, `Capacity` (max 20), current enrollment count, and assigned staff.
*   **FUN-ENRL-02:** When processing a new enrollment, the system shall allow the Administrator to check real-time availability against the classroom's `Capacity`.
*   **FUN-ENRL-03:** If a classroom is at capacity, the Administrator shall be able to place the child on a centralized waiting list.
*   **FUN-ENRL-04:** The waiting list shall support up to 100 entries.
*   **FUN-ENRL-05:** When a spot becomes available, the system shall notify the Administrator (via the reminder system or a dedicated alert) to facilitate contacting the next child on the waiting list.

#### 3.1.4 Daily Attendance and Check-in/out (FUN-ATT)
*   **FUN-ATT-01:** A Teaching Assistant shall be able to record a child's arrival time (check-in) for the current day.
*   **FUN-ATT-02:** A Teaching Assistant shall be able to record a child's departure time (check-out) for the current day.
*   **FUN-ATT-03:** The system shall automatically calculate the duration of care based on check-in and check-out times.
*   **FUN-ATT-04:** If a child's check-out time exceeds the center's official closing time, the system shall flag the record for late fee calculation (see FUN-BILL-03).

#### 3.1.5 Behavior and Immunization Tracking (FUN-TRACK)
*   **FUN-TRACK-01:** A Teacher shall be able to add, view, and edit behavioral comments and notes for any child in their assigned classroom(s). These notes shall be stored as part of the child's permanent record.
*   **FUN-TRACK-02:** An Administrator shall be able to define standard immunization types and schedules. *[Undecided: Exact method for schedule management].*
*   **FUN-TRACK-03:** The system shall allow authorized users to record immunizations for a child (`ImmunizationType`, `DateAdministered`, `DueDate`).
*   **FUN-TRACK-04:** The system shall be able to generate a list of children with immunizations due based on the `DueDate` field.

#### 3.1.6 Billing and Invoicing (FUN-BILL)
*   **FUN-BILL-01:** The system shall automatically initiate a monthly billing cycle at a configurable date (e.g., last day of the month).
*   **FUN-BILL-02:** The system shall calculate a base monthly fee for each enrolled child.
*   **FUN-BILL-03:** The system shall calculate applicable late pick-up fees based on attendance records flagged by FUN-ATT-04.
*   **FUN-BILL-04:** The system shall generate an `Invoice` for each `Customer`, aggregating fees for all their enrolled children and including a detailed breakdown of charges, including late fees.
*   **FUN-BILL-05:** Each generated invoice shall include a notice listing any upcoming or overdue immunizations for the customer's children.
*   **FUN-BILL-06:** An Administrator shall be able to view, print, and mark invoices as `Paid` or `Pending`.

#### 3.1.7 Reporting (FUN-REP)
*   **FUN-REP-01:** An Administrator shall be able to generate and print a preformatted Customer Directory report.
*   **FUN-REP-02:** An Administrator shall be able to generate and print a preformatted Immunization Due report.
*   **FUN-REP-03:** An Administrator shall be able to generate and print an Enrollment Summary report (showing children per classroom).
*   **FUN-REP-04:** An Administrator shall be able to generate and print a Billing Summary report for a given period.

#### 3.1.8 Reminder System (FUN-REM)
*   **FUN-REM-01:** Any employee shall be able to create a personal reminder with a description and a future date.
*   **FUN-REM-02:** Upon login on the specified date, the system shall display the reminder to the user via a pop-up notification. *[Undecided: Final implementation plan for the pop-up mechanism].*
*   **FUN-REM-03:** The system shall provide a calendar control for users to select the reminder date. *[Undecided: Specific control to be used].*

### 3.2 Non-Functional Requirements

#### 3.2.1 Usability (NF-US)
*   **NF-US-01:** The system shall present a consistent web-based interface across all modules.
*   **NF-US-02:** The background color of all application windows and primary containers shall be blue (#0000FF or similar approved shade).
*   **NF-US-03:** Common tasks (e.g., child check-in) shall be achievable in three clicks or fewer from the main menu.

#### 3.2.2 Performance (NF-PER)
*   **NF-PER-01:** The system shall respond to 95% of user requests (page loads, searches, saves) within 20 seconds under normal operational load.
*   **NF-PER-02:** The database shall be indexed to optimize query performance for key searches (child by name, customer lookup).

#### 3.2.3 Reliability & Supportability (NF-REL)
*   **NF-REL-01:** The system shall maintain an operational availability of 99% during core business hours (7:00 AM - 6:00 PM, weekdays).
*   **NF-REL-02:** The system shall reliably support the entry, storage, update, and deletion of all domain data (parent, child, employee, billing) without data corruption.
*   **NF-REL-03:** The system shall perform daily automated backups of the database.

#### 3.2.4 Security (NF-SEC)
*   **NF-SEC-01:** All user passwords shall be stored in the database using a strong, salted hashing algorithm (e.g., bcrypt, PBKDF2).
*   **NF-SEC-02:** User sessions shall be managed securely to prevent session hijacking.
*   **NF-SEC-03:** Direct database access shall be restricted to authorized system administrators only.

#### 3.2.5 Compatibility (NF-COM)
*   **NF-COM-01:** The client-side interface shall be compatible with Internet Explorer version 5.0 and above and Netscape Navigator version 7.0 and above.

## 4. Data Model

### 4.1 Conceptual Data Model
The core entities and their relationships are derived from the provided domain elements:
*   An **Employee** (Admin, Teacher, Assistant) authenticates to the system.
*   A **Customer** (Parent) has one or more **Children**.
*   A **Child** is assigned to one **Classroom**.
*   A **Classroom** has one primary Teacher and one Assistant (from the Employee pool), and a capacity of up to 20 Children.
*   A **Child** has zero or more **Immunization Records**.
*   A **Customer** receives one or more **Invoices** monthly.
*   **Attendance** records (implied entity) log check-in/out times for a Child on a given date.

### 4.2 Logical Data Model (Simplified Schema)
```sql
-- Core Tables as per provided elements
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    Username VARCHAR(50) UNIQUE NOT NULL,
    PasswordHash VARCHAR(255) NOT NULL, -- Hashed, not plain text
    Role VARCHAR(20) NOT NULL CHECK (Role IN ('Admin', 'Teacher', 'Assistant')),
    FirstName VARCHAR(50),
    LastName VARCHAR(50)
);

CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL,
    Address VARCHAR(255),
    HomePhone VARCHAR(20),
    EmergencyContact VARCHAR(255)
);

CREATE TABLE Classroom (
    ClassroomID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Capacity INT NOT NULL CHECK (Capacity <= 20),
    AssignedTeacherID INT FOREIGN KEY REFERENCES Employee(EmployeeID),
    AssistantID INT FOREIGN KEY REFERENCES Employee(EmployeeID)
);

CREATE TABLE Child (
    ChildID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Photo VARBINARY(MAX), -- Or a path to stored image
    ClassroomID INT FOREIGN KEY REFERENCES Classroom(ClassroomID),
    CustomerID INT NOT NULL FOREIGN KEY REFERENCES Customer(CustomerID)
);

CREATE TABLE ImmunizationRecord (
    RecordID INT PRIMARY KEY,
    ChildID INT NOT NULL FOREIGN KEY REFERENCES Child(ChildID),
    ImmunizationType VARCHAR(100) NOT NULL,
    DateAdministered DATE,
    DueDate DATE NOT NULL
);

CREATE TABLE Invoice (
    InvoiceID INT PRIMARY KEY,
    CustomerID INT NOT NULL FOREIGN KEY REFERENCES Customer(CustomerID),
    InvoiceDate DATE NOT NULL,
    TotalAmount DECIMAL(10, 2) NOT NULL,
    LateFeeDetails VARCHAR(500),
    Status VARCHAR(20) NOT NULL CHECK (Status IN ('Pending', 'Paid', 'Overdue'))
);

-- Additional implied table
CREATE TABLE Attendance (
    AttendanceID INT PRIMARY KEY,
    ChildID INT NOT NULL FOREIGN KEY REFERENCES Child(ChildID),
    AttendanceDate DATE NOT NULL DEFAULT GETDATE(),
    CheckInTime DATETIME,
    CheckOutTime DATETIME,
    LateFlag BIT DEFAULT 0
);

CREATE TABLE WaitingList (
    WaitlistID INT PRIMARY KEY,
    ChildFirstName VARCHAR(50),
    ChildLastName VARCHAR(50),
    DateOfBirth DATE,
    ParentName VARCHAR(100),
    ContactPhone VARCHAR(20),
    DateAdded DATE NOT NULL DEFAULT GETDATE(),
    Priority INT -- Could be used for ordering
);
```

## 5. Appendices

### 5.1 Undecided Issues & TBDs
1.  **Reminder Pop-up Implementation:** Determine if pop-ups are browser-native `alert()`, a custom modal within the application, or a dedicated dashboard widget.
2.  **Password Reset Process:** Decide between an automated email-based reset flow or a manual process where the Administrator resets and provides a temporary password.
3.  **Calendar Control:** Select a specific ASP.NET calendar control or JavaScript widget for date selection in reminders and other fields.
4.  **Immunization Schedule Management:** Define the UI and logic for Admins to create and edit standard immunization schedules (e.g., DTaP at 2, 4, 6 months).
5.  **Audit Trail Design:** Specify the table structure and level of detail (e.g., `AuditLogID`, `UserID`, `Timestamp`, `TableChanged`, `RecordID`, `OldValue`, `NewValue`).
6.  **Session Timeout Handling:** Finalize the timeout duration and user experience (e.g., warning message before timeout, redirect to login with saved form data?).

### 5.2 Risk Management Summary
| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| Scope Creep | Medium | High | Adhere to signed-off SRS. Manage change requests formally. Prioritize "High" requirements. |
| Performance Degradation | Medium | Medium | Implement database indexing from the start. Conduct load testing with realistic data volumes. |
| Security Vulnerabilities | Medium | High | Follow secure coding practices (hashed passwords, parameterized queries). Conduct security review. |
| User Resistance | High | Medium | Involve key users (Admin, Teacher) in UAT. Provide clear training materials and intuitive UI. |
| Billing Errors | Low | High | Develop detailed billing logic specs. Conduct thorough unit and integration testing on all billing scenarios. |

---
**Approval**

This Software Requirements Specification is hereby approved.

**Stakeholder Representative Signature:** _________________________
**Print Name:** _________________________ **Date:** _______________

**Development Lead Signature:** _________________________
**Print Name:** _________________________ **Date:** _______________