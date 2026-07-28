# Software Requirements Specification (SRS)
## Management Processes Module for Integrated Library System (ILS)

**Document Version:** 1.0  
**Date:** [Date of Generation]  
**Status:** Draft for Review  
**Project:** Evergreen ILS Enhancement - Georgia PINES Consortium

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Management Processes module of the Evergreen Integrated Library System (ILS). This module is designed to provide comprehensive reporting, analysis, and batch management tools for the Georgia PINES consortium. The intended audience includes project stakeholders, system architects, developers, testers, and the library staff user community.

#### 1.2 Scope
The Management Processes module is a core administrative component of the ILS, focused exclusively on data analysis, reporting, and inventory management utilities. It provides tools for library staff and administrators to derive operational, financial, and strategic insights from library data.

**In-Scope:**
*   Ad-hoc and templated report generation against all ILS data domains (collections, patrons, transactions, finances).
*   A secure, user-friendly query builder interface.
*   Batch inventory management operations (e.g., inter-branch transfers).
*   Configuration and management of reports, templates, and user permissions.
*   Longitudinal data archiving and anonymized statistical analysis.
*   Interfaces with core ILS databases and external vendor systems.

**Out-of-Scope:**
*   Core Online Public Access Catalog (OPAC) patron search and discovery functions.
*   Acquisitions workflows (ordering, receiving, invoicing).
*   Cataloging workflows (bibliographic record creation and maintenance).
*   Real-time circulation desk operations (check-in/check-out interfaces).

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **ILS:** Integrated Library System.
*   **OPAC:** Online Public Access Catalog.
*   **PINES:** Public Information Network for Electronic Services.
*   **API:** Application Programming Interface.
*   **MARC:** Machine-Readable Cataloging.
*   **EDIFACT:** Electronic Data Interchange for Administration, Commerce, and Transport.
*   **Global System Administrator:** Administrator with system-wide configuration privileges.
*   **Local System Administrator:** Administrator with privileges limited to a specific branch or set of branches.

#### 1.4 References
*   Evergreen ILS Core System Documentation
*   Georgia PINES Consortium Operational Guidelines
*   WCAG 2.0 Accessibility Guidelines

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its users, and operating environment. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements, including performance, security, and usability.

### 2. Overall Description

#### 2.1 Product Perspective
This module is an enhancement to the existing, centrally-hosted Evergreen ILS. It is a dependent subsystem that sits atop the core ILS database and must interoperate seamlessly with the Acquisitions and Cataloging modules for data integrity. It is separate from but may supply data to the patron-facing OPAC. The system architecture is server-based, serving both web browser and dedicated Windows client interfaces.

#### 2.2 Product Functions
The high-level functions of the Management Processes module are:
1.  **Report Design & Management:** Provide tools to create, save, template, and secure reports.
2.  **Data Analysis & Reporting:** Generate reports for Collections, Patrons, Transactions, and Finances.
3.  **Batch Inventory Management:** Execute bulk operations on library items.
4.  **Data Archiving:** Anonymize and store historical transaction data for trend analysis.
5.  **System Administration:** Configure user roles, permissions, and system-wide report settings.

#### 2.3 User Characteristics
| User Role | Expertise | Primary Activities |
| :--- | :--- | :--- |
| **Frontline Staff** | Basic computer literacy, understanding of library circulation. | Run pre-defined, templated reports for daily operations (e.g., overdue lists, daily circulation counts). |
| **Library Managers** | Advanced library operations knowledge, data analysis skills. | Create and run ad-hoc and templated reports for branch-level analysis, planning, and management. |
| **Local System Administrators** | Technical proficiency with the ILS, understanding of SQL concepts. | Manage report templates and permissions for their assigned branches; perform complex ad-hoc queries. |
| **Global System Administrators** | Expert-level ILS and database administration skills. | Configure system-wide report settings, manage all security groups/roles, and oversee data archiving processes. |

#### 2.4 Constraints
*   **Technical:** Must operate on Linux or Solaris server infrastructure. Must interface with an existing, complex ILS database schema.
*   **Operational:** Must not degrade performance of core circulation and cataloging functions during peak operational hours.
*   **Regulatory:** Financial reports must comply with standard auditing practices.
*   **Dependency:** Functionality is wholly dependent on the data structures and APIs of the core Evergreen ILS.

#### 2.5 Assumptions and Dependencies
*   It is assumed that all users have a general understanding of library services and terminology.
*   The module depends entirely on the continuous availability and integrity of the core ILS database.
*   Successful interfacing with vendor websites is partially dependent on the vendors' external API stability and documentation.

### 3. Specific Requirements

#### 3.1 External Interface Requirements
**3.1.1 User Interfaces**
*   The system shall provide a web-based interface compatible with Internet Explorer 6.0+ and Firefox 2.0+.
*   The system shall provide an alternative Windows client application.
*   All interfaces shall produce standards-compliant HTML (e.g., XHTML 1.0 Strict) to ensure accessibility.

**3.1.2 Hardware Interfaces**
*   The module shall operate on designated application servers running Linux or Solaris.

**3.1.3 Software Interfaces**
*   **Core ILS Database:** The module shall have read and (where appropriate for batch operations) write access to the central ILS relational database.
*   **Vendor Systems:** The module shall be capable of interfacing with external vendor websites via published APIs or standard file transfer protocols (MARC, EDIFACT) for data exchange.

**3.1.4 Communications Interfaces**
*   Standard HTTP/HTTPS for web interface communication.
*   Support for secure FTP (SFTP) or similar protocols for batch file transfers with vendors.

#### 3.2 Functional Requirements
**3.2.1 Report Query Tool (FR-QT)**
*   **FR-QT-01:** The system shall provide a graphical, user-friendly query builder that allows authorized users to select data fields, set filter conditions, and define sort orders without writing SQL.
*   **FR-QT-02:** The query builder shall provide access to all major library data types: Bibliographic, Item, Patron, Transaction (Circulation, Holds), and Financial.
*   **FR-QT-03:** The system shall allow users to save query definitions as private or shared report templates.

**3.2.2 Report Management & Security (FR-RMS)**
*   **FR-RMS-01:** The system shall allow Global and Local System Administrators to create and manage secure report templates.
*   **FR-RMS-02:** Templated reports shall allow controlled customization (e.g., setting date ranges, choosing branch limits) by users with "run" permissions.
*   **FR-RMS-03:** User access to reports and report creation tools shall be controlled through a configurable system of security groups or roles (e.g., "Staff," "Manager," "Admin").

**3.2.3 Collection Analysis Reports (FR-CAR)**
*   **FR-CAR-01:** The system shall generate pre-defined reports for collection usage (circulation counts by classification, copy).
*   **FR-CAR-02:** The system shall generate pre-defined reports for collection capacity and shelf space analysis.
*   **FR-CAR-03:** The system shall generate pre-defined and ad-hoc reports to support weeding projects (e.g., items with zero circulations over X years).

**3.2.4 Patron Analysis Reports (FR-PAR)**
*   **FR-PAR-01:** The system shall generate pre-defined reports on patron demographics (age, zip code, registration date).
*   **FR-PAR-02:** The system shall generate pre-defined and ad-hoc reports on patron activity (total checkouts, hold patterns, fine history).

**3.2.5 Transaction Analysis Reports (FR-TAR)**
*   **FR-TAR-01:** The system shall generate pre-defined and ad-hoc reports for all circulation transactions (check-ins, check-outs, renewals).
*   **FR-TAR-02:** The system shall generate pre-defined and ad-hoc reports on hold requests (volume, fulfillment time, turnover).

**3.2.6 Financial Reports (FR-FIN)**
*   **FR-FIN-01:** The system shall generate pre-defined financial reports for fines accrued, payments received, and outstanding balances.
*   **FR-FIN-02:** The system shall generate reports estimating collection value for insurance and auditing purposes.
*   **FR-FIN-03:** All financial reports shall be formatted to comply with standard auditing requirements (clear audit trail, non-editable output).

**3.2.7 Batch Inventory Management (FR-BIM)**
*   **FR-BIM-01:** The system shall provide a utility to select groups of items based on a query and perform batch actions.
*   **FR-BIM-02:** The system shall support the batch transfer of selected items from one branch to another, updating the database and generating transfer slips.

**3.2.8 Data Archiving (FR-DA)**
*   **FR-DA-01:** The system shall provide a utility to archive aged transaction data from the operational database.
*   **FR-DA-02:** During archiving, the system shall anonymize patron-specific data to protect privacy while preserving statistical usefulness for longitudinal analysis.

#### 3.3 Non-Functional Requirements

**3.3.1 Performance Requirements**
*   **PERF-01:** The system shall support concurrent use by staff from 286 library locations without causing disruption to core ILS functions (OPAC, circulation).
*   **PERF-02:** The system shall be designed to handle data volumes associated with 17 million annual circulation transactions. Standard pre-defined reports shall execute within an average of 30 seconds during peak load.

**3.3.2 Accessibility Requirements**
*   **ACC-01:** The user interface shall be compatible with common screen-reading software (e.g., JAWS, NVDA).
*   **ACC-02:** The user interface shall be compatible with screen-magnification software.

**3.3.3 Security Requirements**
*   **SEC-01:** All user access shall require authentication via the core ILS authentication system.
*   **SEC-02:** Fine-grained user rights and privileges shall be controllable through configurable security groups or roles managed within the module.
*   **SEC-03:** Financial data and patron personal data shall be accessible only to users with explicitly granted permissions.

**3.3.4 Operational & Environmental Requirements**
*   **OE-01:** The module shall operate on a Linux or Solaris server environment.
*   **OE-02:** The system shall use a fully relational database (PostgreSQL) as its back-end.
*   **OE-03:** A distinct development and training environment, separate from production, shall be maintained. Configuration and report templates shall be migratable from development to production.

**3.3.5 Data Quality Requirements**
*   **DQ-01:** All reports must clearly indicate the data source and the time/date the report was generated.
*   **DQ-02:** Financial reports must be numerically consistent and traceable back to source transaction records.

### 4. Appendices

#### 4.1 Priority and Acceptance
*   All requirements listed in this document are classified as **Priority 1 (Critical)**.
*   Final system acceptance is contingent upon successful testing by the designated user group, validating all new report development functionalities.
*   The system must demonstrably fulfill the specific reporting examples and detailed requirements contained in the source project documentation's appendices (referenced in Section 1.4).

#### 4.2 Open Issues
*   Specific details of vendor API integrations will be defined during the design phase based on vendor documentation.
*   The detailed schema for the anonymized statistical archive will be finalized in collaboration with consortium data analysts.

---
*Document End*