# Software Requirements Specification (SRS)
## Gemini 8-m Telescopes Control System (GCS)

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Gemini Control System (GCS) software. It serves as the primary reference for developers, system architects, and project managers involved in the design, implementation, and testing of the control and data acquisition systems for the Gemini 8-m Telescopes. The document is oriented toward the development team, not the end-user.

#### 1.2 Scope
The GCS software encompasses the following core components:
*   **Telescope and Instrument Control:** Software for commanding and monitoring all telescope and instrument subsystems.
*   **Data Acquisition:** Systems for acquiring, processing, and storing detector data.
*   **Observation Execution:** Support for multiple operational modes: Interactive, Queue-based, Remote, and Service Observing.
*   **System Infrastructure:** On-line databases, inter-subsystem communication, and data specification frameworks.
*   **User Interfaces:** Operational interfaces tailored to different user roles and access levels.
*   **External Integration:** Interfaces for integration with external software systems such as star catalogs and data reduction pipelines.

**Out-of-Scope Items:**
*   Specification of commercial or public-domain software internals; only their required interfaces are defined.
*   Embedded software with no direct software interface to the GCS.
*   Detailed hardware specifications (covered in separate Hardware Requirements documents).
*   Implementation of full, mirrored redundancy; only cost-effective redundancy is required.
*   Development of automatic expert scheduling software; the system shall provide decision-support tools only.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **GCS:** Gemini Control System
*   **SRS:** Software Requirements Specification
*   **COTS:** Commercial Off-The-Shelf
*   **CVS:** Concurrent Versions System
*   **UI:** User Interface
*   **API:** Application Programming Interface
*   **FITS:** Flexible Image Transport System (a standard data format in astronomy)

#### 1.4 References
*   Gemini Observatory High-Level Requirements Document.
*   Ward/Mellor Structured Analysis and Design Methodology.
*   Relevant telescope and instrument hardware interface control documents (ICDs).

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its stakeholders, and operating environment. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements, including performance, safety, and design constraints.

### 2. Overall Description

#### 2.1 Product Perspective
The GCS is the central supervisory software system for the Gemini 8-m Telescopes. It operates as an integrated system of subsystems, mediating between human operators (Astronomers, Telescope Operators, etc.) and the physical telescope/instrument hardware. It must interface with external astronomical databases and data processing tools.

#### 2.2 Product Functions (High-Level)
1.  Execute pre-defined and real-time observation sequences.
2.  Provide real-time monitoring and control of all telescope and instrument parameters.
3.  Acquire, format, tag, and store scientific and engineering data.
4.  Manage user authentication, authorization, and role-based access control.
5.  Facilitate communication between distributed software components.
6.  Log all system events, commands, and errors for diagnostics and auditing.
7.  Support system configuration, calibration, and simulation modes.

#### 2.3 User Characteristics and Stakeholders
| Stakeholder | Role | Primary Interaction with GCS |
| :--- | :--- | :--- |
| **Astronomer** | End-user/Principal Investigator | Submits observation programs; may monitor data acquisition remotely. |
| **Science Observer** | On-site Data Specialist | Monitors real-time data quality and integrity during observations. |
| **Telescope Operator** | On-site System Controller | Has direct control for safety and performance; executes observations. |
| **Support Personnel** | Maintenance & Engineering | Accesses subsystems for diagnostics, repair, and updates. |
| **Developer** | Software Engineer | Develops, tests, and integrates subsystems in a simulated environment. |
| **Administrator** | Observatory Operations Manager | Manages schedules, system configuration, and high-level operations. |

#### 2.4 Core Use Cases
1.  **UC-1: Submit Automated Observation Program**
    *   **Actor:** Astronomer
    *   **Precondition:** Astronomer is authenticated, and a valid observing program exists.
    *   **Flow:** Astronomer submits program to the queue scheduler. GCS validates and queues the program for execution at the appropriate time with minimal required interaction.
2.  **UC-2: Direct Telescope/Instrument Control**
    *   **Actor:** Telescope Operator
    *   **Precondition:** Operator has "control" level access. System is in interactive mode.
    *   **Flow:** Operator issues real-time commands (e.g., slew, configure instrument). GCS executes commands while enforcing software safety limits and monitoring hardware interlocks.
3.  **UC-3: Monitor Data Acquisition**
    *   **Actor:** Science Observer
    *   **Precondition:** An observation is in progress.
    *   **Flow:** Observer views real-time data display, quality metrics (e.g., SNR, FWHM), and acquisition logs to validate data integrity.
4.  **UC-4: Test Subsystem in Simulation**
    *   **Actor:** Developer
    *   **Precondition:** A software or configuration update is ready for testing.
    *   **Flow:** Developer deploys subsystem to a simulated environment. GCS provides simulated hardware interfaces to allow full functional testing without impacting the operational system.
5.  **UC-5: Perform System Maintenance**
    *   **Actor:** Support Personnel
    *   **Precondition:** Maintenance window is authorized.
    *   **Flow:** Personnel access diagnostic interfaces, run tests, update software/firmware, and modify configuration parameters.
6.  **UC-6: Review System Utilization**
    *   **Actor:** Administrator
    *   **Precondition:** Administrator is authenticated.
    *   **Flow:** Administrator queries databases for reports on telescope time usage, system performance history, and future schedule.

#### 2.5 Operating Environment
*   **Hardware:** Must be portable and not assume specific hardware beyond defined interfaces (e.g., VME, PLC, detector controllers).
*   **Software:** Must run on standard observatory workstations and servers. Must integrate with specified COTS packages and standard OS (e.g., UNIX-based systems).
*   **Network:** Must operate over observatory LAN with support for remote operation across WAN links with bandwidth limitations. Must support distributed architecture with multiple nodes.

#### 2.6 Design and Implementation Constraints
1.  **Development Standards:** Use of Ward/Mellor or equivalent structured analysis/design methodology. All code under version control (CVS).
2.  **Portability:** Software shall be hardware-independent. Dependencies on specific hardware must be abstracted via defined interfaces.
3.  **Remote Operation:** All core functionality must be accessible remotely, with UI/performance adapted transparently for bandwidth constraints.
4.  **Safety:** The system shall implement software travel limits and interlocks, which work in conjunction with independent hardware safety systems.
5.  **COTS/Standards:** Prefer commercial packages, off-the-shelf software, and international/community standards (e.g., for data formats, communications) where feasible.

#### 2.7 Assumptions and Dependencies
*   Assumes stable and defined hardware interfaces (to be specified in ICDs).
*   Dependent on the availability of specific external systems (star catalogs, weather feeds).
*   Assumes adequate computational and network resources are provisioned as per target system specifications (to be decided).

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Observation Management
*   **FR-1.1:** The system shall accept, validate, and store observation programs defined in the Gemini observation definition format.
*   **FR-1.2:** The system shall support Queue, Interactive, Remote, and Service observing modes.
*   **FR-1.3:** The system shall provide a scheduler to execute queued programs based on target visibility, conditions, and priority.
*   **FR-1.4:** The system shall provide decision-support tools (e.g., visibility plots, condition comparisons) to assist in scheduling decisions.

##### 3.1.2 Telescope and Instrument Control
*   **FR-2.1:** The system shall provide command and status interfaces for all telescope axes (azimuth, altitude), enclosure, and active optics.
*   **FR-2.2:** The system shall provide command and status interfaces for all facility instruments.
*   **FR-2.3:** The system shall enforce configurable software limits for all movable components.
*   **FR-2.4:** The system shall monitor hardware interlock status and halt motion if an interlock is triggered.

##### 3.1.3 Data Acquisition and Handling
*   **FR-3.1:** The system shall acquire detector data from instrument controllers.
*   **FR-3.2:** The system shall apply standard headers (containing observation metadata, telescope/instrument status) to all data.
*   **FR-3.3:** The system shall write final data products in FITS format to a specified storage system.
*   **FR-3.4:** The system shall generate real-time data quality assessment metrics.

##### 3.1.4 User Interface
*   **FR-4.1:** The system shall provide role-based UIs: a simplified interface for Astronomers, a comprehensive control interface for Operators, and a diagnostic interface for Support.
*   **FR-4.2:** All UIs shall be accessible from both on-site and remote locations.
*   **FR-4.3:** The system shall provide a consistent "look and feel" across all control applications.

##### 3.1.5 System Management and Diagnostics
*   **FR-5.1:** The system shall maintain a comprehensive time-stamped log of all commands, system events, and errors.
*   **FR-5.2:** The system shall provide tools to start, stop, and monitor the status of all GCS software processes.
*   **FR-5.3:** The system shall support a simulation mode where hardware interfaces are replaced by software simulators.
*   **FR-5.4:** The system shall allow for on-line configuration changes where safe and appropriate.

##### 3.1.6 Communication and Integration
*   **FR-6.1:** The system shall implement a defined communication protocol for all inter-subsystem messaging.
*   **FR-6.2:** The system shall provide APIs for integration with external star catalog services.
*   **FR-6.3:** The system shall interface with external data reduction pipelines to notify them of new data availability.

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance Requirements
*   **PR-1:** The system shall limit downtime due to software failures to a maximum of **2%** of scheduled observing time (goal: 1%). This equates to no more than 15 minutes per night or one full night per month.
*   **PR-2:** The system shall recover from and reconfigure after a software error condition to resume observing within **5 minutes**.
*   **PR-3:** The system shall support at least **six (6) active control nodes** and **two (2) monitoring nodes** simultaneously without degradation of control loop performance or data throughput.
*   **PR-4:** Command latency from UI to hardware actuation shall be less than 100ms for critical control loops.

##### 3.2.2 Safety Requirements
*   **SR-1:** Software limits shall be secondary to independent hardware interlocks.
*   **SR-2:** All safety-critical commands shall require confirmation and shall be audited.
*   **SR-3:** The system shall prevent unsafe configurations (e.g., instrument collision).

##### 3.2.3 Reliability, Availability, and Maintainability
*   **RAM-1:** Mean Time Between Failures (MTBF) for key control processes shall exceed 1000 hours.
*   **RAM-2:** The system shall be designed for a mean time to repair (MTTR) of less than 30 minutes for software faults.
*   **RAM-3:** Software shall be modular to allow for updates to individual subsystems without requiring a full system restart.

##### 3.2.4 Security Requirements
*   **SEC-1:** The system shall implement user authentication and role-based authorization.
*   **SEC-2:** Critical commands shall be restricted based on user role and physical location (e.g., some commands only available on-site).
*   **SEC-3:** All external communication links shall support secure connection protocols.

##### 3.2.5 Portability & Compatibility
*   **PC-1:** The software shall be compilable and executable on standard Linux distributions without modification.
*   **PC-2:** Data products shall comply with the FITS standard and relevant Gemini data standards.

### 4. Appendices

#### 4.1 Undecided Issues (TBD)
The following issues require resolution and will be addressed in future revisions of this SRS or in supplementary interface documents:
1.  The specific standard for acquisition and storage of detector data (beyond FITS).
2.  The choice of physical/link layer protocol for data transfer between subsystems (e.g., Ethernet-based protocol selection).
3.  Detailed hardware specifications (CPU, RAM, storage) for development and target systems.
4.  Final standards for the online software environment (e.g., specific OS version, middleware).
5.  Detailed supportability plan, including defined maintenance levels and staffing requirements.
6.  Descriptions and access methods for integrated star catalogs.

#### 4.2 Traceability Matrix
(A separate traceability matrix document will link these requirements to design elements, test cases, and verification methods.)

---
*Document End*