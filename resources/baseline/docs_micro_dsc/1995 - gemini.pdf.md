# Software Requirements Specification (SRS)
## Gemini Control System (GCS)

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Gemini Control System (GCS) software. The GCS is responsible for the operational control of the Gemini 8-meter telescopes and their associated scientific instruments to facilitate astronomical data acquisition. This document serves as a comprehensive guide for developers, testers, project managers, and stakeholders.

#### 1.2 Scope
The scope of the Gemini Control System encompasses the software required to:
*   Command and monitor telescope hardware (mount, mirrors, dome, etc.) and instrument hardware (detectors, filters, gratings, etc.).
*   Support multiple, concurrent observing modes for diverse user communities.
*   Provide a simulation environment for planning, testing, and training.
*   Manage the lifecycle of astronomical data from acquisition to archival transfer.
*   Enable remote operation from designated Gemini facilities, accounting for network constraints.

**Out of Scope:**
*   Detailed hardware design specifications for telescopes or instruments.
*   Scientific data reduction and analysis pipelines.
*   Administrative and proposal management software.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **EPICS:** Experimental Physics and Industrial Control System. A toolkit for building distributed control systems.
*   **IOC:** Input/Output Controller. A real-time software component in EPICS that interfaces with hardware.
*   **VxWorks:** A real-time operating system (RTOS).
*   **FITS:** Flexible Image Transport System. The standard data format used in astronomy.
*   **CVS:** Concurrent Versions System. A version control system.
*   **SRS:** Software Requirements Specification.
*   **GCS:** Gemini Control System.
*   **RTOS:** Real-Time Operating System.

#### 1.4 References
*   EPICS Official Documentation
*   VxWorks System Reference
*   FITS Standard (NASA/Science Office of Standards and Technology)
*   IEEE Std 830-1998 - Recommended Practice for Software Requirements Specifications

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details the specific requirements, including functional, interface, performance, and design constraints.

### 2. Overall Description

#### 2.1 Product Perspective
The GCS is a mission-critical, distributed software system. It acts as the intermediary between astronomers/operators and the telescope/instrument hardware. It integrates with lower-level EPICS IOCs running on VxWorks for real-time control and with higher-level user interfaces and data systems. The system must operate reliably in the demanding environment of a professional astronomical observatory.

#### 2.2 Product Functions (Summary)
1.  **Telescope & Instrument Control:** Precise positioning, configuration, and monitoring.
2.  **Multi-Mode Observation Execution:** Support for Interactive, Queue-based, Remote, and Service observing.
3.  **Simulation:** A virtual telescope/instrument simulator for offline use.
4.  **Data Acquisition & Handling:** Control detectors, assemble FITS headers, write FITS files, and manage data transfer to archives.
5.  **Status Monitoring & Alarm Handling:** Provide a comprehensive view of system health and alert operators to faults.
6.  **Sequencing:** Execute complex, pre-defined sequences of observations.
7.  **Remote Operations:** Allow control from geographically distributed facilities with managed functionality.

#### 2.3 User Characteristics
*   **Astronomers (Interactive/Remote Users):** Scientists with domain expertise but varying levels of familiarity with the specific control software. Require intuitive interfaces to execute their programs.
*   **Observatory Operators:** Highly trained staff responsible for safe telescope operations, queue execution, and system monitoring.
*   **Systems Engineers & Developers:** Personnel who maintain, configure, and extend the software. Proficient in EPICS, real-time systems, and software engineering.
*   **Service Observers:** Staff executing observations on behalf of astronomers.

#### 2.4 Constraints
1.  **Technical Constraints:**
    *   The Input/Output Controller (IOC) subsystems **shall** be implemented using the **EPICS toolkit**.
    *   The IOC subsystems **shall** run on the **VxWorks** real-time operating system.
    *   All acquired scientific data **shall** be stored and transferred in **FITS format**.
    *   All software development **shall** utilize a version control system, specifically **CVS**.
2.  **Regulatory/Compliance Constraints:** Development must follow standard software engineering methodologies for safety-critical systems.
3.  **Operational Constraints:** Remote operation functionality will be limited by the available bandwidth and latency of the communication links to various facilities.

#### 2.5 Assumptions and Dependencies
*   It is assumed that the underlying telescope and instrument hardware meet their specified performance and interface requirements.
*   The system depends on the continued support and development of the EPICS toolkit.
*   Adequate network infrastructure is assumed to be available at the observatory sites.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Observation Modes
*   **FR-OM-01: Interactive Mode**
    The system shall allow a locally-present astronomer or operator to have direct, real-time control of the telescope and instrument for executing an observing program.
*   **FR-OM-02: Queue-based Mode**
    The system shall be able to execute a ranked list of observing programs (a queue) automatically, optimizing for conditions and priority, with operator oversight.
*   **FR-OM-03: Remote Mode**
    The system shall provide authenticated astronomers with the ability to conduct observations from a designated remote facility, with the interface adapting functionality based on available network bandwidth.
*   **FR-OM-04: Service Mode**
    The system shall support execution of observations by observatory staff on behalf of an astronomer, with all necessary metadata captured for later delivery.

##### 3.1.2 Simulation
*   **FR-SIM-01: Virtual Telescope Simulator**
    The system shall provide a software simulator that accurately models the behavior of the telescope and instruments, decoupled from real hardware.
*   **FR-SIM-02: Planning & Testing**
    The simulator shall be used for science observation planning, sequence testing, and operator training without requiring telescope time.

##### 3.1.3 Data Acquisition and Management
*   **FR-DA-01: FITS File Generation**
    The system shall acquire data from instruments, generate standard-compliant FITS headers containing all necessary observational and instrumental metadata, and write the data to FITS files.
*   **FR-DA-02: Data Transfer**
    The system shall automatically transfer completed FITS files to the observatory's archival storage system.
*   **FR-DA-03: Data Integrity**
    The system shall verify the integrity of each FITS file before confirming successful acquisition and initiating transfer.

##### 3.1.4 Control and Monitoring
*   **FR-CTRL-01: EPICS IOC Control**
    The system shall command and monitor all telescope and instrument subsystems via EPICS Process Variables (PVs) interfacing with the VxWorks-based IOCs.
*   **FR-CTRL-02: Status Display**
    The system shall provide a unified, real-time graphical display showing the status of all critical system components.
*   **FR-CTRL-03: Alarm Management**
    The system shall detect, log, categorize (e.g., Warning, Major, Critical), and display alarms to operators.

#### 3.2 External Interface Requirements

##### 3.2.1 Hardware Interfaces
*   **EI-HW-01:** The software shall interface with telescope motors, encoders, sensors, and environmental monitors via EPICS IOCs.
*   **EI-HW-02:** The software shall interface with instrument components (CCDs, filter wheels, calibration units) via EPICS IOCs.

##### 3.2.2 Software Interfaces
*   **EI-SW-01:** The high-level control applications shall communicate with the low-level IOCs via the EPICS Channel Access protocol.
*   **EI-SW-02:** The data transfer subsystem shall interface with the observatory archive system using a defined protocol (e.g., secure FTP, custom API).

##### 3.2.3 Communication Interfaces
*   **EI-COM-01:** The system shall support remote connections over TCP/IP networks.
*   **EI-COM-02:** The remote user interface shall implement data compression and selective updating to function within constrained bandwidth limits.

#### 3.3 Performance Requirements
*   **PR-01: Control Loop Timing**
    Critical real-time control loops (e.g., guiding, mirror control) executed on the VxWorks IOCs shall have a deterministic update rate of ≤ 1 millisecond.
*   **PR-02: Command Response**
    The system shall acknowledge high-level user commands (e.g., "slew to target") within 500 milliseconds.
*   **PR-03: Data Write Speed**
    The system shall be capable of writing FITS data to local disk at a rate sufficient to handle the maximum data output of the supported instruments without loss.
*   **PR-04: System Availability**
    The core control system shall have an operational availability of 99.5% during scheduled observing time.

#### 3.4 Design Constraints
*   **DC-01: EPICS Architecture**
    The system shall be designed according to the distributed client/server model prescribed by EPICS.
*   **DC-02: Real-Time Core**
    All hardware-proximal control logic shall reside within EPICS IOCs on the VxWorks RTOS.
*   **DC-03: Version Control**
    All source code, configuration files, and documentation shall be maintained in a CVS repository.

#### 3.5 Software System Attributes
*   **SSA-01: Reliability**
    The system shall implement watchdog timers and redundancy for critical IOCs to prevent single points of failure from causing uncontrolled telescope movements.
*   **SSA-02: Maintainability**
    The software shall be modular, with clear interfaces. Code shall be well-documented. Adherence to CVS use is required for change tracking.
*   **SSA-03: Portability**
    While IOCs are locked to VxWorks, the operator and engineering client applications shall be designed to run on standard Linux and/or Windows workstations.

#### 3.6 Other Requirements
*   **OR-01: Security**
    The system shall implement user authentication and authorization. Remote access shall be secured via encrypted connections. Command privileges shall be tiered based on user role (e.g., Astronomer, Operator, Engineer).
*   **OR-02: Logging**
    All user commands, system errors, alarms, and key state changes shall be timestamped and logged to a persistent, searchable system log.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Manager | | | |
| Lead Systems Engineer | | | |
| Software Lead | | | |
| Quality Assurance | | | |