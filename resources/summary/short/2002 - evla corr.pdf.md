# Short Summary: EVLA Correlator Monitor & Control System Requirements

## Background and Objectives
The EVLA Correlator Monitor & Control System (CMCS) provides the physical link between the WIDAR Correlator hardware and the EVLA monitor & control system, serving as the primary interface for configuring, operating, and servicing the correlator. Its primary objectives are to translate configuration data into hardware settings, process dynamic control and monitor data, ensure system health through autonomous recovery, and provide real-time data processing and debugging tools.

## In Scope
- Translating EVLA M&C configuration data into correlator hardware configurations.
- Processing and transferring dynamic control data (e.g., models, filter parameters) and monitor data (e.g., auto-correlation products).
- Monitoring correlator health and autonomously recovering from hardware and computing faults.
- Performing limited real-time data processing and probing, such as collecting and displaying auto-correlation products.
- Providing easy system access for testing and debugging via the Virtual Correlator Interface (VCI).

## Out of Scope
- Full backend data processing (handled by the Backend Data Processing System).
- Long-term data archiving (managed by the e2e System).
- Direct user interaction without going through the VCI or MCCC.
- Hardware design of the correlator boards themselves.
- External network security beyond the MCCC-EVLA M&C interface.

## Stakeholders and Core Use Cases
**Stakeholders:**
- **Array Operator:** Monitors system status and error messages through the EVLA M&C system.
- **Engineers and Technicians:** Perform maintenance, diagnose faults, and conduct performance tests using remote inspection tools.
- **Software Developer:** Develops and troubleshoots system software, requiring remote access for off-hours support.
- **Web User:** Authorized individuals with restricted access to specific system parts for monitoring or administrative purposes.

**Core Use Cases:**
1. As an Array Operator, I want to view real-time status and error messages so that I can ensure the correlator is operating correctly.
2. As an Engineer, I want to remotely inspect individual CMIB devices so that I can diagnose and repair hardware faults quickly.
3. As a Technician, I want to run performance tests on correlator subsystems so that I can verify system health and functionality.
4. As a Software Developer, I want to access the system remotely so that I can troubleshoot software issues during non-working hours.
5. As a Web User, I want to view restricted system data so that I can monitor specific aspects without full administrative access.
6. As an Administrator, I want to manage user access and privileges so that I can control system security and functionality.

## Success Metrics
- System achieves high availability with minimal downtime, continuing operations during partial maintenance.
- All real-time processing deadlines are met without data loss or corruption.
- Error messages are accurately categorized and accessible for efficient troubleshooting.

## Major Constraints
- The CMCS is critical to the astronomical data path; unavailability results in data loss.
- Hardware must be modular and hot-swappable to facilitate easy fault detection and repair.
- Network interfaces must be isolated (MCCC-CMIB, MCCC-CPCC, MCCC-EVLA M&C) for security and performance.
- Software must support real-time requirements and be written in a readable, familiar language.
- All computers must have local disk and file systems to operate standalone during network failures.

## Undecided Issues
- Specific actions for external systems to take upon CPCC hard failures are to be determined.
- The exact format and protocols for auxiliary data (e.g., delay models, phase corrections) from EVLA M&C or dedicated servers need finalization.
- The method for automatic activation of the backup MCCC system (via CPCC or human intervention) requires further decision.
- The acceptable delay for resuming operations from standby mode is to be determined.
- Details on the implementation of the redundant communication path (e.g., RS-232c) between MCCC and CPCC need final specification.