# Software Requirements Specification (SRS)
## Gemini 8-Meter Telescopes Control System
**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the operational and functional requirements for the Gemini Control System (GCS) software. It serves as the primary guide for the design, development, and validation of the controls and data acquisition systems for the Gemini 8-meter Telescopes. The intended audience includes software architects, developers, testers, and project managers.

#### 1.2 Scope
The scope of this document encompasses the non-commercial software developed for the integrated control of the telescope and its instruments, including:
*   The Observatory Control System (OCS), Sequencer, and Scheduler.
*   Telescope Control Software (TCS) and Instrument Control Software (ICS).
*   User interfaces for observation and monitoring.
*   Interfaces to commercial software packages (e.g., EPICS, data analysis tools).
*   Integration with external systems (e.g., archive, star catalogs, time reference).

**Out of Scope:**
*   Detailed field-level implementation specifics for individual hardware components.
*   The development of commercial or public-domain software packages themselves (e.g., EPICS core, PV-Wave).
*   Detailed mechanical or electrical engineering specifications.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **EPICS:** Experimental Physics and Industrial Control System.
*   **FITS:** Flexible Image Transport System.
*   **GCS:** Gemini Control System.
*   **GUI/CLUI:** Graphical User Interface / Command-Line User Interface.
*   **ICS:** Instrument Control Software.
*   **IOC:** Input/Output Controller (EPICS server).
*   **OCS:** Observatory Control System.
*   **OPI:** Operator Interface (EPICS client).
*   **SLA:** Service Level Agreement.
*   **TCS:** Telescope Control Software.
*   **TPS:** Transactions Per Second.
*   **WAN:** Wide Area Network.

#### 1.4 References
*   EPICS Official Documentation.
*   FITS Standard, NASA/Science Office of Standards and Technology.
*   POSIX (IEEE Std 1003.1) Operating System Interface Standard.
*   Gemini Observatory Operational Policies.

#### 1.5 Document Overview
This document is structured to present stakeholder needs, system functionality, data models, interfaces, and quality requirements. Subsequent sections detail use cases, functional requirements, domain information, external interfaces, and non-functional constraints.

### 2. Overall Description

#### 2.1 Product Perspective
The GCS is the central, integrated software system that commands, coordinates, and monitors all telescope and instrument subsystems. It operates within a distributed computing environment, interacting with multiple external entities as shown in the context diagram below.

```
[ Astronomer / Observer / Operator ] <--> [ User Interface ] <--> [ Observatory Control System (OCS) ]
                                                                          |
                                                                          v
[ Archive System ] <-- [ Data Flow ] -- [ OCS ] -- [ Commands/Status ] --> [ EPICS IOCs (TCS, ICS, Detectors) ]
                                                                          |
                                                                          v
[ Quick-Look Tools ] <-- [ Data ] -- [ System Disks ] <-- [ Engineering Data ] -- [ Time Ref, Star Catalogs, Visitor Inst. ]
```

#### 2.2 Stakeholders and User Classes
| User Class | Description | Key Requirements |
| :--- | :--- | :--- |
| **Astronomer** | End-user proposing science. May be remote. | Simple, safe interface for data collection and quality assessment. No direct control. |
| **Science Observer** | On-site staff monitoring data acquisition. | Observing and monitoring access. Validate data integrity. |
| **Telescope Operator** | On-site controller for telescope/instrument integrity. | Direct control, monitoring, operation, and testing privileges. |
| **Support Personnel** | On/near-site maintenance staff. | Full monitoring, operation, and testing access for maintenance. |
| **Developer** | Personnel designing/testing subsystems. | Full monitoring and testing access during maintenance/test levels. |
| **Administrator** | Personnel for high-level functional control. | Monitoring and administrative inquiry access only. |

#### 2.3 Operating Environment
*   **Hardware:** Distributed workstations, real-time IOCs (VME/VXI), detector controllers, network infrastructure.
*   **Software:** POSIX-compliant OS (e.g., Unix), EPICS core runtime, Tcl/Tk or equivalent for GUI, support for IDL/PV-Wave.
*   **Networks:** High-speed local network (LAN) for control and data, WAN connections for remote operations, isolated control loops where necessary.

### 3. System Features and Requirements

#### 3.1 Feature: Queue-Based Observing Execution
**Description:** The system shall automatically execute pre-defined Science Programs from a queue, driven by environmental conditions and priority rules.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-01** | The Scheduler shall evaluate site conditions (e.g., seeing, cloud cover, humidity) against the requirements of queued Science Programs. | High |
| **FR-02** | The Scheduler shall dispatch the highest-priority feasible Science Program to the Sequencer. | High |
| **FR-03** | The Sequencer shall interpret the executable steps of a Science Program. | High |
| **FR-04** | The Sequencer shall validate and send commands to the OCS for execution. | High |
| **FR-05** | The system shall support preemption of an executing observation if a higher-priority program becomes feasible, following defined observatory rules. | Medium |

#### 3.2 Feature: Interactive Observing
**Description:** The system shall allow authorized users to submit immediate commands for execution, mediated by the OCS and Sequencer.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-06** | The User Interface shall provide a mechanism for submitting immediate (interactive) commands to the OCS. | High |
| **FR-07** | The OCS shall validate interactive commands against the user's role and current system state. | High |
| **FR-08** | The Sequencer shall operate in a "pass-through" mode to execute validated interactive commands immediately, bypassing the queue. | High |

#### 3.3 Feature: Data Acquisition and Archiving
**Description:** The system shall acquire detector data, perform basic pre-processing, allow for quick-look assessment, and automatically archive final data products.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-09** | The ICS shall acquire data from detectors and perform initial storage within the IOC. | High |
| **FR-10** | The system shall transfer acquired data to designated system disks for quick-look assessment within seconds of readout completion. | High |
| **FR-11** | The system shall automatically format science data into FITS format with complete header metadata (including observation parameters and system status). | High |
| **FR-12** | The system shall transfer completed FITS data products to the external archive system during the observing night. | High |
| **FR-13** | Data shall remain accessible on local system disks for interactive analysis for a minimum of 7 days. | Medium |

#### 3.4 Feature: Fault Detection and Recovery
**Description:** The system shall monitor subsystem health, detect errors, notify operators, and support reconfiguration for degraded operation or safe shutdown.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-14** | All subsystems shall report health metrics and alarm conditions to the OCS/engineering log. | High |
| **FR-15** | The OCS shall notify the Telescope Operator immediately upon detection of a serious error or alarm. | High |
| **FR-16** | Upon a non-critical subsystem failure, the system shall support operator-initiated reconfiguration (e.g., switching to a backup instrument) to continue observing with degraded performance. | High |
| **FR-17** | Upon a fatal error, the system shall move the affected subsystem(s) to a predefined safe state. | High |
| **FR-18** | The system shall log sufficient diagnostic information (state, commands, parameters) prior to a fault to enable post-mortem analysis. | High |

#### 3.5 Feature: System Monitoring and Logging
**Description:** The system shall provide comprehensive status displays and maintain detailed logs of all commands and system events.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-19** | The User Interface shall provide real-time status displays for all major subsystems, tailored to the user's access mode. | High |
| **FR-20** | The system shall log every command issued with a unique ID, timestamp, source, target, and parameters. | High |
| **FR-21** | The system shall maintain an engineering log capable of recording parameter values at rates up to 200 Hz for diagnostic purposes. | Medium |
| **FR-22** | Logs shall be sufficient to reconstruct the complete sequence of events for any observation. | High |

#### 3.6 Feature: Access Control and Security
**Description:** The system shall enforce role-based privileges and protect system integrity through Access Mode Allocation and network security.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-23** | User authentication shall be required to obtain any access level. | High |
| **FR-24** | System privileges (Monitor, Observe, Operate, Test, Administer) shall be assigned based on user role (see 2.2). | High |
| **FR-25** | The Access Mode Allocation mechanism shall prevent privilege deadlock (e.g., two users requiring exclusive control of the same resource). | Medium |
| **FR-26** | WAN connections shall be mediated by firewalls or secure gateways. | High |

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Type:** Graphical (primary) and Command-Line.
*   **Toolkit:** Portable (e.g., Tcl/Tk on X11).
*   **Requirements:** Homogeneous look-and-feel across all subsystems. Interface presentation shall reflect the user's current access mode (e.g., controls disabled for monitors).
*   **Performance:** Command acceptance/rejection feedback within 2 seconds. Status updates within 4 seconds for local users.

#### 4.2 Hardware Interfaces
*   **Time Reference:** Input of IRIG-B time signals to all IOCs for synchronization.
*   **Detector Controllers:** High-speed link for data transfer (specific protocol TBD by Hardware/Network Team).
*   **Limit Switches/Interlocks:** Hardware signals for independent safety systems.

#### 4.3 Software Interfaces
| Interface | Direction | Protocol/Standard | Key Requirement |
| :--- | :--- | :--- | :--- |
| **EPICS Channel Access** | Bidirectional | EPICS CA | Network-transparent control/monitoring. Support peak load of 100 TPS. Handshaking <200ms. |
| **Archive System** | Outbound | FITS Format | Automatic ingestion of data products with headers. |
| **Quick-Look Analysis** | Inbound | File/Stream | Provide data in a format readable by IDL/PV-Wave for concurrent analysis. |
| **Star Catalogs** | Inbound | Query Protocol (TBD) | Provide candidate guide/standard stars based on position/magnitude queries. |
| **Visitor Instrument** | Bidirectional | Standardized Subset of Gemini ICS API | Support status exchange and basic commanding. |

#### 4.4 Communications Interfaces
*   **Local Network (LAN):** High-bandwidth, low-latency network for real-time control and data flow. Design must include redundancy (e.g., double loops) for critical paths.
*   **Wide Area Network (WAN):** For remote operations. Software shall be bandwidth-aware, employing data compression where possible.

### 5. Non-Functional Requirements

#### 5.1 Performance
*   The control system shall handle a peak information load of **100 transactions per second**.
*   Detector readout times shall range from **0.1 seconds** (for small focusing arrays) to **2-3 minutes** (for full mosaic readouts).
*   Remote UI updates shall be within limits defined by available WAN bandwidth.

#### 5.2 Reliability, Availability, and Maintainability
*   **Availability:** Total system downtime shall not exceed **1%** of scheduled observing time (approximately ≤1 night per month).
*   **Recovery Time:** The system shall support reconfiguration and recovery from a non-fatal error within **5 minutes** of error onset.
*   **Testability:** Subsystem design shall include Built-In Test (BIT) aiming for **≥90% fault detection** before impact on science data.

#### 5.3 Safety and Security
*   **Safety:** A hierarchical safety system shall be implemented: 1) Independent hardware interlocks, 2) Hard software limit switches, 3) Soft software limit switches, 4) Application-level limits.
*   **Security:** Control networks shall be isolated where possible. All external access (WAN) shall traverse secured gateways.

#### 5.4 Compliance
*   The software shall adhere to **POSIX** standards for operating system calls.
*   All archived and externally transported science data shall comply with the **FITS** standard.

### 6. Data Model and Domain Information
Core entities for system design:
*   **Science Program:** `Program_ID`, Astronomer_ID, Priority, Target_List, Instrument_Configurations, Observing_Sequence.
*   **Observation:** `Obs_ID`, Timestamp, Science_Program_ID, Instrument_ID, Exposure_Parameters, Data_Quality_Flags.
*   **Subsystem:** `Subsystem_ID`, Status (RUNNING, STANDBY, FAULT, MAINTENANCE), Configuration_Version, Health_Metrics.
*   **User:** `User_ID`, Role, Current_Access_Mode, Assigned_Privileges.
*   **Command:** `Command_ID` (timestamped), Source_User, Target, Opcode, Parameter_Set, Status.
*   **Data Product:** `Data_ID`, Observation_ID, Format, Storage_Location, Compression_Flag.
*   **Engineering Log:** `Log_ID`, Subsystem_ID, Timestamp, Parameter_Name, Value, Log_Level (INFO, WARNING, ERROR, FATAL).

### 7. Acceptance Criteria
The system will be considered acceptable when it successfully passes test scenarios demonstrating the following capabilities:
1.  **Queue Scheduling:** Given a queue with multiple valid Science Programs, the system shall correctly select and execute the highest-priority feasible program.
2.  **Remote Monitoring:** A remote user with monitoring privileges shall be able to view real-time status and data images without causing any interruption to the active observation.
3.  **Fault Tolerance:** Upon simulated failure of a non-critical component (e.g., a guide camera), the system shall alert the operator and allow observation to continue using an alternative resource (e.g., a different guide probe).
4.  **Multi-Instrument Operation:** While one instrument is acquiring a science exposure, calibration commands (e.g., moving a filter wheel) shall be executable on a different, mounted instrument without affecting the ongoing exposure.

### 8. Project Planning Appendices

#### 8.1 Milestones and Release Strategy
1.  **Milestone 1:** Core OCS and Sequencer ("pass-through" mode).
2.  **Milestone 2:** Integration of TCS and first ICS via EPICS.
3.  **Milestone 3:** Basic Interactive Observing from on-site control room.
4.  **Milestone 4:** Queue-Based Observing and Science Program preparation.
5.  **Milestone 5:** Remote Operations (monitoring, then observing).
6.  **Milestone 6 (Future):** Advanced Scheduler for Flexible Scheduling.

#### 8.2 Risk Management
| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| Complexity of scheduling software | Medium | High | Phased delivery. Implement basic sequencer first; design modular interfaces for future advanced scheduler. |
| WAN bandwidth limitations | High | Medium | Design bandwidth-aware software with data compression. Define and enforce minimum link specifications. |
| Visitor instrument integration challenges | High | Medium | Publish a clear, stable standard interface. Offer enhanced integration support on a collaborative basis. |
| Single points of failure in network/IOCs | Medium | High | Design redundant network paths. Maintain spares for critical hardware. Establish fast replacement procedures. |

#### 8.3 Open Issues and TBDs
1.  **G8MT Detector Data Standard:** Definition for acquisition and storage. *(Owner: Data Flow Working Group)*
2.  **Detector Data Link:** Final choice of hardware link and protocol. *(Owner: Hardware/Network Team)*
3.  **IOC/Workstation Hardware Spec:** Detailed specifications. *(Owner: Systems Engineering)*
4.  **Software Development Standards:** Details for online software and dev environment. *(Owner: Software Standards Committee)*
5.  **Star Catalog Access:** Specific protocols and descriptions. *(Owner: Archive/Science Operations Team)*
6.  **Scheduling Algorithms:** Detailed rules for expert scheduler. *(Owner: Science Operations & Software Dev)*
7.  **Command Timeouts/Retries:** Specific values and protocols for all interactions. *(Owner: OCS & ICS Development Teams)*

---
*Document End*