# Software Requirements Specification (SRS)
## Water Use Tracking (WUT) System
### For the Southwest Florida Water Management District (SWFWMD)

**Document Version:** 1.0
**Date:** [Date of Generation]
**Status:** Draft for Review

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Water Use Tracking (WUT) System. The intended audience includes project stakeholders, sponsors, business experts, technical development teams, quality assurance personnel, and future system maintainers. This document serves as the foundation for system design, development, testing, and acceptance.

### 1.2 Project Scope
The WUT System is a GIS-based decision-support application designed to spatially and temporally track, analyze, and report on regulatory and water resource management data. Its primary mission is to support the implementation, monitoring, and validation of the Southern Water Use Caution Area (SWUCA) Management Plan and SWUCA II Rules.

**In-Scope:**
*   Integration of data from existing District databases (Regulatory Database - RDB, Water Management Database - WMDB, GIS) into a unified Oracle-based platform.
*   Provision of web-based tools for internal staff and external customers to:
    *   View and search water use permits spatially and by attributes.
    *   Analyze permitted vs. actual water use (pumpage).
    *   Assess compliance status and trends.
    *   Track Net Benefit transactions (relocations, credits, lapsed quantities).
    *   Generate standardized and ad-hoc reports.
    *   Support impact analysis related to Minimum Flows and Levels (MFLs).
*   Implementation of a nightly data replication process from source systems (DB2) to the WUT Oracle database.
*   A configurable system managed by a WUT Administrator.

**Out-of-Scope (Non-Goals):**
*   Major changes to existing hardware or core software infrastructure.
*   Direct modification of source legacy systems (e.g., mainframe DB2 RDB/WMDB schemas or applications).
*   Implementation of all identified potential requirements in the initial system release.
*   Replacement of source systems; WUT is a read-only reporting and analysis layer.

### 1.3 Definitions, Acronyms, and Abbreviations
*   **FGDC:** Federal Geographic Data Committee
*   **GIS:** Geographic Information System
*   **MFL:** Minimum Flows and Levels
*   **MIA:** Minimum Aquifer Level
*   **RDB:** Regulatory Database
*   **SLA:** Service Level Agreement
*   **SWFWMD:** Southwest Florida Water Management District
*   **SWUCA:** Southern Water Use Caution Area
*   **WMDB:** Water Management Database
*   **WUT:** Water Use Tracking

### 1.4 References
*   SWUCA Management Plan
*   SWUCA II Rules
*   District IT Standards and Architecture Guidelines
*   Source System (RDB, WMDB) Data Dictionaries

### 1.5 Document Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its users, and constraints. Section 3 details the specific functional and non-functional requirements. Appendices may contain supplementary diagrams or data models.

## 2. Overall Description

### 2.1 Product Perspective
The WUT System is a new, independent web application that sits within the District's existing IT ecosystem. It is an "information consumer" that replicates and transforms data from authoritative source systems to provide enhanced analytical and spatial visualization capabilities.

**System Interfaces:**
1.  **Regulatory Database (RDB):** Inbound interface for nightly replication of permit, permittee, well, and compliance data.
2.  **Water Management Database (WMDB):** Inbound interface for nightly replication of pumpage, water level, and related resource data.
3.  **District GIS (ArcSDE/Oracle):** Bi-directional interface for serving spatial layers (permit boundaries, well points, base maps) and executing spatial queries.
4.  **District Authentication System:** Inbound interface for real-time user authentication and role provisioning.
5.  **Water Use Estimates Source (SAS/Excel):** Inbound interface for periodic import of estimated water use data for unmetered permits.
6.  **Web Client (Browser):** Outbound interface delivering HTML, JavaScript, maps, and reports to end-users.

### 2.2 User Classes and Characteristics
| User Class | Description | Key Characteristics & Needs |
| :--- | :--- | :--- |
| **Executive Sponsor** | Provides strategic direction and oversight. | Needs high-level summary reports, trend dashboards, and assurance that the system supports regulatory goals. |
| **Co-Sponsor** | Oversees operational aspects (data, modeling, rule compliance). | Requires accurate data integration, tools to verify rule adherence, and support for modeling inputs. |
| **Science Business Expert** | Performs water use estimation and MFL impact analysis. | Needs robust query tools, access to pumpage history, estimated use data, and spatial analysis functions. |
| **Regulatory Business Expert** | Evaluates permits and ensures compliance. | Requires detailed permit views, compliance status, Net Benefit summaries, and lapsed quantity reports. |
| **General WUT User (Internal)** | District staff from various departments. | Needs to view maps, search for permits, run standard reports, and export data. |
| **General WUT User (External)** | Public, consultants, permit holders. | Requires read-only access to public permit information, map viewing, and basic search capabilities (subject to security model). |
| **WUT Administrator** | Manages the WUT application. | Needs interfaces to configure system parameters, manage news, and monitor data loads. |
| **Water Use Estimator** | Maintains estimated water use data. | Requires ability to import, validate, and store estimated use datasets for unmetered permits. |
| **Technical Expert** | Supports system development and maintenance. | Needs well-documented APIs, database schemas, and operational logs. |

### 2.3 Operating Environment
*   **Software:** Microsoft .NET Framework, ESRI ArcGIS Server/API, Oracle Database 11g/12c, IIS Web Server.
*   **Hardware:** District-standard application and database servers.
*   **Network:** District intranet for primary access; potential external access via DMZ.
*   **Client:** Modern web browsers (e.g., Chrome, Firefox, Edge, Safari) with JavaScript enabled.

### 2.4 Design and Implementation Constraints
1.  Must leverage existing District IT infrastructure and adhere to established standards.
2.  Source system data structures (DB2) are considered immutable; replication must adapt to their schema.
3.  The system must comply with District security policies and integrate with the central authentication system.
4.  Spatial data and metadata must align with FGDC standards where applicable.
5.  The initial release scope is constrained to core functionality as defined in Section 3.

### 2.5 Assumptions and Dependencies
**Assumptions:**
*   Source systems (RDB, WMDB) will maintain adequate data quality and provide reliable change-data-capture for replication.
*   Necessary GIS layers (e.g., permit polygons) will be available and maintained in ArcSDE.
*   Stakeholders will be available for timely feedback during elaboration and testing phases.

**Dependencies:**
1.  Successful completion of necessary source system (RDB/WMDB) changes to expose required data.
2.  Availability of GIS resources for layer creation and maintenance.
3.  Integration support for the District Authentication System.

## 3. System Features and Requirements

### 3.1 Functional Requirements

#### 3.1.1 Data Integration & Management (FR-DIM)
*   **FR-DIM-01:** The system shall replicate changed data from the source Regulatory Database (RDB) to the WUT Oracle database via a scheduled nightly job.
*   **FR-DIM-02:** The system shall replicate changed data from the source Water Management Database (WMDB) to the WUT Oracle database via a scheduled nightly job.
*   **FR-DIM-03:** The replication process shall normalize and restructure source data into a format optimized for reporting and spatial analysis within the WUT schema.
*   **FR-DIM-04:** The system shall provide an administrative interface for the Water Use Estimator to import, validate, and store water use estimate data from external files (e.g., SAS, Excel).
*   **FR-DIM-05:** The system shall log all replication and data import activities, capturing success/failure status, record counts, and error details.

#### 3.1.2 Spatial Visualization & Map Interaction (FR-MAP)
*   **FR-MAP-01:** The system shall provide an interactive web map displaying base layers (e.g., imagery, boundaries) and water-use data layers (e.g., permit areas, well points).
*   **FR-MAP-02:** Users shall be able to select and activate/deactivate layers in the map legend.
*   **FR-MAP-03:** Users shall be able to pan, zoom, and identify features on the map by clicking.
*   **FR-MAP-04:** The system shall allow users to search for permits by drawing a polygon, rectangle, or circle on the map. (See Acceptance Criteria: Spatial Permit Search).
*   **FR-MAP-05:** Clicking a permit or well symbol on the map shall display a pop-up with key attributes and hyperlinks to detailed views.

#### 3.1.3 Permit Search & Discovery (FR-SRH)
*   **FR-SRH-01:** The system shall provide a search interface allowing users to find permits using criteria such as Permit Number, Permittee Name, Status, County, or SWUCA boundary.
*   **FR-SRH-02:** Search results shall be displayed in a list and simultaneously highlighted on the map.
*   **FR-SRH-03:** Users shall be able to select a permit from the search results list to navigate to its detailed view.

#### 3.1.4 Permit Detail & Analysis (FR-PER)
*   **FR-PER-01:** The system shall display a comprehensive view for a selected Water Use Permit, showing all core attributes (Permit Number, Status, Dates, Permittee, Total Quantity).
*   **FR-PER-02:** From the permit detail view, users shall be able to navigate to related information:
    *   **FR-PER-02.1:** List and map of associated wells/withdrawal points.
    *   **FR-PER-02.2:** Pumpage history (reported and estimated) in tabular and chart form.
    *   **FR-PER-02.3:** Compliance history and status.
    *   **FR-PER-02.4:** Net Benefit transaction summary. (See Acceptance Criteria: Net Benefit Reporting).
    *   **FR-PER-02.5:** Lapsed quantities summary.

#### 3.1.5 Reporting (FR-RPT)
*   **FR-RPT-01:** The system shall generate pre-defined reports (e.g., Permit Summary, Pumpage by Basin, Compliance Status Report).
*   **FR-RPT-02:** Users shall be able to export report results to standard formats (PDF, Excel, CSV).
*   **FR-RPT-03:** Users shall be able to export the current map view as an image (e.g., PNG, JPEG) or PDF document.
*   **FR-RPT-04:** The Net Benefit report shall allow aggregation by geographic area (e.g., SWUCA, County) and user-specified date range.

#### 3.1.6 System Administration (FR-ADM)
*   **FR-ADM-01:** The WUT Administrator shall be able to configure system-wide business rule parameters (e.g., thresholds, default date ranges).
*   **FR-ADM-02:** The WUT Administrator shall be able to post and manage news/announcements on the application homepage.
*   **FR-ADM-03:** The system shall provide a dashboard for monitoring the status of nightly replication jobs.

#### 3.1.7 Security & Authentication (FR-SEC)
*   **FR-SEC-01:** All users must authenticate via the District's central authentication system before accessing the WUT application.
*   **FR-SEC-02:** The system shall implement Role-Based Access Control (RBAC). Access to specific data sets (e.g., estimated pumpage, compliance details) and functions (e.g., data import) shall be restricted based on user roles.
*   **FR-SEC-03:** All authentication and authorization failures shall be logged.

### 3.2 Non-Functional Requirements

#### 3.2.1 Performance
*   **NF-PER-01:** The system shall render standard map views (with base layers and one data layer) within 5 seconds under normal load.
*   **NF-PER-02:** Simple permit search queries (by permit number or name) shall return results within 3 seconds.
*   **NF-PER-03:** Complex spatial queries (e.g., "find all permits in this polygon") shall return results within 10 seconds.

#### 3.2.2 Reliability & Availability
*   **NF-REL-01:** The application shall have an availability of 99% during core business hours (7:00 AM to 6:00 PM, Monday-Friday).
*   **NF-REL-02:** The nightly data replication process shall succeed in 99.9% of its scheduled executions.

#### 3.2.3 Security
*   **NF-SEC-01:** All communication between the client browser and web server shall use HTTPS (TLS 1.2+).
*   **NF-SEC-02:** User session timeouts shall be enforced after a period of inactivity not to exceed 30 minutes.
*   **NF-SEC-03:** The system shall be protected against common web vulnerabilities (e.g., OWASP Top 10).

#### 3.2.4 Usability
*   **NF-USA-01:** The user interface shall be consistent with other District web applications where possible.
*   **NF-USA-02:** The system shall provide context-sensitive help and tooltips for major features.

#### 3.2.5 Compliance
*   **NF-COM-01:** The system's data outputs must be defensible for use in permit decisions governed by SWUCA rules.
*   **NF-COM-02:** All spatial metadata shall be compliant with FGDC standards.

#### 3.2.6 Observability & Supportability
*   **NF-OBS-01:** The system shall log all application errors with sufficient detail (timestamp, user, operation, stack trace) to enable debugging.
*   **NF-OBS-02:** The system shall track and store anonymized usage statistics for key features (report runs, map interactions, search queries).

### 3.3 Acceptance Criteria
The following are specific, testable criteria derived from the functional requirements.

**AC-01: Spatial Permit Search**
*   **Given** an authenticated user is viewing the interactive map,
*   **When** the user activates the "Draw Search Area" tool and creates a polygon on the map,
*   **Then** the system shall visually highlight all Water Use Permits whose spatial boundary intersects the drawn polygon, and a results list shall be updated with the count and basic details of those permits.

**AC-02: Permit Detail Navigation**
*   **Given** a user has performed a search resulting in permits displayed on the map,
*   **When** the user clicks on a permit symbol on the map,
*   **Then** a pop-up window shall appear displaying the Permit Number, Permittee Name, Status, and a hyperlink labeled "View Full Details". Clicking this link shall navigate the user to the comprehensive permit detail view (FR-PER-01).

**AC-03: Net Benefit Summary for a Permit**
*   **Given** a user is viewing the detailed page for a specific Water Use Permit (Permit ID: X),
*   **When** the user clicks the "Net Benefit Summary" tab or link,
*   **Then** the system shall display a table listing all NetBenefitTransactions where `SourcePermitID = X` or `DestinationPermitID = X`, including columns for Transaction Type, Linked Permit, Quantity, and Effective Date.

**AC-04: Area-Based Net Benefit Report**
*   **Given** a user navigates to the Net Benefit Report tool,
*   **When** the user selects "SWUCA" as the geographic boundary and specifies a start date of 01/01/2020 and an end date of 12/31/2023,
*   **Then** the system shall generate a report showing the aggregate sum of all Net Benefit quantities (grouped by transaction type) for transactions effective within the date range and associated with permits located within the SWUCA boundary.

## 4. Appendices

### 4.1 Domain Model (Entity-Relationship Summary)
The core data model for the WUT system includes the following principal entities:
*   **WaterUsePermit:** The central entity. `PermitID` (PK), `PermitNumber` (Unique), `Status`, `IssueDate`, `ExpirationDate`, `PermitteeID` (FK), `TotalPermittedQuantity`.
*   **Permittee:** `PermitteeID` (PK), `Name`, `ContactInfo`.
*   **Well/WithdrawalPoint:** `WellID` (PK), `UID` (Unique), `PermitID` (FK), `Aquifer`, `Location` (Spatial Point), `ConstructionDetails`.
*   **PumpageRecord:** `RecordID` (PK), `WellID` (FK), `Month`, `Year`, `ReportedQuantity`, `EstimatedQuantity`.
*   **ComplianceRecord:** `ComplianceID` (PK), `PermitID` (FK), `ReportType`, `SubmissionDate`, `Status`.
*   **NetBenefitTransaction:** `TransactionID` (PK), `SourcePermitID` (FK), `DestinationPermitID` (FK), `Quantity`, `Type`, `EffectiveDate`.
*   **SpatialBoundary:** `BoundaryID` (PK), `Type` (e.g., SWUCA, MIA, County), `Geometry` (Spatial Polygon).
*   **BusinessRuleParameter:** `ParameterID` (PK), `Name`, `Value`, `EffectiveDate`.

*(Note: A full Entity-Relationship Diagram (ERD) should be developed during the design phase.)*

### 4.2 Risk Register
| ID | Risk Description | Probability | Impact | Mitigation Strategy | Owner |
| :--- | :--- | :--- | :--- | :--- | :--- |
| R-01 | Source system (RDB/WMDB) changes are delayed. | Medium | High | Collaborate closely with IRD team. Develop contingency to stage needed data within WUT. | Project Manager |
| R-02 | Evolving SWUCA rule interpretations affect requirements. | Medium | High | Maintain regular stakeholder review. Design configurable business rules (FR-ADM-01). | Co-Sponsors |
| R-03 | Performance degradation with large spatial queries. | High | Medium | Prototype and load test early. Implement database indexing, query optimization, and summary tables. | Technical Lead |
| R-04 | Data quality issues from source systems propagate to WUT. | High | High | Implement WUT data validation reports. Establish formal process to report errors back to source system owners. | Process Owner |

### 4.3 Open Issues and Decisions Pending
1.  Final prioritization of features for Phase 2 (post-initial release).
2.  Detailed RBAC matrix defining permissions for "External User" role.
3.  Formal SLA for system response time under external/public user load.
4.  Operational process for correcting source data errors identified via WUT.
5.  Final decision on implementation of advanced analytical tools (e.g., time-series "heat maps").

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Executive Sponsor | | | |
| Co-Sponsor | | | |
| Project Manager | | | |
| Technical Lead | | | |