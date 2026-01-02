# Software Requirements Specification (SRS)
## For the WIDAR Correlator Monitor & Control Interface System (MCCIS)

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the WIDAR Correlator Monitor & Control Interface System (MCCIS). This system serves as the critical bridge between the EVLA (Expanded Very Large Array) Monitor & Control (M&C) software and the WIDAR correlator hardware. The primary purpose of this document is to provide a complete description of the system's capabilities, interfaces, and performance characteristics to serve as a basis for design, implementation, and verification.

#### 1.2 Document Conventions
*   Requirements are uniquely identified with tags (e.g., `FR-001`, `NFR-010`).
*   **Shall** indicates a mandatory requirement.
*   **Should** indicates a desirable, but not mandatory, feature.
*   *Italicized text* provides explanatory notes.
*   This document uses Markdown formatting for clarity.

#### 1.3 Scope
The MCCIS provides the physical link and primary software interface between the WIDAR Correlator hardware and the EVLA monitor & control system for configuration, operation, and servicing. The system resides logically and physically between the EVLA M&C network and the correlator hardware subsystems within a shielded room. The scope includes:
*   Software services for configuration translation, command processing, and data monitoring.
*   Network interface management adhering to specified constraints.
*   Health monitoring and autonomous fault recovery logic.
*   It does **not** include the EVLA M&C system itself, the WIDAR correlator digital signal processing algorithms, or the astronomical data pipeline.

#### 1.4 References
*   IEEE Std 802.3-2018 - Ethernet Standard
*   EVLA M&C System Interface Control Document (ICD)
*   WIDAR Correlator Hardware Specifications

### 2. Overall Description

#### 2.1 Product Perspective
The MCCIS is a subsystem of the larger EVLA observatory control system. It acts as a middleware component, insulating the high-level, astronomy-focused M&C system from the low-level details of the correlator hardware.

**System Context Diagram:**
```
[ EVLA M&C System ] <---(Ethernet/Fiber)---> [ MCCIS ] <---(Internal Links)---> [ WIDAR Hardware ]
      (External)       (Config, Control,          |        (Hardware-specific
                       Monitor Data)              |         commands, telemetry)
                                                   |
                                            [ Health DB/Logs ]
```

#### 2.2 Product Functions
The core functions of the MCCIS are:
1.  **Configuration Translation:** Convert high-level observational setup from the M&C system into detailed hardware register writes and firmware loads for the correlator.
2.  **Command & Data Processing:** Relay dynamic control commands (e.g., start/stop integration, phase switches) and aggregate monitor data (temperatures, voltages, status flags) from hardware.
3.  **Health Monitoring & Fault Recovery:** Continuously assess the state of the correlator and its subsystems, executing predefined recovery procedures for known fault conditions without operator intervention where possible.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Primary Interaction |
| :--- | :--- | :--- |
| **Array Operators** | Astronomers or telescope operators. Use the EVLA M&C interface. Not experts in correlator hardware. | Indirectly via the EVLA M&C system. Require reliable operation and clear fault notifications. |
| **Engineers & Technicians** | Hardware and systems experts. Responsible for maintenance and deep troubleshooting. | Direct interaction with MCCIS for diagnostics, manual overrides, and servicing procedures. |
| **Software Developers** | Maintain and extend the MCCIS and EVLA M&C software. | Interact with APIs, log files, and system documentation for integration and debugging. |

#### 2.4 Operating Environment
*   **Hardware:** Industrial-grade servers located in a controlled environment. Interfaces with specialized FPGA-based correlator hardware.
*   **Software:** Expected to run on a Linux-based operating system.
*   **Network:** Must operate across two network segments:
    1.  An external connection to the EVLA M&C network.
    2.  An internal network to the correlator hardware within a shielded enclosure.

#### 2.5 Design and Implementation Constraints
1.  **Critical Availability Constraint:** `NFR-001` - The system is a critical component; its unavailability results in the loss of incoming astronomical data. Design must prioritize stability and recovery.
2.  **Network Interface Constraint:** `NFR-002` - All external and internal software interfaces shall use standard Ethernet (IEEE 802.3 compliant) at a minimum speed of 100 Mbits/sec.
3.  **Physical Link Constraint:** `NFR-003` - The network pathway between the MCCIS and the external EVLA M&C network that penetrates the shielded room **shall** be implemented using fiber optic media to mitigate electromagnetic interference (EMI).

#### 2.6 Assumptions and Dependencies
*   It is assumed the EVLA M&C system will provide configuration data in the agreed-upon format and protocol.
*   The system depends on the stability and correct operation of the underlying Linux OS and network drivers.
*   Hardware register maps and communication protocols for the WIDAR correlator are stable and documented.

### 3. System Features and Requirements

#### 3.1 Configuration Translation Service
*   `FR-001` - The system **shall** receive a complete observational configuration block from the EVLA M&C system.
*   `FR-002` - The system **shall** validate the received configuration for internal consistency and against known hardware limits.
*   `FR-003` - The system **shall** translate the validated high-level configuration into a sequence of low-level hardware-specific commands (register writes, firmware filenames, memory addresses).
*   `FR-004` - The system **shall** report the success or failure of the configuration load back to the EVLA M&C system.

#### 3.2 Dynamic Control and Monitor Data Processing
*   `FR-005` - The system **shall** accept real-time control commands (e.g., `START_INTEGRATION`, `STOP`) from the M&C system and relay them to the appropriate hardware subsystem with minimal latency (< 100 ms).
*   `FR-006` - The system **shall** periodically poll hardware subsystems for monitor data (e.g., voltages, temperatures, error flags) at a configurable rate (default: 1 Hz).
*   `FR-007` - The system **shall** aggregate, timestamp, and buffer monitor data.
*   `FR-008` - The system **shall** provide the aggregated monitor data to the EVLA M&C system upon request or via a periodic publish mechanism.

#### 3.3 Health Monitoring and Autonomous Recovery
*   `FR-009` - The system **shall** continuously compare monitor data against predefined nominal operating ranges and thresholds.
*   `FR-010` - The system **shall** generate a fault alert for the operator upon detection of an out-of-tolerance condition.
*   `FR-011` - For a defined subset of known, recoverable faults (e.g., software process crash, network link flap, programmable chip configuration loss), the system **shall** automatically execute a predefined recovery sequence without requiring operator input.
*   `FR-012` - The system **shall** log all fault detection events and autonomous recovery actions with full context (timestamp, subsystem, data values) to a persistent store.

#### 3.4 Interfaces

##### 3.4.1 EVLA M&C System Interface
*   `FR-013` - The interface **shall** be implemented over TCP/IP Ethernet.
*   `FR-014` - The application-layer protocol **shall** be as defined in the EVLA M&C ICD (e.g., XML-RPC, JSON over TCP, custom binary protocol).

##### 3.4.2 Correlator Hardware Interface
*   `FR-015` - The system **shall** communicate with WIDAR hardware subsystems via Ethernet (for supervisory controllers) and/or direct PCIe/Serial links (for low-level control) as defined by hardware specifications.

##### 3.4.3 User Interface
*   `FR-016` - The system **shall** provide a command-line interface (CLI) for use by Engineers and Technicians for diagnostic and manual control purposes.
*   `FR-017` - The system **shall** provide a structured log file (e.g., syslog, plain text with defined fields) accessible to Software Developers.

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
*   `NFR-004` - The configuration translation process for a standard observing setup **shall** complete within 5 seconds.
*   `NFR-005` - End-to-end latency for a dynamic control command (from receipt from M&C to issuance to hardware) **shall** be less than 100 milliseconds under normal load.
*   `NFR-006` - The system must be capable of handling and processing monitor data from all subsystems at the maximum polling rate without sustained buffer overflows.

#### 4.2 Safety & Criticality Requirements
*   `NFR-001` is restated here as a primary driver for all design decisions.
*   `NFR-007` - The system **shall** be designed for high availability, targeting 99.9% uptime during scheduled observing periods.
*   `NFR-008` - In the event of a catastrophic software failure, the system **shall** fail in a state that allows the hardware to be placed in a safe, non-destructive mode.

#### 4.3 Security Requirements
*   `NFR-009` - The system **shall** authenticate all connection attempts from the EVLA M&C network.
*   `NFR-010` - The system **shall** only accept commands from authorized source IP addresses/processes.

#### 4.4 Network Requirements
*   `NFR-002` and `NFR-003` (stated in Section 2.5) are critical network requirements.

### 5. Appendices

#### Appendix A: Glossary
*   **EVLA:** Expanded Very Large Array
*   **M&C:** Monitor and Control
*   **MCCIS:** Monitor & Control Interface System (the subject of this SRS)
*   **WIDAR:** Wideband Interferometric Digital ARchitecture (the correlator design)
*   **ICD:** Interface Control Document

#### Appendix B: To Be Determined (TBD)
*   Specific application-layer protocol with EVLA M&C (to be defined by referenced ICD).
*   Detailed list of recoverable faults and their corresponding recovery sequences.
*   Complete hardware register map and low-level command set for WIDAR subsystems.

---
*This document is considered the authoritative source for requirements for the MCCIS project. All subsequent design and testing activities shall be traced to the requirements contained herein.*