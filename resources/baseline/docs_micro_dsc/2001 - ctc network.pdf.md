# Software Requirements Specification (SRS)
## Regional Traffic Management Integration Network (RTMIN)
### For the Dallas/Ft. Worth Metroplex

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft for Review

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Regional Traffic Management Integration Network (RTMIN). The primary purpose of this document is to provide a detailed description of the system to be developed, serving as a basis for agreement between stakeholders and as a guide for the development and quality assurance teams.

### 1.2 Scope
The RTMIN system will create a unified regional network for the Dallas/Ft. Worth metroplex. It will integrate disparate, agency-specific Traffic Management Systems (TMS) into a single, coherent data repository. The system will enable two-way communication: **ingesting** standardized traffic data from multiple sources and **providing** a centralized platform for situational awareness and remote device control. The scope includes the server-side application, data integration services, and a web-based client interface. It excludes modifications to existing agency TMS, field device hardware, and underlying network infrastructure.

### 1.3 Definitions, Acronyms, and Abbreviations
*   **ASN.1:** Abstract Syntax Notation One. A standard for describing data structures.
*   **DATEX:** Data Exchange specification for traffic information in Europe, used here with ASN.1 encoding.
*   **DFW:** Dallas/Ft. Worth metroplex.
*   **ITS:** Intelligent Transportation Systems.
*   **SRS:** Software Requirements Specification.
*   **TCP/IP:** Transmission Control Protocol/Internet Protocol.
*   **TMDD:** Traffic Management Data Dictionary. An ITS standard for defining traffic management data concepts.
*   **TMS:** Traffic Management System.
*   **RTMIN:** Regional Traffic Management Integration Network (the system described herein).

### 1.4 References
*   ITS Standards: Traffic Management Data Dictionary (TMDD), Version X.X
*   DATEX II ASN.1 Schema Specifications
*   Microsoft Windows NT 4.0 (or later) System Documentation

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its perspective, functions, and constraints. Section 3 details the specific requirements, including external interfaces, functional capabilities, and non-functional attributes.

## 2. Overall Description

### 2.1 Product Perspective
The RTMIN is a new, independent system that acts as a middleware layer and central hub. It interfaces with existing external agency TMS (as data publishers) and serves internal operators (as data consumers and command issuers). The system architecture is client-server, with a Windows NT server hosting the core application and a web-based client accessible via standard browsers.

### 2.2 Product Functions
The high-level functions of the RTMIN are:
1.  **Data Acquisition & Standardization:** Connect to multiple agency TMS, collect raw traffic data, and transform it into a TMDD-compliant, standardized format.
2.  **Data Repository Management:** Store standardized real-time and historical traffic data, including device statuses, traffic conditions, and incident reports.
3.  **Situational Awareness Visualization:** Present a consolidated, web-based geographical map displaying current traffic conditions, incident locations, and field device statuses.
4.  **Device Command & Control:** Provide authenticated operators with the ability to issue commands (e.g., change message sign text, adjust signal timing) to field devices via their respective agency TMS and monitor command status.
5.  **Data Distribution:** Share the consolidated, standardized data feed with authorized external systems (future capability).

### 2.3 User Characteristics
*   **Traffic Management Center (TMC) Operator:** Primary user. Skilled in traffic management concepts, uses the web interface for monitoring and control. Requires clear, reliable visualizations and intuitive control mechanisms.
*   **System Administrator:** Technical user responsible for configuring data source connections, managing user accounts, and monitoring system health. Requires robust administrative tools.
*   **External Agency System (Machine User):** Acts as a data publisher (sending data to RTMIN) and potentially a data subscriber (receiving commands from RTMIN). Communication is entirely via the DATEX/ASN over TCP/IP protocol.

### 2.4 Constraints
1.  **Regulatory/Standard Constraints:** The system **must** utilize the ITS Traffic Management Data Dictionary (TMDD) standard for its internal data model and external data representation.
2.  **Protocol Constraint:** All external system-to-system data transmission **must** use the DATEX data model encoded in ASN.1 over TCP/IP connections.
3.  **Hardware/Platform Constraint:** The core server application **must** be designed to execute in a Microsoft Windows NT 4.0 (or specified later) operating system environment.
4.  **Legacy System Constraint:** The system cannot require modifications to the existing agency TMS software; integration must be achieved through defined external interfaces.

### 2.5 Assumptions and Dependencies
*   **Assumption:** Participating agency TMS will be capable of establishing a TCP/IP connection and formatting data according to the agreed-upon DATEX/ASN profile.
*   **Assumption:** A stable network infrastructure with sufficient bandwidth exists between the central RTMIN server and all connected agency TMS.
*   **Dependency:** The project depends on the availability of complete and accurate TMDD and DATEX/ASN schema documentation.

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 User Interfaces
*   **UI-1:** A web-based, interactive geographical map shall be the primary user interface.
*   **UI-2:** The map shall display layers for traffic flow (color-coded segments), incidents (icons), and field devices (status-indicating icons).
*   **UI-3:** Clicking a device icon shall open a detailed status panel and, if permissions allow, a control panel for issuing commands.
*   **UI-4:** The interface shall include authentication via a login screen and role-based menu options.

#### 3.1.2 Hardware Interfaces
*   **HW-1:** The server shall run on commercial off-the-shelf (COTS) hardware compatible with Microsoft Windows NT.
*   **HW-2:** The system requires a persistent network connection to the agency TMS and to client workstations.

#### 3.1.3 Software Interfaces
*   **SI-1:** The server shall implement a TCP/IP socket listener to accept DATEX/ASN data streams from agency TMS.
*   **SI-2:** The server shall be capable of initiating TCP/IP connections to agency TMS for the purpose of sending device commands, as per the DATEX/ASN protocol.
*   **SI-3:** The internal application data model shall be fully compliant with the latest adopted version of the TMDD standard.

#### 3.1.4 Communications Interfaces
*   **CI-1:** All data exchange with external agency systems shall use the DATEX II data model, encoded using ASN.1 PER (Packed Encoding Rules) or UPER (Unaligned PER), transmitted over TCP/IP.
*   **CI-2:** The specific DATEX publication (e.g., `TrafficStatusPublication`) and subscription mechanisms shall be detailed in a separate Interface Control Document (ICD).

### 3.2 Functional Requirements

#### 3.2.1 Data Collection & Standardization Module
*   **FR-1:** The system shall connect to a minimum of 10 distinct agency TMS data feeds concurrently.
*   **FR-2:** The system shall ingest data packets in DATEX/ASN format from each connected feed.
*   **FR-3:** The system shall parse the ASN.1-encoded data, validate its structure against the defined DATEX schema, and map the incoming data elements to the internal TMDD-compliant data model.
*   **FR-4:** The system shall log all data reception errors and source connectivity status.

#### 3.2.2 Data Repository & Management Module
*   **FR-5:** The system shall store standardized real-time data in a structured, queryable database.
*   **FR-6:** The system shall maintain a historical archive of traffic conditions and device statuses for a configurable period (minimum 30 days).
*   **FR-7:** The system shall associate all data with its source agency and a timestamp.

#### 3.2.3 Web-Based Map & Visualization Module
*   **FR-8:** The web client shall display a map of the DFW metroplex using a standard tiled mapping library (e.g., OpenLayers, Leaflet).
*   **FR-9:** The system shall visually represent real-time traffic speed/flow on road segments using a standard color gradient (e.g., green/yellow/red/black).
*   **FR-10:** The system shall plot incident icons (e.g., crash, construction) and field device icons (e.g., dynamic message sign, traffic signal, camera) at their correct geographical coordinates.
*   **FR-11:** Device icons shall visually indicate their operational status (e.g., normal, fault, offline).

#### 3.2.4 Device Command & Control Module
*   **FR-12:** An authenticated operator with "Control" privileges shall be able to select a field device from the map and open a command dialog.
*   **FR-13:** The command dialog shall present control options specific to the device type (e.g., text entry for message signs, predefined plans for signals).
*   **FR-14:** Upon command submission, the system shall format the command into a TMDD-compliant action, then encode it into a DATEX/ASN `ControlRequest` message.
*   **FR-15:** The system shall route the `ControlRequest` message via TCP/IP to the appropriate agency TMS responsible for the target device.
*   **FR-16:** The system shall monitor for and display `ControlResponse` and `ControlStatus` messages from the agency TMS, updating the operator on the command's progress (e.g., "Sent," "Acknowledged," "Executed," "Failed").

### 3.3 Non-Functional Requirements

#### 3.3.1 Performance Requirements
*   **PER-1:** The system shall process and store incoming data updates from all feeds with a latency of less than 10 seconds from time of receipt to time of availability in the repository and on the map.
*   **PER-2:** The web-based map shall refresh incident and device status data automatically at an interval configurable between 10 and 60 seconds.
*   **PER-3:** The system shall support a minimum of 25 concurrent web client users without significant degradation of map responsiveness.

#### 3.3.2 Safety & Security Requirements
*   **SEC-1:** All user access shall require authentication (username/password).
*   **SEC-2:** The system shall implement role-based access control (RBAC) with at least three roles: Viewer, Operator, Administrator.
*   **SEC-3:** Only users with the "Operator" role or higher shall be permitted to issue device commands.
*   **SEC-4:** All commands issued shall be logged with the user ID, timestamp, device ID, command details, and final status.

#### 3.3.3 Reliability & Availability
*   **REL-1:** The core server application shall have a target availability of 99.5% during standard operating hours (05:00 - 23:00 local time).
*   **REL-2:** The system shall implement connection retry logic for failed links to agency TMS.

#### 3.3.4 Platform Compliance
*   **PLAT-1:** The server-side application shall be fully compatible with the Microsoft Windows NT 4.0 operating system and its standard system libraries.
*   **PLAT-2:** The web client shall be accessible from common web browsers (Internet Explorer 5.0+, Netscape Navigator 4.7+) without requiring browser plugins.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| Quality Assurance | | | |