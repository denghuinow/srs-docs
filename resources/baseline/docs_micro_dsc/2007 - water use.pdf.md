# Software Requirements Specification (SRS)
## SWUCA Management & Regulatory Tracking System (SMaRTS)
### For Southwest Florida Water Management District

**Document Version:** 1.0  
**Date:** [Current Date]  
**Prepared for:** Southwest Florida Water Management District  
**Prepared by:** [Your Organization/Team Name]

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the SWUCA Management & Regulatory Tracking System (SMaRTS). The primary purpose of SMaRTS is to provide a unified, GIS-based platform for the spatial and temporal tracking, visualization, and analysis of regulatory and water resource management data. This system is critical for supporting the implementation, monitoring, and reporting requirements of the Southern Water Use Caution Area (SWUCA) Management Plan.

### 1.2 Document Conventions
*   **Requirements IDs:** Follow the format `FR-XXX` for Functional Requirements and `NFR-XXX` for Non-Functional Requirements.
*   **Priority:** (H) High, (M) Medium, (L) Low. High-priority items are essential for minimum viable product (MVP) release.
*   **Keywords:** `MUST`, `SHALL`, `WILL` indicate mandatory requirements. `SHOULD`, `COULD`, `MAY` indicate desirable but not mandatory features.

### 1.3 Intended Audience and Reading Suggestions
*   **Project Sponsors & Management:** Focus on Sections 1 (Introduction), 2 (Overall Description), and 5 (External Interface Requirements) to understand project scope and constraints.
*   **Business Analysts & Subject Matter Experts:** Focus on Sections 3 (System Features) and 4 (Data Requirements) to validate functional needs.
*   **Development Team & Architects:** Focus on Sections 4 (Data Requirements), 5 (External Interface Requirements), and 6 (Non-Functional Requirements) for technical design and implementation.
*   **QA/Test Team:** Use the entire document, especially Section 3, to develop test plans and cases.

### 1.4 Project Scope
SMaRTS is a web-based application that integrates existing enterprise data sources to provide enhanced visualization, querying, and reporting capabilities for water use and regulatory compliance data. The system's core focus is on data related to the SWUCA.

**In-Scope:**
*   Development of a new web application with map-based and form-based user interfaces.
*   Creation of services and connectors to read and integrate data from specified legacy databases (DB2 Regulatory, DB2 Water Management, ArcSDE/Oracle GIS).
*   Implementation of search, spatial analysis, visualization, and standard reporting functions as defined herein.
*   Deployment and operation within the District's approved hardware/software architecture.

**Out-of-Scope:**
*   Modification of source database schemas or legacy application logic.
*   Data entry or transactional updates to source systems (SMaRTS is primarily a read-only reporting/analysis tool unless otherwise specified).
*   Collection or integration of new data types not already present in the specified source systems. The need for such data will be identified but its procurement is a separate project.
*   Hardware procurement or major infrastructure changes.

## 2. Overall Description

### 2.1 Product Perspective
SMaRTS is a new, independent system that will sit within the District's application ecosystem. It is a "consumer" of data from several authoritative systems of record, as shown in the context diagram below.

```
[External Data Sources] --> [SMaRTS Application] --> [District Users]
        |                           |                         |
    (DB2 Regulatory)         (Web Server, App Server)    (Web Browser)
    (DB2 Water Mgmt)         (GIS Map Server)
    (ArcSDE/Oracle GIS)
```

### 2.2 Product Functions (Summary)
1.  **Permit Data Access:** Search, retrieve, and display detailed water use permit information.
2.  **Spatial Visualization & Analysis:** Display permits and related data on interactive maps, with tools for spatial querying (e.g., "show all permits within this watershed").
3.  **Reporting & Analytics:** Generate standardized and ad-hoc reports on water use volumes, compliance status, and temporal trends, with export capabilities.
4.  **Data Integration:** Securely and reliably access and correlate data from multiple disparate backend databases.

### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Regulatory Staff** | Experts in permit details, compliance. Frequent users. | Fast access to permit details, compliance status, spatial context of permits. |
| **Resource Managers** | Focus on basin/regional trends, water budgets. | Aggregate data views, trend analysis, reporting for management plans (SWUCA). |
| **Field Inspectors** | Mobile, need site-specific info. | Quick lookup of permit info for a location, map viewing on tablets. |
| **Public/Stakeholders** (Potential) | Limited access, read-only. | General water use information, public reports (may be a future phase). |

### 2.4 Operating Environment
*   **Hardware:** Must operate on the District's existing server infrastructure (specifics TBD).
*   **Software:** Must be compatible with the District's standard web browsers (e.g., latest Chrome, Edge, Firefox). Backend must integrate with existing ESRI ArcGIS Enterprise, DB2, and Oracle environments.
*   **Networks:** Must function within the District's secure intranet. External access (e.g., for field staff) must comply with District security policies.

### 2.5 Design and Implementation Constraints
1.  **Integration Constraint:** The system **MUST NOT** create redundant data stores for source data. It shall access live or replicated data from the existing DB2 (Regulatory, Water Management) and ArcSDE/Oracle (GIS) databases.
2.  **Architectural Constraint:** The system **MUST** be designed to operate within the District's current hardware and software architecture standards without requiring major upgrades.
3.  **Data Scope Constraint:** If required data attributes or entities are identified that are not present in the specified source databases, their inclusion is **OUT OF SCOPE** for this development project. The project will document these gaps for potential future resolution.

### 2.6 Assumptions and Dependencies
*   **Assumption:** Read-only access or appropriate replicated copies of the source databases will be available for SMaRTS.
*   **Assumption:** Source databases have sufficient data quality and consistency to support integrated reporting.
*   **Dependency:** Continued operation and maintenance of the underlying source database systems (DB2, Oracle, ArcSDE).
*   **Dependency:** Availability of District GIS web services (e.g., base maps, feature services).

## 3. System Features

### 3.1 Feature 1: Permit Information Search and View
**Description:** Users shall be able to find and view detailed water use permit information through various search methods.

**Sub-features:**
*   **FR-001 (H): Basic Search.** The system shall allow users to search for permits by Permit Number, Applicant Name, or Site Address.
*   **FR-002 (H): Advanced Search.** The system shall provide an advanced search form with multiple filters (e.g., Permit Status, Water Use Category, County, Issue/Expiration Date range).
*   **FR-003 (H): Permit Detail View.** Upon selecting a permit from search results, the system shall display a comprehensive, read-only view of all permit data, including associated conditions, authorized quantities, and well information.
*   **FR-004 (M): Spatial Search Initiation.** From the permit detail view, the system shall provide a "Locate on Map" button to center the map on that permit's location.

### 3.2 Feature 2: Spatial Data Visualization and Analysis
**Description:** Users shall interact with an interactive map to view permits and related geographic data layers, and perform spatial queries.

**Sub-features:**
*   **FR-010 (H): Interactive Map Interface.** The system shall provide a standard web map interface with zoom, pan, and layer control functionality.
*   **FR-011 (H): Layer Management.** Users shall be able to toggle the visibility of key GIS layers relevant to SWUCA (e.g., SWUCA boundary, basins, watersheds, groundwater contours, permit locations).
*   **FR-012 (H): Identify Tool.** Users shall be able to click on a permit location or other feature on the map to view its attributes in a pop-up window.
*   **FR-013 (M): Spatial Query.** Users shall be able to draw a polygon or select a pre-defined boundary (e.g., a watershed) and query for all permits intersecting that area. Results shall be listed and summarized.
*   **FR-014 (L): Thematic Mapping.** The system shall allow users to symbolize permit points on the map based on an attribute (e.g., color by permit status, size by authorized volume).

### 3.3 Feature 3: Reporting and Analytics
**Description:** Users shall generate standardized reports and perform basic trend analysis on water use and compliance data.

**Sub-features:**
*   **FR-020 (H): Pre-defined Reports.** The system shall offer a menu of standard reports (e.g., "Annual Water Use by Basin," "Permits Expiring in Next Quarter," "Compliance Summary by County").
*   **FR-021 (H): Report Parameterization.** For pre-defined reports, users shall be able to set parameters (e.g., date range, geographic area, permit type).
*   **FR-022 (H): Report Export.** Generated reports shall be exportable to common formats (PDF, Excel).
*   **FR-023 (M): Ad-hoc Data Export.** Users shall be able to export the dataset resulting from a search or spatial query to Excel or CSV format.
*   **FR-024 (L): Trend Charts.** The system shall generate simple time-series charts (e.g., total monthly/annual water use for a selected area over a 5-year period).

## 4. Data Requirements

### 4.1 Data Sources & Integration
The system must integrate data from the following primary sources:
1.  **DB2 - Regulatory Database:** Primary source for permit details, applicants, conditions, compliance events.
2.  **DB2 - Water Management Database:** Primary source for actual water use reporting data, well construction details.
3.  **ArcSDE / Oracle - GIS Database:** Primary source for spatial geometries of permits (well points), regulatory boundaries (SWUCA, basins), and other geographic layers.

### 4.2 Key Data Entities & Relationships
*   **Permit** *(Links to Regulatory DB & GIS DB)*
*   **Permittee/Applicant** *(Regulatory DB)*
*   **Well** *(Links to Water Mgmt DB & GIS DB)*
*   **Water Use Report** *(Water Mgmt DB)*
*   **Compliance Inspection** *(Regulatory DB)*
*   **Spatial Feature** (SWUCA Boundary, Basin, County) *(GIS DB)*

### 4.3 Data Mapping & Joins
A critical technical requirement is defining and implementing the reliable keys for joining data across systems (e.g., a common Permit ID or Well ID). Specific mapping will be developed during the design phase.

## 5. External Interface Requirements

### 5.1 User Interfaces
*   The application shall be a responsive web application accessible via modern browsers.
*   The main interface shall consist of a header, a collapsible sidebar for search/controls, and a main content area dominated by the interactive map or report view.
*   All data tables shall support pagination, sorting, and basic filtering.

### 5.2 Hardware Interfaces
*   The application servers must interface with the District's database servers via secure, high-speed network connections.

### 5.3 Software Interfaces
1.  **DB2 Interfaces:** Use approved ODBC/JDBC drivers or REST APIs (if available) to connect to the Regulatory and Water Management DB2 databases.
2.  **ArcGIS Enterprise Interface:** Use ESRI ArcGIS API for JavaScript to consume map services (feature services, dynamic services, tile layers) from the District's ArcGIS Enterprise.
3.  **Oracle/ArcSDE Interface:** Access spatial data primarily via ArcGIS Enterprise services. Direct SQL access may be required for complex spatial queries and will use standard Oracle drivers.

### 5.4 Communications Interfaces
*   All client-server communication shall use HTTPS.
*   Internal service-to-database communication shall use secure protocols as mandated by District IT policy.

## 6. Non-Functional Requirements

### 6.1 Performance Requirements
*   **NFR-001:** The map interface shall load initial view (with default layers) within 5 seconds over the District intranet.
*   **NFR-002:** A simple permit search (by number or name) shall return results in under 3 seconds.
*   **NFR-003:** The system shall support at least 50 concurrent users without significant degradation in performance.

### 6.2 Security Requirements
*   **NFR-010:** The system shall integrate with the District's Active Directory (or equivalent) for user authentication.
*   **NFR-011:** Role-based access control (RBAC) shall be implemented, aligning with User Classes defined in 2.3.
*   **NFR-012:** All database connection strings, credentials, and API keys shall be stored securely, not in source code.

### 6.3 Reliability & Availability
*   **NFR-020:** The system shall have a target operational availability of 99.5% during standard business hours (7 AM - 6 PM, Mon-Fri).
*   **NFR-021:** The system shall gracefully handle the unavailability of a source database, providing informative messages to users and degrading functionality appropriately.

### 6.4 Maintainability
*   **NFR-030:** The system shall be designed with clear separation between the data access layer, business logic, and presentation layer to facilitate maintenance.
*   **NFR-031:** All configuration items (e.g., report definitions, map service URLs) shall be external to the compiled code.

---
*This document is considered the baseline for the SMaRTS project. Any changes must follow the approved change control process.*