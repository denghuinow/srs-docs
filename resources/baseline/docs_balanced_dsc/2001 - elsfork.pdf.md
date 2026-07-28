# Software Requirements Specification (SRS)
## Open Standard Wind Turbine Communication System

**Document ID:** SRS-WTCS-001  
**Version:** 1.0  
**Date:** [Date of Generation]  
**Status:** Draft for Review  
**Classification:** Public

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for a standardized, manufacturer-agnostic communication system for remote monitoring, control, and data acquisition (SCADA) of wind turbines and wind farms. The primary purpose is to establish an open standard to replace proprietary solutions, ensuring interoperability, reliability, and security in wind energy operations.

#### 1.2 Scope
This specification covers the data exchange and communication protocols between individual wind turbine controllers and remote supervisory systems (e.g., farm-level SCADA, owner/operator systems). It explicitly defines the interfaces, data models, and behaviors required for this exchange.

**In-Scope:**
*   Standardized data models for wind turbine parameters, alarms, events, and commands.
*   Communication services for real-time data, historical data retrieval, alarm handling, and command execution.
*   Security mechanisms for authentication, integrity, and optional confidentiality.
*   Definition of performance and reliability criteria.

**Out-of-Scope:**
*   Internal design and implementation of the wind turbine controller hardware or software.
*   Internal design and Human-Machine Interface (HMI) of the remote SCADA system.
*   Physical layer communication media specification (e.g., fiber, radio).
*   Detailed data dictionary for every possible turbine component (to be defined in a companion document).

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **SCADA** | Supervisory Control and Data Acquisition. |
| **HMI** | Human-Machine Interface. |
| **IEC** | International Electrotechnical Commission. |
| **OPC** | Open Platform Communications (formerly OLE for Process Control). |
| **PCC** | Point of Common Coupling. |
| **Analogue Signal** | A continuously variable measurement (e.g., wind speed, temperature, voltage). |
| **Binary Signal** | A two-state signal (e.g., circuit breaker status, turbine running/stopped). |
| **Gateway** | A device that translates between different communication protocols. |

#### 1.4 References
*   IEC 61400-25 (Series): Communications for monitoring and control of wind power plants.
*   IEC 61850: Communication networks and systems for power utility automation.
*   IEC 60870-5 (Series): Telecontrol equipment and systems.
*   Industry reports on wind farm interoperability (2000-2001).

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the system, its stakeholders, and operating environment. Section 3 details the specific functional requirements. Section 4 outlines the non-functional requirements. Appendices contain supporting information.

### 2. Overall Description

#### 2.1 Product Perspective
The Wind Turbine Communication System (WTCS) is a middleware layer that sits between the proprietary wind turbine controller and the open, standardized remote systems. It may be implemented as integrated software within the turbine controller or as a separate gateway device for legacy turbines.

```
[Remote SCADA / Operator System] <---(Open Standard Protocol)---> [WTCS Interface] <---(Proprietary/Standard)---> [Wind Turbine Controller & I/O]
                                                                         ^
                                                                         |
                                                                 [Legacy Turbine Gateway]
```

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Wind Turbine Operator** | Daily operational staff. Requires clear, immediate information for safe and efficient operation. | Remote control, real-time status, immediate alarm notification. |
| **Electrical System Operator** | Manages high-voltage transmission grid stability. Requires authority over active power control. | Send power set-points, receive grid compliance data. |
| **Electrical Network Operator** | Manages distribution network and connection at PCC. Focus on power quality and contractual compliance. | Periodic power quality measurements (voltage, frequency, harmonics). |
| **Owner / Asset Manager** | Financial and performance oversight. Focus on long-term trends and Return on Investment (ROI). | Historical production data, availability reports, energy counters. |
| **External Party (Vendor/Service)** | Third-party providing maintenance or specialized services. Requires limited, secure access. | Diagnostic data access, fault logs, conditional monitoring data. |

#### 2.3 Operating Environment
*   **Hardware:** Industrial-grade computing and networking equipment located within wind turbine nacelles and towers, subject to extreme environmental conditions.
*   **Software:** Real-time operating systems, protocol stacks, and application software running on turbine controllers and gateways.
*   **Physical Environment:** Wide temperature ranges (-30°C to +50°C), high humidity, salinity (coastal sites), and constant vibration.

#### 2.4 Design and Implementation Constraints
1.  **Interoperability Mandate:** Must adhere to open, internationally recognized standards where possible.
2.  **Safety Independence:** Communication system failure must not compromise the independent, hardwired safety systems of the turbine.
3.  **Legacy Support:** Must provide a defined path for integration with existing wind farms using proprietary protocols via gateways.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** A reliable underlying network infrastructure (corporate WAN, leased lines, radio) exists between the turbine and the control center.
*   **Dependency:** Final selection of a specific communication protocol (e.g., IEC 61850) will be made based on industry consensus and field test results.
*   **Dependency:** The development of a comprehensive data dictionary (logical node definitions, data attributes) will be completed in parallel.

### 3. Specific Requirements

#### 3.1 Functional Requirements

**3.1.1 Connection Management**
*   **FR-01:** The system shall establish a secure communication session between the remote system and the turbine controller upon request.
*   **FR-02:** The system shall authenticate the identity of the remote system before allowing data exchange or command execution.
*   **FR-03:** The system shall monitor the communication link and generate a local event upon connection loss or restoration.

**3.1.2 Data Acquisition & Transmission**
*   **FR-04:** The turbine controller shall collect analogue measurements (e.g., wind speed, power output, temperature) from sensors.
*   **FR-05:** The system shall transmit analogue measurements to the remote system **periodically**, with configurable intervals (e.g., 1-60 seconds). *Linked to User Story 6.*
*   **FR-06:** The system shall transmit binary status points (e.g., breaker status, turbine state) to the remote system **periodically** or **on change**.
*   **FR-07:** The system shall provide **on-demand** (polled) read access to any data point defined in the data model.

**3.1.3 Alarm and Event Handling**
*   **FR-08:** The system shall detect predefined fault conditions within the turbine controller. *Linked to User Story 1.*
*   **FR-09:** Upon detection, the system shall **spontaneously** (event-driven) transmit an alarm message to the remote system with severity, timestamp, and description.
*   **FR-10:** The system shall log all alarms and operational events (e.g., commands executed, mode changes) locally in a non-volatile event log.
*   **FR-11:** The remote system shall be able to acknowledge alarms, and this acknowledgment status shall be reflected at the turbine.

**3.1.4 Command and Control**
*   **FR-12:** The system shall receive control commands (e.g., START, STOP, SET ACTIVE POWER) from authenticated and authorized remote systems. *Linked to User Story 2 & 4.*
*   **FR-13:** The system shall validate the received command for legality and safety (e.g., not allowing a START if winds are above cut-out speed) before execution.
*   **FR-14:** The system shall send a positive or negative acknowledgment message back to the remote system for every command received.
*   **FR-15:** The source (operator ID) and timestamp of every executed command shall be recorded in the event log.

**3.1.5 Historical Data Retrieval**
*   **FR-16:** The system shall store historical time-series data (e.g., 10-minute averages of key parameters) and production counters locally. *Linked to User Story 3.*
*   **FR-17:** The system shall respond to historical data queries from the remote system, transferring data for specified parameters and time ranges.
*   **FR-18:** The system shall provide access to integrated counters (e.g., total energy produced in kWh, total operational hours).

**3.1.6 System Management**
*   **FR-19:** Authorized users shall be able to retrieve the current configuration and software version of the communication system.
*   **FR-20:** The system shall support secure, remote updates of configuration parameters (e.g., data reporting intervals, alarm setpoints).
*   **FR-21:** The system shall support secure, authenticated access for specific data sets to authorized external parties. *Linked to User Story 5.*

#### 3.2 Data Model Requirements
The system shall implement a logical data model based on the following core entities:

```javascript
// Example Object Definitions
WindTurbine {
    TurbineID: String,          // Unique identifier
    Status: Enum,               // Running, Stopped, Faulted, etc.
    Location: GeoCoordinates,
    Capacity: Float,            // kW or MW
    CommissionDate: Date
}

AnalogueSignal {
    SignalID: String,           // e.g., "WTG01.WindSpeed.Avg"
    Value: Float,
    Unit: String,               // e.g., "m/s"
    Timestamp: DateTime,
    Quality: Enum,              // Good, Invalid, Substituted, etc.
    AveragingMethod: String     // e.g., "10-min average"
}

BinaryCommand {
    CommandID: String,
    Type: Enum,                 // START, STOP, RESET, etc.
    Timestamp: DateTime,        // Time of issuance
    AcknowledgmentStatus: Enum, // Pending, Accepted, Rejected
    Source: String              // ID of issuing operator/system
}

Alarm {
    AlarmID: String,
    TriggerCondition: String,   // Logical condition
    Severity: Enum,             // Critical, Major, Minor, Warning
    Timestamp: DateTime,        // Time of activation
    AcknowledgmentStatus: Enum, // Unacknowledged, Acknowledged
    Description: String
}
```

#### 3.3 Interface Requirements
*   **3.3.1 Communication Interface:** Shall support a client-server or publisher-subscriber model over TCP/IP.
*   **3.3.2 Protocol:** Shall implement an application-layer protocol supporting the services defined in Section 3.1. Specific protocol (e.g., MMS from IEC 61850, OPC DA/UA) is TBD (See Undecided Issues).
*   **3.3.3 Gateway Interface:** A legacy gateway shall provide a well-defined mapping between the proprietary turbine protocol and the standard WTCS protocol and data model.

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
*   **PER-01:** The end-to-end transfer time for time-critical commands (e.g., STOP, power set-point) from the remote system HMI to execution at the turbine shall be ≤ **500 ms** under normal network conditions.
*   **PER-02:** The system shall support concurrent communication sessions with multiple remote clients (≥ 5).
*   **PER-03:** The system shall be capable of handling a minimum data throughput of 100 data points per second per turbine during bulk historical data transfers.

#### 4.2 Safety & Reliability Requirements
*   **REL-01:** A failure of the WTCS shall not prevent the wind turbine's independent safety system from executing a safe shutdown.
*   **REL-02:** The communication system shall have a Mean Time Between Failures (MTBF) of > 50,000 hours.
*   **REL-03:** Data integrity shall be ensured through message checksums or cryptographic hashes.

#### 4.3 Security Requirements
*   **SEC-01:** All communication sessions shall require authentication using strong credentials (e.g., certificates, secure passwords).
*   **SEC-02:** The system shall enforce role-based access control (RBAC), differentiating between operators, system operators, and vendors.
*   **SEC-03:** Data integrity shall be protected for all messages. Confidentiality (encryption) shall be supported as an optional feature for sensitive command and data traffic.
*   **SEC-04:** The system shall audit and log all authentication attempts (successful and failed).

#### 4.4 Availability Requirements
*   **AVA-01:** The communication system software shall have an availability of 99.5% or higher.
*   **AVA-02:** The design shall support redundant communication channels (e.g., primary and backup network links) to prevent data loss during single-path failures.

#### 4.5 Environmental Requirements
*   **ENV-01:** All hardware components of the WTCS located in the turbine nacelle shall be rated for operation in temperatures from **-30°C to +55°C**.
*   **ENV-02:** Hardware shall be protected against humidity, salt mist, and vibration as per IEC 61400-1 standards for wind turbine components.

### 5. Appendices

#### Appendix A: User Story Mapping
| User Story | Mapped Functional Requirements |
| :--- | :--- |
| 1. Receive immediate alarms | FR-08, FR-09 |
| 2. Send set-point commands | FR-12, FR-13, FR-14 |
| 3. Retrieve historical counters | FR-16, FR-17, FR-18 |
| 4. Remote start/stop | FR-12, FR-13, FR-14 |
| 5. Secure external access | FR-02, FR-21, SEC-02 |
| 6. Periodic analogue updates | FR-04, FR-05 |

#### Appendix B: Undecided Issues & TBD
1.  **Protocol Selection:** Final recommendation between IEC 61850-7-420, OPC UA, or a derivative is pending field test results and industry working group consensus.
2.  **Data Dictionary:** A companion document, "WTCS Data Dictionary," will define the specific `SignalID` naming conventions and logical nodes for all common turbine components.
3.  **Encryption Standard:** Specific algorithms and key management protocols for optional encryption are to be defined (e.g., TLS 1.2+, AES-256).
4.  **Redundancy Cost-Benefit:** Guidelines for implementing requirement AVA-02 will be developed, considering farm size and criticality.
5.  **Condition Monitoring:** Requirements for standardizing vibration, oil analysis, and other condition monitoring data formats and transmission will be addressed in a future revision.
6.  **Secondary Systems:** Interfaces for meteorological masts, fire alarms, and CCTV will be scoped in a separate integration specification.

---
*Document End*