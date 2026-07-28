# Software Requirements Specification (SRS)
## Child Care Center Management System (CCCMS)
**Version:** 1.0  
**Date:** October 26, 2023  
**Prepared for:** Child Care Center Stakeholders  
**Prepared by:** [Your Company/Team Name]

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Child Care Center Management System (CCCMS). The purpose of this system is to provide a centralized, web-based platform to manage the daily administrative operations of a child care center, thereby improving efficiency, accuracy, and customer service.

#### 1.2 Document Conventions
This SRS follows the IEEE 830-1998 standard. Requirements are uniquely identified with tags (e.g., **FR-001**, **NFR-001**). Priority levels are indicated as:
*   **High (H):** Essential for core functionality and release.
*   **Medium (M):** Important but can be deferred if necessary.
*   **Low (L):** Desirable enhancement.

#### 1.3 Intended Audience and Reading Suggestions
*   **Project Sponsors & Management:** Focus on Sections 1 (Introduction), 2 (Overall Description), and 5 (External Interface Requirements) for project scope and high-level capabilities.
*   **Developers & QA Engineers:** Focus on Sections 3 (System Features) and 4 (Non-Functional Requirements) for detailed specifications.
*   **End-Users (Center Staff):** Focus on Section 3 (System Features) to understand system functionality.

#### 1.4 Project Scope
The CCCMS will be a comprehensive web application that automates and streamlines the management of child and parent accounts, daily attendance tracking, automated billing with late-pickup fee calculation, and generation of standard operational reports. The system will replace manual, paper-based, or disparate spreadsheet processes.

**In-Scope:**
*   Child and family information management.
*   Enrollment process and waiting list management.
*   Daily check-in/check-out with time tracking.
*   Automated invoice generation and billing.
*   Standard report generation.
*   User role-based access (Administrator, Staff).

**Out-of-Scope:**
*   Real-time video monitoring of classrooms.
*   Parent-facing portal for payments or communication (Phase 2 consideration).
*   Payroll or employee scheduling for staff.
*   Meal planning or nutritional tracking.

#### 1.5 References
*   IEEE Std 830-1998, IEEE Recommended Practice for Software Requirements Specifications.

### 2. Overall Description

#### 2.1 Product Perspective
The CCCMS is a new, standalone web application. It will interact with a backend Microsoft SQL Server database. It must be accessible from standard web browsers within the center's network or via secure internet access.

#### 2.2 Product Functions (Summary)
1.  **Family & Child Management:** Maintain demographic data, contact information, medical/immunization records, and authorized pickup lists.
2.  **Enrollment & Waitlist Management:** Handle application intake, class assignment, and manage a prioritized waiting list.
3.  **Attendance Tracking:** Record daily arrival and departure times using a simple staff interface.
4.  **Billing & Invoicing:** Automatically calculate monthly tuition and applicable late-pickup fees, generating itemized invoices.
5.  **Reporting:** Produce standard reports for operational and compliance needs.

#### 2.3 User Classes and Characteristics
*   **Administrator:** Full system access. Manages all data, user accounts, system configuration (e.g., fee schedules), and generates all reports. Computer-literate.
*   **Center Staff (Teachers/Caregivers):** Primary users for daily check-in/check-out. Limited access to child profiles (allergies, pickup auth) and basic attendance views. Variable computer proficiency.

#### 2.4 Operating Environment
*   **Software:**
    *   **Server:** Microsoft Windows Server, Internet Information Services (IIS), Microsoft .NET Framework, ASP.NET.
    *   **Database:** Microsoft SQL Server.
    *   **Client:** Web browsers: Microsoft Internet Explorer 5.5+ and Netscape Navigator 7.0+. (See NFR-001)
*   **Hardware:** Standard web server and database server specifications to support expected user load (approx. 10-20 concurrent users).

#### 2.5 Design and Implementation Constraints
1.  **C-001:** The application must be developed using **Microsoft ASP.NET** technology.
2.  **C-002:** The database must be **Microsoft SQL Server**.
3.  **C-003:** The user interface must be compatible with the specified legacy browsers (Internet Explorer, Netscape Navigator), limiting the use of modern JavaScript frameworks.

#### 2.6 Assumptions and Dependencies
*   Assumes center staff have reliable internet/intranet access.
*   Assumes a system administrator will be trained to manage user accounts and basic configurations.
*   Dependent on accurate and timely data entry by staff for attendance and billing accuracy.

### 3. System Features

#### 3.1 Feature 1: Family and Child Management
**Description:** This feature allows administrators to create and maintain comprehensive records for families and children.

**Priority:** High

**Requirements:**
*   **FR-001 (H):** The system shall allow an Administrator to create a new family account, capturing parent/guardian names, addresses, phone numbers, and email addresses.
*   **FR-002 (H):** The system shall allow an Administrator to add one or more children to a family account, capturing child's name, date of birth, enrollment date, assigned classroom, and medical notes/allergies.
*   **FR-003 (H):** The system shall allow an Administrator to maintain a list of authorized individuals for picking up each child, including their name, relation, and contact phone.
*   **FR-004 (M):** The system shall allow an Administrator to record and track immunization records and expiration dates for each child.

#### 3.2 Feature 2: Enrollment and Waitlist Management
**Description:** This feature manages the process from initial inquiry to active enrollment, including handling overflow via a waitlist.

**Priority:** High

**Requirements:**
*   **FR-005 (H):** The system shall allow an Administrator to create a prospective child/family record from an inquiry.
*   **FR-006 (H):** The system shall allow an Administrator to formally enroll a prospective child into an available slot in a specific classroom.
*   **FR-007 (H):** The system shall maintain a centralized waiting list. When a slot becomes available, the Administrator shall be able to view and contact the next eligible family on the list.
*   **FR-008 (M):** The system shall allow prioritization of the waitlist (e.g., by application date, sibling priority).

#### 3.3 Feature 3: Daily Attendance Tracking
**Description:** This feature allows staff to quickly record child arrival and departure times, which forms the basis for billing.

**Priority:** High

**Requirements:**
*   **FR-009 (H):** The system shall provide a Staff user with a simple, daily view (e.g., by classroom) to mark a child's check-in time (defaulting to current time).
*   **FR-010 (H):** The system shall provide a Staff user with a simple, daily view to mark a child's check-out time (defaulting to current time).
*   **FR-011 (H):** The system shall calculate the total hours present for each child each day based on check-in/check-out times.
*   **FR-012 (H):** The system shall flag a check-out that occurs after the child's scheduled pickup time.

#### 3.4 Feature 4: Billing and Invoicing
**Description:** This feature automates the generation of monthly invoices, incorporating base tuition and calculated late fees.

**Priority:** High

**Requirements:**
*   **FR-013 (H):** The system shall allow an Administrator to define billing schedules (e.g., monthly flat rate) and late-pickup fee rules (e.g., $1 per minute after 6:00 PM).
*   **FR-014 (H):** The system shall automatically generate a monthly invoice for each family, calculating total charges based on:
    *   Enrolled child(ren) monthly tuition.
    *   Sum of late-pickup fees incurred during the billing period.
*   **FR-015 (H):** The system shall allow an Administrator to view, print, and mark invoices as "Sent" and "Paid."

#### 3.5 Feature 5: Reporting
**Description:** This feature provides pre-defined reports for operational and regulatory compliance.

**Priority:** Medium

**Requirements:**
*   **FR-016 (M):** The system shall generate an **Enrollment Report** listing all currently enrolled children, their classroom, and emergency contacts.
*   **FR-017 (M):** The system shall generate an **Immunization Report** listing children with upcoming or expired immunizations.
*   **FR-018 (M):** The system shall generate a **Customer Information Directory** report with family and child details for internal use.

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
*   **NFR-001:** The system shall respond to **all user requests** (page loads, form submissions, report generation) within **20 seconds** under normal operating conditions.
*   **NFR-002:** The attendance check-in/check-out interface for Staff shall be optimized for speed, targeting sub-3-second response times for update actions.

#### 4.2 Usability Requirements
*   **NFR-003:** The interface for Staff users (attendance) shall require minimal training (<30 minutes) and no more than 3 clicks to perform a check-in/check-out.
*   **NFR-004:** All error messages shall be clear and instruct the user on corrective action.

#### 4.3 Reliability & Availability
*   **NFR-005:** The system shall be available for use during center operating hours (6:00 AM - 8:00 PM, Monday-Friday), targeting 98% uptime.

#### 4.4 Security Requirements
*   **NFR-006:** Access shall require username and password authentication.
*   **NFR-007:** User roles (Administrator, Staff) shall enforce feature-level authorization (e.g., Staff cannot generate invoices or modify family data).

#### 4.5 Browser Compatibility
*   **NFR-008:** The application shall be fully functional and render correctly on **Microsoft Internet Explorer 5.5 and later** and **Netscape Navigator 7.0 and later**.

### 5. External Interface Requirements

#### 5.1 User Interfaces
*   The UI shall be clean, professional, and use a consistent layout and navigation scheme.
*   Primary navigation will be via a top menu bar for Administrators and a simplified task-oriented menu for Staff.

#### 5.2 Hardware Interfaces
*   None specified beyond standard client/server web architecture.

#### 5.3 Software Interfaces
*   **Database:** The application shall interface with a Microsoft SQL Server database via ADO.NET.

#### 5.4 Communications Interfaces
*   The application shall use HTTP/HTTPS over TCP/IP for client-server communication.

---

### Appendix A: Glossary

| Term | Definition |
| :--- | :--- |
| **Authorized Pickup** | An individual, other than the primary parent/guardian, who is permitted to sign out and take a child from the center. |
| **Late-Pickup Fee** | A monetary charge applied when a child is checked out after their officially scheduled pickup time. |
| **Prospective Child** | A child who has inquired or applied for enrollment but has not yet been assigned a slot. |
| **Scheduled Pickup Time** | The contracted time by which a specific child must be picked up daily, as recorded in their enrollment agreement. |

### Appendix B: To Be Determined (TBD)
*   Specific fee structures and calculation formulas.
*   Detailed report formats and column definitions.
*   Backup and disaster recovery procedures.