# Software Requirements Specification (SRS)
## Correlator Monitor and Control System (CMCS)
### For the WIDAR Correlator, Expanded Very Large Array (EVLA)

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the Correlator Monitor and Control System (CMCS). The CMCS provides the physical link and primary software interface to configure, operate, and service the WIDAR Correlator hardware for the EVLA. It serves as a critical abstraction layer between the high-level EVLA Monitor & Control (M&C) system and the correlator hardware.

The intended audience for this document includes project managers, software architects, developers, testers, system engineers, and end-users (operators, technicians, administrators).

### 1.2 Scope
The CMCS is responsible for:
*   Translating high-level configuration from the EVLA M&C system into low-level hardware commands.
*   Handling real-time monitor and control data streams to and from the correlator hardware.
*   Monitoring the health and state of all correlator subsystems.
*   Performing automatic fault detection and recovery.
*   Providing limited real-time data processing and probing tools.
*   Managing interfaces with external data feeds (models, time standards, phase corrections).
*   Outputting specific data products to the Correlator Backend Data Processing System.

**Out of Scope:**
*   The design and specification of the WIDAR correlator hardware itself.
*   The backend data processing pipeline that receives CMCS output.
*   The high-level observation scheduling and control logic of the EVLA M&C system.

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **CMCS** | Correlator Monitor and Control System (the subject of this SRS). |
| **EVLA** | Expanded Very Large Array. |
| **WIDAR** | Wideband Interferometric Digital ARchitecture. |
| **M&C** | Monitor and Control. |
| **CMIB** | Correlator Monitor Interface Board (hardware module). |
| **PCI/ISA** | Peripheral Component Interconnect / Industry Standard Architecture (computer bus standards). |

### 1.4 References
*   EVLA System Architecture Description
*   WIDAR Correlator Hardware Technical Specifications
*   EVLA M&C System Interface Control Document

### 1.5 Overview
The remainder of this document is structured as follows:
*   **Section 2** provides a general description of the product, its functions, users, and constraints.
*   **Section 3** specifies the detailed functional requirements.
*   **Section 4** specifies the non-functional requirements.
*   **Appendix A** may include supplementary information.

## 2. Overall Description

### 2.1 Product Perspective
The CMCS is an integrated component within the hierarchical EVLA Monitor and Control structure. It acts as a modularizing abstraction layer, isolating the specifics of the correlator hardware from the broader telescope control environment.

**System Interfaces:**
1.  **EVLA M&C System:** The primary command source. Interface is over a dedicated, physically separate Ethernet/fiber network.
2.  **Correlator Backend Data Processing System:** The primary data sink for specific products. Interface is over a secondary virtual network.
3.  **Correlator Hardware:** The controlled equipment. Interface is via CMIB modules connected to carrier boards using PCI/ISA or serial/parallel busses.
4.  **External Data Servers:** For auxiliary data such as delay models, time standards (UTC), and phase corrections.

### 2.2 Product Functions
The core functions of the CMCS are:
1.  Configuration Translation
2.  Hardware State & Health Monitoring
3.  Real-time Data Processing & Transfer
4.  Automatic Fault Detection and Recovery
5.  Real-time Data Probing & Diagnostics
6.  Data Product Output Management
7.  External Data Feed Integration

### 2.3 User Characteristics
| User Class | Primary Interaction | Skill Level | Key Needs |
| :--- | :--- | :--- | :--- |
| **Array Operator** | Indirect, via EVLA M&C GUI. | High (telescope operations). | Clear status, error alerts, and high-level health summaries. |
| **Engineer/Technician** | Direct, using CMCS diagnostic tools. | Expert (hardware/software). | Detailed fault tracing to module level, remote inspection tools, maintenance controls. |
| **Software Developer** | Direct, via development and debugging interfaces. | Expert (software). | Remote access for debugging, logging, process control, and system testing. |
| **Administrator** | Direct, via system management interfaces. | Expert (system administration). | Full system control, user/role management, security configuration, log access. |

### 2.4 Constraints
1.  **Criticality Constraint:** The CMCS is a critical system. Its failure results in the loss of astronomical data.
2.  **Architectural Constraint:** The system must employ a master/slave network topology.
3.  **Network Constraint:** Networks for M&C and backend data must be isolated (physically or virtually).
4.  **Operational Constraint:** Software must be capable of running continuously between planned maintenance windows without requiring a full system restart.

### 2.5 Assumptions and Dependencies
*   **Assumption:** Configuration data received from the EVLA M&C system is syntactically and semantically valid.
*   **Assumption:** All required auxiliary data (e.g., geometric delay models) will be available from designated external servers.
*   **Assumption:** The Correlator Backend Data Processing System can accept the data rates and formats output by the CMCS.
*   **Dependency:** CMCS functionality is dependent on the stability and performance of its dedicated control computers and internal network.
*   **Dependency:** The system requires specific, timely data feeds from external systems (time, models, corrections).

## 3. Specific Requirements

### 3.1 External Interface Requirements
#### 3.1.1 EVLA M&C System Interface (IF-01)
*   **REQ-IF-01.1:** The CMCS shall receive observation configuration data (e.g., frequency setup, integration time) from the EVLA M&C system via a dedicated Ethernet/fiber network.
*   **REQ-IF-01.2:** The CMCS shall provide consolidated system status, health alerts, and acknowledgment messages back to the EVLA M&C system on the same network.

#### 3.1.2 Backend Data System Interface (IF-02)
*   **REQ-IF-02.1:** The CMCS shall output specific data sets (including but not limited to auto-correlation spectra) to the Correlator Backend Data Processing System via a secondary virtual network.
*   **REQ-IF-02.2:** The data output stream shall include necessary metadata (timestamp, configuration ID) synchronized with the data payload.

#### 3.1.3 Correlator Hardware Interface (IF-03)
*   **REQ-IF-03.1:** The CMCS shall communicate with all CMIB modules via the appropriate carrier board buses (PCI/ISA, serial, parallel).
*   **REQ-IF-03.2:** The system shall be able to address and control each hardware module individually.

### 3.2 Functional Requirements
#### 3.2.1 Configuration Management (FUN-01)
*   **REQ-FUN-01.1:** The system shall translate high-level observation configuration parameters from the EVLA M&C into a complete set of low-level register writes and commands for the correlator hardware.
*   **REQ-FUN-01.2:** The system shall validate the translated configuration for internal consistency before applying it to the hardware.
*   **REQ-FUN-01.3:** The system shall maintain and report the current active configuration state.

#### 3.2.2 Monitoring & Data Handling (FUN-02)
*   **REQ-FUN-02.1:** The system shall continuously monitor the state, health, and performance of all correlator subsystems (power, temperature, data flow, error flags).
*   **REQ-FUN-02.2:** The system shall process real-time control data (e.g., phase corrections) and apply them to the hardware within a specified deadline.
*   **REQ-FUN-02.3:** The system shall acquire, timestamp, and buffer monitor data from the hardware for internal use and external reporting.

#### 3.2.3 Fault Management & Recovery (FUN-03)
*   **REQ-FUN-03.1:** The system shall automatically detect faults in hardware modules, control processors, operating systems, and communication links.
*   **REQ-FUN-03.2:** Upon detection of a fault, the system shall first attempt automatic recovery (e.g., reset a module, restart a software process) without operator intervention.
*   **REQ-FUN-03.3:** All fault events and recovery attempts shall be logged with precise timestamps and severity levels.
*   **REQ-FUN-03.4:** If automatic recovery fails, the system shall escalate the fault to the EVLA M&C system and designated engineers.

#### 3.2.4 Diagnostics & Data Probing (FUN-04)
*   **REQ-FUN-04.1:** The system shall provide authorized engineers/developers with tools to remotely inspect the internal data flow of the correlator.
*   **REQ-FUN-04.2:** The system shall provide the capability to capture and display (e.g., via a GUI) real-time auto-correlation spectra from any designated antenna or baseline.
*   **REQ-FUN-04.3:** Diagnostic tools shall allow fault tracing down to the level of individual hardware modules (CMIBs).

#### 3.2.5 External Data Integration (FUN-05)
*   **REQ-FUN-05.1:** The system shall accept and integrate external data feeds, including delay models, time standard signals (e.g., 1PPS, UTC), and real-time phase corrections.
*   **REQ-FUN-05.2:** The system shall synchronize its internal operations and data timestamps with the provided time standard.

#### 3.2.6 System Management (FUN-06)
*   **REQ-FUN-06.1:** The system shall require all users to authenticate with a unique identifier and password.
*   **REQ-FUN-06.2:** The system shall enforce role-based access control (RBAC), with permissions for Operators, Engineers, Developers, and Administrators as defined in Section 2.3.
*   **REQ-FUN-06.3:** An Administrator shall have the ability to create, modify, and delete user accounts and assign roles.
*   **REQ-FUN-06.4:** Individual software processes shall be able to be killed and restarted remotely with minimal impact on other running processes and hardware.

### 3.3 Non-Functional Requirements

#### 3.3.1 Reliability & Availability (NF-01)
*   **REQ-NF-01.1:** The system shall achieve an operational availability of **99.95%** over any calendar month, excluding planned maintenance.
*   **REQ-NF-01.2:** The Mean Time Between Failures (MTBF) for software-caused system interruptions shall be greater than **1000 hours**.
*   **REQ-NF-01.3:** The system shall be designed to run continuously for a minimum of **90 days** without requiring a restart.

#### 3.3.2 Performance (NF-02)
*   **REQ-NF-02.1:** The system shall apply real-time control data (e.g., phase corrections) to the hardware with a latency of less than **10 milliseconds** from data receipt.
*   **REQ-NF-02.2:** The system shall respond to hardware interrupts within a deterministic, bounded timeframe specified in the hardware ICD to prevent data corruption.
*   **REQ-NF-02.3:** Health monitor data shall be polled, processed, and made available for internal alerts and external reporting at a minimum frequency of **1 Hz**.

#### 3.3.3 Security (NF-03)
*   **REQ-NF-03.1:** All network communication between the CMCS and external systems (EVLA M&C, Backend) shall be encrypted using industry-standard protocols (e.g., TLS).
*   **REQ-NF-03.2:** User sessions shall expire after a period of **15 minutes** of inactivity.
*   **REQ-NF-03.3:** All authentication attempts (successful and failed) shall be logged.

#### 3.3.4 Maintainability & Serviceability (NF-04)
*   **REQ-NF-04.1:** The software shall be modular, with clear APIs and logging, to facilitate debugging by developers.
*   **REQ-NF-04.2:** Hardware components shall be physically accessible and designed as Field-Replaceable Units (FRUs) where possible.
*   **REQ-NF-04.3:** The system shall support the hot-swapping of designated hardware modules and the restart of software subsystems without requiring a full system shutdown.

#### 3.3.5 Safety
*   *Not applicable for this software system. Safety is managed at the hardware/power level.*

## 4. Acceptance Criteria
Formal acceptance of the CMCS will require verification against the following key criteria:

1.  **Functional Correctness:** Successful demonstration of all requirements in Section 3.2 using test configurations and simulated hardware.
2.  **Interface Compliance:** Verification of correct data exchange and protocol adherence with the EVLA M&C and Backend system simulators.
3.  **Performance Validation:** Measurement and confirmation that real-time latency (REQ-NF-02.1) and interrupt handling deadlines are met under maximum load conditions.
4.  **Reliability Demonstration:** Execution of a sustained 30-day endurance test with simulated fault injection, meeting availability (REQ-NF-01.1) and MTBF targets.
5.  **Security Audit:** Successful penetration testing and validation of access controls (REQ-NF-03.1, REQ-NF-03.2) by an independent auditor.
6.  **Recovery Procedures:** Demonstration of automatic fault recovery (REQ-FUN-03.2) and manual process restart (REQ-FUN-06.4) without data loss or system crash.

---
*Document End*