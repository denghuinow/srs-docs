# Software Requirements Specification (SRS)
## Dallas/Ft. Worth Regional Center-to-Center Communications Network (C2C)

**Document Version:** 3.0  
**Date:** [Date of Document Finalization]  
**Status:** Baseline

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Dallas/Ft. Worth Regional Center-to-Center (C2C) Communications Network. It serves as the authoritative reference for developers, testers, project managers, and stakeholders, ensuring a common understanding of the system to be delivered.

#### 1.2 Scope
This project establishes a regional C2C communications network for the Dallas/Ft. Worth metroplex. Its primary goal is to create a common repository for regional traffic data and a standardized mechanism for exchanging device control information between disparate Traffic Management Centers (TMCs) and transportation agencies.

**In-Scope:**
*   Development of a central C2C infrastructure (Data Collector, common repository).
*   Creation of standardized interfaces (based on TMDD/DATEX-ASN) for data exchange with participating centers.
*   Development of client applications: a public Web Map, an Incident GUI, and a Remote Control GUI.
*   Integration with initial participating TMCs (e.g., TxDOT Dallas and Ft. Worth).
*   Configuration and deployment of the system within the regional network.

**Out-of-Scope (Key Non-Goals):**
*   Modification of legacy TMC systems' internal logic or databases.
*   Direct integration of new, standards-based systems via a project-specific custom protocol. Such systems must connect natively using the ITS standards (TMDD).
*   Provision of network hardware or wide-area network (WAN) connectivity between agencies.
*   Management of field devices (e.g., DMS, CCTV) themselves; the system only facilitates command and status exchange.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **C2C:** Center-to-Center
*   **TMC:** Traffic Management Center
*   **TxDOT:** Texas Department of Transportation
*   **NCTCOG:** North Central Texas Council of Governments
*   **ITS:** Intelligent Transportation Systems
*   **TMDD:** Traffic Management Data Dictionary (an ITS standard)
*   **DATEX-ASN:** Data Exchange - Abstract Syntax Notation (a standard encoding format)
*   **DMS:** Dynamic Message Sign
*   **CCTV:** Closed-Circuit Television
*   **GUI:** Graphical User Interface
*   **SLA:** Service Level Agreement

#### 1.4 References
*   ITS Standards: Traffic Management Data Dictionary (TMDD) Version 3.0+
*   DATEX II / ASN.1 Encoding Rules
*   Project Charter: Dallas/Ft. Worth Regional C2C Network
*   NCTCOG Regional ITS Architecture

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the system, its stakeholders, and operating environment. Section 3 details the specific functional and non-functional requirements. Appendices contain supplementary information such as data models and interface specifications.

### 2. Overall Description

#### 2.1 Product Perspective
The C2C system is a middleware platform that sits between independent agency TMCs and end-user applications. It acts as a data hub, translating between agency-native formats and the regional ITS standard (TMDD), enabling interoperability.

**System Interfaces:**
1.  **Upstream:** Connections to participating TMCs (TxDOT Dallas, TxDOT Ft. Worth, etc.).
2.  **Downstream:** Data feeds to the Web Map Server, Incident GUI, and Remote Control GUI.
3.  **External:** Initial basemap data sourced from the NCTCOG Geo-Data Warehouse.

#### 2.2 Stakeholders and User Characteristics
| Stakeholder Group | Description | Key Interests / Influence |
| :--- | :--- | :--- |
| **NCTCOG / Software Task Force** | Project sponsor and governing body. | Regional coordination, funding, requirement definition, and acceptance. |
| **Traffic Management Centers (TMCs)** | Primary operators (e.g., TxDOT). | Providing reliable data, receiving valid control commands, maintaining sovereignty over their devices. |
| **Agencies without formal TMCs** | Secondary users (e.g., city traffic departments). | Inputting incident data and potentially issuing control requests via provided GUIs. |
| **System Administrators** | Technical personnel for the C2C system. | Configuring, deploying, monitoring, and troubleshooting the C2C infrastructure. |
| **Public / Web Users** | General public accessing traffic information. | Viewing accurate, near-real-time traffic conditions, incidents, and device statuses on a web map. |

#### 2.3 Operating Environment
*   **Hardware:** The C2C server software will be deployed on standard enterprise-grade servers located in a secure data center.
*   **Software:** Will operate on a modern server operating system (e.g., Linux/Windows Server). Components will interface with relational databases (e.g., PostgreSQL/PostGIS) and web/application servers.
*   **Networks:** Will communicate over TCP/IP via secured agency networks (potentially using VPNs over the Internet). Must be resilient to intermittent network outages.

#### 2.4 Design and Implementation Constraints
1.  **Compliance Constraint:** All center-to-center data exchange **must** comply with the TMDD standard and use DATEX/ASN encoding.
2.  **Architectural Constraint:** The system must use a "building block" approach with configurable adapters to interface with heterogeneous legacy TMC systems.
3.  **Security Constraint:** All device control commands **must** be authenticated. Communication channels between components must be secured.

#### 2.5 User Documentation
The following documentation shall be provided:
*   System Administrator Manual (installation, configuration, maintenance)
*   Incident GUI User Guide
*   Remote Control GUI User Guide
*   TMC Interface Specification (for participating centers)

#### 2.6 Assumptions and Dependencies
*   **Assumption:** Participating TMCs will develop or provide the necessary local interface to convert their native data to/from the TMDD standard.
*   **Assumption:** Agencies will provide the necessary network firewall configurations to allow communication with the C2C infrastructure.
*   **Dependency:** Availability and accuracy of initial basemap data from the NCTCOG Geo-Data Warehouse.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Data Aggregation & Repository Management
*   **FR-1: Data Reception:** The C2C Data Collector shall accept incoming TMDD-formatted data streams via TCP/IP from participating centers.
*   **FR-2: Data Validation:** The system shall validate the structure and required fields of incoming TMDD messages before storage.
*   **FR-3: Data Storage:** The system shall store validated traffic conditions, incidents, and device statuses in the common repository, maintaining data history as configured.
*   **FR-4: Graceful Degradation:** If the connection to a participating center is lost, the system shall log the failure, continue operating with data from remaining centers, and attempt reconnection per a configured policy.

##### 3.1.2 Data Dissemination
*   **FR-5: Data Provisioning:** The system shall provide a standardized API (e.g., REST/WebSocket) for client applications (Web Map, GUIs) to query consolidated, real-time data from the repository.
*   **FR-6: Web Map Data Feed:** The system shall serve geographic data (links, nodes), current traffic conditions, incident locations, and device icons to the Web Map Server in a format it can consume (e.g., GeoJSON, vector tiles).

##### 3.1.3 Incident Management
*   **FR-7: Incident Input:** The Incident GUI shall allow authenticated agency users to manually input new traffic incidents or lane closures, including description, location (map pick or link/node selection), and severity.
*   **FR-8: Incident Propagation:** Incidents entered via the Incident GUI shall be formatted as TMDD messages and stored directly in the C2C repository, making them immediately available for dissemination.

##### 3.1.4 Device Command & Control
*   **FR-9: Command Initiation:** The Remote Control GUI shall allow authenticated users to select a field device (DMS, CCTV), specify command parameters, and issue a control command.
*   **FR-10: Command Routing:** The C2C infrastructure shall route the TMDD-formatted control command to the interface of the center that owns the target device.
*   **FR-11: Command Validation:** The target center's interface is responsible for validating user credentials and checking if the command is issued within a pre-configured acceptable timeframe.
*   **FR-12: Command Execution Feedback:** The system shall relay the command execution status (e.g., "accepted," "rejected - invalid timeframe," "failed - command not supported") from the target center back to the Remote Control GUI.
*   **FR-13: Command Logging:** The system shall log all device control commands, including timestamp, user, device, action, and outcome.

##### 3.1.5 User & System Administration
*   **FR-14: User Authentication:** The system shall authenticate users of the Incident and Remote Control GUIs via username and password.
*   **FR-15: Role-Based Access:** The system shall support configurable user roles (e.g., "Incident Reporter," "Device Operator," "Administrator") to control access to functions.
*   **FR-16: Network/Device Registry:** System Administrators shall be able to configure and manage the list of participating networks, roadway links/nodes, and field devices within the C2C system.

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance
*   **NFR-1:** The Web Map shall refresh and display updated traffic condition data at intervals not exceeding **5 minutes**.
*   **NFR-2:** The Data Collector shall process and store incoming TMDD messages with a latency of **< 1 second** under normal load (defined as data from 5 simultaneous centers).
*   **NFR-3:** The system's data provisioning API shall respond to queries for consolidated data within **2 seconds** for 95% of requests under typical load.

##### 3.2.2 Reliability & Availability
*   **NFR-4:** The core C2C server software shall achieve **99.5% uptime** during standard regional operational hours (e.g., 5:00 AM - 10:00 PM daily).
*   **NFR-5:** The system shall be designed for graceful degradation, continuing partial operation if connectivity to one or more participating centers is lost.

##### 3.2.3 Security
*   **NFR-6:** All device control commands **must** be authenticated. Authentication checks must be performed within **3 seconds**.
*   **NFR-7:** All communication between the C2C infrastructure and TMCs/GUIs shall occur over defined protocols (TCP/IP) on secured networks, employing agency-approved security measures (e.g., VPNs, TLS).

##### 3.2.4 Compliance
*   **NFR-8:** The system's external center-to-center data exchange interface shall comply with the **TMDD standard (Version 3.0 or later)** and use **DATEX/ASN encoding**.

##### 3.2.5 Observability & Maintainability
*   **NFR-9:** The system must log all device control commands and their final outcomes for audit purposes.
*   **NFR-10:** The system shall provide a "test mode" with detailed, configurable activity logging (message payloads, routing decisions) to facilitate debugging and integration.

#### 3.3 System Attributes

##### 3.3.1 Domain Model
The core data entities managed by the system are as follows:
```yaml
Network:
  - id (String, Unique, PK)
  - name (String)
  - owner_agency (String, Required)

Link:
  - id (String, Unique, PK)
  - network_id (Foreign Key to Network)
  - start_node_id (Foreign Key to Node)
  - end_node_id (Foreign Key to Node)
  - direction (Enum: NB, SB, EB, WB, BOTH)
  - speed_limit (Integer)

Node:
  - id (String, Unique, PK)
  - network_id (Foreign Key to Network)
  - latitude (Float, Required)
  - longitude (Float, Required)

TrafficCondition:
  - link_id (Foreign Key to Link)
  - timestamp (DateTime, Required)
  - speed (Float)
  - volume (Integer)

Incident:
  - id (String, Unique, PK)
  - network_id (Foreign Key to Network)
  - location_description (String)
  - geometry (GeoJSON, e.g., Point/LineString)
  - description (String, Required)
  - status (Enum: Reported, Confirmed, Cleared)
  - severity (Enum: Minor, Moderate, Major)

Device:
  - id (String, Unique, PK)
  - network_id (Foreign Key to Network)
  - type (Enum: DMS, CCTV, Sensor, etc.)
  - location (GeoJSON Point)
  - status (String, Required, e.g., "Online", "Offline", "Active")

DeviceCommand:
  - id (String, Unique, PK)
  - device_id (Foreign Key to Device)
  - username (String, Required, Foreign Key to User)
  - timestamp_requested (DateTime)
  - command_type (String)
  - command_parameters (JSON)
  - status (Enum: Pending, Accepted, Rejected, Failed)

User:
  - username (String, Unique, PK)
  - role (Enum: Viewer, Reporter, Operator, Admin)
  - associated_network_id (Foreign Key to Network, Nullable)
```

##### 3.3.2 External Interfaces
| System | Direction | Interaction | Protocol/Format | Key Notes |
| :--- | :--- | :--- | :--- | :--- |
| Participating TMCs | Inbound | Data Pub & Command Rx | TCP/IP, TMDD/DATEX-ASN | Adapter required for native format translation. SLA: Data freq. (e.g., 1 min), Command response < 10s. |
| C2C Data Collector | Outbound | Data Provisioning | REST API / WebSocket, JSON/GeoJSON | Serves consolidated data to clients. SLA: Query response < 2s. |
| Web Map Server | Outbound | Map Data Feed | Vector Tiles / GeoJSON | Provides geometry and dynamic data for rendering. SLA: Refresh data ≤ 5 min. |
| Incident GUI App | Inbound | Direct Data Input | HTTPS, JSON | Authenticated submission of incidents. |
| Remote Control GUI App | Bi-Dir | Device C2 | HTTPS, WebSocket (JSON) | Authenticated command send and status receive. |
| NCTCOG Geo-Data Warehouse | Inbound (Init) | Basemap Source | File Transfer / GeoDB | Provides initial static roadway network layers. |

### 4. Acceptance Criteria
Acceptance criteria are defined in Gherkin-style format.

**AC-1: Real-Time Traffic Display on Web Map**
*   **Scenario:** Displaying current traffic speeds.
    *   Given the Web Map application is loaded and the C2C system is receiving live data from multiple TMCs,
    *   When a public user views a major highway segment (e.g., I-35E),
    *   Then that roadway link is displayed color-coded (green/yellow/red) based on the current speed data stored in the C2C repository.
*   **Scenario:** Displaying a new incident.
    *   Given a new traffic incident has been entered and saved via the Incident GUI,
    *   When the Web Map performs its next data refresh,
    *   Then an appropriate incident icon appears at the correct geographic location on the map.

**AC-2: Cross-Jurisdictional Device Control**
*   **Scenario:** Successful DMS message change.
    *   Given an authenticated user of the Remote Control GUI with "Operator" role has selected a DMS owned by a different agency,
    *   When the user submits a valid "Change Message" command with appropriate parameters during the center's accepted command timeframe,
    *   Then the system sends the command and the GUI displays a confirmation status (e.g., "Command Accepted by [Agency]").
*   **Scenario:** Rejected unsupported command.
    *   Given a user attempts to issue a CCTV "Momentary Pan" command to a camera owned by the Ft. Worth TMC,
    *   And the Ft. Worth system does not support the "Momentary Pan" command type,
    *   When the command is processed,
    *   Then the Remote Control GUI displays a failure status indicating "Command type not supported by target center."

### 5. Project Planning & Risk Management

#### 5.1 Milestones and Release Strategy
1.  **Milestone 1:** Finalize and baseline this SRS (Version 3.0).
2.  **Milestone 2:** Complete detailed design for core C2C infrastructure and interfaces to initial centers (TxDOT TMCs).
3.  **Milestone 3:** Develop and complete unit testing for core Data Collector, Data Transmission, and Web Map Server components.
4.  **Milestone 4:** Complete integration testing with initial participating centers (Dallas and Ft. Worth TxDOT TMCs).
5.  **Milestone 5:** Develop, test, and deploy the Incident GUI and Remote Control GUI applications.
6.  **Milestone 6:** Conduct a pilot deployment and obtain operational acceptance with a subset of device types (e.g., DMS control, CCTV status, incident flow) before authorizing full regional rollout.

#### 5.2 Risk List and Mitigation Strategies
| ID | Risk Description | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- | :--- |
| R-1 | Heterogeneous/legacy TMC systems increase interface complexity. | High | High | Use configurable "building block" adapters. Develop a clear TMC Interface Specification early. |
| R-2 | Network latency/outages delay critical device commands. | Medium | High | Implement configurable command timeframes. Provide clear, real-time status feedback to operators. Design system for graceful degradation. |
| R-3 | ITS standards (TMDD) evolve post-deployment. | Medium | Medium | Isolate standard-specific encoding/decoding logic into separate, swappable modules. |
| R-4 | Complex configuration for associating transit & roadway data leads to errors. | High | Medium | Document the complexity explicitly. Build robust configuration management tools with validation checks. |
| R-5 | Security vulnerabilities in remote command over public networks. | Medium | Critical | Mandate authentication for all commands. Design relies on agency-managed network-level security (firewalls, VPNs). Perform security penetration testing. |
| R-6 | Insufficient processing capacity for region-wide data volume. | Low | High | Design core components for horizontal scalability. Conduct performance testing using projected peak data volumes. |

### 6. Open Issues & Decisions Pending
The following items require resolution and are the responsibility of the indicated parties:

1.  **OID-1:** Specific speed thresholds (in MPH) for color-coding links on the Web Map (Green/Yellow/Red).
    *   **Responsible:** NCTCOG Software Task Force.
2.  **OID-2:** The definitive list of days and times (command timeframes) each participating center will accept remote control commands for each device type (DMS, CCTV).
    *   **Responsible:** Individual Participating Centers (TxDOT Dallas, TxDOT Ft. Worth, etc.).
3.  **OID-3:** Final resolution strategy for data inconsistencies between roadway network links (managed by one center) and associated transit data links (managed by another).
    *   **Responsible:** NCTCOG & Affected Agency Architects.
4.  **OID-4:** Specific firewall rule and gateway configuration details to allow the Remote Control GUI to communicate from agency networks (or the public internet) to the C2C infrastructure.
    *   **Responsible:** System Integrator & Agency IT Departments.

---
*Document End*