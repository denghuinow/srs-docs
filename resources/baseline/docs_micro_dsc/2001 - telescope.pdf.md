# Software Requirements Specification (SRS)
## X-Ray Telescope (XRT) Control Processor Flight Software
### For the Swift Gamma-Ray Burst Observatory

**Document Identifier:** SRS-XRT-FSW-1001
**Revision:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

## 1. Introduction

### 1.1 Purpose
This document defines the requirements for the flight software (FSW) of the X-Ray Telescope (XRT) Control Processor on the Swift observatory. The software is responsible for the control of the XRT instrument, the collection and processing of its scientific data, management of instrument health and safety, and all interfaces with the Swift spacecraft bus. This SRS serves as the authoritative specification for developers, testers, and project stakeholders.

### 1.2 Scope
The software covered by this SRS executes on the dedicated XRT Control Processor. Its scope encompasses:
*   Real-time command processing and instrument state management.
*   Acquisition, processing, and formatting of science data from the XRT CCD camera.
*   Generation and transmission of instrument housekeeping (HK) and science telemetry.
*   Closed-loop thermal control of telescope tube and baffle heaters.
*   Management of all interfaces with the Swift spacecraft Command & Data Handling (C&DH) system (Spacecraft Control Unit).
*   Enforcement of critical flight constraints related to telemetry size and data rates.

Out of scope: Spacecraft bus FSW, ground segment software, CCD detector physics models, and the physical thermal hardware.

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **XRT** | X-Ray Telescope |
| **FSW** | Flight Software |
| **SCU** | Spacecraft Control Unit |
| **HK** | Housekeeping |
| **TM** | Telemetry |
| **TC** | Telecommand |
| **CCD** | Charge-Coupled Device |
| **S/C** | Spacecraft |
| **kbps** | kilobits per second |

### 1.4 References
*   Swift Observatory Mission Requirements Document (MRD)
*   Swift XRT Instrument Interface Control Document (ICD)
*   Swift Spacecraft to Payload ICD (SC-ICD-001)
*   CCSDS Packet Telemetry Standard (Blue Book)
*   Project Software Development Plan (SDP)

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a high-level description of the product. Section 3 details specific requirements, organized by functionality, interfaces, and constraints.

## 2. Overall Description

### 2.1 Product Perspective
The XRT FSW is a mission-critical component of the Swift observatory payload. It operates as an embedded application on the radiation-hardened XRT Control Processor. The software interfaces directly with the XRT CCD Camera electronics and heater drivers, and communicates with the Swift spacecraft's SCU via a MIL-STD-1553B data bus (or equivalent). It is a subordinate element within the overall spacecraft data and command hierarchy.

### 2.2 Product Functions
The primary functions of the XRT FSW are:
1.  **Command Execution:** Receive, validate, and execute telecommunications from the SCU to configure instrument states, camera modes, and operational parameters.
2.  **Science Data Processing:** Control the CCD camera, collect raw image/data frames, perform onboard processing (e.g., bias subtraction, event detection, grading), and format the processed science data into standard telemetry packets.
3.  **Health & Safety Management:** Continuously monitor instrument HK data (voltages, currents, temperatures). Execute autonomous responses to out-of-limit conditions, including fault detection, isolation, and recovery (FDIR) procedures and thermal control.
4.  **Thermal Control:** Implement closed-loop control algorithms for the telescope tube and thermal baffle heaters to maintain components within their allowable flight temperature ranges.
5.  **Telemetry Generation:** Generate and transmit real-time HK packets and buffered science data packets to the SCU for downlink, strictly adhering to defined size and rate constraints.

### 2.3 User Characteristics
The intended "users" of this software are:
*   **The Swift Spacecraft (SCU):** The primary operational interface, sending commands and receiving telemetry.
*   **Ground Operators:** Scientists and engineers who interact with the instrument indirectly by uplinking commands via the SCU and receiving telemetry on the ground.

### 2.4 Constraints
1.  **Real-time HK Packet Size:** Any housekeeping packet generated for immediate transmission to the SCU shall not exceed **230 bytes** in total length (including CCSDS primary and secondary headers).
2.  **Ground System Limitations:** The ground data system is incapable of reassembling segmented (multi-packet) data units or decompressing data. All telemetry packets delivered to the SCU must be complete, independently decodable entities.
3.  **Science Data Rate:** The average downlink rate for XRT science telemetry, as delivered to the SCU, shall not exceed **3.9 kbps** over any significant observation period (e.g., one orbit).
4.  **Flight Hardware:** The software must operate within the computational (CPU, memory), storage (buffer size), and power limits of the qualified XRT Control Processor hardware.
5.  **Real-Time Operation:** The software must meet all hard and soft real-time deadlines for command response, data acquisition, and HK sampling.

### 2.5 Assumptions and Dependencies
*   The SCU provides a stable, compliant 1553 interface.
*   The CCD camera hardware and low-level drivers function as specified in the hardware ICD.
*   Accurate time correlation between the spacecraft clock and science data is provided by the SCU.

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 Spacecraft (SCU) Interface
*   **IF-001:** The FSW shall communicate with the Swift SCU via the MIL-STD-1553B bus as a Remote Terminal (RT).
*   **IF-002:** The FSW shall receive and acknowledge telecommunications as defined in the SC-ICD-001.
*   **IF-003:** The FSW shall transmit HK and science telemetry packets to the SCU using the messaging scheme defined in SC-ICD-001.

#### 3.1.2 XRT CCD Camera Interface
*   **IF-010:** The FSW shall send control signals and clocking sequences to the CCD camera to initiate exposures and read out frames.
*   **IF-011:** The FSW shall receive digitized pixel data from the CCD camera via a dedicated high-speed serial or parallel interface.

#### 3.1.3 Thermal Hardware Interface
*   **IF-020:** The FSW shall issue proportional power commands to the telescope tube heater drivers based on temperature sensor feedback.
*   **IF-021:** The FSW shall issue on/off commands to the thermal baffle heater drivers based on temperature sensor feedback.

### 3.2 Functional Requirements

#### 3.2.1 Command Processing
*   **FUNC-010:** The FSW shall accept and validate all command opcodes defined in the XRT Command Dictionary.
*   **FUNC-011:** The FSW shall transition the instrument between the following predefined states upon command: OFF, STANDBY, IDLE, SCIENCE, CALIBRATION, SAFE.
*   **FUNC-012:** The FSW shall configure the CCD camera into the commanded mode (e.g., Imaging, Photodiode, Windowed, Timing) with all associated parameters (exposure time, sub-array coordinates, etc.).
*   **FUNC-013:** The FSW shall provide a positive verification (acknowledgment) or negative verification (error code) for each received command.

#### 3.2.2 Science Data Handling
*   **FUNC-020:** The FSW shall acquire a full frame of raw pixel data from the CCD camera per the configured science mode.
*   **FUNC-021:** The FSW shall perform onboard processing of raw frames, including at minimum: bias level subtraction, cosmic ray rejection, and X-ray event detection/grading.
*   **FUNC-022:** The FSW shall format the processed science data into CCSDS-compliant Source Packets with the Application Process ID (APID) as defined in the ICD.
*   **FUNC-023:** The FSW shall manage an internal science data buffer to temporarily hold packets prior to transmission to the SCU.

#### 3.2.3 Telemetry Generation
*   **FUNC-030:** The FSW shall generate real-time HK packets at a rate of 1 Hz.
    *   **CONSTRAINT-001 (FUNC-030):** Each 1 Hz HK packet shall be ≤ 230 bytes.
*   **FUNC-031:** The FSW shall generate and transmit buffered science telemetry packets to the SCU as bandwidth is available.
    *   **CONSTRAINT-002 (FUNC-031):** The average rate of science telemetry transmission shall be ≤ 3.9 kbps.
*   **FUNC-032:** All telemetry packets (HK and Science) shall be complete, containing all necessary data for ground processing without reassembly or decompression.
    *   **CONSTRAINT-003 (FUNC-032):** No packet segmentation or data compression shall be used.

#### 3.2.4 Thermal Control
*   **FUNC-040:** The FSW shall sample temperature sensors for the telescope tube and thermal baffles at a rate of 0.1 Hz.
*   **FUNC-041:** The FSW shall implement a proportional-integral-derivative (PID) control algorithm to maintain the telescope tube temperature within ±1.0°C of the setpoint.
*   **FUNC-042:** The FSW shall implement a thermostatic (hysteresis) control algorithm to maintain the thermal baffle temperatures within their specified operational range.

#### 3.2.5 Fault Management
*   **FUNC-050:** The FSW shall monitor critical HK parameters (e.g., voltages, temperatures, camera status) against predefined red and yellow limits.
*   **FUNC-051:** Upon detection of a red-limit violation, the FSW shall autonomously transition the instrument to SAFE mode and notify the SCU via a dedicated alarm packet.
*   **FUNC-052:** Upon detection of a yellow-limit violation, the FSW shall generate an alert within the standard HK telemetry for ground operator awareness.

### 3.3 Performance Requirements
*   **PERF-001:** The FSW shall respond to a time-critical command (e.g., "Enter SAFE Mode") within 50 milliseconds of receipt.
*   **PERF-002:** The FSW shall complete the processing of one full CCD frame (including event detection) within 2.4 seconds to support the required observational cadence.
*   **PERF-003:** The time correlation accuracy between the spacecraft time (embedded in the telemetry packet header) and the science data shall be better than 1 millisecond.

### 3.4 Design Constraints
*   **DES-001:** The software shall be developed in ANSI C, compliant with the MISRA C guidelines for safety-critical systems.
*   **DES-002:** The software shall utilize the real-time operating system (RTOS) provided with the flight processor (e.g., VxWorks, RTEMS).
*   **DES-003:** All inter-task communication and synchronization shall use RTOS-provided mechanisms (queues, semaphores).

### 3.5 Software System Attributes

#### 3.5.1 Reliability
*   **ATTR-001:** The software shall achieve a minimum of 99.9% availability over a 24-hour period during nominal science operations.

#### 3.5.2 Maintainability
*   **ATTR-010:** All software modules shall have a cyclomatic complexity of less than 15.

#### 3.5.3 Safety
*   **ATTR-020:** The software shall ensure that under no single-point failure shall the heaters be driven to a condition that could damage the telescope optics or structure.

---
**APPROVALS**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| **Software Lead** | | | |
| **Systems Engineer** | | | |
| **Project Manager** | | | |