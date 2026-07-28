# Software Requirements Specification (SRS)
## Dallas/Ft. Worth Regional Center-to-Center Communications Network (DFW C2C)

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Dallas/Ft. Worth Regional Center-to-Center Communications Network (DFW C2C). The intended audience includes project stakeholders, system architects, software developers, testers, and the operations teams of participating Traffic Management Centers (TMCs).

#### 1.2 Scope
The DFW C2C system will establish a common, standardized repository for regional traffic information and enable the secure exchange of device control commands between multiple, dissimilar Traffic Management Centers (TMCs) operated by different agencies (e.g., TxDOT, city municipalities) within the DFW metroplex.

**In-Scope:**
*   Development of a central data hub/server that collects, standardizes, stores, and distributes traffic data.
*   Implementation of standardized communication protocols for interfacing with existing TMC backend systems.
*   Provision of a web-based graphical map for displaying a consolidated regional traffic picture.
*   Provision of client applications for incident/lane closure management and remote device control.
*   Routing of device status and control commands between interconnected TMCs.

**Out-of-Scope:**
*   Direct interface with field devices (e.g., Dynamic Message Signs, CCTV cameras). Communication with field devices remains the responsibility of the individual, legacy TMC systems.
*   Modification of existing TMC backend systems, beyond enabling communication via the defined project protocol.
*   Provision of real-time traffic data to the general public beyond the defined web map display.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **C2C** | Center-to-Center Communications |
| **TMC** | Traffic Management Center |
| **TMDD** | Traffic Management Data Dictionary (ITS Standard) |
| **DATEX/ASN** | Data Exchange/Abstract Syntax Notation (ITS Standard) |
| **DMS** | Dynamic Message Sign |
| **LCS** | Lane Control Signal |
| **CCTV** | Closed-Circuit Television |
| **TxDOT** | Texas Department of Transportation |
| **GUI** | Graphical User Interface |
| **DFW** | Dallas/Fort Worth |

#### 1.4 References
*   ITS Standards: Traffic Management Data Dictionary (TMDD)
*   ITS Standards: DATEX/ASN over TCP/IP
*   Project Charter: DFW Regional C2C Network Initiative

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its functions, and its operating environment. Section 3 specifies the detailed functional and non-functional requirements. Appendices may contain supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
The DFW C2C system is a middleware application that acts as a data hub and command router. It extends a foundational TxDOT C2C project to interconnect multiple, independent agency TMCs. The system sits logically between these existing centers, facilitating interoperability without requiring wholesale replacement of legacy systems.

**System Interfaces:**
*   **Backend TMC Systems:** The primary external interface. The C2C server will connect to each participating TMC's backend system to receive data and forward commands using a standardized protocol.
*   **Web Clients:** Public and authorized users will access the regional traffic map via a standard web browser (HTTP/HTTPS).
*   **Standalone Client Applications:** Authorized operators will use dedicated GUI applications for incident management and remote device control, connecting to the C2C server over a network.

#### 2.2 Product Functions
The core functions of the DFW C2C system are:
1.  **Data Aggregation & Storage:** Collect, translate (if necessary), and store standardized traffic data from multiple, heterogeneous TMC systems into a common regional repository.
2.  **Device Status Distribution:** Receive status data for various field devices (DMS, LCS, CCTV, ramp meters, traffic signals) from owning TMCs and distribute this data to other authorized TMCs.
3.  **Cross-Jurisdictional Device Control:** Receive device control commands from an operator at one TMC, validate authority, and route the command to the TMC system that owns the target device for execution.
4.  **Regional Situation Display:** Serve a web-based graphical map that visually integrates and displays regional traffic conditions, incident data, and device locations from all connected centers.
5.  **Incident & Lane Closure Management:** Provide a dedicated GUI tool for agency personnel to manually input, update, and manage incident and lane closure information within the common repository.
6.  **Remote Command Interface:** Provide a secure, standalone GUI for authorized operators to issue control commands for field devices across the region.

#### 2.3 User Characteristics
| User Class | Description | Key Skills/Knowledge |
| :--- | :--- | :--- |
| **TMC Operator** | Primary user at each agency center. Monitors traffic, responds to incidents, controls devices. | Proficient in traffic management concepts and native TMC software. Basic computer literacy. |
| **TMC Supervisor/Manager** | Oversees operations, coordinates multi-agency responses. | Deep understanding of regional traffic networks and inter-agency protocols. |
| **System Administrator** | Installs, configures, and maintains the C2C server and client software. | Strong IT network and Windows NT system administration skills. |
| **Public User** | Views traffic conditions via the public web map. | General web browsing skills. No special training required. |

#### 2.4 Constraints
*   **Software:** The system shall utilize ESRI's ARC Internet Map Server and Map Objects for all mapping and geospatial visualization components.
*   **Platform:** Server components must execute in a Microsoft Windows NT operating environment.
*   **Standards:** All data transmission between the C2C system and TMC backend systems shall comply with the ITS TMDD standard and utilize DATEX/ASN encoding over TCP/IP.
*   **Architecture:** The system cannot mandate changes to the internal database or logic of existing TMC systems.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** Each connected TMC will provide a stable, continuous data feed in either the project-defined protocol (based on TMDD/DATEX) or a legacy format with a known translation path.
*   **Assumption:** Participating agencies have established legal and operational agreements governing the sharing of data and cross-jurisdictional control of devices.
*   **Dependency:** The system's functionality is dependent on the reliability and availability of the network connections between the C2C hub and each TMC.
*   **Dependency:** Successful implementation depends on the cooperation of each agency's technical staff to establish and maintain the interface connections.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Data Hub Services
*   **FR-1:** The system shall collect traffic data (including roadway network definitions, traffic conditions, and incident reports) from each connected TMC backend system at intervals defined per agency agreement.
*   **FR-2:** The system shall translate incoming data from legacy TMC formats into the standard TMDD/DATEX format for storage in the common repository.
*   **FR-3:** The system shall store all standardized data in a persistent regional repository with configurable data retention policies.
*   **FR-4:** The system shall distribute updated device status information (for DMS, LCS, CCTV, ramp meters, signals) from the owning TMC to all other subscribed TMCs within 30 seconds of receipt.

##### 3.1.2 Device Control Routing
*   **FR-5:** The system shall receive a device control command from an authenticated user via the Remote Control GUI.
*   **FR-6:** The system shall validate the user's authorization to control the target device based on pre-configured agency permissions.
*   **FR-7:** If authorized, the system shall route the command to the backend system of the TMC that owns the target device.
*   **FR-8:** The system shall provide a confirmation (or error) message back to the originating user indicating the command's dispatch status.

##### 3.1.3 Web-Based Map Application
*   **FR-9:** The system shall provide a public-facing website displaying a graphical map of the DFW regional roadway network.
*   **FR-10:** The map shall display near-real-time traffic conditions (e.g., congestion levels, speeds) color-coded on roadway segments.
*   **FR-11:** The map shall display incident icons and lane closure information with relevant details available on click/hover.
*   **FR-12:** The map shall display the locations and status (e.g., on, off, fault) of key field devices (DMS, CCTV, etc.).

##### 3.1.4 Client Applications
*   **FR-13:** **Incident Management GUI:** The system shall provide a standalone application allowing authorized users to manually create, update, resolve, and delete incident and lane closure records in the common repository.
*   **FR-14:** **Remote Control GUI:** The system shall provide a secure standalone application that allows authenticated operators to select a remote field device (e.g., DMS), formulate a valid command (e.g., load a message), and issue that command via the C2C hub.

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance
*   **NFR-1:** The data hub shall be capable of processing and storing data feeds from up to 10 distinct TMC systems simultaneously.
*   **NFR-2:** The time from a device status change at a source TMC to its availability in the common repository shall be less than 60 seconds (latency).
*   **NFR-3:** The web map shall refresh displayed traffic condition data at a minimum interval of 5 minutes.

##### 3.2.2 Reliability & Availability
*   **NFR-4:** The C2C server system shall achieve 99.5% operational availability during core business hours (6:00 AM - 8:00 PM, Central Time).
*   **NFR-5:** The system shall implement data persistence and recovery mechanisms to prevent loss of repository data in the event of a service restart.

##### 3.2.3 Security
*   **NFR-6:** All data transmissions between the C2C hub and TMC backend systems shall occur over secure, dedicated network connections or encrypted VPN tunnels.
*   **NFR-7:** The Remote Control GUI shall require strong user authentication (username/password) and all control commands shall be logged for audit purposes.
*   **NFR-8:** Access to the Incident Management GUI shall be restricted based on user roles and agency affiliation.

##### 3.2.4 Compliance & Standards
*   **NFR-9:** The system's external data exchange interfaces **shall** fully comply with the ITS Traffic Management Data Dictionary (TMDD) standard, version as specified in the project interface control documents.
*   **NFR-10:** The encoding and transmission of all C2C data **shall** use the DATEX/ASN standard over TCP/IP.
*   **NFR-11:** Server components **shall** be designed to execute within a Microsoft Windows NT 4.0 (or compatible) operating environment.

#### 3.3 System Attributes

##### 3.3.1 Interoperability
The system's primary purpose is to achieve interoperability between disparate TMC systems. Success is measured by the accurate and timely exchange of data and commands as specified in FR-1 through FR-8.

##### 3.3.2 Scalability
The system architecture shall allow for the addition of new TMC agency connections with minimal disruption to existing services.

### 4. Acceptance Criteria
The system will be considered acceptable upon successful completion of the following validation tests:

1.  **Data Flow Verification:** Demonstrate that standardized traffic data (network, conditions, incidents) flows correctly from at least two dissimilar test TMC systems into the common repository and is accurately stored.
2.  **Device Status Sharing:** Demonstrate that a change in the status of a device (e.g., a DMS going to "fault") in one test TMC system is correctly received and displayed within the system of a second, connected test TMC within the specified latency period.
3.  **Web Map Integration:** Verify that the integrated data from multiple test sources is correctly displayed on the web-based graphical map, including traffic conditions, incidents, and device locations.
4.  **Remote Command Execution:** Demonstrate that an authorized user using the Remote Control GUI can successfully issue a command (e.g., "Blank Sign") for a device owned by a different test TMC, and that the command is properly routed, received, and executed by the target TMC's backend system, with appropriate confirmation returned to the user.

---
*Document End*