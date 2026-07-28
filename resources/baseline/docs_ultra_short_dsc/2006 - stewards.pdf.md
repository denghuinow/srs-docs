# Software Requirements Specification (SRS) for STEWARDS
**Document Version:** 1.0  
**Date:** [Date of Generation]  
**Prepared for:** USDA Agricultural Research Service (ARS)  
**Prepared by:** [Your Organization/Name]

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the STEWARDS (Sustaining The Earth’s Watersheds - Agricultural Research Data System) data portal. The primary purpose of this document is to provide a detailed description of the system's capabilities, interfaces, and performance characteristics to serve as a foundation for design, development, testing, and acceptance. The intended audience includes project stakeholders, system architects, developers, testers, and the ARS Office of the Chief Information Officer (OCIO).

### 1.2 Scope
STEWARDS is a centralized web-based data portal designed to provide single-point access to standardized, well-documented water, soil, management, and economic data from multiple, historically independent ARS research watersheds. The system serves as the central repository for the Conservation Effects Assessment Project (CEAP) watershed assessment studies and supports broader agricultural and hydrological research.

**In-Scope:**
*   Consolidation and storage of diverse, standardized data types from up to 15 ARS watersheds.
*   Provision of tools for browsing, querying, visualizing, and downloading data and metadata.
*   Support for annual data uploads from watershed locations using standardized formats.
*   Implementation of role-based access control for different user classes.
*   Maintenance of a searchable metadata catalog compliant with Federal Geographic Data Committee (FGDC) standards.
*   Delivery of user support via documentation, tutorials, and help desk functions.

**Out-of-Scope:**
*   Provision of real-time data access. Data updates occur annually following local quality assurance.
*   Replacement of local data management responsibilities at individual watersheds.
*   Direct data collection from field sensors or instruments.

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **ARS** | Agricultural Research Service |
| **CEAP** | Conservation Effects Assessment Project |
| **ERS** | Economic Research Service |
| **FGDC** | Federal Geographic Data Committee |
| **NRCS** | Natural Resources Conservation Service |
| **OCIO** | Office of the Chief Information Officer |
| **QA/QC** | Quality Assurance / Quality Control |
| **SRS** | Software Requirements Specification |
| **STEWARDS** | Sustaining The Earth’s Watersheds - Agricultural Research Data System |
| **SWAT/AnnAGNPS** | Agricultural hydrological and water quality models |

### 1.4 References
*   USDA ARS Web Policies and Standards
*   Federal Geographic Data Committee (FGDC) Metadata Standards
*   USDA Accessibility Requirements (Section 508)

### 1.5 Document Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details specific functional requirements. Section 4 outlines non-functional requirements. Section 5 covers external interface requirements. Section 6 lists other requirements including constraints and dependencies.

## 2. Overall Description

### 2.1 Product Perspective
STEWARDS is a new, self-contained web application that operates within the existing ARS OCIO IT infrastructure. It interfaces with users via a standard web browser and relies on backend database and application servers managed by the OCIO. The system positions itself as the authoritative central repository for CEAP watershed data, integrating data from ARS watersheds and other agencies (NRCS, ERS) to support analytical models and research.

### 2.2 Product Functions
The core functions of STEWARDS are:
1.  **Data Repository:** Securely store and manage diverse data types (biophysical, spatial, time-series, land use, economic).
2.  **Data Discovery & Access:** Allow users to browse, search, query, and download datasets and their associated metadata.
3.  **Data Visualization:** Provide integrated tools for visualizing time-series charts and spatial data within an interactive map interface.
4.  **Data Ingestion:** Support authenticated watershed personnel in uploading and validating data annually using system-defined templates and filters.
5.  **Metadata Management:** Maintain a comprehensive, searchable metadata database that complies with FGDC standards.
6.  **Reporting & Export:** Generate tabular reports and enable data export in standard, research-ready formats (e.g., CSV, Shapefile).
7.  **User Support:** Provide online documentation, tutorials, and a mechanism for help desk support.

### 2.3 User Characteristics
| User Class | Skill Level | Key Responsibilities / Needs |
| :--- | :--- | :--- |
| **System Operators & Data Managers (OCIO Staff)** | Expert | Full administrative access for system maintenance, user management, backup, archiving, and troubleshooting. |
| **Watershed Uploaders** | Intermediate (Technical) | Authenticated access to upload, validate, and manage data specifically for their assigned watershed(s) on an annual cycle. |
| **ARS Researchers** | Intermediate to Expert | Authenticated access to query, visualize, and download all data (including sensitive agency data) for research purposes. |
| **Non-ARS Researchers** | Intermediate to Expert | Authenticated access to query, visualize, and download only publicly released data. |
| **Public Users** | Novice to Intermediate | Unauthenticated, read-only access to browse and download publicly released data and metadata. |

### 2.4 Operating Environment
*   **Hardware:** Resides on ARS OCIO-managed network servers (likely located at the Beltsville center) with T1 or higher network connections.
*   **Software:**
    *   **Server:** Microsoft Windows Server, Microsoft SQL Server (database), IIS/Apache (web server).
    *   **Client:** Platform-independent web interface compatible with standard browsers (Internet Explorer, Netscape, Firefox as per contemporary standards).
*   **Policy:** Must comply with all USDA and ARS OCIO security, accessibility, and web design policies.

### 2.5 Design and Implementation Constraints
1.  **Database:** The system must utilize the corporate standard Microsoft SQL Server for the primary database management system.
2.  **Compliance:** The application must adhere to USDA accessibility standards (e.g., Section 508), web design policies, and IT security policies.
3.  **Client-Side Independence:** Client-side code (e.g., HTML, JavaScript) must be as platform- and browser-independent as possible.
4.  **Architecture:** The system must be designed for maintainability, allowing modifications to the database schema without requiring a complete system overhaul.

### 2.6 Assumptions and Dependencies
*   **Assumptions:**
    *   Each participating watershed location will have the necessary resources and personnel to prepare and upload data in the required standardized format.
    *   The ARS OCIO operational platform in Beltsville will be available and supported for hosting.
*   **Dependencies:**
    *   Partial project funding is anticipated from NRCS through FY07.
    *   The long-term operational viability of STEWARDS depends on future funding from ARS base or discretionary funds.

## 3. System Features and Requirements

### 3.1 Feature 1: Data Management and Storage
**Description:** The system shall provide a secure, structured repository for diverse data types from multiple watersheds.
**Priority:** High

| Requirement ID | Requirement Description |
| :--- | :--- |
| **FR1.1** | The system shall store biophysical data (e.g., water quality, soil properties). |
| **FR1.2** | The system shall store geospatial data (e.g., watershed boundaries, monitoring site locations). |
| **FR1.3** | The system shall store time-series data (e.g., stream discharge, precipitation). |
| **FR1.4** | The system shall store land use and management practice data. |
| **FR1.5** | The system shall store economic data related to agricultural practices. |
| **FR1.6** | The system shall associate all stored data with comprehensive FGDC-compliant metadata. |

### 3.2 Feature 2: Data Discovery, Access, and Download
**Description:** Users shall be able to find, explore, and retrieve data based on various criteria.
**Priority:** High

| Requirement ID | Requirement Description |
| :--- | :--- |
| **FR2.1** | The system shall provide a public browse interface to explore data by watershed, site, or data topic. |
| **FR2.2** | The system shall provide a search interface for metadata (keywords, location, date range, parameter). |
| **FR2.3** | The system shall allow authenticated users to perform advanced queries on the data itself. |
| **FR2.4** | The system shall enable users to download datasets in standard formats (e.g., CSV for tabular data, Shapefile for spatial data). |
| **FR2.5** | The system shall automatically download the corresponding metadata file with any dataset download. |

### 3.3 Feature 3: Data Visualization
**Description:** The system shall provide integrated tools for graphical and spatial representation of data.
**Priority:** Medium

| Requirement ID | Requirement Description |
| :--- | :--- |
| **FR3.1** | The system shall provide an interactive map view to display watershed boundaries, monitoring sites, and other spatial layers. |
| **FR3.2** | Users shall be able to select sites from the map to access associated data and metadata. |
| **FR3.3** | The system shall generate time-series plots (e.g., hydrographs, concentration trends) for selected data. |
| **FR3.4** | Visualization tools shall be accessible within the web browser without requiring specialized client software. |

### 3.4 Feature 4: Data Upload and Validation
**Description:** Authorized watershed personnel shall be able to submit new or updated data annually.
**Priority:** High

| Requirement ID | Requirement Description |
| :--- | :--- |
| **FR4.1** | The system shall provide a secure, authenticated upload portal for Watershed Uploaders. |
| **FR4.2** | The system shall enforce the use of standardized data templates and formats during upload. |
| **FR4.3** | The system shall perform initial automated quality control (QC) filters and validation checks on uploaded data. |
| **FR4.4** | The system shall provide clear feedback to the uploader on the success or failure of the upload and validation process. |
| **FR4.5** | Uploaded data shall remain in a "staging" state until approved/released by a designated data manager. |

### 3.5 Feature 5: User Management and Security
**Description:** The system shall control access based on user roles and protect data integrity.
**Priority:** High

| Requirement ID | Requirement Description |
| :--- | :--- |
| **FR5.1** | The system shall implement user authentication (username/password). |
| **FR5.2** | The system shall enforce role-based access control (RBAC) as defined in Section 2.3. |
| **FR5.3** | ARS Researchers shall have access to all data, including sensitive datasets not available to the public. |
| **FR5.4** | Non-ARS Researchers shall only have access to data flagged as "Public." |
| **FR5.5** | Public users shall have read-only access to public data without authentication. |
| **FR5.6** | The system shall protect data from unauthorized modification or deletion. |
| **FR5.7** | All user actions (uploads, downloads, logins) shall be logged for auditing purposes. |

### 3.6 Feature 6: Reporting and Help
**Description:** The system shall provide output reports and support resources.
**Priority:** Medium

| Requirement ID | Requirement Description |
| :--- | :--- |
| **FR6.1** | The system shall generate standardized tabular reports summarizing data availability by watershed or parameter. |
| **FR6.2** | The system shall provide comprehensive online user documentation and tutorials. |
| **FR6.3** | The system shall include a "Help Desk" contact mechanism or ticket system for user support. |

## 4. Non-Functional Requirements

### 4.1 Performance
*   **Query Response:** Metadata search queries shall return results within a few seconds under normal load.
*   **Data Retrieval:** Retrieval and preparation of large, complex datasets for download may take from several minutes to hours. Users must be notified of expected delays for large requests.
*   **Concurrent Users:** The system shall support a minimum of [TBD] concurrent users without significant degradation in performance.

### 4.2 Security
*   The system shall implement confidentiality controls to ensure users can only access data appropriate to their role.
*   All data transmissions involving authentication or sensitive data shall use encryption (e.g., HTTPS).
*   Security practices must follow ARS OCIO policies and standards.

### 4.3 Availability
*   The web portal shall be available 24 hours a day, 7 days a week, with a target uptime of 99%, excluding scheduled maintenance windows.

### 4.4 Data Integrity
*   Extensive QA/QC is the responsibility of the local watershed prior to upload.
*   The system shall perform validation checks during upload to catch format errors and basic outliers.
*   Once approved and stored, data shall be protected from unauthorized modification. Versioning of datasets may be considered.

### 4.5 Maintainability
*   The database schema shall be modular and well-documented to allow for the addition of new data types or watersheds without a major system overhaul.
*   The codebase shall adhere to standard coding practices to facilitate future updates and bug fixes.

## 5. External Interface Requirements

### 5.1 User Interfaces
*   The primary interface shall be a web-based application compatible with standard browsers (as of project date: Internet Explorer, Netscape, Firefox).
*   The interface shall be intuitive, consistent, and compliant with USDA web design and accessibility standards.

### 5.2 Software Interfaces
*   **Database:** Microsoft SQL Server.
*   **Web Server:** Microsoft Internet Information Services (IIS) or Apache, as provisioned by ARS OCIO.
*   **Application Logic:** Developed in a language compatible with the OCIO environment (e.g., ASP.NET, Java).

### 5.3 Communications Interfaces
*   The system shall operate over standard HTTP/HTTPS protocols.
*   It shall rely on the existing ARS OCIO network infrastructure at the Beltsville center.

## 6. Other Requirements

### 6.1 Acceptance Criteria
System acceptance will be based on:
1.  Successful demonstration of all high-priority functional requirements (FR1.x, FR2.x, FR4.x, FR5.x).
2.  Validation through user testing that the interface is clear, complete, and consistent for all user classes.
3.  Verification that performance metrics (query response times, availability) are met.
4.  Confirmation that the system operates within the defined constraints (SQL Server, USDA policies).

### 6.2 Priority of Features
The highest priority is the robust **Database Management System** (core of Features 1 & 4), as it forms the foundational component for all other functionality. Following this, data access (Feature 2) and security (Feature 5) are critical. Visualization (Feature 3) and reporting (Feature 6) are important but of secondary priority.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Technical Lead | | | |
| Quality Assurance | | | |