# Software Requirements Specification (SRS)
## STEWARDS System
### Sustaining The Earth’s Watersheds, Agricultural Research Data System

**Document Version:** 1.0  
**Date:** [Date of Generation]  
**Prepared for:** USDA Agricultural Research Service (ARS)  
**Prepared by:** [Your Organization/Team Name]

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the STEWARDS (Sustaining The Earth’s Watersheds, Agricultural Research Data System). The primary audience for this document includes the project stakeholders, development team, quality assurance team, and system administrators. This SRS serves as the foundation for system design, implementation, testing, and project management.

### 1.2 Scope
STEWARDS is a centralized data repository and access system designed to provide one-point access to standardized, well-documented water, soil, management, and economic data from USDA-ARS research watersheds. The system's core purpose is to support the Conservation Effects Assessment Project (CEAP) by enabling policy-relevant, multi-site analyses of conservation practice effects.

**In-Scope:**
*   A web-based portal for searching, visualizing, and downloading integrated watershed data.
*   A backend system for ingesting, translating, storing, and managing data from twelve (12) initial ARS Benchmark Watersheds.
*   Role-based access control for six distinct user classes.
*   Support for time-series and spatial (GIS) data types.
*   Enforcement of FGDC-compliant metadata for all datasets.
*   System administration functions for backup, monitoring, and user management.

**Out-of-Scope:**
*   In-field data collection hardware and software.
*   Advanced statistical or hydrological modeling tools within the portal.
*   Real-time data streaming and processing.
*   Development of data preparation tools for watershed sites (though interface for uploading their prepared data is in-scope).

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **ARS** | Agricultural Research Service |
| **CEAP** | Conservation Effects Assessment Project |
| **FGDC** | Federal Geographic Data Committee |
| **GIS** | Geographic Information System |
| **NRCS** | Natural Resources Conservation Service |
| **OCIO** | Office of the Chief Information Officer |
| **QA/QC** | Quality Assurance / Quality Control |
| **PK** | Primary Key (Database) |
| **SRS** | Software Requirements Specification |
| **STEWARDS** | Sustaining The Earth’s Watersheds, Agricultural Research Data System |

### 1.4 References
*   USDA ARS Web Policies and Standards
*   FGDC Content Standard for Digital Geospatial Metadata
*   USDA Enterprise Architecture Guidelines
*   Project Charter: STEWARDS System Development

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its users, and constraints. Section 3 details the specific functional and data requirements. Section 4 outlines non-functional requirements. Appendices may contain supplementary diagrams or models.

## 2. Overall Description

### 2.1 Product Perspective
STEWARDS is a new, self-contained web application. It will interface with the existing ARS OCIO infrastructure in Beltsville, MD, for hosting, authentication services, and network security. It must comply with overarching USDA IT policies.

### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Responsibilities |
| :--- | :--- | :--- |
| **Public User** | No authentication required. Limited technical expertise assumed. | Browse and download publicly available data. |
| **Research User** | Authenticated non-ARS researcher. Subject-matter expertise varies. | Search, visualize, and download non-sensitive data for research. |
| **ARS User** | Authenticated ARS researcher. High domain expertise. | Full access to search, visualize, and download all ARS data (including protected). |
| **Watershed Uploader** | Authenticated watershed staff. Infrequent system user. | Upload QA/QC'd data and metadata for their assigned watershed(s). |
| **Data Operations Manager** | Authenticated OCIO staff. High technical and data management expertise. | Manage data archiving, metadata compliance, and system data integrity. |
| **System Operator** | Authenticated OCIO staff. Highest system privileges. | Maintain application code, perform system backups, monitor health, manage user accounts. |

### 2.3 Operating Environment
*   **Software:** Application will be deployed on ARS OCIO-approved web and database servers. Specific stack (.NET, specific GIS server) is currently undecided.
*   **Hardware:** Hosted on ARS OCIO infrastructure in Beltsville, MD. Scalable storage and load balancing details are undecided.
*   **Network:** Accessible via the public internet, protected by USDA firewall and security policies.

### 2.4 Design and Implementation Constraints
1.  Must comply with USDA web style guides, accessibility standards (Section 508), and IT security policies.
2.  Database schema must be modular and extensible to accommodate future watersheds and data topics.
3.  System must be designed for 99% availability.
4.  All metadata must be compliant with the FGDC standard at launch.

### 2.5 Assumptions and Dependencies
**Assumptions:**
1.  Watershed sites will have the resources to prepare data in the required standard exchange format at least annually.
2.  NRCS/ARS funding will continue through FY07 and potentially beyond.
3.  Users will have a modern web browser with JavaScript enabled.

**Dependencies:**
1.  Continued funding from NRCS/ARS.
2.  Provision of data preparation resources by participating watershed sites.
3.  Availability of ARS OCIO infrastructure and support for deployment.

## 3. System Features and Requirements

### 3.1 Functional Requirements

#### FR-1: Data Ingestion and Management
*   **FR-1.1:** The system shall provide an authenticated web interface for Watershed Uploaders to upload data files for their authorized watershed(s).
*   **FR-1.2:** Upon upload, the system shall automatically translate data from the standard exchange format into the internal STEWARDS database schema.
*   **FR-1.3:** The system shall require and validate the presence of an FGDC-compliant metadata record for each dataset upon upload.
*   **FR-1.4:** The system shall provide an interface for the Data Operations Manager to view, edit, and validate metadata records for compliance.
*   **FR-1.5:** The system shall allow the Data Operations Manager to flag datasets for review, archive, or deletion.

#### FR-2: Data Discovery and Search
*   **FR-2.1:** The system shall provide a public catalog for browsing data by watershed.
*   **FR-2.2:** The system shall provide a search interface for users to query metadata by: Location (watershed, coordinates), Theme/Topic (e.g., water quality, climate), and Free-text keywords.
*   **FR-2.3:** Search results shall be displayed in a list, showing dataset title, watershed, abstract, and date range.
*   **FR-2.4:** The system shall enforce access controls, filtering out sensitive datasets from search results for Public and Research Users.

#### FR-3: Data Visualization and Access
*   **FR-3.1:** For time-series data, the system shall generate interactive charts (e.g., discharge over time) based on user-selected date ranges.
*   **FR-3.2:** The system shall provide a tabular view of raw data points underlying any visualization.
*   **FR-3.3:** For spatial data layers, the system shall integrate a GIS web interface (e.g., interactive map) to allow users to view layer boundaries and attributes.
*   **FR-3.4:** Visualizations and data views shall be rendered within the user's browser without requiring additional plugins.

#### FR-4: Data Export
*   **FR-4.1:** Users shall be able to select one or more datasets from search results or visualizations for download.
*   **FR-4.2:** The system shall export time-series data in CSV format.
*   **FR-4.3:** The system shall export spatial data in ESRI Shapefile format.
*   **FR-4.4:** All data downloads shall be bundled with their associated FGDC metadata in a standard XML format.

#### FR-5: User and System Administration
*   **FR-5.1:** The System Operator shall be able to create, modify, enable, disable, and delete user accounts.
*   **FR-5.2:** The System Operator shall be able to assign users to one or more user classes (roles).
*   **FR-5.3:** The system shall perform automated, encrypted backups of the database and file storage on a scheduled basis.
*   **FR-5.4:** The system shall provide a dashboard for System Operators to monitor system health (uptime, disk space, recent errors).

### 3.2 Data Requirements
The system shall store and manage the following core entities and their attributes:

```sql
-- Core Data Entities (Conceptual Schema)
Watershed {
    Watershed_ID (PK): Integer
    Name: String
    Location: Geometry/Text
    Description: Text
    Research_Goals: Text
}

Site {
    Site_ID (PK): Integer
    Watershed_ID (FK): Integer
    Location_Coordinates: Geometry
    Station_Type: String
    Description: Text
}

DataTopic {
    Topic_ID (PK): Integer
    Topic_Name: String (e.g., "Climate", "Water Quality")
    Description: Text
    Measurement_Unit_Lookup: String
}

TimeSeriesData {
    Data_Record_ID (PK): Integer
    Site_ID (FK): Integer
    Topic_ID (FK): Integer
    Timestamp: DateTime
    Parameter_Value: Float
    Quality_Flag: String
}

SpatialDataLayer {
    Layer_ID (PK): Integer
    Watershed_ID (FK): Integer
    Layer_Name: String
    Data_Format: String (e.g., "Shapefile", "GeoTIFF")
    Description: Text
    File_Path: String
}

MetadataRecord {
    Metadata_ID (PK): Integer
    Dataset_ID: Integer -- Foreign key to either TimeSeries or Spatial Data
    Dataset_Type: String -- e.g., "TimeSeries", "Spatial"
    FGDC_Compliant_XML: XML
    Abstract: Text
    Quality_Assurance_Info: Text
}
```

## 4. Non-Functional Requirements

### 4.1 Performance
*   **NFR-P.1:** Simple metadata searches and queries shall return results within 5 seconds for 95% of requests under normal load.
*   **NFR-P.2:** Generation of standard visualizations (charts for 1 year of daily data) shall complete within 10 seconds.
*   **NFR-P.3:** The system shall be capable of handling large data export requests (e.g., decadal datasets). Users shall be notified that such requests may take minutes to hours and may be delivered asynchronously via email.

### 4.2 Availability
*   **NFR-A.1:** The system shall achieve 99% operational uptime, excluding scheduled maintenance windows.
*   **NFR-A.2:** Scheduled maintenance shall be announced at least 48 hours in advance and shall not exceed 4 hours per month.

### 4.3 Security
*   **NFR-S.1:** The system shall integrate with ARS OCIO authentication services.
*   **NFR-S.2:** All user sessions shall be conducted over HTTPS.
*   **NFR-S.3:** Role-Based Access Control (RBAC) shall be strictly enforced as defined in Section 2.2.
*   **NFR-S.4:** All user input shall be sanitized to prevent SQL injection and cross-site scripting (XSS) attacks.
*   **NFR-S.5:** Sensitive data shall be stored and transmitted in a manner consistent with ARS data confidentiality policies.

### 4.4 Usability
*   **NFR-U.1:** The user interface shall be consistent with USDA web style guidelines.
*   **NFR-U.2:** A first-time Public User shall be able to locate and download a public dataset within 3 minutes without training.
*   **NFR-U.3:** The data upload interface for Watershed Uploaders shall be wizard-based or similarly guided, with clear instructions and validation feedback.

### 4.5 Portability & Adaptability
*   **NFR-PA.1:** The database design shall use abstraction layers (e.g., stored procedures, ORM) to minimize the impact of future schema changes on the application code.
*   **NFR-PA.2:** The system shall be designed to allow for the addition of new watersheds and data topics through configuration files or admin interfaces, where possible, without code modification.

### 4.6 Compliance
*   **NFR-C.1:** The system shall comply with USDA Web Style Guide.
*   **NFR-C.2:** The system shall meet Section 508 accessibility standards.
*   **NFR-C.3:** All system components shall comply with ARS OCIO security hardening policies.

## 5. Appendices

### Appendix A: User Story Mapping to Requirements
| User Story | Related Functional Requirements |
| :--- | :--- |
| 1. Watershed Uploader: Upload data | FR-1.1, FR-1.3 |
| 2. ARS User: Search metadata | FR-2.1, FR-2.2, FR-2.3 |
| 3. Research User: Visualize time-series | FR-3.1, FR-3.2 |
| 4. Public User: Download spatial data | FR-2.1, FR-3.3, FR-4.1, FR-4.3 |
| 5. Data Ops Manager: Ensure FGDC metadata | FR-1.3, FR-1.4 |
| 6. System Operator: 99% availability | NFR-A.1 |

### Appendix B: Open Issues and TBDs
1.  **Metadata Creation Workflow:** Specific tools and detailed steps for watershed staff to create/edit FGDC metadata are undetermined.
2.  **Technology Stack:** Final selection of application framework (.NET versions), GIS server software (ArcGIS Server, GeoServer, etc.), and database system is pending.
3.  **Hardware Scaling:** Detailed specifications for web/application servers, database servers, load balancers, and scalable storage are to be defined.
4.  **Support Model:** Formal procedures, service level agreements (SLAs), and staffing for user help desk support are not yet established.
5.  **Future Watershed Integration:** Protocol for adding three potential additional watersheds with different land uses is to be developed.
6.  **Metadata Standard Evolution:** A contingency plan for migrating from FGDC to the ISO 19115 metadata standard, if required, is needed.