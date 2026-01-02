# Software Requirements Specification (SRS)
## Regional Center-to-Center (C2C) Communications Network
### For the Dallas/Fort Worth Area

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft for Review

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Dallas/Fort Worth Regional Center-to-Center (C2C) Communications Network. This document is intended for use by the project stakeholders, including system architects, developers, testers, and the end-user agencies, to ensure a common understanding of the system to be developed.

### 1.2 Scope
The system is a regional communications network designed to facilitate interoperability between Traffic Management Centers (TMCs) and other transportation agencies in the Dallas/Fort Worth metropolitan area. The core purpose is to establish a standardized, shared repository for regional traffic data and to enable secure, remote command and control of Intelligent Transportation Systems (ITS) field devices across jurisdictional boundaries.

**In-Scope:**
*   Development of a central server application for data aggregation, storage, and distribution.
*   Implementation of standardized C2C communication interfaces for data exchange and device control.
*   Provision of a web-based client application for data visualization and device management.
*   Integration with existing agency TMC systems that comply with specified standards.
*   Management of roadway network data, traffic conditions, incidents, and lane closures.
*   Remote status monitoring and control of field devices (DMS, LCS, CCTV).

**Out-of-Scope:**
*   Development of field device hardware or firmware.
*   Modification of legacy agency systems that do not support the mandated standards.
*   Direct data collection from field sensors (assumes data is provided by connected TMCs).
*   Physical network infrastructure (assumes TCP/IP connectivity exists).

### 1.3 Definitions, Acronyms, and Abbreviations

| Term | Definition |
| :--- | :--- |
| **C2C** | Center-to-Center communications. |
| **TMC** | Traffic Management Center. |
| **ITS** | Intelligent Transportation Systems. |
| **TMDD** | Traffic Management Data Dictionary (ITS Standard). |
| **DATEX/ASN** | A standardized European data exchange profile for traffic information, using Abstract Syntax Notation (ASN.1) encoding. |
| **DMS** | Dynamic Message Sign. |
| **LCS** | Lane Control Signal. |
| **CCTV** | Closed-Circuit Television camera. |
| **TCP/IP** | Transmission Control Protocol/Internet Protocol. |

### 1.4 References
*   *Traffic Management Data Dictionary (TMDD)*, Version 3.0, USDOT.
*   *DATEX II* User Guide and ASN.1 Specifications.
*   *Microsoft Windows NT 4.0 Technical Specifications*.

### 1.5 Overview
The remainder of this SRS is structured as follows: Section 2 provides an overall description of the product, its users, and constraints. Section 3 details the specific functional and non-functional requirements.

## 2. Overall Description

### 2.1 Product Perspective
The C2C Network is a new, independent system that will act as a middleware hub between existing agency TMCs. It will not replace existing TMC software but will provide a standardized interface for data sharing and device control that agencies can connect to. The system architecture is client-server, with a central server managing communications and a web-based client providing the user interface.

### 2.2 Product Functions
The system shall provide three primary functions:
1.  **Data Repository & Exchange:** Collect, validate, store, and distribute standardized traffic data from participating agencies.
2.  **Device Management:** Transmit status information and forward command/control messages for ITS field devices between authorized centers.
3.  **Situational Awareness:** Present a consolidated, real-time graphical view of regional traffic conditions and incidents via a web-based map interface.

### 2.3 User Characteristics
| User Class | Expertise | Primary Interaction |
| :--- | :--- | :--- |
| **TMC Operator** | Proficient in traffic management concepts and local TMC software. Uses the system daily. | Uses web map to view regional conditions. May send device control requests (e.g., change DMS message). |
| **TMC System (Automated)** | Machine-to-machine interface. | Sends and receives standardized data and device status messages automatically. |
| **Agency Supervisor/Planner** | Understands traffic data but may not be an operator. | Accesses system for historical data review, reporting, and planning purposes. |
| **System Administrator** | IT professional with knowledge of Windows NT, networking, and application management. | Installs server software, manages user accounts, monitors system health, and performs backups. |

### 2.4 Constraints
1.  **Regulatory/Standards Constraints:** The system **must** implement communications compliant with the **Traffic Management Data Dictionary (TMDD)** and use **DATEX/ASN** message encoding for all C2C data exchanges over **TCP/IP**.
2.  **Hardware/Platform Constraints:** The central server application **must** be designed to operate within a **Microsoft Windows NT 4.0** (or later) operating environment.
3.  **Interoperability Constraint:** The system must be capable of interfacing with heterogeneous TMC systems, relying solely on the mandated standards for compatibility.

### 2.5 Assumptions and Dependencies
*   Participating agencies have TCP/IP network connectivity to the central server location.
*   Agency TMC systems will be upgraded or configured to generate and consume TMDD/DATEX messages as required.
*   The Windows NT platform will be maintained and secured by the hosting organization.

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 User Interfaces
*   **UI-1:** The system shall provide a web-based graphical user interface (GUI) accessible via a standard web browser (e.g., Internet Explorer 5.0+).
*   **UI-2:** The GUI shall be centered on an interactive map display of the Dallas/Fort Worth roadway network.
*   **UI-3:** The map shall provide pan, zoom, and layer control functions (e.g., toggle incidents, DMS locations, CCTV feeds, lane closures).

#### 3.1.2 Hardware Interfaces
*   **HW-1:** The server shall communicate with client workstations and remote TMC centers over standard Ethernet TCP/IP networks.

#### 3.1.3 Software Interfaces
*   **SI-1:** The C2C Server shall implement a TCP/IP socket interface for receiving and transmitting TMDD/DATEX/ASN messages.
*   **SI-2:** The system shall include a configuration module to define and manage connections to partner TMCs (IP address, port, agency ID, supported message types).

#### 3.1.4 Communications Interfaces
*   **CI-1:** All external C2C communications shall use the TMDD message framework.
*   **CI-2:** All external C2C message payloads shall be encoded per the DATEX/ASN.1 schema.
*   **CI-3:** Communications shall be over persistent or on-demand TCP/IP connections, as defined per partner agreement.

### 3.2 Functional Requirements

#### 3.2.1 Data Management Module
*   **F-DM-1:** The system shall receive and parse incoming TMDD messages (e.g., `trafficFlow`, `incident`, `laneClosure`) from connected TMCs.
*   **F-DM-2:** The system shall validate the structure and content of incoming messages against the TMDD/DATEX standard.
*   **F-DM-3:** The system shall store all validated data in a central, time-stamped database.
*   **F-DM-4:** The system shall distribute relevant data updates to all other connected TMCs authorized to receive that data type.
*   **F-DM-5:** The system shall provide a mechanism to query historical data by time range, location, and data type.

#### 3.2.2 Device Control Module
*   **F-DC-1:** The system shall receive and forward TMDD `deviceControlRequest` messages from an originating TMC to the TMC responsible for the target device.
*   **F-DC-2:** The system shall receive and forward corresponding `deviceStatus` messages from the controlling TMC back to the originating TMC and other authorized subscribers.
*   **F-DC-3:** The system shall maintain a registry of field devices (DMS, LCS, CCTV), mapping each device to its controlling TMC.
*   **F-DC-4:** The system shall not interpret or modify the payload of device control messages; it shall act as a trusted router.

#### 3.2.3 Web Client Module
*   **F-WC-1:** The web client shall display a map with real-time traffic conditions (e.g., color-coded speed, congestion).
*   **F-WC-2:** The web client shall display icons for incidents, lane closures, DMS locations, and CCTV locations.
*   **F-WC-3:** Selecting a CCTV icon shall launch a separate window or pane displaying the live video feed (provided by the source TMC).
*   **F-WC-4:** Selecting a DMS icon shall display its current message and status, and provide an interface for authorized users to submit a new message request.
*   **F-WC-5:** The client shall allow filtering of displayed information by type, severity, and jurisdiction.

### 3.3 Non-Functional Requirements

#### 3.3.1 Performance Requirements
*   **PER-1:** The system shall be capable of processing and distributing incident data from any TMC to all other TMCs with a latency of less than 10 seconds under normal load (95th percentile).
*   **PER-2:** The web map shall refresh displayed data automatically at a user-configurable interval (default 60 seconds) without requiring a full page reload.

#### 3.3.2 Safety & Security Requirements
*   **SEC-1:** The system shall require user authentication (username/password) for access to the web client.
*   **SEC-2:** The system shall implement role-based access control (RBAC) to define permissions (e.g., View-Only, Device-Control, System-Admin).
*   **SEC-3:** All C2C connections shall be authenticated at the center level using a pre-shared key or certificate mechanism.
*   **SEC-4:** The system shall log all device control requests, including originating user, time, target device, and request details.

#### 3.3.3 Reliability & Availability
*   **REL-1:** The central server shall have 99.5% uptime during core operational hours (5:00 AM - 10:00 PM, 7 days/week).
*   **REL-2:** The system shall implement data persistence such that no more than 5 minutes of data are lost in the event of an unexpected server restart.

#### 3.3.4 System Attributes
*   **SYS-1:** The system shall be designed for scalability to support up to 15 distinct TMC/agency connections.
*   **SYS-2:** The server software shall be installable on a standard Windows NT 4.0 server without requiring modifications to the base OS kernel.

---
*End of Document*