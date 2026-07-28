# Detailed Summary: STEWARDS System Requirements Specification

## Background and Scope
STEWARDS (Sustaining the Earth's Watersheds – Agricultural Research Data System) is a centralized data system being developed by the USDA Agricultural Research Service (ARS) to support the Conservation Effects Assessment Project (CEAP). The system will provide one-point access to standardized, well-documented water, soil, management, and economic data from twelve ARS Benchmark Watersheds, facilitating multi-site analyses of conservation practice effects. The core system consists of a database management system for storage and a client application for user access, enabling search, analysis, visualization, and download of integrated watershed data. Non-goals include providing real-time public data access (data will be updated annually) and replacing local watershed data management responsibilities.

## Stakeholders Matrix and Use Cases
*   **System Operator (OCIO Staff)**: Maintains executable code with full system access.
*   **Data Operations Manager (OCIO Staff)**: Manages data archiving and maintenance with read/write/modify privileges.
*   **Watershed Uploaders (Local Staff)**: Upload local data to their allocated watershed space.
*   **ARS Users (Scientists/Engineers)**: Access data for ARS research, requiring authentication for sensitive data.
*   **Research Users (Non-ARS Scientists)**: Access data for external research but cannot view password-protected sensitive data.
*   **Public Users**: Access public data without authentication for general use.

**Main Scenarios**: User logs in and selects a watershed; user searches metadata by theme/location; user queries and visualizes time-series data; user downloads selected data in standard formats; watershed staff upload annual QA/QC data.
**Exception Scenarios**: User attempts to access restricted data without proper authentication; system encounters low transmission speed and offers a non-graphical interface; large data request exceeds acceptable response time, prompting an alternate delivery method.

## Business Process
**Main Process (Data Access & Download)**:
1.  **Trigger**: User navigates to STEWARDS portal.
2.  User authenticates (if required for access level).
3.  User selects a watershed from the top-level view.
4.  User searches/browses metadata or data by site, topic, or location.
5.  User applies filters (time range, parameters).
6.  System extracts and presents data (tabular or chart view).
7.  User selects download format (e.g., CSV, shapefile).
8.  **Output**: User downloads formatted data package.

**Key Branch A (Data Upload from Watershed)**:
1.  **Trigger**: Annual schedule or request from central system.
2.  Local staff perform QA/QC on new data.
3.  Data is translated into STEWARDS standard format using local filters.
4.  Data is uploaded to the central database via the web interface.
5.  **Output**: Central database is updated.

**Key Branch B (Metadata Search)**:
1.  User selects metadata search option.
2.  User enters search criteria (location, theme, keyword).
3.  System queries metadata database.
4.  **Output**: User views list of datasets with links to formal metadata and site descriptions.

## Domain Model
Core entities include:
*   **Watershed** (required): ID, Name, Location.
*   **Site/Sampling Station** (required, references Watershed): Site_ID, Description, Geo-coordinates.
*   **Topic/Theme** (required): Topic_ID, Name (e.g., Climate, Water Quality).
*   **Measurement Data** (required, references Site & Topic): Data_ID, Timestamp, Value, Unit (reference), Quality_Flag.
*   **Metadata Record** (required, references Data): Metadata_ID, FGDC-compliant fields, Abstract.
*   **Spatial Data Layer** (references Watershed): Layer_ID, Type (e.g., raster, vector), Format.
*   **User** (required for authenticated access): User_ID, Class, Authentication_Info.
*   **Data Upload Transaction** (references Watershed & User): Upload_ID, Timestamp, Status.

## Interfaces and Integrations
*   **User Web Interface**: Direction: System-to-User. Interaction: Browser-based GUI. Input: Search criteria, clicks. Output: HTML pages, data visualizations, download files. SLA: 99% availability.
*   **Database Management System (Microsoft SQL Server)**: Direction: Internal. Interaction: Primary data storage. Input: Queries, uploads. Output: Result sets. SLA: Backups week-nightly, off-site weekly.
*   **GIS Server Application (e.g., ArcIMS)**: Direction: Internal/System-to-User. Interaction: Spatial data rendering and query. Input: Spatial queries. Output: Interactive maps, GIS data extracts.
*   **Watershed Local Systems**: Direction: External-to-System. Interaction: Data upload via standard exchange files. Input: Formatted data files. Output: Upload confirmation/status.
*   **Authentication Service (e.g., Microsoft Active Directory)**: Direction: Internal. Interaction: User login validation. Input: User credentials. Output: Authentication token/access level.
*   **Email Services**: Direction: System-to-User. Interaction: Alerts and data delivery for large requests. Input: User request. Output: Email with data link/notification.

## Acceptance Criteria
*   **Capability: Public Data Access**
    *   Given a public user visits the STEWARDS portal, when they browse to a watershed and select a public dataset, then they can download the data in a tab-delimited format without logging in.
*   **Capability: Authenticated Data Search**
    *   Given an ARS researcher is logged into STEWARDS, when they perform a metadata search by watershed and topic, then the system returns a list of relevant datasets with links to detailed site descriptions.
*   **Capability: Data Visualization**
    *   Given a user has selected a time-series dataset, when they specify a date range and choose "View Chart", then the system generates a graphical plot of the data for visual examination.
*   **Capability: Watershed Data Upload**
    *   Given watershed staff have prepared an annual data file in the standard format, when they use the upload tool, then the data is validated and populated into the central database, and a confirmation is displayed.

## Non-functional Metrics
*   **Performance**: Query response times for metadata searches should be a few seconds; system load should not visibly deteriorate with increasing users.
*   **Reliability/Availability**: System must be available 24/7 with 99% uptime tolerance.
*   **Security**: Implement authentication, confidentiality controls per user class, and data integrity validation during uploads.
*   **Compliance**: Adhere to USDA web style, accessibility, and security policies; metadata compliant with FGDC standards.
*   **Observability**: System must support administrative metrics tracking (user access, download estimates).

## Milestones and Release Strategy
1.  Complete detailed requirements analysis (Version 2.0 of SRS).
2.  Finalize logical and physical system design (database schema, interface specs).
3.  Develop and test prototype with data from pilot watershed(s).
4.  Develop data translation filters for all watersheds.
5.  Perform initial population of the database with historical data.
6.  Deploy Version 1.0 system for CEAP and ARS user access, followed by eventual public release.

## Risk List and Mitigation Strategies
1.  **Risk**: Inadequate resources at watersheds for data preparation/upload. **Mitigation**: Identify minimal CEAP data sets; central team provides additional support, accepting potential delays.
2.  **Risk**: Funding uncertainty post-FY07. **Mitigation**: Develop proposal for base/discretionary fund support; adjust timelines accordingly.
3.  **Risk**: Database design lacks flexibility for future changes. **Mitigation**: Design structure with room for modification without major overhaul.
4.  **Risk**: Portability issues when re-hosting system. **Mitigation**: Implement server-side code as much as possible; test on different platforms.
5.  **Risk**: Complex interface for infrequent watershed uploaders. **Mitigation**: Prioritize simple, intuitive design for upload tasks; use wizards.
6.  **Risk**: Large data requests impact system performance. **Mitigation**: Advise users of long wait times; offer FTP/email delivery alternative.
7.  **Risk**: Inconsistent data formats from watersheds. **Mitigation**: Jointly develop standard exchange format and translation filters.
8.  **Risk**: Inadequate help desk support. **Mitigation**: Determine staffing needs during design and propose to NPS.

## Undecided Issues and Responsible Parties
1.  Selection of specific metadata input tool. (STEWARDS Database Team)
2.  Detailed load-balancing and fail-over strategy for servers. (OCIO)
3.  Final determination of help desk funding and structure. (NPS/STEWARDS Team)
4.  Specific protocols for handling model input/output data and uncertainty reporting. (CEAP Modeling Team)
5.  Conversion plan if federal metadata standard shifts to ISO 19115. (STEWARDS Database Team)
6.  Detailed testing plan based on use cases. (Development Team)
7.  Final list of required GIS server applications and browser plug-ins. (Development Team)
8.  Procedures for handling intentional denial-of-service attacks. (OCIO Security)