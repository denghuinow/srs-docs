# Software Requirements Specification (SRS)
## Child Care Center Management System (CCCMS)
**Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Child Care Center Management System (CCCMS). It is intended for use by the project stakeholders, including the development team, quality assurance, and the management of the child care center. This SRS serves as the primary reference for system design, implementation, and verification.

#### 1.2 Scope
The CCCMS is a web-based application designed to automate the administrative and operational tasks of a single child care center. The system will manage:
*   Child enrollment, classroom assignments, and waiting lists.
*   Daily attendance tracking for billing purposes.
*   Child records, including immunization dates and teacher comments.
*   Family account management and monthly invoice generation.
*   Standard administrative reporting.
*   User account management with role-based access control.
*   A personal daily reminders feature for staff.

**Out of Scope:**
*   Ensuring compliance with federal, state, or local licensing regulations.
*   Managing payroll, employee scheduling, or advanced financial accounting.
*   Providing interfaces to external business systems (e.g., state subsidy systems, accounting software).
*   Supporting multi-center or franchise operations.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **CCCMS:** Child Care Center Management System.
*   **Administrator:** A system user with full privileges to manage all data and functions.
*   **Teacher/Assistant:** A system user with privileges limited to attendance and child notes for assigned classrooms.
*   **ASP.NET:** A web application framework developed by Microsoft.
*   **UI:** User Interface.

#### 1.4 References
*   IEEE Std 830-1998: Recommended Practice for Software Requirements Specifications.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its users, and constraints. Section 3 details the specific functional requirements. Section 4 outlines the non-functional requirements, including performance, security, and technical constraints.

---

### 2. Overall Description

#### 2.1 Product Perspective
The CCCMS is a standalone, web-based client-server application. It will replace existing manual paper-based or spreadsheet-driven processes. The system consists of a web-based UI layer, an application logic layer, and a centralized database server. There are no specified interfaces to external systems.

#### 2.2 Product Functions
The core functions of the CCCMS are:
1.  **User Management:** Secure login and role-based access control.
2.  **Family & Child Management:** Create, read, update, and delete (CRUD) operations for family accounts and child profiles.
3.  **Enrollment & Classroom Management:** Assign children to classrooms based on age/capacity and manage a waiting list.
4.  **Attendance Tracking:** Record child arrival and departure times, with logic to flag late pickups.
5.  **Record Keeping:** Maintain child-specific data, including immunization schedules and daily teacher comments.
6.  **Billing & Invoicing:** Automatically calculate monthly fees based on attendance, apply discounts, and generate printable invoices.
7.  **Reporting:** Generate standard reports (customer directory, classroom enrollment, immunization due lists).
8.  **Staff Reminders:** Provide a personal dashboard for staff to view and manage daily reminders.

#### 2.3 User Characteristics
| User Class | Skill Level | Key Responsibilities |
| :--- | :--- | :--- |
| **Administrator** | High computer literacy. Understands center operations. | Full system configuration, user management, enrollment, billing, report generation. |
| **Teacher/Assistant** | Basic computer literacy. | Record daily attendance (check-in/out) for children in their classroom; add/view behavioral and developmental notes. |

#### 2.4 Constraints
*   **Technical:** The application must be built using ASP.NET technology and deployed on a compatible Microsoft web server.
*   **Browser Compatibility:** The UI must be compatible with Internet Explorer and Netscape Navigator.
*   **Architectural:** The system is designed for a single child care center only.

#### 2.5 Assumptions and Dependencies
*   It is assumed the child care facility maintains its own compliance with all relevant regulations; the system is a tool and does not guarantee compliance.
*   The system depends on a stable database server and network environment within the center.
*   Users are assumed to have access to a compatible web browser and basic training on the system.

---

### 3. Specific Requirements

#### 3.1 External Interface Requirements
**3.1.1 User Interfaces**
*   The system shall provide a consistent, intuitive web-based interface.
*   All data entry forms shall include appropriate validation and user feedback.
*   Navigation shall be logical and role-appropriate (e.g., teachers do not see billing menus).

**3.1.2 Hardware Interfaces**
*   The system requires a central database server and a web server capable of running ASP.NET applications.

**3.1.3 Software Interfaces**
*   **Database:** Microsoft SQL Server or equivalent relational database.
*   **Web Server:** Microsoft Internet Information Services (IIS) or equivalent supporting ASP.NET.

**3.1.4 Communications Interfaces**
*   Standard HTTP/HTTPS protocols for web browser communication.

#### 3.2 Functional Requirements
**3.2.1 User Authentication and Authorization (FR-01)**
*   **FR-01.1:** The system shall require users to authenticate with a unique username and a 6-8 character alphanumeric password.
*   **FR-01.2:** The system shall provide two primary user roles: Administrator and Teacher.
*   **FR-01.3:** Administrators shall have access to all system functions.
*   **FR-01.4:** Teachers shall only have access to: Attendance module for their assigned classroom(s) and Child Notes module for children in their classroom(s).

**3.2.2 Family and Child Management (FR-02)**
*   **FR-02.1:** The system shall allow Administrators to create, view, edit, and deactivate family accounts (including contact information, address, phone).
*   **FR-02.2:** The system shall allow Administrators to create, view, edit, and deactivate child records linked to a family account (including name, date of birth, medical/immunization data).
*   **FR-02.3:** The system shall maintain a history of a child's classroom assignments.

**3.2.3 Enrollment and Classroom Management (FR-03)**
*   **FR-03.1:** The system shall allow Administrators to define classrooms (name, age group, maximum capacity).
*   **FR-03.2:** The system shall allow Administrators to enroll a child in an available classroom, subject to capacity limits.
*   **FR-03.3:** The system shall automatically manage a waiting list when a classroom is at capacity, allowing Administrators to place children on the list and enroll them when space becomes available.

**3.2.4 Attendance Tracking (FR-04)**
*   **FR-04.1:** The system shall provide an interface for Teachers to record a child's daily check-in (arrival) and check-out (departure) time.
*   **FR-04.2:** The system shall calculate daily attendance hours based on check-in/out times.
*   **FR-04.3:** The system shall flag a pick-up as "late" if it occurs after a configurable daily closing time (e.g., 6:00 PM).

**3.2.5 Billing and Invoicing (FR-05)**
*   **FR-05.1:** The system shall allow Administrators to define billing rates (e.g., weekly fee, hourly late fee).
*   **FR-05.2:** The system shall allow Administrators to define discounts per family or child (e.g., sibling discount).
*   **FR-05.3:** At the end of a billing period (monthly), the system shall automatically generate an invoice for each family, calculating total fees based on attendance data and applying configured discounts and late fees.
*   **FR-05.4:** The system shall provide a printable view of each invoice.

**3.2.6 Reporting (FR-06)**
*   **FR-06.1:** The system shall generate and display a **Customer Directory Report** (family and child contact information).
*   **FR-06.2:** The system shall generate and display an **Enrollment Report** (list of children per classroom).
*   **FR-06.3:** The system shall generate and display an **Immunization Due Report** (list of children with upcoming or past-due immunization dates).

**3.2.7 Staff Reminders (FR-07)**
*   **FR-07.1:** The system shall provide each user with a personal dashboard.
*   **FR-07.2:** Users shall be able to create, view, and dismiss simple text-based reminders for themselves on their dashboard.

#### 3.3 Non-Functional Requirements

**3.3.1 Performance Requirements**
*   The system shall respond to any user action (page load, form submission, report generation) within **20 seconds** under normal operational load.

**3.3.2 Security Requirements**
*   All user passwords shall be stored in the database using industry-standard hashing (salted hash).
*   User sessions shall timeout after a period of inactivity (configurable, Medium/Low priority).
*   All system access shall occur over a secure network (HTTPS recommended for production).

**3.3.3 Software Quality Attributes**
*   **Usability:** The interface shall be intuitive for users with basic computer skills. Common tasks (e.g., marking attendance) shall require minimal clicks.
*   **Reliability:** The system shall maintain data integrity and be available during core business hours (7:00 AM - 7:00 PM).
*   **Maintainability:** The code shall be well-documented to allow for future modifications by developers familiar with ASP.NET.

**3.3.4 Technical Requirements**
*   The application shall be developed using **ASP.NET**.
*   The web interface shall be compatible with **Internet Explorer 5.0+** and **Netscape Navigator 7.0+**.

---

### 4. Appendices

#### 4.1 Priority and Acceptance
*   **High Priority (Mandatory for Acceptance):** All requirements in sections FR-01 through FR-06, and non-functional requirements 3.3.1, 3.3.2 (password hashing), and 3.3.4.
*   **Medium/Low Priority (May be deferred):** Specific UI features for reminders (FR-07), auto-logoff timing, advanced report filtering. These are desirable but not required for initial acceptance.
*   **Acceptance Approach:** The system will be accepted upon successful demonstration that it correctly implements all High Priority functional and non-functional requirements as specified in this document.

#### 4.2 Open Issues
*   The specific format and data fields for immunization records require further clarification with the client.
*   The mechanism for "configurable" daily closing time (FR-04.3) needs to be defined (global setting vs. per-classroom).