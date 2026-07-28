# Software Requirements Specification (SRS)
## Swift X-Ray Telescope (XRT) Control Processor (XCP) Flight Software (FSW)
**Document ID:** XRT-SRS-L4-001
**Revision:** 1.0
**Date:** [Date]
**Status:** Draft

---

### 1. Introduction

#### 1.1 Purpose
This document defines the Level 4 Software Requirements Specification (SRS) for the Swift X-Ray Telescope (XRT) Control Processor (XCP) Flight Software (FSW). It serves as the definitive source of functional, performance, and interface requirements for the software that controls the XRT instrument aboard the Swift Gamma Ray Burst Explorer mission. The intended audience includes software developers, systems engineers, integration and test personnel, and project stakeholders.

#### 1.2 Scope
The XCP FSW is responsible for the real-time control and data processing of the XRT instrument. Its scope encompasses:
*   Processing science data (images, light curves, spectra) from the XRT CCD camera.
*   Receiving, validating, and executing commands from the spacecraft's Spacecraft Control Unit (SCU).
*   Generating and transmitting housekeeping (HK) and science telemetry to the SCU via a MIL-STD-1553B data bus interface.
*   Controlling instrument subsystems including heaters, the thermo-electric cooler (TEC), and the telescope alignment monitor (TAM).
*   Performing onboard error detection, correction (EDAC), and continuous system health monitoring.

This specification explicitly excludes:
*   Spacecraft-level functions (e.g., attitude control, slewing, power bus management).
*   Ground-based data processing, analysis, or archiving software.
*   The physical hardware design or manufacturing of XRT components.
*   High-level mission planning or observatory coordination.
*   Support for external data formats or communication protocols beyond those specified herein (e.g., non-CCSDS).

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **CCD** | Charge-Coupled Device (the XRT camera sensor) |
| **CCSDS** | Consultative Committee for Space Data Systems |
| **FSW** | Flight Software |
| **GRB** | Gamma-Ray Burst |
| **HK** | Housekeeping |
| **SCU** | Spacecraft Control Unit |
| **SMOC** | Science Mission Operations Center |
| **TAM** | Telescope Alignment Monitor |
| **TBD** | To Be Determined |
| **TDRSS** | Tracking and Data Relay Satellite System |
| **TEC** | Thermo-Electric Cooler |
| **XCP** | XRT Control Processor |
| **XRT** | X-Ray Telescope |

#### 1.4 References
*   Swift Mission Level 1 Requirements Document
*   XRT Instrument Interface Control Document (ICD)
*   SCU/XRT 1553B Bus ICD
*   CCSDS Packet Telemetry Standard (Blue Book)
*   SSFF, IMAGE, CUBIC FSW Heritage Documentation

#### 1.5 Overview
The remainder of this document is structured as follows:
*   **Section 2:** Overall Description – Provides context, user characteristics, constraints, and assumptions.
*   **Section 3:** Specific Requirements – Details functional, interface, performance, and design requirements.
*   **Appendix A:** Data Dictionary (Outline)
*   **Appendix B:** Undecided Issues & TBD Log

---

### 2. Overall Description

#### 2.1 Product Perspective
The XCP FSW is a mission-critical component of the Swift Observatory. It resides on the XRT instrument's dedicated processor and interfaces directly with the XRT hardware (CCD, TEC, Heaters, TAM) and the spacecraft's SCU. The software acts as the intermediary, translating high-level science observation commands into low-level hardware controls and converting raw detector data into formatted science and engineering telemetry for downlink.

#### 2.2 User Characteristics
The primary "users" of the XCP FSW are indirect:
*   **Flight Operators at SMOC:** Issue commands and monitor telemetry. They are familiar with ITOS ground system and spacecraft operations procedures.
*   **Scientists (PSU):** Define observation parameters and analyze downlinked data. They provide algorithms for centroiding and data processing.
*   **The Spacecraft (SCU):** An automated system that sends periodic commands and polls for telemetry.

#### 2.3 Major Constraints
1.  **Telemetry Bandwidth:** The TDRSS downlink allocation constrains the average science telemetry rate to **< 3.9 kbps**.
2.  **Packet Size:** Real-time HK packets must not exceed **230 bytes** per SCU 1553 frame to ensure reliable transfer.
3.  **Ground System Limitations:** The ITOS ground system cannot reassemble segmented CCSDS packets or decompress data; telemetry must be formatted accordingly.
4.  **Contact Schedule:** Limited ground contacts via the Malindi station (~7 per day) prohibit time-intensive, interactive operations.
5.  **Software Reuse:** The design must incorporate and adapt reusable components from the SSFF, IMAGE, and CUBIC flight software projects to reduce cost and risk.

#### 2.4 Assumptions and Dependencies
*   The SCU 1553B interface and driver hardware will perform reliably.
*   The XRT hardware (CCD, TEC) will perform within its specified parameters.
*   Ground command sequences will be validated prior to uplink.
*   Success metrics (e.g., centroiding accuracy) are dependent on both software algorithms and hardware optical performance.

---

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Command Processing (XCP-FUN-010)
**Description:** The software shall receive, decode, validate, and execute commands from the SCU via the MIL-STD-1553B interface.
**Requirements:**
*   XCP-FUN-011: The software shall accept both time-tagged and immediate execution commands.
*   XCP-FUN-012: The software shall validate command syntax and parameter ranges before execution.
*   XCP-FUN-013: The software shall provide positive (Accept) or negative (Reject) acknowledgment for each command received.

##### 3.1.2 Science Data Processing (XCP-FUN-020)
**Description:** The software shall acquire data from the CCD in multiple modes, process it, and format it for telemetry.
**Requirements:**
*   XCP-FUN-021: The software shall support three primary observation modes: **Imaging**, **Photo-Diode (PD)**, and **Photon-Counting (PC)**. Mode-specific parameters (e.g., integration times, window sizes) are TBD (see Table 2).
*   XCP-FUN-022: The software shall calculate and apply a bias correction to raw CCD frames.
*   XCP-FUN-023: In Imaging mode, the software shall perform onboard centroiding of point sources with an accuracy of **2.5 arcseconds** within **5 seconds** of data acquisition.
*   XCP-FUN-024: The software shall automatically transition between PD, PC, and Imaging modes based on configurable count rate thresholds to prevent CCD saturation and optimize science return.

##### 3.1.3 Telemetry Generation (XCP-FUN-030)
**Description:** The software shall generate and output housekeeping and science telemetry packets.
**Requirements:**
*   XCP-FUN-031: The software shall generate periodic, real-time HK packets containing temperatures, voltages, currents, and status flags. Each packet shall be ≤ **230 bytes**.
*   XCP-FUN-032: The software shall format science data into CCSDS-compliant source packets for downlink.
*   XCP-FUN-033: The average science data telemetry rate shall not exceed the allocated **3.9 kbps**.

##### 3.1.4 Subsystem Control (XCP-FUN-040)
**Description:** The software shall control and monitor the state of instrument subsystems.
**Requirements:**
*   XCP-FUN-041: The software shall regulate the TEC to maintain the CCD at its operational temperature setpoint.
*   XCP-FUN-042: The software shall control heater circuits based on temperature thresholds to maintain instrument thermal stability.
*   XCP-FUN-043: The software shall monitor TAM data to detect potential telescope misalignment.

##### 3.1.5 Fault Management (XCP-FUN-050)
**Description:** The software shall detect, respond to, and log anomalous conditions.
**Requirements:**
*   XCP-FUN-051: The software shall perform continuous memory EDAC (Error Detection and Correction).
*   XCP-FUN-052: The software shall monitor critical HK parameters (e.g., over-temperature, over-voltage) and transition to a predefined safe-hold state if limits are violated.
*   XCP-FUN-053: The software shall maintain a circular log of anomaly events for later downlink.

##### 3.1.6 Software Maintenance (XCP-FUN-060)
**Description:** The software shall support in-flight updates.
**Requirements:**
*   XCP-FUN-061: The software shall support the upload of patch files via the EEPROM file system, allowing for correction of on-orbit issues without a full software reload.

#### 3.2 Interface Requirements

##### 3.2.1 1553B Bus Interface (XCP-INT-010)
**Description:** Interface with the SCU.
**Requirements:**
*   XCP-INT-011: The software shall implement the MIL-STD-1553B protocol as specified in the SCU/XRT ICD.
*   XCP-INT-012: The software shall respond to bus controller messages within the required timeframe.

##### 3.2.2 Hardware Device Interfaces (XCP-INT-020)
**Description:** Interfaces to XRT-specific hardware.
**Requirements:**
*   XCP-INT-021: The software shall communicate with the CCD controller to initiate exposures and read out data.
*   XCP-INT-022: The software shall send control signals to the TEC and heater power drivers.
*   XCP-INT-023: The software shall read analog and digital data from the TAM sensor.

#### 3.3 Performance Requirements
*   XCP-PER-010: **CPU Margin:** The software shall demonstrate >95% CPU margin in worst-case operational scenarios (e.g., simultaneous data processing, centroiding, and HK collection).
*   XCP-PER-020: **Centroiding Latency:** Source centroid coordinates shall be available for telemetry within 5 seconds of CCD readout completion.
*   XCP-PER-030: **Command Response:** The software shall generate a command acknowledgment within 100 ms of receipt.

#### 3.4 Design Constraints
*   XCP-DES-010: The software shall be written in ANSI C.
*   XCP-DES-020: The software architecture shall be modular to facilitate the integration of heritage components from SSFF/IMAGE/CUBIC.
*   XCP-DES-030: Memory allocation for observation data buffers shall be static and determined during initialization to avoid fragmentation. Optimal sizing TBD.

#### 3.5 Software Quality Attributes
*   **Reliability:** The software shall have a mean time between failures (MTBF) consistent with mission lifetime requirements.
*   **Maintainability:** Code shall be well-commented and adhere to a defined coding standard to support patching.
*   **Testability:** Requirements shall be verifiable through test, analysis, inspection, or demonstration.

---

### Appendix A: Data Dictionary (Outline)
*(To be populated)*
*   Command Opcodes and Parameters
*   Housekeeping Packet Structure
*   Science Data Packet Structure (for Imaging, PD, PC modes)
*   TAM Data Parameters (TBD)
*   Error/Event Log Codes

### Appendix B: Undecided Issues & TBD Log

| ID | Issue Description | Responsible Party | Date Raised | Status |
| :-- | :--- | :--- | :--- | :--- |
| TBD-001 | Final numerical values for science data acquisition modes (Table 2: integration times, window sizes, etc.) | PSU / SwRI | [Date] | Open |
| TBD-002 | Specific algorithms for bias calculation and centroiding | PSU | [Date] | Open |
| TBD-003 | Verification methods for requirements XCP-FUN-022 through XCP-FUN-027 | SwRI/Test Team | [Date] | Open |
| TBD-004 | Definition of TAM parameters and data format | GSFC/PSU | [Date] | Open |
| TBD-005 | Optimal memory allocation sizes for observation data buffers | SwRI | [Date] | Under Analysis |

---

**Document Approval:**

| Name | Role | Signature | Date |
| :--- | :--- | :--- | :--- |
| | Project Manager, SwRI | | |
| | Lead Systems Engineer, GSFC | | |
| | Science Lead, PSU | | |