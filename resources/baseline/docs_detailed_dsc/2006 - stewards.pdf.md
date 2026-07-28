# **STEWARDS System Requirements Specification (SRS)**
**Document Version:** 2.0
**Project:** Sustaining the Earth's Watersheds – Agricultural Research Data System
**Client:** USDA Agricultural Research Service (ARS)
**Date:** [Date of Generation]
**Status:** Draft for Review

---

## **1. Introduction**

### **1.1 Purpose**
This document defines the functional and non-functional requirements for the STEWARDS (Sustaining the Earth's Watersheds – Agricultural Research Data System). It serves as a contract between the development team, stakeholders, and project sponsors, providing a comprehensive blueprint for system design, development, testing, and deployment.

### **1.2 Document Conventions**
*   **Requirements:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Keywords:** "Shall" indicates a mandatory requirement. "Should" indicates a recommendation. "May" indicates a permissible action.
*   **Formatting:** User interface elements are `highlighted`. Database entities are **bolded**.

### **1.3 Project Scope**
STEWARDS is a centralized data system designed to provide one-point, standardized access to water, soil, management, and economic data from twelve ARS Benchmark Watersheds. Its primary purpose is to support the Conservation Effects Assessment Project (CEAP) by enabling multi-site analyses of agricultural conservation practice effects.

**In-Scope:**
*   A centralized relational database for storing standardized, well-documented watershed data.
*   A web-based client application for searching, browsing, visualizing, analyzing, and downloading integrated data.
*   Role-based access control for public, research, and ARS users.
*   A secure web interface for watershed staff to upload annual QA/QC data in a standard format.
*   Generation of FGDC-compliant metadata.
*   Integration with GIS services for spatial data visualization and extraction.

**Out-of-Scope (Non-Goals):**
*   Real-time data access or streaming; data will be updated on an annual basis.
*   Replacement of local watershed data management systems or responsibilities.
*   Advanced statistical or hydrological modeling within the core application.
*   Management of non-CEAP or non-watershed-related ARS data.

### **1.4 References**
*   USDA ARS CEAP Program Documentation
*   Federal Geographic Data Committee (FGDC) Content Standard for Digital Geospatial Metadata
*   USDA Web Policies and Accessibility Standards (Section 508)
*   Project Charter and Vision Document for STEWARDS

## **2. Overall Description**

### **2.1 Product Perspective**
STEWARDS is a new, self-contained web application. It will integrate with existing enterprise infrastructure:
*   **Authentication Service:** (e.g., Microsoft Active Directory) for validating ARS user credentials.
*   **GIS Server:** (e.g., ArcIMS) for serving spatial data layers and enabling map-based interactions.
*   **Email Services:** For sending notifications and facilitating large data deliveries.
*   **Watershed Local Systems:** As external data sources via standardized file uploads.

### **2.2 User Classes and Characteristics**
| User Class | Description | Key Characteristics & Requirements |
| :--- | :--- | :--- |
| **Public User** | General public, educators, students. | No authentication required. Read-only access to publicly released data. Simple, intuitive interface. |
| **Research User** | Non-ARS scientists, collaborators. | May require authentication for some data. Cannot access sensitive/restricted data. Needs robust search and download capabilities. |
| **ARS User** | ARS scientists, engineers, analysts. | Requires authentication. Access to sensitive data relevant to their work. Needs advanced query, visualization, and data export tools. |
| **Watershed Uploader** | Local watershed technical staff. | Authenticated access to a specific watershed's upload module. Needs a simple, wizard-driven interface for annual data submission. |
| **Data Operations Manager** | OCIO staff managing system data. | Read/write/modify privileges to the database for archiving and maintenance. Requires data validation and bulk operation tools. |
| **System Operator** | OCIO staff maintaining system health. | Full system access for code deployment, server monitoring, and troubleshooting. Requires administrative dashboards and logs. |

### **2.3 Operating Environment**
*   **Server:** Microsoft Windows Server environment.
*   **Database:** Microsoft SQL Server.
*   **Web Server:** Internet Information Services (IIS) or equivalent.
*   **Client:** Standard modern web browsers (e.g., Chrome, Firefox, Edge, Safari) without mandatory plug-ins.
*   **GIS:** GIS server application (e.g., ArcIMS) for spatial services.

### **2.4 Design and Implementation Constraints**
1.  The system shall comply with USDA web style guides, security policies, and accessibility standards.
2.  All metadata shall be compliant with the FGDC metadata standard.
3.  The database schema shall be designed to allow for future modification without a major overhaul.
4.  Server-side code shall be prioritized to enhance portability and simplify re-hosting.

### **2.5 Assumptions and Dependencies**
*   Watersheds have the capacity to perform basic QA/QC and format data for annual upload.
*   Stable funding and server resources will be provided for development and ongoing operation.
*   The FGDC metadata standard will remain stable for the initial development period.
*   An enterprise authentication service will be available for integration.

## **3. System Features and Requirements**

### **3.1 Feature: User Authentication and Authorization**
**Description:** The system shall control access based on user class, authenticating users where necessary and enforcing data visibility rules.

**Requirements:**
*   `FR-010` The system shall allow users to access public data without any form of login.
*   `FR-011` The system shall provide a login page for ARS Users, Research Users, Watershed Uploaders, and Managers/Operators.
*   `FR-012` The system shall validate user credentials against the integrated Authentication Service (e.g., Active Directory).
*   `FR-013` The system shall enforce access control lists (ACLs) such that:
    *   ARS Users can view all data (public and sensitive) for watersheds.
    *   Research Users can view only public, non-sensitive data.
    *   Watershed Uploaders can write data only to their assigned watershed(s).
    *   Data Operations Managers can read/write/modify all data.
*   `FR-014` The system shall display a clear error message if a user attempts to access a restricted resource without proper authorization.

### **3.2 Feature: Watershed Data Discovery and Search**
**Description:** Users shall be able to find datasets of interest by browsing by location (watershed, site) or searching metadata by theme, keyword, or location.

**Requirements:**
*   `FR-020` The system shall present a top-level view (e.g., interactive map or list) of all twelve ARS Benchmark Watersheds.
*   `FR-021` The user shall be able to select a watershed to view its detailed description and associated data topics.
*   `FR-022` The system shall provide a metadata search interface with criteria including: Watershed, Site/Station, Topic/Theme (e.g., Climate, Water Quality), Keyword, and Date Range.
*   `FR-023` The system shall return a list of datasets matching the search criteria. Each result shall include: Dataset Title, Location, Topic, Date Range, and a link to its full FGDC-compliant metadata record.
*   `FR-024` The user shall be able to click a link from the search results to view a detailed site description and the formal metadata record.

### **3.3 Feature: Data Visualization and Presentation**
**Description:** Users shall be able to view data in tabular and graphical formats for examination prior to download.

**Requirements:**
*   `FR-030` Upon selecting a specific time-series dataset, the system shall present the data in a paginated tabular view by default.
*   `FR-031` The user shall be able to specify a date range and/or parameter filters to refine the displayed data.
*   `FR-032` The user shall be able to select a "View Chart" option to generate a graphical plot (e.g., time-series line chart) of the filtered data.
*   `FR-033` The system shall provide basic chart controls (e.g., zoom, pan, export as image).
*   `FR-034` The system shall integrate with the GIS Server to display spatial data layers (e.g., soil maps, land use) in an interactive map view when spatial data is selected.

### **3.4 Feature: Data Export and Download**
**Description:** Users shall be able to download selected data in standard, usable formats.

**Requirements:**
*   `FR-040` From the data table or visualization view, the user shall be able to initiate a download.
*   `FR-041` The system shall allow the user to select a download format (e.g., CSV, tab-delimited text, ESRI Shapefile for spatial data).
*   `FR-042` The download file shall include all currently filtered/viewed data, relevant metadata headers, and column definitions.
*   `FR-043` For standard-sized requests, the download shall be delivered directly via the browser.
*   `FR-044` If a data request is estimated to exceed a pre-defined performance threshold (e.g., >50MB, >30 sec processing), the system shall notify the user of the delay and offer an alternative delivery method (e.g., email notification with a secure FTP link).

### **3.5 Feature: Watershed Data Upload**
**Description:** Authorized watershed staff shall be able to upload annual QA/QC data to the central database.

**Requirements:**
*   `FR-050` The system shall provide an authenticated upload portal accessible only to Watershed Uploaders and higher-privilege roles.
*   `FR-051` The upload interface shall be a simple, wizard-driven process to guide infrequent users.
*   `FR-052` The system shall validate that the uploaded file conforms to the STEWARDS standard exchange format (structure, column headers, data types).
*   `FR-053` The system shall perform integrity checks (e.g., referential integrity with existing **Sites**, valid **Topic** codes).
*   `FR-054` Upon successful validation and upload, the system shall update the central database and display a confirmation message to the user, including a **Data Upload Transaction** ID.
*   `FR-055` If validation fails, the system shall clearly report the errors back to the user without committing any data to the database.

### **3.6 Feature: System Administration and Observability**
**Description:** Administrators shall be able to monitor system health and usage.

**Requirements:**
*   `FR-060` The system shall log all user authentication attempts (success and failure).
*   `FR-061` The system shall track and log estimates of data downloads (user class, dataset, size).
*   `FR-062` The system shall provide an administrative dashboard for System Operators and Data Operations Managers to view system metrics and logs.
*   `FR-063` The system shall support the scheduling and execution of weekly nightly database backups and weekly off-site backups.

## **4. Non-Functional Requirements**

### **4.1 Performance**
*   `NFR-001` The response time for metadata searches shall be less than 5 seconds under normal load.
*   `NFR-002` The system load (page responsiveness) shall not visibly deteriorate with up to 50 concurrent users.
*   `NFR-003` The system shall detect low client transmission speeds and may offer a low-bandwidth, non-graphical interface alternative.

### **4.2 Reliability & Availability**
*   `NFR-010` The system shall maintain 99% uptime, excluding scheduled maintenance windows.
*   `NFR-011` The system shall be designed for 24/7 availability.

### **4.3 Security**
*   `NFR-020` All authentication shall occur over encrypted connections (HTTPS).
*   `NFR-021` User passwords shall never be stored in plain text within the STEWARDS database.
*   `NFR-022` Data integrity checks (e.g., checksums, validation rules) shall be performed during all data upload transactions.
*   `NFR-023` The system shall be developed following USDA security policies for web applications.

### **4.4 Compliance**
*   `NFR-030` The public user interface shall comply with Section 508 accessibility standards.
*   `NFR-031` All system metadata shall be compliant with the FGDC Content Standard for Digital Geospatial Metadata.
*   `NFR-032` The web interface shall adhere to the official USDA web style guide.

## **5. Data Model**
The core persistent entities for the STEWARDS system are as follows. This is a logical model; the physical SQL Server schema will be derived from it.

*   **Watershed** (`Watershed_ID` PK, Name, Description, Boundary_Geometry`)
*   **Site** (`Site_ID` PK, `Watershed_ID` FK, Site_Code, Name, Description, Latitude, Longitude, Elevation`)
*   **Topic** (`Topic_ID` PK, Topic_Name, Description`) // e.g., "Precipitation", "Nitrate Concentration"
*   **Measurement_Data** (`Data_ID` PK, `Site_ID` FK, `Topic_ID` FK, Timestamp, Data_Value, Unit_Of_Measure, Quality_Flag, Is_Sensitive`)
*   **Metadata_Record** (`Metadata_ID` PK, `Data_Source_FK`, FGDC_Title, FGDC_Abstract, FGDC_Keywords, ... [All FGDC fields])
*   **Spatial_Layer** (`Layer_ID` PK, `Watershed_ID` FK, Layer_Name, Layer_Type, Format, Path_URL`)
*   **User** (`User_ID` PK, Username, User_Class, Last_Login`) // Authentication details managed externally.
*   **Upload_Transaction** (`Upload_ID` PK, `User_ID` FK, `Watershed_ID` FK, Upload_Timestamp, File_Name, Status, Validation_Log`)

## **6. External Interface Requirements**

### **6.1 User Interfaces**
*   The primary interface shall be a web application compatible with major browsers.
*   The layout shall be clean, professional, and consistent with USDA branding.
*   Key UI flows are defined in the Business Process section (1.3).

### **6.2 Hardware Interfaces**
*   The system shall run on standard USDA-approved server hardware.

### **6.3 Software Interfaces**
1.  **Database:** Microsoft SQL Server. The application shall execute SQL queries and stored procedures.
2.  **Authentication Service:** (e.g., LDAP query to Microsoft Active Directory). Input: Username/Password. Output: Authentication success/failure and user group membership.
3.  **GIS Server:** (e.g., ArcIMS). Input: Spatial query parameters (bounding box, layer name). Output: Map images or GIS data streams via standard protocols (WMS, WFS).
4.  **Email Service (SMTP):** Input: Recipient address, subject, body/link. Output: Sent email notification.

### **6.4 Communications Interfaces**
*   HTTP/HTTPS for all web traffic.
*   Potential FTP/SFTP for alternative large data delivery.

## **7. Appendices**

### **7.1 Acceptance Test Scenarios**
*   **Scenario 1 (Public Access):** Given a public user visits the STEWARDS portal, when they browse to a watershed and select a public dataset, then they can download the data in a tab-delimited format without logging in.
*   **Scenario 2 (Authenticated Search):** Given an ARS researcher is logged in, when they perform a metadata search by watershed and topic, then the system returns a list of relevant datasets with links to detailed site descriptions.
*   **Scenario 3 (Visualization):** Given a user has selected a time-series dataset, when they specify a date range and choose "View Chart", then the system generates a graphical plot of the data.
*   **Scenario 4 (Data Upload):** Given watershed staff have prepared an annual data file in the standard format, when they use the upload tool, then the data is validated and populated into the central database, and a confirmation is displayed.

### **7.2 Risk Management**
Refer to the provided Risk List and Mitigation Strategies in the project summary. These risks shall be reviewed and tracked in the project management plan.

### **7.3 Open Issues**
The following items are pending decisions and are the responsibility of the noted parties:
1.  Selection of specific metadata input tool. *(STEWARDS Database Team)*
2.  Detailed load-balancing and fail-over strategy for servers. *(OCIO)*
3.  Final determination of help desk funding and structure. *(NPS/STEWARDS Team)*
4.  Specific protocols for handling model input/output data and uncertainty reporting. *(CEAP Modeling Team)*
5.  Conversion plan if federal metadata standard shifts to ISO 19115. *(STEWARDS Database Team)*
6.  Detailed testing plan based on use cases. *(Development Team)*
7.  Final list of required GIS server applications and browser plug-ins. *(Development Team)*
8.  Procedures for handling intentional denial-of-service attacks. *(OCIO Security)*