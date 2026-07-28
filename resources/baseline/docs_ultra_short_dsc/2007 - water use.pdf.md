# Software Requirements Specification (SRS)
## Water Use Tracking and Analysis System (WUTAS)
### Version 1.0

**Prepared by:** [Author Name/Team]
**Date:** [Date]
**For:** [District Name] Water Management District

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the Water Use Tracking and Analysis System (WUTAS). The primary purpose of this system is to provide a GIS-based decision-support tool for tracking, analyzing, and reporting on water use permit data spatially and temporally. It is specifically designed to support the validation of the Southern Water Use Caution Area (SWUCA) Recovery Strategy rules. This specification is intended for use by the project stakeholders, development team, quality assurance team, and project management.

### 1.2 Scope
The WUTAS will integrate data from existing legacy systems—the Regulatory Database (RDB), Water Management Database (WMDB), and Geographic Information System (GIS)—to create a centralized analysis layer. The system is strictly for **reporting, analysis, and decision support**; it will **not** create, update, or delete records within the source regulatory or water management databases. The scope includes:
*   A web-based user interface and integration with ArcGIS ArcView.
*   Core functions for viewing, searching, mapping, and reporting on permit data.
*   Functionality to support SWUCA rule validation, including lapsed quantity tracking and net benefit analysis.
*   Role-based access for general users, regulatory evaluators, and system administrators.

**Out of Scope:**
*   Modification of source data in the RDB, WMDB, or GIS.
*   Advanced analytics such as complex water quality trend calculations or population modeling (deferred to Phase 2).
*   Direct permit application processing or regulatory workflow management.

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **GIS** | Geographic Information System |
| **SWUCA** | Southern Water Use Caution Area |
| **RDB** | Regulatory Database |
| **WMDB** | Water Management Database |
| **WUP** | Water Use Permit |
| **WUTAS** | Water Use Tracking and Analysis System |
| **ArcSDE** | ArcGIS Spatial Database Engine |

### 1.4 References
*   SWUCA Recovery Strategy & Management Plan
*   District Technical Architecture Standards
*   District Change Management Procedures

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its users, and constraints. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements, including performance, security, and supportability.

## 2. Overall Description

### 2.1 Product Perspective
The WUTAS is a new, independent system that operates as a "decision-support layer" atop three existing legacy systems. It consumes replicated, read-only data from these sources to provide integrated views and analytical capabilities not present in the source systems.

**System Interfaces:**
*   **Data Source Interfaces:** Nightly replication processes from IBM DB2 (RDB, WMDB) and HP-UX ArcSDE/Oracle (GIS) into the WUTAS operational data store (Oracle).
*   **User Interfaces:**
    *   Primary: Web-based application accessible via standard browsers.
    *   Secondary: Integration with ArcGIS ArcView desktop for advanced spatial operations.
*   **Software Interfaces:** Must operate within the District's standard .NET framework and Oracle database environment.
*   **Communication Interfaces:** HTTP/HTTPS for web access; database connectivity protocols for data replication.

### 2.2 Product Functions (High-Level)
1.  Permit Data Exploration: Search, view, and retrieve water use permit details.
2.  Spatial Analysis & Visualization: Display permits and related spatial features (e.g., basins, wellfields) on interactive maps with thematic styling.
3.  Reporting: Generate standardized (canned) and user-defined (ad-hoc) reports on permit status, pumpage history, and compliance.
4.  SWUCA Rule Support: Track the movement and allocation of lapsed water quantities. Calculate and present net benefit analyses for proposed permit changes.
5.  Data Maintenance: Allow authorized users to view and maintain water use estimates for unmetered permits and manage system reference data.

### 2.3 User Characteristics
| User Class | Expertise | Key Tasks |
| :--- | :--- | :--- |
| **General WUT User** (Staff/Public) | Basic computer literacy. Familiar with web maps and simple searches. | View public maps, search for permit information, run read-only reports. |
| **WUP Evaluator** (Regulatory Staff) | Subject matter expert in hydrology and regulations. Proficient with GIS concepts. | Analyze permit applications in spatial context, review adjacent permit history, run trend analyses, perform net benefit calculations. |
| **Water Use Estimator** | Specialized staff with knowledge of estimation methodologies. | Input, update, and validate estimated water use data for unmetered permits. |
| **WUT Administrator** | IT-literate staff familiar with system administration. | Manage user roles and permissions, configure system parameters, post system news, monitor data replication status. |

### 2.4 Constraints
*   **Technical:** Must be developed using the District's approved technology stack (.NET, Oracle) and deployable within its existing hardware/network infrastructure.
*   **Data:** System functionality is dependent on the accuracy, completeness, and nightly availability of data from the source RDB, WMDB, and GIS databases.
*   **Regulatory:** System outputs must align with statutory definitions and time frames governing permit evaluation.
*   **Architectural:** The system shall be read-only with respect to source systems. All analytical data must be derived from the replicated data store.

### 2.5 Assumptions and Dependencies
*   **Assumption:** The source systems (RDB, WMDB, GIS) will remain stable and operational, and will contain the necessary data fields (e.g., lapsed quantity flags) required for WUTAS functionality.
*   **Assumption:** A nightly batch process for data replication from source systems to the WUTAS database will be established and maintained by the IT operations team.
*   **Dependency:** Successful implementation is dependent on the continued support and compatibility of third-party software (ArcGIS, Oracle, .NET).

## 3. Specific Requirements

### 3.1 External Interface Requirements
#### 3.1.1 User Interfaces
*   **UI-01:** The web interface shall be intuitive, consistent with District web standards, and accessible via modern browsers (Chrome, Edge, Firefox).
*   **UI-02:** All data displayed to the user shall show descriptive values (e.g., "Active") and not internal system codes (e.g., "A").
*   **UI-03:** The ArcView integration shall allow a user to launch context-specific map views from the web application and pass relevant permit identifiers.

#### 3.1.2 Hardware Interfaces
*   **HW-01:** The system shall operate on the District's existing server hardware. No specific new client hardware is required beyond standard workstations.

#### 3.1.3 Software Interfaces
*   **SI-01:** The application database shall be Oracle 19c or later.
*   **SI-02:** The application layer shall be built using the District's standard .NET framework.
*   **SI-03:** The system shall read spatial data via connections to the replicated ArcSDE geodatabase.

#### 3.1.4 Communications Interfaces
*   **CI-01:** The web application shall communicate over HTTPS.
*   **CI-02:** Database replication shall use secure, authenticated connections as defined by District DBA standards.

### 3.2 Functional Requirements
#### 3.2.1 Module: Permit Search and View
*   **FR-01:** The system shall allow users to search for water use permits by permit number, holder name, location (county, basin), and status.
*   **FR-02:** The system shall display a detailed permit view containing all relevant data from the integrated sources (RDB, WMDB, GIS), including permit details, attached conditions, well information, and historical pumpage.

#### 3.2.2 Module: Interactive Mapping
*   **FR-03:** The system shall display an interactive web map with base layers (e.g., streets, aerial imagery) and permit data layers.
*   **FR-04:** Users shall be able to select a permit on the map to view its summary details or click to navigate to the full permit detail view (FR-02).
*   **FR-05:** The system shall allow users to theme (color-code) permits on the map based on attributes such as status, water use category, or pumpage volume.

#### 3.2.3 Module: Reporting
*   **FR-06:** The system shall provide a set of pre-defined (canned) reports (e.g., "Permit Summary by Basin," "Annual Pumpage by Category").
*   **FR-07:** The system shall provide an ad-hoc report builder allowing authorized users to select data fields, apply filters, and define grouping/sorting to create custom reports.
*   **FR-08:** All reports shall be exportable to standard formats (PDF, Excel).

#### 3.2.4 Module: SWUCA Rule Support
*   **FR-09:** The system shall provide a dedicated interface to trace the movement of lapsed water quantities from a source permit to subsequent permits.
*   **FR-10:** The system shall calculate and display a "Net Benefit" analysis for a proposed permit change, comparing projected impacts to minimum aquifer levels against a baseline, as defined by SWUCA rules.

#### 3.2.5 Module: System Administration
*   **FR-11:** The system shall implement role-based security controlling access to functions (View, Analyze, Administer) and data sensitivity levels.
*   **FR-12:** Authorized administrators shall be able to manage user accounts and assign roles.
*   **FR-13:** Authorized estimators shall be able to input and update annual water use estimates for permits designated as unmetered.

### 3.3 Non-Functional Requirements

#### 3.3.1 Performance Requirements
*   **PER-01:** The system shall support concurrent use by at least 50 users without significant degradation in response time.
*   **PER-02:** Critical user queries (e.g., permit search, opening a standard report) shall return results within 5 seconds under normal load 95% of the time.
*   **PER-03:** Data from source systems is considered current as of the last successful nightly replication. Real-time data is not required.

#### 3.3.2 Reliability & Availability
*   **REL-01:** The web application shall have an operational availability of 99% during standard business hours (7 AM - 7 PM, Mon-Fri).
*   **REL-02:** Query results for the same parameters must be consistent and reproducible when run at different times (assuming no underlying data change between runs).

#### 3.3.3 Supportability
*   **SUP-01:** The system shall be designed and documented according to the District's programming standards and guidelines.
*   **SUP-02:** The system shall integrate with the District's existing change management and version control processes.
*   **SUP-03:** All application logs shall be written to a centralized location following District logging standards.

#### 3.3.4 Usability & Security
*   **USA-01:** The system shall provide context-sensitive help and tooltips for major features and field definitions.
*   **SEC-01:** Access shall be controlled via integration with the District's central authentication system (e.g., Active Directory).
*   **SEC-02:** User roles (General User, Evaluator, Estimator, Administrator) shall dictate accessible menus, functions, and data sensitivity levels.

## 4. Appendices

### 4.1 Acceptance Criteria
Formal acceptance of the system will be based on successful demonstration that all requirements outlined in this document (mapped to verified business use cases) have been met. A dedicated User Acceptance Test (UAT) plan will be executed, focusing on the core functions of tracking, reporting, mapping, and SWUCA rule support.

### 4.2 Deferred Features
The following features are explicitly identified for future releases and are not part of the acceptance criteria for the initial release:
*   Water quality trend analysis and visualization.
*   Complex demographic or population modeling linked to water use.
*   Predictive analytics for water demand.

---
*Document End*