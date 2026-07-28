# Software Requirements Specification (SRS)
## Gemini 8-Meter Telescopes Control System

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review
**Classification:** Proprietary

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document establishes the complete functional and non-functional requirements for the Gemini 8-Meter Telescopes (G8MT) Control System software. It serves as the definitive guide for software developers, system architects, and testers involved in the design, implementation, and validation of the telescope's control and data acquisition systems. The primary goal is to enable the efficient, reliable, and automated acquisition of astronomical data.

#### 1.2 Document Conventions
*   **Requirements:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Keywords:** "Shall" indicates a mandatory requirement. "Should" indicates a goal or desirable feature. "May" indicates an optional capability.
*   **Acronyms:**
    *   **G8MT:** Gemini 8-Meter Telescopes
    *   **TCS:** Telescope Control Software
    *   **ICS:** Instrument Control Software
    *   **OCS:** Observatory Control Software
    *   **IOC:** Input/Output Controller
    *   **BIT:** Built-In Test
    *   **FITS:** Flexible Image Transport System
    *   **CVS:** Concurrent Versions System

#### 1.3 Intended Audience and Reading Suggestions
This document is intended for:
*   **Software Developers & Architects:** To understand system capabilities and design constraints.
*   **Project Managers:** To track requirement implementation.
*   **Test Engineers:** To develop verification and validation plans.
*   **System Integrators:** To understand component interfaces.

It is not intended as an end-user manual for astronomers.

#### 1.4 Project Scope
The scope of this SRS encompasses the software required to control the Gemini 8-meter telescopes and their instruments, including:
*   High-level observation sequencing and scheduling.
*   Low-level real-time control of telescope and instrument hardware.
*   Data acquisition, pre-processing, and storage.
*   System monitoring, fault management, and error recovery.
*   User interfaces for operators, observers, and support staff.
*   Configuration management and support tools.

Excluded from scope are:
*   The design of the physical telescope and instrument hardware.
*   Offline scientific data reduction and analysis pipelines.
*   Detailed design of network or computing infrastructure hardware.

#### 1.5 References
*   Gemini Observatory High-Level Operational Concept Document.
*   G8MT Hardware Interface Control Documents (ICDs) - To be defined.
*   FITS Standard Document (NASA/Science Office of Standards and Technology).

### 2. Overall Description

#### 2.1 Product Perspective
The G8MT Control System is a component within the larger Gemini Observatory ecosystem. It interfaces with:
*   **Hardware:** Telescope mount, mirrors, drives, encoders, instruments, detectors, environmental sensors.
*   **External Systems:** Weather station, site monitoring, time servers, archival storage systems.
*   **Users:** Via multiple role-based graphical and programmatic interfaces.

The system is envisioned as a distributed, networked application following a client-server model, with critical real-time components running on dedicated IOCs.

#### 2.2 Product Functions (High-Level)
1.  **System Initialization & Configuration:** Boot, self-test, and bring all subsystems to a known operational state.
2.  **Observation Management:** Accept, validate, queue, schedule, and execute observing programs.
3.  **Real-Time Control:** Precisely point the telescope and configure instruments based on sequenced commands.
4.  **Data Handling:** Acquire detector data, apply pre-processing, format, compress, and store it reliably.
5.  **Monitoring & Alarming:** Continuously monitor subsystem health and status, generating alerts for faults.
6.  **Error Handling & Recovery:** Detect failures and execute procedures to reconfigure or safely halt operations.
7.  **User Interaction:** Provide role-specific interfaces for control, monitoring, and maintenance.

#### 2.3 User Classes and Characteristics
| User Class | Primary Goal | Technical Expertise | Typical Access |
| :--- | :--- | :--- | :--- |
| **Astronomer** | Execute science plan, assess data quality. | High in science, variable in operations. | Remote or local; high-level sequencer interface. |
| **Science Observer** | Ensure data integrity and plan execution. | High in instrument and data quality. | Local control room; monitoring and validation tools. |
| **Telescope Operator** | Ensure system safety and performance. | Expert in telescope operations and procedures. | Local control room; direct control interfaces. |
| **Support Personnel** | Maintain, repair, and configure hardware/software. | Expert in specific subsystems. | Direct engineering access, possibly during downtime. |
| **Developer** | Create, test, and upgrade software modules. | Expert in software engineering and domain. | Development and test environments. |
| **Administrator** | Manage system resources, schedules, and health. | High in system administration and operations. | Administrative interfaces and tools. |

#### 2.4 Operating Environment
*   **Hardware:** To be finalized (see Undecided Issues). Will include real-time IOCs, control workstations, monitoring nodes, data servers, and network infrastructure.
*   **Software:** Will rely on G8MT standards for online software and development environment (to be defined). Expected to include a real-time OS for IOCs, UNIX/Linux for workstations and servers, and commercial/off-the-shelf middleware where appropriate.
*   **Network:** Local high-speed network for control and data, with potentially lower-bandwidth links for remote operations.

#### 2.5 Design and Implementation Constraints
1.  **Modularity:** The system shall be designed as loosely coupled, modular subsystems.
2.  **Standards Compliance:** Must adhere to G8MT software and data standards once defined.
3.  **Table-Driven Configuration:** Where possible, system behavior shall be controlled by configuration tables, not code.
4.  **Legacy Compatibility:** Must support a stable interface for "visitor" instruments not built to the latest standards.
5.  **Safety:** Software shall incorporate and enforce hardware safety interlocks.

#### 2.6 User Documentation
*   Online Help integrated into control interfaces.
*   System Administrator's Guide.
*   Software Developer's Guide and API Documentation.
*   Operator and Observer Procedures Manual.

#### 2.7 Assumptions and Dependencies
*   The underlying telescope and instrument hardware will meet its specified performance criteria.
*   G8MT software and data standards will be established prior to detailed design.
*   Adequate network bandwidth will be provisioned for critical control and data flows.

### 3. System Features and Requirements

#### 3.1 Feature: System Initialization & Control
**Description:** The system must initialize from a powered-off or reset state to a ready-for-operations condition.

*   `FR-010` The system shall perform a power-on self-test (POST) of core computing hardware upon startup.
*   `FR-011` The system shall download the latest operational software and configuration to all IOCs.
*   `FR-012` The system shall initialize all telescope and instrument subsystems to a predefined "safe" or "parked" state.
*   `FR-013` The system shall report the status (OK, WARNING, FAILED) of each subsystem after initialization to the OCS.
*   `FR-014` The system shall allow an operator to start, stop, and restart individual software subsystems without a full reboot.

#### 3.2 Feature: Observation Planning & Queue Management
**Description:** Users shall create and submit observing programs, which are managed in a queue by a scheduler.

*   `FR-020` The system shall provide a tool (or interface) for creating computer-executable science programs, specifying targets, instrument configurations, and exposure sequences.
*   `FR-021` The system shall include a telescope and instrument simulator to allow testing of science programs offline.
*   `FR-022` The system shall maintain a queue of observation programs submitted for execution.
*   `FR-023` The scheduler shall prioritize and select programs from the queue based on: target visibility, instrument configuration, weather conditions, and program priority.
*   `FR-024` The system shall support both "classical" (immediate, interactive) and "queue-based" (scheduled, automated) observing modes.

#### 3.3 Feature: Observation Execution
**Description:** The system shall execute observing sequences by controlling the telescope and instruments.

*   `FR-030` The automatic sequencer shall interpret a science program and generate low-level commands for the TCS and ICS.
*   `FR-031` The TCS shall accept commands to point the telescope at specified celestial coordinates with a defined tracking mode.
*   `FR-032` The ICS shall accept commands to configure all instrument parameters (filters, gratings, detector modes, etc.).
*   `FR-033` The sequencer shall send a command to initiate an exposure and await confirmation of completion from the instrument.
*   `FR-034` The system shall provide a "pass-through" mode where manual operator commands are passed directly to the TCS/ICS without sequencer intervention.

#### 3.4 Feature: Data Acquisition & Storage
**Description:** The system shall acquire data from detectors, process it, and store it permanently.

*   `FR-040` The system shall read raw detector data from instrument interfaces.
*   `FR-041` The system shall apply mandatory pre-processing (e.g., bias subtraction, linearity correction) as defined by the instrument configuration.
*   `FR-042` The system shall package the data and comprehensive header metadata into standard FITS files.
*   `FR-043` The system shall compress data using a loss-less algorithm before storage.
*   `FR-044` The system shall write the final data product to at least two separate physical storage systems concurrently.
*   `FR-045` The system shall generate a unique, persistent `Exposure_ID` for each dataset and record it in the observational database.

#### 3.5 Feature: System Monitoring & Fault Management
**Description:** The system shall continuously monitor its state and respond to faults.

*   `FR-050` All software subsystems shall report their status (health, state, key parameters) to a central monitoring service at a configurable rate.
*   `FR-051` The system shall compare sensor readings and states against predefined normal operating ranges.
*   `FR-052` Upon detecting a parameter out of range or a subsystem failure, the system shall generate a fault message with: `Subsystem_ID`, timestamp, severity, and problem description.
*   `FR-053` Faults shall be displayed to the operator and logged to a persistent engineering database.
*   `FR-054` For critical faults, the system shall automatically execute a predefined safeing procedure (e.g., stop tracking, close shutter, park instrument).

#### 3.6 Feature: Error Recovery & Reconfiguration
**Description:** The system shall attempt to recover from failures and continue operations.

*   `FR-060` The system shall provide a library of predefined recovery procedures for common subsystem failures.
*   `FR-061` Upon non-critical subsystem failure, the system shall attempt to reconfigure operations to use redundant components or bypass the failure if possible.
*   `FR-062` The goal for automated recovery and resumption of observations after a non-critical fault shall be less than 5 minutes.
*   `FR-063` The system shall allow an operator to manually initiate and guide recovery procedures.

#### 3.7 Feature: User Access & Security
**Description:** Access to system functions shall be controlled based on user role and context.

*   `FR-070` All users shall authenticate with a unique user ID and credentials.
*   `FR-071` The system shall implement an Access Mode Allocation system that grants permissions based on: User Role, Operational Level (e.g., Daytime, Nighttime), and Location (e.g., Local, Remote).
*   `FR-072` The Telescope Operator shall always have the ability to override automated sequences and assume direct control for safety purposes.
*   `FR-073` Support personnel shall be able to access a dedicated maintenance mode for diagnostics, which locks out operational commands from other users.
*   `FR-074` All access attempts and privilege escalations shall be logged.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Operator Interface:** Graphical UI with real-time status displays, alarm panels, and direct control widgets. Must update status displays within 4 seconds (`NFR-010`).
*   **Sequencer Interface:** For Astronomers/Science Observers. Simplified, form-based interface for loading and monitoring science programs. Must be "simple and safe" as per user story.
*   **Engineering Interface:** For Support/Developers. Lower-level access to subsystem parameters, log viewers, and test harnesses.

#### 4.2 Hardware Interfaces
*   Interfaces to telescope drives, encoders, mirror controllers, and instrument mechanisms via IOCs.
*   Interfaces to detector readout electronics (technology to be defined).
*   Interfaces to environmental sensors (temperature, pressure, wind).

#### 4.3 Software Interfaces
*   **Database Interface:** To observational and engineering databases (schema defined in Domain Data Elements).
*   **Scheduling Interface:** API for submitting and managing programs in the queue.
*   **External System Interfaces:** To weather station, time server, and archival storage systems.

#### 4.4 Communications Interfaces
*   Inter-process communication (IPC) between software modules (e.g., CORBA, EPICS Channel Access).
*   Network protocols for communication with IOCs and between workstations.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-010` The system shall provide acknowledgment (accept/reject) of any control command entered at an operator workstation within 2 seconds.
*   `NFR-011` Status displays at local control stations shall be updated with new information from subsystems within 4 seconds.
*   `NFR-012` The data acquisition pipeline shall be capable of handling the maximum expected data rate from the largest planned detector without loss.

#### 5.2 Safety & Reliability Requirements
*   `NFR-020` The total system downtime due to software or software-handled hardware failures shall not exceed 2% of scheduled observing time (requirement), with a goal of 1% (~15 minutes per night).
*   `NFR-021` No single software failure shall cause irrecoverable damage to telescope or instrument hardware.

#### 5.3 Scalability & Capacity Requirements
*   `NFR-030` The system architecture shall support simultaneous operation from up to six (6) active control nodes and two (2) monitoring nodes without appreciable performance degradation.

#### 5.4 Maintainability & Supportability Requirements
*   `NFR-040` Software shall be designed with high modularity. Subsystems shall be table-driven where possible.
*   `NFR-041` Each major software subsystem shall include Built-In Test (BIT) facilities and a corresponding software simulator module for offline testing.
*   `NFR-042` A formal supportability plan, addressing maintenance levels, personnel skills, and support equipment, shall be delivered with the system.

#### 5.5 Security Requirements
*   `NFR-050` The Access Mode Allocation system (`FR-071`) shall be the primary security mechanism.
*   `NFR-051` The system shall provide intrusion protection for the astronomical and engineering databases.
*   `NFR-052` All network communication for critical control shall be secure and authenticated.

### 6. Data Model & Lifecycle
*(Derived from Domain Data Elements)*
```yaml
Science_Program:
  primary_key: Program_ID
  attributes: [Astronomer_ID, Target_Coordinates, Instrument_Config, Exposure_Sequence, Scheduling_Priority, Creation_Date, Status]

Observation:
  primary_key: Exposure_ID
  attributes: [Program_ID, Timestamp, Instrument_ID, Detector_Data_Path, Header_Metadata]

Subsystem:
  primary_key: Subsystem_ID
  attributes: [Status, Config_Parameters, Software_Version, Log_Pointer]

User_Session:
  primary_key: Session_ID
  attributes: [User_ID, Location, Access_Mode, Assigned_Resources, Login_Time]
```

### 7. Appendices

#### Appendix A: Glossary
*   **IOC:** Input/Output Controller. A dedicated computer responsible for low-level, real-time control of hardware.
*   **Sequencer:** The software component that translates high-level observation scripts into low-level TCS/ICS commands.
*   **OCS:** Observatory Control Software. The overarching software layer coordinating telescope, instrument, and facility systems.

#### Appendix B: Analysis Models
*To be developed during design phase (e.g., State diagrams for telescope, Use Case diagrams for key processes).*

#### Appendix C: Issues & TBDs (Undecided Issues)
1.  Definition of the G8MT standard for acquisition and storage of detector data.
2.  Choice of link technology for high-speed detector data transfer.
3.  Final hardware specification for development and target systems.
4.  G8MT standards for online software and the development environment.
5.  The detailed content of the formal supportability plan.
6.  Descriptions and software access requirements for star catalogs.

#### Appendix D: Risks & Mitigations
| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| Single-point hardware failures | Medium | High | Implement redundancy and software retry procedures. Design for reconfiguration. |
| Software standards evolution breaking visitor instrument compatibility | Medium | Medium | Define a stable, long-lived interface subset for visitors. Case-by-case handling for extras. |
| Insufficient network bandwidth for remote ops | Medium | Low/Medium | Design for minimal bandwidth use, employ compression. Accept variable transparency. |
| High complexity leading to unreliable software | High | High | Enforce modularity, use COTS, apply strict configuration control (CVS). |
| Cascading failures across subsystems | Medium | High | Design for subsystem autonomy. Isolate communication links and shared resources. |

---
*Document End*