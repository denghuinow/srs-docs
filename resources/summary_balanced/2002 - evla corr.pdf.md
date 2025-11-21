# Balanced Summary

## Goals and Scope
The EVLA Correlator Monitor & Control System provides the physical link between WIDAR Correlator hardware and the EVLA monitor & control system. It handles correlator configuration, operation, and servicing while providing hardware abstraction through the Virtual Correlator Interface. Primary functions include receiving configuration data, processing dynamic control data, monitoring system health, and enabling testing access.

## Roles and User Stories
- **Array Operator**: I want to receive status and error messages through the M&C system so that I can monitor array operations effectively.
- **Engineer/Technician**: I want remote inspection tools so that I can diagnose faults to specific hot-swappable subsystems.
- **Software Developer**: I want remote system access so that I can troubleshoot during non-working hours.
- **Administrator**: I want unrestricted system access so that I can manage all user privileges and system components.
- **Web User**: I want authorized restricted access so that I can view normally protected system areas.

## Key Processes
1. **System Initialization** (trigger: power-on) - CMIBs boot and configure from local storage for standalone operation.
2. **Configuration Reception** (trigger: EVLA M&C input) - MCCC receives and translates configuration data into hardware-specific tables.
3. **Hardware Monitoring** (trigger: continuous operation) - System monitors correlator health and subsystem states.
4. **Data Processing** (trigger: real-time requirements) - CMIBs handle real-time control data with deterministic response times.
5. **Fault Detection** (trigger: system anomalies) - Watchdog processes detect hardware/software failures.
6. **Recovery Execution** (trigger: fault detection) - System autonomously attempts recovery through reboots and failover.
7. **Data Output** (trigger: backend requests) - System provides processed data to backend systems with configurable rates.

## Domain Data Elements
- **Configuration Table**: table_id, hardware_target, parameter_set, validity_period, activation_time
- **Monitor Data**: data_id, timestamp, subsystem_id, health_metrics, error_codes
- **User Account**: user_id, username, access_level, login_credentials, privilege_set
- **Hardware Device**: device_id, ip_address, status_indicator, location, firmware_version
- **Error Log**: log_id, error_time, source_component, severity, description, resolution_status
- **Control Parameter**: param_id, value, update_frequency, destination, validation_rules

## Non-functional Requirements
- System must meet all real-time processing deadlines to prevent data loss
- Hardware shall support hot-swappable components for continuous operation
- Software shall operate between maintenance windows without total restart
- Network interfaces shall provide physical isolation between system layers
- All users must authenticate via secure login mechanisms
- System shall continue partial operations during maintenance activities

## Milestones and External Dependencies
- Integration with EVLA Monitor & Control System interface
- Delivery of auxiliary data feeds (delay models, time codes)
- Backend system capability to handle CMCS output data rates
- Hardware component availability meeting PC104+ standards
- UPS infrastructure implementation for graceful shutdown

## Risks and Mitigation Strategies
- **Network failure**: Redundant communication paths between MCCC and CPCC
- **Hardware faults**: Modular design with hot-swappable components and visual indicators
- **Software hangs**: Hardware watchdog timers for automatic reboot
- **Security breaches**: Multi-layer authentication and privilege management
- **Data overflow**: Configurable data rates and spooling during network outages

## Undecided Issues
- Automatic vs manual backup MCCC activation during failures
- Specific actions for CPCC hardware failures
- Exact delay tolerance for standby mode resumption
- Complete list of hot-swappable components
- Detailed RFI specifications for network materials
- Not mentioned