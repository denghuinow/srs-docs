# Software Requirements Specification (SRS)
## System Administration Module for an Integrated Library System (ILS)

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review
**Project:** Integrated Library System (ILS) - Administration Module

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the System Administration Module of a large-scale Integrated Library System (ILS). It is intended for use by the project stakeholders, including library directors, managers, system administrators, development teams, and quality assurance personnel, to ensure a common understanding of the system's capabilities and constraints.

#### 1.2 Scope
The System Administration Module provides centralized management, configuration, monitoring, and control for all aspects of the ILS. It supports a multi-branch library environment with real-time transaction processing and robust data management. The module's scope encompasses:
*   Server, database, and application monitoring and alerting.
*   Management of user accounts (staff and patron) and security privileges.
*   Centralized configuration of business rules and system parameters.
*   Data backup, recovery, and integrity management.
*   Client software deployment and update management.
*   Report generation, customization, and scheduling.
*   Administration of system-level functions such as record locks and transaction logs.

This specification presupposes the existence of core ILS data structures and functionality (e.g., bibliographic, item, and patron data models) provided by other modules (Cataloging, Circulation, OPAC).

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **API:** Application Programming Interface
*   **ILS:** Integrated Library System
*   **KPI:** Key Performance Indicator
*   **MARC:** Machine-Readable Cataloging
*   **NCIP:** NISO Circulation Interchange Protocol
*   **ODBC:** Open Database Connectivity
*   **OPAC:** Online Public Access Catalog
*   **SIP2:** Standard Interchange Protocol v2
*   **SQL:** Structured Query Language
*   **SFTP:** SSH File Transfer Protocol
*   **SSL:** Secure Sockets Layer
*   **SSH:** Secure Shell

#### 1.4 References
*   Project Charter: ILS Modernization Initiative
*   SRS for Acquisitions Module
*   SRS for Cataloging Module
*   SRS for OPAC/Patron Interface Module

#### 1.5 Overview
The remainder of this document is structured as follows:
*   **Section 2:** Overall Description - Provides context, user characteristics, and constraints.
*   **Section 3:** Specific Requirements - Details functional requirements, data models, and non-functional requirements.
*   **Appendices:** Include supplementary information such as user story mappings.

### 2. Overall Description

#### 2.1 Product Perspective
The System Administration Module is a core component of the new ILS, replacing legacy administration tools. It interfaces directly with:
*   **Other ILS Modules:** For applying configuration rules and retrieving operational data.
*   **Database Backend:** For direct management, backup, and monitoring.
*   **Server OS:** For resource monitoring and shell access.
*   **External Systems:** Via APIs/SFTP for vendor data interchange.
*   **Client Workstations:** For software deployment and management.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **System Administrator** | Technical IT staff. Deep knowledge of servers, networks, and databases. | Proactive monitoring, automated maintenance, secure access, client management. |
| **Staff (Librarians/Technicians)** | Primary daily users of the ILS. Varied technical proficiency. | Efficient record editing, conflict-free collaboration, customizable reports. |
| **Managers / Library Managers** | Supervisory role. Focus on metrics and service delivery. | Performance dashboards, configurable reports, oversight of rules affecting service. |
| **Library Directors** | Strategic role. Minimal direct system use. | High-level system health and usage reports. |
| **Patrons** | End-customers. Access via OPAC. | Not direct users of this module, but affected by its configuration (loan rules, blocks). |

#### 2.3 Operating Environment
*   **Server:** Linux (primary) or Solaris operating systems.
*   **Client Access:** Accessible via modern web browsers **and/or** a dedicated Windows-compatible client application (TBD).
*   **Database:** A fully relational SQL-based RDBMS (e.g., PostgreSQL, Oracle) with ODBC support.
*   **Network:** Must support secure internal and external communications over SSL/TLS, SSH, and SFTP.

#### 2.4 Design and Implementation Constraints
1.  Must integrate with existing ILS module data structures without requiring major schema changes.
2.  Must support real-time, concurrent processing for high-volume transactions (20M+ circulations annually).
3.  Must comply with library accessibility standards (e.g., WCAG), ensuring compatibility with screen readers.
4.  Must provide command-line (root shell) and file-level access for advanced administrative tasks.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** Other ILS module SRS documents will be finalized, providing stable interface definitions.
*   **Assumption:** A collaborative development environment with user prototyping will be established.
*   **Dependency:** Successful integration with the core Cataloging and Acquisitions modules.
*   **Dependency:** Availability of external vendor API specifications for data interchange.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 System Monitoring & Alerting (SYS-MON)
*   **SYS-MON-1:** The system shall provide a real-time dashboard displaying key server metrics (CPU, memory, disk I/O, database connections).
*   **SYS-MON-2:** The system shall allow administrators to set configurable thresholds for all monitored metrics.
*   **SYS-MON-3:** The system shall generate alerts via dashboard notification, email, and/or SMS when a threshold is breached.
*   **SYS-MON-4:** The system shall maintain a searchable log of all alerts and system events.

##### 3.1.2 User Account Management (USR-MGT)
*   **USR-MGT-1:** The system shall provide consoles for creating, modifying, and disabling staff and patron accounts.
*   **USR-MGT-2:** The system shall support the use of configurable account templates based on staff role (e.g., Librarian, Technician).
*   **USR-MGT-3:** The system shall allow assignment of privileges to individual accounts or workgroups with granularity down to specific functions (e.g., "Can waive fines > $5").
*   **USR-MGT-4:** The system shall log all account creation and modification events in the Transaction Log.

##### 3.1.3 Configuration & Business Rule Management (CFG-MGT)
*   **CFG-MGT-1:** The system shall provide a dedicated console for viewing and editing centralized configuration files.
*   **CFG-MGT-2:** The system shall provide a graphical interface for creating and modifying business rules (Loan Periods, Holds Policies, Suppression Rules).
*   **CFG-MGT-3:** Rules shall be definable by criteria (Patron Type, Item Location, Material Type) and applicable to specific user groups.

##### 3.1.4 Backup and Data Recovery (BCK-RCV)
*   **BCK-RCV-1:** The system shall support full, incremental, and transaction log backups.
*   **BCK-RCV-2:** The system shall allow backups to be scheduled or triggered manually.
*   **BCK-RCV-3:** The system shall support integration with third-party enterprise backup software.
*   **BCK-RCV-4:** The system shall provide tools for point-in-time data recovery (rollback) from backups.

##### 3.1.5 Client Software Management (CLI-MGT)
*   **CLI-MGT-1:** The system shall allow administrators to deploy and install ILS client software packages to managed workstations from a central server.
*   **CLI-MGT-2:** The system shall allow scheduling and staging of software updates across defined groups of workstations (e.g., by branch).
*   **CLI-MGT-3:** The system shall report deployment status and failures.

##### 3.1.6 Report Generation and Scheduling (RPT-GEN)
*   **RPT-GEN-1:** The system shall provide a report builder allowing staff to create custom queries against all major record types (Patron, Item, Bibliographic, Transaction).
*   **RPT-GEN-2:** The system shall output reports in CSV, Excel (XLSX), and printable PDF formats.
*   **RPT-GEN-3:** The system shall allow reports to be run on-demand or scheduled for automatic generation and distribution.
*   **RPT-GEN-4:** Managers shall be able to create and save custom dashboards composed of multiple KPI widgets (e.g., daily circulation, active holds).

##### 3.1.7 Record Lock Administration (LCK-ADM)
*   **LCK-ADM-1:** The system shall display a list of currently locked records, including lock type, user, and duration.
*   **LCK-ADM-2:** The system shall allow administrators to set a maximum allowable lock duration.
*   **LCK-ADM-3:** The system shall allow administrators to manually override and release record locks.

##### 3.1.8 Job Scheduling Console (JOB-SCH)
*   **JOB-SCH-1:** The system shall provide a central console to view, schedule, enable, disable, and monitor all system jobs (backups, report generation, data imports/exports).
*   **JOB-SCH-2:** The console shall display job history, status (success/failure), and logs.

#### 3.2 Data Requirements

##### 3.2.1 Logical Data Model (Key Entities)
The module will interact extensively with the following core ILS entities:
```sql
-- Simplified representation of key tables
Patron (patron_id PK, name, account_status, privilege_level, email, phone, balance)
Item (item_id PK, barcode, bib_id FK, current_status, location_code, circ_history)
Bibliographic_Record (bib_id PK, title, author, isbn, publish_year, marc_xml)
Staff_Account (staff_id PK, login_name, role, workgroup, is_active)
Transaction_Log (transaction_id PK, timestamp, user_id, ip_address, action, record_id, details)
Business_Rule (rule_id PK, rule_type, criteria_json, action, applicable_group)
```

##### 3.2.2 Data Import/Export
*   The system shall support batch import and export of patron and bibliographic data via standard formats (MARC21, CSV).
*   Data transfers with external vendors shall be configurable to use secure protocols (SFTP with various authentication modes).

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance
*   The monitoring dashboard shall update metrics in near real-time (< 5-second refresh).
*   Configuration changes shall be applied system-wide within 60 seconds.
*   The system shall support concurrent access and updates by a minimum of 500 simultaneous staff users and external interfaces (SIP2/NCIP).

##### 3.3.2 Security
*   All administrative access shall require authentication.
*   All data transfers (internal/external) shall use encryption (SSL/TLS, SFTP, SSH).
*   The system shall provide full audit trails via the Transaction Log for all administrative actions.

##### 3.3.3 Usability & Accessibility
*   The administrative interface shall be compliant with WCAG 2.1 Level AA for accessibility.
*   Comprehensive, context-sensitive online help shall be provided.

##### 3.3.4 Reliability & Availability
*   Core administrative functions (user auth, basic configuration) shall have 99.5% uptime.
*   The design shall support server clustering for high availability of monitoring and alerting services.

##### 3.3.5 Supportability
*   The system shall provide full access to raw configuration files and application logs for debugging.
*   The SQL database shall be accessible via ODBC for external reporting tools.

### 4. Appendices

#### Appendix A: User Story to Requirement Mapping

| User Story | Mapped Functional Requirements |
| :--- | :--- |
| 1. System Admin - Monitor/Alerts | SYS-MON-1, SYS-MON-2, SYS-MON-3 |
| 2. Staff - Concurrent Record Access | (Implied by system constraint) LCK-ADM-1, LCK-ADM-3 |
| 3. Manager - Custom Dashboards | RPT-GEN-4 |
| 4. System Admin - Schedule Tasks | JOB-SCH-1, JOB-SCH-2, BCK-RCV-2 |
| 5. Staff - Custom Queries/Reports | RPT-GEN-1, RPT-GEN-2 |
| 6. System Admin - Client Software Mgmt | CLI-MGT-1, CLI-MGT-2, CLI-MGT-3 |

#### Appendix B: Open Issues / TBD Items
1.  **Primary Administrative Interface:** Decision pending between web-browser-based vs. Windows-native client.
2.  **Configuration Migration:** Process for promoting configurations from Dev/Test to Production is undefined.
3.  **Scheduled Job Catalog:** Final list of all system-defined scheduled jobs is to be determined.
4.  **Help System Structure:** Detailed information architecture for the online help system is pending.
5.  **Requirement Prioritization:** Detailed timeline for "Priority 2" vs. "Priority 3" requirements requires stakeholder workshop.

---
*Document End*