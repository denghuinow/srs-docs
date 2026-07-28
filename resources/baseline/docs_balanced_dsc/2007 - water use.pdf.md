# Software Requirements Specification (SRS)
## Water Use Tracking (WUT) System
**Document Version:** 1.0  
**Date:** [Date of Generation]  
**Status:** Draft for Review

---

### **1. Introduction**

#### **1.1 Purpose**
This document defines the functional and non-functional requirements for the Water Use Tracking (WUT) System. It serves as a comprehensive guide for developers, testers, project managers, and stakeholders, ensuring a common understanding of the system's capabilities, constraints, and goals. The intended audience includes the development team, quality assurance, system administrators, and all business stakeholders listed in Section 2.

#### **1.2 Project Scope**
The WUT System is a GIS-based enterprise application designed to spatially and temporally track, analyze, and report on water use data for the Southwest Florida Water Management District. Its primary mission is to support the Southern Water Use Caution Area (SWUCA) Management Plan by automating the validation and assessment of SWUCA II Rules. The system will replace existing manual and inconsistent tracking methods with a centralized, automated solution for monitoring permitted water allocations and actual consumption trends District-wide.

**In-Scope:**
*   A web-based interface for searching, viewing, and analyzing water use permit data.
*   GIS integration for spatial visualization and analysis of permits, wells, and regulatory zones.
*   Automated nightly data replication from legacy DB2 systems to a read-only Oracle operational data store.
*   Tools for data quality control, aggregation, and standard report generation.
*   Administrative functions for system configuration.
*   Generation of data packages for external groundwater modeling software.

**Out-of-Scope:**
*   Direct modification of source data in legacy mainframe systems (RDB, WMDB).
*   Real-time, transactional data entry for new permits or compliance reports (remains in source systems).
*   Advanced hydrological or demand modeling engines (focus is on data provision and rule assessment).
*   Public user account creation or complex self-service portals beyond basic map viewing.

#### **1.3 Definitions, Acronyms, and Abbreviations**
*   **DB2:** IBM Database 2 (legacy mainframe database system).
*   **FGDC:** Federal Geographic Data Committee.
*   **GIS:** Geographic Information System.
*   **MFL:** Minimum Flows and Levels.
*   **RDB:** Regulatory Database (legacy system).
*   **RUP:** Rational Unified Process.
*   **SRS:** Software Requirements Specification.
*   **SWUCA:** Southern Water Use Caution Area.
*   **WUP:** Water Use Permit.
*   **WUT:** Water Use Tracking.
*   **WMDB:** Water Management Database (legacy system).

#### **1.4 References**
*   SWUCA Management Plan, Southwest Florida Water Management District.
*   District Programming Standards and IT Architecture Guidelines.
*   Rational Unified Process (RUP) Methodology Documentation.

#### **1.5 Document Overview**
This SRS is organized into sections describing the overall product perspective, specific functional requirements, external interfaces, non-functional requirements, and appendices for supporting information.

---

### **2. Overall Description**

#### **2.1 Product Perspective**
The WUT System is a new component within the District's existing IT ecosystem. It acts as a reporting and analysis layer atop authoritative source systems.
*   **Interfaces:**
    *   **Legacy Databases:** Consumes read-only, replicated data from IBM DB2 (RDB, WMDB) via a nightly ETL process to an Oracle database.
    *   **GIS Services:** Integrates with ESRI ArcGIS services for base maps, spatial data layers, and geoprocessing.
    *   **External Systems:** Generates export files (e.g., well packages) for consumption by groundwater modeling software (e.g., MODFLOW).
*   **Constraints:**
    *   Must adhere to District security policies and hardware/software architecture standards.
    *   Dependent on the successful completion of the HP-UX system upgrade and stable data replication.
    *   Must comply with FGDC metadata standards where applicable.

#### **2.2 User Classes and Characteristics**
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Water Use Permit Evaluator** | Regulatory staff. Expert in permit rules. Needs spatial context for decisions. | Map-based permit visualization, spatial querying, overlay analysis with regulatory zones. |
| **Technical Services Staff** | Scientific/engineering staff. Analyzes trends and supports modeling. | Data aggregation (temporal/spatial), trend analysis, export functionality. |
| **Records & Data Staff** | Data management specialists. Ensures data quality. | Data validation tools, discrepancy reporting, audit views. |
| **External Customer** | Public, consultants, other agencies. Limited technical knowledge. | Simple, intuitive public map interface with predefined queries and reports. |
| **WUT Administrator** | IT or power user. Maintains system health. | Configuration management, user role management, news/alert updates. |
| **Planning Department Staff** | Long-term resource planners. | Demographic/land use data integration, "what-if" scenario analysis capabilities. |
| **Executive/Co-Sponsors** | Management. Strategic oversight. | High-level dashboards, summary reports, compliance status overviews. |

#### **2.3 Operating Environment**
*   **Software:** Web browser client (IE, Firefox, etc.), Oracle Database, ESRI ArcGIS Server/Desktop components, HP-UX or Windows Server application tier.
*   **Hardware:** District-standard servers and workstations.
*   **Networks:** District intranet for internal users; secure public-facing network segment for external access.

#### **2.4 Design and Implementation Constraints**
1.  Must use the District's approved Oracle database for all application data storage.
2.  GIS functionality must be compatible with the District's version of ESRI ArcGIS.
3.  Development must follow the iterative Rational Unified Process (RUP).
4.  The user interface must be accessible from standard web browsers without requiring specialized plugins where possible.

#### **2.5 Assumptions and Dependencies**
*   **Assumption:** Source systems (RDB, WMDB, GIS) will provide accurate and timely data via the replication process.
*   **Assumption:** Business experts will be available for clarifying rule logic and user acceptance testing.
*   **Dependency:** Successful daily data replication from DB2 to Oracle (Milestone 2).
*   **Dependency:** Implementation of necessary data structures for "lapsed quantities" in legacy systems (Milestone 4).
*   **Dependency:** Stability of the overall District IT infrastructure during development and deployment.

---

### **3. System Features and Requirements**

#### **3.1 Feature 1: User Authentication and Role-Based Access**
**3.1.1 Description**
The system shall authenticate users against the District's central directory service and present a customized interface based on assigned roles and permissions.

**3.1.2 Functional Requirements**
*   **FR1.1:** The system shall require user authentication before granting access to any non-public feature.
*   **FR1.2:** The system shall integrate with [District LDAP/Active Directory] for authentication.
*   **FR1.3:** The system shall present a role-specific homepage or menu after login, filtering available functions (e.g., Admin tools, QC tools).
*   **FR1.4:** The system shall provide a public-facing interface accessible without authentication, offering limited, predefined map views and reports.

#### **3.2 Feature 2: Data Management and Replication**
**3.2.1 Description**
The system shall rely on a nightly, automated process to replicate and normalize data from source DB2 systems to a dedicated Oracle database for read-only operational use.

**3.2.2 Functional Requirements**
*   **FR2.1:** A scheduled ETL job shall extract data from the specified DB2 tables (RDB, WMDB).
*   **FR2.2:** The ETL process shall transform and load data into the normalized WUT Oracle schema, handling data type conversions and basic cleansing.
*   **FR2.3:** The system shall log all replication activities, including record counts, start/end times, and any errors encountered.
*   **FR2.4:** The WUT application shall only read data from the Oracle replica, never writing back to the source systems.

#### **3.3 Feature 3: Water Use Permit Search and Retrieval**
**3.3.1 Description**
Users shall be able to locate Water Use Permits using a variety of search criteria, with results presented in both list and map form.

**3.3.2 Functional Requirements**
*   **FR3.1:** The system shall provide a search interface with criteria including, but not limited to: Permit ID, Permittee Name, Location (Address, County, Township/Range/Section), Predominate Use Type, and Status.
*   **FR3.2:** Search results shall be displayed in a tabular list showing key permit attributes.
*   **FR3.3:** Selecting a permit from the results list shall display its full detail view and optionally zoom the map to its location.
*   **FR3.4:** The system shall allow spatial search by user-drawn polygon, rectangle, or buffer around a selected feature.

#### **3.4 Feature 4: Spatial Visualization and Analysis**
**3.4.1 Description**
The system shall provide an interactive map for visualizing permits, wells, and related GIS layers, enabling spatial analysis to support regulatory decision-making.

**3.4.2 Functional Requirements**
*   **FR4.1:** The map interface shall display base layers (e.g., streets, aerial imagery) and operational layers (e.g., permits as points, SWUCA boundaries, MFL zones as polygons).
*   **FR4.2:** Users shall be able to toggle the visibility of any layer.
*   **FR4.3:** Clicking a permit or well on the map shall display a pop-up with its key attributes and links to detailed information.
*   **FR4.4:** The system shall allow users to select a geographic area (e.g., a sub-basin, user-drawn polygon) and aggregate total permitted and reported pumpage for all features within that area.
*   **FR4.5:** The system shall support spatial queries such as "show all permits within 1 mile of this proposed well" or "identify all wells in a specific aquifer."

#### **3.5 Feature 5: Reporting and Data Export**
**3.5.1 Description**
The system shall generate standardized reports and allow export of data in common formats.

**3.5.2 Functional Requirements**
*   **FR5.1:** The system shall provide a library of pre-defined reports (e.g., Permit Summary, Pumpage by Basin, Compliance Status Report).
*   **FR5.2:** Users shall be able to filter reports by runtime parameters (e.g., date range, county, use type).
*   **FR5.3:** Reports shall be exportable to PDF, Excel, and CSV formats.
*   **FR5.4:** The system shall generate a "Well Package" file containing a specified set of well attributes formatted for import into groundwater modeling software.

#### **3.6 Feature 6: Data Quality Control Tools**
**3.6.1 Description**
Authorized users shall have access to tools to identify, flag, and initiate correction of data inconsistencies.

**3.6.2 Functional Requirements**
*   **FR6.1:** The system shall provide validation checks (e.g., permits with missing coordinates, wells with pumpage exceeding permitted amounts).
*   **FR6.2:** QC results shall be presented in a list, allowing users to drill into the problematic records.
*   **FR6.3:** The system shall provide a mechanism to flag a record as "suspect" and generate a structured request for correction to the responsible source system team. **FR6.4:** The system shall not allow direct editing of source data through the QC interface.

#### **3.7 Feature 7: Administrative Functions**
**3.7.1 Description**
Administrators shall be able to configure system parameters and manage content.

**3.7.2 Functional Requirements**
*   **FR7.1:** Administrators shall be able to update system-wide parameters used in calculations (e.g., estimation coefficients, rule thresholds).
*   **FR7.2:** Administrators shall be able to post and manage news items or alerts on the system homepage.
*   **FR7.3:** (Future) Administrators shall be able to manage user roles and permissions within the WUT application.

---

### **4. External Interface Requirements**

#### **4.1 User Interfaces**
*   The primary interface shall be a web application compatible with modern browsers (HTML5, CSS3, JavaScript).
*   GIS components may require a Citrix-hosted ArcMap session or utilize ESRI Web AppBuilder/JavaScript API for a pure web experience (see Undecided Issues).
*   All interfaces shall follow District branding and usability guidelines.

#### **4.2 Hardware Interfaces**
*   The application server shall interface with the Oracle database server via standard ODBC/JDBC connections.
*   The application shall interface with GIS map servers via REST APIs or direct service calls.

#### **4.3 Software Interfaces**
*   **Oracle Database:** JDBC connection for all application data queries.
*   **ESRI ArcGIS Services:** REST API endpoints for map rendering, geocoding, and spatial analysis.
*   **Legacy DB2 Systems:** Connection via scheduled ETL tool (e.g., Informatica, custom script) for data replication only.

#### **4.4 Communications Interfaces**
*   HTTP/HTTPS for web traffic.
*   LDAP for user authentication.

---

### **5. Non-Functional Requirements**

#### **5.1 Performance Requirements**
*   **Search Response:** Simple permit searches shall return results in < 3 seconds.
*   **Map Rendering:** Initial map load with standard layers shall complete in < 5 seconds. Pan/zoom operations shall refresh in < 2 seconds.
*   **Report Generation:** Standard aggregate reports for a county-sized area shall generate in < 30 seconds.
*   The system shall support concurrent use by a minimum of 50 internal users and 100 public sessions.

#### **5.2 Safety Requirements**
*   Not applicable (no physical safety implications).

#### **5.3 Security Requirements**
*   All user sessions shall timeout after 30 minutes of inactivity.
*   All data transmissions containing sensitive information shall use HTTPS.
*   Access to administrative functions shall be restricted to the "WUT Administrator" role.
*   Public users shall have no access to personally identifiable information or draft permit data.

#### **5.4 Software Quality Attributes**
*   **Usability:** The system shall achieve a task success rate of >90% for core user stories (e.g., find a permit, generate a report) during formal usability testing with target user groups.
*   **Reliability:** The system shall have an operational availability of 99.5% during core business hours (7 AM - 6 PM, Mon-Fri).
*   **Supportability:** The system shall be deployed using District-standard procedures. All custom code shall be documented per District standards.
*   **Data Integrity:** The system shall provide clear audit trails for all administrative configuration changes.
*   **Interoperability:** The system shall successfully consume and display data from the Oracle replica and published ArcGIS Map Services without custom adaptation.

---

### **6. Other Requirements**

#### **6.1 Appendices**
*   **Appendix A: Data Dictionary** - Detailed schema for the WUT Oracle database, based on Domain Data Elements.
*   **Appendix B: Wireframes/UI Mockups** - Visual representations of key interfaces.
*   **Appendix C: Glossary of Business Terms** - Definitions of terms like "Lapsed Quantity," "Net Benefit," etc.

#### **6.2 Undecided Issues & TBD**
1.  **Release Prioritization:** Requirements for Phase 2 will be prioritized post-initial release.
2.  **External Data Protocols:** Update intervals for land use/population data will be defined in collaboration with data stewards.
3.  **Detailed Security Model:** Specific permissions per user role (e.g., Evaluator vs. Tech Services) require further analysis.
4.  **FGDC Metadata Management:** Process and responsibility for metadata maintenance requires a District-wide policy decision.
5.  **Scenario Analysis Architecture:** The technical approach for "what-if" modeling requires a separate design spike.
6.  **Deployment Method:** The final architecture (web vs. Citrix-hosted thick client) for advanced GIS editing/analysis is pending a feasibility study.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Business Analyst | | | |
| Lead Developer | | | |
| Quality Assurance Lead | | | |