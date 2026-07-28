**Purpose & Scope**
The system automates the administrative and operational tasks of a child care center. It manages child enrollment, attendance, billing, immunizations, and reporting. It does not handle compliance with federal, state, or local licensing regulations.

**Product Background / Positioning**
This is a web-based management system intended to replace manual processes within a single child care center. It centralizes customer, child, and billing data to improve operational workflow and allow staff to focus more on child care.

**Core Functional Overview**
*   Manage child enrollment, classroom assignments, and a waiting list.
*   Record and track child arrival/departure times for billing late pickups.
*   Maintain child records, including immunization dates and teacher comments.
*   Generate and print monthly customer invoices with applicable discounts.
*   Produce standard administrative reports (e.g., customer directory, enrollment, immunizations).
*   Manage user accounts with role-based access privileges.
*   Provide a personal daily reminders feature for staff.

**Key Users & Usage Scenarios**
*   **Administrators:** Full system access. They enroll children, manage accounts, generate all reports and invoices, and configure system data.
*   **Teachers/Assistants:** Limited access. They record child attendance times and add/edit behavioral notes for the children they supervise.
*   **Typical Scenario:** An administrator checks classroom capacity, enrolls a new child, and creates a family account. Teachers log child attendance and notes daily. At month's end, administrators run reports and print invoices, which include immunization due notices.

**Major External Interfaces**
The system provides a web-based user interface accessible via standard browsers. It relies on a centralized database server. There are no specified interfaces to other external business systems.

**Key Non-functional Requirements**
*   The system must respond to all user requests within 20 seconds.
*   Users must authenticate with a unique username and a 6-8 character alphanumeric password.
*   The web interface must be compatible with Internet Explorer and Netscape Navigator.
*   The application must be built using ASP.NET technology.

**Constraints, Assumptions & Dependencies**
*   The software must be deployed on a web server supporting Microsoft ASP.NET.
*   It is assumed the child care facility is already compliant with all relevant regulations.
*   The system is designed for operation within a single center.

**Priorities & Acceptance Approach**
High-priority requirements are mandatory and include core functions like user roles, security login, child/parent record management, attendance tracking, billing, and key reports. Medium and Low priority features (e.g., specific reminder pop-ups, auto-logoff) may be deferred. Acceptance will be based on the system correctly implementing the specified high-priority functional and non-functional requirements.