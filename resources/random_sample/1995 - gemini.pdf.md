# Balanced Summary

## Goals and Scope
This document defines the operational requirements for the Gemini Control System software, guiding development of controls and data acquisition systems. It establishes general criteria and specific functional requirements for software design across the Gemini 8-m Telescopes Project. The specification targets control system developers rather than science end-users, building upon operational concepts while incorporating both science and control system requirements.

## Roles and User Stories
- **Astronomer**: As an astronomer, I want to submit observing commands via a scheduler so that I can efficiently acquire science data through automated sequences.
- **Science Observer**: As a science observer, I want to monitor data acquisition and validate data integrity so that I can ensure the science plan functions to the astronomer's needs.
- **Telescope Operator**: As a telescope operator, I want direct control of telescope and instruments so that I can maintain system integrity during observations.
- **Support Staff**: As support staff, I want full access to all subsystems so that I can perform maintenance and diagnostic work.
- **Developer**: As a developer, I want access to test-level operation so that I can install and test new software packages and releases.

## Key Processes
1. **System Startup** (trigger: power-on) - The system initializes through cold/warm startup procedures loading all necessary software components.
2. **Observation Planning** (trigger: user request) - Astronomers develop science programs using planning tools and telescope simulators.
3. **Command Submission** (trigger: observation sequence) - Users submit commands to a scheduler queue for execution by the sequencer.
4. **Data Acquisition** (trigger: exposure command) - Detector data is acquired, compressed, and stored in standard formats with multiple backup copies.
5. **Quality Assessment** (trigger: data acquisition) - Quick-look analysis provides on-line data quality evaluation for observer feedback.
6. **System Monitoring** (trigger: continuous operation) - All subsystems are continuously monitored for operational status and fault conditions.
7. **Error Recovery** (trigger: fault detection) - The system implements recovery procedures to handle errors and maintain operation.

## Domain Data Elements
- **Observation Data**: Primary key: Observation_ID; Fields: timestamp, detector_data, instrument_config, weather_conditions, target_coordinates
- **Science Program**: Primary key: Program_ID; Fields: astronomer_id, observation_sequence, scheduling_constraints, instrument_requirements
- **Subsystem Status**: Primary key: Subsystem_ID; Fields: operational_status, configuration, error_logs, performance_metrics
- **Telescope Configuration**: Primary key: Config_ID; Fields: instrument_setup, focus_parameters, tracking_parameters, safety_limits
- **User Session**: Primary key: Session_ID; Fields: user_id, access_level, location, active_commands
- **Engineering Data**: Primary key: Data_ID; Fields: subsystem_telemetry, environmental_data, maintenance_logs, calibration_data

## Non-functional Requirements
- System must support up to 6 active control nodes and 2 monitoring nodes simultaneously
- Command acceptance/rejection within 2 seconds before corresponding action occurs
- Data retention capacity for 7 days of largest instrument data, with last 3 days interactively available
- Support for remote operations with functionality transparent to location despite bandwidth limitations
- Fault detection for 90% of subsystem failures before impacting observations
- Warm startup within 1 minute excluding software download time

## Milestones and External Dependencies
- Definition of G8MT standard for detector data acquisition and storage
- Selection of data transfer link technology
- Establishment of hardware specifications for control systems
- Definition of G8MT standards for online software and development environment
- Development of supportability plan for long-term maintenance

## Risks and Mitigation Strategies
- **Complex distributed system integration**: Use modular design with standardized interfaces and virtual telescope simulation for testing
- **Remote operations bandwidth limitations**: Design system with location transparency and graceful degradation based on available bandwidth
- **Subsystem failure impact**: Implement redundancy where cost-effective and procedures for reconfiguration around failed components
- **Visitor instrument compatibility**: Provide stable, long-lived interface standards while allowing for custom integration as needed
- **Software evolution over long lifecycle**: Use portable code, industry standards, and modular architecture to facilitate upgrades

## Undecided Issues
- Definition of G8MT standard for acquisition and storage of detector data
- Link chosen to transfer data between subsystems
- Desirable hardware specification for control systems
- G8MT standards for online software and development environment
- Supportability plan for long-term system maintenance
- Descriptions and access methods for star catalogs