# Software Requirements Specification (SRS)
## Real-Time Astronomical Data Processing Pipeline (RTADPP)

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review  
**Authors:** Systems Engineering Team

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Real-Time Astronomical Data Processing Pipeline (RTADPP). The RTADPP is a critical software system that processes raw correlator output into formatted spectral data for archival and scientific analysis. This document is intended for use by stakeholders, project managers, software developers, testers, and system architects involved in the design, implementation, and validation of the system.

#### 1.2 Scope
The RTADPP operates as the intermediary processing layer between the **Correlator** and the **End-to-End (E2E) Archive System**. Its primary responsibility is to ingest real-time lag data from the correlator, assemble it into time-series, perform Fourier Transforms to generate spectral data, and deliver the processed results in a defined format to the E2E system. The system does **not** include:
*   The correlator hardware or its internal processing software.
*   The E2E archive's long-term storage, user interface, or data distribution mechanisms.
*   Higher-level scientific calibration or imaging processes.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **Correlator** | The upstream system that computes cross-correlation lags from antenna signals. |
| **Lag Data** | The raw, time-integrated output of the correlator, representing the cross-correlation function. |
| **E2E System** | The downstream End-to-End archive responsible for permanent storage and distribution of processed data. |
| **Fourier Transform (FT)** | The mathematical operation converting time-series lag data into the frequency domain (spectrum). |
| **RTADPP** | Real-Time Astronomical Data Processing Pipeline (the system described herein). |
| **SLA** | Service Level Agreement. |
| **Uptime** | The percentage of time the system is operational and processing data. |

#### 1.4 References
*   Observatory System Architecture Document, Version 3.1
*   Correlator Data Interface Control Document (ICD), Revision B
*   End-to-End Archive Data Ingestion Specification, Version 2.4

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a high-level description of the product and its operating environment. Section 3 details specific system requirements, including functional, interface, and non-functional requirements.

### 2. Overall Description

#### 2.1 Product Perspective
The RTADPP is a standalone, mission-critical component within the larger observatory data flow. It is a successor to previous batch-processing systems and is designed for continuous, real-time operation.

**System Interfaces:**
*   **Upstream:** Correlator Data Stream (Network Interface)
*   **Downstream:** E2E System Ingestion Service (Network Interface)
*   **Monitoring/Control:** Observatory Monitoring and Control System (OMCS) via API/Message Bus.

#### 2.2 User Characteristics
| User Class | Primary Responsibilities | Technical Expertise | Interaction Mode |
| :--- | :--- | :--- | :--- |
| **Array Operator** | Monitor pipeline health, initiate/stop processing for observations. | High (system operations) | Graphical User Interface (GUI), alarm dashboards. |
| **Engineers & Technicians** | Diagnose faults, perform maintenance, update configuration. | Very High (system-level) | Command Line Interface (CLI), admin GUI, log files. |
| **Astronomer/Scientist** | Verify data quality for their observation, may request reprocessing. | Medium (domain expert) | Limited GUI for status checks, access to processed metadata and quality metrics. |
| **Software Developer** | Develop, maintain, and extend pipeline software modules. | Very High (programming) | Source code, configuration files, development APIs. |

#### 2.3 Key Constraints
1.  **Criticality:** The system is **mission-critical**. Any unscheduled downtime results in the permanent loss of incoming astronomical data. This mandates high-availability design and rapid fault recovery.
2.  **Performance:** System throughput is a primary constraint, bounded by:
    *   Computational hardware (CPU/GPU) capacity for Fourier Transforms.
    *   Network bandwidth between the Correlator, RTADPP, and E2E Archive.
3.  **Data Integrity & Reversibility:** All data processing operations (e.g., assembly, Fourier Transform) must be **mathematically reversible** or retain sufficient metadata to allow reconstruction of the original correlator output from the final processed data product. This is essential for data validation and reprocessing.

#### 2.4 Assumptions and Dependencies
*   The Correlator will provide data according to the specified ICD.
*   The E2E Archive system will be available to accept processed data within agreed-upon SLA windows.
*   Sufficient computational and network infrastructure will be provisioned to meet throughput requirements.
*   The system will operate in a controlled, observatory-grade data center environment.

### 3. Specific Requirements

#### 3.1 Functional Requirements

**FR-1: Data Ingestion**
*   **FR-1.1:** The system shall continuously receive real-time data packets from the Correlator via the network interface defined in the Correlator ICD.
*   **FR-1.2:** The system shall validate the integrity (e.g., via checksums) and completeness of each incoming data packet.
*   **FR-1.3:** The system shall acknowledge receipt of valid packets to the Correlator as per the ICD protocol.
*   **FR-1.4:** The system shall log and alert operators of any ingestion errors or sustained data stream interruptions.

**FR-2: Time-Series Assembly**
*   **FR-2.1:** The system shall assemble individual correlator lag packets into continuous, time-ordered data blocks (time-series) for each baseline and polarization.
*   **FR-2.2:** The system shall apply necessary geometric and instrumental delays (as per configuration) during assembly.
*   **FR-2.3:** The system shall tag each assembled time-series block with precise start time, duration, and metadata identifying the source observation and antennas.

**FR-3: Fourier Transform Processing**
*   **FR-3.1:** The system shall perform a Fourier Transform on each assembled time-series block to convert lag data to the spectral domain.
*   **FR-3.2:** The Fourier Transform algorithm and any windowing functions applied shall be configurable and documented.
*   **FR-3.3:** The system shall retain all parameters and coefficients used in the FT process as part of the output product's metadata to satisfy the reversibility constraint.

**FR-4: Data Formatting and Delivery**
*   **FR-4.1:** The system shall format the spectral data and its comprehensive metadata into the structure specified by the E2E Archive Ingestion Specification.
*   **FR-4.2:** The system shall transmit the formatted data product to the designated E2E Archive ingestion endpoint.
*   **FR-4.3:** The system shall confirm successful delivery and log any transmission failures for retry or manual intervention.

**FR-5: Monitoring and Control**
*   **FR-5.1:** The system shall provide a real-time dashboard displaying pipeline health, throughput (MB/s), processing latency, and data backlog.
*   **FR-5.2:** The system shall expose an API for the OMCS to start, stop, pause, and query the status of the pipeline.
*   **FR-5.3:** The system shall generate configurable alerts for critical failures, performance degradation, and SLA breaches.

**FR-6: Data Reprocessing**
*   **FR-6.1:** The system shall allow authorized users to initiate reprocessing of archived raw correlator data.
*   **FR-6.2:** The reprocessing function shall use the same reversible processing chain as the real-time pipeline.

#### 3.2 Interface Requirements

**IR-1: Correlator Interface**
*   **IR-1.1:** Protocol: [Specify, e.g., Custom UDP/TCP, VLBInet, etc.]
*   **IR-1.2:** Data Format: As per Correlator ICD Rev. B, Section 4.
*   **IR-1.3:** Bandwidth: Must sustain [X] Gbps continuous data rate.

**IR-2: E2E Archive Interface**
*   **IR-2.1:** Protocol: [Specify, e.g., HTTPS REST API, gRPC, etc.]
*   **IR-2.2:** Data Format: As per E2E Ingestion Spec v2.4.
*   **IR-2.3:** Authentication: [Specify, e.g., OAuth2.0, API Key].

**IR-3: Operations Interface**
*   **IR-3.1:** A web-based GUI shall be provided for operator control and monitoring (port 443).
*   **IR-3.2:** A CLI shall be provided for administrative and diagnostic tasks.

#### 3.3 Non-Functional Requirements

**NFR-1: Performance**
*   **NFR-1.1:** The end-to-end processing latency (correlator output to E2E delivery) shall not exceed **5 seconds** under nominal load.
*   **NFR-1.2:** The system must be capable of processing a sustained input data rate of **[X] Gbps** without building a backlog.

**NFR-2: Reliability & Availability**
*   **NFR-2.1:** The system shall have an uptime of **99.95%** in any calendar month.
*   **NFR-2.2:** The system shall implement automatic failover with a recovery time objective (RTO) of **< 60 seconds** for software failures.
*   **NFR-2.3:** No single hardware failure shall cause permanent data loss.

**NFR-3: Data Integrity**
*   **NFR-3.1:** The system shall ensure the integrity of all data processed, with a target of zero undetected corruption.
*   **NFR-3.2:** As per the key constraint, all processing steps must be **reversible**. The system must provide tools to reconstruct input from output using archived metadata.

**NFR-4: Maintainability**
*   **NFR-4.1:** The system shall be modular, with clear separation between ingestion, assembly, processing, and delivery components.
*   **NFR-4.2:** All software shall be version-controlled, and deployment shall be automated.

**NFR-5: Security**
*   **NFR-5.1:** All external interfaces (GUI, API) shall require authentication.
*   **NFR-5.2:** System access shall be role-based, corresponding to the user classes defined in Section 2.2.
*   **NFR-5.3:** All data in transit shall be encrypted.

---
*Document End*