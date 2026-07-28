# Software Requirements Specification (SRS)
## EVLA Correlator Monitor & Control System (CMCS)

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the EVLA (Expanded Very Large Array) Correlator Monitor & Control System (CMCS). The CMCS serves as the critical interface between the WIDAR Correlator hardware and the overarching EVLA Monitor & Control (M&C) system. This SRS is intended for use by project managers, system architects, software developers, test engineers, and stakeholders to guide the design, implementation, verification, and validation of the system.

#### 1.2 Scope
The CMCS provides the primary interface for configuring, operating, and servicing the WIDAR Correlator hardware. Its core functions include:
*   Translating high-level configuration data from the EVLA M&C system into hardware-specific settings.
*   Executing real-time control commands and collecting monitor data from correlator hardware.
*   Processing and distributing dynamic monitor and control data to backend systems.
*   Continuously monitoring system health and performing autonomous fault detection and recovery.
*   Providing secure access for operation, maintenance, and debugging.

The system is architected as a modular, redundant master/slave network to isolate the correlator hardware from the broader EVLA environment. Out of scope are the EVLA M&C system itself, the backend data processing pipelines, the WIDAR correlator hardware firmware, and the scientific data correlation algorithms.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **CMCS:** Correlator Monitor & Control System
*   **EVLA:** Expanded Very Large Array
*   **M&C:** Monitor and Control
*   **MCCC:** Master Control and Configuration Computer
*   **CMIB:** Correlator Monitor and Interface Board
*   **CPCC:** Correlator Power and Computer Controller
*   **VCI:** Virtual Correlator Interface
*   **PC104+:** A standardized form factor for embedded computing modules.
*   **UPS:** Uninterruptible Power Supply
*   **UTC:** Coordinated Universal Time

#### 1.4 References
*   EVLA System Architecture Document
*   WIDAR Correlator Hardware Specifications
*   PC104+ Standard Specifications
*   (To be added: VCI Interface Control Document)

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details specific functional requirements. Section 4 outlines non-functional requirements. Section 5 lists external interface requirements. Appendices contain supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
The CMCS is a subsystem of the larger EVLA observatory. It acts as a middleware layer, insulating the sensitive, real-time correlator hardware from the higher-level, less time-critical EVLA M&C system.

**System Interfaces:**
1.  **EVLA M&C System:** Provides observation configuration data and receives system status/health messages.
2.  **WIDAR Correlator Hardware (via CMIBs):** The ultimate target for control commands and source of monitor data.
3.  **Backend Processing/Archive Systems:** Receives processed monitor and correlator data products.
4.  **External Data Servers:** Provides auxiliary data (e.g., delay models, time standards, phase corrections).
5.  **User Workstations:** Provides access for operators, engineers, developers, and administrators.

#### 2.2 Product Functions
The primary functions of the CMCS are:
1.  **Configuration Management:** Receive, validate, and translate observation configurations.
2.  **Real-Time Control & Monitoring:** Execute commands and collect data from hardware modules.
3.  **Data Handling:** Process, packetize, and route monitor and control data.
4.  **Health & Fault Management:** Continuously monitor system state, detect anomalies, and execute recovery procedures.
5.  **Access Control & Security:** Authenticate users and enforce role-based access privileges.
6.  **Diagnostics & Maintenance:** Provide tools for remote inspection, testing, and debugging.

#### 2.3 User Characteristics
| User Role | Expertise | Primary Interaction |
| :--- | :--- | :--- |
| **Array Operator** | Astronomy operations, EVLA M&C system | Uses EVLA M&C interface for high-level status and alerts. |
| **Engineer/Technician** | Hardware diagnostics, RF systems | Uses remote diagnostic tools (CLI/GUI) for fault tracing and repair. |
| **Software Developer** | Software engineering, debugging | Uses remote access for log inspection, debugging, and software updates. |
| **Administrator** | System administration, cybersecurity | Uses admin tools for user management, system configuration, and security auditing. |
| **Web User** | Limited technical, interested party | Uses a restricted web portal for read-only status viewing. |

#### 2.4 Constraints
1.  **Hardware:** CMIBs must conform to the PC104+ form factor and interface with predefined correlator carrier boards.
2.  **Real-Time Performance:** All control loops and data processing must meet strict, hardware-defined deadlines.
3.  **Legacy Integration:** Must interface with existing EVLA M&C protocols and data formats.
4.  **Physical Environment:** Must operate reliably in a rack-mounted, data center environment.

#### 2.5 Assumptions and Dependencies
*   The EVLA M&C system will provide a stable, well-defined configuration data stream (VCI).
*   External data feeds (time, delay models) will be available and reliable.
*   The backend systems will be capable of ingesting the data rates and formats produced by the CMCS.
*   Adequate network infrastructure (redundant, isolated networks) will be provisioned.

### 3. Specific Requirements

#### 3.1 Functional Requirements

**3.1.1 Configuration Management**
*   **FR-1:** The MCCC shall receive configuration data from the EVLA M&C system via the Virtual Correlator Interface (VCI).
*   **FR-2:** The MCCC shall translate the high-level VCI configuration into hardware-specific configuration tables for target CMIBs and hardware modules.
*   **FR-3:** The system shall validate configuration data for completeness and internal consistency before translation.
*   **FR-4:** The system shall log all configuration transactions, including source, timestamp, target, and translation status.

**3.1.2 Hardware Control & Monitoring**
*   **FR-5:** CMIBs shall execute control commands received from the MCCC on their assigned hardware modules.
*   **FR-6:** CMIBs shall periodically collect monitor data (e.g., autocorrelations, state counts, temperatures, voltages) from their managed hardware.
*   **FR-7:** The system shall timestamp all monitor data with synchronized UTC.
*   **FR-8:** CMIBs shall packetize monitor data and transmit it to the MCCC and/or designated backend interfaces.

**3.1.3 Data Distribution & Auxiliary Ingestion**
*   **FR-9:** The MCCC shall distribute processed monitor and state data to the EVLA M&C system for operator display.
*   **FR-10:** The system shall output correlator data products to the designated backend processing and archive systems.
*   **FR-11:** The system shall accept, validate, and repackage external auxiliary data feeds (e.g., delay models) for delivery to the correlator hardware.

**3.1.4 Fault Detection & Recovery**
*   **FR-12:** The system shall continuously monitor the health of all CMCS components (MCCC, CPCC, CMIBs, processes) using watchdog timers and heartbeats.
*   **FR-13:** Upon detection of a faulty CMIB or software process, the system shall automatically attempt recovery (e.g., software restart, board reboot) without human intervention.
*   **FR-14:** If automatic recovery fails, the system shall escalate the fault by generating a high-severity alert to the EVLA M&C system and logging the event.
*   **FR-15:** The CPCC shall monitor the health of the primary MCCC and manage failover to a hot-standby MCCC in case of primary failure.

**3.1.5 User Access & Security**
*   **FR-16:** All user access to the CMCS shall require authentication with a unique username and encrypted password.
*   **FR-17:** The system shall enforce role-based access control (RBAC). Privileges shall be configurable by an Administrator.
*   **FR-18:** The system shall provide a secure, remote command-line and/or graphical interface for Engineers and Developers to perform diagnostics and debugging.
*   **FR-19:** The system shall provide a restricted web interface for Web Users to view system status.
*   **FR-20:** All user actions (login, commands issued, configuration changes) shall be logged in an audit trail.

**3.1.6 Diagnostics & Maintenance**
*   **FR-21:** The system shall provide tools to remotely read the status (LEDs, registers) of individual hardware modules.
*   **FR-22:** The system shall allow authorized users to view, filter, and search system event and error logs.
*   **FR-23:** Software processes shall be able to be gracefully stopped, killed, and restarted remotely with minimal impact on other running processes.

#### 3.2 Non-Functional Requirements

| ID | Category | Requirement | Verification Method |
| :--- | :--- | :--- | :--- |
| **NFR-1** | Reliability/Availability | The system shall achieve 99.9% operational availability over a calendar year, excluding scheduled maintenance. | Analysis of system logs and downtime reports. |
| **NFR-2** | Reliability/Availability | Automatic recovery from a slave CMIB failure shall be completed within < 60 seconds of fault detection. | Fault injection testing. |
| **NFR-3** | Performance | All CMCS processors shall meet 100% of their defined real-time deadlines for hardware control and data processing under maximum specified load. | Real-time performance profiling and stress testing. |
| **NFR-4** | Performance | The system shall resume full operation from a standby idle mode with a delay of no more than **TBD** seconds. | Benchmark testing. |
| **NFR-5** | Security | All network communication for control and authentication shall use encrypted protocols (e.g., TLS, SSH). | Design review and penetration testing. |
| **NFR-6** | Security | User sessions shall timeout after 15 minutes of inactivity. | Functional testing. |
| **NFR-7** | Serviceability | Mean Time To Repair (MTTR) for a field-replaceable hardware module (CMIB) shall be less than 30 minutes. | Design review of hardware accessibility. |
| **NFR-8** | Scalability | The software architecture shall support a 20% increase in the number of managed hardware modules without requiring a redesign of core components. | Design review and modularity analysis. |
| **NFR-9** | Documentation | All software source code shall be documented following the [Doxygen/Javadoc] standard. All APIs shall have formally written interface specifications. | Code and document review. |

#### 3.3 External Interface Requirements

**3.3.1 User Interfaces**
*   **CLI/GUI:** A secure, remote diagnostic interface for Engineers/Developers.
*   **Web Portal:** A read-only web interface for status monitoring by Web Users.
*   **EVLA M&C Interface:** Status and error messages integrated into the main EVLA operator console.

**3.3.2 Hardware Interfaces**
*   **CMIB to Correlator Hardware:** Defined by the carrier board specification (PC104+ and custom connectors).
*   **CPCC to Rack Power:** A power monitor/control bus (specification **TBD**).
*   **Network Interfaces:** Physically separate Gigabit Ethernet networks for Control, Monitor, and External communication.

**3.3.3 Software/Communication Interfaces**
*   **VCI (to EVLA M&C):** A well-defined, "unambiguous" data stream protocol and format (specification **TBD**).
*   **Backend Data Output:** A defined packet format and network protocol for science and monitor data.
*   **External Data Input:** Defined APIs or protocols for receiving time, delay, and phase correction data.

#### 3.4 Data Requirements
The system shall manage the following core data entities:
*   **Configuration Tables**
*   **Monitor Data Packets**
*   **Hardware Module Inventory & State**
*   **System Event/Error Logs**
*   **User Accounts and Audit Trails**
*   **Control Command Queue**

(Detailed schema for each entity is provided in the supplied Domain Data Elements list).

### 4. Appendices

#### Appendix A: Undecided Issues (To Be Resolved)
1.  **Failover Authority:** Mechanism for MCCC failover (automatic vs. manual confirm).
2.  **CPCC Failure Response:** Defined procedure for external systems upon CPCC hard failure.
3.  **Power Bus Specification:** Final details of the CPCC-to-rack power control bus.
4.  **VCI Format:** Detailed specification of the configuration data stream from EVLA M&C.
5.  **Standby Resume Time:** Quantitative tolerance for resuming from idle mode (NFR-4).
6.  **Operating System Selection:** OS for MCCC (e.g., Linux) and CMIB (e.g., Real-Time Linux, VxWorks).

#### Appendix B: Risk Log
| Risk ID | Description | Probability | Impact | Mitigation Strategy | Owner |
| :--- | :--- | :--- | :--- | :--- | :--- |
| R-01 | Single point of failure in MCCC | Medium | Critical | Implement redundant MCCC pair with CPCC-managed failover. | [TBD] |
| R-02 | Network congestion disrupts control | Medium | High | Use isolated, dedicated networks; implement control data spooling. | [TBD] |
| R-03 | Unauthorized access | Low | Critical | Robust auth, encryption, firewalls, and activity logging. | [TBD] |
| R-04 | Complex faults lead to long diagnosis | Medium | Medium | Design comprehensive remote diagnostic tools and clear error messaging. | [TBD] |
| R-05 | Future scalability limitations | Low | Medium | Adopt modular hardware/software design from outset. | [TBD] |

---
*Document End*