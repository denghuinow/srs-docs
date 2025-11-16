# System Overview

This system is designed for requirement extraction, aiming to accurately distill key requirements from various requirement documents in a concise and clear manner to facilitate efficient work. The Center-to-Center (C2C) Communications Network project for the Dallas/Ft. Worth Regional area is based on a Texas Department of Transportation (TxDOT) C2C project. It implements a repository for traffic data and provides a mechanism to exchange device control information between Traffic Management Centers (TMCs) using ITS Traffic Management Data Dictionary (TMDD) standards.

The C2C infrastructure interconnects several dissimilar traffic management systems through interfaces that communicate with existing systems in a "system specific" format, which is then converted to a standard format based on ITS standards. The infrastructure is created using a series of building blocks that allow the software to be utilized in a number of configurations by simply altering the configuration parameters.

Key system characteristics:
- Distributed architecture supporting multiple interconnected Traffic Management Centers
- Real-time data collection and dissemination capabilities
- Standards-based communication protocols for interoperability
- Extensible design allowing for future system enhancements
- Comprehensive security framework for data protection
- Robust error handling and system recovery mechanisms
- Support for both centralized and decentralized control architectures
- Modular design facilitating component reuse and replacement
- Platform independence enabling deployment on various hardware configurations
- Comprehensive logging and monitoring capabilities for system diagnostics

# Goals and Objectives

The C2C project has the following primary goals:
- Provide a common repository for traffic information for the DFW Metroplex
- Provide a World Wide Web based graphical map to display traffic conditions
- Enable agencies without formal TMCs to participate through a Windows application
- Support ITS center-to-center communications for command/control/status of various ITS field devices
- Utilize National ITS standards for implementation
- Provide an extensible software system for all local or regional partners

Additional objectives include:
- Facilitating regional coordination and information sharing among transportation agencies
- Improving traffic management efficiency through centralized data collection and analysis
- Enhancing public information dissemination through web-based interfaces
- Supporting emergency response coordination during critical events
- Enabling performance measurement and system optimization through data analytics
- Promoting standardization and interoperability across different traffic management systems

# Interface Requirements

The C2C system defines comprehensive interface requirements for various transportation devices:

## Roadway Network and Traffic Data
- Roadway network information including network identifier, name, links, and nodes
- Traffic conditions data with delay, travel time, volume, speed, density, and occupancy
- Incident data with location, description, status, affected lanes, classification, and severity
- Lane closure information with location, status, affected lanes, and timing
- Traffic data elements conform to ITS Traffic Management Data Dictionary (TMDD) standards
- Data exchange format based on DATEX/ASN.1 encoding rules for interoperability

## Dynamic Message Signs (DMS) and Lane Control Signals (LCS)
- DMS status information including location, geometry, status, and current message
- DMS control commands for remote centers to set messages and beacon status
- LCS status with location, geometry, capabilities, status, and current pattern
- LCS control commands for pattern control from remote centers
- DMS message length and character set limitations defined by TMDD specifications
- LCS pattern definitions include allowable combinations and timing sequences

## Closed Circuit Television (CCTV)
- CCTV status information including location, status, lock status, and current settings
- CCTV control requests for camera movement and positioning
- Video snapshot capabilities with JPEG format output
- CCTV switching commands between input and output channels

## Traffic Management Devices
- Ramp meter status and control with plan and cycle time management
- Highway Advisory Radio (HAR) status and control with message text and duration
- Traffic signal status including state, failure state, and plan information
- Traffic signal control commands for plan execution

## Environmental and Specialized Systems
- Environmental Sensor Station (ESS) data with readings and alarm status
- High Occupancy Vehicle (HOV) lane status and control
- Parking lot information with capacity and utilization data
- School zone status and control plans
- Railroad crossing status with train timing information
- Reversible lane status and direction control
- Dynamic lane assignment status and control

## Transit Systems
- Bus stop information with location, routes, and frequency
- Bus location data with schedule adherence and capacity
- Light/Commuter rail stop and location information
- Park and Ride lot status with capacity and utilization
- Vehicle priority information for signal preemption

## Network and Command Interfaces
- Network device status for all connected devices
- Command timeframe requests and responses for determining when centers accept commands
- Network status monitoring including connectivity, latency, and bandwidth utilization
- Command queue management for handling multiple concurrent device control requests
- Status update notifications for real-time system state changes
- Network error detection and recovery mechanisms
- Support for both wired and wireless communication infrastructures

# Functional Requirements

## Data Management
- Data collector designed to support TMDD data elements and message set information
- Data transmission using TMDD standard with DATEX/ASN message sets over TCP/IP
- TCP/IP connection management derived from TCP/IP transmission requirements
- Data validation and integrity checks for all incoming and outgoing messages
- Automatic data archiving for long-term storage and historical analysis
- Real-time data synchronization between redundant system components
- Data compression techniques for efficient network transmission
- Support for incremental data updates to minimize bandwidth usage

## Web Map Application
- Display of interstates and state highways with color-coded speed representations based on configurable speed values
- Incident display as icons with detailed information on click
- Tabular incident display with location, type, severity, and status
- Device visualization for DMS (current message), LCS (current signals), and CCTV (status) with location information
- Map user can alter magnification (zoom level) and pan in North, South, East or West directions
- Basemap data derived from the North Central Texas Council of Governments (NCTCOG) Geo-Data warehouse

## User Interfaces
- Incident GUI for entering incident and lane closure information without a Center
- Incident GUI allows input of location (latitude/longitude), description, status, affected lanes, detection time, response time, estimated time to clear queue, and queue length
- Incident GUI allows modification and deletion of previously entered incidents and lane closures
- Remote Control GUI for device command/control from remote centers via public networks
- Remote Control GUI executes as a local application on a PC and generates TMDD device control messages
- Remote Control GUI prompts for username and password when initiated
- Remote Control GUI allows selection of network identifier and devices (DMS, LCS, CCTV, Ramp Meter, HAR, Traffic Signal, HOV, School Zone, Reversible Lane, Dynamic Lane) for control
- For each device command/control status request sent by the Remote GUI, the status returned from the network identifier is displayed in a scrollable list
- User interface supports multiple language options for international deployments
- Graphical user interface with intuitive navigation and consistent design patterns
- Context-sensitive help system for user guidance and support
- Keyboard shortcuts for efficient user operations
- Customizable user preferences and interface layouts

# Design and Construction Standards

- Server execution in Microsoft Windows NT environment
- Implementation in C/C++ programming language
- Web interface using ESRI ARC Internet Map Server (ARC IMS)
- GUI applications using ESRI Map Objects
- DATEX/ASN runtime library availability for communicating systems
- System designed with modular architecture allowing individual components to be replaced or upgraded independently
- Database storage using industry-standard relational database management system
- Communication protocols implemented using standard TCP/IP stack
- System integration through well-defined APIs for third-party components
- Configuration files in XML format for easy deployment and customization
- Error messages and logs in standardized format for troubleshooting
- Backup procedures using industry-standard database backup mechanisms
- System deployment using automated installation scripts
- Code version control using industry-standard repository management
- Automated testing procedures for system validation and verification
- Documentation generation tools for maintaining up-to-date system documentation
- Compliance with accessibility standards for user interface components
- Support for internationalization and localization in user interfaces

# Operational Requirements

The C2C Project operates in two modes:
- Normal mode: Receives data from all connected systems and combines into a single data store
- Test mode: Performs normal operations with additional activity logging for development and testing

In normal operation, the system continuously polls connected systems for data updates at configurable intervals. The system maintains historical data for trend analysis and reporting purposes. All data exchanges between centers are logged for security and audit purposes.

In test mode, the system provides enhanced diagnostic capabilities including:
- Detailed message logging for all TMDD communications
- Performance metrics collection for system optimization
- Simulation capabilities for testing new configurations
- Debugging interfaces for troubleshooting connectivity issues
- Trace functionality for tracking data flow through system components

The system supports concurrent access by multiple users and centers, with appropriate access controls and authentication mechanisms. Error handling and recovery procedures are implemented to ensure system stability and data integrity.

System maintenance procedures:
- Automated backup scheduling with configurable frequency and retention policies
- Database maintenance routines including index optimization and statistics updates
- System health monitoring with proactive alerting for potential issues
- Software update deployment with rollback capabilities for failed updates
- Performance tuning recommendations based on historical usage patterns

System administration functions include:
- User account management with role-based access control
- Configuration management for network identifiers and device mappings
- Performance monitoring and system health checks
- Backup and recovery procedures for critical data
- Software update and patch management procedures
- System monitoring through SNMP-based network management protocols
- Automated alerting for system failures or performance degradation
- Remote diagnostics and troubleshooting capabilities
- Scheduled maintenance windows for system updates
- Database optimization and index management

Performance requirements:
- System response time for data queries shall not exceed 2 seconds under normal load conditions
- Maximum concurrent user connections supported: 100 simultaneous users
- Data update frequency from field devices: configurable between 30 seconds and 5 minutes
- Map rendering time for full display shall not exceed 3 seconds
- System uptime shall be maintained at 99.5% excluding scheduled maintenance periods

Fault tolerance and redundancy:
- Automatic failover mechanisms for critical system components
- Data replication across multiple database servers
- Network redundancy through multiple communication paths
- Graceful degradation of services during partial system failures
- Automatic restart procedures for failed system processes

Security requirements include:
- Encrypted communication channels for data transmission
- User authentication with strong password policies
- Audit trails for all system access and modifications
- Protection against unauthorized access to control functions
- Secure storage of sensitive configuration data
- Role-based access control for fine-grained permission management
- Secure session management with automatic timeout features
- Protection against common web application vulnerabilities
- Regular security updates and patch management procedures
- Intrusion detection and prevention mechanisms

System scalability features:
- Horizontal scaling through addition of network nodes
- Vertical scaling through hardware upgrades
- Dynamic resource allocation based on demand
- Load balancing across multiple system instances
- Support for geographically distributed deployments
- Automatic load distribution based on system performance metrics
- Support for cloud-based deployment options
- Elastic scaling capabilities for handling variable workloads

This requirement specification ensures a comprehensive, standards-based approach to regional traffic management and information sharing.
