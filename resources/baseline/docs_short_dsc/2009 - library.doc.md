# Software Requirements Specification (SRS)
## Management Processes for Integrated Library System (ILS)
### For the Evergreen ILS, PINES Consortium, Georgia

**Document Version:** 1.0  
**Date:** [Date of Generation]  
**Status:** Draft for Review  
**Project Sponsor:** PINES Consortium  
**Primary Author:** [Name/Title]

---

## 1. Introduction

### 1.1 Purpose
This document provides a comprehensive specification for the development of enhanced management reporting and analytics modules within the Evergreen Integrated Library System (ILS) used by the Georgia PINES consortium. It is intended for use by project managers, software developers, quality assurance testers, system administrators, and stakeholder representatives to ensure a common understanding of the system's functional and non-functional requirements.

### 1.2 Scope
This project focuses on augmenting the existing Evergreen ILS with advanced data-driven management capabilities. The core deliverables include a user-friendly reporting interface, configurable report templates, data archiving mechanisms, and operational utilities designed to support the management of library services, collections, and patron demographics across a large, multi-branch consortium.

**In-Scope Components:**
*   Query and Reporting Interface
*   Management Report Generation (Inventory, Financial, Transactional, Demographic)
*   Transaction Data Archiving with Privacy Protections
*   Report Types: Pre-defined ("Canned"), On-Demand, and Ad-Hoc
*   Operational Utilities: Batch Item Transfer and Record Purging Identification

**Out-of-Scope Components:**
*   Detailed UI/UX design specifications and data structure diagrams (to be handled iteratively).
*   Online Public Access Catalog (OPAC) functionality.
*   Acquisitions and Cataloging module requirements.
*   Prescriptive software development process definitions.
*   Modifications to core ILS enterprise data structures.

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **ILS** | Integrated Library System. The enterprise software for managing library operations. |
| **PINES** | Public Information Network for Electronic Services. Georgia's statewide resource-sharing consortium. |
| **Evergreen** | The open-source ILS software used by the PINES consortium. |
| **OPAC** | Online Public Access Catalog. The public-facing search interface. |
| **MARC21** | Machine-Readable Cataloging format, the standard for bibliographic data. |
| **EDIFACT** | Electronic Data Interchange For Administration, Commerce, and Transport. A standard for electronic data interchange. |
| **Canned Report** | A pre-defined, parameter-driven report template provided with the system. |
| **Ad-Hoc Report** | A report created by a user using an open-template query builder. |

### 1.4 References
*   Evergreen ILS Official Documentation
*   PINES Consortium Strategic Plan
*   Georgia State Library Standards and Auditing Requirements
*   WCAG 2.1 Accessibility Guidelines

### 1.5 Overview
The remainder of this SRS is structured as follows: Section 2 provides an overall description of the product, its users, and constraints. Section 3 details the specific functional and non-functional requirements. Appendices may contain supplementary information.

## 2. Overall Description

### 2.1 Product Perspective
This project is a major enhancement module for the existing Evergreen ILS. It is a server-based application that interacts directly with the ILS's relational database. It must integrate seamlessly with the existing staff client and web-based administration interfaces.

### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Staff** | General library employees. Varied technical skill. | Efficient access to pre-defined reports for daily tasks (weeding, holds). |
| **Library Manager** | Supervises a single branch/department. Decision-maker for local collection. | Analytical reports on collection use, space, and demographics for operational optimization. |
| **Library Director** | Executive leadership. Sets strategic priorities. | High-level, aggregated reports (e.g., board reports) for planning and advocacy. |
| **Local System Administrator** | IT/management staff at a library system level. | Granular control over report permissions and data access for staff within their jurisdiction. |
| **Global System Administrator** | Consortium-level technical and managerial staff. | System-wide configuration, data archiving for privacy/compliance, and consortium-level statistical reporting. |
| **Patron** | End-user of library services. | *Indirect stakeholder;* their privacy must be protected by data archiving processes. |

### 2.3 Operating Environment
*   **Server:** Linux or Solaris operating systems.
*   **Client Access:** Standard modern web browsers (Chrome, Firefox, Safari, Edge) and Windows-compatible client software where applicable. Must support assistive technologies (screen readers).
*   **Database:** Fully relational database back-end (PostgreSQL, as used by Evergreen).
*   **Output:** Standards-compliant HTML, CSV, PDF, and potentially other standard formats (e.g., XLSX).

### 2.4 Design and Implementation Constraints
1.  **Technical:** Must not alter core Evergreen ILS data structures. Must use existing authentication/authorization frameworks (security groups/roles).
2.  **Integration:** Must interface with external vendor systems via published APIs and support standard data formats (MARC21, EDIFACT).
3.  **Operational:** Must include a dedicated development and training environment with a documented process for migrating report templates and configurations to production.
4.  **Performance:** Must support concurrent report generation from 286 locations during business hours without degrading core ILS functions (circulation, cataloging).

### 2.5 Assumptions and Dependencies
*   The underlying Evergreen ILS core is stable and provides accurate, timely data.
*   Stakeholders will participate in an iterative process to finalize the "canned" report list and UI design details.
*   Sufficient server resources will be allocated to handle the processing load of analytical queries.

## 3. System Requirements

### 3.1 Functional Requirements

#### 3.1.1 Reporting Interface (FR-UI)
*   **FR-UI-01:** The system shall provide a web-based interface for discovering, creating, scheduling, and running reports.
*   **FR-UI-02:** The interface shall include a query builder tool allowing authorized users to create ad-hoc reports by selecting data fields, applying filters, and defining sort logic without writing SQL.
*   **FR-UI-03:** The interface shall allow users to save ad-hoc query configurations as reusable templates.

#### 3.1.2 Report Generation & Types (FR-REP)
*   **FR-REP-01:** The system shall generate management reports for the following categories:
    *   **Inventory Control:** (e.g., collection age, circulation activity by location, lost items).
    *   **Financial Records:** (e.g., fines accrued/collected, fee-based transaction summaries).
    *   **Transaction Analysis:** (e.g., circulation trends, hold request success rates, peak usage times).
    *   **Patron Demographics:** (e.g., registration trends, active user counts by defined geographic or demographic segments).
*   **FR-REP-02:** The system shall provide a library of pre-defined "canned" reports (list TBD, see Undecided Issues).
*   **FR-REP-03:** The system shall support on-demand execution of any report (canned or user-template).
*   **FR-REP-04:** The system shall allow authorized users to schedule reports for automatic generation and distribution (e.g., via email).

#### 3.1.3 Permissions and Security (FR-SEC)
*   **FR-SEC-01:** Access to reports, data fields, and reporting functions shall be controlled by configurable permissions assigned to security groups or roles.
*   **FR-SEC-02:** A **Local System Administrator** shall be able to restrict which reports and specific data fields (e.g., patron personal identification numbers) are accessible to staff within their administrative domain.
*   **FR-SEC-03:** All report access and execution shall be logged for auditing purposes.

#### 3.1.4 Data Archiving (FR-ARC)
*   **FR-ARC-01:** The system shall provide a utility for a **Global System Administrator** to archive detailed transaction records (e.g., circulation history).
*   **FR-ARC-02:** The archiving process shall anonymize or purge personally identifiable information (PII) from the archived records to protect patron privacy.
*   **FR-ARC-03:** Archived data shall retain sufficient non-identifiable demographic and statistical information (e.g., patron age range, zip code, material type) to support longitudinal analysis.
*   **FR-ARC-04:** The duration for which detailed, non-archived transaction history is maintained shall be configurable (X days, where X is TBD).

#### 3.1.5 Operational Utilities (FR-UTIL)
*   **FR-UTIL-01:** The system shall provide a utility to select and transfer batches of items (e.g., 50 books) from one branch to another, updating item status and location in the ILS.
*   **FR-UTIL-02:** The transfer utility shall allow for setting a return date/condition, after which items can be identified for return to their original location. The specific reversion method is TBD.
*   **FR-UTIL-03:** The system shall provide a utility to identify bibliographic or item records that meet configurable criteria for purging (e.g., no circulation in Y years, no items attached), subject to permissions.

#### 3.1.6 Report Processing (FR-PROC)
*   **FR-PROC-01:** The system shall manage a report processing queue for on-demand and scheduled reports.
*   **FR-PROC-02:** The queue shall have a prioritization mechanism (details TBD) to manage system load.

### 3.2 Non-Functional Requirements

#### 3.2.1 Performance Requirements (NFR-PER)
*   **NFR-PER-01:** The reporting interface shall load in under 3 seconds for 95% of page requests during peak consortium hours.
*   **NFR-PER-02:** Execution of standard pre-defined reports shall complete within 2 minutes for 95% of executions, given typical dataset sizes for a single library system.
*   **NFR-PER-03:** The system shall support at least 50 concurrent report-generation requests without causing a >10% performance degradation in core ILS transaction processing (circulation check-in/out).

#### 3.2.2 Usability Requirements (NFR-USA)
*   **NFR-USA-01:** The reporting interface shall conform to WCAG 2.1 Level AA guidelines for accessibility.
*   **NFR-USA-02:** Staff users shall be able to locate and run a common pre-defined report with no more than 3 clicks from the main reporting dashboard.
*   **NFR-USA-03:** Context-sensitive help or tooltips shall be available for all report parameters and data field selections.

#### 3.2.3 Reliability & Availability (NFR-REL)
*   **NFR-REL-01:** The reporting modules shall have an availability of 99.5% during all library open hours across the consortium.
*   **NFR-REL-02:** A failed report generation job shall not crash the reporting service or affect other unrelated jobs.

#### 3.2.4 Security & Compliance (NFR-SEC)
*   **NFR-SEC-01:** All financial reports generated shall adhere to standard governmental accounting practices (GAP) and be sufficient for state audit requirements.
*   **NFR-SEC-02:** The data archiving process shall be documented and provide an audit trail to verify the anonymization of PII.

#### 3.2.5 Implementation Constraints (NFR-IMP)
*   **NFR-IMP-01:** The system shall be implemented as an enhancement to the existing Evergreen codebase, following its development standards and version control practices.

## 4. Appendices

### 4.1 User Stories Mapping to Requirements
| User Story | Mapped Functional Requirements |
| :--- | :--- |
| 1. Library Manager: Analyze collection use/space | FR-REP-01 (Inventory), FR-UI-02/03 (Ad-Hoc) |
| 2. Staff: Run pre-defined reports | FR-REP-02, FR-UI-01 |
| 3. Local Admin: Control report access | FR-SEC-01, FR-SEC-02 |
| 4. Library Director: Pre-defined board reports | FR-REP-02, FR-REP-04 |
| 5. Global Admin: Archive/anonymize data | FR-ARC-01, FR-ARC-02, FR-ARC-03 |
| 6. Staff: Batch item transfer utility | FR-UTIL-01, FR-UTIL-02 |

### 4.2 Undecided Issues & Open Questions
1.  **Query Tool UI:** The specific widgets, layout, and interaction patterns for the ad-hoc query builder (FR-UI-02) require user experience research and iterative design.
2.  **Transaction History Duration:** The configurable value `X` in FR-ARC-04 must be determined based on legal, operational, and storage considerations.
3.  **Canned Report Catalog:** A final, prioritized list of pre-defined reports (FR-REP-02) must be developed in consultation with all stakeholder groups.
4.  **Transfer Reversion Logic:** The method (automatic batch vs. manual list) and criteria (date passed, scan trigger) for reverting transferred items (FR-UTIL-02) needs specification.
5.  **Queue Prioritization:** The algorithm for prioritizing reports in the processing queue (FR-PROC-02) (e.g., by user role, report size, schedule time) must be defined.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| Quality Assurance Lead | | | |
| Global System Administrator (Stakeholder) | | | |