# Software Requirements Specification (SRS)
## Dallas/Ft. Worth Regional Center-to-Center Communications Network (C2C)

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Dallas/Ft. Worth Regional Center-to-Center Communications Network (C2C). It serves as a comprehensive guide for developers, testers, project managers, and stakeholders, ensuring a common understanding of the system to be developed. The primary audience includes the NCTCOG Software Task Force, development teams, and participating agency representatives.

#### 1.2 Project Scope
The C2C project will establish a regional communications network to facilitate the sharing of traffic information and remote control of Intelligent Transportation Systems (ITS) field devices among Traffic Management Centers (TMCs) in the Dallas/Ft. Worth metropolitan area.

**In-Scope:**
*   Development of a central C2C data repository (Data Collector).
*   Implementation of protocol adapters to convert disparate TMC data to the standard Traffic Management Data Dictionary (TMDD) format.
*   Development of a web-based application for public viewing of color-coded traffic condition maps.
*   Development of a secure Remote Control GUI for authorized operators to control field devices across jurisdictions.
*   Development of an Incident/Lane Closure Reporting GUI for agencies without formal TMCs.
*   Implementation of data exchange using DATEX/ASN over TCP/IP protocols.
*   System administration tools for configuration and monitoring.

**Out-of-Scope:**
*   Modification of existing, legacy TMC systems at participating agencies.
*   Provision of network hardware or infrastructure (firewalls, routers, leased lines).
*   Development of the NCTCOG Geo-Data warehouse (integration only).
*   Definition of inter-agency operational policies and memoranda of understanding (MOUs).

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **C2C:** Center-to-Center Communications
*   **TMC:** Traffic Management Center
*   **NCTCOG:** North Central Texas Council of Governments
*   **ITS:** Intelligent Transportation Systems
*   **TMDD:** Traffic Management Data Dictionary (a national ITS standard)
*   **DATEX/ASN:** A standardized data exchange protocol and encoding format.
*   **DMS:** Dynamic Message Sign
*   **CCTV:** Closed-Circuit Television
*   **GUI:** Graphical User Interface
*   **TCP/IP:** Transmission Control Protocol/Internet Protocol

#### 1.4 References
*   ITS Standards - Traffic Management Data Dictionary (TMDD) Version X.X
*   DATEX/ASN Specification Documentation
*   NCTCOG Regional ITS Architecture

### 2. Overall Description

#### 2.1 Product Perspective
The C2C system is a new, independent software system that will act as a regional integration hub. It interfaces externally with:
1.  **Legacy TMC Systems:** Via project-specific protocol adapters.
2.  **NCTCOG Geo-Data Warehouse:** For base map geometry and reference data.
3.  **End-User Browsers:** For the public web map and administrative GUIs.
4.  **Agency Networks:** Via TCP/IP connections for data exchange and device control.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **TMC Operator** | Technically proficient, agency-employed, operates local TMC software. | Share data, view regional status, remotely control devices to manage cross-jurisdictional incidents. |
| **Agency User (No TMC)** | May have limited technical training (e.g., public works staff). | Report incidents/lane closures easily, view regional traffic data. |
| **Public User** | General public, uses standard web browsers. | View current traffic speeds and incidents on an intuitive map for trip planning. |
| **System Administrator** | High technical skill, employed by NCTCOG or managing agency. | Install, configure, monitor, and extend the C2C system components. |
| **Project Developer/Tester** | Software developer/integrator. | Test system components in isolation with detailed logging. |

#### 2.3 Operating Environment
*   **Server Platform:** Core C2C server components (Data Collector, communication modules) shall execute in a Microsoft Windows NT 4.0 (or later) environment.
*   **Client Platform:** GUI applications (Remote Control, Incident Reporting) shall be compatible with Windows-based PCs. The public web map shall be accessible via standard web browsers (e.g., Internet Explorer 5.0+, Netscape Navigator 4.0+).
*   **Network:** The system shall operate over standard TCP/IP networks. DATEX/ASN runtime libraries must be installed on all computers participating in C2C data exchange.
*   **External Systems:** Must interface with various legacy TMC systems (specific interfaces TBD per agency).

#### 2.4 Design and Implementation Constraints
1.  **Interoperability Constraint:** All C2C data exchange shall comply with the national ITS TMDD standard and associated message sets.
2.  **Implementation Constraint:** Core server software shall be implemented in the C/C++ programming language.
3.  **Architectural Constraint:** The system shall be designed as a set of configurable, reusable software "building blocks" to promote extensibility.
4.  **Operational Constraint:** The system must support two distinct modes: Normal Operation and Test Mode (with comprehensive activity logging).

#### 2.5 Assumptions and Dependencies
*   **Assumption:** Participating agencies will provide necessary network connectivity and firewall configuration to allow TCP/IP communication with the central C2C server.
*   **Assumption:** The NCTCOG Geo-Data warehouse will be available and provide accurate, up-to-date base map data.
*   **Dependency:** Successful integration is dependent on the development and configuration of protocol adapters for each unique legacy TMC system.
*   **Dependency:** The definition of link identifiers between the roadway network and transit databases is a procedural dependency outside the software's control.

### 3. System Features and Requirements

#### 3.1 Data Collection, Conversion, and Storage
**3.1.1 Description**
The system shall receive traffic and device data from connected TMCs, convert it from native formats to the standard TMDD format, and store it in a central repository.

**3.1.2 Functional Requirements**
| ID | Requirement |
| :--- | :--- |
| **FR-010** | The system shall provide a configurable protocol adapter interface for each connected legacy TMC system. |
| **FR-011** | The protocol adapter shall convert incoming system-specific data (incidents, device status, traffic conditions) into TMDD-compliant messages. |
| **FR-012** | The system shall deposit all converted TMDD data into the central C2C Data Collector repository. |
| **FR-013** | The Data Collector shall store data elements as defined in Section 4 (Domain Data Model). |
| **FR-014** | The system shall timestamp all incoming data upon receipt. |

#### 3.2 Regional Data Exchange
**3.2.1 Description**
The system shall facilitate the reliable exchange of standardized TMDD data between all participating centers over a TCP/IP network.

**3.2.2 Functional Requirements**
| ID | Requirement |
| :--- | :--- |
| **FR-020** | The system shall exchange data between centers using the DATEX/ASN protocol over TCP/IP. |
| **FR-021** | The system shall be capable of both sending data originated locally and receiving data from remote centers. |
| **FR-022** | The communication module shall manage connection status and handle communication errors (e.g., retry logic, alerting). |

#### 3.3 Web-Based Traffic Map
**3.3.1 Description**
The system shall generate and serve a public-facing, color-coded graphical map displaying current traffic speeds and incident information.

**3.3.2 Functional Requirements**
| ID | Requirement |
| :--- | :--- |
| **FR-030** | The system shall generate a map image (e.g., GIF/JPEG) depicting the roadway network. |
| **FR-031** | Roadway links shall be color-coded based on current average speed (Green: free flow, Yellow: congested, Red: heavily congested). *[Thresholds TBD]*. |
| **FR-032** | The map shall display icons for active incidents and lane closures, with tooltips or a legend showing details (type, location, severity). |
| **FR-033** | The map shall refresh automatically at a configurable interval (e.g., every 5 minutes). |
| **FR-034** | The map shall be accessible via a standard web browser without requiring proprietary plugins. |

#### 3.4 Remote Device Control
**3.4.1 Description**
Authorized operators shall be able to send control commands to field devices (e.g., DMS, CCTV) located in another agency's jurisdiction via a secure GUI.

**3.4.2 Functional Requirements**
| ID | Requirement |
| :--- | :--- |
| **FR-040** | The system shall provide a Remote Control GUI requiring username/password authentication. |
| **FR-041** | The GUI shall present the operator with a list of controllable devices from all participating centers, filtered by device type and location. |
| **FR-042** | For DMS devices, the GUI shall allow the user to compose a message, select font/justification, and issue a `PostMessage` command. |
| **FR-043** | For CCTV devices, the GUI shall allow the user to issue standard commands (`Pan`, `Tilt`, `Zoom`, `Focus`). *Note: Support for `Momentary Pan/Tilt` and `Tour` commands is agency-dependent.* |
| **FR-044** | The system shall format the user's command into a TMDD-compliant control message and route it to the TMC responsible for the target device. |
| **FR-045** | The system shall implement command timeframe controls (e.g., a command may only be valid for 5 minutes) to prevent device lock-up. |
| **FR-046** | The GUI shall provide feedback on the command status (Sent, Acknowledged, Rejected, Timed Out). |

#### 3.5 Incident and Lane Closure Reporting
**3.5.1 Description**
Users from agencies without a formal TMC shall be able to manually input incident and lane closure data into the regional system via a dedicated GUI.

**3.5.2 Functional Requirements**
| ID | Requirement |
| :--- | :--- |
| **FR-050** | The system shall provide an Incident/Lane Closure Reporting GUI with user authentication. |
| **FR-051** | The GUI shall allow the user to select an incident/lane closure type, location (from a map or list), severity, description, and schedule. |
| **FR-052** | Upon submission, the system shall create a TMDD-compliant message and inject it directly into the C2C Data Collector for regional distribution. |

#### 3.6 System Administration and Monitoring
**3.6.1 Description**
The system shall provide capabilities for configuration, status monitoring, and operation in a test mode.

**3.6.2 Functional Requirements**
| ID | Requirement |
| :--- | :--- |
| **FR-060** | The system shall allow an administrator to configure parameters for software "building blocks" (e.g., center addresses, device lists, map thresholds). *[Detailed parameters TBD]*. |
| **FR-061** | The system shall provide a network-wide device status summary, showing device type, location, and current state (e.g., `ONLINE`, `OFFLINE`, `ACTIVE`, `FAULT`). |
| **FR-062** | The system shall support a "Test Mode" where all data exchange and commands are logged to a detailed activity file but not acted upon by recipient centers. |
| **FR-063** | The system shall generate alerts for critical errors (e.g., repository failure, loss of connection to a major center). |

### 4. Domain Data Model
The following entities represent the core information managed by the C2C system.

```plaintext
RoadwayNetwork
----------------
PK NetworkIdentifier: String
   NetworkName: String
   ListOfLinks: Array[Link]
   ListOfNodes: Array[Node]
   NumberOfLinks: Integer

TrafficIncident
----------------
PK IncidentID: String
   NetworkIdentifier: String (FK)
   Location: Geometry
   Description: String
   Status: Enum [Reported, Confirmed, Cleared]
   Severity: Enum [Minor, Moderate, Major]
   ConfirmedTime: DateTime

FieldDevice
----------------
PK DeviceIdentifier: String
   NetworkIdentifier: String (FK)
   DeviceType: Enum [DMS, CCTV, Sensor]
   Location: LatLong
   Status: Enum [Online, Offline, Fault]
   CurrentState: String (e.g., DMS Message, CCTV Preset)

TrafficCondition
----------------
PK Composite(LinkIdentifier: String, Timestamp: DateTime)
   NetworkIdentifier: String (FK)
   Speed: Float (mph)
   Volume: Integer (veh/hr)
   Occupancy: Float (%)
   TravelTime: Float (min)

LaneClosure
----------------
PK LaneClosureID: String
   NetworkIdentifier: String (FK)
   Location: Geometry
   Description: String
   AffectedLanes: String
   StartTime: DateTime
   EndTime: DateTime

UserCommandRequest
----------------
PK RequestID: String
   Username: String
   TargetDeviceID: String (FK)
   CommandParameters: String
   Timestamp: DateTime
   Status: Enum [Pending, Executed, Failed]
```

### 5. Non-Functional Requirements

#### 5.1 Performance
*   **Data Latency:** The time from an event occurring at a source TMC to it being available in the central repository shall not exceed 60 seconds under normal load.
*   **Map Generation:** The public web map shall be generated and served to the client browser within 15 seconds of a request.

#### 5.2 Reliability & Availability
*   The core C2C server components shall have an operational availability of 99.5% during standard business hours (6:00 AM - 8:00 PM, Monday-Friday).
*   The system shall implement data persistence to prevent loss of critical incident and device status information during a controlled restart.

#### 5.3 Security
*   All remote control and data reporting actions shall require user authentication via username and password.
*   The system shall not store passwords in plain text.
*   Command execution shall be subject to configurable timeframe controls to prevent unauthorized long-term device takeover.

#### 5.4 Interoperability & Extensibility
*   The system **shall** comply with TMDD standard message sets for all C2C data exchange.
*   The software architecture **shall** be modular, using configurable "building blocks" to allow the addition of new partner agencies, device types, and data elements with minimal code changes.

#### 5.5 Operational
*   The system **shall** operate in two modes: Normal and Test (with full activity logging).
*   Core server components **shall** execute on the Microsoft Windows NT platform.
*   Core software **shall** be implemented in C/C++.

### 6. Appendices

#### Appendix A: Undecided Issues (TBD)
1.  **Map Color Thresholds:** Specific speed values (in MPH) for defining "Free Flow" (Green), "Congested" (Yellow), and "Heavily Congested" (Red) conditions.
2.  **CCTV Command Support:** Final list of supported CCTV commands (`Momentary Pan/Tilt`, `Tour`) will depend on the capabilities of each agency's underlying system.
3.  **Network Configuration:** Detailed specifications for firewall traversal and connectivity over public networks for the Remote Control GUI require further network architecture analysis.
4.  **Building Block Parameters:** The complete set of configurable parameters for agency-specific deployments needs to be defined during the design phase.
5.  **Link ID Management:** A procedural solution is required to maintain consistency between roadway network links and transit database links.

#### Appendix B: Risk Log
| Risk | Probability | Impact | Mitigation Strategy | Owner |
| :--- | :--- | :--- | :--- | :--- |
| Legacy System Integration | High | High | Develop project-specific protocol adapters. | Development Team |
| Cross-Agency Device Security | Medium | High | Implement authentication + command timeouts. | System Architect |
| Network/Firewall Connectivity | Medium | Medium | Use standard TCP/IP; require agency IT coordination. | Project Manager |
| Data Inconsistency (Road/Transit) | High | Medium | Acknowledge as procedural issue; clear ownership definitions. | NCTCOG |
| Scalability with New Partners | Low | High | Modular, building-block design from inception. | System Architect |

---
*This document is considered proprietary to the North Central Texas Council of Governments and its project partners.*