# Detailed Summary

## Background and Scope
The Gemini Control System software requirements specification defines operational requirements for controlling the Gemini 8-meter telescopes and associated instrumentation. The system supports multiple observing modes including interactive, queue-based, remote operations, and service observing. It establishes criteria for software development across telescope control, data acquisition, and instrument interfaces. Non-goals include complete hardware redundancy and automatic failover systems.

## Role Matrix and Use Cases
**Roles:** Astronomer (data collection), Science Observer (data validation), Telescope Operator (system control), Support Staff (maintenance), Developer (system development), Administrator (system management)

**Main Scenarios:**
- Queue-based observing execution
- Remote operations monitoring
- Instrument configuration changes
- System maintenance procedures
- Fault detection and notification
- Data acquisition and archiving

## Business Process
**Main Observing Process (8 steps):**
1. User submits observation program
2. Scheduler validates and queues program
3. Sequencer executes observation commands
4. Telescope and instruments configure
5. Data acquisition initiated
6. Quality assessment performed
7. Data archived to storage
8. Status reported to users

**Key Branches:**
- **Fault Recovery:** Detect fault → Notify operator → Attempt recovery → Log incident
- **Remote Operations:** Authenticate user → Establish connection → Mirror operations → Compress data transmission

## Domain Model
**Entities:**
- ObservationProgram (program_id: unique, target_coordinates: required)
- Instrument (instrument_id: unique, status: required, configuration: reference)
- Telescope (telescope_id: unique, position: required)
- DataAcquisition (acquisition_id: unique, timestamp: required, instrument_id: reference)
- User (user_id: unique, access_level: required)
- CommandQueue (command_id: unique, priority: required, status: required)
- SystemLog (log_id: unique, timestamp: required, severity: required)
- Archive (archive_id: unique, data_reference: required, metadata: required)

## Interfaces and Integrations
- **EPICS Control System** (bidirectional) - Real-time control interface using Channel Access protocol
- **Data Archive System** (outbound) - FITS format data transfer with complete header information
- **User Interface** (bidirectional) - X-windows based GUI with Tcl/Tk implementation
- **Remote Operations** (bidirectional) - Network transparent access with bandwidth adaptation
- **Instrument Control** (bidirectional) - Standardized hardware interfaces via VME/IOC systems
- **Database Systems** (bidirectional) - SYBASE relational database for configuration and logging

## Acceptance Criteria
**Given** an approved observation program **When** submitted to the scheduler **Then** it should be queued for execution within 2 seconds

**Given** a system fault condition **When** detected by monitoring systems **Then** appropriate notifications should be generated within 5 seconds

**Given** remote user connection **When** authenticated with valid credentials **Then** system access should be granted according to privilege level

## Non-functional Metrics
**Performance:** Command acceptance/rejection within 2 seconds; Status updates within 4 seconds at local stations
**Reliability:** Maximum 15 minutes downtime per night; 5-minute recovery from error conditions
**Security:** Multi-level access control; Network intrusion protection via firewalls
**Compliance:** POSIX-compliant system calls; FITS format data standards

## Milestones and Release Strategy
1. Core control system implementation
2. Basic observing mode functionality
3. Remote operations capability
4. Queue scheduling system
5. Full instrument integration
6. Commissioning and handover

## Risk List and Mitigation Strategies
- **Network bandwidth limitations** - Implement data compression and prioritization
- **Subsystem integration complexity** - Use standardized interfaces and virtual telescope model
- **Remote operations security** - Deploy firewall protection and access controls
- **Software version compatibility** - Implement strict configuration management
- **Hardware obsolescence** - Design for hardware independence and portability

## Undecided Issues and Responsible Parties
1. Detector data acquisition/storage standard (Not mentioned)
2. Data transfer link technology selection (Not mentioned)
3. Hardware specification details (Not mentioned)
4. Online software development environment standards (Not mentioned)
5. Supportability plan completion (Not mentioned)
6. Star catalog descriptions and interfaces (Not mentioned)