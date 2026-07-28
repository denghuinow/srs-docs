# Software Requirements Specification (SRS)
## For the X-Ray Telescope Control Processor (XCP) Flight Software
**Document ID:** SRS-XCP-FSW-001  
**Version:** 1.0  
**Date:** [Date of Generation]  
**Status:** Draft for Review

---

### **1.0 Introduction**

#### **1.1 Purpose**
This Software Requirements Specification (SRS) document defines the functional, performance, and design requirements for the X-Ray Telescope Control Processor (XCP) Flight Software (FSW). This software is responsible for controlling the Swift mission's X-Ray Telescope (XRT) to autonomously detect, locate, and observe Gamma-Ray Bursts (GRBs). The intended audience includes stakeholders, project managers, systems engineers, software developers, testers, and integration personnel from Penn State University (PSU), Southwest Research Institute (SwRI), NASA Goddard Space Flight Center (GSFC), and associated ground operations teams.

#### **1.2 Scope**
The XCP FSW operates on the XRT instrument's onboard processor. Its scope encompasses:
*   Control of the CCD camera and its operational modes (Imaging, Photo-diode, Windowed Timing, Photon Counting).
*   Autonomous processing of science data for GRB detection and centroiding.
*   Management of instrument states and thermal systems (heaters, TEC).
*   Communication with the Swift spacecraft via the MIL-STD-1553B data bus.
*   Collection and reporting of housekeeping telemetry.
*   Handling of faults and errors to ensure robust operation over the mission's three-year design life.
*   Provision of interfaces for ground testing and simulation.

Out of scope: The design of the physical hardware, low-level device drivers for non-XRT components, and the ground-based data processing systems (though compatibility is a key requirement).

#### **1.3 Definitions, Acronyms, and Abbreviations**
| Term | Definition |
| :--- | :--- |
| **BIT** | Built-In Test |
| **CCD** | Charge-Coupled Device (camera) |
| **CCSDS** | Consultative Committee for Space Data Systems |
| **FSW** | Flight Software |
| **GRB** | Gamma-Ray Burst |
| **GSE** | Ground Support Equipment |
| **HK** | Housekeeping |
| **PID** | Proportional-Integral-Derivative (control loop) |
| **PSU** | Penn State University |
| **SAA** | South Atlantic Anomaly |
| **SCU** | Spacecraft Control Unit |
| **SMOC** | Science Mission Operations Center |
| **SRR** | Software Requirements Review |
| **SwRI** | Southwest Research Institute |
| **TBR** | To Be Resolved |
| **TBD** | To Be Determined |
| **TEC** | Thermoelectric Cooler |
| **XCP** | X-ray telescope Control Processor |
| **XRT** | X-Ray Telescope |

#### **1.4 References**
1.  Swift Mission Level Requirements Document, NASA GSFC.
2.  XRT Instrument Requirements Document, PSU.
3.  MIL-STD-1553B, "Digital Time Division Command/Response Multiplex Data Bus".
4.  CCSDS 133.0-B, "Telemetry Space Data Link Protocol".
5.  SSFF, IMAGE, CUBIC Project Software Design Documents, SwRI. *(Note: Updates to this list are required per stakeholder review)*

#### **1.5 Document Overview**
This document is structured to present a comprehensive view of the software requirements. Following this introduction, Section 2 provides an overall description of the product and its operating environment. Section 3 details specific requirements, organized by functionality, interface, and quality attributes. Appendices may contain supporting data models and traceability matrices.

---

### **2.0 Overall Description**

#### **2.1 Product Perspective**
The XCP FSW is a component of the Swift XRT instrument. It interfaces with the Swift spacecraft avionics and acts as the sole controller for the XRT's science and support subsystems.

**System Interfaces:**
*   **Spacecraft (SCU):** Primary command and data interface via a MIL-STD-1553B bus.
*   **XRT CCD Camera:** Direct control for mode setting, data acquisition, and readout.
*   **XRT Thermal System:** Control of heaters and the CCD Thermoelectric Cooler (TEC).
*   **XRT Analog Sensors:** Acquisition of voltages, currents, and temperatures for housekeeping.
*   **Ground Test Equipment:** Support for RS-232 and Ethernet interfaces for pre-launch integration and testing.

#### **2.2 User Characteristics**
The primary "users" of the software are the systems and subsystems it controls, and the ground operators who command it. Key stakeholder roles are:
*   **Scientist (PSU):** Requires autonomous, accurate GRB data.
*   **Flight Software Engineer (SwRI):** Requires a modular, reliable codebase.
*   **Mission Operator (SMOC):** Requires clear, timely telemetry for health monitoring.
*   **Systems Integrator:** Requires accurate simulators for testing.
*   **Ground Software Developer:** Requires standardized, compatible data packets.
*   **Project Manager:** Requires robust fault tolerance for mission assurance.

#### **2.3 Design and Implementation Constraints**
1.  **Hardware:** Must operate within the computational (CPU throughput, memory) and power constraints of the RAD6000 processor and associated flight hardware.
2.  **Standards:** Shall implement CCSDS packet standards for telemetry and MIL-STD-1553B protocols for bus communication.
3.  **Legacy Code:** Shall maximize reuse of qualified software components from the SSFF, IMAGE, and CUBIC projects to reduce cost and risk.
4.  **Safety:** Shall implement safeguards against unsafe commands (e.g., premature door opening, thermal runaway).

#### **2.4 Assumptions and Dependencies**
*   The spacecraft will provide stable power, a 1PPS signal, and periodic time synchronization messages.
*   The PSU science algorithms for event recognition and centroiding will be delivered and integrated as a software component.
*   Ground system simulators (SCU, 1553) from Spectrum Astro will be available for integration testing.
*   The mission-level definition of South Atlantic Anomaly (SAA) entry/exit (flag or 3-circle model) will be provided.

---

### **3.0 Specific Requirements**

#### **3.1 Functional Requirements**

##### **3.1.1 Boot and Initialization (XCP-FUN-001)**
*   **XCP-FUN-001.1:** The software shall perform a full initialization sequence upon power-up or watchdog timer reset.
*   **XCP-FUN-001.2:** The software shall execute a suite of Built-In Tests (BIT) on CPU, memory, and critical interfaces during initialization.
*   **XCP-FUN-001.3:** The software shall load the operational flight program from the designated EEPROM boot block.

##### **3.1.2 Command Processing (XCP-FUN-002)**
*   **XCP-FUN-002.1:** The software shall receive, validate (checksum), and decode commands from the MIL-STD-1553B bus.
*   **XCP-FUN-002.2:** The software shall dispatch valid commands to the appropriate subsystem handler (camera control, thermal control, configuration).
*   **XCP-FUN-002.3:** The software shall reject and log invalid commands with an appropriate error code.

##### **3.1.3 Science Data Acquisition & Processing (XCP-FUN-003)**
*   **XCP-FUN-003.1:** The software shall control the CCD camera, cycling through the following modes based on incident flux: Imaging, Photo-diode, Windowed Timing, Photon Counting. *(Note: Final numerical thresholds for mode transitions are TBD - see Table 2)*.
*   **XCP-FUN-003.2:** The software shall execute PSU-provided algorithms to detect potential GRB events within the CCD data stream.
*   **XCP-FUN-003.3:** Upon detection, the software shall calculate the centroid position of the GRB source to a specified accuracy.
*   **XCP-FUN-003.4:** The software shall generate formatted Science Report packets containing observation data, centroid results, and timestamps for downlink.

##### **3.1.4 Housekeeping Collection (XCP-FUN-004)**
*   **XCP-FUN-004.1:** The software shall periodically collect data from all analog and digital health sensors (temperature, voltage, current, status flags).
*   **XCP-FUN-004.2:** The software shall format this data into standard CCSDS Housekeeping Telemetry Packets.
*   **XCP-FUN-004.3:** The software shall transmit HK packets to the spacecraft at a configurable rate (e.g., 1 Hz).

##### **3.1.5 Time Synchronization (XCP-FUN-005)**
*   **XCP-FUN-005.1:** The software shall maintain a local mission elapsed time clock.
*   **XCP-FUN-005.2:** The software shall synchronize its local clock upon receipt of a spacecraft time message, using the 1PPS signal for fine adjustment.

##### **3.1.6 Error Handling and Fault Management (XCP-FUN-006)**
*   **XCP-FUN-006.1:** The software shall detect single-bit memory errors using EDAC and correct them autonomously.
*   **XCP-FUN-006.2:** The software shall log all detected errors (memory, interface, task) with a unique ID, timestamp, and context.
*   **XCP-FUN-006.3:** Upon detection of a multiple-bit memory error or other unrecoverable fault, the software shall initiate a controlled software reboot.

##### **3.1.7 Thermal Control (XCP-FUN-007)**
*   **XCP-FUN-007.1:** The software shall monitor temperatures of the telescope tube, baffle, and CCD.
*   **XCP-FUN-007.2:** The software shall regulate heater outputs using PID control loops to maintain components within their survival and operational ranges.
*   **XCP-FUN-007.3:** The software shall control the CCD TEC to maintain the CCD at its optimal operational temperature.

#### **3.2 External Interface Requirements**

##### **3.2.1 Spacecraft 1553B Interface (XCP-INT-001)**
*   **XCP-INT-001.1:** The software shall implement the MIL-STD-1553B remote terminal protocol as specified by the SCU interface control document.
*   **XCP-INT-001.2:** The software shall respond to valid bus commands within the required timeframe.

##### **3.2.2 Ground Test Interfaces (XCP-INT-002)**
*   **XCP-INT-002.1:** The software shall support a command/telemetry interface via RS-232 for bench testing.
*   **XCP-INT-002.2:** The software shall support a simulation/data injection interface via Ethernet for use with ground simulators.

##### **3.2.3 Data Packet Format (XCP-INT-003)**
*   **XCP-INT-003.1:** All telemetry (Science and HK) downlinked via the spacecraft shall conform to CCSDS packet standards.
*   **XCP-INT-003.2:** Critical housekeeping and status packets for immediate ground processing by ITOS shall be uncompressed and non-segmented.

#### **3.3 Data Requirements**
The software shall manage the following core data entities:

| Data Element | Primary Key | Key Attributes |
| :--- | :--- | :--- |
| **CCD Frame** | Frame ID | Pixel array, timestamp, readout mode, bias map |
| **Telecommand** | Command ID | Function code, parameters, source timestamp, checksum |
| **Housekeeping Packet** | HK ID | Sensor array (temps, volts), system status flags, error counts, timestamp |
| **Science Report** | Report ID | Observation ID, target coordinates, flux, centroid data, compressed image data, timestamp |
| **System Configuration** | Config ID | EEPROM map, boot parameters, PID coefficients, mode thresholds |
| **Error Log Entry** | Error ID | Error code, severity, memory address/task ID, timestamp |

*(Note: Specific parameters for TAM offsets, TEC coefficients, etc., are marked TBR and require update)*.

#### **3.4 Non-Functional Requirements**

##### **3.4.1 Reliability & Safety (XCP-NFR-001)**
*   **XCP-NFR-001.1:** The software shall achieve a reliability of 0.99 over a 72-hour autonomous operation period.
*   **XCP-NFR-001.2:** The software shall prevent unsafe actuator commands (e.g., door open during launch phase) via hardware interlocks and software checks.
*   **XCP-NFR-001.3:** Thermal control loops shall include hysteresis and limits to prevent oscillatory behavior or damage.

##### **3.4.2 Performance (XCP-NFR-002)**
*   **XCP-NFR-002.1:** The **average** science data rate produced by the XCP shall not exceed 3.9 kbps over any 10-minute interval.
*   **XCP-NFR-002.2:** The software shall process and centroid a detected GRB event to generate an alert packet within 5 seconds of CCD frame readout completion.
*   **XCP-NFR-002.3:** The software CPU utilization shall have a margin of ≥20% under worst-case science load (validated via analysis in Appendix D).

##### **3.4.3 Maintainability & Supportability (XCP-NFR-003)**
*   **XCP-NFR-003.1:** The software shall be designed with modular components, allowing for independent updates to science algorithms, thermal control, or communication modules.
*   **XCP-NFR-003.2:** At least 40% of the core framework code shall be reused from existing SwRI flight software projects (SSFF, IMAGE, CUBIC).

##### **3.4.4 Compatibility & Testability (XCP-NFR-004)**
*   **XCP-NFR-004.1:** The software's ground test interface shall be functionally identical to its flight (1553) interface to allow SMOC displays and procedures to be used without modification during testing.
*   **XCP-NFR-004.2:** All software functions shall be verifiable through unit test, hardware-in-the-loop test, or simulation.

#### **3.5 Undecided Issues (TBD/TBR)**
1.  Final numerical values for science data acquisition mode transition thresholds (Table 2).
2.  Specific parameters and verification for PSU event recognition/centroiding algorithms.
3.  Data dictionary entries for TAM offsets and TEC control coefficients.
4.  Verification method for requirements in sections 5.22-5.27 of the source material.
5.  Algorithm for determining SAA entry (use spacecraft flag or internal 3-circle model).
6.  Completion of updates to all documents listed in Section 2.0 (References).

---

### **4.0 Appendices**

#### **Appendix A: Traceability Matrix**
*(A table tracing User Stories from the summary to specific SRS requirements (e.g., User Story #1 maps to XCP-FUN-003.2, XCP-FUN-003.3, XCP-NFR-002.2) would be placed here.)*

#### **Appendix B: Data Dictionary**
*(An expanded definition of all data elements, including bit-level formats for packets, would be placed here. This appendix would note fields marked TBR.)*

#### **Appendix C: Risk Log**
| Risk ID | Description | Probability | Impact | Mitigation Strategy | Owner |
| :--- | :--- | :--- | :--- | :--- | :--- |
| R-01 | CPU Throughput Exceeded | Medium | High | Optimize algorithms; validate margins via detailed calculation (Ref. Appendix D). | SwRI |
| R-02 | Memory Buffer Overflow | Low | High | Implement ring buffers; monitor & throttle data production. | SwRI |
| R-03 | Clock Sync Failure | Low | Medium | Use redundant time sources; implement periodic re-sync. | SwRI |
| R-04 | Heater Control Oscillations | Medium | Medium | Tune PID parameters in thermal vacuum test; implement hysteresis. | SwRI/PSU |
| R-05 | Ground System (ITOS) Incompatibility | Medium | High | Mandate uncompressed, non-segmented packets for HK/alert data. | GSFC/SwRI |

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| **Software Lead, SwRI** | | | |
| **Systems Engineer, PSU** | | | |
| **Mission Representative, NASA GSFC** | | | |