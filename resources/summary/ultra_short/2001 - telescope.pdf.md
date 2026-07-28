**Purpose & Scope**
The system is the flight software for the X-Ray Telescope (XRT) Control Processor on the Swift Gamma Ray Burst Explorer. Its purpose is to autonomously control the XRT instrument, process its scientific CCD data, and manage thermal control and communications with the spacecraft. It does not control the spacecraft's slewing or overall mission planning.

**Product Background / Positioning**
The XRT is one of three science instruments on the Swift observatory, designed for multi-wavelength transient astronomy. The software executes on a dedicated RAD6000 processor within the XRT Electronics Package (XEP). It interfaces directly with the spacecraft's control unit via a MIL-STD-1553B bus and manages all local hardware, including the CCD camera, heaters, coolers, and alignment monitor.

**Core Functional Overview**
1.  Process science data from the CCD camera (images, light curves, spectra) and format it into CCSDS packets for downlink.
2.  Receive and dispatch spacecraft commands to configure instrument states and camera modes.
3.  Transmit detailed housekeeping telemetry (voltages, temperatures, status) to the spacecraft.
4.  Control 36 telescope tube heaters and 3 baffle heaters to maintain thermal stability.
5.  Control the Thermo-Electric Cooler (TEC) to regulate the CCD temperature.
6.  Operate the Telescope Alignment Monitor (TAM) to measure mechanical drift.
7.  Synchronize the local clock with the spacecraft time via 1PPS and time messages.
8.  Execute autonomous observation sequences (Automatic, Preplanned, Target of Opportunity) based on spacecraft slew status and source flux.

**Key Users & Usage Scenarios**
*   **Spacecraft Control Unit (SCU):** The primary command source and telemetry destination. It sends observation targets and mode commands, receives science and housekeeping data.
*   **Ground Operators:** Send direct instrument commands (e.g., diagnostic modes, parameter updates, memory uploads) primarily during manual (MANUAL) or red (RED) system states.
*   **Typical Scenario:** The spacecraft slews to a new GRB target. The software autonomously performs pre-observation calibration, detects the source, centroids its position, and transmits a position message. It then dynamically switches between Image, Photo-Diode, Windowed Timing, and Photon Counting modes based on the decaying source flux to optimize data collection throughout the observation.

**Major External Interfaces**
*   **Spacecraft:** Dual-redundant MIL-STD-1553B bus for commands and telemetry; RS-422 hardline for One-Pulse-Per-Second (1PPS) time synchronization.
*   **Camera Head:** Digital interface for CCD image data.
*   **Telescope Alignment Monitor (TAM):** RS-422 serial interface for image data.
*   **Local Hardware Modules:** Interfaces via VME bus to the Power Distribution Module, Sequencer Module, Analog I/O, and Communication Module.

**Key Non-functional Requirements**
*   **Performance:** Must generate and manage an average science telemetry data rate of ~1 kbps, with peaks up to ~100 kbps for short durations. CPU throughput margin must be calculated and maintained.
*   **Reliability/Availability:** Includes Error Detection and Correction (EDAC) for DRAM, a memory scrubber task, and primary/alternate software images in EEPROM for recovery from failures.
*   **Safety:** Must prevent inadvertent opening of the camera door. Must respond to spacecraft "Safehold" notifications to allow safe power-down.
*   **Constraints:** Real-time housekeeping packets are limited to 230 bytes. The ground system (ITOS) cannot initially reassemble segmented packets or decompress data.

**Constraints, Assumptions & Dependencies**
*   **Downlink Bandwidth:** The TDRSS downlink bandwidth allocated to the spacecraft limits housekeeping data rates.
*   **Ground Contact Limitation:** Limited daily ground contacts dictate that software must avoid time-consuming setup during nominal operations.
*   **External System Capabilities:** Initial dependency on the ground system's (ITOS) inability to process segmented or compressed packets.
*   **Hardware:** Dependent on the correct operation of the RAD6000 processor, MIL-STD-1553B interface chip, and the CCD sequencer (AD21020).

**Priorities & Acceptance Approach**
*   **Top Priority:** Core science data acquisition and processing in AUTO mode, including source detection, centroiding, and mode switching based on flux.
*   **High Priority:** Reliable command and telemetry interfaces with the spacecraft, time synchronization, and thermal control (heaters, TEC).
*   **Medium Priority:** Ground command-able manual (MANUAL) and diagnostic (RED) modes, memory upload/dump capabilities.
*   **Acceptance:** Requirements are verified through analysis, inspection, demonstration, and test. Key performance metrics (data rates, CPU margin) and functional sequences (observation flow) will be demonstrated during integration and test.