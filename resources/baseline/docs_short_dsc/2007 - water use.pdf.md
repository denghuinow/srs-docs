# Software Requirements Specification (SRS)
## Water Use Tracking (WUT) System
**Document Version:** 1.0
**Date:** [Date of Generation]
**Prepared for:** Southwest Florida Water Management District
**Prepared by:** [Your Name/Team]

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Water Use Tracking (WUT) System. The intended audience includes project stakeholders, developers, testers, and project managers. This document serves as the foundation for system design, implementation, verification, and project management.

#### 1.2 Scope
The WUT System is a GIS-based application designed to spatially and temporally track and analyze regulatory and resource management data. Its primary purpose is to support the Southern Water Use Caution Area (SWUCA) Management Plan and validate SWUCA II Rules by providing automated tools for monitoring water use trends and compliance.

**In-Scope Features:**
*   Spatial and temporal analysis of permitted and actual water use within the SWUCA.
*   Data aggregation tools for defined geographic areas (e.g., counties, watersheds, user-defined polygons).
*   Support for water use permit evaluation and compliance monitoring workflows.
*   Integration of data from existing Regulatory (DB2), Water Management, and GIS (ArcSDE) databases.
*   Spatial analysis, visualization, and reporting capabilities for internal staff and external customers via a web interface.

**Out-of-Scope Items:**
*   Structural modifications to existing mainframe DB2 databases or legacy applications.
*   Development of new hardware or core software infrastructure.
*   Comprehensive water quality data collection or ETL processes into the Water Management Database.
*   Real-time data synchronization; the system will operate on replicated data updated on a nightly basis.
*   Implementation of all potential long-term requirements in the initial release (phased approach).

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **SWFMD / District** | Southwest Florida Water Management District |
| **WUT** | Water Use Tracking System |
| **SWUCA** | Southern Water Use Caution Area |
| **GIS** | Geographic Information System |
| **ArcSDE** | ArcGIS Spatial Database Engine |
| **ETL** | Extract, Transform, Load |
| **SRS** | Software Requirements Specification |

#### 1.4 References
*   SWUCA Management Plan
*   SWUCA II Rules
*   District IT Architecture and Security Standards
*   District Change Management Procedures

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its users, and constraints. Section 3 details the specific functional and non-functional requirements. Appendices may contain supplementary diagrams or data models.

### 2. Overall Description

#### 2.1 Product Perspective
The WUT System is a new application that will integrate as a component within the District's existing IT ecosystem. It will depend on data from source systems (Regulatory DB2, Water Management DB) via a replicated Oracle reporting database and spatial data served via ArcSDE. It will present a web-based interface to users.

**System Interfaces:**
*   **Database Interface:** Read-only access to the Oracle reporting database (nightly replication from DB2) and ArcSDE geodatabases.
*   **User Interface:** Web-based interface accessible via District intranet for internal users and via public internet (with appropriate security) for external users.

#### 2.2 Product Functions (High-Level)
1.  **Spatial Data Visualization:** Display water use permits, actual usage, and related features on interactive maps.
2.  **Temporal Trend Analysis:** Chart and analyze water use data over user-selected time periods.
3.  **Geographic Aggregation:** Calculate sum, average, and other statistics of water use for selected geographic areas.
4.  **Reporting:** Generate standardized and ad-hoc reports in printable/downloadable formats (e.g., PDF, Excel).
5.  **Data Quality Tools:** Provide interfaces for staff to identify, flag, and review potential data discrepancies.
6.  **Query and Search:** Allow users to find permits, locations, and data based on multiple criteria.

#### 2.3 User Characteristics
| Stakeholder Category | Representative Role | Key Characteristics / Skills |
| :--- | :--- | :--- |
| **Executive Sponsors** | Bruce Wirth | Strategic oversight, non-technical, requires high-level summaries and reports. |
| **Science Business Experts** | Albert Bond | Hydrological modeling expertise, requires access to raw and aggregated data for analysis. |
| **Regulatory Business Experts** | Christine Jackson | Deep knowledge of permitting rules, requires tools to assess compliance and spatial impact. |
| **Technical Experts** | Steven Dicks | GIS and DB expertise, will provide support and may perform advanced system functions. |
| **Internal Operational Users** | Permit Evaluators, Records Staff | Daily system users, require efficient, task-oriented workflows for evaluation and data QC. |
| **External Customers** | Local Government Staff | Public users, require intuitive, self-service access to maps and standard reports. |

#### 2.4 Constraints
1.  **Technical:** The system must not require structural changes to source DB2, Oracle, or ArcSDE databases.
2.  **Architectural:** Must operate within the District's approved hardware, software, and network architecture.
3.  **Data Latency:** System data will be as of the last successful nightly replication job; real-time data is not required.
4.  **Regulatory:** System workflows must support adherence to statutory time frames for permit evaluation.
5.  **Procedural:** Development and deployment must comply with District programming standards and change management procedures.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** The nightly data replication process from mainframe to Oracle reporting database is reliable and will continue.
*   **Assumption:** Required spatial data layers (county boundaries, watersheds, SWUCA boundary) are maintained and available in ArcSDE.
*   **Dependency:** Project success is dependent on subject matter expert (SME) availability for requirement clarification and user acceptance testing.

### 3. Specific Requirements

#### 3.1 Functional Requirements

**3.1.1 Spatial Visualization and Analysis**
*   **FR-1:** The system shall display an interactive map with base layers (e.g., streets, aerial imagery, county lines).
*   **FR-2:** The system shall allow users to toggle the display of thematic data layers including:
    *   Active Water Use Permits
    *   Historical Actual Water Use points/locations
    *   SWUCA Boundary
    *   Watershed boundaries
*   **FR-3:** The system shall allow users to select a geographic area of interest using predefined boundaries (county, watershed) or by drawing a custom polygon.
*   **FR-4:** The system shall, for a selected area, list all water use permits and their attributes in a table view.

**3.1.2 Data Aggregation and Trend Analysis**
*   **FR-5:** The system shall calculate the total permitted pumpage (annual quantity) for a user-selected geographic area and time period.
*   **FR-6:** The system shall calculate the total reported actual water use for a user-selected geographic area and time period.
*   **FR-7:** The system shall generate a line or bar chart showing aggregated water use (permitted or actual) over a user-defined time series (e.g., 1990-2023).

**3.1.3 Reporting**
*   **FR-8:** The system shall provide a set of pre-configured standard reports (e.g., "SWUCA Annual Water Use Summary").
*   **FR-9:** The system shall allow users to generate an ad-hoc report based on current map view, selected area, and applied filters.
*   **FR-10:** The system shall export reports in PDF and Excel (.xlsx) formats.

**3.1.4 Data Quality and Management**
*   **FR-11:** The system shall provide a dedicated interface for Records staff to identify permits with missing or outlier data based on configurable rules.
*   **FR-12:** The system shall allow authorized users to flag a data record for review, adding a comment, without directly editing the source database.

**3.1.5 User Access and Security**
*   **FR-13:** The system shall authenticate users against the District's active directory.
*   **FR-14:** The system shall implement role-based access control (RBAC) with at least the following roles:
    *   **Public User:** Read-only access to public maps and standard reports.
    *   **Internal User:** Read-only access to all internal data and tools.
    *   **Data Steward:** Internal User privileges + ability to flag data for QC.
    *   **Administrator:** Full system configuration and user role management.

#### 3.2 Non-Functional Requirements

**3.2.1 Performance**
*   **NF-1:** The map interface shall load initial view and base layers within 5 seconds over the District intranet.
*   **NF-2:** A spatial query for permits within a county boundary shall return results within 10 seconds.
*   **NF-3:** Aggregation calculations for a 10-year period within a major watershed shall complete within 15 seconds.

**3.2.2 Usability**
*   **NF-4:** The web interface shall conform to WCAG 2.1 Level AA accessibility standards.
*   **NF-5:** Core user tasks (e.g., generate a standard report for a selected county) shall be achievable with 3 or fewer clicks from the homepage for authenticated internal users.

**3.2.3 Reliability & Availability**
*   **NF-6:** The system shall have 99% operational availability during standard business hours (7:00 AM - 6:00 PM, Mon-Fri).
*   **NF-7:** The system shall gracefully handle source database unavailability by displaying a clear maintenance message.

**3.2.4 Security**
*   **NF-8:** All user sessions shall timeout after 30 minutes of inactivity.
*   **NF-9:** All data transmitted over public networks shall be encrypted using TLS 1.2 or higher.

### 4. Appendices

#### 4.1 User Stories Mapping to Requirements
| User Story | Mapped Functional Requirements |
| :--- | :--- |
| 1. As a Permit Evaluator, I want to view spatial impacts... | FR-1, FR-2, FR-3, FR-4 |
| 2. As a Technical Services Staff, I want to aggregate permitted pumpage... | FR-3, FR-5, FR-7 |
| 3. As a Records Staff, I want tools for quality control... | FR-11, FR-12 |
| 4. As a Resource Conservation member, I want to access data for model calibration... | FR-4, FR-6, FR-9, FR-10 |
| 5. As an Executive Staff, I want to generate standard reports... | FR-8, FR-10 |
| 6. As an External Customer, I want to interact with web-accessible maps... | FR-1, FR-2, FR-8, FR-13, FR-14 (Public Role) |

#### 4.2 Undecided Issues & Open Questions
1.  **Release Prioritization:** The priority of requirements marked for subsequent releases is to be finalized post-initial UAT.
2.  **Data Update Protocols:** Detailed procedures for updating reference data (e.g., new watershed boundaries) need to be defined.
3.  **Net Benefit Calculations:** Specific algorithms and tracking requirements for Net Benefit metrics require further business rule definition.
4.  **Security Role Granularity:** Detailed permissions within the "Internal User" and "Data Steward" roles need to be specified.
5.  **Data Gaps:** Mitigation strategies for requirements dependent on currently unavailable data (e.g., "relocated quantities") are pending data source analysis.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Business Analyst | | | |
| Lead Developer | | | |
| Quality Assurance Lead | | | |