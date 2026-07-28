# Software Requirements Specification (SRS)
## EVLA Correlator Monitor & Control System (CMCS)

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the EVLA Correlator Monitor & Control System (CMCS). The CMCS serves as the critical interface between the WIDAR Correlator hardware and the broader EVLA Monitor & Control (M&C) system. This SRS is intended for use by project managers, system architects, software developers, testers, and stakeholders to guide the development, verification, and validation of the system.

#### 1.2 Document Conventions
- Requirements are uniquely identified as `FR` (Functional Requirement) or `NFR` (Non-Functional Requirement), followed by a numeric ID.
- Keywords **SHALL**, **SHOULD**, **MAY**, **WILL**, and **MUST** are used as defined in IETF RFC 2119.
- All references to external systems (e.g., EVLA M&C, Backend Data Processing) are assumed to be defined in their respective interface documentation.

#### 1.3 Project Scope
The CMCS is the primary system for configuring, operating, monitoring, and servicing the WIDAR Correlator. Its core responsibility is to translate high-level observational configurations into low-level hardware settings, manage real-time control data, monitor system health, and facilitate debugging, all while ensuring high availability and data integrity.

**In-Scope Elements:**
*   Translation of EVLA M&C configuration data into correlator hardware configurations.
*   Processing and transfer of dynamic control data (e.g., delay models, filter parameters) and monitor data (e.g., auto-correlation products).
*   System health monitoring and autonomous recovery from hardware and computing faults.
*   Limited real-time data processing and probing (e.g., collection and display of auto-correlation spectra).
*   Provision of system access for testing and debugging via the Virtual Correlator Interface (VCI).

**Out-of-Scope Elements:**
*   Full backend data processing and reduction (handled by the Backend Data Processing System).
*   Long-term scientific data archiving (managed by the e2e System).
*   Direct user interaction bypassing the authorized interfaces (VCI or MCCC).
*   Physical hardware design of the correlator boards (CMIBs, etc.).
*   External network security beyond the defined MCCC-EVLA M&C interface boundary.

#### 1.4 References
*   EVLA System Architecture Document
*   WIDAR Correlator Hardware Specifications
*   EVLA Monitor & Control System Interface Control Document (ICD)
*   IETF RFC 2119 - Key words for use in RFCs to Indicate Requirement Levels

### 2. Overall Description

#### 2.1 Product Perspective
The CMCS is a subsystem within the larger EVLA data acquisition chain. It interfaces upstream with the EVLA M&C system for commands and configurations, and downstream with the WIDAR correlator hardware (CMIBs, CPCC). It outputs monitor data and system status to operators and engineers, and passes formatted correlation products to the Backend Data Processing System.

**System Context Diagram:**
```
[EVLA M&C System] <---Commands/Config---> [MCCC] <---Control---> [CPCC]
       |                                          |                   |
       |---Status/Monitor Data---|                |---Control---> [CMIBs]
                                                                      |
                                                                      |---Corr. Products---> [Backend Data Processing]
```
*   **MCCC:** Monitor & Control Computer Cluster
*   **CPCC:** Correlator Programmable Clock and Control
*   **CMIB:** Correlator Monitor Interface Board

#### 2.2 Product Functions
1.  **Configuration Management:** Receive, validate, and translate observation schedules and configurations from EVLA M&C into hardware-specific commands.
2.  **Real-Time Control:** Process and deliver dynamic parameters (e.g., phase corrections, delay models) to the correlator hardware during observations.
3.  **Health Monitoring:** Continuously monitor the status of all correlator hardware and software components.
4.  **Fault Management:** Detect, log, categorize faults, and execute predefined autonomous recovery procedures.
5.  **Data Probing & Debugging:** Provide tools for authorized users to inspect real-time data streams and hardware registers for diagnostic purposes.
6.  **Access Control & Security:** Manage user roles, authentication, and authorization for system access via the VCI and web interfaces.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Array Operator** | Uses EVLA M&C interface; not a correlator expert. | High-level system status, clear error alerts, simple controls. |
| **Engineer/Technician** | Deep hardware/software knowledge; performs maintenance. | Low-level hardware access, diagnostic tools, remote inspection. |
| **Software Developer** | Develops and maintains CMCS software. | Remote system access, debugging tools, log inspection, ability to deploy/test patches. |
| **Web User** | Authorized personnel (e.g., project scientists, managers). | Read-only access to specific monitoring pages or system metrics. |
| **Administrator** | Responsible for system integrity and security. | User account management, privilege assignment, system configuration backup/restore. |

#### 2.4 Operating Environment
*   **Hardware:** Commercial Off-The-Shelf (COTS) servers (MCCC), custom FPGA-based hardware (CPCC, CMIBs). Hardware must be modular and hot-swappable.
*   **Software:** Real-time operating system or real-time extensions on MCCC. Software must be written in a readable, maintainable language (e.g., C++, Python).
*   **Networks:** Isolated, dedicated networks for MCCC-CMIB, MCCC-CPCC, and MCCC-EVLA M&C communications.
*   **Durability:** 24/7 operational availability in an observatory environment.

#### 2.5 Design and Implementation Constraints
1.  **Criticality Constraint:** The CMCS is in the critical data path. Unavailability results in immediate loss of astronomical data. (`NFR-CRIT-01`)
2.  **Modularity Constraint:** Hardware components (e.g., CMIBs) must be modular and hot-swappable to facilitate rapid repair. (`NFR-HW-01`)
3.  **Network Isolation Constraint:** The three primary network interfaces (MCCC-CMIB, MCCC-CPCC, MCCC-EVLA M&C) must be physically or logically isolated for security and deterministic performance. (`NFR-SEC-01`)
4.  **Software Constraint:** Core control software must support real-time deadlines and be written in a language familiar to the maintenance team. (`NFR-SW-01`)
5.  **Resilience Constraint:** All computers (MCCC nodes) must have local disk and file systems to operate in a standalone mode during network failures. (`NFR-RES-01`)

#### 2.6 Assumptions and Dependencies
*   The EVLA M&C system will provide configuration data in an agreed-upon format and protocol.
*   The Backend Data Processing system is available to receive correlation products.
*   A stable power and cooling infrastructure is provided.
*   The format for auxiliary data (delay models, etc.) will be finalized prior to integration.

### 3. System Features and Requirements

#### 3.1 Feature: Configuration Translation and Download
**Description:** The system shall accept high-level observation configurations from the EVLA M&C system and translate them into the specific register settings and commands required by the correlator hardware (CPCC, CMIBs).

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| `FR-CONF-01` | The MCCC SHALL receive observation configuration blocks from the EVLA M&C system via the defined interface. | High |
| `FR-CONF-02` | The MCCC SHALL validate the syntax and semantic consistency of received configuration data. | High |
| `FR-CONF-03` | The MCCC SHALL translate validated configurations into hardware-specific command sequences for the CPCC and all relevant CMIBs. | High |
| `FR-CONF-04` | The MCCC SHALL download the translated configuration to the CPCC and CMIBs, verifying successful acknowledgment from each device. | High |
| `FR-CONF-05` | The system SHALL allow a configuration to be pre-loaded and held in a "standby" state before being activated synchronously across the hardware. | Medium |

#### 3.2 Feature: Real-Time Monitoring and Data Transfer
**Description:** The system shall continuously monitor hardware health and transfer both monitor data (e.g., auto-correlations) and dynamic control data.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| `FR-MON-01` | The CMIBs SHALL collect pre-defined monitor data (e.g., power levels, auto-correlation spectra) at a configurable rate. | High |
| `FR-MON-02` | The MCCC SHALL poll or receive pushed monitor data from all CMIBs and aggregate it. | High |
| `FR-MON-03` | The MCCC SHALL make aggregated system health and status data available to the EVLA M&C system in real-time. | High |
| `FR-MON-04` | The MCCC SHALL process and forward dynamic control data (e.g., delay models) from EVLA M&C or auxiliary servers to the CPCC within a defined latency bound (TBD). | High |
| `FR-MON-05` | The system SHALL provide a tool (via VCI) for an Engineer to selectively probe and display real-time data from any CMIB channel. | Medium |

#### 3.3 Feature: Fault Detection and Autonomous Recovery
**Description:** The system shall detect hardware and software faults, categorize them, log them, and attempt autonomous recovery where predefined procedures exist.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| `FR-FLT-01` | The system SHALL continuously monitor for faults including, but not limited to: CMIB/CPCC communication loss, hardware error flags, software process crashes, and network failures. | High |
| `FR-FLT-02` | Detected faults SHALL be immediately logged with a timestamp, severity level (Critical, Error, Warning, Info), and source identifier. | High |
| `FR-FLT-03` | For faults with predefined recovery procedures (e.g., a stuck CMIB), the system SHALL automatically attempt recovery (e.g., power cycle, software restart) without human intervention. | High |
| `FR-FLT-04` | The system SHALL notify the EVLA M&C system of all Critical and Error-level faults immediately upon detection. | High |
| `FR-FLT-05` | The system SHALL provide a detailed fault history log accessible via the VCI for diagnostic purposes. | Medium |

#### 3.4 Feature: User Access and Control (VCI)
**Description:** The system shall provide a Virtual Correlator Interface (VCI) for authorized users to access the system for testing, debugging, and advanced control.

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| `FR-ACC-01` | The VCI SHALL require user authentication before granting access. | High |
| `FR-ACC-02` | The VCI SHALL enforce role-based access control (RBAC) based on user classes (Operator, Engineer, Developer, Admin). | High |
| `FR-ACC-03` | An Engineer, via the VCI, SHALL be able to remotely inspect the status and registers of any individual CMIB or the CPCC. | High |
| `FR-ACC-04` | A Technician, via the VCI, SHALL be able to initiate and monitor predefined performance tests on correlator subsystems. | High |
| `FR-ACC-05` | A Software Developer, via the VCI, SHALL have remote access to system logs, software processes, and the ability to restart services for troubleshooting. | High |
| `FR-ACC-06` | An Administrator, via the VCI, SHALL be able to create, modify, and delete user accounts and assign privileges. | High |
| `FR-ACC-07` | A Web User SHALL be able to access a read-only web portal to view specific, restricted system data (e.g., overall health dashboard) without VCI login. | Medium |

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
| ID | Requirement Description |
| :--- | :--- |
| `NFR-PER-01` | The system SHALL meet all real-time processing deadlines for control data transfer as defined in the detailed design (latency bounds TBD). |
| `NFR-PER-02` | System status updates to the EVLA M&C operator console SHALL have a latency of less than 2 seconds. |
| `NFR-PER-03` | The VCI interface SHALL respond to user queries (e.g., register read) within 5 seconds under normal load. |

#### 4.2 Availability & Reliability Requirements
| ID | Requirement Description |
| :--- | :--- |
| `NFR-AVL-01` | The overall CMCS SHALL achieve 99.9% availability per calendar year, excluding scheduled maintenance. |
| `NFR-AVL-02` | The system SHALL be designed to continue correlation operations (potentially degraded) during maintenance on a single MCCC node or a subset of CMIBs. |
| `NFR-REL-01` | No single point of hardware failure (excluding the CPCC) SHALL cause a complete loss of correlator function. |

#### 4.3 Security Requirements
| ID | Requirement Description |
| :--- | :--- |
| `NFR-SEC-02` | All remote access (VCI, web) SHALL be conducted over encrypted channels (e.g., SSH, HTTPS). |
| `NFR-SEC-03` | User passwords SHALL be stored using strong, salted cryptographic hashes. |
| `NFR-SEC-04` | The system SHALL automatically log out inactive VCI sessions after a period of 30 minutes. |

#### 4.4 Maintainability & Supportability Requirements
| ID | Requirement Description |
| :--- | :--- |
| `NFR-MNT-01` | The system SHALL provide comprehensive, categorized, and searchable logging for all operational and error events. |
| `NFR-MNT-02` | Software components SHALL be designed for modularity to allow for independent updates where possible. |

### 5. Appendices

#### Appendix A: Undecided Issues (TBD)
The following items require resolution and will be incorporated into a future revision of this SRS:
1.  Specific actions for external systems (EVLA M&C, Backend) to take upon a CPCC hard failure.
2.  Exact format and protocol for auxiliary data (delay models, phase corrections) from EVLA M&C or dedicated servers.
3.  Method for automatic activation of the backup MCCC system (failover triggered by CPCC vs. human intervention).
4.  The maximum acceptable delay for resuming full operations from a low-power "standby" mode.
5.  Detailed implementation specification for the redundant serial (RS-232c) communication path between MCCC and CPCC.

#### Appendix B: Glossary
*   **CMCS:** Correlator Monitor & Control System
*   **MCCC:** Monitor & Control Computer Cluster
*   **CPCC:** Correlator Programmable Clock and Control
*   **CMIB:** Correlator Monitor Interface Board
*   **VCI:** Virtual Correlator Interface
*   **M&C:** Monitor & Control
*   **EVLA:** Expanded Very Large Array
*   **WIDAR:** Wideband Interferometric Digital ARchitecture