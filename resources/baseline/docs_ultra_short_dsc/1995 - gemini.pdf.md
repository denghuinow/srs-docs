# Software Requirements Specification (SRS)
## For the Gemini 8-meter Telescopes Control and Data Acquisition System

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

## 1. Introduction

### 1.1 Purpose
This document defines the requirements for the Gemini 8-meter Telescopes Control and Data Acquisition (GCDA) software. It serves as the authoritative specification for developers, testers, and project managers. The primary purpose of the GCDA system is to enable the efficient acquisition of astronomical data by providing integrated control of the telescope, its instruments, and auxiliary systems.

### 1.2 Scope
The scope of this SRS encompasses the core control and data acquisition software, including its subsystems for sequencing, scheduling, monitoring, data handling, and fault management. It defines the required interfaces to commercial and public-domain software (e.g., analysis packages, databases, archives) but does not specify the requirements for those external systems themselves. The software is intended for use by control system developers, telescope operators, and support personnel, not directly by astronomer end-users for scientific analysis.

### 1.3 Definitions, Acronyms, and Abbreviations
*   **GCDA:** Gemini Control and Data Acquisition
*   **IOC:** Input/Output Controller (embedded VxWorks node)
*   **EPICS:** Experimental Physics and Industrial Control System
*   **LAN/WAN:** Local/Wide Area Network
*   **POSIX:** Portable Operating System Interface
*   **DBMS:** Database Management System
*   **VME:** Versa Module Europa (computer bus standard)
*   **Interactive Observing:** Mode where an operator directly commands the telescope in real-time.
*   **Queue Observing:** Primary operational mode where pre-defined observation programs are executed by a scheduler with minimal human intervention.
*   **Sequencer:** Software component that executes a pre-programmed series of commands for an observation.

### 1.4 References
*   Gemini Project Operational Concepts Document
*   EPICS Toolkit Documentation
*   POSIX Standards (IEEE Std 1003.1)
*   Unresolved External Standards Action Items (Data Storage, Transfer Links)

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 specifies the detailed system requirements, both functional and non-functional. Appendices may contain supplementary information.

## 2. Overall Description

### 2.1 Product Perspective
The GCDA system is the core, mission-critical software layer for the Gemini telescopes. It logically follows the project's Operational Concepts document. It operates within a larger ecosystem, integrating with telescope hardware (mount, mirrors, enclosures), instrument hardware (detectors, spectrographs), and external software systems (archives, data reduction packages). The system is middleware, providing a unified framework for control and data flow.

### 2.2 Product Functions
The high-level functions of the GCDA system are:
1.  To support multiple astronomical observing modes.
2.  To schedule and sequence complex science observations autonomously.
3.  To facilitate remote monitoring and control operations.
4.  To manage and coordinate multiple scientific instruments.
5.  To acquire, process, store, and transmit scientific and engineering data.
6.  To maintain a centralized, real-time status and configuration database.
7.  To detect, log, notify, and assist in recovery from system faults.

### 2.3 User Characteristics
| User Role | Expertise | Primary Interaction |
| :--- | :--- | :--- |
| **Astronomer (Principal Investigator)** | Expert in science goals, not control systems. | Submits observing program; monitors data acquisition via high-level sequencer/scheduler interface. No direct hardware control. |
| **Science Observer** | Trained in data acquisition integrity and instrument performance. | On-site role monitoring the quality of incoming data, may request sequence adjustments. |
| **Telescope Operator** | Expert in telescope and instrument operations. | On-site controller with direct command privileges. Manages real-time operations, handles anomalies, performs calibrations. |
| **Support Staff / Developer** | Expert in software and hardware systems. | Maintains, tests, and develops the system. Has high-level access for diagnostics, simulation, and software updates. |

### 2.4 Constraints
*   **Development Standards:** Must use UNIX (POSIX-compliant OS), X-windows for GUI, Tcl/Tk for GUI scripting, VxWorks on IOCs, and the EPICS control system toolkit.
*   **Software Reuse:** Must utilize commercial off-the-shelf (COTS) and public-domain software where feasible and effective.
*   **Portability:** Software shall be hardware-independent where possible, ensuring longevity and ease of hardware upgrades.
*   **External Dependencies:** System design is dependent on the final definition of external standards for detector data formats and high-speed transfer links (see Unresolved Action Items).

### 2.5 Assumptions and Dependencies
*   It is assumed that sufficient network bandwidth (both LAN and WAN) is provisioned to support the full functionality of remote operations.
*   The system depends on the underlying hardware (VME crates, microprocessors, network switches) being operational and performing to specification.
*   The system assumes the existence of defined external interfaces (e.g., to the STARCAT archive) which will provide specific APIs or protocols for integration.

### 2.6 Apportioning of Requirements
*   **High Priority (Phase 1):** Interactive observing mode, basic telescope and instrument control, core data acquisition and storage, operator GUI.
*   **Medium Priority (Phase 2):** Queue-based observing scheduler and sequencer, advanced data handling (compression, transmission), remote monitoring capabilities.
*   **Lower Priority (Phase 3):** Enhanced fault recovery automation, comprehensive simulation modules for all subsystems, advanced service observing features.

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 User Interfaces
*   **UI.1:** The system shall provide a graphical user interface (GUI) for control and monitoring.
*   **UI.2:** The GUI shall have a homogeneous "look and feel" across all telescope and instrument control subsystems.
*   **UI.3:** The GUI shall be portable across standard UNIX workstation platforms (e.g., Sun SPARC, HP-UX, Linux).
*   **UI.4:** The GUI shall be network-transparent, allowing any authorized interface to connect to any control server from anywhere on the control network.

#### 3.1.2 Hardware Interfaces
*   **HW.1:** The system shall interface with standard VME-based control electronics.
*   **HW.2:** The system shall provide software skeleton frameworks and device support modules for embedded microprocessors (IOCs) to standardize hardware integration.
*   **HW.3:** The system shall interface with a dedicated time distribution bus for system-wide time synchronization.

#### 3.1.3 Software Interfaces
*   **SI.1:** The system shall provide an interface for quick-look data analysis packages (e.g., PV-Wave, IDL) to access recent science data.
*   **SI.2:** The system shall interface with the Gemini archive system (STARCAT) for the permanent storage of science and engineering data.
*   **SI.3:** The system shall interface with standard star catalog services.
*   **SI.4:** The system shall interface with a commercial DBMS (e.g., Oracle, PostgreSQL) for the system-wide parameter and status database.

#### 3.1.4 Communications Interfaces
*   **CI.1:** Internal control communications shall use a standard TCP/IP-based control LAN.
*   **CI.2:** The system shall support secure WAN connections for remote operations from designated facilities.
*   **CI.3:** High-volume detector data shall be transported via specialized high-speed data buses (e.g., reflective memory).

### 3.2 Functional Requirements

#### 3.2.1 Observing Modes
*   **FUN-OM.1:** The system shall support **Interactive Observing**, allowing a Telescope Operator to issue direct, real-time commands.
*   **FUN-OM.2:** The system shall support **Queue Observing**, where a scheduler selects and a sequencer executes pre-defined observation programs from a ranked queue.
*   **FUN-OM.3:** The system shall support **Remote Observing**, allowing authorized users to monitor and control observations from an off-site location.
*   **FUN-OM.4:** The system shall support **Service Observing**, where staff execute programs on behalf of an absent astronomer.

#### 3.2.2 Scheduling and Sequencing
*   **FUN-SQ.1:** The system shall provide a **Scheduler** that selects the next observation from the queue based on target visibility, weather conditions, program priority, and instrument configuration.
*   **FUN-SQ.2:** The system shall provide a **Sequencer** capable of executing an observation program, which is a scripted series of telescope, instrument, and data acquisition commands.
*   **FUN-SQ.3:** The sequencer shall be able to pause, resume, or abort an observation sequence based on operator input or automatic fault conditions.

#### 3.2.3 Instrument Control and Coordination
*   **FUN-IC.1:** The system shall be able to control and monitor multiple instruments mounted on the telescope concurrently.
*   **FUN-IC.2:** Only one instrument shall be in the "active" (acquiring science data) state at any given time. The system shall manage the handoff between instruments.
*   **FUN-IC.3:** The system shall load and configure instrument-specific software modules as required.

#### 3.2.4 Data Acquisition and Handling
*   **FUN-DH.1:** The system shall acquire raw detector data from the active instrument.
*   **FUN-DH.2:** The system shall acquire and record engineering data (temperatures, pressures, positions, status points) from all subsystems.
*   **FUN-DH.3:** The system shall apply lossless or lossy compression to science data as configured.
*   **FUN-DH.4:** The system shall write science and engineering data to short-term disk storage and transmit it to the long-term archive.

#### 3.2.5 Status and Configuration Database
*   **FUN-DB.1:** The system shall maintain a distributed, real-time database containing the current state, configuration, and alarm status of all controlled parameters.
*   **FUN-DB.2:** The database shall retain a historical record of parameter changes for a minimum of 7 days.

#### 3.2.6 Fault Management
*   **FUN-FM.1:** The system shall detect and classify faults from hardware and software monitors.
*   **FUN-FM.2:** The system shall generate immediate visual and auditory alarms for critical faults directed to the Telescope Operator.
*   **FUN-FM.3:** The system shall log all faults, warnings, and operational commands to a time-stamped, searchable log.
*   **FUN-FM.4:** The system shall provide documented recovery procedures for known fault conditions and allow for manual system reconfiguration.

### 3.3 Non-Functional Requirements

#### 3.3.1 Performance
*   **PERF-1:** The system shall support simultaneous operation from up to **6 active control nodes** (issuing commands) and **2 monitoring-only nodes**.
*   **PERF-2:** The system shall provide acknowledgment (acceptance or rejection) of any control command within **2 seconds** under normal load.
*   **PERF-3:** Status displays on the local control LAN shall update to reflect a changed parameter value within **4 seconds**.

#### 3.3.2 Reliability, Availability, and Maintainability
*   **RAM-1:** The total system downtime (including scheduled and unscheduled maintenance) shall not exceed **2%** per calendar year, with a goal of **1%**.
*   **RAM-2:** The system shall be designed to allow for recovery or reconfiguration from a software error condition within **5 minutes**.
*   **RAM-3:** All software modules shall be designed with modularity, encapsulation, and shall be fully documented.
*   **RAM-4:** All software shall be under version control.
*   **RAM-5:** Critical subsystems shall include self-test routines and simulation modules to allow for testing without engaging hardware.

#### 3.3.3 Data Capacity
*   **DATA-1:** The short-term storage system shall have the capacity to retain **7 days** of continuous data from the instrument with the largest data output rate.
*   **DATA-2:** Data from the most recent **3 days** shall be available for interactive access and quick-look analysis directly from online disk storage.

#### 3.3.4 Security
*   **SEC-1:** The system shall implement user authentication.
*   **SEC-2:** The system shall implement a role-based privilege model (e.g., Operator, Observer, Support, Administrator) defining allowed commands and data access.
*   **SEC-3:** The system shall be particularly hardened against unauthorized access attempts originating from the WAN. Firewalls and access control lists (ACLs) shall be employed.
*   **SEC-4:** All inter-process communication on the control network shall be secure against eavesdropping or spoofing.

#### 3.3.5 Portability
*   **PORT-1:** The core control software shall be portable across POSIX-compliant operating systems without modification.
*   **PORT-2:** The GUI shall be portable across platforms supported by standard X-windows and Tcl/Tk distributions.

### 3.4 Acceptance Criteria
Formal system acceptance will be contingent upon successful demonstration of the following:
1.  Execution of built-in test procedures for all software modules.
2.  Verification of all performance requirements (PERF-1, PERF-2, PERF-3) under simulated load.
3.  Demonstration of all four observing modes (Interactive, Queue, Remote, Service) using simulated and real hardware.
4.  Validation of data capacity requirements (DATA-1, DATA-2).
5.  A reliability run demonstrating system stability over a defined period, tracking downtime against the RAM-1 goal.
6.  A security audit confirming the implementation of SEC-1 through SEC-4 requirements.

---
**END OF DOCUMENT**