# Software Requirements Specification (SRS)
## EVLA Correlator Monitor & Control System (CMCS)

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the EVLA Correlator Monitor & Control System (CMCS). The CMCS serves as the critical software and hardware interface between the WIDAR correlator hardware and the broader EVLA Monitor & Control (M&C) infrastructure. It is intended for use by project managers, system architects, software developers, testers, and stakeholders to guide the development, verification, and validation of the system.

#### 1.2 Scope
The CMCS is responsible for:
*   Translating high-level observation configurations from the EVLA M&C system into hardware-specific commands for the correlator.
*   Managing real-time monitoring data flows from hardware and controlling hardware states.
*   Ensuring system health through autonomous fault detection and recovery mechanisms.
*   Providing diagnostic and debugging tools for engineers and developers.
*   Outputting specific data products (e.g., auto-correlations, state counts) to the backend data processing system.

**Out of Scope:**
*   Direct scientific data processing (e.g., cross-correlation, fringe fitting).
*   Interpretation or correction of ambiguous or invalid configuration data from upstream systems.
*   Long-term archival of monitor data.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **CMCS:** Correlator Monitor & Control System.
*   **EVLA:** Expanded Very Large Array.
*   **M&C:** Monitor & Control.
*   **MCCC:** Master Correlator Control Computer.
*   **CMIB:** Correlator Monitor Interface Board.
*   **CPCC:** Correlator Power Control Computer.
*   **VCI:** Virtual Correlator Interface.
*   **COTS:** Commercial Off-The-Shelf.
*   **SLA:** Service Level Agreement.
*   **UTC:** Coordinated Universal Time.
*   **WIDAR:** Wideband Interferometric Digital ARchitecture.

#### 1.4 References
*   EVLA System Architecture Document
*   IEEE 802.3 Standard for Ethernet
*   PC104+ Specification

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its stakeholders, and operating environment. Section 3 details the specific functional and non-functional requirements. Appendices may contain supplementary diagrams or data models.

### 2. Overall Description

#### 2.1 Product Perspective
The CMCS is a subsystem within the larger EVLA correlator system. It acts as a middleware layer, isolating the real-time, deterministic hardware control plane from the higher-level network-based control and monitoring plane.

**System Context Diagram:**
```
[ EVLA M&C System ] <---(VCI/Status)---> [ MCCC (Primary/Backup) ] <---(Control/Monitor)---> [ CMIBs (xN) ] <---> [ Correlator Hardware ]
       ^                                                                         ^
       |                                                                         |
       |                                                                   (Data Output)
       |                                                                         v
       |                                                           [ Backend Data Processing ]
       |                                                                         ^
       |                                                                         |
       +-----------------------(Status/Errors)-----------------------------------+
```
*(Note: CPCC and test interfaces not shown for simplicity)*

#### 2.2 Stakeholders and User Classes
| Stakeholder | Role & Interest |
| :--- | :--- |
| **Array Operator** | Monitors overall system health and error messages via the EVLA M&C interface. Requires clear, actionable status summaries. |
| **Engineer/Technician** | Performs maintenance, diagnostics, and repair. Requires deep, remote access to hardware states and diagnostic tools. |
| **Software Developer** | Develops, debugs, and maintains CMCS software. Requires system access for debugging and logging. |
| **Authorized Web User** | Has restricted, read-only access to specific monitoring data (e.g., system health dashboard). |
| **EVLA M&C System** | External system providing configuration and receiving status. Acts as a user and data source. |
| **Backend Data System** | External system consuming specific data products (e.g., auto-correlations). |
| **System Administrator** | Manages user accounts, access privileges, and system software updates. |

#### 2.3 Operating Environment
*   **Hardware:** The system will operate on specialized hardware including the MCCC (COTS server), CMIBs (embedded PC104+ boards), and the CPCC.
*   **Software:** Will run on a real-time or general-purpose COTS operating system (TBD). Software will be developed in a language suitable for embedded and control applications (e.g., C, C++, Python).
*   **Networks:** Utilizes multiple, physically isolated networks: a control network (MCCC<->CMIB), a data output network, and an external communication network (to EVLA M&C).
*   **Physical:** Located in the EVLA correlator room, subject to standard data center environmental controls.

#### 2.4 Design and Implementation Constraints
1.  The CMIB form factor must comply with PC104+ standards.
2.  All network interfaces shall comply with IEEE 802.3 (Ethernet).
3.  The system must use a master/slave (MCCC/CMIB) architecture to enforce network isolation.
4.  Software must be developed with maintainability and readability as high priorities.

#### 2.5 Assumptions and Dependencies
1.  **AS-1:** The EVLA M&C system will provide unambiguous and valid configuration data.
2.  **AS-2:** The correlator hardware provides reliable hardware watchdogs and status registers.
3.  **DE-1:** The project is dependent on the timely delivery and specification of the correlator hardware.
4.  **DE-2:** The interfaces and protocols of the EVLA M&C system are stable and documented.

### 3. System Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Configuration Management
*   **REQ-F-1.1:** The MCCC shall receive observation configuration data from the EVLA M&C system via the Virtual Correlator Interface (VCI).
*   **REQ-F-1.2:** The MCCC shall validate the structure and completeness of incoming configuration data against a known schema.
*   **REQ-F-1.3:** The MCCC shall translate a validated configuration into hardware-specific control tables for each target CMIB and hardware board.
*   **REQ-F-1.4:** The MCCC shall distribute the generated control tables and any required auxiliary data (e.g., delay models) to the appropriate CMIBs.
*   **REQ-F-1.5:** Upon loss of communication with the EVLA M&C system, the CMCS shall continue operating using the last successfully applied configuration.

##### 3.1.2 Hardware Monitoring & Control
*   **REQ-F-2.1:** Each CMIB shall continuously monitor the health and status of its associated correlator hardware boards via hardware register reads.
*   **REQ-F-2.2:** Each CMIB shall report its status and hardware monitor data to the MCCC at a configurable rate.
*   **REQ-F-2.3:** The MCCC shall be capable of sending control commands (e.g., register writes, reboot signals) to any CMIB for execution on its hardware.
*   **REQ-F-2.4:** The system shall respond to hardware interrupts deterministically to prevent data loss.

##### 3.1.3 Fault Detection and Recovery
*   **REQ-F-3.1:** The MCCC shall detect a failed or unresponsive CMIB via heartbeat or status timeout.
*   **REQ-F-3.2:** Upon detecting a CMIB failure, the MCCC shall automatically attempt recovery by issuing a remote reboot command to that CMIB.
*   **REQ-F-3.3:** A successfully rebooted CMIB shall autonomously request and apply its last known configuration from the MCCC and resume normal operation.
*   **REQ-F-3.4:** If CMIB recovery fails after a defined number of attempts, the MCCC shall generate a high-severity alert for manual intervention.
*   **REQ-F-3.5:** The CPCC shall monitor the heartbeat of the primary MCCC.
*   **REQ-F-3.6:** Upon detection of a primary MCCC hard failure, the system shall activate the backup MCCC. The mechanism (auto/manual) is TBD (See Undecided Issues 2).
*   **REQ-F-3.7:** The backup MCCC shall maintain synchronized state with the primary to allow resumption of control with minimal disruption.

##### 3.1.4 Data Output
*   **REQ-F-4.1:** The MCCC shall package monitor data (e.g., state counts, auto-correlation products) as specified by the backend system.
*   **REQ-F-4.2:** The MCCC shall output the packaged data streams to the correlator backend data processing system over a dedicated network interface at requested rates.

##### 3.1.5 Status and Logging
*   **REQ-F-5.1:** The MCCC shall stream system status, health, and error messages to the EVLA M&C system.
*   **REQ-F-5.2:** All system events, errors, and inter-layer messages shall be timestamped with UTC.
*   **REQ-F-5.3:** All error and debug messages shall be accessible and filterable (by severity, source, etc.) at the MCCC layer. The schema is TBD (See Undecided Issues 7).

##### 3.1.6 Testing and Diagnostics
*   **REQ-F-6.1:** The system shall provide a test interface (e.g., GUI, command line) for authorized users to inject test configurations and direct commands.
*   **REQ-F-6.2:** The test interface shall provide real-time visibility into system traffic and debug information without disrupting ongoing operations.

##### 3.1.7 System Management
*   **REQ-F-7.1:** All user access to the CMCS (MCCC, CMIBs, test interface) shall require authentication via unique login credentials. The format is TBD (See Undecided Issues 8).
*   **REQ-F-7.2:** An administrator shall have the capability to create, modify, and delete user accounts and assign access privileges.
*   **REQ-F-7.3:** User passwords shall be stored in an encrypted format.

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance
*   **REQ-NF-1.1:** The MCCC and CMIB processors shall meet all defined real-time data processing deadlines for control and monitoring loops.
*   **REQ-NF-1.2:** The system's response to hardware interrupts shall be deterministic, with a bounded, specified maximum latency.

##### 3.2.2 Reliability & Availability
*   **REQ-NF-2.1:** The CMCS software shall be capable of running continuously between scheduled maintenance windows without requiring a full system restart.
*   **REQ-NF-2.2:** The system architecture shall support indefinite operation with no complete loss of correlator service, except in the case of a total facility power failure.
*   **REQ-NF-2.3:** The MCCC shall be implemented as a redundant pair to eliminate a single point of failure.

##### 3.2.3 Security
*   **REQ-NF-3.1:** Access to system control functions shall be restricted based on user privilege levels.
*   **REQ-NF-3.2:** All external network communications shall be conducted over isolated networks to minimize attack surface.

##### 3.2.4 Maintainability
*   **REQ-NF-4.1:** The hardware design shall be modular to allow for future scalability (e.g., adding CMIBs).
*   **REQ-NF-4.2:** Software shall be well-documented and follow readable coding standards to facilitate maintenance and upgrades.

##### 3.2.5 Compliance
*   **REQ-NF-5.1:** The system shall comply with relevant IEEE and PC104+ standards as specified in Section 2.4.

### 4. Interface Requirements

#### 4.1 Hardware Interfaces
*   **HI-1:** CMIB to Correlator Hardware Board: Defined by hardware register map (separate hardware spec).
*   **HI-2:** CPCC to Power Monitor/Control Bus: Protocol and medium TBD (See Undecided Issues 6).

#### 4.2 Software Interfaces
*   **SI-1: Virtual Correlator Interface (VCI).** Protocol and API for communication with EVLA M&C. Input: Configuration blocks. Output: Status/Error stream.
*   **SI-2: CMIB Control Protocol.** Internal protocol between MCCC and CMIBs for control table distribution, monitoring, and recovery commands.
*   **SI-3: Backend Data Interface.** Protocol for outputting data products (auto-correlations, state counts) to the backend system.
*   **SI-4: CPCC Failover Interface.** Redundant serial or network link for heartbeat and failover triggering between MCCC(s) and CPCC.

#### 4.3 Communication Interfaces
*   **CI-1:** Control Network (MCCC<->CMIBs). Isolated Ethernet.
*   **CI-2:** Data Output Network (MCCC->Backend). Isolated Ethernet.
*   **CI-3:** External Network (MCCC<->EVLA M&C). Standard site network.

### 5. Appendices

#### 5.1 Domain Model Summary
Key entities and their core attributes:
*   **Configuration:** `id`, `source`, `parameters`, `validity_timestamp`
*   **Control Table:** `id`, `target_hardware_id`, `config_data`, `generation_timestamp`
*   **CMIB:** `hardware_id`, `ip_address`, `status`, `associated_rack`
*   **Monitor Data:** `id`, `type`, `source`, `timestamp`, `payload`
*   **Error Message:** `id`, `severity`, `source`, `timestamp`, `description`, `ack_status`

#### 5.2 Acceptance Criteria (Verification)
*   **AC-1 (Configuration):** Given a valid configuration from EVLA M&C, when processed, then corresponding control tables are generated and received by target CMIBs.
*   **AC-2 (Fault Recovery):** Given a CMIB failure, when detected, then a remote reboot is attempted and the module reintegrates upon success.
*   **AC-3 (Failover):** Given a primary MCCC hard failure, when detected, then the backup MCCC is activated and assumes control with minimal data interruption.
*   **AC-4 (Data Output):** Given a backend request, when the system is operational, then the requested data stream is delivered at the specified rate.

#### 5.3 Undecided Issues & TBDs
| ID | Issue | Responsible Party |
| :--- | :--- | :--- |
| 1 | Actions for external systems upon CPCC hard failure. | System Architects |
| 2 | Automatic vs. manual backup MCCC activation mechanism. | Operations & Software Team |
| 3 | Acceptable delay to resume from standby idle mode. | Performance Team |
| 4 | Definition of "minimal impact" for process restart. | Software Development Team |
| 5 | Selection of COTS OS for CMIB/MCCC. | Software & Hardware Integration |
| 6 | Protocol/medium for Power Monitor/Control Bus. | Hardware Engineers |
| 7 | Schema for categorizing/filtering error messages. | Software Development Team |
| 8 | Format of unique user identification. | Security & Software Team |

---
*Document End*