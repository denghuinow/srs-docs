# STEWARDS System Requirements Specification

## 1. Introduction

### 1.1 Purpose
The USDA Agricultural Research Service (ARS) is developing STEWARDS (Sustaining the Earth's Watersheds – Agricultural Research Data System) to organize, document, manipulate and compile water, soil, management, and economic data for assessment of conservation practices. The system provides one-point access to data from ARS research watersheds in well-documented, standardized formats, supporting the Conservation Effects Assessment Project (CEAP) watershed-scale assessment.

### 1.2 Project Scope
STEWARDS supports twelve ARS Benchmark Watersheds representing primarily rainfed cropland, with some containing irrigated cropland, grazingland, wetlands, and confined animal feeding operations. The system delivers consistent high quality data through a one-stop data portal to CEAP clients and eventually the public. It consists of two main parts: a central database management system for storage and management of data, and a client application for user access and interaction with data.

## 2. Overall Description

### 2.1 Product Perspective
STEWARDS is a new, centralized data system sourcing data from long-term ARS watersheds, with CEAP project participants expected to participate first. ARS researchers at watershed locations retain primary responsibility for data collection and management.

### 2.2 Product Features
The system enables diverse end-users to access, search, analyze, visualize, download, and report various types of integrated watershed data including:
- Biophysical data (point-based, spatially variable, time series)
- Land use, management, and conservation practices data
- Economic data
- Data from NRCS, ERS, NASS and other agencies where applicable

### 2.3 User Classes
- UCC-1: System operator (OCIO staff with full system access)
- UCC-2: Data operations manager (DBA with read/write/modify privileges)
- UCC-3: Watershed uploaders (write access to allocated watershed space)
- UCC-4: ARS users (authenticated access to watershed data)
- UCC-5: Research users (non-ARS researchers with similar needs)
- UCC-6: Public users (general public access to public data)

### 2.4 Operating Environment
- Web browsers: Microsoft Internet Explorer 5.0/6.0, Netscape 4.7/6/7, FireFox
- Certified and Accredited servers with corporate approved OS versions
- Corporate Intranet access with optional Internet access through firewall
- Public access to reviewed and approved datasets

### 2.5 Design and Implementation Constraints
- Platform independence on client side
- Microsoft SQL Server database engine
- Compliance with Accessibility, Web Design, and Security policies
- Annual data uploading frequency limiting interface complexity
- Database structure completeness with room for modification

## 3. System Features

### 3.1 Database Management System
Central component providing stable, secured, high-performance data storage and maintenance. Supports various data types including spatial data (vector, raster, imagery), tabular data (static and time-series), spreadsheets, documents, reports, photographs, and URL links.

### 3.2 Metadata Availability
Maintains metadata reports for each database using Federal Content Standard for Digital Geospatial Metadata (FGDC-STD-001-1998). Includes metadata input tools, query systems, and database for browse and query functionality.

### 3.3 Data Dissemination
Platform-independent web service for electronic data availability. Alternative media options for users with incompatible computing environments.

### 3.4 Hardware Requirements
- Online storage for hundreds of megabytes to gigabytes of data
- Week-nightly backups with secure off-site storage
- Load balanced application and database servers
- Private network environment for back-end operations
- Standard ARS OCIO hardware resources

### 3.5 Software Requirements
- Backup software solutions for data and applications
- HTTP and GIS server applications
- Commonly supported web browsers with restricted plug-in use
- Email server applications for alerts and information delivery
- Microsoft SQL Server as primary database management system
- Standardized data formats (tab-delimited text) for client system compatibility

### 3.6 Data Migration and Retrieval
Data subject to quality assurance before uploading. Initial population requires joint development of transition filters between STEWARDS team and individual watersheds. Annual updates use same filters.

#### 3.6.1 Quality Assurance
Local watershed staff perform QA/QC procedures before uploading. Two-level quality assurance: local site level and central site level. Primary responsibility for data quality assurance rests with individual sites.

#### 3.6.2 Populating Data
Basic watershed information reformatted to STEWARDS data schema and CEAP modeling requirements. Time-series data processed through local and CEAP QA/QC procedures.

#### 3.6.3 Updating Data
Annual data collection, processing through QA/QC procedures, and uploading using initial population filters. Compliance expected per CEAP watershed project plans.

#### 3.6.4 Data Derivation/Aggregation
Supports access to individual watershed data, sub-watershed data, or entire datasets. Multiple levels of time-series data aggregation (daily, monthly, yearly). Flexible data export in terms of volume and output formats.

## 4. External Interface Requirements

### 4.1 User Interfaces
Simple, consistent interface using commonly understood terminology. Thin-client architecture eliminating need for user training. User testing ensures clarity, completeness, and consistency.

### 4.2 Hardware Interfaces
Uses standard ARS OCIO hardware resources including Ethernet network/T1 connection, network servers, and management tools. Includes low transmission speed warnings and non-graphical interface options.

### 4.3 Software Interfaces
Uses standard ARS OCIO software resources including MS ASP/Java Scripts, C++/C#, MS SQL server and IIS, or PHP/Perl, JB scripts, MySQL server, and Apache server.

### 4.4 Communications Interfaces
Uses ARS OCIO communications resources including HTTP protocol for web browser/server communication and TCP/IP network protocol.

## 5. Other Nonfunctional Requirements

### 5.1 Performance Requirements
- No visible response time deterioration with increased users
- Metadata query response times of few seconds or less
- Data loading speed comparable to productivity tools

### 5.2 Safety Requirements
Server data protected from power loss. Data in transit losses monitored and uploading process repeated.

### 5.3 Security Requirements
Four primary components: authentication, confidentiality, integrity, and availability.
- Authentication using industry best practices and single-sign-on systems
- Confidentiality through user class boundaries and appropriate security features
- Data integrity through extensive validation and review processes
- 99% system availability (with 5% tolerance)

### 5.4 Software Quality Attributes
- Portability of query results between environments
- Adaptability for necessary changes in later phases
- System availability during intended operational period

## Appendix A: Acronyms
- AnnAGNPS: Annualized Agricultural Non-Point Source
- ARS: Agricultural Research Service
- CEAP: Conservation Effects Assessment Project
- DBA: Database Administrator
- ERS: Economics Research Service
- GIS: Geographical Information System
- NRCS: Natural Resources Conservation Service
- OCIO: Office of Chief Information Officer
- SWAT: Soil and Water Assessment Tool
- USDA: US Department of Agriculture
