# Software Requirements Specification (SRS)
## Flight Software for the X-Ray Telescope Control Processor (XRT-CP)
### Swift Gamma Ray Burst Explorer Observatory

**Document Identifier:** SRS-XRT-CP-FSW-1.0
**Date:** 2023-10-27
**Status:** Preliminary

---

## 1. Introduction

### 1.1 Purpose
This document defines the requirements for the Flight Software (FSW) of the X-Ray Telescope Control Processor (XRT-CP) on the Swift Gamma Ray Burst Explorer observatory. It serves as a contract between the software development team, systems engineering, instrument team, and mission operations to ensure a common understanding of the software's functionality, performance, and constraints.

### 1.2 Scope
The XRT-CP FSW is responsible for the real-time control and data handling of the X-Ray Telescope (XRT) instrument. Its scope encompasses:
*   Processing science data from the Charge-Coupled Device (CCD) camera.
*   Managing all command and telemetry interfaces with the spacecraft's Spacecraft Control Unit (SCU).
*   Executing thermal control loops for instrument stability.
*   Managing internal instrument states and modes.
*   Synchronizing with the spacecraft's time reference.
*   The software resides on the dedicated XRT Control Processor hardware. It interfaces with the Swift SCU, the XRT CCD camera, the Telescope Alignment Monitor (TAM), and various thermal control hardware (heaters, Thermo-Electric Cooler). It does **not** include ground-based software (e.g., ITOS), spacecraft bus FSW, or the scientific algorithms for data analysis performed on the ground.

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **CCDS** | Consultative Committee for Space Data Systems |
| **CCSDS** | CCSDS Packet Telemetry standard |
| **FSW** | Flight Software |
| **HK** | Housekeeping |
| **ITOS** | Integrated Test and Operations System (Ground system) |
| **SCU** | Spacecraft Control Unit |
| **TAM** | Telescope Alignment Monitor |
| **TDRSS** | Tracking and Data Relay Satellite System |
| **TEC** | Thermo-Electric Cooler |
| **XRT** | X-Ray Telescope |
| **XRT-CP** | X-Ray Telescope Control Processor |

### 1.4 References
1.  Swift Observatory Mission Requirements Document (MRD)
2.  XRT Instrument Interface Control Document (ICD)
3.  Swift SCU to Payload ICD
4.  CCSDS 102.0-B-6: Packet Telemetry
5.  CCSDS 202.0-B-4: TC Synchronization and Channel Coding

### 1.5 Overview
The remainder of this SRS is organized as follows: Section 2 provides a high-level description of the product and its operational context. Section 3 details specific requirements, organized by functionality, interfaces, and quality attributes.

## 2. Overall Description

### 2.1 Product Perspective
The XRT-CP FSW is a component of the larger Swift observatory system. It acts as the intermediary between the spacecraft bus and the XRT instrument hardware.

**System Interfaces:**
*   **Spacecraft Control Unit (SCU):** Primary command and data interface. Receives time-tagged and real-time commands, transmits HK and science telemetry packets.
*   **XRT CCD Camera:** Source of science image data.
*   **Telescope Alignment Monitor (TAM):** Provides alignment data.
*   **Thermal Hardware:** Heater relays (tube, baffle) and TEC controller for temperature regulation.
*   **XRT-CP Internal Hardware:** Timers, ADCs, GPIOs, watchdog.

### 2.2 Product Functions
The core functions of the XRT-CP FSW are:
1.  **Science Data Processing:** Acquire, process, and packetize CCD image data into CCSDS packets.
2.  **Command Execution:** Decode, validate, and execute commands from the SCU.
3.  **Telemetry Generation:** Generate and transmit real-time and stored HK telemetry packets containing engineering data.
4.  **Thermal Control:** Execute closed-loop control algorithms to maintain instrument components within their operational temperature ranges.
5.  **Time Management:** Synchronize the internal clock with spacecraft time and timestamp all data.
6.  **State Management:** Manage instrument operational modes (e.g., SLEEP, STANDBY, SCIENCE) and fault detection states.

### 2.3 User Characteristics
*   **Primary "User":** The **Spacecraft Control Unit (SCU)**. It is an automated system that sends commands and receives telemetry via defined protocols. It requires deterministic, reliable responses.
*   **End Users:** **Ground Operators** at the Mission Operations Center. They interact indirectly via telecommands (TC) and telemetry (TM). They are experts in spacecraft operations but rely on the software to present data in the specified, constrained formats.

### 2.4 Constraints
1.  **Downlink Bandwidth:** The TDRSS allocation for XRT is **1 kbps**, imposing strict limits on total telemetry volume.
2.  **Packet Size:** Real-time HK packets **shall not exceed 230 bytes** to comply with SCU buffer limitations.
3.  **Ground System Limitations:** The spacecraft **does not reassemble segmented packets**, and the ITOS ground system **cannot decompress packets**. All packetization and compression must be transparently reversible on the ground.
4.  **Contact Schedule:** Ground contacts are limited to approximately **seven per day, each 7-10 minutes long**, driving the need for autonomous operation and stored data management.
5.  **Real-Time Operation:** The software must meet all hard real-time deadlines for command processing, thermal control, and data acquisition.
6.  **Radiation Environment:** The software must be designed for operation in a space radiation environment, incorporating mitigation strategies for Single Event Effects (SEEs).

### 2.5 Assumptions and Dependencies
*   The SCU provides a stable, synchronized 1 Hz time pulse.
*   The XRT hardware interfaces (electrical, protocol) are stable as defined in the ICDs.
*   The allocated 1 kbps downlink bandwidth is a fixed constraint for mission lifetime.

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 SCU Command Interface (RS-422)
*   **XRT-CP-FSW-INT-001:** The software shall receive command transfer frames from the SCU via the RS-422 asynchronous serial interface as defined in the SCU-Payload ICD.
*   **XRT-CP-FSW-INT-002:** The software shall decode CCSDS Telecommand Packets from the received frames.
*   **XRT-CP-FSW-INT-003:** The software shall generate a command acceptance or error response packet for each valid command received, as specified by the protocol.

#### 3.1.2 SCU Telemetry Interface (RS-422)
*   **XRT-CP-FSW-INT-010:** The software shall transmit CCSDS Telemetry Packets to the SCU via the dedicated RS-422 serial interface.
*   **XRT-CP-FSW-INT-011:** The software shall format all packets (HK and Science) according to CCSDS 102.0-B-6, with APID, sequence count, and timestamp.
*   **XRT-CP-FSW-INT-012:** The software shall not transmit packets at an aggregate rate exceeding the 1 kbps allocated bandwidth.

#### 3.1.3 CCD Camera Interface
*   **XRT-CP-FSW-INT-020:** The software shall initiate and control CCD image readout via the defined parallel digital interface.
*   **XRT-CP-FSW-INT-021:** The software shall collect raw pixel data from the CCD and apply onboard calibration (bias subtraction, flat-field reference).

### 3.2 Functional Requirements

#### 3.2.1 Command Processing
*   **XRT-CP-FSW-FUN-001:** The software shall process real-time commands within 100 ms of receipt from the SCU.
*   **XRT-CP-FSW-FUN-002:** The software shall manage a time-tagged command queue and execute commands at the specified spacecraft MET.
*   **XRT-CP-FSW-FUN-003:** The software shall validate all commands for correctness (length, checksum, parameter ranges) before execution.
*   **XRT-CP-FSW-FUN-004:** The software shall support commands for: mode transitions, heater/TEC setpoint changes, CCD configuration, memory load/dump, and software reset.

#### 3.2.2 Housekeeping Telemetry Generation
*   **XRT-CP-FSW-FUN-010:** The software shall generate a Real-Time HK packet at a configurable rate (1 Hz default).
*   **XRT-CP-FSW-FUN-011:** Each Real-Time HK packet shall include: processor status, mode, temperatures (tube, baffle, CCD), primary voltages, heater states, TEC current, and error counters.
*   **XRT-CP-FSW-FUN-012:** The software shall generate a Stored HK packet at a lower rate (e.g., 1/60 Hz) for playback during ground contacts, containing all data from requirement XRT-CP-FSW-FUN-011 plus supplemental data.
*   **XRT-CP-FSW-FUN-013:** The size of the Real-Time HK packet shall be ≤ 230 bytes.

#### 3.2.3 Science Data Processing
*   **XRT-CP-FSW-FUN-020:** The software shall format processed CCD image data into CCSDS Source Packets.
*   **XRT-CP-FSW-FUN-021:** The software shall support multiple observation modes (e.g., Imaging, Photodiode) with different data formats and rates as commanded.
*   **XRT-CP-FSW-FUN-022:** The software shall apply lossless compression to science data packets before transmission, as the ground system cannot decompress.
*   **XRT-CP-FSW-FUN-023:** Science data packets shall be stored in a non-volatile memory buffer for later downlink if real-time downlink is unavailable.

#### 3.2.4 Thermal Control
*   **XRT-CP-FSW-FUN-030:** The software shall execute a 10 Hz control loop to read temperature sensors (tube, baffle, CCD).
*   **XRT-CP-FSW-FUN-031:** The software shall control the tube and baffle heater relays using a proportional (P) control law to maintain setpoints within ±2°C.
*   **XRT-CP-FSW-FUN-032:** The software shall control the TEC to maintain the CCD temperature at its commanded setpoint (-75°C ± 0.5°C).
*   **XRT-CP-FSW-FUN-033:** Heater and TEC control shall be automatically disabled in SAFE mode.

#### 3.2.5 Time Synchronization & TAM
*   **XRT-CP-FSW-FUN-040:** The software shall synchronize its internal clock to the spacecraft MET using the 1 Hz pulse from the SCU.
*   **XRT-CP-FSW-FUN-041:** All telemetry packets shall be timestamped with the synchronized MET.
*   **XRT-CP-FSW-FUN-042:** The software shall read the Telescope Alignment Monitor (TAM) sensor at a commanded rate and include the data in the HK telemetry stream.

### 3.3 Performance Requirements
*   **XRT-CP-FSW-PER-001:** The software shall utilize ≤ 70% of the processor's worst-case timing budget to maintain a 20% margin for operations.
*   **XRT-CP-FSW-PER-002:** The software shall boot from a cold start and be ready to receive commands within 60 seconds of power application.
*   **XRT-CP-FSW-PER-003:** The watchdog timer shall be serviced within the defined timeout period (e.g., 500 ms). Failure to service shall trigger a processor reset.

### 3.4 Design Constraints
*   **XRT-CP-FSW-CON-001:** The software shall be written in ANSI C, with no dynamic memory allocation after initialization.
*   **XRT-CP-FSW-CON-002:** The software shall be structured as a cyclic executive with a fixed 10 Hz major frame.
*   **XRT-CP-FSW-CON-003:** All critical data structures and variables shall be protected against corruption by Single Event Upsets (SEUs) using EDAC memory or software-based redundancy/checksums.

### 3.5 Software Quality Attributes
*   **Reliability:** The software shall have a Mean Time Between Failures (MTBF) of > 50,000 hours. All single-point failures shall be identified and mitigated where possible.
*   **Availability:** The software shall be available for science operations > 99% of the time, excluding planned outages for ground contacts or spacecraft maneuvers.
*   **Maintainability:** The code shall adhere to a defined coding standard (e.g., NASA JPL or MISRA C subset) and be fully documented with Doxygen-style comments.
*   **Safety:** The software shall implement a SAFE mode, entered autonomously upon detection of critical faults (e.g., over-temperature, persistent communication loss), which disables non-essential functions and maintains survival heating.

---
**END OF DOCUMENT**