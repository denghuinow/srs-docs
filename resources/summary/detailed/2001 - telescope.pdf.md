# Detailed Summary: X-Ray Telescope Control Processor (XCP) Software Requirements

## Background and Scope
The X-Ray Telescope Control Processor (XCP) Flight Software (FSW) is a Level 4 specification for the Swift Gamma Ray Burst Explorer mission. Its primary purpose is to control the X-Ray Telescope (XRT), process science data from the Charge-Coupled Device (CCD) camera, and manage interfaces with the spacecraft. The software handles command reception, telemetry transmission, heater control, and telescope alignment monitoring. Non-goals include implementing field-level hardware details not specified in the referenced interface documents and handling spacecraft-level functions outside the XRT's responsibility.

## Stakeholders Matrix and Use Cases
*   **Penn State University (PSU) Department of Astronomy and Astrophysics (Customer):** Provides science requirements and develops the science data processing algorithms (Event Recognition Processor, Data Collection Control).
*   **Southwest Research Institute (SwRI) Automation and Data Systems Division (Developer):** Responsible for the overall software development, system framework, and integration.
*   **NASA Goddard Space Flight Center (GSFC) (Mission Management):** Defines top-level mission and science requirements.
*   **Swift Spacecraft Control Unit (SCU) (External System):** Provides commands, receives telemetry, and supplies time synchronization via the 1553 bus.
*   **Lockheed Martin Federal Systems (LMFS) (Hardware Supplier):** Supplies the RAD6000 processor board; its documentation informs low-level software requirements.

**Main Scenarios:**
1.  **Automatic Observation Sequence:** Triggered by a spacecraft slew; software autonomously performs bias calculations, detects the GRB source, centroids, and transmits position data.
2.  **Manual Command Processing:** In MANUAL state, ground commands configure observation modes, heater parameters, and diagnostic functions.
3.  **Housekeeping Telemetry Collection:** Periodic sampling of voltages, temperatures, and statuses for downlink.
4.  **Time Synchronization:** Updating the local clock based on spacecraft "time-at-the-tone" messages.
5.  **Error Recovery:** Detecting and logging memory errors (EDAC), performing Built-In Tests (BIT), and recovering via watchdog reset or alternate software boot.

**Exception Scenarios:**
6.  **Red State Operation:** Processing only critical (RED) commands after a fault; all others are rejected.
7.  **CCD Overtemperature or Voltage Error:** Transitioning to a safe state (MANUAL) with the CCD unpowered.
8.  **Uncorrectable Memory Error:** Initiating a processor reset via the watchdog timer.

## Business Process
**Main Process: Automated GRB Observation (Trigger: `SISCATTITUDE` message with `IS_SETTLED=false`)**
1.  **Pre-slew Activities:** While spacecraft is >10 arcminutes from target, calculate row bias map, image bias map, and optionally collect a raw data image.
2.  **Slew Settlement:** Wait for `IS_SETTLED=true`.
3.  **Initial Detection:** Acquire image frames, sum pixels, and check against a detection threshold until source is found or timeout.
4.  **Centroid & Notification:** Perform centroid calculation on detected source; transmit XRT Position Message to UVOT and ground (TDRSS) if successful, else send error.
5.  **Mode Selection:** Based on source flux (counts per second), dynamically switch between Photo-Diode (Fast Timing), Windowed Timing (Slow Timing), and Photon Counting modes.
6.  **Data Processing:** In each mode, process CCD data (collapsing to single pixel/row or analyzing individual events) using the Event Recognition Processor.
7.  **Report Generation:** Generate and compress science data reports (Fast Timing Frame, Spectrum, Event List) for transmission to the spacecraft.
8.  **Observation End:** Conclude when target is occulted and spacecraft slews to a new target.

**Key Branch A: Preplanned/Target of Opportunity Observation**
*   Similar to automatic sequence, but omits the transmission of the autonomous XRT Position Message.

**Key Branch B: Entry into RED State**
*   Trigger: Commanded from MANUAL state or autonomous detection of a severe fault (e.g., CCD bias error).
*   Action: Reject all non-RED commands.
*   Transition: Return to MANUAL state after executing a RED command or after a RED command timeout.

## Domain Model (Key Entities)
*   **System State (`XCP_STATE`):** Required. Represents the operational mode: OFF, BOOT, INIT, MANUAL, AUTO, RED.
*   **Telecommand (`CMD`):** Required. A CCSDS packet containing command data, timestamp, and checksum. Reference to `SC_TIME`.
*   **Housekeeping Data (`HK_*` composites):** Required. Collected sets of sensor readings (voltages, temperatures, statuses) from various subsystems (CCD, Heaters, TEC, etc.).
*   **Science Data Report (`PKG_SS`, `PKG_TDRSS`):** Required. Compressed output products (images, light curves, spectra, event lists) for downlink.
*   **Sequencer Program (`SEQ_PRG`):** Required/Unique. Binary image defining CCD clocking waveforms for a specific observation mode.
*   **Bias Map (`BIAS_MAP_ID`):** Required. Calibration data (per-pixel or per-column) subtracted from science images.
*   **Heater Control Parameters (`THTR_PARMS`, `BHTR_PARMS`):** Required. Setpoints and hysteresis values for tube and baffle heater control loops.
*   **Error Log (`ERRNO`, `BIT_RESULT`, `EDAC` data):** Required. Records of software errors, built-in test results, and memory error occurrences.

## Interfaces and Integrations
1.  **Spacecraft Control Unit (SCU) via MIL-STD-1553B**
    *   **Direction:** Bidirectional.
    *   **Interaction:** Command reception and telemetry transmission using CCSDS packet protocol.
    *   **Input:** Telecommands (`CMD`), Time Synchronization messages (`SITIMETONE`).
    *   **Output:** Housekeeping packets (`PKG_RTHK`), Science data packets (`PKG_TDRSS`, `PKG_SS`), Heartbeat.
    *   **SLA:** Must adhere to bus protocol defined in ICD 1143-EI-S19121; real-time HK packets ≤230 bytes.

2.  **Camera Head (CCD)**
    *   **Direction:** Input.
    *   **Interaction:** Raw analog video data digitized and buffered by the Signal Chain board.
    *   **Input:** `CCD_DATA` stream (rows of pixel values).
    *   **Output:** N/A (Control is via sequencer and DACs).
    *   **SLA:** Data rate varies by mode (e.g., ~60 kHz in Photo-Diode mode).

3.  **Timer/Sequencer Module (TSM)**
    *   **Direction:** Control.
    *   **Interaction:** Load and execute sequencer programs to generate CCD clock waveforms.
    *   **Input:** `SEQ_ID` to select program.
    *   **Output:`SEQ_PRG` download, start/stop control.
    *   **SLA:** Must support up to 64 distinct waveform patterns.

4.  **Telescope Alignment Monitor (TAM) via RS-422**
    *   **Direction:** Bidirectional.
    *   **Interaction:** Power control, command transmission, and image data reception.
    *   **Input:** `TAM_DATA` (CCD image).
    *   **Output:** `TAM_RS422_CMD`, power enable/disable.
    *   **SLA:** Serial interface; data used for centroid-based alignment correction.

5.  **Power Distribution Module (PDM)**
    *   **Direction:** Control.
    *   **Interaction:** Enable/disable relays for heaters, TAM power, TEC, and door actuators.
    *   **Input:** Heater status registers (`PDM_STAT`).
    *   **Output:** Relay control signals (`PDM_EN`, `PDM_DIS`).
    *   **SLA:** Digital I/O; includes over-current protection status.

6.  **Analog I/O System**
    *   **Direction:** Bidirectional.
    *   **Interaction:** Reads housekeeping sensors (voltages, temps) and sets CCD bias voltages via DACs.
    *   **Input:** Multiplexed `ANIO_DATA`.
    *   **Output:`DAC_TBL` values for CCD bias.
    *   **SLA:** Sampling rate and accuracy as defined for telemetry.

7.  **Thermo-Electric Cooler (TEC)**
    *   **Direction:** Control.
    *   **Interaction:** Closed-loop PID control of CCD temperature using a digital potentiometer.
    *   **Input:** Temperature sensor readings.
    *   **Output:`TEC_VOLTAGE` control signals.
    *   **SLA:** Supports automatic/manual cooling/heating modes with configurable ramp rates.

8.  **Ground Support Equipment (GSE) / Engineering Ethernet**
    *   **Direction:** Bidirectional (Development/Test only).
    *   **Interaction:** Used for low-level driver testing, software loading, and debugging via RS-232 or Ethernet.
    *   **Input:** Test commands, software patches.
    *   **Output:** Diagnostic data.
    *   **SLA:** Not used in flight units.

## Acceptance Criteria (Examples)
*   **Capability: Automatic Source Detection and Centroiding**
    *   **Given** the XRT is in AUTO state and a valid `SISCATTITUDE` message with `IS_SETTLED=true` is received,
    *   **When** a detectable GRB source is present in the field of view,
    *   **Then** the software shall acquire an image, identify the source, compute its centroid, and transmit an XRT Position Message within 5 seconds of slew settle.
*   **Capability: Command Processing in RED State**
    *   **Given** the XRT is in the RED state,
    *   **When** a non-RED telecommand is received,
    *   **Then** the software shall reject the command, increment the rejection counter, and transition the state to MANUAL.
*   **Capability: Housekeeping Generation**
    *   **Given** the configured housekeeping period (e.g., 10 seconds),
    *   **When** the periodic timer expires,
    *   **Then** the software shall sample all defined HK sensors, format the data into a CCSDS packet ≤230 bytes, and queue it for transmission to the SCU.

## Non-Functional Metrics
*   **Performance:** Average science data rate shall not exceed the allocated 3.9 kbps. CPU margin calculations (Appendix D) must show sufficient headroom for worst-case processing loads.
*   **Reliability:** The software shall detect and correct single-bit DRAM errors (EDAC) and log multiple-bit errors. It shall recover from fatal errors via watchdog reset and boot from an alternate software image if primary fails.
*   **Security/Compliance:** Software shall comply with NASA MIDEX mission assurance requirements (GSFC-410-MIDEX-003) and Swift-specific guidelines. Flight code shall be write-locked in EEPROM.
*   **Observability:** All significant errors (command rejections, memory errors, task failures) shall be logged to EEPROM and reported in housekeeping telemetry for ground analysis.

## Milestones and Release Strategy
1.  Software Requirements Review (SRR) – Completed (Rev. 1 baseline).
2.  Delivery of Core Framework & Driver CSCs (SwRI).
3.  Delivery of Science Application CSCs (PSU).
4.  Integration and Test (I&T) with Hardware Simulators.
5.  Qualification Testing with Engineering Model (EM) Hardware.
6.  Delivery of Flight Software for integration with Flight Unit (FU).

## Risk List and Mitigation Strategies
1.  **Risk:** CPU throughput margin may be insufficient for worst-case data processing.
    *   **Mitigation:** Detailed performance modeling (Appendix D); optimize algorithms; consider processor speed upgrade option.
2.  **Risk:** Late delivery or changes to PSU-developed science algorithms (XCP-ERP, XCP-DCC).
    *   **Mitigation:** Define clear interfaces early; use simulators for SwRI framework development; maintain regular coordination.
3.  **Risk:** Complexity of autonomous observation sequence leading to logic errors.
    *   **Mitigation:** Extensive simulation and testing using validated scenario scripts; peer review of state transition logic.
4.  **Risk:** EEPROM wear-out from frequent logging of errors/housekeeping.
    *   **Mitigation:** Implement wear-leveling in the EEPROM File System (EEFS); limit high-frequency writes to volatile RAM where possible.
5.  **Risk:** Inadequate fault detection in critical hardware (e.g., CCD heater failure).
    *   **Mitigation:** Implement comprehensive HK limit checking; define safe states (RED, MANUAL) for fault conditions.
6.  **Risk:** 1553 bus communication latency or errors affecting time-critical messages (e.g., position to UVOT).
    *   **Mitigation:** Design with retry capability where possible; validate timing via system-level testing.
7.  **Risk:** Memory leaks or fragmentation over long-term operation (3-year mission).
    *   **Mitigation:** Use static memory allocation where feasible; rigorous testing for memory management errors.
8.  **Risk:** Misinterpretation of evolving interface control documents (ICDs).
    *   **Mitigation:** Maintain strict version control of referenced docs; formalize interface agreement with SCU team.

## Undecided Issues and Responsible Parties
1.  **Final numerical values for science data acquisition modes** (Table 2 details TBD). *Responsible: PSU.*
2.  **Specific algorithms and parameters for centroiding, event recognition, and bias calculation** (Sections 5.22-5.24, 5.26-5.27 TBD/TBR). *Responsible: PSU.*
3.  **Completion of referenced document data** (Section 2.0). *Responsible: SwRI/PSU/GSFC.*
4.  **Final definition of data dictionary items** marked TBD/TBR (Section 6). *Responsible: SwRI/PSU.*
5.  **Verification method for TBD/TBR requirements** (Appendix A). *Responsible: SwRI/PSU.*
6.  **Ground system (ITOS) capability to handle segmented packets** may impact data packaging. *Responsible: GSFC.*
7.  **Precise TEC control coefficients and parameters** (TEC_PARMS_TBL). *Responsible: PSU/Thermal team.*
8.  **South Atlantic Anomaly (SAA) detection method and parameters** (`SAA_FLAG`, `SAA_PARMS`). *Responsible: PSU/SwRI.*