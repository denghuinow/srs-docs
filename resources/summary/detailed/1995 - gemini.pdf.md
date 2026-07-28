# Detailed Summary: Gemini 8-m Telescopes Control System Software Requirements

## Background and Scope
This document defines the operational requirements for the Gemini Control System software, guiding the development of controls and data acquisition systems for the Gemini 8-m Telescopes. It establishes general criteria and specific functional requirements for software and controls design, oriented toward developers rather than end-users. The scope includes non-commercial software developed for telescope and instrument control, interfaces to commercial packages, and external software integration. Non-goals include detailed field-level implementation specifics and the development of commercial or public-domain software packages themselves.

## Stakeholders Matrix and Use Cases
*   **Astronomer**: The end-user who proposes science programs and may interact remotely; requires a simple, safe interface for data collection and quality assessment, with no direct telescope control privileges.
*   **Science Observer**: On-site personnel responsible for monitoring data acquisition and validating data integrity for the astronomer, using observing and monitoring access modes.
*   **Telescope Operator**: On-site controller responsible for telescope and instrument integrity during observations, with privileges for direct control, monitoring, operation, and testing.
*   **Support Personnel**: On-site or near-site staff responsible for hardware and software maintenance, installation, and configuration changes, requiring full monitoring, operation, and testing access.
*   **Developer**: Personnel responsible for designing, testing, configuring, and upgrading subsystems, requiring full monitoring and testing access during maintenance and test levels.
*   **Administrator**: Personnel responsible for high-level functional control, scheduling changes, and system modifications, with access for monitoring and administrative inquiries only.

**Main Scenarios**: 1) Queue-based observing program execution via sequencer. 2) Interactive observing with OCS mediation. 3) Remote monitoring/eavesdropping. 4) Service observing by Gemini staff. 5) Telescope/instrument start-up and shutdown procedures. 6) System reconfiguration due to subsystem failure. 7) Maintenance and diagnostic testing. 8) Science program planning using the virtual telescope simulator.
**Exception Scenarios**: 1) Fault detection and notification. 2) Recovery from serious errors with degraded performance. 3) Manual intervention due to fatal errors. 4) Dynamic reallocation of resources via Access Mode Allocation to prevent deadlock.

## Business Process
**Main Process: Queue-Based Observing Execution**
1.  **Trigger**: Scheduler dispatches a pre-programmed Science Program to the Sequencer based on site conditions and priority rules.
2.  Sequencer interprets program and sends validated commands to Observatory Control System (OCS).
3.  OCS routes commands to appropriate subsystems (Telescope Control Software, Instrument Control Software).
4.  Subsystems execute commands (e.g., slewing, configuring instrument, starting exposure).
5.  Detector data is acquired, pre-processed if needed, and stored initially within IOCs.
6.  Data is transferred to Gemini system disks for quick-look assessment.
7.  Data is automatically archived in FITS format with full header information.
8.  Sequencer proceeds to next observation in queue or awaits interactive input.

**Key Branch A: Interactive Observing**
1.  **Trigger/Input**: Observer submits command via User Interface to OCS queue.
2.  OCS validates command and forwards to Sequencer.
3.  Sequencer executes command immediately (if in "pass-through" mode) or places in queue.
4.  Execution and data flow continue as main process steps 4-7.

**Key Branch B: Fault Recovery**
1.  **Trigger**: Subsystem reports a serious error or alarm.
2.  OCS logs error and notifies Telescope Operator.
3.  Operator assesses and may initiate reconfiguration (e.g., switch to backup instrument).
4.  System resumes observing with degraded capability if possible; goal is recovery within 5 minutes.

## Domain Model
*   **Science Program** (required): A formal, executable description of an observer's plan. Fields: Program_ID (unique), Astronomer_ID (reference), Priority, Target_List, Instrument_Configurations, Observing_Sequence.
*   **Observation** (required): An instance of data collection. Fields: Obs_ID (unique), Timestamp, Science_Program_ID (reference), Instrument_ID (reference), Exposure_Parameters, Data_Quality_Flags.
*   **Subsystem** (required): A controllable component (e.g., TCS, ICS). Fields: Subsystem_ID (unique), Status (e.g., RUNNING, MAINTENANCE), Configuration_Version, Health_Metrics.
*   **User** (required): An entity interacting with the system. Fields: User_ID (unique), Role (reference to stakeholder class), Access_Mode, Assigned_Privileges.
*   **Command** (required): An instruction issued to the system. Fields: Command_ID (unique, time-stamped), Source, Target (subsystem/channel/broadcast), Opcode, Parameter_Set.
*   **Data Product** (required): Acquired scientific or engineering data. Fields: Data_ID (unique), Observation_ID (reference), Format (e.g., FITS), Storage_Location, Compression_Flag.
*   **Archive Record** (required): Entry in the long-term storage system. Fields: Archive_ID (unique), Data_ID (reference), Ingestion_Date, Proprietary_Period.
*   **Engineering Log** (required): Record of system status and events. Fields: Log_ID (unique), Subsystem_ID (reference), Timestamp, Parameter_Name, Value, Log_Level (e.g., WARNING).

## Interfaces and Integrations
*   **User Interface (GUI/CLUI)**
    *   **System**: Portable User Interface Toolkit (e.g., Tcl/Tk on X11).
    *   **Direction**: Bidirectional (User ↔ OCS).
    *   **Theme**: Homogeneous "look and feel" across subsystems, reflecting access mode.
    *   **Input**: Observing commands, parameter changes.
    *   **Output**: Status displays, quick-look data, alerts.
    *   **SLA**: Command acceptance/rejection within 2 sec; status updates within 4 sec locally.
*   **EPICS Channel Access**
    *   **System**: EPICS Toolkit.
    *   **Direction**: Bidirectional (OPI/IOC ↔ IOC).
    *   **Theme**: Network-transparent access to IOC databases for control and monitoring.
    *   **Input**: Gets/Puts of process variables, monitor establishment.
    *   **Output**: Process variable values, alarm notifications.
    *   **SLA**: Handshaking within 100-200 msec; supports peak control load of ~100 TPS.
*   **Archive System (e.g., STARCAT)**
    *   **System**: External Archiving Software.
    *   **Direction**: Outbound (Gemini → Archive).
    *   **Theme**: Automatic storage of science data in FITS format.
    *   **Input**: Completed data products with headers.
    *   **Output**: Archive confirmation, on-line access to non-proprietary data.
    *   **SLA**: Data archived during observing; 7-day on-site interactive data retention.
*   **Quick-Look Analysis (e.g., PV-Wave/IDL)**
    *   **System**: Supported Data Analysis Package.
    *   **Direction**: Inbound (Gemini Data → Analysis).
    *   **Theme**: Synchronous data quality assessment.
    *   **Input**: Preprocessed or raw data from system disks.
    *   **Output**: Quality metrics (S/N, image quality) for observer feedback.
    *   **SLA**: Analysis concurrent with acquisition to inform next observation.
*   **Star Catalogs**
    *   **System**: External Astronomical Databases.
    *   **Direction**: Inbound (Catalog → Gemini).
    *   **Theme**: On-line access for guide/standard star selection.
    *   **Input**: Query (position, magnitude).
    *   **Output**: List of candidate stars.
    *   **SLA**: Response for planning and real-time acquisition.
*   **Time Reference System**
    *   **System**: Site Time Distribution Hardware.
    *   **Direction**: Inbound (Time Source → Gemini IOCs).
    *   **Theme**: Synchronization of subsystem clocks.
    *   **Input**: IRIG-B time signals.
    *   **Output**: Synchronized timestamps on commands and data.
    *   **SLA**: Accuracy as defined for control and data correlation.
*   **Visitor Instrument Interface**
    *   **System**: Visitor-Provided Control System.
    *   **Direction**: Bidirectional (Gemini OCS ↔ Visitor ICS).
    *   **Theme**: Standardized subset of Gemini instrument interface for basic support.
    *   **Input**: Status requests, preprogrammed sequences, telescope offsets.
    *   **Output**: Instrument status, acknowledgment.
    *   **SLA**: Stable, long-lived interface; coordinated motions not standardly supported.
*   **Wide Area Network (WAN)**
    *   **System**: Communication Links to Remote Facilities.
    *   **Direction**: Bidirectional.
    *   **Theme**: Transparent remote operations (observing, monitoring, diagnostics).
    *   **Input/Output**: Compressed video, commands, status, data.
    *   **SLA**: Performance degrades with bandwidth; security via firewalls/gateways.

## Acceptance Criteria
*   **Capability: Queue Scheduling & Execution**
    *   Given a validated Science Program in the queue, when site conditions match its requirements, then the Scheduler shall dispatch it to the Sequencer for execution.
    *   Given an executing observation, when a higher-priority program becomes feasible, then the Scheduler shall be able to preempt and resequence the queue according to observatory rules.
*   **Capability: Remote Monitoring**
    *   Given an active observing session, when a remote user with monitoring privileges connects, then they shall be able to view selected status and data without impacting the observation.
    *   Given a remote monitoring session, when the local user interface updates, then the remote display shall reflect the change within a time limit defined by link bandwidth.
*   **Capability: Fault Tolerance**
    *   Given a non-critical subsystem failure, when the error is detected, then the system shall reconfigure to continue observing with degraded performance and notify the operator.
    *   Given a fatal error in a subsystem, when recovery is not possible, then the system shall move to a safe state and log sufficient information to diagnose the cause.
*   **Capability: Multi-Instrument Operation**
    *   Given multiple mounted instruments with one active, when calibration commands are sent to an inactive instrument, then they shall execute without impacting the active instrument's data acquisition.

## Non-Functional Metrics
*   **Performance**: Peak control information load of 100 transactions per second (TPS). Detector readout times from 0.1 sec (focusing) to 2-3 minutes (full mosaic).
*   **Reliability/Availability**: System downtime goal of ≤1% (≤1 night/month). Recovery/reconfiguration goal within 5 minutes of error onset.
*   **Security**: Protection via Access Mode Allocation and network firewalls. Safety via hierarchy of software limits, soft/hard limit switches, and independent hardware interlocks.
*   **Compliance**: Adherence to POSIX for OS calls, use of FITS format for data archiving and transport.
*   **Observability**: All commands and system events logged with timestamps to enable full observation reconstruction. Engineering data loggable at up to 200 Hz.

## Milestones and Release Strategy
1.  Development of core Observatory Control System (OCS) and Sequencer with "pass-through" command execution.
2.  Integration of Telescope Control Software (TCS) and first Instrument Control Software (ICS) using EPICS/IOC standard.
3.  Support for basic Interactive Observing mode from on-site control room.
4.  Implementation of Queue-Based Observing and Science Program preparation environment.
5.  Enablement of Remote Operations (monitoring, then observing) for base facilities.
6.  Development and integration of advanced Scheduler for Flexible Scheduling (may be a future phase).

## Risk List and Mitigation Strategies
1.  **Risk**: Complexity of full queue-based and flexible scheduling software may exceed estimates.
    *   **Mitigation**: Implement basic sequencer first; design for future scheduler integration; consider phased delivery.
2.  **Risk**: Bandwidth limitations for remote operations degrade functionality below useful levels.
    *   **Mitigation**: Design software to be bandwidth-aware, using data compression; define minimum acceptable link specifications.
3.  **Risk**: Integrating diverse visitor instruments via a stable, minimal interface proves insufficient for user needs.
    *   **Mitigation**: Clearly define and publish the standard interface subset; offer collaborative support for enhanced integration on a case-by-case basis.
4.  **Risk**: Single points of failure in network or critical IOCs cause extended downtime.
    *   **Mitigation**: Design network with redundancy (e.g., double loops); establish swift hardware replacement procedures; maintain spares for critical components.
5.  **Risk**: Evolution of commercial software (OS, EPICS) or hardware standards creates long-term maintenance burdens.
    *   **Mitigation**: Use portable, standards-based code; isolate hardware dependencies in driver layers; participate in EPICS community for influence.
6.  **Risk**: Insufficient system monitoring leads to undetected failures impacting data quality.
    *   **Mitigation**: Implement mandatory built-in test (BIT) and health monitoring in all subsystems; set clear testability goals (e.g., 90% fault detection before impact).
7.  **Risk**: Security breaches via WAN connections compromise system integrity or data.
    *   **Mitigation**: Implement robust network gateways/firewalls; use rigorous authentication and privilege management; isolate critical control networks.
8.  **Risk**: Inadequate simulator for virtual telescope hampers planning and testing.
    *   **Mitigation**: Require simulation modules for all subsystems as part of delivery; integrate simulators early in development cycle.

## Undecided Issues and Responsible Parties
1.  Definition of a G8MT standard for acquisition and storage of detector data. (Responsible: Data Flow Working Group)
2.  Link chosen to transfer data from detectors. (Responsible: Hardware/Network Team)
3.  Desirable hardware specification for target IOCs and workstations. (Responsible: Systems Engineering)
4.  G8MT standards for online software and development environment details. (Responsible: Software Standards Committee)
5.  Finalized supportability plan detailing maintenance levels and resources. (Responsible: Supportability Planning Team)
6.  Descriptions and access protocols for star catalogs. (Responsible: Archive/Science Operations Team)
7.  Detailed rules and algorithms for the expert scheduling software. (Responsible: Science Operations & Software Development)
8.  Specific timeout values and retry protocols for all command interactions. (Responsible: OCS & ICS Development Teams)