# Software Requirements Specification (SRS)
## Swift Gamma Ray Burst Explorer: X-Ray Telescope (XRT) Control Processor Flight Software

**Document ID:** SRS-XRT-FSW-001
**Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the requirements for the Flight Software (FSW) of the X-Ray Telescope (XRT) Control Processor on board the Swift Gamma Ray Burst Explorer spacecraft. It is intended for use by software developers, systems engineers, integration and test personnel, and project management.

#### 1.2 Scope
The XRT FSW is responsible for the autonomous operation of the XRT instrument. This includes:
*   Scientific data acquisition and processing from the CCD.
*   Execution of instrument commands.
*   Generation and transmission of telemetry.
*   Thermal control of the telescope and CCD.
*   Management of all interfaces internal to the XRT Electronics Package (XEP).
*   Communication with the spacecraft's Spacecraft Control Unit (SCU).

**Out of Scope:**
*   Control of spacecraft attitude or slewing.
*   Overall mission planning.
*   Science data analysis on the ground.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **CCD** | Charge-Coupled Device (the XRT camera sensor) |
| **CCSDS** | Consultative Committee for Space Data Systems |
| **EDAC** | Error Detection and Correction |
| **EEPROM** | Electrically Erasable Programmable Read-Only Memory |
| **FSW** | Flight Software |
| **GRB** | Gamma-Ray Burst |
| **HK** | Housekeeping |
| **ITOS** | Integrated Test and Operations System (Ground System) |
| **MIL-STD-1553B** | Military Standard serial data bus |
| **RAD6000** | Radiation-Hardened Single-Board Computer |
| **SCU** | Spacecraft Control Unit |
| **TAM** | Telescope Alignment Monitor |
| **TDRSS** | Tracking and Data Relay Satellite System |
| **TEC** | Thermo-Electric Cooler |
| **TOO** | Target of Opportunity |
| **VME** | Versa Module Europa (computer bus standard) |
| **XEP** | XRT Electronics Package |
| **XRT** | X-Ray Telescope |

#### 1.4 References
*   Swift Observatory System Requirements Document
*   XRT Instrument Interface Control Document (ICD)
*   CCSDS Packet Telemetry Standard (Blue Book)
*   MIL-STD-1553B Notices and Command/Telemetry Database

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details specific requirements, including functional, interface, and non-functional requirements.

### 2. Overall Description

#### 2.1 Product Perspective
The XRT FSW is a component of the Swift observatory, a multi-wavelength mission dedicated to the study of gamma-ray bursts. The software is hosted on a dedicated RAD6000 processor within the XEP. It acts as the intermediary between the spacecraft's SCU and all XRT subsystem hardware (Camera, Heaters, Cooler, TAM, Power Modules).

#### 2.2 Product Functions
The core functions of the XRT FSW are:
1.  **Science Data Processing:** Acquire, process, and packetize CCD data (images, light curves, spectra).
2.  **Command Execution:** Receive, validate, and dispatch commands from the SCU and ground.
3.  **Telemetry Generation:** Produce and transmit HK and science data packets to the SCU.
4.  **Thermal Control:** Regulate 36 tube heaters, 3 baffle heaters, and the CCD TEC.
5.  **Alignment Monitoring:** Operate the TAM to detect telescope mechanical drift.
6.  **Time Management:** Synchronize the local clock with spacecraft time via 1PPS signals and time messages.
7.  **Autonomous Observation:** Execute observation sequences (AUTO, Preplanned, TOO), including source detection, centroiding, and dynamic mode switching based on source flux.

#### 2.3 User Characteristics
*   **Primary User (Spacecraft Control Unit - SCU):** An automated system that sends high-level observation commands and receives telemetry. Interaction is via predefined 1553 messages.
*   **Secondary User (Ground Operators):** Human operators who send direct instrument commands for configuration, diagnostics, and recovery. Interaction is primarily during non-nominal (MANUAL/RED) modes.

#### 2.4 Constraints
*   **Hardware Platform:** Must execute on the RAD6000 processor within the XEP VME chassis.
*   **Telemetry Size:** Real-time HK packets shall not exceed 230 bytes.
*   **Ground System Limitation:** The initial ground system (ITOS) cannot reassemble segmented CCSDS packets or decompress data.
*   **Downlink Bandwidth:** Total XRT telemetry volume is constrained by the allocated TDRSS downlink bandwidth.
*   **Operational Autonomy:** Must perform nominal observations with minimal ground intervention due to limited daily contacts.

#### 2.5 Assumptions and Dependencies
*   The RAD6000 processor, MIL-STD-1553B interface, and CCD sequencer (AD21020) hardware will function as specified.
*   The SCU will provide valid time synchronization messages and 1PPS signals.
*   The ground command system will format commands according to the XRT ICD.

### 3. Specific Requirements

#### 3.1 External Interface Requirements
##### 3.1.1 Spacecraft Interface (MIL-STD-1553B)
*   **REQ-IF-001:** The FSW shall communicate with the SCU via a dual-redundant MIL-STD-1553B bus as a Remote Terminal (RT).
*   **REQ-IF-002:** The FSW shall receive and acknowledge all valid commands addressed to the XRT subsystem within 20 ms of the 1553 message transmission.
*   **REQ-IF-003:** The FSW shall transmit HK and science data packets in the format and according to the schedule defined in the XRT-SCU ICD.

##### 3.1.2 Time Synchronization Interface (RS-422)
*   **REQ-IF-004:** The FSW shall accept a 1 Pulse Per Second (1PPS) signal via an RS-422 hardline and synchronize its internal software clock to this signal with an accuracy of ±1 ms.
*   **REQ-IF-005:** The FSW shall process spacecraft absolute time messages received over the 1553 bus to maintain long-term clock correlation.

##### 3.1.3 Camera Head Interface
*   **REQ-IF-006:** The FSW shall interface with the CCD Camera Head via a dedicated digital bus to initiate exposures and read out image data.

##### 3.1.4 Telescope Alignment Monitor Interface (RS-422)
*   **REQ-IF-007:** The FSW shall communicate with the TAM via an RS-422 serial interface to command image captures and receive image data.

##### 3.1.5 Local VME Bus Interfaces
*   **REQ-IF-008:** The FSW shall communicate with the following XEP modules via the VME bus:
    *   Power Distribution Module (PDM)
    *   Sequencer Module (handles CCD timing)
    *   Analog I/O Module (for temperature/voltage readings)
    *   Communication Module (1553 interface)

#### 3.2 Functional Requirements
##### 3.2.1 Command Processing
*   **REQ-FN-101:** The FSW shall validate all incoming commands for correct format, address, and checksum.
*   **REQ-FN-102:** The FSW shall support command execution from the following system states: AUTO, MANUAL, RED.
*   **REQ-FN-103:** The FSW shall dispatch valid commands to the appropriate internal software module (e.g., thermal, camera, TAM).

##### 3.2.2 Telemetry Generation
*   **REQ-FN-201:** The FSW shall generate comprehensive HK telemetry packets at a configurable rate (1 Hz nominal), containing voltages, temperatures, subsystem statuses, and software state.
*   **REQ-FN-202:** The FSW shall format all telemetry (HK and Science) into standard CCSDS packets with appropriate Application Process IDs (APIDs).
*   **REQ-FN-203:** The FSW shall manage telemetry buffers to prevent overrun during peak science data rates (~100 kbps).

##### 3.2.3 Science Data Processing
*   **REQ-FN-301:** The FSW shall control the CCD to operate in the following modes: Image, Photo-Diode, Windowed Timing, and Photon Counting.
*   **REQ-FN-302:** In AUTO mode, the FSW shall autonomously detect a source in the CCD field of view and calculate its centroid position.
*   **REQ-FN-303:** The FSW shall autonomously switch CCD modes based on the measured source flux to optimize science return and telemetry volume, as defined in the observation logic.
*   **REQ-FN-304:** The FSW shall generate and transmit a "Position" message to the SCU upon successful source centroiding.

##### 3.2.4 Thermal Control
*   **REQ-FN-401:** The FSW shall control 36 telescope tube heaters using a proportional control algorithm to maintain the tube within its specified temperature range.
*   **REQ-FN-402:** The FSW shall control 3 baffle heaters independently.
*   **REQ-FN-403:** The FSW shall regulate the CCD temperature via the TEC to -100°C ± 0.5°C.

##### 3.2.5 Time Management
*   **REQ-FN-501:** The FSW shall maintain a software clock synchronized to spacecraft Universal Time (UT).
*   **REQ-FN-502:** All science and HK data packets shall be timestamped with the synchronized software clock.

##### 3.2.6 Fault Management & Autonomy
*   **REQ-FN-601:** The FSW shall implement a memory scrubber task to periodically read and correct DRAM using EDAC.
*   **REQ-FN-602:** The FSW shall store a primary and an alternate (recovery) software image in EEPROM.
*   **REQ-FN-603:** Upon receipt of a spacecraft "Safehold" notification, the FSW shall place the instrument in a safe, low-power state to allow for spacecraft power-down.
*   **REQ-FN-604:** The FSW shall prevent any command from opening the camera door unless a specific, validated enable sequence is received.

#### 3.3 Performance Requirements
*   **REQ-PF-001:** The FSW shall sustain an **average** science data rate of approximately 1 kbps.
*   **REQ-PF-002:** The FSW shall handle **peak** science data rates of up to 100 kbps for durations specified in the observation profiles.
*   **REQ-PF-003:** The software design shall maintain a minimum CPU throughput margin of 20% under worst-case operational load.
*   **REQ-PF-004:** Command acknowledgment latency shall be less than 50 ms (95th percentile).

#### 3.4 Design Constraints
*   **REQ-DC-001:** The software shall be written in ANSI C.
*   **REQ-DC-002:** The software shall run on the VxWorks 5.x real-time operating system.
*   **REQ-DC-003:** The software shall be structured as a set of concurrent tasks with priority-based scheduling.

#### 3.5 Software System Attributes
##### 3.5.1 Reliability
*   **REQ-AT-001:** The software shall have a mean time between critical failures (MTBCF) greater than 10,000 operational hours.
*   **REQ-AT-002:** Single-event upsets (SEUs) in memory shall be detected and corrected by the EDAC/scrubber system without operational impact.

##### 3.5.2 Safety
*   **REQ-AT-003:** The software shall include independent checks (e.g., command counters, hardware interlocks) to prevent inadvertent camera door actuation.
*   **REQ-AT-004:** Heater control loops shall include hardware and software limits to prevent overheating.

##### 3.5.3 Maintainability
*   **REQ-AT-005:** The software shall support in-flight patching of non-volatile parameters and upload of new software images via ground command.

### 4. Verification and Acceptance

#### 4.1 Priority
| Priority Level | Requirements |
| :--- | :--- |
| **Top** | REQ-FN-301, REQ-FN-302, REQ-FN-303 (Core AUTO mode science) |
| **High** | REQ-IF-001, REQ-IF-002, REQ-IF-003, REQ-FN-401, REQ-FN-403, REQ-FN-501 (Interfaces, Thermal, Time) |
| **Medium** | REQ-FN-102 (MANUAL/RED modes), REQ-AT-005 (Memory upload) |

#### 4.2 Acceptance Approach
Each requirement shall be verified by one of the following methods:
*   **Test:** Direct execution of test procedures on flight-equivalent hardware/software (e.g., demonstration of mode switching, measurement of data rates).
*   **Analysis:** Mathematical or logical evaluation (e.g., CPU margin analysis, reliability prediction).
*   **Inspection:** Review of design documents, code, or telemetry formats.
*   **Demonstration:** Observation of operational functionality (e.g., autonomous observation sequence flow).

Key performance metrics (data rates, CPU margin) and critical functional sequences (e.g., a complete AUTO observation from slew complete to mode switching) will be demonstrated during system integration and test.

---
**END OF DOCUMENT**