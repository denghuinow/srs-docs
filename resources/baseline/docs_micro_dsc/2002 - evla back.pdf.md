# Software Requirements Specification (SRS)
## Real-Time Correlator Data Processing System (RTCDPS)
**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Real-Time Correlator Data Processing System (RTCDPS). The primary purpose of this system is to ingest, assemble, process, and deliver astronomical data from the Correlator to the End-to-End (E2E) archive in real-time, ensuring data integrity and reversibility. This document is intended for use by project stakeholders, system architects, software developers, and quality assurance teams.

#### 1.2 Scope
The RTCDPS will:
*   Interface directly with the Correlator subsystem to receive real-time lag data frames.
*   Perform time-series assembly and Fourier Transform operations on the incoming data.
*   Format the resulting spectral data into a defined archive-ready structure.
*   Transmit the processed data to the designated End-to-End archive interface.
*   Ensure all processing steps are logged and reversible.

**Out of Scope:**
*   Long-term storage management within the E2E archive.
*   User-facing data analysis or visualization tools.
*   Control or configuration of the upstream Correlator hardware.
*   Post-archive scientific data processing pipelines.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **Correlator** | The upstream instrument producing raw interferometric lag data. |
| **Lag Data / Lag Frame** | The raw, time-domain correlation data output by the Correlator. |
| **Spectral Data** | The frequency-domain data produced after applying a Fourier Transform to the lag data. |
| **E2E Archive** | The End-to-End archive, the downstream system for permanent data storage. |
| **RTCDPS** | Real-Time Correlator Data Processing System (the system described herein). |
| **Real-Time Processing** | Processing that completes within a fixed deadline, defined by the input data rate, to prevent pipeline overflow and data loss. |
| **Reversibility** | The property that allows the original raw input data to be perfectly reconstructed from the processed output data and associated metadata. |
| **Throughput** | The rate at which the system processes data, measured in Gigabits per second (Gbps) or similar. |

#### 1.4 References
*   Correlator Hardware Interface Control Document (ICD)
*   End-to-End Archive Data Format Specification v2.1
*   Project Charter: Next-Gen Astronomical Data Pipeline

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a high-level description of the product and its operating environment. Section 3 details specific system requirements, including external interfaces, functional capabilities, and non-functional constraints.

### 2. Overall Description

#### 2.1 Product Perspective
The RTCDPS is a middleware processing component within a larger astronomical observatory data pipeline. It acts as a critical bridge between the data acquisition system (Correlator) and the permanent repository (E2E Archive).

**System Interfaces:**
*   **Upstream:** Correlator data stream (via high-speed network).
*   **Downstream:** E2E Archive ingestion API (via observatory network).
*   **Supporting:** System monitoring/alerting dashboard, configuration database.

#### 2.2 Product Functions
The high-level functions of the RTCDPS are:
1.  **Data Ingestion:** Continuously receive streamed lag data frames.
2.  **Buffer Management:** Temporarily store incoming frames to manage processing bursts.
3.  **Time-Series Assembly:** Group sequential lag frames into contiguous time blocks.
4.  **Spectral Processing:** Apply a calibrated Fourier Transform to convert lag data to the spectral domain.
5.  **Data Formatting:** Package spectral data and critical metadata into the E2E archive specification format.
6.  **Data Delivery:** Transmit formatted data packets to the archive.
7.  **State & Logging:** Maintain processing state, log all operations, and ensure reversibility metadata is preserved.

#### 2.3 User Characteristics
The primary users of the system are:
*   **System Operators:** Observatory personnel who monitor system health, throughput, and error states. They require clear alerting and operational logs.
*   **Data Engineers:** Personnel who configure processing parameters and verify data integrity. They require access to reversibility tools and metadata.
*   **The System Itself:** Acts as an autonomous agent, requiring robust self-monitoring and error recovery.

#### 2.4 Constraints
1.  **Real-Time Deadline:** Processing latency must not exceed the time-to-fill the system's input buffers, as defined by the peak Correlator data rate. Data loss is unacceptable.
2.  **Reversibility Mandate:** All processing steps must be losslessly reversible. Sufficient metadata and transformation coefficients must be retained to reconstruct original lag frames from spectral data.
3.  **Hardware Limitations:** Computational throughput is bound by the available CPU/GPU resources of the designated processing cluster.
4.  **Network Limitations:** Input (from Correlator) and output (to Archive) bandwidth are fixed by existing infrastructure.

#### 2.5 Assumptions and Dependencies
*   The Correlator output data format and network protocol will remain stable for a defined major version.
*   The E2E Archive ingestion interface will be available and within network latency tolerances.
*   Sufficient computational hardware will be provisioned to meet the baseline data rate defined in the Correlator ICD.

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 Correlator Data Interface
*   **REQ-INT-COR-01:** The system shall accept a continuous UDP multicast stream from the Correlator as its primary data input.
*   **REQ-INT-COR-02:** The system shall implement the packet structure and sequence numbering defined in the Correlator ICD v3.0.
*   **REQ-INT-COR-03:** The system shall detect and log packet loss, generating an alert if loss exceeds 0.1% over a 60-second window.

##### 3.1.2 E2E Archive Interface
*   **REQ-INT-ARC-01:** The system shall deliver formatted data via a secure HTTPS POST API to the endpoint specified in the configuration.
*   **REQ-INT-ARC-02:** The data payload shall conform to the JSON schema specified in the E2E Archive Data Format Specification v2.1.
*   **REQ-INT-ARC-03:** The system shall implement retry logic with exponential backoff for transient archive communication failures.

#### 3.2 Functional Requirements

##### 3.2.1 Data Reception & Validation
*   **REQ-FUN-01:** The system shall receive and decode individual lag data frames from the network stream.
*   **REQ-FUN-02:** Each frame shall be validated for integrity using a checksum or CRC present in the packet header.
*   **REQ-FUN-03:** Invalid or corrupted frames shall be logged with a unique error ID and discarded. The system shall not halt processing.

##### 3.2.2 Time-Series Assembly
*   **REQ-FUN-04:** The system shall assemble validated lag frames into a time-ordered buffer to form a contiguous time series for a configurable integration period (e.g., 1 second).
*   **REQ-FUN-05:** Gaps in the time series due to discarded packets shall be flagged in the output metadata.

##### 3.2.3 Spectral Processing
*   **REQ-FUN-06:** The system shall apply a windowing function and a Fast Fourier Transform (FFT) to each integrated time-series block to produce spectral data.
*   **REQ-FUN-07:** The FFT algorithm and all processing coefficients (e.g., window function parameters) shall be versioned and recorded as metadata attached to the output.

##### 3.2.4 Data Formatting & Delivery
*   **REQ-FUN-08:** The system shall package the spectral data array, timestamps, integration parameters, and reversibility metadata into the specified E2E archive format.
*   **REQ-FUN-09:** The system shall transmit the formatted data block to the archive within 5 seconds of completing the integration period.

##### 3.2.5 Reversibility
*   **REQ-FUN-10:** The system shall retain all necessary information (including raw frame sequence, FFT coefficients, and window function) such that a standalone utility can reconstruct the original lag data from the archived spectral data and its associated metadata package.
*   **REQ-FUN-11:** This reversibility metadata shall be included as a distinct, well-documented section within the output payload delivered to the archive.

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance Requirements
*   **REQ-PER-01:** The system shall sustain real-time processing of the Correlator's maximum specified data rate of 10 Gbps without building unbounded backlog.
*   **REQ-PER-02:** The 95th percentile of processing latency (from frame receipt to archive dispatch) shall be less than the integration period + 2 seconds.
*   **REQ-PER-03:** The system shall utilize computational resources efficiently, with a target CPU utilization under 80% during peak load to accommodate processing spikes.

##### 3.3.2 Reliability & Availability
*   **REQ-REL-01:** The system shall have an operational availability of 99.9% during scheduled observation periods.
*   **REQ-REL-02:** The system shall implement a hot-standby or failover mechanism to minimize downtime in case of hardware failure.
*   **REQ-REL-03:** No single point of software failure shall cause irreversible data loss. Data in flight during a failure must be recoverable from buffers or logs.

##### 3.3.3 Operational Requirements
*   **REQ-OPS-01:** The system shall provide a monitoring dashboard displaying key metrics: input data rate, processing latency, archive upload status, error counts, and system resource usage.
*   **REQ-OPS-02:** All system actions, errors, and data integrity events shall be logged to a centralized, queryable logging service with configurable severity levels.
*   **REQ-OPS-03:** Configuration parameters (e.g., integration period, archive endpoint, processing coefficients) shall be modifiable without requiring a full system restart.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Manager | | | |
| Lead System Architect | | | |
| Quality Assurance Lead | | | |