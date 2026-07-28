# Software Requirements Specification (SRS) for the Clarus System

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Clarus system. It is intended for use by the project stakeholders, including system architects, developers, testers, project managers, and end-user representatives, to ensure a common understanding of the system to be developed.

### 1.2 Scope
The Clarus system is a centralized data management platform designed to collect, perform quality assurance on, and disseminate surface transportation environmental data. This data includes atmospheric (e.g., air temperature, visibility), pavement (e.g., surface temperature, condition), and hydrologic (e.g., water level, precipitation) observations from sensor networks across North America. The system's primary goal is to enhance roadway safety, traffic mobility, and the accuracy of weather forecasting by providing qualified, reliable environmental data to authorized users and downstream service providers.

**In-Scope:**
*   Ingestion of data from heterogeneous, autonomous sensor networks and third-party contributors.
*   Implementation of automated and human-in-the-loop data quality checking (QC) processes.
*   Secure storage of raw and quality-checked data and associated metadata.
*   Controlled dissemination of data based on configurable sharing agreements.
*   A 24x7 operational capability with high availability.
*   An open, standards-based architecture for interfaces and data formats.

**Out-of-Scope:**
*   The physical environmental sensor units themselves.
*   The development of consumer-facing weather or traffic applications by end-users.
*   Direct control or actuation of field devices (e.g., road signs, barriers).

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **Clarus** | The name of the surface transportation environmental data system. |
| **ESN** | Environmental Sensor Network. A collection of field sensors. |
| **QC** | Quality Check / Quality Control. The process of validating and qualifying data. |
| **NTCIP 1204** | National Transportation Communications for ITS Protocol - Environmental Sensor Station (ESS) Interface Standard. |
| **Metadata** | Data describing the source, location, timing, and characteristics of the environmental observations. |
| **Data Sharing Agreement** | A rule set defining which users or systems are authorized to receive specific data streams. |

### 1.4 References
*   NTCIP 1204 v03.15: Standard on Environmental Sensor Station (ESS) Interface
*   Project Charter: Clarus System Initiative
*   Data Sharing Agreement Framework Document

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a high-level description of the product and its operating environment. Section 3 details specific system requirements, including external interfaces, functional capabilities, and non-functional attributes.

## 2. Overall Description

### 2.1 Product Perspective
Clarus is a standalone, server-based system that acts as a middleware data broker between data producers (sensor networks) and data consumers (service providers, analysts). It is independent of specific sensor hardware but must interface with a wide variety of data collection systems. The system must integrate with existing authentication/authorization infrastructure.

### 2.2 Product Functions
The core high-level functions of the Clarus system are:
1.  **Data Collection:** Reliably ingest environmental data feeds from diverse, geographically dispersed sources using standard and proprietary protocols.
2.  **Data Quality Assurance:** Apply a configurable suite of automated QC algorithms (e.g., range checks, rate-of-change checks, spatial consistency checks) and provide a user interface for manual QC by trained analysts.
3.  **Data Management & Storage:** Securely store all incoming data, QC flags, metadata, and user activity logs in a persistent, auditable repository.
4.  **Data Dissemination:** Distribute qualified data and metadata to authorized external systems and users according to enforceable data sharing agreements.
5.  **System Administration:** Provide tools for managing users, data sources, sharing agreements, QC parameters, and monitoring system health.

### 2.3 User Characteristics
| User Class | Description | Technical Expertise |
| :--- | :--- | :--- |
| **System Administrator** | Manages system configuration, user accounts, and overall health. | High. Expert in system operations. |
| **Data Quality Analyst** | Reviews automated QC flags, performs manual data validation and correction. | Medium-High. Understands meteorology/data science. |
| **Data Consumer (Machine)** | External system (e.g., weather model, traveler info system) that receives data via API. | N/A (System-to-System) |
| **Data Consumer (Human)** | Researcher or operator who queries and retrieves data via a web interface. | Medium. Proficient in data retrieval tools. |
| **Data Provider** | External entity that configures and manages the feed of their sensor data into Clarus. | Medium. Understands data transmission protocols. |

### 2.4 Constraints
1.  **Legal/Contractual:** Data dissemination **must be strictly controlled** by source-specific data sharing agreements. The system must enforce these agreements programmatically.
2.  **Operational:** The system **must operate continuously (24 hours a day, 7 days a week)** with minimal planned downtime. High availability and disaster recovery provisions are required.
3.  **Architectural:** The system architecture **must be open and standards-based**. Interfaces for data collection and dissemination should prioritize industry standards such as **NTCIP 1204** and other relevant OGC (Open Geospatial Consortium) standards where applicable.
4.  **Regulatory:** The system must comply with relevant data security and privacy regulations applicable to government-held transportation data.

### 2.5 Assumptions and Dependencies
*   **Assumption:** Data providers will have the capability to transmit data to a designated Clarus ingestion endpoint using a documented protocol.
*   **Assumption:** A separate enterprise user directory (e.g., LDAP) will be available for user authentication integration.
*   **Dependency:** The system's ability to disseminate data in specific formats is dependent on the adoption of those formats by the consumer community.

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 User Interfaces
*   **UI-1:** A secure, role-based web portal shall provide functionalities for data quality analysts, data consumers (human), and administrators.
*   **UI-2:** The portal shall include dashboard views for system status, data feed health, and QC workload.
*   **UI-3:** All data displays (tables, maps, time-series graphs) shall clearly indicate the applied QC flags.

#### 3.1.2 Hardware Interfaces
*   **HW-1:** The system shall be deployable on standard commercial off-the-shelf (COTS) server hardware in a data center environment.

#### 3.1.3 Software Interfaces
*   **SI-1:** The system shall implement an **NTCIP 1204-compliant** server interface to collect data from compatible Environmental Sensor Stations (ESS).
*   **SI-2:** The system shall support ingestion via **HTTPS POST** with JSON/XML payloads for non-NTCIP data providers.
*   **SI-3:** The system shall provide a **RESTful API** over HTTPS for authorized data dissemination to machine consumers.
*   **SI-4:** The system shall integrate with the enterprise **LDAP/Active Directory** service for user authentication.

#### 3.1.4 Communications Interfaces
*   **CI-1:** All external communications (data ingestion, dissemination, user access) shall use encrypted channels (TLS 1.2 or higher).

### 3.2 Functional Requirements

#### 3.2.1 Data Collection (DC)
*   **DC-FR1:** The system shall accept and parse real-time and batch data feeds from registered sensor networks.
*   **DC-FR2:** The system shall support a minimum of three (3) concurrent standard data formats/protocols (including NTCIP 1204) at launch.
*   **DC-FR3:** The system shall generate an acknowledgment receipt for each successfully ingested data message.
*   **DC-FR4:** The system shall log all ingestion attempts, including failures with diagnostic information.

#### 3.2.2 Data Quality Checking (QC)
*   **QC-FR1:** The system shall apply a configurable set of automated QC tests to each incoming observation (e.g., plausible value range, step change detection).
*   **QC-FR2:** The system shall assign a discrete QC flag (e.g., "Passed", "Failed", "Suspect", "Corrected") to each observation based on automated tests.
*   **QC-FR3:** The system shall present observations that fail automated tests in a dedicated work queue for manual review by a Data Quality Analyst.
*   **QC-FR4:** An analyst shall be able to override an automated QC flag and assign a manual flag, providing a text reason for the override.
*   **QC-FR5:** All QC flags (automated and manual) shall be stored immutably as part of the observation's permanent record.

#### 3.2.3 Data Dissemination (DD)
*   **DD-FR1:** The system shall evaluate each data dissemination request against the active Data Sharing Agreements associated with the requested data source(s).
*   **DD-FR2:** The system shall only disseminate data to users or systems authorized by the relevant sharing agreement(s).
*   **DD-FR3:** The dissemination API shall allow filtering of data by: geographic region, sensor type, parameter, time range, and QC flag status.
*   **DD-FR4:** The system shall disseminate both the environmental observation value and its associated QC flag and metadata (sensor ID, location, timestamp).

#### 3.2.4 System Administration (SA)
*   **SA-FR1:** An administrator shall be able to create, modify, and deactivate user accounts and assign roles/permissions.
*   **SA-FR2:** An administrator shall be able to configure and activate new Data Sharing Agreements, specifying data sources and authorized consumers.
*   **SA-FR3:** An administrator shall be able to configure parameters for the automated QC algorithms (e.g., set threshold values).

### 3.3 Non-Functional Requirements

#### 3.3.1 Performance Requirements
*   **PER-1:** The system shall ingest 95% of incoming real-time data messages with an end-to-end latency of less than 60 seconds from time of sensor observation to time of storage.
*   **PER-2:** The system shall process and respond to 95% of data dissemination API queries within 5 seconds under normal load.
*   **PER-3:** The system shall be designed to handle a peak load of 10,000 sensor stations reporting at 5-minute intervals.

#### 3.3.2 Safety Requirements
*   *Not directly applicable to this software system. Safety is impacted by the *use* of the data, not its collection/management.*

#### 3.3.3 Security Requirements
*   **SEC-1:** All access to the system's web portal and APIs shall require authentication.
*   **SEC-2:** The system shall implement role-based access control (RBAC) to enforce functional permissions.
*   **SEC-3:** The system shall audit and log all data access (queries, downloads) and all modifications to QC flags, sharing agreements, and system configuration.
*   **SEC-4:** Data at rest in the system's databases shall be encrypted.

#### 3.3.4 Software Quality Attributes
*   **AVAIL-1:** The system shall achieve 99.5% operational availability in any calendar month, excluding scheduled maintenance windows.
*   **REL-1:** The system shall have a mean time between critical failures (MTBCF) of not less than 720 hours.
*   **MAIN-1:** The system shall be designed to allow for the addition of new data formats and QC algorithms with minimal changes to the core system architecture (Modifiability).
*   **USAB-1:** The manual QC interface shall allow an analyst to review and flag a minimum of 50 observations per hour.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead System Architect | | | |
| Quality Assurance Manager | | | |