# Software Requirements Specification (SRS)
## Management Processes Module for Integrated Library System (ILS)

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Prepared for:** PINES Consortium  
**Prepared by:** [Your Organization/Team Name]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Management Processes module of an Integrated Library System (ILS). The primary purpose is to replace and enhance the reporting, analytics, and inventory management capabilities within the PINES consortium's existing Evergreen ILS. This document serves as a comprehensive guide for stakeholders, developers, testers, and project managers throughout the system's lifecycle.

#### 1.2 Scope
The scope of this project is the design, development, and implementation of a standalone Management Processes module. This module will provide consortium staff and individual library administrators with advanced tools for data querying, report generation, and inventory control. It will interface with the existing ILS database but will be architecturally separate from the Online Public Access Catalog (OPAC) module to ensure no degradation of public-facing services.

**In-Scope:**
*   Configurable query builders and reporting tools against the ILS relational database.
*   Generation of standardized operational, financial, and board-level reports.
*   Inventory management functions (tracking, transferring, weeding).
*   A web-based interface and a dedicated Windows client application.
*   Backend services hosted on Linux/Solaris servers.

**Out-of-Scope:**
*   Modification of the existing OPAC module's functionality or user interface.
*   Core circulation, cataloging, or patron management transaction processing (these remain with the base Evergreen system).
*   Migration of historical data (though the module must be capable of accessing it).

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **ILS:** Integrated Library System.
*   **OPAC:** Online Public Access Catalog. The public-facing interface for library patrons.
*   **PINES:** Public Information Network for Electronic Services. A consortium of libraries in Georgia using the Evergreen ILS.
*   **Evergreen:** The open-source ILS currently in use by PINES.
*   **SRS:** Software Requirements Specification.
*   **RDBMS:** Relational Database Management System.

#### 1.4 References
*   PINES Evergreen System Documentation.
*   Existing Evergreen ILS SRS and Architecture Documents.
*   ISO/IEC/IEEE 29148:2018 Standard for Requirements Engineering.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a high-level description of the product and its operating environment. Section 3 details specific functional requirements. Section 4 outlines non-functional requirements including performance, security, and constraints. Appendices may contain supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
The Management Processes module is a new, self-contained component that will augment the existing Evergreen ILS ecosystem. It will connect to the same fully relational database backend as the core Evergreen system but will operate independently to ensure that management and reporting workloads do not impact the performance or availability of the patron-facing OPAC.

**System Interfaces:**
*   **Database Interface:** Direct, read-optimized connection to the primary Evergreen RDBMS (e.g., PostgreSQL). Write operations will be limited to specific inventory management functions.
*   **OPAC Module:** No direct interface. Independence is a key constraint.

**User Interfaces:**
*   **Web Browser Interface:** Accessible via modern browsers (Chrome, Firefox, Safari, Edge).
*   **Windows Client Application:** A dedicated desktop application for Windows 10/11.

#### 2.2 Product Functions
The high-level functions of the module are:
1.  **Data Exploration & Querying:** Provide tools to build, save, and execute custom queries across bibliographic, item, patron, and transaction data.
2.  **Report Generation & Scheduling:** Generate pre-defined and ad-hoc reports. Support automated scheduling and distribution of reports (e.g., via email).
3.  **Inventory Management:** Facilitate system-wide tracking of material status, manage inter-branch transfer requests, and support weeding workflows based on configurable criteria.
4.  **Financial & Collection Analysis:** Produce reports on collection age, circulation statistics, cost-per-use, and other metrics for strategic planning.

#### 2.3 User Characteristics
*   **Library Directors/Board Members:** Need high-level summary reports (financial, usage statistics). Minimal technical expertise.
*   **Library Managers & Department Heads:** Require operational reports (circulation trends, overdue items, collection status). Moderate system familiarity.
*   **Technical Staff & System Librarians:** Will create complex custom queries, configure report templates, and manage system-wide inventory processes. High technical expertise.
*   **PINES Consortium Administrators:** Require global reports across all member libraries and system configuration tools.

#### 2.4 Constraints
1.  **Platform Constraint:** The server component must operate on existing PINES infrastructure, which is based on **Linux and/or Solaris** operating systems.
2.  **Client Access Constraint:** The system must be accessible via a standard **web browser** and must also provide a **native Windows client application**.
3.  **Architectural Constraint:** The module must use a **fully relational database backend** (the existing Evergreen database). It must not introduce any elements that constrain the functionality or performance of the separate **OPAC module**.
4.  **Legacy Data Constraint:** Must be compatible with the existing Evergreen database schema without requiring major structural changes.

#### 2.5 Assumptions and Dependencies
*   The existing Evergreen ILS database will remain the system of record and will be stable during the development period.
*   Sufficient server resources (CPU, memory, I/O) will be allocated to the new module to ensure performance does not degrade the core ILS.
*   Users will have appropriate permissions within the ILS to access the data relevant to their roles.

### 3. Specific Requirements

#### 3.1 Functional Requirements

**3.1.1 Query and Reporting Tools (QR)**
*   **QR-1:** The system shall provide a graphical query builder allowing users to select tables, fields, and define conditions without writing SQL.
*   **QR-2:** The system shall allow advanced users to write, validate, and execute custom SQL queries directly, with read-only access by default.
*   **QR-3:** Users shall be able to save frequently used queries and share them with other users based on permission groups.
*   **QR-4:** Query results shall be exportable in at least the following formats: CSV, PDF, and XLSX.

**3.1.2 Standardized Reporting (SR)**
*   **SR-1:** The system shall include a library of pre-defined reports for:
    *   **SR-1.1:** Operational Reports (e.g., daily circulation, active patrons, holds queue).
    *   **SR-1.2:** Financial Reports (e.g., fines collected, material costs by branch).
    *   **SR-1.3:** Board/Summary Reports (e.g., monthly usage statistics, year-over-year growth).
    *   **SR-1.4:** Collection Analysis Reports (e.g., copyright date distribution, circulation by subject).
*   **SR-2:** Users shall be able to schedule reports to run automatically at specified times (e.g., first day of the month).
*   **SR-3:** The system shall allow scheduled reports to be distributed via email to a configurable list of recipients.

**3.1.3 Inventory Management (IM)**
*   **IM-1:** The system shall provide a real-time search and view of item status across all branches, including location, circulation status, and last transaction date.
*   **IM-2:** Staff shall be able to create and manage batch transfers of materials between branches, generating pull lists for sending locations and receiving slips for destinations.
*   **IM-3:** The system shall support weeding workflows by allowing staff to define criteria (e.g., "last circulated > 5 years ago, condition = poor") and generate candidate item lists for review.
*   **IM-4:** All inventory-related actions (transfers, discards) shall create audit trails in the database.

#### 3.2 Non-Functional Requirements

**3.2.1 Performance Requirements**
*   **PER-1:** The query interface shall return results for standard pre-defined reports (< 1000 rows) within **5 seconds** 95% of the time.
*   **PER-2:** Complex ad-hoc queries or large reports (> 10,000 rows) shall provide a progress indicator and shall not cause a browser or client timeout for operations under **10 minutes**.

**3.2.2 Security Requirements**
*   **SEC-1:** User authentication shall integrate with the existing Evergreen ILS authentication system.
*   **SEC-2:** The system shall implement role-based access control (RBAC), mirroring and extending Evergreen permissions where necessary, to restrict data and functions (e.g., financial data, ability to run system-wide queries).
*   **SEC-3:** All data transmitted between the client and server shall be encrypted using TLS 1.2 or higher.

**3.2.3 Software Quality Attributes**
*   **REL-1:** The module shall have a target availability of 99.5% during standard business hours (8 AM - 8 PM local time).
*   **USAB-1:** The web interface shall conform to WCAG 2.1 Level AA guidelines for accessibility.
*   **MAIN-1:** All configuration for reports and queries shall be stored in the database or external files, not in hard-coded application logic.

### 4. Appendices

#### 4.1 Data Model Overview
*(This section would typically include or reference an Entity-Relationship Diagram or a list of key database tables and views the module will primarily interact with, such as: `actor.usr` (patrons), `biblio.record_entry`, `asset.copy` (items), `money.billing` (fines), `action.circulation` (transactions)).*

#### 4.2 Report Mockups
*(Link to or describe location of wireframes/mockups for key report interfaces and the query builder.)*

---
**Document Approval:**

| Name | Role | Signature | Date |
| :--- | :--- | :--- | :--- |
| | Project Sponsor | | |
| | Lead Developer | | |
| | Quality Assurance | | |