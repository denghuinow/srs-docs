# Detailed Summary

## Background and Scope
The EVLA Correlator Monitor & Control System (CMCS) provides the physical link between WIDAR Correlator hardware and the EVLA monitor & control system, serving as the primary interface for configuration, operation, and servicing. Primary functions include receiving configuration data from EVLA M&C and translating it to hardware configuration, processing dynamic control/monitor data, monitoring subsystem health with autonomous recovery, and providing real-time data processing tools. Non-goals include direct astronomical data processing and end-user scientific analysis interfaces.

## Role Matrix and Use Cases
- **Array Operator**: Monitors system status and error messages through M&C interface
- **Engineers/Technicians**: Performs maintenance, debugging, and hardware diagnostics via remote tools
- **Software Developer**: Develops/troubleshoots system software with remote access capabilities
- **Administrator**: Has unrestricted system access for user management and security controls
- **Web User**: Limited authorized access to restricted system components
- **EVLA M&C System**: External system providing configuration data and receiving monitor data

## Business Process
**Main Process - Correlator Configuration & Operation (8 steps):**
1. Receive configuration from EVLA M&C system
2. Translate configuration via Virtual Correlator Interface (VCI)
3. Distribute hardware configuration tables to CMIB subsystems
4. Monitor hardware status and health metrics
5. Process real-time control data updates
6. Output monitor data to backend and archive systems
7. Continuously validate system operation
8. Handle graceful shutdown when requested

**Key Branch - Hardware Failure Recovery (4 steps):**
- Trigger: CMIB subsystem failure detection
- Detect non-responsive hardware component
- Issue alert to maintenance personnel
- Attempt automatic reboot and reconfiguration
- Restore component to operational state

## Domain Model
- **MCCC** (Master Correlator Control Computer): hostname (unique), network_interfaces (required), system_state (required)
- **CMIB** (Correlator Monitor Interface Board): board_id (unique/required), ip_address (unique), hardware_status (required), location (required)
- **CPCC** (Correlator Power Control Computer): system_id (unique), power_status (required), temperature_readings (required)
- **Configuration**: config_id (unique), hardware_mapping (required), validity_check (required)
- **MonitorData**: timestamp (required), data_type (required), values (required), source (reference)
- **UserAccount**: username (unique/required), access_level (required), login_history (required)
- **ErrorLog**: error_id (unique), timestamp (required), severity (required), component (reference)
- **HardwareComponent**: component_id (unique), type (required), status (required), location (required)

## Interfaces and Integrations
- **EVLA M&C System** (Inbound): Configuration data reception, control commands; Input: Observation parameters, system commands; Output: Configuration acknowledgments; SLA: Real-time response required
- **Backend Data Processing** (Outbound): Monitor data streaming; Input: Data format requests; Output: State counts, auto-correlations; SLA: Timely delivery with buffering
- **Correlator Hardware** (Bidirectional): Hardware control/monitoring; Input: Configuration tables; Output: Hardware status, error signals; SLA: Deterministic response times
- **Power Monitoring System** (Inbound): Environmental monitoring; Input: Power/temperature data; Output: Alert notifications; SLA: Continuous monitoring
- **Test Interface** (Bidirectional): Debugging access; Input: Test commands; Output: System state information; SLA: On-demand availability

## Acceptance Criteria
**Configuration Capability:**
- Given a valid configuration from EVLA M&C, When processed by VCI, Then correlator hardware should be properly configured within specified timeframe
- Given an invalid configuration request, When validation fails, Then system should reject configuration and report specific errors

**Monitoring Capability:**
- Given operational correlator hardware, When monitor data is requested, Then system should provide complete status information with proper timestamps
- Given a hardware failure condition, When detected by monitoring system, Then appropriate alerts should be generated and recovery initiated

## Non-functional Metrics
- **Performance**: Deterministic response to hardware interrupts; Meet all data processing deadlines
- **Reliability**: Continuous operation between maintenance windows; 99%+ availability target
- **Security**: Encrypted authentication; Role-based access control
- **Compliance**: IEEE 802.3 network standards; RFI specifications for shielded room
- **Observability**: Comprehensive error logging; Remote diagnostic capabilities

## Milestones and Release Strategy
1. CMIB hardware specification and prototyping
2. MCCC software framework development
3. VCI interface implementation
4. Integration testing with correlator hardware
5. Security and access control implementation
6. Production deployment and operations handover

## Risk List and Mitigation Strategies
- **Network Failure**: Redundant communication paths and network isolation
- **Hardware Component Failure**: Hot-swappable modules with automatic detection
- **Software Hangs**: Watchdog timers with automatic reboot capabilities
- **Power Outages**: UPS systems with graceful shutdown coordination
- **Security Breaches**: Multi-layer authentication and access logging
- **Configuration Errors**: Validation checks and rollback capabilities
- **Performance Bottlenecks**: Modular design allowing component upgrades
- **Maintenance Complexity**: Comprehensive documentation and remote access tools

## Undecided Issues and Responsible Parties
- Automatic vs manual MCCC failover activation (System Architects)
- Specific CPCC failure response procedures (Hardware Team)
- Exact data rate capabilities for output streams (Performance Team)
- Final RFI compliance testing methodology (Compliance Team)
- Detailed UPS capacity and runtime specifications (Facilities Team)
- Complete hot-swap implementation details (Hardware Team)
- Final user privilege granularity (Security Team)
- Backup restoration procedures (Operations Team)