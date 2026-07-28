# Software Requirements Specification (SRS)
## Dallas/Ft. Worth Regional Center-to-Center (C2C) Communications Network

**Document Version:** 1.0
**Date:** October 26, 2023
**Status:** Draft for Review
**Prepared for:** North Central Texas Council of Governments (NCTCOG) / Software Task Force
**Prepared by:** Southwest Research Institute (SwRI)

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Dallas/Ft. Worth Regional Center-to-Center (C2C) Communications Network. It serves as a formal agreement between the project sponsor (NCTCOG), stakeholders, and the system developer (SwRI) regarding the capabilities, constraints, and quality attributes of the software system to be delivered.

#### 1.2 Scope
This project will develop a software system to integrate disparate traffic management systems across the Dallas/Ft. Worth region. The system will establish a common data repository, enable cross-agency command and control of Intelligent Transportation Systems (ITS) field devices, and provide public-facing traffic information—all based on national ITS standards to ensure interoperability and future extensibility.

**In-Scope Elements:**
*   Development of standardized interfaces for exchanging roadway network, traffic condition, incident, and lane closure data.
*   Software modules for status monitoring and remote control of ITS field devices (Dynamic Message Signs, CCTV cameras, ramp meters, etc.).
*   A public, web-based graphical map displaying real-time traffic conditions and incidents.
*   A Windows desktop application for non-TMC agencies to input incident and lane closure data.
*   Implementation of communications using ITS standards (TMDD, DATEX/ASN) over TCP/IP.

**Out-of-Scope Elements:**
*   Detailed design of internal data structures or processing algorithms within partner agencies' legacy systems.
*   Network architecture, firewall configuration, or VPN setup for the Remote Control GUI.
*   Support for device-specific commands not ratified by all participating centers.
*   Resolution of data model inconsistencies between independently managed roadway and transit networks.
*   Justification for requirements considered self-evident.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **ARC IMS:** ESRI's ARC Internet Map Server
*   **ASN.1:** Abstract Syntax Notation One (Data encoding standard)
*   **C2C:** Center-to-Center
*   **CCTV:** Closed-Circuit Television
*   **DART:** Dallas Area Rapid Transit
*   **DATEX:** Data Exchange (European traffic data standard, used here for encoding)
*   **DMS:** Dynamic Message Sign
*   **GUI:** Graphical User Interface
*   **ITS:** Intelligent Transportation Systems
*   **NCTCOG:** North Central Texas Council of Governments
*   **SRS:** Software Requirements Specification
*   **SwRI:** Southwest Research Institute
*   **TMC:** Traffic Management Center
*   **TMDD:** Traffic Management Data Dictionary (an ITS standard)
*   **TxDOT:** Texas Department of Transportation

#### 1.4 References
*   ITS Standards - Traffic Management Data Dictionary (TMDD)
*   ISO/IEC 8824-1:2015 - Abstract Syntax Notation One (ASN.1)
*   ESRI ARC IMS Product Documentation
*   Project Charter and Statement of Work, NCTCOG

#### 1.5 Overview
The remainder of this document is structured as follows:
*   **Section 2:** Overall Description – Provides context, user characteristics, constraints, and assumptions.
*   **Section 3:** Specific Requirements – Details all functional, interface, performance, and design constraints.
*   **Appendices:** Include supplementary information such as data dictionary excerpts or use case diagrams.

### 2. Overall Description

#### 2.1 Product Perspective
The C2C system is a new, standalone software suite that will act as a middleware layer between existing, heterogeneous Traffic Management Systems operated by TxDOT, City of Dallas, DART, and other regional agencies. It will not replace these legacy systems but will provide a standardized communication bridge and a unified data repository.

#### 2.2 Product Functions (Summary)
1.  **Data Integration Hub:** Aggregate and store traffic data (speeds, volumes, incidents, lane closures) from multiple agency sources.
2.  **Device Interoperability Gateway:** Translate and route status queries and control commands for ITS field devices between agencies using a standard protocol.
3.  **Public Information Portal:** Serve real-time, color-coded traffic maps and incident lists to the public via a web browser.
4.  **Data Entry Client:** Provide a simple application for agencies without a TMC to contribute incident data to the regional system.
5.  **System Management:** Provide configuration, monitoring, and logging tools for network administrators.

#### 2.3 User Characteristics
| User Class | Skill Level | Primary Interaction |
| :--- | :--- | :--- |
| **TMC Operator** (TxDOT, City) | Expert | Uses existing TMC software; indirect interaction via C2C data/command routing. May use Remote Control GUI. |
| **Public Traveler** | Novice | Uses Public Web Map via standard web browser. No authentication required. |
| **Agency Data Entry Clerk** | Casual | Uses dedicated Incident Input GUI. Requires basic data entry skills. |
| **System/Network Administrator** | Expert | Installs, configures, and monitors C2C server software. Uses configuration files and log viewers. |
| **System Integrator (SwRI)** | Expert | Configures system "building blocks" to onboard new partner agencies. |

#### 2.4 Constraints
1.  **Technical:** The core server and desktop GUI applications must be developed in C/C++ and run on the Microsoft Windows NT operating system.
2.  **Technical:** The public web map must be implemented using ESRI's ARC Internet Map Server (ARC IMS) product.
3.  **Technical:** All C2C data exchange must comply with the TMDD standard, be encoded in DATEX/ASN.1 format, and be transported over TCP/IP sockets.
4.  **Design:** The system architecture must use configurable adapters to interface with dissimilar partner agency systems.
5.  **Design:** The Incident Input GUI and Remote Control GUI must be developed using C/C++ and ESRI Map Objects.

#### 2.5 Assumptions and Dependencies
*   Assumption: Participating agencies will provide stable TCP/IP network connectivity to a designated central server location.
*   Assumption: Each agency will develop or procure the necessary "adapter" to translate between their internal data formats and the project's TMDD/DATEX standard.
*   Dependency: Successful project outcomes depend on agencies agreeing on a common set of device commands for each device type.
*   Dependency: The public web map is dependent on ARC IMS software licenses and infrastructure.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Data Repository and Exchange (FRE-100 Series)
*   **FRE-101:** The system shall receive, parse, and store TMDD/DATEX messages containing traffic network data (link geometries, node definitions) from all connected centers.
*   **FRE-102:** The system shall receive, parse, and store TMDD/DATEX messages containing real-time traffic conditions (link speed, volume, occupancy) from all connected centers at a configurable interval (e.g., every 30-60 seconds).
*   **FRE-103:** The system shall receive, parse, and store TMDD/DATEX messages containing incident and lane closure reports from all connected centers and the Incident Input GUI.
*   **FRE-104:** The system shall distribute updated traffic condition, incident, and device status data to all subscribed centers in TMDD/DATEX format upon receipt or on a periodic broadcast basis.

##### 3.1.2 Device Monitoring and Control (FRE-200 Series)
*   **FRE-201:** The system shall receive and forward TMDD/DATEX device status requests from an authorized center to the center owning the target device (DMS, CCTV, ramp meter, etc.).
*   **FRE-202:** The system shall receive and forward TMDD/DATEX device control commands from an authorized center to the center owning the target device.
*   **FRE-203:** The system shall enforce a configurable "Days/Times Commands Accepted" matrix per device type and owning center. Commands sent outside accepted timeframes shall be rejected with an error message.
*   **FRE-204:** The system shall maintain a real-time inventory and status (e.g., online, offline, fault) of all regional devices reported by owning centers.

##### 3.1.3 Public Web Map (FRE-300 Series)
*   **FRE-301:** The web map shall display a color-coded representation of current traffic speeds on major roadways. Colors (Green/Yellow/Red) shall correspond to speed thresholds **TBD MPH**.
*   **FRE-302:** The web map shall display icons representing the location and type of active incidents and lane closures.
*   **FRE-303:** The web map shall display icons representing the location of key ITS field devices (DMS, CCTV). Clicking a CCTV icon may initiate a request for a static snapshot **TBD**.
*   **FRE-304:** The web map shall include a legend, zoom/pan controls, and a refresh mechanism (automatic or manual).

##### 3.1.4 Incident Input GUI (FRE-400 Series)
*   **FRE-401:** The GUI shall provide a form-based interface for entering incident details: location (select from map or list), type, severity, lanes affected, start time, and estimated duration.
*   **FRE-402:** The GUI shall allow entry of lane closure information associated with an incident or maintenance.
*   **FRE-403:** Upon submission, the GUI shall package the data into a valid TMDD/DATEX message and transmit it to the central C2C server.

##### 3.1.5 System Administration (FRE-500 Series)
*   **FRE-501:** The system shall operate in a "Test Mode" where messages are logged in human-readable detail but not forwarded to partner centers.
*   **FRE-502:** The system shall maintain comprehensive transaction logs of all messages received, processed, and sent, including timestamps and source/destination.
*   **FRE-503:** System parameters (center addresses, data intervals, command timeframes) shall be configurable via text-based configuration files without code modification.

#### 3.2 Interface Requirements

##### 3.2.1 External Hardware/Software Interfaces (INT-100 Series)
*   **INT-101:** The C2C Server shall communicate with each partner agency's system via a dedicated, persistent TCP/IP socket connection on a port **TBD**.
*   **INT-102:** The Public Web Map shall be accessible via HTTP/HTTPS on a standard web browser (IE, Firefox, etc.) without requiring plugins.

##### 3.2.2 Communication Protocols and Standards (INT-200 Series)
*   **INT-201:** All C2C data exchange shall use message structures defined in the Traffic Management Data Dictionary (TMDD) v2.x.
*   **INT-202:** All C2C messages shall be encoded using the DATEX/ASN.1 PER (Packed Encoding Rules) **TBD** (Unaligned/Aligned).
*   **INT-203:** The system shall implement a project-specific application-level protocol over TCP/IP for message framing, acknowledgment, and heartbeats.

#### 3.3 Performance Requirements
*   **PER-001:** The system shall process and store incoming traffic condition updates from all centers with a latency of less than 5 seconds from receipt to repository update.
*   **PER-002:** The Public Web Map shall refresh displayed data at intervals not exceeding 2 minutes.
*   **PER-003:** The C2C server shall be capable of simultaneously maintaining connections with up to 10 regional centers.
*   **PER-004:** The system shall have an operational availability of 99.5% during core hours (6:00 AM - 8:00 PM, 7 days/week).

#### 3.4 Design Constraints
*   **CON-001:** The software shall be implemented in ANSI C/C++.
*   **CON-002:** The system shall be designed as a collection of configurable components (e.g., agency-specific adapters, data filters) to facilitate the addition of new partner agencies.
*   **CON-003:** Database schemas (if used) shall be derived from the TMDD logical model.

#### 3.5 Undecided Issues (To Be Resolved)
1.  Specific speed thresholds for web map color-coding.
2.  Mechanism for maintaining consistent link IDs between roadway and transit network datasets.
3.  Final list of supported CCTV commands (e.g., tour, momentary control).
4.  Finalized "Days/Times Commands Accepted" matrix for all device types and centers.
5.  Security and connectivity plan for the Remote Control GUI across public networks.

---
*This document is subject to change upon resolution of undecided issues and stakeholder review.*