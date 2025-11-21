# Detailed Summary

## Background and Scope
The X-Ray Telescope Control Processor (XCP) Flight Software controls the Swift Gamma Ray Burst Explorer's X-Ray Telescope instrument. It processes science data from the CCD camera, manages thermal control systems, handles spacecraft communications via MIL-STD-1553B interface, and supports autonomous observation sequences. Non-goals include ground system development and hardware design beyond specified interfaces.

## Role Matrix and Use Cases
- **Spacecraft Control Unit**: Primary command source and telemetry destination
- **Science Operations**: Automated observation sequence execution
- **Ground Operations**: Telecommand uplink and health monitoring
- **Thermal Management**: Heater and cooler control
- **Fault Management**: Error detection and recovery handling
- **Data Processing**: Science data compression and formatting

Main scenarios: Automated burst observation, manual command execution, thermal control operations, fault recovery
Exception scenarios: Memory errors, communication failures, CCD over-temperature conditions

## Business Process
**Main Observation Process (8 steps)**:
1. Receive slew notification from spacecraft
2. Perform pre-observation bias calculations
3. Detect settled attitude
4. Acquire initial image frame
5. Perform source detection and centroiding
6. Transmit position message
7. Select appropriate data acquisition mode based on flux
8. Continue observation until target occultation

**Key Branches**:
- **Source Not Found**: Continue frame accumulation until timeout
- **Mode Transition**: Switch between imaging, timing, and photon counting based on count rate

## Domain Model
- **Observation** (required: target_id, observation_id, mode)
- **Telecommand** (required: function_code, application_data)
- **Telemetry Packet** (required: APID, sequence_count, timestamp)
- **CCD Data** (required: pixel_data, frame_count)
- **Heater Control** (required: heater_id, setpoint, status)
- **Memory Block** (required: address, checksum, size)
- **Sequencer Program** (required: program_id, waveform_pattern)
- **Error Log** (required: error_number, timestamp, address)

## Interfaces and Integrations
- **MIL-STD-1553B Driver**: System: Spacecraft, Direction: Bidirectional, Input: Commands, Output: Telemetry packets, SLA: Real-time response
- **RS-422 Driver**: System: Telescope Alignment Monitor, Direction: Bidirectional, Input: TAM image data, Output: Control commands
- **Analog I/O Driver**: System: Housekeeping sensors, Direction: Input, Input: Voltage/temperature readings, Output: None
- **EEPROM File System**: System: Non-volatile storage, Direction: Bidirectional, Input: File operations, Output: Stored data, SLA: 100k write cycles
- **Power Distribution**: System: Heater/TEC control, Direction: Output, Input: Enable commands, Output: Relay status
- **Timer/Sequencer**: System: CCD clock generation, Direction: Output, Input: Waveform programs, Output: Clock signals

## Acceptance Criteria
**Given** the spacecraft is settled on target **When** in AUTO mode **Then** XCP shall automatically begin observation sequence

**Given** a memory single-bit error occurs **When** EDAC detects it **Then** system shall correct error and log event

**Given** CCD temperature exceeds threshold **When** in any operational state **Then** system shall transition to safe state

**Given** valid telecommand received **When** in MANUAL state **Then** system shall execute command and return status

## Non-functional Metrics
- **Performance**: Process CCD data at 60,000 pixels/sec, respond to commands within 100ms
- **Reliability**: 99.9% uptime, automatic recovery from single-bit memory errors
- **Security**: Command authentication, memory protection
- **Compliance**: CCSDS packet standards, MIL-STD-1553B protocol
- **Observability**: Comprehensive housekeeping telemetry, error logging

## Milestones and Release Strategy
1. Driver-level integration complete
2. Application framework verification
3. Science algorithm integration
4. System-level testing
5. Flight software delivery
6. On-orbit commissioning

## Risk List and Mitigation Strategies
- **CPU throughput margin**: Conservative performance estimates, optimization of critical algorithms
- **Memory corruption**: EDAC protection, memory scrubbing, checksum verification
- **Command processing delays**: Priority-based task scheduling, watchdog monitoring
- **Thermal control stability**: PID tuning margins, redundant temperature sensors
- **Data loss during high rates**: Buffering strategies, flow control mechanisms
- **Clock synchronization errors**: Redundant time sources, graceful degradation
- **EEPROM wear**: Write minimization strategies, wear leveling
- **Single event upsets**: Error detection/correction, safe state transitions

## Undecided Issues and Responsible Parties
- Final science data acquisition mode parameters (PSU)
- TEC control algorithm coefficients (PSU)
- Bias calculation algorithms selection criteria (PSU)
- SAA detection method parameters (SwRI/PSU)
- Memory dump packet segmentation strategy (SwRI)
- Final telemetry compression ratios (SwRI/PSU)
- On-orbit patch management procedures (SwRI)
- Not mentioned: Final radiation hardening requirements