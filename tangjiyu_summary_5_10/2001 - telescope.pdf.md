# X-Ray Telescope Control Processor Software Requirements Specification

## 1. Scope
This document defines the software requirements for the Swift X-Ray Telescope (XRT) Control Processor (XCP) Flight Software (FSW). This is a Level 4 specification as defined in the Swift Missions Requirements Document.

## 2. System Overview
The Swift observatory is a NASA medium-class explorer satellite for multi-wavelength transient astronomy. Its goal is to determine the origin of Gamma-Ray Bursts (GRBs) and exploit data from these bursts to probe the early universe. Swift employs three semi-autonomous science instruments: the Burst Alert Telescope (BAT), the X-Ray Telescope (XRT), and the Ultraviolet/Optical Telescope (UVOT).

The XRT is a sensitive, autonomous X-ray Charge-Coupled Device (CCD) imaging spectrometer designed to measure the flux, spectrum, and light curve of GRBs and afterglow over a wide dynamic range. It refines BAT positions to 2.5" within 5 seconds of target acquisition for typical bursts.

### 2.1 XRT Electronics Package (XEP)
The XEP is mounted on the Spacecraft and includes:
- VERSAmodule European (VME) enclosure with separate digital and analog sections
- Low voltage power supply
- Lockheed-Martin Federal Systems single board computer using the RAD6000 microprocessor
- Communication board with MIL-STD-1553 interface, Real Time Clock, UART for Telescope Alignment Monitor (TAM)
- Relay board for controlling heaters, TAM power, camera door actuators, and pressure relief valve
- Sequencer board using AD21020 microprocessor to generate CCD clock waveforms
- Housekeeping board for reading voltages, temperatures, and pressure
- Clock board for CCD clock and bias voltage inputs
- Signal Chain board for processing CCD analog video output
- Thermo-Electric Cooler (TEC) power supply

### 2.2 Camera Head
The Camera Head contains the CCD camera with an image section, store section, and two readout registers with video outputs. The CCD has synchronized three-phase clocks that shift pixel rows and individual pixels.

### 2.3 Thermo-Electric Cooler (TEC)
The CCD is cooled by a TEC. The CCD's temperature is closed-loop controlled by the FSW. Telecommands control the temperature setpoint, ramp rate, and mode. A digital potentiometer controls the temperature setpoint.

### 2.4 Power
The XRT is powered by the spacecraft through two 28VDC power buses: Operational Power Bus (OPB) and Survival Power Bus (SPB). The OPB is dual redundant, and the SPB is single string.

### 2.5 Communications Network
The XRT communicates with the spacecraft via dual redundant MIL-STD-1553B serial interface. Data is formatted into packets within frames according to the Swift 1553 Bus Protocol Interface Control Document.

### 2.6 Real Time Clock (RTC)
A local copy of the spacecraft clock is maintained and used to timestamp data packets formatted as CCSDS Source Packets. Synchronization uses an At-The-Tone message and a One-Pulse-Per-Second (1PPS) signal.

### 2.7 Telescope Alignment Monitor (TAM)
The TAM measures changes in mechanical alignment of the XRT tube using a point source of light reflected by mirrors to a CCD camera. A centroid algorithm achieves resolution better than pixel size.

### 2.8 Doors and Sun Shutter
The XRT has a telescope tube door (spacecraft-controlled) and a camera door (XEP-controlled). The camera door cannot be closed once opened. The Sun Shutter is automatically opened/closed by a photosensor but can be overridden.

### 2.9 Heaters
The telescope tube has 36 heater groups closed-loop controlled by FSW. The Mirror Baffle has three heater groups: Survival (spacecraft-controlled) and Control (FSW-controlled).

### 2.10 Housekeeping
The XRT monitors CCD bias/clock voltages, miscellaneous voltages, circuit board/mirror/telescope tube/contamination/baffle/TEC/miscellaneous temperature sensors, and miscellaneous sensors.

## 3. Operational Concepts

### 3.1 Functions
The FSW primary functions include:
- Process science data from the camera and relay to spacecraft as CCSDS Source Packets
- Receive commands from spacecraft establishing instrument state and camera mode
- Transmit detailed housekeeping data to spacecraft as CCSDS Source Packets
- Receive time message and synchronize local spacecraft clock
- Control telescope tube and thermal baffle heaters
- Read the TAM

### 3.2 Observation Sequence
The XRT supports three observation types: Automatic, Preplanned, and Target of Opportunity. The sequence involves:
- Pre-observation activities (calculate row bias map, image bias map, collect raw data image)
- Fast timing mode when spacecraft settles
- Source detection and centroid calculation
- Mode switching based on count rate (Photo-Diode, Windowed Timing, Photon-Counting)

### 3.3 States
FSW states include: Off, Boot, Init, Manual, Red, and Auto. State transitions are controlled by commands, autonomous conditions, and spacecraft actions.

### 3.4 Science Data Acquisition Modes
Modes include Bias Image/Row Calculation, Image, Photo-Diode (Fast Timing), Windowed Timing (Slow Timing), Photon Counting, Null, Ramp DACs, and Raw Data modes.

### 3.5 Error Detection, Reporting and Recovery
- Primary and alternate FSW configurations in EEPROM with software locking
- EDAC memory for error detection and correction
- Memory Scrubber task to repair single bit errors
- Heartbeat message indicating "aliveness" to spacecraft

## 4. Constraints
Key constraints include:
- TDRSS downlink bandwidth limited to 1 kbps
- Limited ground contacts (7 per day of 7-10 minutes)
- Real-time HK packets limited to 230 bytes
- No packet segmentation/reassembly capability in ground system
- Ground system cannot decompress packets

## 5. Goals
Software goals emphasize simplicity, reliability, maintainability, reusability, and testability through:
- Simple, consistent data flow interfaces
- Minimal a priori knowledge of SCU operations
- Modular, reusable designs
- Flexible design for ground I&T and flight configurations
- Error-free code production
- Minimal rework at integration levels
- Fault-tolerant design

## 6. Software Components

### 6.1 System and Framework Flight Software
- MIL-STD-1553B Driver (XCP-1553)
- RS-422 Driver (XCP-422)
- Analog I/O Driver (XCP-ANIO)
- Built-In Tests CSC (XCP-BIT)
- Bootstrap CSC (XCP-BOOT)
- CCD Interface CSC (XCP-CCD)
- Command and Control CSC (XCP-CCM)
- CCD Data Driver (XCP-CDD)
- Data Compression CSC (XCP-DCX)
- Error Detection and Correction CSC (XCP-EDAC)
- EEPROM File System CSC (XCP-EEFS)
- EEPROM Interface Driver (XCP-EEPRM)
- Engineering Ethernet Driver (XCP-ENET)
- Power Distribution Driver (XCP-PDD)
- Periodic Processing CSC (XCP-PP)
- Real-Time Operating System CSC (XCP-RTOS)
- SCU Interface CSC (XCP-SCUI)
- Sequencer CSC (XCP-SEQ)
- Time Synchronization CSC (XCP-TIS)
- Timer/Sequencer Driver (XCP-TSD)
- Tube Heater Control CSC (XCP-THC)

### 6.2 Science Flight Software
- Baffle Heater Control CSC (XCP-BHC)
- Data Collection Control CSC (XCP-DCC)
- Event Recognition Processor CSC (XCP-ERP)
- Telescope Alignment Monitor CSC (XCP-TAM)
- Thermo-electric Cooler CSC (XCP-TEC)

## 7. Data Dictionary
The data dictionary defines key data elements including:
- System configuration and volatile areas
- Built-in test results
- Housekeeping data structures
- Command and telemetry packet formats
- CCD data and control parameters
- Memory and hardware interface definitions
- Time synchronization data
- Heater and TEC control parameters
- Error handling and reporting data
