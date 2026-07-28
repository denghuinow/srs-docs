# Software Requirements Specification (SRS)
## EVLA Correlator Backend System
**Document Version:** 1.0
**Date:** [Date of Generation]
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Expanded Very Large Array (EVLA) Correlator Backend System. This system is a mission-critical, real-time data processing pipeline responsible for receiving, assembling, processing, and formatting astronomical correlation data for scientific analysis and archiving. The intended audience includes stakeholders, project managers, system architects, software developers, and testers.

#### 1.2 Scope
The EVLA Correlator Backend System is positioned between the Correlator and the End-to-End (e2e) archive system. Its core responsibility is the real-time transformation of raw correlator lag data into processed spectral data, delivered to the archive.

**In-Scope Elements:**
*   Real-time reception and assembly of correlator lag data packets into time-ordered series.
*   Execution of core signal processing (Fourier Transforms) and configurable optional processing steps.
*   Formatting of processed spectral data into the prescribed output format for the e2e system.
*   Comprehensive system health monitoring, error detection, logging, and automated recovery procedures.
*   Bidirectional communication with the external Monitor and Control (M&C) system for command reception, status reporting, and auxiliary data ingestion.

**Out-of-Scope Elements:**
*   Direct user interfaces (all interaction is via the M&C system).
*   Spectral "stitching" across different correlator sub-bands.
*   Long-term data storage and management (e2e system responsibility).
*   Generation of raw correlator lag data or auxiliary observational data (e.g., weather, pointing).
*   Final synthesis of visibility data from individual baseline data.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **EVLA:** Expanded Very Large Array
*   **e2e:** End-to-End (archive system)
*   **M&C:** Monitor and Control System
*   **RFI:** Radio Frequency Interference
*   **Lag Data:** The raw, time-domain correlation products output by the correlator.
*   **Spectral Data:** The frequency-domain data produced after applying a Fourier Transform to lag data.
*   **Real-Time:** Processing that keeps pace with the incoming data stream without introducing unbounded latency or data loss.
*   **Mission-Critical:** A system whose failure results in the permanent loss of valuable, irrecoverable data (astronomical observations).

#### 1.4 References
*   EVLA System Architecture Overview
*   e2e Archive System Data Format Specification
*   M&C System Interface Control Document (ICD)
*   Correlator Output Data Specification

#### 1.5 Overview
The remainder of this SRS is organized as follows:
*   **Section 2:** Overall Description of the system, its context, and high-level operation.
*   **Section 3:** Specific Requirements detailing functional, interface, performance, and other attributes.
*   **Appendices:** For supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
The Backend System is a component within the larger EVLA data pipeline. It is a standalone software system with dependencies on external hardware (compute nodes, network) and external systems (Correlator, M&C, e2e Archive).

**System Context Diagram:**
```
[Correlator] --(Lag Data ~1.6 GB/s)--> [EVLA Backend System] --(Spectral Data ~25 MB/s)--> [e2e Archive]
         ^                                                                       ^
         |                                                                       |
         |--(Status/Control Data)-----------[M&C System]------------(Status/Control Data)---|
```
*   **Correlator:** Source of the primary input data stream.
*   **M&C System:** Provides commands, configuration (observational parameters), auxiliary data, and is the sole conduit for user interaction and system status monitoring.
*   **e2e Archive:** The final destination for all processed science data.

#### 2.2 Product Functions (High-Level)
1.  **Data Ingestion & Assembly:** Receive UDP/TCP packets containing lag data from the Correlator and assemble them into complete, time-ordered integration blocks.
2.  **Core Processing:** Apply a Fourier Transform to convert lag data blocks into spectral data.
3.  **Optional Processing:** Apply user-selectable processing steps (e.g., spectral windowing, flagging) as configured via M&C.
4.  **Data Formatting & Export:** Package processed spectral data into the specified format and transmit it reliably to the e2e archive system.
5.  **System Management:** Monitor health, log events, handle errors, execute recovery procedures, and communicate status to the M&C system.
6.  **Command & Control:** Receive and act upon operational commands (start, stop, reconfigure) from the M&C system.

#### 2.3 User Characteristics
| Stakeholder | Primary Interaction | Skill Level |
| :--- | :--- | :--- |
| **Array Operator** | Via M&C GUI. Monitors system health, acknowledges alerts, initiates standard procedures. | Expert in observatory operations, not necessarily in backend software. |
| **Engineer/Technician** | Via diagnostic tools & logs. Performs hardware/software maintenance and troubleshooting. | High technical skill in relevant hardware and software systems. |
| **Astronomer/Scientist** | Via M&C GUI. Configures optional processing parameters for their specific observation. | Expert in radio astronomy data and processing needs. |
| **Software Developer** | Via development tools, logs, and debugging interfaces. Maintains and extends the system software. | Expert software engineer with knowledge of real-time systems. |
| **System Administrator** | Via system configuration tools and access control lists. Manages OS, security, and user permissions. | Expert in system administration and security. |

#### 2.4 Constraints
1.  **Mission-Critical Operation:** The system must be designed for maximum availability. Data loss is unacceptable.
2.  **Processing Reversibility:** The data processing chain must be mathematically reversible or accompanied by sufficient metadata to reconstruct the raw input from the final output.
3.  **Performance Limitations:** Design is bounded by available CPU/GPU power, memory bandwidth, network throughput, and software algorithm efficiency.
4.  **External System Resilience:** The system must buffer data and continue core processing during temporary losses of connection to the e2e archive or M&C system without data loss.
5.  **Open-Source Preference:** All software and operating system components should use industry-standard, preferably open-source, technologies to ensure maintainability and reduce vendor lock-in.
6.  **Correlator Mode Changes:** The system must dynamically adapt to changes in the correlator's operational mode (e.g., bandwidth, spectral resolution) as signaled via M&C.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** The Correlator output data format and network protocol are stable and well-defined.
*   **Assumption:** The M&C system provides a reliable, well-documented interface for command and status exchange.
*   **Assumption:** The e2e archive system can accept data at the sustained output rate and provides a confirmation mechanism.
*   **Dependency:** Availability of sufficient computational hardware meeting minimum performance specifications.
*   **Dependency:** A stable, high-bandwidth, low-latency network infrastructure.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Data Input & Assembly (REQ-F-100)
*   **REQ-F-101:** The system shall receive lag data packets from the Correlator via a dedicated, high-speed network interface.
*   **REQ-F-102:** The system shall assemble incoming packets into complete integration blocks based on embedded sequence numbers and timestamps.
*   **REQ-F-103:** The system shall detect and log packet loss or corruption from the Correlator.
*   **REQ-F-104:** The system shall re-order time-series data as necessary to ensure chronological processing.

##### 3.1.2 Core Data Processing (REQ-F-200)
*   **REQ-F-201:** The system shall apply a Fourier Transform to each assembled block of lag data to produce a corresponding block of complex spectral data.
*   **REQ-F-202:** The processing shall be mathematically reversible, preserving all information necessary to reconstruct the original lag data.
*   **REQ-F-203:** The system shall apply configuration parameters (e.g., normalization factors) received from the M&C system during processing.

##### 3.1.3 Optional Data Processing (REQ-F-300)
*   **REQ-F-301:** The system shall allow the selection of optional processing algorithms (e.g., Hanning window, spectral averaging) via parameters from the M&C system.
*   **REQ-F-302:** The system shall apply the selected optional processing steps to the spectral data in a defined, configurable order.
*   **REQ-F-303:** All applied processing steps and their parameters shall be recorded in the output data metadata.

##### 3.1.4 Data Output & Export (REQ-F-400)
*   **REQ-F-401:** The system shall format the processed spectral data and its complete metadata into the structure specified by the e2e archive interface.
*   **REQ-F-402:** The system shall transmit the formatted data blocks to the e2e archive system via a reliable protocol (e.g., TCP with acknowledgment).
*   **REQ-F-403:** The system shall implement a retry mechanism with local buffering to handle temporary e2e archive unavailability without data loss.

##### 3.1.5 Monitor & Control Interface (REQ-F-500)
*   **REQ-F-501:** The system shall receive, validate, and execute operational commands (START, STOP, RECONFIGURE, SHUTDOWN) from the M&C system.
*   **REQ-F-502:** The system shall provide a continuous, real-time status stream to the M&C system, including: health (OK, WARNING, ERROR), processing state, data rates, and buffer utilization.
*   **REQ-F-503:** The system shall ingest and utilize auxiliary data (e.g., timestamp corrections, antenna positions) provided by the M&C system, embedding it into the output metadata.
*   **REQ-F-504:** The system shall report all errors and significant events (alerts) to the M&C system with a severity level (INFO, WARNING, ERROR, CRITICAL).

##### 3.1.6 System Management & Resilience (REQ-F-600)
*   **REQ-F-601:** The system shall perform continuous self-monitoring of critical resources (CPU, memory, disk space, network links, process health).
*   **REQ-F-602:** Upon detection of a non-fault condition (e.g., e2e archive timeout), the system shall engage automated recovery procedures (e.g., increase buffering, retry connection) and alert the M&C system.
*   **REQ-F-603:** The system shall maintain detailed operational logs, accessible remotely for debugging.
*   **REQ-F-604:** The system shall support a "standby" or "idle" state from which it can resume full processing with minimal delay upon command.

#### 3.2 Interface Requirements

##### 3.2.1 Correlator Interface
*   **Protocol:** UDP or TCP, as defined by the Correlator ICD.
*   **Data Rate:** Minimum sustained 1.6 Gigabytes per second.
*   **Data Format:** As per Correlator Output Data Specification.

##### 3.2.2 M&C System Interface
*   **Protocol:** Defined by M&C ICD (e.g., CORBA, DDS, custom TCP).
*   **Commands:** Must accept the set defined in the M&C ICD.
*   **Status:** Must provide the status fields defined in the M&C ICD.
*   **Auxiliary Data:** Must accept and process all data structures defined in the M&C ICD.

##### 3.2.3 e2e Archive Interface
*   **Protocol:** Reliable stream (e.g., TCP).
*   **Data Rate:** Minimum sustained 25 Megabytes per second.
*   **Data Format:** As per e2e Archive Data Format Specification.

#### 3.3 Performance Requirements
*   **REQ-P-001:** The system shall sustain a **minimum input data rate of 1.6 GB/s** and a **minimum output data rate of 25 MB/s** without dropping data or introducing unbounded latency.
*   **REQ-P-002:** The end-to-end processing latency (from receipt of final packet of an integration to the start of its transmission to e2e) shall be deterministic and documented.
*   **REQ-P-003:** System availability target: **99.95%** in any rolling 30-day period, excluding scheduled maintenance and total power failure.
*   **REQ-P-004:** The system shall be capable of **indefinite operation** (weeks/months) without requiring a restart due to software issues like memory leaks.
*   **REQ-P-005:** Command response time from M&C system to acknowledged execution shall be less than 1 second for critical commands (STOP, RECONFIGURE).

#### 3.4 System Attributes

##### 3.4.1 Reliability, Availability, and Maintainability (RAM)
*   **REQ-RAM-001:** The system shall implement hardware redundancy (e.g., power supplies, network paths) where single points of failure would cause data loss.
*   **REQ-RAM-002:** Software components shall be designed for graceful degradation and restartability without affecting unrelated processing threads.
*   **REQ-RAM-003:** Comprehensive remote diagnostic tools shall be provided to Engineers for troubleshooting hardware and software state.

##### 3.4.2 Security
*   **REQ-SEC-001:** All external interfaces (M&C, e2e) shall require authentication.
*   **REQ-SEC-002:** The System Administrator shall be able to define role-based access controls (RBAC) for operators, engineers, and scientists via integration with the M&C system's security model.
*   **REQ-SEC-003:** System logs shall be protected from unauthorized modification or deletion.

##### 3.4.3 Portability & Open Source Compliance
*   **REQ-PORT-001:** The application software shall be designed to run on a standard Linux distribution (e.g., RHEL, Rocky Linux).
*   **REQ-PORT-002:** Where possible, the system shall utilize open-source libraries and tools (e.g., FFTW, HDF5).

#### 3.5 Other Requirements
*   **REQ-O-001:** The system shall be delivered with comprehensive documentation, including installation, administration, and API guides.
*   **REQ-O-002:** A detailed test plan, demonstrating compliance with all performance and functional requirements, shall be part of the delivery.

### 4. Appendices

#### 4.1 Undecided Issues (TBD)
The following issues require resolution and will be incorporated into a future revision of this SRS:
1.  **Buffer Sizing:** The specific amount of excess memory/disk storage required for buffering during external system outages.
2.  **Auxiliary Data Grace Period:** The maximum duration the system can operate correctly without receiving updated auxiliary data (e.g., pointing) from the M&C system.
3.  **Standby Recovery Time:** The maximum acceptable delay (e.g., 30 seconds, 5 minutes) when resuming full processing from a standby/idle state.
4.  **Internal Data Structures:** The final design of internal data buffers, parameter tables, and metadata containers.
5.  **Optional Algorithm Catalog:** The definitive list and specification of optional time/frequency domain processing algorithms to be implemented in the first release.

#### 4.2 User Stories Mapped to Requirements
| User Story | Mapped Requirements |
| :--- | :--- |
| **Array Operator:** Clear error/status messages. | REQ-F-504, REQ-F-502 |
| **Engineer:** Remote diagnostic tools. | REQ-F-603, REQ-RAM-003 |
| **Astronomer:** Select optional processing. | REQ-F-301, REQ-F-302 |
| **Software Developer:** Remote logs/debugging. | REQ-F-603 |
| **System Administrator:** Manage privileges. | REQ-SEC-002 |