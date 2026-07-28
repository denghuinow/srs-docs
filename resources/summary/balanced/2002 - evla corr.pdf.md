# Balanced Summary: EVLA Correlator Monitor & Control System

## Goals and Scope
The EVLA Correlator Monitor & Control System (CMCS) provides the primary interface between the WIDAR Correlator hardware and the EVLA monitor & control system, enabling configuration, operation, and servicing. Its core functions include translating configuration data from EVLA M&C into hardware settings, processing dynamic control and monitor data, monitoring system health for autonomous recovery, and providing real-time data processing tools. The system is designed as a modular, redundant master/slave network to isolate correlator hardware from the broader EVLA environment.

## Stakeholders and User Stories
*   **Array Operator**: Monitors overall array status and receives error messages through the EVLA M&C system.
*   **Engineers and Technicians**: Perform maintenance, diagnostics, and repairs using remote tools to inspect hardware and trace faults.
*   **Software Developer**: Develops, troubleshoots, and maintains system software, requiring remote access for debugging.
*   **Web User**: A limited set of authorized individuals granted restricted access to specific system parts.
*   **Administrator**: Has unrestricted access to all system aspects for management, security, and user privilege control.

**User Stories:**
1.  As an **Array Operator**, I want to receive clear status and error messages through the M&C system so that I can monitor the overall health of the correlator during observations.
2.  As an **Engineer**, I want remote access to inspect individual hardware modules and trace faults so that I can perform rapid diagnosis and repair.
3.  As a **Software Developer**, I want remote access to system logs and debugging tools so that I can troubleshoot software issues outside of normal working hours.
4.  As an **Administrator**, I want to manage user access privileges and system-wide settings so that I can ensure security and proper system operation.
5.  As a **Technician**, I want tools to monitor power, temperature, and hardware status so that I can perform preventive maintenance and verify repairs.
6.  As a **Web User**, I want controlled access to specific monitoring data so that I can view system status without full operational privileges.

## Key Processes
1.  **Configuration Reception & Translation (Trigger: EVLA M&C command)**: The MCCC receives configuration data from the EVLA M&C system and translates it into hardware-specific configuration tables via the Virtual Correlator Interface (VCI).
2.  **Hardware Control & Monitoring (Trigger: Periodic schedule or event)**: Slave CMIBs execute control commands and collect monitor data (e.g., autocorrelations, state counts) from the correlator hardware they manage.
3.  **Data Distribution (Trigger: Data availability)**: Processed monitor and control data is output to backend processing and the EVLA M&C system over dedicated network interfaces.
4.  **Auxiliary Data Ingestion (Trigger: External data feed)**: The system accepts and packages external data feeds (e.g., delay models, time standards) for delivery to the correlator hardware.
5.  **Fault Detection & Recovery (Trigger: System watchdog or health check)**: The system autonomously detects hardware/software faults, attempts recovery (e.g., rebooting a CMIB), and escalates alerts if unsuccessful.
6.  **System Health Monitoring (Trigger: Continuous operation)**: Watchdog processes and the CPCC monitor the health of all CMCS computers (MCCC, CPCC, CMIBs) to ensure high availability.
7.  **User Access & Control (Trigger: User login/request)**: Authorized users interact with the system through the VCI or test GUI for configuration, monitoring, and debugging.

## Domain Data Elements
*   **Configuration Table**: (Key: Config_ID). Fields: Target_Hardware, Parameter_Set, Validity_Time, Translation_Status.
*   **Monitor Data Packet**: (Key: Packet_ID). Fields: Source_CMIB, Timestamp_UTC, Data_Type (e.g., autocorrelation, state count), Value, Health_Status.
*   **Hardware Module**: (Key: Hardware_ID). Fields: IP_Address, Board_Type, Operational_Status, Location (Rack/Board), Last_Test_Result.
*   **System Event / Error Log**: (Key: Event_ID). Fields: Timestamp, Severity, Source_Component, Description, Resolution_Action.
*   **User Account**: (Key: Username). Fields: Password_Hash, Access_Level, Privilege_Set, Last_Login, Contact_Info.
*   **Control Command**: (Key: Command_ID). Fields: Issuer, Destination, Command_Type, Parameters, Execution_Time.

## Non-Functional Requirements
1.  **Reliability/Availability**: The system must be self-monitoring and capable of automatic recovery from processor failures, OS crashes, and communication disruptions to minimize astronomical data loss.
2.  **Performance**: All CMCS processors must meet real-time deadlines for hardware control and data processing to prevent data corruption or overflow.
3.  **Security**: All access requires unique user authentication (e.g., encrypted login), with privileges granularly controlled by an administrator.
4.  **Serviceability/Maintainability**: All hardware must be readily accessible for repair, and all software must be debuggable, killable, and restartable with minimal operational impact.
5.  **Scalability**: Hardware and software must be modular and expandable to meet future data and processing demands transparently to existing interfaces.
6.  **Documentation**: Hardware specifications and software code must be well-documented, readable, and written in familiar languages.

## Milestones and External Dependencies
1.  Finalization of the Virtual Correlator Interface (VCI) specification and integration points with the EVLA M&C system.
2.  Completion of CMIB hardware design conforming to PC104+ standards and correlator carrier board interfaces.
3.  Establishment of the redundant network and power control infrastructure (CPCC, UPS, switches).
4.  Availability of external data feeds (delay models, time codes, phase corrections) from the EVLA M&C or dedicated servers.
5.  Validation that backend and archive systems can accept the CMCS output data rates and formats.

## Risks and Mitigation Strategies
1.  **Risk**: Single point of failure in the master MCCC leading to total correlator control loss.
    *   **Mitigation**: Implement a hot-swappable, redundant MCCC pair with automatic failover coordinated by the CPCC.
2.  **Risk**: Network congestion or failure disrupting real-time control data to hardware.
    *   **Mitigation**: Use physically separate, isolated networks for control, monitoring, and external communication; implement data spooling for temporary outages.
3.  **Risk**: Unauthorized access or malicious interference compromising correlator operations.
    *   **Mitigation**: Employ robust authentication, encryption, network routers/firewalls, and detailed activity logging.
4.  **Risk**: Difficulty in diagnosing faults due to system complexity, leading to extended downtime.
    *   **Mitigation**: Design comprehensive remote diagnostic tools, clear hierarchical error messaging, and ensure hardware modules have visual health indicators (LEDs).
5.  **Risk**: Inability to meet real-time processing deadlines as correlator capabilities expand.
    *   **Mitigation**: Design with modular, scalable hardware and software from the outset, allowing for incremental performance upgrades.

## Undecided Issues
1.  The specific mechanism and authority (automatic vs. human intervention) for activating the backup MCCC after a primary failure.
2.  The exact actions to be taken by external systems in response to a hard failure of the CPCC.
3.  The final specification for the power monitor/control bus connecting the CPCC to hardware racks.
4.  The detailed format and protocol for the "unambiguous" configuration data stream from EVLA M&C.
5.  The specific "minimal delay" tolerance for the system resuming operations from a standby idle mode.
6.  The choice of operating system(s) for the CMIB and MCCC layers that best balances real-time performance, support, and development familiarity.