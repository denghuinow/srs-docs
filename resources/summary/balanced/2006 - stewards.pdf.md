# Balanced Summary: STEWARDS System Requirements

## Goals and Scope
STEWARDS is a centralized data system designed to provide one-point access to standardized, well-documented water, soil, management, and economic data from USDA-ARS research watersheds. Its primary goal is to support the Conservation Effects Assessment Project (CEAP) by enabling policy-relevant, multi-site analyses of conservation practice effects. The system will serve as a repository where diverse users can access, search, analyze, visualize, and download integrated watershed data, initially from twelve ARS Benchmark Watersheds.

## Stakeholders and User Stories
*   **System Operator (OCIO Staff):** Maintains executable code with full system access.
*   **Data Operations Manager (OCIO Staff):** Manages data archiving and maintenance with read/write/modify privileges.
*   **Watershed Uploader (Watershed Staff):** Uploads local data to their allocated watershed space.
*   **ARS User (ARS Researcher):** Accesses ARS watershed data for research, requiring authentication for protected data.
*   **Research User (Non-ARS Researcher):** Accesses ARS watershed data for research but cannot access password-protected sensitive data.
*   **Public User (General Public):** Accesses publicly available data without authentication.

**User Stories:**
1.  As a **Watershed Uploader**, I want to upload locally collected and QA-checked data so that it is available in the central repository for users.
2.  As an **ARS User**, I want to search and query metadata by location, theme, or keyword so that I can find relevant datasets for my research.
3.  As a **Research User**, I want to visualize time-series data (e.g., stream discharge) over a specified timeframe so that I can select the correct data for download.
4.  As a **Public User**, I want to browse and download spatial data (e.g., GIS layers) so that I can use it in my own analyses.
5.  As a **Data Operations Manager**, I want to ensure all data has associated FGDC-compliant metadata so that data provenance and quality are documented.
6.  As a **System Operator**, I want the system to have 99% availability so that users can reliably access data and services.

## Key Processes
1.  **Data Preparation (Trigger: Annual schedule/local completion):** Watershed staff perform quality assurance/control on local data and prepare it in a standard exchange format.
2.  **Data Upload (Trigger: Prepared data files):** Watershed staff use an upload tool to transfer data files to the central STEWARDS database.
3.  **Data Translation & Storage (Trigger: File upload):** The system translates uploaded data into the standardized STEWARDS schema and stores it with associated metadata.
4.  **User Search & Discovery (Trigger: User query):** Users browse watersheds or search metadata and data catalogs to locate datasets of interest.
5.  **Data Access & Visualization (Trigger: User selection):** Users examine selected data through tabular reports or visualization tools (e.g., charts, GIS interfaces).
6.  **Data Download (Trigger: User request):** Users download selected data in standardized formats (e.g., CSV, shapefiles).
7.  **System Administration (Trigger: Scheduled/on-demand):** Operators perform backups, user management, and system monitoring.

## Domain Data Elements
*   **Watershed** (PK: Watershed_ID): Name, Location, Description, Research_Goals.
*   **Site/Sampling Station** (PK: Site_ID): Watershed_ID, Location_Coordinates, Station_Type, Description.
*   **Data Topic** (PK: Topic_ID): Topic_Name (e.g., Climate, Water Quality), Description, Measurement_Unit_Lookup.
*   **Time-Series Data** (PK: Data_Record_ID): Site_ID, Topic_ID, Timestamp, Parameter_Value, Quality_Flag.
*   **Spatial Data Layer** (PK: Layer_ID): Watershed_ID, Layer_Name, Data_Format, Description, File_Path.
*   **Metadata Record** (PK: Metadata_ID): Dataset_ID, FGDC_Compliant_Fields, Abstract, Quality_Assurance_Info.

## Non-Functional Requirements
1.  **Performance:** Query response times should be a few seconds; large data retrievals may take minutes to hours.
2.  **Availability:** System must be available 24/7 with 99% uptime.
3.  **Security:** Implement authentication, confidentiality controls, and data integrity validation per ARS OCIO practices.
4.  **Usability:** Interface must be simple, consistent, and intuitive, requiring minimal training for infrequent users.
5.  **Portability/Adaptability:** Database and application design must allow for future modifications and changes.
6.  **Compliance:** Must adhere to USDA web style, accessibility, and security policies.

## Milestones and External Dependencies
1.  Completion of detailed system design and prototyping.
2.  Development of data translation filters for initial population from watersheds.
3.  Operational deployment on ARS OCIO infrastructure in Beltsville, MD.
4.  Dependency on continued NRCS/ARS funding through FY07 and beyond.
5.  Dependency on watershed sites providing resources for data preparation and upload.

## Risks and Mitigation Strategies
1.  **Risk:** Watershed sites have inadequate resources for data preparation.
    *   **Mitigation:** Identify minimal CEAP data requirements; central team provides additional support, potentially delaying some data.
2.  **Risk:** Funding from NRCS is insufficient or discontinued.
    *   **Mitigation:** Seek base or discretionary ARS funds, though this may adjust project timelines.
3.  **Risk:** Database design is insufficiently flexible for future needs.
    *   **Mitigation:** Design with modularity and extensibility in mind to allow modification without large overhauls.
4.  **Risk:** Complex user interface for infrequent data uploaders.
    *   **Mitigation:** Design upload interface for simplicity and provide clear documentation/tutorials.
5.  **Risk:** Data integrity issues from uploads or system errors.
    *   **Mitigation:** Implement rigorous QA/QC at local and central levels, along with system backup and validation procedures.

## Undecided Issues
1.  Specific tools and detailed workflow for metadata creation and editing at watershed sites.
2.  Final selection of software stack (e.g., specific .NET components, GIS server applications).
3.  Detailed hardware specifications for load balancing and storage scaling.
4.  Formal procedures and staffing model for user help desk support.
5.  Protocol for integrating data from three potential additional watersheds representing other land uses.
6.  Long-term plan for potential migration to ISO 19115 metadata standard if mandated.