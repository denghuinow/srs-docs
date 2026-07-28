**Purpose & Scope**
The system is a GIS-based tool for tracking and analyzing water use permit data spatially and temporally. It supports the validation of the SWUCA Recovery Strategy rules. It does not modify the source regulatory or water management databases; it is for reporting, analysis, and decision support.

**Product Background / Positioning**
The system integrates data from the District's existing Regulatory Database (RDB), Water Management Database (WMDB), and Geographic Information System (GIS). It serves as a centralized decision-support layer atop these legacy systems to fulfill analysis needs for the SWUCA Management Plan.

**Core Functional Overview**
*   View and search water use permits and their details.
*   View spatial data and permit information on interactive maps.
*   Generate standardized and ad-hoc reports on permit and pumpage data.
*   Track the movement and use of lapsed water quantities.
*   Analyze net benefit calculations for permit changes impacting minimum water levels.
*   View compliance and pumpage information for permits.
*   View and maintain water use estimates for unmetered permits.

**Key Users & Usage Scenarios**
*   **General WUT Users (District Staff & External Public):** View maps, search permits, run read-only reports.
*   **WUP Evaluators (Regulatory Staff):** Analyze new permit applications by viewing spatial context, adjacent permits, and historical trends.
*   **Water Use Estimators & WUT Administrators (Specialized Staff):** Maintain system parameters, news, and import estimated water use data.

**Major External Interfaces**
*   **Data Sources:** IBM DB2 (RDB, WMDB), HP-UX ArcSDE/Oracle (GIS). Data is replicated nightly.
*   **User Interface:** Web-based application and ArcGIS ArcView desktop integration.
*   **External Systems:** Links to other district websites and data (e.g., adjacent water districts).

**Key Non-functional Requirements**
*   **Performance:** Must support statutory time frames for permit evaluation. Data replication occurs daily.
*   **Reliability:** Query results must be consistent and reliable over time. Data must be accurate.
*   **Supportability:** Must be a web application deployable within the District's current architecture (Oracle, .NET). Must follow District programming and change management standards.
*   **Usability:** Requires role-based security. Data values must be displayed, not internal codes.

**Constraints, Assumptions & Dependencies**
*   Dependent on the continued availability and stability of the source RDB, WMDB, and GIS databases.
*   Assumes required data (e.g., lapsed quantities) will be collected and stored in the source systems.
*   Must operate within the District's existing hardware/software environment (DB2, Oracle, ArcGIS, .NET).

**Priorities & Acceptance Approach**
*   Initial release focuses on core tracking, reporting, mapping, and SWUCA rule support functions.
*   Advanced analytics (e.g., water quality trend calculation, complex population modeling) are deferred to a subsequent release.
*   Acceptance will be based on the system fulfilling the mapped business requirements and use cases.