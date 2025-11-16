# Detailed Summary

## Background and Scope
The Dallas/Ft. Worth Regional Center-to-Center Communications Network (C2C) creates a standardized infrastructure for sharing traffic data and device control between Traffic Management Centers. Based on Texas Department of Transportation initiatives, it implements a common repository using ITS standards including Traffic Management Data Dictionary (TMDD). The system connects dissimilar traffic management systems through standardized interfaces while supporting extensibility to local, regional, and statewide levels. Non-goals include not implementing field-level device protocols directly.

## Role Matrix and Use Cases
- **Traffic Management Center Operator**: Monitors traffic conditions and controls field devices
- **Remote Agency User**: Accesses system via GUI applications without formal TMC
- **System Administrator**: Manages C2C infrastructure and configurations
- **Web Map User**: Views traffic conditions through web interface
- **Data Provider**: Supplies traffic data from connected systems
- **Main Scenarios**: Data collection and aggregation, device status monitoring, remote device control, incident reporting, web map display
- **Exception Scenarios**: Device communication failures, authentication failures, data format conversion errors

## Business Process
**Main Process (Data Collection & Distribution)**
1. Connected systems provide traffic data in native formats
2. Data converters transform to TMDD standard format
3. Data stored in common repository
4. Web map application retrieves aggregated data
5. Users access traffic information via web interface
6. Remote GUI applications submit device control requests
7. Control commands converted to system-specific formats
8. Commands executed on target field devices

**Key Branch (Device Control)**
- Trigger: Remote control request
- Authentication and authorization validation
- Command timeframe verification
- Command execution and status reporting

**Key Branch (Incident Management)**
- Trigger: Incident detection or user report
- Incident data entry and validation
- Distribution to connected systems
- Web map display and notification

## Domain Model
- **Roadway Network** (identifier: unique, name: required, links: reference, nodes: reference)
- **Traffic Link** (identifier: unique, roadway: required, direction: required, capacity: required)
- **Incident** (identifier: unique, location: required, status: required, severity: required)
- **Field Device** (identifier: unique, type: required, location: required, status: required)
- **Device Command** (device_id: reference, username: required, password: required, parameters: required)
- **Traffic Condition** (link_id: reference, timestamp: required, speed: required, volume: required)
- **User Account** (username: unique, password: required, permissions: required)
- **Network Configuration** (network_id: unique, agency: required, devices: reference)

## Interfaces and Integrations
- **Roadway Network Interface**: System-to-C2C, bidirectional, network topology data exchange
- **Traffic Conditions Interface**: System-to-C2C, bidirectional, real-time traffic measurements
- **Device Status Interface**: System-to-C2C, bidirectional, field device status monitoring
- **Device Control Interface**: C2C-to-System, bidirectional, remote device command/control
- **Web Map Interface**: C2C-to-User, output, graphical traffic display
- **Incident GUI**: User-to-C2C, input, incident data entry and management
- **Remote Control GUI**: User-to-C2C, bidirectional, device control from public networks

## Acceptance Criteria
**Data Collection Capability**
- Given multiple traffic management systems are connected
- When each system provides traffic data in native formats
- Then all data is converted to TMDD standard and stored in common repository

**Web Map Display**
- Given traffic data is available in repository
- When user accesses web map interface
- Then interstate and state highways display with color-coded speed conditions

**Remote Device Control**
- Given authenticated user with proper permissions
- When user submits device control command via Remote GUI
- Then command executes on target device and status returns to user

## Non-functional Metrics
- **Performance**: Support real-time data updates from multiple connected systems; Web map refresh within 30 seconds
- **Reliability**: 99% system availability during normal operations; Graceful degradation during partial system failures
- **Security**: User authentication for all control functions; Secure data transmission between centers
- **Compliance**: Conform to ITS TMDD standards; Follow Texas DOT requirements
- **Observability**: Comprehensive activity logging in test mode; System status monitoring capabilities

## Milestones and Release Strategy
1. Core C2C infrastructure implementation
2. Basic data collection and web map functionality
3. Device status monitoring for DMS, LCS, CCTV
4. Remote control capabilities for key device types
5. Additional device type support (ramp meters, HAR, traffic signals)
6. Full regional deployment with all connected systems

## Risk List and Mitigation Strategies
- **Data Format Incompatibility**: Use TMDD standards with configurable converters
- **Network Connectivity Issues**: Implement robust connection management and failover
- **Authentication Security**: Secure credential management and transmission
- **System Performance Degradation**: Scalable architecture with load monitoring
- **Device Control Conflicts**: Command timeframe validation and lock mechanisms
- **Data Consistency**: Regular synchronization and validation procedures
- **Configuration Management**: Centralized configuration with version control
- **Inter-agency Coordination**: Clear protocols and communication channels

## Undecided Issues and Responsible Parties
- Specific speed thresholds for color coding on web map (NCTCOG)
- Detailed command timeframe schedules per device type (TxDOT)
- Firewall and gateway configuration for public network access (Network Team)
- Specific TMDD version and implementation details (Standards Committee)
- Performance tuning parameters for production deployment (Operations Team)
- Backup and recovery procedures (System Administrators)
- User training and documentation requirements (Training Team)
- Long-term maintenance and support model (Management)