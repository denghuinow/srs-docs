# Software Requirements Specification (SRS)
## EVLA Correlator Backend System

**Document Version:** 1.0
**Date:** October 26, 2023
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the EVLA (Expanded Very Large Array) Correlator Backend System. It serves as the authoritative specification for developers, testers, project managers, and stakeholders, ensuring a common understanding of the system's capabilities, constraints, and interfaces.

#### 1.2 Scope
The EVLA Correlator Backend System is the primary real-time astronomical data processing pipeline component. It is positioned between the Correlator and the End-to-End (e2e) archive systems. Its core responsibility is to receive correlator data, assemble time-series, perform Fourier Transforms and optional processing, and deliver formatted spectral results for permanent archiving.

**In-Scope:**
*   Real-time reception of lag frame data from the Correlator.
*   Time-series assembly and core spectral processing.
*   Optional, user-configurable data processing steps.
*   Integration, formatting, and output to the e2e system.
*   System health monitoring, fault detection, and automated recovery.
*   User access control and system administration.
*   Remote diagnostics and maintenance interfaces.

**Out-of-Scope:**
*   Functionality of the upstream Correlator.
*   Functionality of the downstream e2e archive system.
*   Functionality of the external Monitor & Control (M&C) system, except for the interfaces through which it receives parameters and metadata.
*   Long-term data storage or user-facing data analysis tools.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **AIPS++:** Astronomical Information Processing System, a software suite for astronomical data processing.
*   **Baseline:** A pair of antennas; the fundamental unit for correlation.
*   **Correlator:** The upstream system that computes cross-correlation lags from antenna signals.
*   **e2e System:** The End-to-End data archive and distribution system.
*   **EVLA:** Expanded Very Large Array.
*   **FFT:** Fast Fourier Transform.
*   **Lag Frame:** A network packet containing a block of correlation data for a specific baseline and time.
*   **M&C System:** Monitor and Control System.
*   **Measurement Set (MS):** The AIPS++ standard format for interferometric data.
*   **RFI:** Radio Frequency Interference.
*   **SRS:** Software Requirements Specification.

#### 1.4 References
*   EVLA System Architecture Overview
*   Correlator Interface Control Document (ICD)
*   e2e Archive System ICD
*   M&C System ICD

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product and its operating environment. Section 3 details specific functional requirements. Section 4 outlines non-functional requirements. Appendices contain supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
The Backend System is a mission-critical, real-time data processing component within the larger EVLA data pipeline. It acts as a mediator, transforming raw correlator output into science-ready spectral data.

**System Interfaces:**
1.  **Correlator Interface:** High-speed network link (e.g., 10/40/100 GbE) for receiving a continuous stream of lag frame packets.
2.  **M&C Interface:** Network link for receiving processing parameters, observational metadata, and for transmitting system status, health, and error reports.
3.  **e2e Interface:** Network link for delivering formatted output datasets (e.g., AIPS++ Measurement Sets) to the archive.
4.  **Administrative/User Interface:** Secure network interface (SSH, Web GUI) for system configuration, monitoring, diagnostics, and maintenance by authorized personnel.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Array Operator** | Monitors overall observatory health. Non-technical user of the M&C interface. | Consolidated, high-level status and alerting via M&C. |
| **Astronomer/Scientist** | Defines the scientific goals of an observation. | Ability to select and parameterize optional data processing steps (e.g., windowing). |
| **Engineer/Technician** | Maintains system hardware/software. Deep technical knowledge. | Remote diagnostic tools, hardware status, hot-swappable components. |
| **Software Developer** | Develops and debugs system software. | Remote access, logging, debugging interfaces, and the ability to restart processes. |
| **System Administrator** | Manages system access and overall configuration. | Full system control, user/privilege management, audit logs. |
| **Web User** | Authorized external user with limited needs. | Restricted, role-based access to specific non-critical system functions or data. |

#### 2.3 Operating Environment
*   **Hardware:** A distributed cluster of high-performance compute nodes with multi-core processors, significant RAM, and high-speed interconnects (InfiniBand or high-speed Ethernet). Specialized network interface cards for data ingestion.
*   **Software:** Linux-based operating system. Middleware for parallel processing and cluster management (e.g., MPI, Slurm). Custom real-time processing applications.
*   **Physical:** Located in a controlled data center environment with stable power and cooling.

#### 2.4 Design and Implementation Constraints
1.  **Real-time Processing:** The system must process data at the incoming rate with deterministic latency. Batch processing is not acceptable.
2.  **Data Fidelity:** All processing must be mathematically reversible to preserve the ability to recover raw input from final output, ensuring scientific integrity.
3.  **Legacy Compatibility:** Output data must conform to the AIPS++ Measurement Set format or other formats specified by the e2e system ICD.
4.  **Use of COTS:** The system shall utilize Commercial Off-The-Shelf (COTS) hardware and standard networking protocols where possible to reduce cost and maintenance.

#### 2.5 Assumptions and Dependencies
*   **D-01:** The Correlator will deliver properly formatted, timestamped lag frame packets at a sustained rate.
*   **D-02:** The M&C system will provide all necessary auxiliary data (e.g., observing parameters) before and during an observation.
*   **D-03:** The e2e archive system will be ready to accept data at the specified output rate and format.
*   **A-01:** The data center provides adequate, stable power and cooling.
*   **A-02:** Sufficient network bandwidth is available between all system components.

### 3. System Features and Requirements

#### 3.1 Feature: Real-Time Data Ingestion and Assembly
**Description:** The system shall continuously receive data from the Correlator and assemble it into complete time-series for processing.

| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-010** | The system shall receive lag frame packets via a dedicated high-speed network interface. | High |
| **FR-011** | The system shall validate the integrity (e.g., via checksum) and sequence of each incoming lag frame. | High |
| **FR-012** | The system shall assemble validated lag frames into complete, correctly ordered time-series (lag sets) per baseline. | High |
| **FR-013** | The system shall buffer incoming data to accommodate transient network jitter without loss. | High |
| **FR-014** | The system shall generate an error report and attempt recovery if a lag frame is corrupted, missing, or arrives out-of-sequence. | Medium |

#### 3.2 Feature: Core Spectral Processing Pipeline
**Description:** The system shall apply mandatory processing steps to transform time-series data into the frequency domain.

| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-020** | The system shall apply necessary normalization and timestamp adjustments to the assembled lag sets. | High |
| **FR-021** | The system shall perform a power-of-two complex Fast Fourier Transform (FFT) on each lag set to produce a processed spectrum. | High |
| **FR-022** | The system shall attach relevant metadata (baseline ID, frequency channel map, timestamps) to each processed spectrum. | High |

#### 3.3 Feature: Optional Data Processing
**Description:** The system shall allow for the application of user-selected, configurable processing steps.

| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-030** | The system shall accept a user-defined sequence of optional processing steps from the M&C system. | High |
| **FR-031** | Optional processing steps shall be chainable and applicable in either the time-domain (pre-FFT) or frequency-domain (post-FFT). | High |
| **FR-032** | Example processes must include, but are not limited to: data windowing (e.g., Hanning) for RFI mitigation and bandpass correction. | Medium |
| **FR-033** | Each process shall have configurable parameters (e.g., window type, scaling factors). | Medium |
| **FR-034** | The system shall record the complete processing history, including all optional steps and parameters, in the output metadata. | High |

#### 3.4 Feature: Data Integration and Output
**Description:** The system shall integrate spectra over time and format the final data product for archiving.

| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-040** | The system shall integrate (sum) spectral data from consecutive spectra over a configurable time duration. | High |
| **FR-041** | The system shall format the integrated spectral data, along with all metadata and processing history, into a standard output dataset (e.g., an AIPS++ Measurement Set). | High |
| **FR-042** | The system shall transmit the formatted output dataset to the e2e archive system. | High |
| **FR-043** | The system shall verify successful receipt of data by the e2e system (e.g., via acknowledgment). | Medium |
| **FR-044** | The system shall buffer output data if the e2e system becomes temporarily unavailable, resending once connectivity is restored. | High |

#### 3.5 Feature: System Monitoring and Fault Management
**Description:** The system shall continuously monitor its own health and perform automatic recovery from failures.

| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-050** | The system shall continuously monitor key metrics: input/output data rates, compute node health, process status, and hardware (CPU, memory, disk, network) utilization. | High |
| **FR-051** | The system shall detect failures in software processes or hardware components. | High |
| **FR-052** | Upon detection of a failure in a non-critical component, the system shall automatically attempt to restart the failed process or failover to a standby/redundant component. | High |
| **FR-053** | The system shall generate consolidated status and error reports and forward them to the M&C system. | High |
| **FR-054** | The system shall continue lossless data processing for a specified period during temporary outages of the M&C or e2e systems by using cached parameters and output buffering. | High |

#### 3.6 Feature: Access Control and Security
**Description:** The system shall enforce secure access for all user classes.

| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-060** | All user access (remote login, web interface) shall require authentication via username and strong password or equivalent mechanism. | High |
| **FR-061** | All remote login sessions (e.g., SSH) shall use encrypted communication channels. | High |
| **FR-062** | The system shall implement role-based access control (RBAC). Privileges shall be defined for the roles: Administrator, Developer, Engineer, Web User. | High |
| **FR-063** | The Administrator shall be able to create, modify, and delete user accounts and assign roles. | High |
| **FR-064** | The system shall maintain audit logs of all user authentication attempts and privileged commands. | Medium |

#### 3.7 Feature: Maintenance and Diagnostics
**Description:** The system shall support maintenance activities with minimal operational disruption.

| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-070** | The system hardware architecture shall support hot-swappable components (e.g., compute nodes, power supplies, fans) to allow replacement without a full system shutdown. | High |
| **FR-071** | The system shall provide remote diagnostic tools allowing engineers to inspect the status of individual hardware components, view detailed system logs, and monitor internal data flows. | High |
| **FR-072** | The system software shall be modular, allowing individual processing pipelines or services to be stopped, upgraded, and restarted independently. | High |
| **FR-073** | The system shall support a "standby idle" mode for individual components or the entire system, from which it can resume full processing with minimal delay. | Medium |

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
| ID | Requirement |
| :--- | :--- |
| **NFR-001** | The system shall sustain a **minimum continuous input data rate of 1.6 Gigabytes per second (GB/s)** from the Correlator. |
| **NFR-002** | The system shall produce a **continuous output data rate of 25 Megabytes per second (MB/s)** to the e2e system. |
| **NFR-003** | End-to-end processing latency (from receipt of the last lag frame of a set to the availability of its integrated spectrum) shall be deterministic and documented. |
| **NFR-004** | The system shall process data in **real-time** without building backlog or dropping packets under specified nominal load. |

#### 4.2 Reliability, Availability, and Maintainability (RAM)
| ID | Requirement |
| :--- | :--- |
| **NFR-010** | The system shall have a target operational availability of **99.9%** (excluding scheduled maintenance). |
| **NFR-011** | The system shall implement automatic failover for critical software processes, with a failover time of less than 5 seconds. |
| **NFR-012** | The system shall be designed for **modular maintenance**, allowing partial shutdowns for upgrades without affecting the entire data pipeline. |
| **NFR-013** | All software shall be well-documented and adhere to coding standards to ensure maintainability. |

#### 4.3 Scalability Requirements
| ID | Requirement |
| :--- | :--- |
| **NFR-020** | The system's hardware architecture (compute, network, storage) shall be **expandable** to ultimately handle an input data rate of **up to 2 GB/s per correlator output channel** without a fundamental redesign. |
| **NFR-021** | The system software shall be designed to distribute processing load across additional compute nodes transparently as they are added. |

#### 4.4 Security Requirements
| ID | Requirement |
| :--- | :--- |
| **NFR-030** | The system shall enforce the **principle of least privilege** for all user accounts. |
| **NFR-031** | User passwords shall adhere to a strong password policy (minimum length, complexity). |
| **NFR-032** | The system shall be resilient to common network-based attacks (e.g., denial-of-service, intrusion attempts). |

#### 4.5 Data Integrity Requirements
| ID | Requirement |
| :--- | :--- |
| **NFR-040** | The system must preserve the full **dynamic range and fidelity** of the input scientific data throughout all processing steps. |
| **NFR-041** | All data processing algorithms (normalization, FFT, optional steps) shall be **mathematically reversible** in principle, allowing the raw input lag frames to be reconstructed from the final output spectra and metadata. |

### 5. Appendices

#### Appendix A: Undecided Issues / Open Questions
The following items require resolution during the design phase and will be updated in future revisions of this SRS:
1.  The specific capacity (in GB/TB and time) of the input and output data buffers for handling Correlator jitter and e2e system outages.
2.  The exact time duration the system can operate losslessly without connection to the e2e system.
3.  The precise amount and duration of correlator data to cache in memory upon loss of critical metadata from the M&C system.
4.  Quantitative specification for "minimal delay" (e.g., < 30 seconds) when resuming from standby idle mode.
5.  The final, approved list of optional time and frequency domain processing algorithms and their detailed mathematical specifications.
6.  The detailed hardware and software protocols for performing "hot-swap" operations on specific components (e.g., node replacement procedure).

#### Appendix B: Data Dictionary
| Data Element | Primary Key | Description | Key Attributes |
| :--- | :--- | :--- | :--- |
| **Lag Frame** | Frame ID | A network packet from the Correlator. | Frame ID, Baseline ID, Timestamp, Lag Values[], Checksum, Auxiliary Data |
| **Lag Set** | Set ID | A complete, ordered time-series for one baseline. | Set ID, Baseline ID, Start Time, End Time, Lag Values[] |
| **Processed Spectrum** | Spectrum ID | The frequency-domain output of the FFT. | Spectrum ID, Baseline ID, Frequency Channels[], Spectral Data[], Metadata |
| **Output Dataset** | Dataset ID | The final, formatted product sent to e2e. | Dataset ID, Integrated Time Span, Spectra[], All Metadata, Processing History |
| **Processing Parameters** | Process ID | User-defined processing configuration. | Process ID, Step Sequence[], Step Parameters[] |
| **System Status Report** | Report ID, Timestamp | Health and status update for M&C. | Timestamp, Report ID, Component ID, Status Code, Metrics, Error/Warning Messages |

---
*End of Document*