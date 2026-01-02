# Software Requirements Specification (SRS)
## Water Use Permit Tracking and Analysis System (WUPTAS)
### Version 1.0

**Prepared for:** District Management
**Prepared by:** [Your Organization/Team Name]
**Date:** [Date]

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the Water Use Permit Tracking and Analysis System (WUPTAS). The primary purpose of this system is to provide automated spatial and temporal tracking, visualization, and analytical capabilities for water use permit data. This SRS serves as a contract between the stakeholders and the development team and will be the basis for system design, implementation, and verification.

### 1.2 Scope
The WUPTAS will be a comprehensive software application that supports the Southern Water Use Caution Area (SWUCA) Management Plan and rule validation efforts. While its analytical focus is on the SWUCA, its data coverage and core functionalities will encompass the entire District's jurisdiction.

**In-Scope:**
*   Development of a new application for spatial visualization, temporal tracking, and analysis of permit data.
*   Integration with existing District Regulatory, GIS, and Water Management databases as data sources.
*   Implementation of data structures and logic for calculating and storing derived data (e.g., lapsed quantities) not present in source systems.
*   Provision of tools for internal staff (evaluators, technical staff) and external customers (public, governments).

**Out-of-Scope:**
*   Modification of the core logic or data schemas of the existing source databases (Regulatory, GIS, Water Management).
*   Direct data entry for primary permit information; the system will be a consumer of authoritative source data.
*   Hardware procurement or fundamental changes to the District's established IT architecture.

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **SWUCA** | Southern Water Use Caution Area |
| **MFL** | Minimum Flows and Levels |
| **GIS** | Geographic Information System |
| **Pumpage** | The volume of water extracted, typically measured over a reporting period. |
| **Lapsed Quantity** | The portion of a permitted water allocation that has not been used and may be subject to recovery or reallocation. |
| **Net Benefit Calculation** | An analysis to determine if a proposed permit change results in a net ecological or hydrological benefit regarding MFLs. |

### 1.4 References
*   SWUCA Management Plan
*   District IT Architecture Standards
*   Data Dictionary for Regulatory Database (REG_DB_vX.X)
*   Data Dictionary for Water Management Database (WM_DB_vX.X)

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its users, and constraints. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements including performance, security, and design constraints.

## 2. Overall Description

### 2.1 Product Perspective
WUPTAS is a new, self-contained application that will reside within the District's existing IT ecosystem. It is dependent on several external systems for its data feed.

```
[External Regulatory DB] ---> [WUPTAS] <--- [External GIS DB]
          |                                      |
          |                                      |
          V                                      V
[External Water Management DB]           [District Authentication Service]
```

The system must coordinate with the administrators of these external databases for any required data view creation or change.

### 2.2 User Classes and Characteristics
| User Class | Characteristics & Key Needs |
| :--- | :--- |
| **Water Use Permit Evaluators** | Primary internal users. Require advanced spatial query tools, change tracking over time, and the ability to run Net Benefit Calculations. |
| **Technical Services Staff** | Require data aggregation tools for area-based analyses and reporting to support planning and rulemaking. |
| **Records and Data Staff** | Require tools to monitor data completeness, flag discrepancies, and ensure the system accurately reflects source data. |
| **External Customers (Public)** | Need read-only access to view generalized permit data, maps, and published reports. Requires an intuitive, non-technical interface. |
| **External Customers (Local Governments)** | Need tools to aggregate water use data within their jurisdictional boundaries. May require enhanced data export capabilities. |
| **System Administrator** | Responsible for user management, system configuration, and monitoring ETL (Extract, Transform, Load) job status. |

### 2.3 Operating Environment
*   **Hardware:** Must operate on the District's standard application servers and utilize existing database servers.
*   **Software:** Must be compatible with the District's standard web browser suite (Chrome, Edge), enterprise GIS software (e.g., ArcGIS Enterprise), and database management systems (e.g., Oracle, SQL Server).
*   **Network:** Must function within the District's internal network and be accessible via a public-facing portal for external users.

### 2.4 Design and Implementation Constraints
1.  **Data Dependency:** System design is constrained by the schema and update frequency of the external Regulatory, GIS, and Water Management databases.
2.  **Architectural Compliance:** The application must adhere to the District's current hardware, software, and security architecture standards. No new major infrastructure components are authorized.
3.  **Data Gap Handling:** The requirement for "lapsed quantities" and potentially other derived data fields necessitates that the application itself must include the business logic and database tables to calculate, store, and manage this information, as it is not available from source systems.

### 2.5 Assumptions and Dependencies
*   It is assumed that source databases (Regulatory, GIS) will provide stable, documented APIs or data export mechanisms.
*   The project's success is dependent on timely coordination with the external database management teams for any necessary source-side changes.
*   It is assumed that accurate spatial data (parcels, permit locations) exists within the District's GIS.

## 3. System Features & Functional Requirements

### 3.1 Feature 1: Spatial Visualization and Analysis
**Description:** The system shall provide an interactive map-based interface for visualizing and analyzing water use permit data.

| Requirement ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR1.1** | The system shall display permit locations as interactive points or polygons on a base map. | High |
| **FR1.2** | Users shall be able to filter the displayed permits by attributes (e.g., permit status, use type, quantity range, date range). | High |
| **FR1.3** | Users shall be able to select a permit on the map to view its detailed attributes in a pop-up or side panel. | High |
| **FR1.4** | The system shall provide standard map tools (zoom, pan, identify, measure). | Medium |
| **FR1.5** | Users shall be able to generate a printable map view with a legend, scale, and title. | Medium |

### 3.2 Feature 2: Temporal Tracking and Change Analysis
**Description:** The system shall track and visualize changes to permit data over time.

| Requirement ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR2.1** | The system shall maintain a historical record of changes to key permit fields: permitted quantity, use type, ownership, and status. | High |
| **FR2.2** | Users shall be able to view a timeline or history log for a selected permit. | High |
| **FR2.3** | The system shall calculate and display "lapsed quantities" based on business rules defined by District policy. | High |
| **FR2.4** | Users shall be able to compare two historical snapshots of a permit or a geographic area to visualize change. | Medium |

### 3.3 Feature 3: Net Benefit Calculation for MFL Impact
**Description:** The system shall provide a tool to analyze the net benefit of a proposed permit change relative to Minimum Flows and Levels.

| Requirement ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR3.1** | The system shall provide a dedicated workflow for inputting parameters of a proposed permit change (e.g., location, new quantity, use). | High |
| **FR3.2** | The system shall execute a pre-defined Net Benefit Calculation model using the input parameters and current environmental/hydrological data. | High |
| **FR3.3** | The system shall generate a standardized report detailing the calculation inputs, methodology, and result (Net Benefit, No Net Benefit, or Inconclusive). | High |
| **FR3.4** | All calculation runs and reports shall be saved to the system with a unique ID for future reference and audit. | Medium |

### 3.4 Feature 4: Data Aggregation and Reporting
**Description:** The system shall allow users to aggregate water use data for custom geographic areas.

| Requirement ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR4.1** | Users shall be able to define an area of interest by drawing on the map, uploading a shapefile, or selecting a pre-defined boundary (e.g., county, basin). | High |
| **FR4.2** | For a user-defined area, the system shall calculate and report aggregate totals for: total permitted quantity, total actual pumpage (by year), and total lapsed quantity. | High |
| **FR4.3** | Users shall be able to export aggregation results and associated spatial data to standard formats (PDF, Excel, CSV, Shapefile). | High |
| **FR4.4** | The system shall allow users to save frequently used areas (e.g., "SWUCA Boundary," "County X") for quick future analysis. | Low |

### 3.5 Feature 5: Compliance Monitoring
**Description:** The system shall facilitate the monitoring of permit compliance based on reported data.

| Requirement ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR5.1** | The system shall visually highlight permits on the map based on compliance status (e.g., compliant, non-compliant, report overdue). | High |
| **FR5.2** | Users shall be able to run a report listing all permits that are non-compliant or have missing pumpage/condition reports for a given period. | High |
| **FR5.3** | The system shall compare submitted annual pumpage against permitted quantities and flag significant or consistent overages. | Medium |

### 3.6 Feature 6: Data Management and Integration
**Description:** The system shall reliably ingest and manage data from external sources.

| Requirement ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR6.1** | The system shall execute scheduled, automated ETL jobs to synchronize permit master data from the Regulatory database. | High |
| **FR6.2** | The system shall execute scheduled ETL jobs to import actual pumpage and condition data from the Water Management database. | High |
| **FR6.3** | The system shall log all ETL job outcomes (success, failure, number of records processed) and provide an alert for failures. | Medium |
| **FR6.4** | The system shall provide an administrative interface to manually trigger or re-run ETL jobs if needed. | Low |

## 4. Non-Functional Requirements

### 4.1 Performance Requirements
*   **Map Rendering:** The initial map view with all active permits shall load within 5 seconds over the District's internal network.
*   **Query Response:** Simple attribute queries shall return results within 3 seconds. Complex spatial aggregations shall return results within 15 seconds.
*   **Concurrent Users:** The system shall support up to 50 concurrent internal users and 100 concurrent external portal users without significant degradation.

### 4.2 Safety & Security Requirements
*   All access shall be controlled via integration with the District's central authentication service (e.g., Active Directory).
*   Role-Based Access Control (RBAC) shall be implemented per the user classes defined in Section 2.2. External users shall have read-only access to public data sets.
*   All data transmissions, especially via the public portal, shall use TLS 1.2 or higher encryption.
*   The system shall not store sensitive personal information not already present in the source databases.

### 4.3 Software Quality Attributes
*   **Reliability:** System uptime shall be 99.5% during core business hours (7 AM - 6 PM, Mon-Fri).
*   **Usability:** The interface for External Customers shall be designed for ease of use, requiring no formal training. Internal user interfaces shall follow District UX standards.
*   **Maintainability:** The system shall be documented with technical design documents and source code comments. It shall use the District's standard development frameworks where possible.
*   **Data Integrity:** The system shall ensure referential integrity between its internal tables and shall provide validation checks on calculated fields (e.g., lapsed quantity).

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| Quality Assurance | | | |