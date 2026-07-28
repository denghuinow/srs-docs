# Short Summary: STEWARDS System Requirements Specification

## Background and Objectives
The USDA Agricultural Research Service (ARS) is developing the STEWARDS (Sustaining the Earth's Watersheds – Agricultural Research Data System) to provide centralized, standardized access to water, soil, management, and economic data from long-term research watersheds. The primary objective is to support the Conservation Effects Assessment Project (CEAP) by enabling policy-relevant, multi-site analyses of conservation practice effects, while serving broader research and public needs.

## In Scope
*   Centralized database management system for storing and managing diverse watershed data (biophysical, land use, economic).
*   Web-based client application for users to access, search, visualize, and download data.
*   Support for twelve initial ARS Benchmark Watersheds participating in CEAP.
*   Annual or more frequent data updates from watershed sites after local quality assurance.
*   Provision of data in standardized formats (e.g., tab-delimited text, shapefiles) for user download.

## Out of Scope
*   Real-time public data access; real-time data remains at the discretion of individual watershed teams.
*   Primary responsibility for data collection and initial quality assurance; this remains with local watershed researchers.
*   Direct management of agricultural model (e.g., SWAT, AnnAGNPS) execution within the system; focus is on providing input data and storing results.
*   Development of location-specific data management protocols; sites may retain existing systems.
*   Guarantee of data availability if watershed sites lack resources for data preparation and upload.

## Stakeholders and Core Use Cases
*   **System Operator (OCIO Staff):** Maintains executable code and requires full system access.
*   **Data Operations Manager / DBA:** Manages data archiving and maintenance with read/write/modify privileges to all data.
*   **Watershed Uploader (Local Staff):** Uploads local data to their watershed's allocated space in the system.
*   **ARS Researcher:** Accesses data for ARS research purposes, potentially including sensitive data under confidentiality agreements.
*   **Non-ARS Researcher:** Accesses data for external research but cannot access password-protected sensitive data.
*   **Public User:** Accesses publicly released data without authentication.

**User Stories:**
1.  As a **Watershed Uploader**, I want to upload annual, quality-assured data files so that the central database is updated with our latest research findings.
2.  As an **ARS Researcher**, I want to search and query metadata across all watersheds by location and theme so that I can find relevant datasets for my analysis.
3.  As a **Non-ARS Researcher**, I want to visualize time-series data (e.g., stream discharge) in a chart over a specified period so that I can select the correct subset for download.
4.  As a **Public User**, I want to browse summary descriptions of watersheds and sampling stations so that I can understand the context of the available data.
5.  As a **Data Operations Manager**, I want to monitor user access and data download metrics so that I can report on system usage and plan for capacity.
6.  As any **User**, I want to download selected data in standard formats (CSV, shapefiles) so that I can use it in my local software applications (e.g., ArcGIS).

## Success Metrics
*   System availability of 99% during intended operational hours.
*   Query response times for metadata searches within a few seconds.
*   Successful annual data updates from participating watershed sites as per negotiated schedules.

## Major Constraints
*   Must use the corporate standard Microsoft SQL Server database engine.
*   Must comply with all USDA/ARS accessibility, web design, and security policies.
*   Data uploading and management interfaces must be simple due to infrequent (e.g., annual) use by watershed staff.
*   The system design must allow for future modifications without a large overhaul.
*   Implementation is dependent on continued funding and the availability of an operational platform at ARS OCIO.

## Undecided Issues
*   Specific data storage capacity requirements (hundreds of megabytes vs. gigabytes).
*   Final details of the load-balancing strategy for application and database servers.
*   The extent and specifics of help desk funding and staffing.
*   Potential future conversion of metadata to the ISO 19115 standard if mandated.
*   Detailed testing plan based on user roles and use cases is to be documented later.