# Software Requirements Specification (SRS)
## Gemini 8m Telescopes Control and Data Acquisition System

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Gemini 8m Telescopes Control and Data Acquisition System (GCDAS). The primary purpose of this system is to provide comprehensive operational control and data acquisition capabilities to facilitate the acquisition of astronomical data. This document serves as a definitive guide for developers, testers, project managers, and stakeholders.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Keywords:** The terms "MUST," "SHALL," "REQUIRED," "WILL," and "SHOULD" are to be interpreted as described in IETF RFC 2119.
*   **Formatting:** User roles are *italicized*. System components and external entities are in `monospace`.

#### 1.3 Scope
The GCDAS encompasses all software necessary for the remote and local control, monitoring, sequencing, and data handling for the Gemini 8m Telescopes. This includes:
*   High-level observation planning and execution software.
*   Middleware for subsystem coordination and communication.
*   User interfaces for operations and engineering.
*   Data acquisition, processing, storage, and transfer pipelines.

**Out of Scope:**
*   Commercial Off-The-Shelf (COTS) packages (e.g., database engines, operating systems), though their integration is required.
*   Embedded firmware or software within subsystems that do not expose a control interface.
*   The detailed design of individual scientific instruments, though their control interfaces are in scope.
*   Telescope hardware or mechanical systems.

#### 1.4 References
*   Gemini Observatory Functional Requirements Document (FRD)
*   IETF RFC 2119 - Key words for use in RFCs to Indicate Requirement Levels
*   Relevant IAU, FITS, and IVOA standards for data formats and protocols.

### 2. Overall Description

#### 2.1 Product Perspective
The GCDAS is the central software "nervous system" of the Gemini Observatory. It interacts with numerous external entities:

```
[Observation Database] <--> [GCDAS Core] <--> [Telescope Subsystems]
                                    |
                                    v
                            [Science Instruments]
                                    |
                                    v
                [Data Storage Archive] <--> [User Interfaces]
```

The system must integrate with existing observatory infrastructure, including telemetry databases, proposal management systems, and external data archives.

#### 2.2 Product Functions
The core high-level functions of the GCDAS are:
1.  **Remote Operations Facilitation:** Enable full telescope control from remote locations.
2.  **Observation Execution:** Automatically execute complex, pre-programmed observing sequences for both queue-based and service observing.
3.  **Subsystem Orchestration:** Coordinate and synchronize the telescope mount, dome, adaptive optics, instruments, and wavefront sensors.
4.  **Data Lifecycle Management:** Acquire raw data, apply real-time processing, compress, annotate with metadata, store reliably, and transfer to designated archives.

#### 2.3 User Classes and Characteristics
| User Class | Description | Key Activities |
| :--- | :--- | :--- |
| *Astronomer* | Principal Investigator; defines scientific goals. | Submits observing proposals, defines observation sequences. |
| *Science Observer* | Staff astronomer executing observations. | Monitors data quality, adjusts observation parameters in real-time. |
| *Telescope Operator* | Technical staff responsible for telescope safety and operation. | Executes and monitors observations, handles faults, performs engineering tasks. |
| *Support Personnel* | Engineers and technicians. | Monitors subsystem health, performs diagnostics, calibrations. |
| *Developer* | Software engineer maintaining/extending the GCDAS. | Implements new features, debugs, writes scripts. |
| *Administrator* | System manager. | Manages user accounts, system configuration, software deployment, logs. |

#### 2.4 Operating Environment
*   **Hardware:** Must operate on standard server-class hardware and workstations. Control interfaces will connect to various real-time and non-real-time telescope hardware.
*   **Software:** Should be portable across major Unix-like operating systems (e.g., Linux distributions). Will rely on COTS for OS, RDBMS, etc.
*   **Network:** Must operate over high-latency, bandwidth-constrained links to support remote operations from anywhere in the world.

#### 2.5 Design and Implementation Constraints
1.  **Hardware Independence:** `NFR-001` - The application logic SHALL be decoupled from specific hardware APIs through abstraction layers.
2.  **Standards Compliance:** `NFR-002` - The system SHALL use established astronomical standards (e.g., FITS for data, ICE or similar for middleware) where feasible and appropriate.
3.  **COTS/Open-Source Preference:** `NFR-003` - The implementation SHALL prefer robust commercial or public-domain software components over custom development for common infrastructure needs.
4.  **Full Mode Support:** `NFR-004` - The system SHALL support all defined observing modes (e.g., classical, queue, service, remote) from the initial operational deployment.

#### 2.6 Assumptions and Dependencies
*   Subsystems (mount, instruments, etc.) will provide stable, documented software control interfaces.
*   Adequate network bandwidth will be available for data transfer and real-time control.
*   External archives and databases will be available and provide defined ingestion APIs.

### 3. System Features and Requirements

#### 3.1 Feature: Remote Operations
**Description:** Provide the capability to conduct all observing, control, monitoring, and diagnostic functions from a geographically remote location.

| Requirement ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| `FR-101` | The system SHALL provide a graphical user interface (GUI) accessible via a standard network connection that replicates the functionality of the local control console. | High |
| `FR-102` | The system SHALL transmit all relevant engineering telemetry and diagnostic data to the remote operator's console in near-real-time (< 2 sec latency). | High |
| `FR-103` | The system SHALL support multiple, concurrent, authenticated remote sessions with configurable privilege levels (e.g., *Observer* view-only, *Operator* control). | Medium |
| `FR-104` | The system SHALL provide remote diagnostic tools to query subsystem status, view logs, and run health-check routines. | Medium |

#### 3.2 Feature: Automated Observation Sequencing
**Description:** Execute pre-defined observation sequences without manual intervention for queue and service observing.

| Requirement ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| `FR-201` | The system SHALL execute observing scripts (sequences) that specify instrument configurations, telescope pointing, exposure parameters, and calibration steps. | High |
| `FR-202` | The system SHALL manage a queue of observation sequences, prioritizing them based on predefined criteria (e.g., weather conditions, target visibility, scientific ranking). | High |
| `FR-203` | The system SHALL be able to pause, resume, or abort an executing sequence based on automated conditions (e.g., cloud detection) or manual command. | High |
| `FR-204` | The system SHALL validate sequence syntax and resource availability (instrument, telescope time) before queue submission. | Medium |

#### 3.3 Feature: Subsystem Control & Coordination
**Description:** Issue commands and synchronize the actions of all telescope subsystems and instruments.

| Requirement ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| `FR-301` | The system SHALL provide a unified interface to send commands to and receive status from all controllable subsystems (e.g., `telescope-mount`, `dome`, `instrument-x`, `ao-system`). | High |
| `FR-302` | The system SHALL coordinate time-critical actions between subsystems (e.g., instrument exposure start synchronized with dome shutter opening). | High |
| `FR-303` | The system SHALL maintain a centralized, consistent state model of the entire telescope facility. | High |
| `FR-304` | The system SHALL implement a fault containment strategy where a failure in one subsystem does not propagate uncontrollably to others. | High |

#### 3.4 Feature: Data Acquisition & Handling
**Description:** Manage the flow of scientific and engineering data from acquisition to final archive.

| Requirement ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| `FR-401` | The system SHALL acquire raw image data and associated telemetry from scientific instruments. | High |
| `FR-402` | The system SHALL annotate all scientific data with comprehensive FITS headers containing observation metadata, instrument settings, and environmental conditions. | High |
| `FR-403` | The system SHALL apply lossless or lossy compression (as configured) to data prior to storage or transfer. | Medium |
| `FR-404` | The system SHALL store data redundantly on local storage and automatically transfer it to a long-term archive system upon observation completion. | High |
| `FR-405` | The system SHALL generate real-time quick-look data products (e.g., reduced images, signal-to-noise estimates) for quality assessment by the *Science Observer*. | Medium |

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Primary Control GUI:** Graphical interface with panels for telescope control, instrument configuration, sequence editor/queue manager, and real-time data display.
*   **Engineering CLI:** Command-line interface for scripting and low-level diagnostics.
*   **Web-based Monitoring Portal:** Read-only web interface for subsystem health and observation status.

#### 4.2 Hardware Interfaces
The system will communicate via standard protocols (Ethernet, Serial-over-IP). Specific hardware driver interfaces are defined by the abstraction layer and are outside this SRS's direct scope.

#### 4.3 Software Interfaces
*   **Database Interface:** SQL interface to the observation catalog and engineering telemetry database (e.g., PostgreSQL).
*   **Subsystem Interfaces:** Defined APIs (e.g., CORBA, XML-RPC, REST) for each major subsystem.
*   **Archive Interface:** Standard protocol (e.g., SFTP, GridFTP) for transferring data to the Gemini Archive.

#### 4.4 Communications Interfaces
*   All internal component communication SHALL use a defined middleware standard (e.g., ICE, DDS) for messaging and remote procedure calls.
*   External remote access SHALL be secured via VPN and/or SSH tunneling.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-101` Command Latency: 95% of non-critical control commands SHALL be acknowledged by the target subsystem within 500ms.
*   `NFR-102` Telemetry Update: Critical engineering telemetry (e.g., mount position, instrument temperature) SHALL be updated at the operator console at a minimum rate of 1 Hz.
*   `NFR-103` Data Throughput: The system SHALL sustain writing processed data to local storage at the peak instrument data generation rate.

#### 5.2 Safety & Reliability Requirements
*   `NFR-201` The system SHALL have a mean time between critical failures (MTBCF) of > 1000 operational hours.
*   `NFR-202` The system SHALL provide a manual "safe state" override that allows an operator to halt all moving systems.
*   `NFR-203` No single software failure shall cause uncontrolled telescope movement or hardware damage.

#### 5.3 Security Requirements
*   `NFR-301` All user access SHALL require authentication.
*   `NFR-302` The system SHALL implement role-based access control (RBAC) mapping to the user classes defined in 2.3.
*   `NFR-303` All remote communication SHALL be encrypted.

#### 5.4 Portability & Maintainability Requirements
*   `NFR-401` The core application software SHALL be compilable and executable on a minimum of two major Linux distributions.
*   `NFR-402` The system SHALL be designed with modular, loosely coupled components to facilitate maintenance and upgrades.

---
**Appendices**

*Appendix A: Glossary*
*Appendix B: Analysis Models* (To be developed)
*Appendix C: To Be Determined List* (To be developed)