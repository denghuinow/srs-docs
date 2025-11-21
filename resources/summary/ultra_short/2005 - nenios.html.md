**Purpose & Scope**  
Automates child care center operations including attendance tracking, billing, immunization management, and reporting. Excludes compliance with federal/state regulations and facility physical management.  

**Product Background / Positioning**  
Web-based solution for day care centers to streamline administrative tasks, replacing manual record-keeping. Integrates with existing center workflows but does not replace regulatory oversight systems.  

**Core Functional Overview**  
- Automated attendance tracking (arrival/departure times) with late-pickup billing.  
- Dynamic billing for single/multiple children and late fees ($10/hour per child).  
- Immunization tracking with due-date reminders and invoice notifications.  
- Customizable reports (enrollment, immunization history, billing).  
- Waiting list management for classroom openings (max 100 entries).  
- Daily reminders for staff with pop-up alerts.  

**Key Users & Usage Scenarios**  
Administrators: Full access to accounts, billing, reports, and waiting lists. Teachers/assistants: Limited to attendance, child comments, and personal reminders. Scenarios: Enrolling children, processing monthly invoices, tracking immunizations.  

**Major External Interfaces**  
Web-based interface accessible via Internet Explorer/Netscape Navigator. Centralized database for data sharing; no external system integrations specified.  

**Key Non-functional Requirements**  
System response time ≤20 seconds per user request. Passwords must be 6–8 alphanumeric characters. Session timeout after 10 minutes of inactivity.  

**Constraints, Assumptions & Dependencies**  
Requires ASP.NET-compatible web server. Maximum 20 children per classroom. Parent/child data storage limited to specified fields (e.g., immunization dates, emergency contacts).  

**Priorities & Acceptance Approach**  
High-priority features: Billing rules (R23–R25), immunization tracking (R18–R22), security (R7, R10). Acceptance requires all high-priority requirements met; low-priority items (e.g., UI color) may be deferred.