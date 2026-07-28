# Detailed Summary: EVLA Correlator Monitor & Control System

## Background and Scope
The EVLA Correlator Monitor & Control System (CMCS) serves as the critical interface between the WIDAR correlator hardware and the broader EVLA monitor & control infrastructure. Its primary functions are to translate configuration data from the EVLA M&C into hardware-specific commands, manage real-time monitoring and control data flows, ensure system health through autonomous recovery, and provide tools for testing and debugging. The system is designed as a master/slave network to isolate real-time hardware control from higher-level network operations. Non-goals include direct user data processing beyond basic auto-correlation display and handling ambiguous or invalid configuration data streams.

## Stakeholders Matrix and Use Cases
*   **Array Operator**: Monitors overall correlator status and error messages channeled through the EVLA M&C system.
*   **Engineers and Technicians**: Perform maintenance, diagnostics, and repairs using remote tools to inspect hardware and trace faults to specific modules.
*   **Software Developer**: Develops, troubleshoots, and maintains CMCS software, requiring remote system access for debugging.
*   **Web User (Authorized)**: Has restricted, read-only or limited access to specific system monitoring data.
*   **EVLA M&C System**: Provides configuration data and auxiliary inputs (e.g., delay models) and receives status and monitor data.
*   **Correlator Backend Data Processing System**: Receives specific data sets (e.g., auto-correlations, state counts) for post-processing.
*   **Correlator Hardware**: The physical hardware (station boards, baseline boards) controlled and monitored by the CMCS.

**Main Scenarios**: 1) Receive and translate a valid configuration from EVLA M&C. 2) Continuously monitor hardware health and status. 3) Output required data streams to the Backend system. 4) Detect a CMIB failure and attempt autonomous recovery. 5) An engineer remotely diagnoses a faulty hardware module. 6) An operator views filtered error messages.
**Exception Scenarios**: 1) Loss of network connection to EVLA M&C (system continues with cached parameters). 2) Unrecoverable MCCC failure triggers failover to the backup system.

## Business Process
**Main Process: Configure and Operate Correlator**
1.  **Trigger**: EVLA M&C sends a new observation configuration.
2.  MCCC receives and validates the configuration via the Virtual Correlator Interface (VCI).
3.  MCCC translates the configuration into hardware-specific control tables.
4.  MCCC distributes control tables and auxiliary data (e.g., delay models) to relevant CMIBs.
5.  CMIBs apply the configuration to their respective correlator hardware boards.
6.  CMIBs and MCCC continuously monitor hardware health and operational status.
7.  MCCC packages and outputs required monitor data (state counts, auto-correlations) to the Backend system.
8.  MCCC streams status and error messages to the EVLA M&C system.
**Output**: Configured and operating correlator, with data flowing to backend and status to M&C.

**Key Branch A: Hardware Fault Recovery**
1.  **Trigger**: A CMIB or its hardware watchdog detects a fault.
2.  Fault is reported to the MCCC, which attempts a remote reboot/restart of the CMIB.
3.  If recovery is successful, the CMIB autonomously reconfigures and resumes operation.
4.  If recovery fails, an alert is issued for manual repair.
**Key Branch B: MCCC Failover**
1.  **Trigger**: Primary MCCC suffers a non-recoverable failure (detected by CPCC or watchdog).
2.  CPCC or external intervention activates the backup MCCC system.
3.  Communications are rerouted to the backup MCCC.
4.  Backup MCCC, having maintained state, resumes control with minimal disruption.

## Domain Model
*   **Configuration**: (Unique ID, Source [EVLA M&C/VCI], Parameters [required], Validity Timestamp)
*   **Control Table**: (Table ID, Target Hardware ID [reference], Configuration Data [required], Generation Timestamp)
*   **CMIB (Correlator Monitor Interface Board)**: (Hardware ID [unique, from board], IP Address, Status, Associated Rack [reference])
*   **MCCC (Master Correlator Control Computer)**: (System ID [primary/backup], Network Interfaces, Operational Status)
*   **CPCC (Correlator Power Control Computer)**: (System ID, Power Bus Connections, Status)
*   **Monitor Data**: (Data ID, Type [e.g., auto-correlation, health], Source CMIB/MCCC [reference], Timestamp [required], Payload)
*   **Error/Status Message**: (Message ID, Severity, Source, Timestamp [required], Description, Acknowledgment Status)
*   **User**: (Username [unique], Access Level, Authentication Credentials)

## Interfaces and Integrations
1.  **EVLA M&C System** | **Inbound/Outbound** | **VCI & Status Stream**
    *   **Input**: Configuration data, auxiliary data (models, time codes).
    *   **Output**: System status, error messages, configuration echoes.
    *   **SLA**: Must accept CMCS output data rates; configuration data must be unambiguous.
2.  **Correlator Backend System** | **Outbound** | **Data Output Interface**
    *   **Input**: Requests for specific data sets/sample rates.
    *   **Output**: State counts, auto-correlation products, other processed data.
    *   **SLA**: Timely and robust delivery over a secondary virtual network.
3.  **Correlator Hardware (via CMIB)** | **Outbound/Inbound** | **Hardware Control & Monitoring**
    *   **Input**: Hardware control register writes, reboot commands.
    *   **Output**: Hardware register reads, operational status, board identifier.
    *   **SLA**: Real-time, deterministic response to hardware interrupts to prevent data loss.
4.  **CPCC** | **Bidirectional** | **Power Monitoring & MCCC Failover**
    *   **Input**: Power/health status signals, MCCC heartbeat.
    *   **Output**: Power control commands, MCCC failover trigger.
    *   **SLA**: Redundant serial link for failover communication during network failure.
5.  **CMCS Test Interface/GUI** | **Inbound** | **Testing & Debugging**
    *   **Input**: Direct commands, configuration for testing.
    *   **Output**: Full system traffic, debug information.
    *   **SLA**: Provides full system access for authorized users without disrupting operations.

## Acceptance Criteria
*   **Capability: Configuration Handling**
    *   Given a valid configuration is received from EVLA M&C, When the MCCC processes it via the VCI, Then corresponding hardware control tables are generated and sent to the appropriate CMIBs.
    *   Given the CMCS is operating, When network connectivity to EVLA M&C is lost, Then the system continues processing using the last known good parameters until queues are exhausted.
*   **Capability: Fault Monitoring and Recovery**
    *   Given a CMIB subsystem fails, When the MCCC detects the failure, Then it attempts a remote reboot and, if successful, reintegrates the module autonomously.
    *   Given the primary MCCC suffers a hard failure, When the CPCC or watchdog detects it, Then the backup MCCC is activated and control is transferred with minimal data interruption.
*   **Capability: Data Output**
    *   Given the Backend system requests auto-correlation products, When the correlator is operational, Then the MCCC packages and delivers the data stream at the requested rate over the designated network.

## Non-functional Metrics
*   **Performance**: Processors must meet all real-time data processing deadlines; System must respond to hardware interrupts deterministically.
*   **Reliability/Availability**: Software must run between maintenance windows without total restart; Hardware must support indefinite operation with no complete service loss except for total power failure.
*   **Security**: All access requires unique login (e.g., username/password); Administrator controls all user privileges and access blocks.
*   **Compliance**: Network interfaces shall comply with IEEE 802.3; CMIB form factor shall comply with PC104+ standards.
*   **Observability**: All system error/debug messages must be accessible at the MCCC layer; All inter-layer messages must have appropriate UTC/wall clock timestamps.

## Milestones and Release Strategy
1.  Finalize and approve hardware specifications (CMIB, MCCC, CPCC).
2.  Establish and test core network topology and isolation.
3.  Develop and integrate the Virtual Correlator Interface (VCI) software.
4.  Implement basic monitoring, control, and autonomous recovery for a single rack.
5.  Integrate with EVLA M&C system for end-to-end configuration testing.
6.  Deploy full-scale system, followed by operational readiness review.

## Risk List and Mitigation Strategies
1.  **Risk**: Unclear or invalid configuration data from EVLA M&C leading to hardware misconfiguration.
    *   **Mitigation**: Assume configuration is unambiguous and valid (as per assumption 2.5.1); implement rigorous validation in the VCI.
2.  **Risk**: Network congestion or failure disrupting real-time control or data output.
    *   **Mitigation**: Use physically isolated networks for control, data, and external comms; implement data spooling for temporary outages.
3.  **Risk**: Single point of failure in the MCCC causing total system outage.
    *   **Mitigation**: Implement a redundant, hot-swappable MCCC pair with state synchronization and automatic failover via CPCC.
4.  **Risk**: Inadequate processing power for future real-time requirements.
    *   **Mitigation**: Design for modular hardware scalability (Req. 3.7.1) and use COTS components for easier upgrades.
5.  **Risk**: Complex fault diagnosis leading to extended downtime.
    *   **Mitigation**: Provide comprehensive remote debugging tools and ensure all error messages are categorized and filterable at the MCCC.
6.  **Risk**: Security breaches from unauthorized access.
    *   **Mitigation**: Implement login authentication, encrypted passwords, and privilege-based access control managed by an administrator.
7.  **Risk**: Difficulty in maintaining or upgrading software due to poor documentation.
    *   **Mitigation**: Mandate well-documented code in familiar languages and adhere to readable coding practices (Req. 3.10.2).
8.  **Risk**: Prolonged power outage exceeding UPS capacity.
    *   **Mitigation**: Use UPS with communication to CMCS to coordinate a safe, system-wide shutdown before backup power is exhausted.

## Undecided Issues and Responsible Parties
1.  **Issue**: Specific actions for external systems to take upon a hard failure of the CPCC. **Responsible**: System Architects/Engineers.
2.  **Issue**: The exact mechanism (automatic vs. manual) for activating the backup MCCC upon primary failure. **Responsible**: Operations & Software Team.
3.  **Issue**: The acceptable minimum delay for the system to resume from standby idle mode. **Responsible**: Performance & Requirements Team.
4.  **Issue**: Definition of "minimal impact" for killing/restarting software processes during normal operations. **Responsible**: Software Development Team.
5.  **Issue**: Selection of the specific COTS operating system(s) for the CMIB and MCCC. **Responsible**: Software & Hardware Integration Team.
6.  **Issue**: Final protocol and physical medium for the Power Monitor/Control Bus between CPCC and hardware. **Responsible**: Hardware Engineers.
7.  **Issue**: Detailed categorization and filtering schema for system error and debug messages. **Responsible**: Software Development Team.
8.  **Issue**: The specific format and content of the "unique identification" for user logins. **Responsible**: Security & Software Team.