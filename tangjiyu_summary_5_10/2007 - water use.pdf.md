# Water Use Tracking (WUT) System Software Requirements Specification

## 1. Introduction

### 1.1 Purpose
The Software Requirements Specification (SRS) documents all requirements for the Water Use Tracking (WUT) System. It details user needs, goals, objectives, and features of the system, serving as a basis for communication between developers and stakeholders, and as input to software testing and quality assurance checks.

### 1.2 Overview
The WUT System's SRS packages artifacts developed during the Implementation Phase, including:
- Vision Document
- Requirements Workshops Summaries
- Requirement Traceability Matrix
- Use Case Model and Use Cases
- Supplementary Specification

This document outlines the process followed to gather requirements and describes how stakeholder requirements make their way into use case documents and system features.

## 2. Project Scope

### 2.1 Problem Statement
The Southern Water Use Caution Area (SWUCA) Management Plan has no current automated way to validate or assess rule implementation. No formal system exists to comprehensively track and analyze geographic and temporal trends in permitted and actual water uses within the SWUCA. Current tracking uses manual and semi-automated methodologies by different groups, leading to inconsistent results. Database management systems were not designed to support these analyses.

### 2.2 Product Position Statement
The WUT Project provides software for several customer types supporting Southwest Florida Water Management District's (SWFWMD) activities defined in the SWUCA Management Plan and to validate SWUCA II Rules. Primary user groups include:
- Water Use Permit (WUP) Evaluators: Assist in WUP review process
- Technical Services Staff: Track and analyze long-term trends in permitted and actual water use
- Records and Data Staff: Quality control/quality assurance of WUP data
- Resource Conservation and Development Department: Calibration of groundwater models and MFL information
- Planning Department: Studies analyzing impacts of changing demographics and economic conditions
- Executive Staff/Governing Board: Standard reports published as hardcopy or web-accessible documents
- External Customers: Local governments, media, and general public with standard interactive map interfaces

### 2.3 Stakeholder Summary
Stakeholders include Executive Sponsors, Co-Sponsors, Science Business Experts, Regulatory Business Experts, Technical Experts, and Other Impacted Parties from various departments within SWFWMD.

### 2.4 Project Environment
The system operates within existing hardware/software infrastructure:
- IBM DB2 Data Server: Upgraded in January 2003 with sufficient capacity
- HP-UX ArcSDE/Oracle Data Server: Replacement system with sufficient capacity
- Communications/Data Network: Data transfer occurs during non-business hours
- Web/ArcIMS Servers: Expanded to support CWM activities
- Desktop Workstations: Operate within ArcGIS ArcView and ArcIMS web browser environment

### 2.5 Product Perspective
The system requires integration of permitting, geographic, and water resource data from:
- Water Use Permit (WUP) Data: From Regulatory Database (RDB) in IBM DB2 environment
- Geographic Data: From GIS in ArcSDE/Oracle environment
- Water Resource Data: From Water Management Database (WMDB) in IBM DB2 environment
- Data Integration: Using Universal ID (UID) as common identifier linking data across systems

### 2.6 Assumptions and Dependencies
- Needed data changes will be made within current applications and databases
- Current databases remain available during WUT System development
- System developed with current hardware and software architecture at the District
- Changes to current architecture could cause delays in system release

### 2.7 Needs
Key needs include:
- Depict geographic and temporal trends in permitted and/or actual pumpage within SWUCA
- "Cradle to grave" tracking and analysis of individual ground and surface water withdrawal points
- Identification of sources for withdrawal points (surface versus ground, aquifer, status, alternative sources)
- Monitoring changes in permitted and actual pumping
- Tracking changes in predominant use types and permit ownership
- Identifying withdrawal points with lapsed permitted quantities
- Aggregate permitted pumpage, actual use, and lapsed quantities for defined geographic areas
- Analyze impacts of alternative supplies on pumpage in particular geographic areas

### 2.8 Other Product Requirements
System developed within current software development environment:
- WMDB, RDB: JCL, SQL, J2EE, COBOL
- SDE/Oracle: PL/SQL, Visual Studio .NET, ArcObjects
- ArcIMS: Visual Studio .NET, ArcIMS ArcObjects
- ArcGIS ArcView: Visual Studio .NET, SQL, ArcObjects

## 3. Requirements Gathering Process

### 3.1 Requirement Workshops and Summaries
Requirement workshops held for Executive Staff, Technical Staff, Science Business Staff, and Regulatory Staff with follow-up interviews. Additional workshop outlined requirements for SWUCA Recovery Plan support.

### 3.2 Requirements Traceability Matrix (RTM)
The WUT RTM documents and manages business and functional requirements organized into meaningful features. Each requirement maps to one or more use cases ensuring all requirements are supported by the WUT software system. RTM enables project scoping by prioritizing features/requirements across system releases.

### 3.3 Use Case Model and Use Cases
Use case model sets functional requirements on the system and serves as essential input to analysis and architectural design. It's a contract between development team and stakeholders regarding system functionality. The WUT Use Case Model consists of two packages:
- Maintain Water Use Tracking Information
- View Water Use Permit Information

### 3.4 Supplementary Specification
Non-functional requirements not readily traceable to specific use cases but critical to project success:
- Qualitative requirements: Usability, Reliability, Performance, Supportability, Performance Measures
- General systems requirements: Security, RDBMS, Backup/Recovery, User Documentation and Training

## 4. WUT Requirements

### 4.1 WUT Requirements Traceability Matrix
Organized into two sections:
- Requirements for Initial Release of WUT System
- Requirements for Possible Subsequent Release of WUT System

Requirements organized into features with matrix columns:
- Req ID: Unique identifier for each requirement
- Requirement Statement: Individual WUT business and functional requirements expressed with "shall," "will," or "must"
- Use Case: Unique name identifying WUT Use Case supporting the requirement

### 4.2 WUT Use Case Model
Created and maintained within Enterprise Architect modeling software. Over forty actors identified and consolidated into general categories. Since most of WUT System is reporting-based, all actors can run reports, view maps, and query water use permits.

#### 4.2.1 Actors
All actors have ability to run reports, view maps, and query water use permits. Only select users can edit data (WUT Administrator, Water Use Estimator).

#### 4.2.2 Use Cases
Critical and architecturally significant use cases for initial release:
- Process Database Replication
- Process WUT System Startup
- View Map
- View Report
- View Water Use Permit
- View Water Use Permit Search

##### 4.2.2.1 Process WUT System Startup
Access browser-based, distributed 3-tier client/server application deployed on SWFWMD's Intranet. Startup page displays information and provides access to system features. Role-based security determines features available to each actor.

##### 4.2.2.2 Generate Well Package
Generate comma-delimited well package file for import into Groundwater Vistas to model impact of well/withdrawal changes. Contains location information and attributes regarding water withdrawal wells within District.

##### 4.2.2.3 Maintain Business Rule Parameters
Update business rule parameters used in system calculations. Parameters not used to change original database information but create "derived" data for reports/screens.

##### 4.2.2.4 Maintain Quick Links
Manage quick links on WUT Home Page to other helpful websites. Links to other water district websites for viewing water use permit information near District boundaries.

##### 4.2.2.5 Maintain Water Use Estimates
Maintain water use estimation values for water use permits. Import water use estimate data for each permit into database table for system use, allowing users to view pumpage data as estimated values.

##### 4.2.2.6 Maintain WUT News
Maintain WUT news items for communication to users accessing WUT Home Page. System administrator can create maintenance news items for display during specified dates.

##### 4.2.2.7 Process Database Replication
Replicate and normalize data copied from DB2 database to read-only Oracle database. Data restructured to take advantage of relational database management system strengths. Nightly updates made with changed data since previous replication.

##### 4.2.2.8 View Change in Use Type or Owner
View information about relocation of permitted quantities associated with specific water use permit. When application relocates permitted quantities with change in use type or owner impacting MFL waterbody below minimum level, subject to certain criteria.

##### 4.2.2.9 View Compliance Information
View Compliance data associated with specific water use permit. Compliance data includes pumpage quantities, meter readings, crop reports, well construction specifications, and other condition data.

##### 4.2.2.10 View Crop Report Information
View crop report data associated with specific permit. Crop report data collected annually/semi-annually including crop/use type, acreage, predominant soil type, and planting dates.

##### 4.2.2.11 View Land Use Information
View land use data associated with specific water use permit. Land use data collected during permit submission or as permit conditions, and from map analysis.

##### 4.2.2.12 View Lapsed or Project Quantities Summary
View lapsed or project quantities data associated with specific water use permit. Track quantities with implementation of new SWUCA rules.

##### 4.2.2.13 View Map
View water use permit information spatially using GIS functionality. Provides multi-dimensional presentation of information for richer analysis.

##### 4.2.2.14 View Mitigation of MFL Impacts
View information on how specific water use permit mitigated impact on MFL waterbody. Applicant demonstrates compliance with all conditions except MFL waterbody impact can apply for permit with Net Benefit.

##### 4.2.2.15 View Net Benefit Summary
Analyze Net Benefit data associated with specific water use permit. Track Net Benefits with implementation of new SWUCA rules. Net Benefit obtained when proposed withdrawal with other activities results in improvement to MFL waterbody.

##### 4.2.2.16 View Report
Produce report from WUT Report Library. System has large number of reports available with actor capability to limit information to specific area of interest.

##### 4.2.2.17 View Resource Information
View water resource data associated with specific water use permit. Water resource data includes water quality data, water flows/levels, total dissolved mineral levels, and rainfall amounts.

##### 4.2.2.18 View Use of Lapsed Quantities
View use of lapsed quantities associated with specific water use permit. Track historically used, reasonable beneficial quantities potentially available from reduced, abandoned, or retired permits.

##### 4.2.2.19 View Use of Quantities Associated With District Projects
View quantities used from District Source Augmentation Projects associated with specific water use permit. Applicant can apply for source augmentation through District water resource development project.

##### 4.2.2.20 View Water Use Permit
View information about specific water use permit. Water use permit required when total capacity ≥1 million gallons/day, total annual average quantities ≥100,000 gallons/day, well diameter ≥6 inches, surface water withdrawal pipe diameters ≥4 inches, cumulative well diameters ≥6 inches in MIA, or withdrawal likely to cause significant adverse impacts.

##### 4.2.2.21 View Water Use Permit Search
Search for and identify water use permit for analysis. Enables actor to efficiently search for and identify permits meeting given search criteria.

##### 4.2.2.22 View Water Withdrawal Credit
View water withdrawal credit information associated with specific water use permit. Water withdrawal credit incentivizes applicant to provide alternative supplies to other water use permit holders.

##### 4.2.2.23 View Well Construction Information
View well construction information associated with specific water use permit. Well construction information gathered during construction and permitting including well depth, casing depth, well diameter, status code, drilling method, and completion date.

##### 4.2.2.24 View Withdrawal Pumpage Information
View withdrawal pumpage information associated with specific water use permit. Pumpage data collected at certain wells and estimated for others based on water and land use categories.

### 4.3 WUT Supplementary Specification
Organizes non-functional requirements into qualitative categories:
- Usability
- Reliability
- Performance
- Supportability

#### 4.3.1 Usability
Ease with which user can learn to operate, prepare inputs for, and interpret outputs of system.
- Quick access to currently published information for decision-making
- Daily replication of DB2 data in Oracle
- Consistency in decision-making among various users
- User-friendly system
- Customizable queries
- Real-time data availability
- Clear documentation for defensibility when permits denied/modified
- Wizards to help users perform tasks
- Decision tree for help desk personnel
- Clear hours of availability established
- Flexibility to handle different scenarios ("what-if" questions)
- On-line help and training
- Training material for in-house training
- Save/download query results to outside system
- Metadata management (FGDC compliant)

#### 4.3.2 Reliability
Ability of system to perform required functions under stated conditions for specified period.
- Update interval protocols for different data types
- Populate missing data in database (permits and pumpage reports)
- Consistent and reliable query results over time
- Better tools to access data than currently available
- Accurate data

#### 4.3.3 Performance
Degree to which device or system fulfills specifications.
- Application fits into statutory time frames for evaluating permitting applications with quick turn-around time
- Reasonable refresh rates
- Established response rates for web page

#### 4.3.4 Supportability
Ability of system to be supported by resources required for specific maintenance tasks.
- Data to support requirements exists in database and readily available
- Compilable versions of code stored in SourceSafe
- Do not use SDE log files
- Consistent naming and terminology conventions
- Web application preferred (if ArcMap, must run in Citrix ArcView)
- Toolbars written in .dll format
- Ease of deployment consideration
- Can extend current District architecture (Oracle Spatial if needed)
- Technical documentation for maintainability
- Follow District change management standards
- Do not join features based on shape column
- System written in map.net (VB or C#)
- Follow District programming standards
