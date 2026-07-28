# Software Requirements Specification (SRS)
## Standardized Wind Turbine Communication System (SWTCS)
**Document Version:** 1.0
**Date:** [Date of Generation]
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Standardized Wind Turbine Communication System (SWTCS). The purpose is to establish a vendor-independent, reliable, and secure communication framework between wind turbine controllers and remote Supervisory Control and Data Acquisition (SCADA) systems. This SRS serves as the definitive specification for developers, system integrators, and stakeholders.

#### 1.2 Scope
The SWTCS encompasses the protocols, services, data structures, and management functions required for standardized remote monitoring and control of wind turbines and wind farms. It focuses on the communication layer, ensuring interoperability between heterogeneous turbine controllers and SCADA systems.

**In-Scope Elements:**
*   Communication protocols and data exchange mechanisms.
*   Definition of operational data points, commands, and alarms.
*   System management functions (configuration, user management, diagnostics).
*   Communication services (authentication, secure session handling, reliable data transfer).
*   A standardized, hierarchical data model for wind turbine assets.

**Out-of-Scope Elements:**
*   Internal SCADA system design, HMI layout, or proprietary control algorithms.
*   Local engineering or maintenance interfaces (e.g., direct PC connections).
*   Voice or video communication subsystems.
*   Functions specific to actors not directly involved in plant operation (e.g., accounting systems).
*   Safety-critical control functions, which must remain localized within the turbine controller.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **SCADA** | Supervisory Control and Data Acquisition |
| **HMI** | Human-Machine Interface |
| **OPC** | Open Platform Communications (a series of standards) |
| **IEC** | International Electrotechnical Commission |
| **WAN** | Wide Area Network |
| **LAN** | Local Area Network |
| **QoS** | Quality of Service |
| **UTC** | Coordinated Universal Time |

#### 1.4 References
*   IEC 61400-25 Series: Communications for monitoring and control of wind power plants.
*   IEC 60870-5 / IEC 61850: Telecontrol and substation automation standards.
*   OPC UA (Unified Architecture) Specification.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its stakeholders, and operating environment. Section 3 details the specific functional and non-functional requirements. Appendices contain supporting information.

### 2. Overall Description

#### 2.1 Product Perspective
The SWTCS is a middleware layer that sits between wind turbine controllers (from various manufacturers) and one or more SCADA systems. It acts as a translator and secure gateway, abstracting proprietary protocols into a standardized interface. For legacy installations, a Gateway component is implied.

#### 2.2 Product Functions (High-Level)
1.  **Data Acquisition:** Periodically and on-demand collection of real-time operational data from turbines.
2.  **Command Transmission:** Secure and validated transmission of control commands (e.g., start, stop, setpoints) to turbines.
3.  **Event & Alarm Handling:** Reliable reporting of turbine alarms and status changes with time stamps.
4.  **Historical Data Retrieval:** Access to logged operational data for analysis.
5.  **System Management:** Configuration, user access control, and system health monitoring.
6.  **Time Synchronization:** Distribution of precise time references to all system components.

#### 2.3 User Characteristics
| Stakeholder | Role & Expertise |
| :--- | :--- |
| **Wind Turbine Operator** | Daily operational oversight. Requires clear presentation of real-time status and alarms. |
| **Control Center Operator** | Grid-focused. Issues fleet-wide commands and setpoints. Understands grid codes. |
| **Maintenance Technician** | Technical expert. Needs detailed historical data, event logs, and diagnostic access. |
| **System Administrator** | IT/OT expert. Manages system configuration, user accounts, and network security. |
| **Owner / Manager** | Financial/performance focus. Requires high-level KPIs, production reports, and availability metrics. |
| **Electrical Network Operator** | External entity. Receives specific grid compliance data (power quality, connection status). |

#### 2.4 Constraints
1.  **Safety Independence:** A failure in the SWTCS must not induce a failure in the turbine's internal safety system.
2.  **Environmental:** Hardware components must be rated for operation in extreme conditions typical of wind turbine nacelles and sites (temperature: -40°C to +70°C, high humidity, vibration).
3.  **Backward Compatibility:** The design must facilitate integration with existing wind power plants via gateway solutions.
4.  **Performance:** Time synchronization accuracy across the system shall be ≥ 10 ms.
5.  **Reliability:** The architecture must support redundant communication paths (e.g., primary and backup WAN links).

#### 2.5 Assumptions and Dependencies
*   It is assumed that a reliable network infrastructure (corporate WAN, leased lines, etc.) is provided.
*   The wind turbine controller provides a stable, documented data interface (even if proprietary).
*   Success depends on vendor adoption of the defined standardized data model.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Data Acquisition & Monitoring (FR-MON)
*   **FR-MON-001:** The system shall acquire real-time data from all configured wind turbines at a configurable sampling rate (1-10 seconds).
*   **FR-MON-002:** The system shall support both cyclic (polled) and report-by-exception (unsolicited) data transmission modes.
*   **FR-MON-003:** The system shall provide access to a minimum dataset per turbine including:
    *   Active Power (kW)
    *   Wind Speed (m/s)
    *   Rotor Speed (rpm)
    *   Generator Speed (rpm)
    *   Blade Pitch Angle (degrees)
    *   Nacelle Position (degrees)
    *   Operational State (e.g., Running, Stopped, Faulted)
    *   Internal Component Temperatures
    *   Production Counter (kWh)

##### 3.1.2 Control & Commanding (FR-CTRL)
*   **FR-CTRL-001:** The system shall transmit discrete commands to a turbine, including `START`, `STOP`, `RESET`, and `EMERGENCY STOP` (with appropriate safety permissions).
*   **FR-CTRL-002:** The system shall transmit analog setpoints, such as Active Power Reference (kW) and Reactive Power Reference (kVAr).
*   **FR-CTRL-003:** All commands shall require positive confirmation from the turbine controller before being considered executed.
*   **FR-CTRL-004:** The system shall validate all commands against the current turbine state and operational limits before transmission (e.g., cannot send `START` if turbine is already running).

##### 3.1.3 Event & Alarm Handling (FR-EVT)
*   **FR-EVT-001:** The system shall receive and time-stamp (with source timestamp if available, otherwise system timestamp) all alarm and event messages from turbines.
*   **FR-EVT-002:** Alarms shall be categorized by severity (e.g., Critical, Major, Minor, Informational).
*   **FR-EVT-003:** The system shall buffer events during communication loss and forward them upon restoration.

##### 3.1.4 Historical Data & Logging (FR-HIST)
*   **FR-HIST-001:** The system shall store or provide access to historical time-series data for a minimum of 365 days.
*   **FR-HIST-002:** The system shall allow retrieval of historical data based on user-defined filters (turbine ID, data point, time range, aggregation interval).

##### 3.1.5 System Management (FR-MGMT)
*   **FR-MGMT-001:** The system shall provide role-based access control (RBAC) with configurable user roles (Viewer, Operator, Administrator, etc.).
*   **FR-MGMT-002:** The system shall allow remote configuration of data points, sampling rates, and communication parameters.
*   **FR-MGMT-003:** The system shall monitor the health and status of all communication channels and report failures.

##### 3.1.6 Data Model & Naming (FR-DATA)
*   **FR-DATA-001:** The system shall implement a hierarchical naming convention for all data points (e.g., `WindFarm/WF01/Turbine/T001/Generator/ActivePower`).
*   **FR-DATA-002:** Each data point shall have associated metadata: Engineering Units, Data Type (Float, Integer, Boolean, String), Min/Max Range, and Access Level (Read-Only, Read-Write).

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance Requirements
*   **NFR-PER-001:** The overall transfer time (from command initiation at SCADA to receipt of confirmation from turbine) for time-critical functions shall be ≤ 0.5 seconds under normal network conditions.
*   **NFR-PER-002:** The system shall support a minimum of 500 concurrent data points updating at a 1-second cycle.
*   **NFR-PER-003:** Time synchronization across all system nodes shall have an accuracy of ≥ 10 ms relative to a UTC source.

##### 3.2.2 Reliability & Availability
*   **NFR-REL-001:** The communication system shall achieve an availability of 99.5% to support continuous remote operation.
*   **NFR-REL-002:** The system design shall allow for redundant communication paths to critical components.

##### 3.2.3 Security Requirements
*   **NFR-SEC-001:** All external communication (between plant and control center) shall support encryption (TLS 1.2 or higher).
*   **NFR-SEC-002:** The system shall authenticate all client connections (SCADA systems, users).
*   **NFR-SEC-003:** The system shall maintain an audit log of all user actions, especially control commands and configuration changes.

##### 3.2.4 Data Integrity
*   **NFR-INT-001:** The system shall employ message integrity checks (e.g., CRCs, cryptographic hashes) to ensure data is not corrupted in transit.
*   **NFR-INT-002:** The residual undetected error rate for data transmission shall be less than 10^-9.

#### 3.3 Interface Requirements
*   **IR-001 SCADA Interface:** The system shall provide a northbound interface to SCADA systems using a standardized protocol (e.g., OPC UA, IEC 61400-25 MMS). *[See Undecided Issues]*
*   **IR-002 Turbine Interface:** The system shall include southbound adapters capable of interfacing with common proprietary turbine protocols (Modbus TCP, Siemens S7, etc.).
*   **IR-003 Time Server Interface:** The system shall support connecting to an NTP or PTP (IEEE 1588) time server.

### 4. Appendices

#### Appendix A: Undecided Issues & TBD
The following items require further architectural decision or stakeholder agreement:
1.  **Protocol Standard:** Final selection between OPC UA, IEC 61400-25, or a hybrid approach.
2.  **Encryption Depth:** Whether to enforce end-to-end encryption or only for WAN segments.
3.  **Network Topology:** Detailed specifications for star, ring, or hybrid topologies for different farm sizes.
4.  **Message Prioritization:** Definition of QoS classes and prioritization schemes for mixed traffic (alarms vs. data).
5.  **Full Data Dictionary:** Completion of the exhaustive list of data points for all turbine subsystems (gearbox, yaw, hydraulics, converter, etc.).

#### Appendix B: Core Use Case Elaboration
**Use Case UC-001: Monitor Real-Time Operational Data**
*   **Actor:** Wind Turbine Operator
*   **Precondition:** Operator is logged in with 'Operator' or 'Viewer' role. Turbines are online.
*   **Main Flow:**
    1.  Operator requests the overview display for a wind farm.
    2.  System presents a list of turbines with key status (State, Power, Wind Speed).
    3.  Operator selects a specific turbine for detailed view.
    4.  System retrieves and displays the full real-time dataset for that turbine.
    5.  Data continues to update at the configured rate.
*   **Postcondition:** Operator is actively monitoring turbine performance.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Architect | | | |
| Quality Assurance | | | |