# Balanced Summary: Water Use Tracking (WUT) Project

## Goals and Scope
The Water Use Tracking (WUT) System is a GIS-based application designed to spatially and temporally track and analyze key regulatory and resource management data for the Southwest Florida Water Management District. Its primary purpose is to support the Southern Water Use Caution Area (SWUCA) Management Plan by validating and assessing SWUCA II Rules, though it will function District-wide. The system aims to replace manual, inconsistent tracking methods with an automated solution for monitoring permitted and actual water use trends.

## Stakeholders and User Stories
**Stakeholders:**
*   **Executive Sponsors (e.g., Bruce Wirth):** Provide executive-level oversight and requirements.
*   **Co-Sponsors (e.g., B.J. Jarvis):** Oversee data entry and ensure project adherence to rules.
*   **Science Business Experts (e.g., Albert Bond):** Estimate water usage and support modeling and compliance activities.
*   **Regulatory Business Experts (e.g., Christine Jackson):** Provide permitting expertise and ensure rule criteria are satisfied.
*   **Technical Experts (e.g., Steven Dicks):** Provide technical, database, and GIS design support.
*   **Other Impacted Parties (e.g., Kurt Fritsch):** Provide cross-departmental perspective and help maintain project scope.

**User Stories:**
1.  As a **Water Use Permit Evaluator**, I want to view permit data spatially on a map so that I can analyze the impact of new applications in their geographic context.
2.  As a **Technical Services Staff member**, I want to aggregate permitted and actual pumpage over defined geographic areas so that I can track long-term water use trends.
3.  As a **Records and Data Staff member**, I want tools to assist in the quality control of Water Use Permit (WUP) data so that data consistency and accuracy are improved.
4.  As an **External Customer**, I want to access standard interactive map interfaces so that I can obtain consistent, public-facing water use information.
5.  As a **WUT Administrator**, I want to maintain system parameters and news items so that the application remains current and configurable.
6.  As a **Planning Department staff member**, I want to analyze impacts of changing demographics on water use so that I can support long-term resource planning.

## Key Processes
1.  **System Access:** An actor requests the WUT System Startup page, triggering role-based authentication and presentation of available features.
2.  **Data Replication:** A scheduled job triggers the nightly replication and normalization of data from the mainframe DB2 database to the read-only Oracle database.
3.  **Permit Search:** An actor enters search criteria (e.g., location, permit number) to identify relevant Water Use Permits for analysis.
4.  **Spatial Analysis:** An actor selects a geographic area and GIS data layers, triggering the system to render a map displaying permit and related spatial information.
5.  **Report Generation:** An actor selects a report from the library and provides optional runtime criteria, triggering the system to retrieve and format the specified data.
6.  **Data Maintenance (Admin):** A privileged actor updates configuration data, such as business rule parameters or water use estimates, which are then used in system calculations.
7.  **Well Package Generation:** An actor requests a well package file, triggering the system to compile well attribute data for export to groundwater modeling software.

## Domain Data Elements
*   **Water Use Permit (WUP):** `Permit_ID` (Primary Key). Key Fields: Permittee_Name, Issue_Date, Expiration_Date, Permitted_Quantity, Predominate_Use_Type.
*   **Withdrawal Point/Well:** `Well_UID` (Primary Key). Key Fields: Permit_ID (FK), Aquifer_Source, Well_Depth, Status, Location_Coordinates.
*   **Pumpage/Water Use:** `Pumpage_Record_ID`. Key Fields: Well_UID, Reporting_Period, Actual_Quantity, Estimated_Flag, Meter_Reading.
*   **Compliance Data:** `Compliance_ID`. Key Fields: Permit_ID, Report_Type (e.g., Crop, Meter), Submission_Date, Reported_Data, Compliance_Status.
*   **Spatial Feature (Polygon):** `Feature_ID`. Key Fields: UID (links to Well/Permit), Geometry, Feature_Type (e.g., Permit_Area, MFL_Zone), Source_Layer.
*   **Net Benefit/Lapsed Quantity Record:** `Transaction_ID`. Key Fields: Source_Permit_ID, Destination_Permit_ID, Quantity_Transferred, Transaction_Type (e.g., Relocation, Lapsed), Effective_Date.

## Non-Functional Requirements
1.  **Usability:** The system must be user-friendly, provide quick access to information, and support consistency in decision-making.
2.  **Reliability:** Query results must be consistent and reliable over time, and the system must populate missing data where possible.
3.  **Performance:** The application must enable quick turnaround to fit within statutory time frames for permit evaluation.
4.  **Supportability:** The system must follow District programming standards, be easily deployable, and include comprehensive technical documentation.
5.  **Data Integrity:** Source data must be accurate and available in real-time, with processes to initiate corrections when errors are discovered.
6.  **Interoperability:** The system must integrate with existing District hardware/software architecture, including DB2, Oracle, and ArcGIS.

## Milestones and External Dependencies
1.  Completion of the HP-UX system upgrade to retire the obsolete Tru-64 system (FY 2004).
2.  Successful daily replication of data from the IBM DB2 systems (RDB, WMDB) to the Oracle database.
3.  Availability and stability of source data systems (Regulatory DB, Water Management DB, GIS) throughout WUT development.
4.  Implementation of necessary data changes in legacy mainframe systems to support new tracking requirements (e.g., lapsed quantities).
5.  Adherence to the iterative Rational Unified Process (RUP) development lifecycle, culminating in the initial system release.

## Risks and Mitigation Strategies
1.  **Risk:** Required data (e.g., for lapsed quantities) is not available in legacy systems.
    *   **Mitigation:** Collaborate with mainframe teams for timely updates; scope contingency to implement required data structures within WUT if necessary.
2.  **Risk:** Changes to the current database architecture or project scope could cause delays.
    *   **Mitigation:** Maintain constant communication with all responsible parties and stakeholders to manage change.
3.  **Risk:** Inconsistent or inaccurate source data undermines system utility.
    *   **Mitigation:** Implement data QC tools within WUT and establish clear processes for initiating corrections to source systems.
4.  **Risk:** System performance does not meet user expectations for response times.
    *   **Mitigation:** Design with performance in mind, establish clear performance benchmarks, and optimize database queries and spatial operations.
5.  **Risk:** Complex SWUCA rule logic is incorrectly implemented.
    *   **Mitigation:** Involve regulatory business experts closely in use case development, testing, and validation of all rule-based calculations.

## Undecided Issues
1.  The final prioritization of requirements identified for a subsequent system release.
2.  Specific protocols and update intervals for different types of external data (e.g., land use, population).
3.  Detailed security model and access restrictions for different user roles beyond the basic administrator/general user distinction.
4.  The exact mechanism and responsibility for managing metadata to FGDC compliance standards.
5.  Resolution of how to best handle "what-if" scenario analysis and drought event modeling within the system architecture.
6.  Final determination on the deployment method (e.g., pure web vs. Citrix-hosted ArcMap components) for all required functionalities.