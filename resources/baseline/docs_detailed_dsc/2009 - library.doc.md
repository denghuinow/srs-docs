# Software Requirements Specification (SRS)
## Management Processes Module for the Georgia PINES Integrated Library System

**Document Version:** 1.0  
**Date:** [Date of Generation]  
**Status:** Draft for Review  
**Project:** PINES ILS Enhancement  
**Module:** Management Processes

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Management Processes module of the Georgia PINES consortium's Integrated Library System (ILS). The primary purpose is to replace and significantly enhance the existing Evergreen ILS reporting capabilities, enabling data-driven decision-making for library services, collections, and patron management across 275+ member locations.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `MP-FR-XXX`. Non-functional requirements are labeled `MP-NFR-XXX`.
*   **Priority:** All requirements specified herein are designated **Priority 1** for the Minimum Viable Product (MVP). Detailed phasing will be determined post-approval.
*   **Keywords:** `MUST`, `SHALL`, `SHOULD`, `MAY` are used as defined in IETF RFC 2119.

#### 1.3 Scope
This specification covers the requirements for the **Management Processes** module, which includes:
*   Reporting and analytics tools for demographics, circulation, financials, and collection management.
*   Inventory control utilities for batch operations.
*   A secure, templated reporting engine with queue management.
*   Integration points with the core ILS and external systems.

**Out of Scope:**
*   Detailed specifications for the OPAC (Online Public Access Catalog), Acquisitions, and Cataloging modules.
*   Field-level user interface (UI) and user experience (UX) design, which will follow an iterative development process.
*   The underlying data migration strategy for the reporting data warehouse (covered in separate document PINES-006).

#### 1.4 References
*   PINES ILS Overall Project Charter
*   Data Archiving & Retention Policy (PINES-006, PINES-025)
*   Legacy Report Inventory (Appendix A)
*   Reporting Data Warehouse Specification (Appendix B)

### 2. Overall Description

#### 2.1 Product Perspective
The Management Processes module is a core component of the new PINES ILS. It interacts with the ILS transactional database and a separate reporting data warehouse. It provides a web-based interface for library staff and administrators, and integrates with external systems for email distribution and data feeds.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Patron** | Provides anonymized usage data. | Privacy protection in all reports. |
| **Staff** | Performs daily operations. | Simple, quick operational reports (e.g., items in transit, daily circulation stats). |
| **Local System Administrator** | Manages a library system (multiple branches). | Ability to create and assign templated reports; configure permissions for local staff. |
| **Library Manager** | Supervises a single branch or department. | Collection analysis, shelf space metrics, staff productivity reports. |
| **Library Director** | Executive oversight, board reporting. | High-level financial, service, and demographic summaries. |
| **Global System Administrator** | Consortium-level management. | System-wide configuration, consortium statistical reports, template governance. |

#### 2.3 Operating Environment
*   **Software:** Must be accessible via web browsers (IE6+, Firefox 2+ compatibility required).
*   **Hardware:** Must operate within the existing PINES server infrastructure.
*   **Integration:** Must interface with the Evergreen ILS core database, SMTP email servers, and vendor APIs (MARC21, EDIFACT).

#### 2.4 Design and Implementation Constraints
1.  The module must not degrade the performance of core circulation functions during peak operational hours.
2.  All demographic reporting must anonymize patron data in compliance with Georgia state privacy laws.
3.  The permission model must support the hierarchical structure of the PINES consortium (Consortium > System > Branch).

#### 2.5 Assumptions and Dependencies
*   **Assumption:** A separate reporting data warehouse or snapshot mechanism will be available for historical queries.
*   **Dependency:** Clear API specifications from the parallel Acquisitions and Cataloging module development teams.
*   **Assumption:** The PINES Reports Working Group will provide final, prioritized lists of canned reports and templates.

### 3. System Features and Requirements

#### 3.1 Feature: Secure, Templated Reporting Engine
**Description:** A system for creating, managing, and executing reports with fine-grained access control.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **MP-FR-010** | The system SHALL provide a web-based interface for report creation, execution, and management. | 1 |
| **MP-FR-011** | The system SHALL support three report types: <br> 1. **Canned Reports:** Pre-defined, executable-only reports. <br> 2. **Templated Reports:** Administrator-defined templates with locked and editable criteria. <br> 3. **On-Demand/Open Template Reports:** Ad-hoc queries for users with appropriate permissions. | 1 |
| **MP-FR-012** | The system SHALL allow users with `Template Creation` rights to create, clone, and save report templates, defining SQL/query logic, output format, and which filter fields are fixed vs. user-editable. | 1 |
| **MP-FR-013** | The system SHALL organize templates into shared folders with configurable permissions (view, run, edit) assignable to user roles. | 1 |
| **MP-FR-014** | The system SHALL validate a user's permissions against the requested report template, data fields, and target library entities before execution. | 1 |
| **MP-FR-015** | Given a staff member lacks ad-hoc query permissions, the system SHALL deny access to the open query tool interface. | 1 |

#### 3.2 Feature: Asynchronous Report Job Management
**Description:** Handles the submission, queuing, execution, and delivery of report requests.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **MP-FR-020** | The system SHALL submit complex or long-running report requests to a processing queue for asynchronous execution. | 1 |
| **MP-FR-021** | The system SHALL provide a user-visible queue status dashboard where users can see the status (Pending, Processing, Complete, Error) and estimated position of their report jobs. | 1 |
| **MP-FR-022** | The system SHALL allow users to cancel their own report jobs that are in a `Pending` state. | 1 |
| **MP-FR-023** | The system SHALL execute report queries against the appropriate data source: operational database for real-time data or the reporting data warehouse for historical data. | 1 |
| **MP-FR-024** | The system SHALL compile results, apply required anonymization to patron data, and format output. | 1 |
| **MP-FR-025** | The system SHALL deliver completed reports via the web UI for download and/or via email attachment based on user selection or template configuration. | 1 |
| **MP-FR-026** | The system SHALL support configurable, recurring scheduled reports (e.g., daily, weekly, monthly). | 1 |

#### 3.3 Feature: Collection Analysis & Inventory Tools
**Description:** Specialized reports and utilities for managing library collections and inventory.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **MP-FR-030** | The system SHALL generate a **Shelf Space Report** that compares, per material genre/format: Circulation Percentage, Collection Percentage, and Shelf Space Percentage for a specified branch or system. | 1 |
| **MP-FR-031** | The system SHALL generate a **"Last Copy" Report** identifying item records that represent the last copy held anywhere within the PINES consortium. | 1 |
| **MP-FR-032** | The system SHALL provide a utility to execute batch inventory actions, starting with **Batch Transfer**. <br> 1. User can query and select a batch of items. <br> 2. User can update the `Location` field for all selected items. <br> 3. The system SHALL generate a pull list. <br> 4. The system SHALL allow the action to be scheduled and/or reverted. | 1 |
| **MP-FR-033** | Reports MUST be able to filter on and include transactions involving uncataloged materials. | 1 |

#### 3.4 Feature: Financial Auditing & Compliance Reporting
**Description:** Tools to generate financial reports that meet governmental auditing standards.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **MP-FR-040** | The system SHALL generate a **Payment Ledger Report** for a given date range that shows each payment transaction and details the specific fine or charge transactions to which it was applied, ensuring compliance with standard double-entry accounting practice. | 1 |
| **MP-FR-041** | All financial report outputs MUST be capable of being formatted to meet state, county, and municipal auditing requirements. | 1 |

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   The primary interface SHALL be a web application compatible with Internet Explorer 6+ and Firefox 2+.
*   The interface SHALL be accessible via screen readers (WCAG 2.0 Level A compliance as a baseline).
*   The report output SHALL be available in CSV, HTML (accessible), and Excel formats.

#### 4.2 Hardware Interfaces
None specified beyond standard server/client web architecture.

#### 4.3 Software Interfaces
| Interface | Direction | Purpose | Data Format | SLA / Constraint |
| :--- | :--- | :--- | :--- | :--- |
| **Evergreen ILS Core DB** | Bi-directional | Source for real-time report data & update for inventory actions. | SQL Queries / Result Sets | Must not disrupt peak circulation performance. |
| **Reporting Data Warehouse** | From Warehouse | Source for historical report data. | SQL Queries / Result Sets | Queries must be optimized for analytical processing. |
| **Email Server (SMTP)** | From System | Distribution of completed reports. | RFC 5322 Email with Attachments | Configurable scheduling and retry on failure. |
| **Vendor APIs** | From System | Automated export of standardized data (e.g., for auditors). | MARC21, EDIFACT, CSV | Adherence to published vendor API specifications. |

#### 4.4 Communications Interfaces
Standard HTTP/HTTPS for web interface and internal API communication.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
| ID | Requirement Description |
| :--- | :--- |
| **MP-NFR-001** | The system MUST support concurrent report generation for at least 286 simultaneous users (one per location). |
| **MP-NFR-002** | The reporting engine MUST implement job queuing and asynchronous processing to prevent user interface blocking for reports estimated to take > 30 seconds. |
| **MP-NFR-003** | The definition of "real-time" data and performance thresholds for queries against the operational database SHALL be defined by the Development Team and Global System Administrators. |

#### 5.2 Safety & Security Requirements
| ID | Requirement Description |
| :--- | :--- |
| **MP-NFR-010** | The system SHALL implement a fine-grained, role-based permission model controlling access to: report templates, template folders, specific database tables/fields, and library organizational units. |
| **MP-NFR-011** | Any report containing patron demographic information (age, zip code) MUST use anonymized or aggregated data to prevent identification of individuals, as per state law. |
| **MP-NFR-012** | All user interactions with the reporting system (login, report run, template edit) SHALL be logged for security auditing. |

#### 5.3 Software Quality Attributes
| Attribute | Requirement |
| :--- | :--- |
| **Reliability** | Report template definitions and historical data snapshots MUST be backed up and recoverable. Scheduled reports SHALL have a configurable retry mechanism (e.g., 3 retries) upon execution failure. |
| **Observability** | Users MUST be able to view the status of their report jobs. System administrators MUST have access to low-level diagnostic logs for troubleshooting failed reports or performance issues. |
| **Maintainability** | The system architecture SHALL allow for new canned reports and template types to be added post-launch without major code changes. |
| **Compliance** | All HTML report output SHALL meet accessibility standards (WCAG 2.0 Level A). |

### 6. Other Requirements

#### 6.1 Appendices
*   **Appendix A:** Inventory of Legacy Evergreen Reports (Gap Analysis Document)
*   **Appendix B:** Reporting Data Warehouse Technical Specification

#### 6.2 Index
*   Key Terms: ILS, PINES, Consortium, Template, Canned Report, Asynchronous Queue, Data Warehouse, Anonymization.

---
### **Approval**

This SRS document has been reviewed and is approved for development.

**Project Manager Signature:** ___________________________ **Date:** _______________

**PINES Reports Working Group Lead:** ____________________ **Date:** _______________

**Global System Administrator Representative:** _____________ **Date:** _______________