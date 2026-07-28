# Short Summary: X-Ray Telescope Control Processor Software Requirements

## Background and Objectives
The Swift X-Ray Telescope (XRT) Control Processor (XCP) Flight Software (FSW) is a Level 4 specification for the Swift Gamma Ray Burst Explorer mission. Its primary objectives are to process science data from the CCD camera, control instrument operations, and communicate with the spacecraft to support GRB observations and afterglow studies.

## In Scope
- Processing science data (images, light curves, spectra) from the CCD camera.
- Receiving and executing commands from the Spacecraft Control Unit (SCU).
- Transmitting housekeeping and science telemetry via MIL-STD-1553B interface.
- Controlling heaters, thermo-electric cooler (TEC), and telescope alignment monitor (TAM).
- Performing error detection, correction, and system health monitoring.

## Out of Scope
- Spacecraft-level functions (e.g., slewing, power management).
- Ground-based data processing or analysis software.
- Hardware design or manufacturing of XRT components.
- Mission planning or high-level observatory coordination.
- External interfaces beyond specified protocols (e.g., non-CCSDS data formats).

## Stakeholders and Core Use Cases
**Stakeholders:**
- **Penn State University (PSU)**: Provides science requirements and develops science flight software components.
- **Southwest Research Institute (SwRI)**: Develops system/framework flight software and integrates the XCP.
- **NASA Goddard Space Flight Center (GSFC)**: Sets mission-level requirements and oversees observatory integration.
- **Spacecraft Control Unit (SCU)**: Commands the XRT and receives telemetry via 1553 bus.
- **Science Mission Operations Center (SMOC)**: Monitors and controls the XRT during operations.
- **Integration and Test Team**: Verifies software functionality during development.

**Core Use Cases:**
1. As a **scientist**, I want the XRT to autonomously detect and centroid on GRB sources so that accurate positions can be relayed to ground telescopes within seconds.
2. As a **flight operator**, I want to command the XRT into different observation modes (Image, Photo-Diode, Photon-Counting) so that I can optimize data collection based on source flux.
3. As a **systems engineer**, I want the software to monitor housekeeping parameters (temperatures, voltages) so that I can detect and respond to anomalies.
4. As a **software developer**, I want reusable components from previous missions (SSFF, IMAGE) so that I can reduce development time and risk.
5. As a **mission planner**, I want the XRT to automatically transition between observation modes based on count rates so that I can maximize science return without manual intervention.
6. As a **ground operator**, I want the ability to upload software patches via EEPROM file system so that I can correct on-orbit issues without full reloads.

## Success Metrics
- Achieve centroiding accuracy of 2.5 arcseconds within 5 seconds of target acquisition.
- Maintain average science telemetry rate below allocated 3.9 kbps.
- Demonstrate >95% CPU margin during worst-case observation scenarios.

## Major Constraints
- TDRSS downlink bandwidth limited to 1 kbps for spacecraft, restricting housekeeping telemetry rates.
- Real-time housekeeping packets must not exceed 230 bytes per SCU frame.
- ITOS ground system cannot reassemble segmented packets or decompress data.
- Limited Malindi ground contacts (~7 per day) restrict time-consuming operations.
- Must reuse existing software components from SSFF, IMAGE, and CUBIC projects.

## Undecided Issues
- Final numerical values for science data acquisition modes (Table 2) are TBD.
- Specific algorithms for bias calculation and centroiding require PSU input.
- Verification methods for several requirements (Sections 5.22-5.27) are TBD.
- Some data dictionary entries (e.g., TAM parameters) need further definition.
- Optimal memory allocation for observation buffers requires additional analysis.