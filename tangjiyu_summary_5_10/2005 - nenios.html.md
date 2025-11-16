# Neños Child Care Center - Software Requirements Specification

## 1. Introduction

### 1.1 Goals and Objectives
The Neños Child Care Management (NCCM) software is a web-based solution designed to automate typical child care center functions, improving operational workflow. The system will assist in managing a child care center by automating activities such as tracking child immunizations, maintaining classroom waiting lists, processing invoices, and printing customer reports. This will allow employees to spend more time caring for children while minimizing administrative document creation time.

### 1.2 Statement of Scope
The system requires user authentication with username and password, with access privileges determined by job classification:
- Administrators: Unlimited access to view/edit all account information, generate reports, and print invoices
- Teachers and Assistants: Limited access to enter/edit child comments and child arrival/departure times, use daily reminders

Key functionalities include:
- Customer account management (registration, editing)
- Classroom management (availability checking, waiting lists)
- Child attendance tracking (arrival/departure times, late pick-up billing)
- Authorized pick-up person management
- Teacher behavior documentation
- Reporting features (preformatted documents, customer reports)
- Daily reminders for employees
- Immunization tracking with notifications
- Billing and invoicing with automated calculations

### 1.3 Software Context
The NCCM system is designed to help day care facilities manage operations efficiently while remaining compliant with regulations. It addresses parent concerns about child-focused staff, individual attention, age-appropriate activities, and special events. The software aims to professionalize day care home facilities and support business growth through improved management capabilities.

### 1.4 Major Constraints
The system will use Microsoft's ASP.NET technology, requiring a web server that supports this technology.

## 2. Functional Requirements

### 2.1 Access Privileges
- Two access levels: administrators and teachers/assistants
- Teachers/assistants limited to child comments and attendance tracking
- Administrators have full data access and reporting capabilities
- Only administrators can view/print reports and invoices
- All employees can use daily reminders

### 2.2 Security
- Unique username and password required for each user
- Password requirements: 6-8 alphanumeric characters
- Account lockout after 3 unsuccessful password attempts
- Automatic logout after 10 minutes of inactivity
- Username format: first 4 characters of last name + first 3 of first name

### 2.3 Daily Reminders
- Employee-specific reminders only
- Date selection from calendar
- Up to 50-character reminder messages
- Popup notification on login when reminder date arrives

### 2.4 Immunizations
- Child records must contain immunization dates
- Two-week advance notifications for upcoming immunizations
- Child records include last physical examination date
- Immunization notifications printed on monthly invoices

### 2.5 Billing
- Single child: $90/month
- Two children: $157.50/month
- Three+ children: $157.50 for first two + $45 each additional
- Late pickup billing: $10/hour per child
- Account history tracking all activity by date
- Itemized invoices available for printing
- Monthly invoice generation

### 2.6 Reports
Required reports include:
- Customer Directory (alphabetical by last name with contact info)
- Daily Classroom & Center Enrollment (present/absent status)
- Birthday Lists & Child Age
- Parent/Child Cross Reference
- Family Registration Information
- Immunization Due & History
- Child Enrollment/Withdrawal
- Child Notes & Comments
- Account Activity

### 2.7 Account Information
- Parent records: name, address, home/work phone, email, emergency contact, authorized pickup
- Child records: name, date of birth, gender, classroom, special needs, photo, teacher comments, immunization dates
- Change logging with user ID, date, time, and description
- Support for entering, storing, and updating all information

### 2.8 Classroom Management
- Maximum 20 children per classroom
- One student per class assignment
- One teacher and one assistant per class
- Waiting list for up to 100 potential customers

### 2.9 User Interface
- Web-based interface compatible with Internet Explorer and Netscape Navigator
- Blue background color for all windows
- System response time within 20 seconds

## 3. Priority Requirements

### 3.1 High Priority (Must Implement)
- Access level differentiation
- Security authentication
- Immunization tracking
- Billing calculations
- Report generation
- Account information management
- Classroom capacity limits
- Web-based interface

### 3.2 Medium Priority (Implementation Determined During Development)
- User change logging
- Immunization scheduling
- Employee-specific reminders only
- Calendar date selection
- System timeout

### 3.3 Low Priority (May Be Eliminated for Schedule)
- Specific username format
- Password reset functionality
- System timeout
- Calendar date selection
- Popup reminder notifications

## 4. Technical Requirements

### 4.1 Platform
- Web-based solution using Microsoft ASP.NET
- Browser compatibility: Internet Explorer and Netscape Navigator
- Centralized database connected to internet for information sharing

## 5. References
- US Census 2000 data
- Dun & Bradstreet Industry Report: Child Care Services
- Department of Children and Family Services statistics
