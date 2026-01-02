# Software Requirements Specification (SRS)
## For the PINES Enhanced Management Reporting & Analysis System (EMRAS)

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft for Review  
**Project:** EMRAS - Evergreen Module Extension

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Enhanced Management Reporting & Analysis System (EMRAS). This system is an extension module for the Evergreen Integrated Library System (ILS) used by the PINES library consortium. The primary purpose is to provide consortium staff with advanced, secure, and user-friendly tools for data querying, reporting, and analytical decision support.

This document is intended for use by the project stakeholders, development team, quality assurance team, and project management.

#### 1.2 Scope
The EMRAS shall be a software module that integrates with the existing PINES Evergreen ILS infrastructure. It will extend Evergreen's capabilities by providing a centralized reporting and analytics engine, accessible via web and dedicated client interfaces.

**In-Scope:**
*   A web-based and Windows client-based interface for report creation, management, and execution.
*   A query builder tool with a user-friendly interface for non-technical staff.
*   A repository of configurable report templates for common reporting needs.
*   A comprehensive, role-based permissions system governing report access, creation, and data visibility.
*   Generation of standardized reports for inventory, patron demographics, transactions, financial auditing, item transfers, and purging.
*   Analytical functions for collection use, branch operational capacity, and patron behavior trends.
*   Support for all 286 PINES member locations.

**Out-of-Scope:**
*   Modification of core Evergreen transactional processing (e.g., circulation, cataloging).
*   Replacement of existing Evergreen basic reporting modules.
*   Direct data warehousing or ETL processes external to the primary Evergreen database.
*   Real-time data streaming or dashboard visualization (beyond generated reports).

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **PINES** | Public Information Network for Electronic Services – Georgia's statewide resource-sharing library consortium. |
| **ILS** | Integrated Library System. |
| **Evergreen** | The open-source ILS used by the PINES consortium. |
| **EMRAS** | Enhanced Management Reporting & Analysis System (the subject of this SRS). |
| **Staff** | General library staff at any member branch. |
| **Local System Admin** | Administrator with elevated permissions for a subset of consortium branches (e.g., a county system). |
| **Global System Admin** | Administrator with permissions across the entire PINES consortium. |
| **Ad-hoc Report** | A one-time, user-created report not saved as a template. |

#### 1.4 References
*   Evergreen ILS Official Documentation
*   PINES Consortium Governance Policies
*   GAAP (Generally Accepted Accounting Principles)
*   GAGAS (Generally Accepted Government Auditing Standards)

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its user classes, and operating environment. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements including performance, security, and constraints.

---

### 2. Overall Description

#### 2.1 Product Perspective
EMRAS is a new, self-contained module that will integrate with the existing Evergreen ILS architecture. It will act as a middleware layer between the user interface and the Evergreen relational database, primarily for read-only analytical queries to avoid impacting transactional performance.

**System Interfaces:**
*   **Evergreen Database:** EMRAS will execute `SELECT` queries against the existing Evergreen production database(s). It must not perform `INSERT`, `UPDATE`, or `DELETE` operations on transactional tables without explicit, logged procedures.
*   **Evergreen Authentication:** The system shall use the existing Evergreen authentication and organizational unit framework for user login and base organizational hierarchy.
*   **Web Server:** The web interface will be served via the existing Evergreen Apache/OAuth infrastructure.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Staff** | General library personnel. Limited technical expertise. | Run pre-defined reports for daily tasks (e.g., hold lists, overdue items). View data for their single branch/location. |
| **Library Manager** | Manages a single branch or small group. Some analytical need. | Analyze branch performance, collection turnover, patron demographics. Create and save custom reports for their scope. |
| **Library Director** | Oversees a library system (multiple branches). Strategic focus. | Compare performance across branches, analyze system-wide trends, generate financial and audit reports. |
| **Local System Administrator** | Technical admin for a library system. Proficient with Evergreen. | Create and clone complex report templates for their system. Manage permissions for Managers and Staff within their scope. Troubleshoot report issues. |
| **Global System Administrator** | PINES consortium-level technical staff. Highest expertise. | Define global report templates. Configure all permission schemas. Audit system usage. Access data across all 286 locations. |

#### 2.3 Operating Environment
*   **Server OS:** Linux (primary) or Solaris server operating systems.
*   **Client Access:** Must be accessible via modern web browsers (Chrome, Firefox, Safari, Edge) and a dedicated Windows client application.
*   **Database:** Must operate with the existing Evergreen relational database (PostgreSQL).
*   **Network:** Must function within the PINES Wide Area Network (WAN), accounting for potential latency to central servers from all locations.

#### 2.4 Design and Implementation Constraints
1.  **Platform Constraint:** The server component must be deployable on the existing PINES Linux/Solaris server infrastructure.
2.  **Integration Constraint:** Must extend, not break, the existing Evergreen ILS authentication and organizational structure.
3.  **Database Constraint:** Must use the existing Evergreen PostgreSQL schema; no major schema alterations are permitted.
4.  **Compliance Constraint:** All financial and audit reports must comply with standard governmental accounting practices (GAAP/GAGAS).
5.  **Scale Constraint:** Must be designed to support data and concurrent users from 286 distinct library locations.

#### 2.5 Assumptions and Dependencies
*   The existing Evergreen database schema is stable and documented.
*   Sufficient server resources (CPU, RAM, I/O) will be allocated to handle reporting workloads without degrading the transactional ILS performance.
*   Users will have received appropriate training on both Evergreen basics and the EMRAS tool.

---

### 3. System Features and Requirements

#### 3.1 Feature: User-Friendly Query & Reporting Interface
**Description:** The system shall provide an intuitive interface for building, saving, and running reports.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-1** | The system shall provide a web-based interface accessible after successful Evergreen login. | High |
| **FR-2** | The system shall provide a Windows client application with equivalent functionality to the web interface. | High |
| **FR-3** | The interface shall include a visual query builder allowing users to select tables, fields, and define filters using drop-downs, checkboxes, and text inputs without writing SQL. | High |
| **FR-4** | The system shall allow users with appropriate permissions to write and execute custom SQL queries directly. | Medium |
| **FR-5** | Users shall be able to save a constructed query as a personal report template or a public template (with admin rights). | High |
| **FR-6** | Users shall be able to clone and modify existing report templates (subject to permissions). | High |
| **FR-7** | Report output shall be exportable in at least the following formats: CSV, PDF, and HTML. | High |

#### 3.2 Feature: Fine-Grained Permission System
**Description:** Access to data and report functions must be strictly controlled based on user roles and organizational hierarchy.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-8** | Permissions shall be based on the user's Evergreen organizational unit (e.g., branch, system, consortium). | High |
| **FR-9** | The system shall implement distinct permissions for: (a) Running reports, (b) Creating personal templates, (c) Creating public templates, (d) Cloning reports, (e) Accessing financial data, (f) Accessing patron personal data. | High |
| **FR-10** | A Global System Admin shall be able to define permission groups (e.g., "Branch Managers", "Auditors") and assign them to users. | High |
| **FR-11** | All report executions shall be logged, recording the user, report run, timestamp, and organizational scope of data accessed. | High |

#### 3.3 Feature: Pre-defined & Ad-hoc Report Generation
**Description:** The system shall supply a library of standard reports and allow for the creation of one-time ad-hoc reports.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-12** | The system shall include a suite of pre-defined report templates for the following categories: <br> • **Inventory:** Item status, lost items, weeding candidates.<br> • **Patron Demographics:** Registration counts, patron types by branch.<br> • **Transactions:** Circulation statistics, hold fulfillment rates, overdue analysis.<br> • **Financial:** Fine revenue, fee assessments, audit trails of monetary transactions.<br> • **Transfers & Purging:** Item transfer tracking, purging workflow status. | High |
| **FR-13** | Users shall be able to create an ad-hoc report, execute it, and optionally discard it without saving. | High |
| **FR-14** | Report parameters (e.g., date range, branch selection) shall be customizable at runtime for both pre-defined and ad-hoc reports. | High |

#### 3.4 Feature: Analytical Functions
**Description:** The system shall provide tools to analyze data for decision support.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-15** | The system shall allow analysis of **collection use** (e.g., circulation per title/copy, turnover rate by classification). | Medium |
| **FR-16** | The system shall provide data to analyze **branch capacity** (e.g., transactions per staff hour, peak usage periods). | Medium |
| **FR-17** | The system shall support analysis of **patron behavior** (e.g., material type preferences, visit frequency, program attendance linkage). | Medium |
| **FR-18** | Analytical reports shall support basic aggregate functions (sum, average, count) and grouping. | High |

#### 3.5 Feature: System Administration
**Description:** Administrators require tools to manage the reporting environment.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-19** | Global System Admins shall be able to enable/disable report templates for the entire consortium or specific library systems. | High |
| **FR-20** | The system shall provide an interface for administrators to view report execution logs and audit data access. | High |
| **FR-21** | The system shall allow administrators to schedule recurring reports (e.g., monthly statistics) and have them emailed to designated recipients. | Medium |

---

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
*   **Query Response:** Standard pre-defined reports shall return initial results for a single branch within 10 seconds under normal load.
*   **Concurrent Users:** The system shall support up to 100 concurrent users executing reports.
*   **Load Impact:** EMRAS reporting queries must be optimized to minimize performance impact on the core Evergreen transactional database. Use of database replicas for reporting is a preferred architectural pattern.

#### 4.2 Safety & Security Requirements
*   **Data Security:** The system shall not expose patron personally identifiable information (PII) or sensitive financial data to users without explicit permission.
*   **Authentication:** All access must be mediated through Evergreen's central authentication system.
*   **Authorization:** All data requests must be filtered through the permission layer (FR-8, FR-9) before execution.
*   **Audit Trail:** As per FR-11, an immutable log of all report executions must be maintained for security auditing.

#### 4.3 Software Quality Attributes
*   **Usability:** The query tool interface shall be usable by library staff with minimal database training. A usability success rate of >90% on core tasks (create a simple report, filter, run) is targeted.
*   **Reliability:** The system shall have 99.5% uptime during standard library operating hours.
*   **Maintainability:** The system shall be documented and designed to allow PINES developers to add new report templates and fields without vendor assistance.

#### 4.4 Compliance Requirements
*   All financial report logic and outputs must comply with **GAAP** and state **auditing standards**.
*   The handling of patron data must comply with **PINES privacy policies** and relevant **state library statutes**.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| System Architect | | | |