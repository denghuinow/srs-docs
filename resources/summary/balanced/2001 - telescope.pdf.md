# Balanced Summary: X-Ray Telescope Control Processor (XCP) Software Requirements

## Goals and Scope
The XCP Flight Software (FSW) controls the Swift X-Ray Telescope (XRT) to detect and analyze Gamma-Ray Bursts (GRBs) by processing science data from the CCD camera, managing instrument states, and communicating with the spacecraft. It ensures autonomous operation for multi-wavelength observations, including data acquisition, heater control, and error handling, within the constraints of the Swift mission’s three-year lifespan.

## Stakeholders and User Stories
- **Penn State University (PSU)**: Responsible for science software components and overall XRT requirements.
- **Southwest Research Institute (SwRI)**: Develops system and framework flight software and integrates hardware interfaces.
- **NASA Goddard Space Flight Center (GSFC)**: Provides mission-level requirements and oversight.
- **Spacecraft Control Unit (SCU)**: Manages communication and coordination with the XRT via the MIL-STD-1553B interface.
- **Ground Support Equipment (GSE)**: Used for integration, testing, and operational monitoring of the XRT.
- **Science Mission Operations Center (SMOC)**: Handles ground-based command and data display.

**User Stories**:
1. As a **scientist**, I want the XRT to autonomously detect and centroid GRB sources so that accurate positions can be relayed to ground telescopes within seconds.
2. As a **flight software engineer**, I want modular, reusable software components so that development time is reduced and reliability is increased across projects.
3. As a **mission operator**, I want real-time housekeeping telemetry and error reporting so that instrument health can be monitored and anomalies addressed promptly.
4. As a **systems integrator**, I want simulators with interfaces matching the SMOC so that testing and operational displays can be reused without modification.
5. As a **ground software developer**, I want uncompressed, non-segmented packets from the XRT so that the ITOS system can process them without upgrades.
6. As a **project manager**, I want the software to handle memory errors and autonomous recovery so that mission continuity is maintained despite hardware faults.

## Key Processes
1. **Boot and Initialization**: Triggered by power-up or watchdog reset; performs Built-In Tests (BIT) and loads the flight program from EEPROM.
2. **Command Processing**: Triggered by MIL-STD-1553B command receipt; dispatches commands to control instrument state and camera modes.
3. **Science Data Acquisition**: Triggered by slew settle or ground command; cycles through imaging, photo-diode, windowed timing, and photon-counting modes based on flux levels.
4. **Housekeeping Collection**: Triggered periodically; reads analog sensors and transmits health data to the spacecraft.
5. **Time Synchronization**: Triggered by spacecraft time messages; syncs the local clock using 1PPS signals.
6. **Error Handling**: Triggered by memory or interface errors; logs faults, attempts correction, and initiates reboot if unrecoverable.
7. **Heater and TEC Control**: Triggered by temperature thresholds; regulates telescope tube, baffle, and CCD cooler via PID loops.

## Domain Data Elements
- **CCD Data** (Primary Key: Frame ID): Pixel values, row counts, bias maps, event thresholds.
- **Telecommand** (Primary Key: Command ID): Function code, parameters, timestamp, checksum.
- **Housekeeping Packet** (Primary Key: HK ID): Sensor readings (voltages, temperatures), error counts, system status.
- **Science Report** (Primary Key: Report ID): Observation ID, target ID, flux, compressed data, timestamp.
- **System Configuration** (Primary Key: Config ID): EEPROM memory maps, boot indices, CPU speed, network settings.
- **Error Log** (Primary Key: Error ID): Error number, memory address, task ID, timestamp.

## Non-Functional Requirements
1. **Reliability**: The software must detect and correct single-bit memory errors autonomously, with reboot on multiple-bit errors.
2. **Performance**: Average science data rate shall not exceed 3.9 kbps, with peak rates managed via buffering.
3. **Maintainability**: Use modular design and reuse components from SSFF, IMAGE, and CUBIC projects to simplify updates.
4. **Safety**: Prevent inadvertent camera door opening and ensure heater controls avoid thermal damage.
5. **Compatibility**: Adhere to CCSDS packet standards and MIL-STD-1553B protocols for spacecraft communication.
6. **Testability**: Support ground testing via RS-232 and Ethernet interfaces, with simulators matching operational interfaces.

## Milestones and External Dependencies
1. **Software Requirements Review (SRR)**: Completed with revisions in February–March 2001.
2. **Delivery of PSU Science Software**: Dependent on finalization of algorithms for event recognition and centroiding.
3. **Integration with Spacecraft Simulators**: Requires SCU and 1553 bus simulators from Spectrum Astro.
4. **Ground System Readiness**: ITOS must be upgraded to handle segmented packets (if used).
5. **Launch Readiness**: Dependent on successful environmental testing and software validation.

## Risks and Mitigation Strategies
1. **CPU Throughput Exceeded**: Mitigation by optimizing algorithms and validating margins via detailed calculations (Appendix D).
2. **Memory Buffer Overflow**: Mitigation by implementing ring buffers and monitoring data rates against telemetry allocations.
3. **Clock Synchronization Failure**: Mitigation by using redundant time sources and periodic resynchronization.
4. **Heater Control Oscillations**: Mitigation by tuning PID parameters and implementing hysteresis in temperature setpoints.
5. **Ground System Incompatibility**: Mitigation by avoiding packet segmentation and compression for ITOS-critical data.

## Undecided Issues
1. Final numerical values for science data acquisition modes (Table 2) are TBD.
2. Specific parameters for the event recognition and centroiding algorithms require PSU input.
3. Some data dictionary entries (e.g., TAM offsets, TEC coefficients) are marked TBR.
4. Verification methods for certain requirements (Sections 5.22–5.27) are TBD.
5. The method for determining South Atlantic Anomaly (SAA) entry (3-circle vs. spacecraft flag) is pending.
6. Updates to referenced documents (Section 2.0) are incomplete and need review.