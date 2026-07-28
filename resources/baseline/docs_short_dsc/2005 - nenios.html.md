# Software Requirements Specification (SRS)
## For
### Neñios Child Care Management (NCCM) Software
**Version:** 1.0  
**Date:** [Date of Document Creation]  
**Prepared for:** Neñios Child Care Center  
**Prepared by:** Code Works Development Team

---

## Table of Contents
1. [Introduction](#1-introduction)
2. [Overall Description](#2-overall-description)
3. [System Features and Requirements](#3-system-features-and-requirements)
4. [External Interface Requirements](#4-external-interface-requirements)
5. [Non-Functional Requirements](#5-non-functional-requirements)
6. [Other Requirements](#6-other-requirements)
7. [Appendix](#7-appendix)

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the Neñios Child Care Management (NCCM) software. It serves as a formal agreement between the stakeholders (Neñios Child Care Center) and the development team (Code Works) regarding the system's capabilities, constraints, and deliverables. The intended audience includes project managers, developers, testers, and the care center's administrative staff.

### 1.2 Document Conventions
- Requirements are categorized as Functional (FR) or Non-Functional (NFR).
- Priority is indicated as High (H), Medium (M), or Low (L).
- All user interface screens shall have a blue background, as per a major constraint.

### 1.3 Project Scope
The NCCM is a centralized, web-based management system designed to automate the core administrative and operational workflows of a child care center. Its primary goal is to reduce time spent on manual tasks, allowing staff to focus more on child care.

#### 1.3.1 In Scope
- Role-based user authentication and authorization.
- Comprehensive management of child, parent, and staff accounts.
- Tracking of child immunizations, daily attendance, and authorized pickups.
- Billing and invoicing engine supporting late fees and multi-child discounts.
- Generation of predefined operational and compliance reports.
- Functionality for employees to set and manage daily reminders.
- System-generated notifications for upcoming immunizations.

#### 1.3.2 Out of Scope
- Ensuring compliance with specific Federal, State, or Local daycare licensing rules.
- Providing direct system access (portal) for parents/guardians.
- Integration with third-party accounting (e.g., QuickBooks) or financial software.
- Development of a native mobile application or offline functionality.
- Implementation of advanced data analytics, machine learning, or predictive business intelligence features.

### 1.4 References
- Project Charter: "Neñios Child Care Center Management Software"
- Stakeholder Interview Notes

## 2. Overall Description

### 2.1 Product Perspective
The NCCM is a new, standalone web application. It will replace existing manual processes (paper-based records, spreadsheets) and serve as the single source of truth for child care center operations. It must interface with a compatible web server and database (implied by ASP.NET).

### 2.2 Product Functions (Summary)
1. **User Management:** Secure login and role-based access control.
2. **Child & Family Management:** Maintain profiles, emergency contacts, immunization records, and authorized pickup lists.
3. **Classroom & Enrollment Management:** Track classroom capacity (max 20 children), manage enrollments, and maintain waiting lists.
4. **Attendance Tracking:** Record child arrival/departure times and flag late pickups.
5. **Behavioral Documentation:** Allow teachers to record notes and observations for parent-teacher conferences.
6. **Billing & Invoicing:** Automatically generate monthly invoices, apply discounts and late fees, and include immunization notices.
7. **Reporting:** Generate standard reports (customer directory, immunization due lists, attendance summaries).
8. **Notifications & Reminders:** System alerts for immunizations and user-defined daily task reminders.

### 2.3 User Classes and Characteristics
| User Class | Key Characteristics | Primary Responsibilities |
| :--- | :--- | :--- |
| **Administrator** | Full system access. Technically proficient. | Manage all data (children, parents, staff, classrooms). Run billing and generate reports. Oversee system configuration. |
| **Teacher** | Regular user. Focused on child development. | Document child behavior and daily comments. May view classroom rosters and child profiles. |
| **Teaching Assistant** | Regular user. Focused on logistics. | Record child arrival/departure times. Track late pickups. |
| **Parent/Customer** | External stakeholder. No direct system login. | Provides information during enrollment. Receives invoices and notices externally. |
| **Care Center Management** | Viewer/Reviewer. | Uses generated reports for operational oversight and decision-making. |

### 2.4 Operating Environment
- **Software:** Microsoft ASP.NET web application. Must be hosted on a compatible Microsoft IIS web server with a supporting database (e.g., Microsoft SQL Server).
- **Client Browsers:** Must be compatible with Internet Explorer and Netscape Navigator.
- **Network:** Standard internet/intranet connectivity.

### 2.5 Design and Implementation Constraints
1. **Technical:** Development must be done using Microsoft ASP.NET.
2. **Browser Compatibility:** The application must function correctly on Internet Explorer and Netscape Navigator.
3. **Business Rule:** Each classroom has a strict maximum capacity of 20 children.
4. **Security:** Passwords must be 6–8 alphanumeric characters. The system must implement security measures after failed login attempts (e.g., account lockout after 5 attempts).
5. **UI/UX:** All application windows must have a blue background.

### 2.6 Assumptions and Dependencies
- Assumption: Care center staff have reliable access to a computer with a compatible web browser.
- Assumption: A suitable server environment for hosting an ASP.NET application is available.
- Dependency: The project timeline and budget are dependent on the availability of stakeholder feedback during review cycles.

## 3. System Features and Requirements

### 3.1 Feature 1: User Authentication & Authorization (FR-01)
**Priority:** High
**Description:** The system shall provide secure login and enforce role-based permissions.
**Requirements:**
- FR-01.1: The system shall require a unique username and a 6-8 character alphanumeric password for authentication.
- FR-01.2: The system shall lock a user account after 5 consecutive failed login attempts.
- FR-01.3: The system shall present different menus and functional capabilities based on user roles (Administrator, Teacher, Teaching Assistant).
- FR-01.4: User sessions shall be maintained securely until explicit logout.

### 3.2 Feature 2: Child & Family Management (FR-02)
**Priority:** High
**Description:** The system shall maintain a centralized database of children, their parents/guardians, and related information.
**Requirements:**
- FR-02.1: The system shall allow administrators to create, read, update, and deactivate child profiles (including name, DOB, medical notes, photo).
- FR-02.2: The system shall link child profiles to one or more parent/guardian profiles (including contact info, address).
- FR-02.3: The system shall maintain a list of authorized individuals for child pickup for each child.
- FR-02.4: The system shall record and track immunization records (type, date administered, next due date).

### 3.3 Feature 3: Classroom & Enrollment Management (FR-03)
**Priority:** High
**Description:** The system shall manage classroom assignments, capacity, and waiting lists.
**Requirements:**
- FR-03.1: The system shall enforce a maximum capacity of 20 children per classroom.
- FR-03.2: The system shall allow administrators to check real-time availability for any classroom.
- FR-03.3: The system shall allow administrators to enroll a child in an available classroom.
- FR-03.4: The system shall maintain a waiting list for fully occupied classrooms and allow administrators to manage it (add, remove, promote).

### 3.4 Feature 4: Daily Attendance & Pickup Tracking (FR-04)
**Priority:** High
**Description:** The system shall record child check-in/check-out times and identify late pickups.
**Requirements:**
- FR-04.1: The system shall allow Teaching Assistants (or authorized roles) to record a child's arrival time.
- FR-04.2: The system shall allow Teaching Assistants to record a child's departure time and select the authorized pickup person from the list.
- FR-04.3: The system shall automatically flag a departure as a "late pickup" if it occurs after the child's scheduled departure time.
- FR-04.4: The system shall make late pickup data available to the billing module.

### 3.5 Feature 5: Child Behavior & Notes (FR-05)
**Priority:** Medium
**Description:** The system shall allow teachers to document observations for use in parent-teacher conferences.
**Requirements:**
- FR-05.1: The system shall allow Teachers to add, edit, and view behavior comments linked to a specific child and date.
- FR-05.2: The system shall allow Teachers to generate a simple report of comments for a specific child over a date range.

### 3.6 Feature 6: Billing & Invoicing (FR-06)
**Priority:** High
**Description:** The system shall automate the generation of monthly invoices, applying relevant fees and discounts.
**Requirements:**
- FR-06.1: The system shall allow administrators to generate invoices for all enrolled children on a monthly basis.
- FR-06.2: The system shall automatically apply a configured multi-child discount for families with more than one enrolled child.
- FR-06.3: The system shall automatically add a late fee for recorded late pickups, based on a configurable rate.
- FR-06.4: Generated invoices shall include a standard notice about upcoming or overdue immunizations for that child.
- FR-06.5: Invoices shall be printable in a clear, standard format.

### 3.7 Feature 7: Reporting (FR-07)
**Priority:** High
**Description:** The system shall generate predefined reports for administrative use.
**Requirements:**
- FR-07.1: The system shall generate a Customer Directory report listing all active parents/guardians and their children.
- FR-07.2: The system shall generate an Immunization Due Report listing children with immunizations due within a user-specified timeframe (e.g., next 30 days).
- FR-07.3: All reports shall be viewable on-screen and printable.

### 3.8 Feature 8: Reminders & Notifications (FR-08)
**Priority:** Medium
**Description:** The system shall provide tools for personal reminders and system-generated alerts.
**Requirements:**
- FR-08.1: The system shall allow any employee to create, view, and dismiss daily task reminders for themselves.
- FR-08.2: The system shall provide administrators with a dashboard or list view of children with immunizations due soon (triggered by the Immunization Due Report logic).

## 4. External Interface Requirements

### 4.1 User Interfaces
- **UI Constraint:** All application windows/screens must have a blue background.
- **Style:** Professional, clear, and intuitive layout appropriate for a business web application.
- **Browser Support:** The interface must render and function correctly in Internet Explorer and Netscape Navigator.

### 4.2 Hardware Interfaces
None specified. The system is a standard web application accessible via supported browsers.

### 4.3 Software Interfaces
- **Web Server:** Must interface with Microsoft Internet Information Services (IIS) for ASP.NET hosting.
- **Database:** Must interface with a relational database management system (e.g., Microsoft SQL Server) for persistent data storage.

### 4.4 Communications Interfaces
Standard HTTP/HTTPS protocols for web communication.

## 5. Non-Functional Requirements

### 5.1 Performance Requirements (NFR-P)
- NFR-P1: The system shall respond to any user request within **20 seconds** under normal operating conditions.
- NFR-P2: Report generation for standard lists (e.g., Customer Directory for up to 200 families) shall complete within 15 seconds.

### 5.2 Security Requirements (NFR-S)
- NFR-S1: All passwords shall be stored in an encrypted/hashed format.
- NFR-S2: User access shall be strictly controlled by role-based permissions.
- NFR-S3: User sessions shall be managed securely to prevent hijacking.

### 5.3 Usability Requirements (NFR-U)
- NFR-U1: Administrative staff shall be able to generate a monthly invoice run for all customers with less than 5 minutes of effort after a one-hour training session.
- NFR-U2: Teaching Assistants shall be able to record the arrival of a child in 3 clicks or less.

### 5.4 Success Metrics
- Reduction in time spent by administrators on manual billing and report generation by at least 50%.
- 100% accuracy in the application of multi-child discounts and late fees on generated invoices.
- All predefined reports are generated successfully and contain correct, up-to-date information.

## 6. Other Requirements

### 6.1 Undecided Issues / Open Questions
The following items require further stakeholder discussion and clarification:
1. The implementation priority and specifics of an automatic logoff feature after a period (e.g., 10 minutes) of inactivity.
2. The specific design and control type (e.g., pop-up calendar, dropdowns) for the date picker in the daily reminders feature.
3. The ability for administrators to configure immunization types and standard schedules within the system.
4. The business rules and system handling for parent referral discounts.
5. The detailed workflow and security protocol for users resetting a forgotten password (e.g., email reset, security questions, administrator intervention).

## 7. Appendix

### 7.1 Glossary
- **NCCM:** Neñios Child Care Management software.
- **Authorized Pickup:** An individual, other than a parent/guardian, who is permitted to collect a child from the center.
- **Late Pickup:** A child who is picked up after their contractually agreed-upon daily departure time.

### 7.2 Core Use Cases (Expanded Reference)
1. **UC-01: Enroll New Child & Manage Waiting List** (Actor: Administrator)
2. **UC-02: Record Child Arrival/Departure** (Actor: Teaching Assistant)
3. **UC-03: Document Child Behavior** (Actor: Teacher)
4. **UC-04: Generate Monthly Invoices** (Actor: Administrator)
5. **UC-05: Set Daily Reminder** (Actor: Any Employee)
6. **UC-06: View Immunization Due Report** (Actor: Administrator)

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor (Neñios) | | | |
| Lead Developer (Code Works) | | | |
| Project Manager | | | |