Here is a comprehensive Software Requirements Specification (SRS) document based on the provided information, structured according to professional standards and formatted in Markdown.

# Software Requirements Specification
## Real-Time Astronomical Data Processing System
### For the EVLA Correlator to End-to-End (e2e) Data Pipeline

**Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft

---

## 1. Introduction

### 1.1 Purpose
This document describes the functional and non-functional requirements for the Real-Time Astronomical Data Processing System. This system is a critical component of the Expanded Very Large Array (EVLA) data pipeline, responsible for processing high-volume data streams between the Correlator and the End-to-End (e2e) systems. The intended audience includes project managers, developers, testers, and system architects.

### 1.2 Scope
The system shall process real-time astronomical data streams, performing the following core functions:
- Assembling incoming lag frames into complete time-series data.
- Performing Fourier Transforms on the assembled time-series.
- Applying user-selectable processing in time and frequency domains.
- Formatting the output into AIPS++ Measurement Sets for consumption by the e2e system.
- Monitoring internal system health and ensuring recovery from failures without data loss.

**Out of Scope:**
- Spectrum stitching across sub-bands.
- Provision of direct user interfaces for operators or scientists.

### 1.3 Definitions, Acronyms, and Abbreviations

| Term | Definition |
| :--- | :--- |
| **EVLA** | Expanded Very Large Array |
| **e2e** | End-to-End System |
| **M&C** | Monitor and Control System |
| **AIPS++** | Astronomical Information Processing System (a data format standard) |
| **UDP/IP** | User Datagram Protocol / Internet Protocol |
| **Lag Frame** | A packet of raw correlation data from the Correlator. |
| **Time-Series** | A complete set of assembled lag frames. |
| **RFI** | Radio Frequency Interference |

### 1.4 References
*   EVLA System Architecture Document
*   AIPS++ Measurement Set Format Specification
*   Correlator Data Interface Control Document

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details the specific functional and non-functional requirements. Appendices may include supplementary information.

## 2. Overall Description

### 2.1 Product Perspective
This system is a middleware component within the larger EVLA data pipeline ecosystem. It acts as a bridge, replacing legacy VLA processing infrastructure. Its position and interfaces are critical, as system failure would result in irreversible scientific data loss.

**System Interfaces:**
*   **Correlator:** Provides the primary input data stream.
*   **M&C System:** Provides control, auxiliary data, and receives status/error reports.
*   **e2e System:** Consumes the final processed output.

### 2.2 Product Functions
The core functions of the system are:
1.  **Data Ingestion & Assembly:** Receive and order lag frames into complete time-series (lag sets).
2.  **Spectral Processing:** Perform Fourier Transforms on time-series data.
3.  **Optional Processing:** Apply configurable processing algorithms (e.g., RFI mitigation).
4.  **Data Formatting:** Convert processed spectra into AIPS++ Measurement Set format.
5.  **Health Monitoring:** Continuously monitor the health of processors, networks, and compute resources.
6.  **Failure Recovery:** Recover from component failures without loss of raw data.

### 2.3 User Characteristics

| User Role | Characteristics & Access Level |
| :--- | :--- |
| **Array Operators** | Receive status and error information exclusively via the M&C system; have no direct access to this system. |
| **Scientists** | Indirect users who specify optional processing parameters (e.g., RFI mitigation flags) which are configured via the M&C system. |
| **Engineers** | Require remote access to diagnose hardware and software faults and perform system maintenance. |
| **Developers** | Require full system access for remote debugging and software development purposes. |
| **Web Users** | Have limited, restricted access for monitoring purposes only (e.g., read-only status dashboards). |

### 2.4 Constraints
*   **Hardware:** System throughput is constrained by the physical limits of the designated hardware.
*   **Network:** The supporting network infrastructure must sustain the real-time data rates for both input and output streams.
*   **Data Format:** The system assumes that lag sets contain a power-of-two number of values (≤262,144).

### 2.5 Assumptions and Dependencies
*   **Assumptions:**
    *   Lag sets will always contain a number of values that is a power of two.
    *   All necessary auxiliary data (e.g., timestamps, configuration) will be delivered via the M&C system interface.
*   **Dependencies:**
    *   The e2e system must be capable of accepting and processing the output data at a sustained rate of ≥25 MB/sec.
    *   The Correlator must reliably deliver lag frames via the specified UDP/IP interface.

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 Correlator Interface
*   **REQ-IF-1:** The system shall accept input data from the Correlator via UDP/IP packets.
*   **REQ-IF-2:** The system shall be designed to handle lag frames that arrive with no guaranteed ordering.

#### 3.1.2 M&C System Interface
*   **REQ-IF-3:** The system shall receive control commands and auxiliary data from the M&C System.
*   **REQ-IF-4:** The system shall send status reports and error alerts to the M&C System.

#### 3.1.3 e2e System Interface
*   **REQ-IF-5:** The system shall output fully formatted AIPS++ Measurement Sets to the e2e system.
*   **REQ-IF-6:** The output data shall be delivered in a manner that requires no further reassembly by the e2e system.

### 3.2 Functional Requirements

#### 3.2.1 Data Processing Requirements
*   **REQ-FN-1:** The system shall assemble incoming lag frames into complete time-series data sets.
    *   **REQ-FN-1.1:** A single time-series (lag set) shall support up to 262,144 values.
*   **REQ-FN-2:** The system shall perform a Fourier Transform on each assembled time-series to convert it to the frequency domain.
*   **REQ-FN-3:** The system shall apply user-selectable processing functions in the time or frequency domain based on parameters received from the M&C system.
*   **REQ-FN-4:** The system shall format the processed spectral data into the standard AIPS++ Measurement Set format.

#### 3.2.2 System Management & Recovery Requirements
*   **REQ-FN-5:** The system shall continuously monitor the health of its internal components, including processors, network interfaces, and compute nodes.
*   **REQ-FN-6:** The system shall recover automatically from a temporary loss of connection with the Correlator without any loss of raw data.
*   **REQ-FN-7:** The system shall recover automatically from a temporary loss of connection with the e2e system without any loss of raw or processed data.
*   **REQ-FN-8:** All data processing steps applied by the system must be reversible, ensuring that the original raw data can be fully recovered.

### 3.3 Non-Functional Requirements

#### 3.3.1 Performance Requirements
*   **REQ-PF-1:** The system shall sustain a minimum input data rate of **1.6 GigaBytes per second** from the Correlator.
*   **REQ-PF-2:** The system shall sustain a minimum output data rate of **25 MegaBytes per second** to the e2e system.

#### 3.3.2 Reliability & Availability
*   **REQ-RL-1:** The system shall achieve an operational availability of **99.9%** during scheduled observation periods.
*   **REQ-RL-2:** The system shall be designed for zero data loss in the event of transient failures in upstream (Correlator) or downstream (e2e) systems.

#### 3.3.3 Security Requirements
*   **REQ-SC-1:** The system shall implement role-based access control (RBAC) with at least the following roles: Administrator, Engineer, Developer, and Web User.
*   **REQ-SC-2:** All user logins, including those for maintenance and debugging, shall be performed over encrypted channels.
*   **REQ-SC-3:** Administrator roles shall have full control over the system, while all other roles shall have restricted access as defined in Section 2.3.

#### 3.3.4 Reversibility Requirement
*   **REQ-RV-1:** As stated in REQ-FN-8, the system must guarantee that all processing is reversible, and raw lag frame data is always recoverable. This is a critical non-functional constraint.

## 4. Acceptance Criteria

Formal acceptance of the system is contingent upon successful verification of the following:

1.  **Throughput Verification:** Demonstrated ability to continuously process an input stream ≥1.6 GB/sec and produce an output stream ≥25 MB/sec under maximum load for a sustained period (e.g., 24 hours).
2.  **Fault Tolerance Verification:** Demonstration of zero data loss during simulated outages of the Correlator and e2e system interfaces.
3.  **Reversibility Verification:** Demonstration that for a given set of processed output data, the original raw input lag frames can be perfectly reconstructed.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Manager | | | |
| Lead Architect | | | |
| Quality Assurance | | | |