# **STEWARDS System Requirements Specification (SRS)**

**Document Version:** 1.0
**Date:** [Date of Generation]
**Project:** Sustaining the Earth's Watersheds – Agricultural Research Data System (STEWARDS)
**Client:** USDA Agricultural Research Service (ARS)
**Prepared For:** ARS OCIO, Conservation Effects Assessment Project (CEAP)
**Status:** Draft for Review

---

## **1. Introduction**

### **1.1 Purpose**
This document defines the functional and non-functional requirements for the STEWARDS (Sustaining the Earth's Watersheds – Agricultural Research Data System). It serves as a formal agreement between the stakeholders and the development team, providing a comprehensive blueprint for system design, development, testing, and deployment. The intended audience includes project managers, system architects, developers, testers, and all stakeholders identified in Section 3.

### **1.2 Document Conventions**
*   **Requirements:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Priority:** (H)igh, (M)edium, (L)ow.
*   **Keywords:** The words `MUST`, `SHALL`, `SHOULD`, `MAY`, and `WILL` are used as defined in IETF RFC 2119.

### **1.3 Project Scope**
STEWARDS is a centralized data system designed to store, manage, and disseminate standardized water, soil, land management, and economic data from long-term ARS research watersheds. Its primary objective is to support the Conservation Effects Assessment Project (CEAP) by enabling cross-watershed, policy-relevant analyses of agricultural conservation practices.

#### **1.3.1 In Scope**
*   A centralized Microsoft SQL Server database for storing diverse watershed research data and associated metadata.
*   A secure, web-based client application for data discovery, visualization, and download.
*   Support for twelve (12) initial ARS Benchmark Watersheds participating in CEAP.
*   Mechanisms for periodic (annual or more frequent) ingestion of quality-assured data from watershed sites.
*   Data export capabilities in standard, interoperable formats (e.g., CSV, tab-delimited text, ESRI Shapefiles).

#### **1.3.2 Out of Scope**
*   Real-time data streaming or public access to real-time data feeds.
*   Primary data collection, sensor management, or initial field-level quality assurance/quality control (QA/QC).
*   Execution of agricultural models (e.g., SWAT, AnnAGNPS) within the system platform.
*   Development or enforcement of site-specific data collection or local management protocols.
*   Guarantee of data availability contingent on external site resources for data preparation.

### **1.4 References**
*   USDA/ARS IT Security Policies
*   USDA/ARS Web Accessibility Standards (Section 508 Compliance)
*   Conservation Effects Assessment Project (CEAP) Goals and Objectives
*   IETF RFC 2119: Key words for use in RFCs to Indicate Requirement Levels
*   ISO 19115 Geographic Information — Metadata (Noted for potential future use)

## **2. Overall Description**

### **2.1 Product Perspective**
STEWARDS is a new, self-contained web application and database system. It will interface with external watershed site personnel who act as data providers. The system does not replace local data systems but provides a centralized repository and dissemination portal. It must integrate into the existing ARS OCIO operational environment, adhering to all corporate infrastructure, security, and design standards.

### **2.2 Product Functions (Summary)**
1.  **Data Management:** Securely store and manage biophysical, geospatial, and economic data with robust metadata.
2.  **Data Ingestion:** Provide authenticated interfaces for watershed staff to upload and update data files.
3.  **Data Discovery:** Enable users to search, filter, and browse datasets by location, theme, time period, and other metadata.
4.  **Data Visualization:** Offer basic graphical visualization (e.g., time-series charts, map previews) of data subsets.
5.  **Data Export:** Allow users to download selected data in standard, analysis-ready formats.
6.  **System Administration:** Provide tools for user management, access monitoring, data stewardship, and system health oversight.

### **2.3 User Classes and Characteristics**
| User Class | Description | Key Characteristics |
| :--- | :--- | :--- |
| **Public User** | General public, educators, students. | No authentication required. Access limited to publicly released data. Minimal technical expertise assumed. |
| **Non-ARS Researcher** | Academic, NGO, or other government researchers. | Requires authentication. Cannot access sensitive/confidential data. Moderate to high technical expertise. |
| **ARS Researcher** | ARS scientists and collaborators. | Requires authentication. May have access to sensitive data under specific agreements. High technical expertise. |
| **Watershed Uploader** | Local staff at a participating watershed. | Authenticated, role-based access restricted to their watershed's data space. Infrequent system use (e.g., annual). |
| **Data Operations Manager / DBA** | ARS OCIO or designated data steward. | Full read/write/modify access to all data and system parameters. Responsible for archiving, backups, and data integrity. |
| **System Operator (OCIO Staff)** | ARS OCIO system administrators. | Full system access for maintenance, deployment, and monitoring of application/database servers. |

### **2.4 Operating Environment**
*   **Server:** Hosted on ARS OCIO-approved infrastructure (Windows Server environment).
*   **Database:** Microsoft SQL Server (corporate standard).
*   **Application Server:** Microsoft IIS or equivalent ARS-approved application server.
*   **Client:** Modern web browsers (Chrome, Firefox, Edge, Safari) with JavaScript enabled.
*   **Network:** Accessible via the public internet, protected by USDA/ARS firewall and security policies.

### **2.5 Design and Implementation Constraints**
1.  `CON-1`: The database layer **MUST** be implemented using Microsoft SQL Server. (H)
2.  `CON-2`: The web application **MUST** comply with all current USDA/ARS IT security, accessibility (e.g., Section 508), and web design standards. (H)
3.  `CON-3`: Data upload and management interfaces for Watershed Uploaders **MUST** be designed for simplicity and clarity, acknowledging their infrequent use. (H)
4.  `CON-4`: The system architecture **SHALL** be modular to accommodate future modifications (e.g., additional watersheds, new data types) without major overhaul. (M)
5.  `CON-5`: Project implementation is contingent upon continued funding and the availability of an operational hosting platform within ARS OCIO. (H)

### **2.6 Assumptions and Dependencies**
*   Participating watershed sites will have the resources and willingness to prepare and upload data according to agreed schedules and formats.
*   ARS OCIO will provide a stable, supported hosting environment for the application and database servers.
*   Clear data sharing agreements and definitions of "sensitive data" will be established prior to system launch.

## **3. System Features and Requirements**

### **3.1 User Authentication and Authorization**
*   `FR-001`: The system **SHALL** support role-based access control (RBAC) for all authenticated functions. (H)
*   `FR-002`: The system **SHALL** allow Public Users to access all non-password-protected data and features without any login. (H)
*   `FR-003`: The system **SHALL** provide a login mechanism using ARS-approved credentials (e.g., USDA eAuth) for all other user classes. (H)
*   `FR-004`: The system **SHALL** restrict Watershed Uploaders to view and modify only the data and metadata associated with their assigned watershed(s). (H)
*   `FR-005`: The system **SHALL** enforce data sensitivity flags, preventing Non-ARS Researchers from accessing data marked as confidential. (H)

### **3.2 Data Management and Ingestion**
*   `FR-010`: The system **SHALL** provide a secure, web-based interface for authenticated Watershed Uploaders to upload data files (e.g., CSV, XML, shapefile components). (H)
*   `FR-011`: The system **SHALL** allow Uploaders to associate uploaded data with descriptive metadata (e.g., parameter, units, time range, quality level). (H)
*   `FR-012`: The system **SHALL** validate the format and completeness of critical metadata upon upload and provide clear error messages. (H)
*   `FR-013`: The system **SHALL** store all data and metadata in a structured Microsoft SQL Server database. (H)
*   `FR-014`: The Data Operations Manager **SHALL** have an interface to review, approve, or reject uploaded data before it becomes publicly visible, if required by workflow. (M)

### **3.3 Data Discovery and Search**
*   `FR-020`: The system **SHALL** provide a public-facing catalog of all watersheds, research sites, and available datasets with summary descriptions. (H)
*   `FR-021`: All users **SHALL** be able to search and filter available datasets by: Watershed Name, Geographic Location (state, bounding box), Data Theme (e.g., water quality, precipitation), Time Period, and Parameter. (H)
*   `FR-022`: Search results **SHALL** display key metadata (title, location, date range, abstract) and indicate access restrictions. (H)
*   `NFR-001`: A metadata search returning < 10,000 records **SHALL** complete within 3 seconds 95% of the time. (H)

### **3.4 Data Visualization and Exploration**
*   `FR-030`: For time-series data, the system **SHALL** generate an interactive chart (e.g., line graph) for a user-specified date range. (H)
*   `FR-031`: For geospatial data (e.g., sampling stations, watershed boundaries), the system **SHALL** display data locations on an interactive map. (H)
*   `FR-032`: Visualizations **SHALL** be generated dynamically based on user-selected parameters and date ranges without requiring a full data download. (H)

### **3.5 Data Export and Download**
*   `FR-040`: Users **SHALL** be able to select specific datasets or data subsets (defined by search, visualization, or manual selection) for download. (H)
*   `FR-041`: The system **SHALL** offer data download in the following standard formats: Comma-Separated Values (CSV), Tab-Delimited Text, and ESRI Shapefile (for spatial data). (H)
*   `FR-042`: Downloaded data files **SHALL** include relevant metadata (as a separate file or header) describing the source, parameters, units, and date of extraction. (M)

### **3.6 System Administration and Reporting**
*   `FR-050`: The Data Operations Manager **SHALL** have an administrative interface to manage user accounts and role assignments. (H)
*   `FR-051`: The system **SHALL** log all user logins, data queries, and download events. (H)
*   `FR-052`: The Data Operations Manager **SHALL** be able to generate reports on system usage metrics (e.g., number of unique users, top downloaded datasets, access patterns). (M)
*   `FR-053`: The System Operator **SHALL** have access to system health dashboards (e.g., server status, disk space, error logs). (H)

## **4. Non-Functional Requirements**

### **4.1 Performance Requirements**
*   `NFR-002`: The system **SHALL** maintain 99% availability during standard operational hours (defined as 7:00 AM to 7:00 PM EST, Monday-Friday, excluding planned maintenance). (H)
*   `NFR-003`: The application interface **SHALL** load initial pages within 4 seconds over a standard broadband connection. (M)
*   `NFR-004`: The system **MUST** be designed to handle concurrent access from a minimum of 50 users. (M)

### **4.2 Safety and Security Requirements**
*   `NFR-005`: All authentication **MUST** comply with USDA/ARS password and account management policies. (H)
*   `NFR-006`: All data transmission between the client and server **MUST** use TLS 1.2 or higher encryption. (H)
*   `NFR-007`: The system **MUST** protect against common web vulnerabilities (e.g., SQL injection, cross-site scripting) as defined by OWASP Top 10. (H)
*   `NFR-008`: Database backups **SHALL** be performed according to ARS OCIO disaster recovery policies. (H)

### **4.3 Software Quality Attributes**
*   **Usability:** Interfaces for Watershed Uploaders must be intuitive, with clear instructions and validation feedback. Public interfaces must be clean and navigable for non-experts.
*   **Reliability:** The system must ensure data integrity, preventing corruption during upload, storage, or download processes.
*   **Maintainability:** The codebase and database schema must be well-documented to facilitate future updates by ARS OCIO staff.
*   **Interoperability:** Data export formats must be widely compatible with standard analysis software (e.g., Excel, R, ArcGIS, QGIS).

## **5. Appendices**

### **5.1 Glossary**
*   **CEAP:** Conservation Effects Assessment Project.
*   **ARS:** Agricultural Research Service.
*   **OCIO:** Office of the Chief Information Officer.
*   **QA/QC:** Quality Assurance / Quality Control.
*   **Metadata:** Data that describes other data (e.g., who collected it, when, where, units of measurement).

### **5.2 Success Metrics**
*   Achieve 99% system availability as defined in `NFR-002`.
*   Achieve sub-3-second metadata search performance as defined in `NFR-001`.
*   Secure successful data updates from >90% of participating watersheds according to their annual negotiated schedules.

### **5.3 Undecided / TBD Issues**
1.  **Storage Capacity:** Final storage requirements (hundreds of MB vs. GB+) need to be quantified based on sample data from the 12 initial watersheds.
2.  **Load Balancing:** The detailed strategy for load balancing across application and database servers will be finalized during the architectural design phase with ARS OCIO.
3.  **Support Model:** Funding, staffing, and procedures for user help desk support are to be determined.
4.  **Metadata Standard:** A decision on implementing ISO 19115-compliant metadata is pending future mandate or stakeholder consensus.
5.  **Detailed Test Plan:** A comprehensive test plan covering all user roles and use cases will be developed as a separate document.