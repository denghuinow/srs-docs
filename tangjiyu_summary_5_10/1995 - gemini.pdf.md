# Gemini 8-m Telescopes Control System - Software Requirements Specification

## System Overview
The Gemini 8-m Telescopes Control System software provides operational requirements for controlling the Gemini telescopes and instrumentation. The system supports multiple observing modes including interactive, queue-based, remote operations, and service observing.

## User Classes
- **Astronomer**: End user collecting science data with minimal direct system control
- **Science Observer**: On-site person monitoring data acquisition and validating data integrity
- **Telescope Operator**: On-site controller responsible for system integrity and accurate observations
- **Support Staff**: Maintenance personnel for hardware and software systems
- **Developer**: Designers, testers, and upgraders of subsystems
- **Administrator**: High-level functional control of the integrated system

## Operational Levels and Access Modes

### Operational Levels
- **Observing Level**: Normal operational mode for data collection
- **Maintenance Level**: Routine maintenance and diagnostic work (typically during daylight)
- **Test Level**: Installation/deinstallation of subsystems with full diagnostics

### Access Modes
- **Observing**: Simple and safe access for science data collection
- **Monitoring**: Read-only mode for observing system status
- **Operation**: Direct control of telescope and instruments (Telescope Operator access)
- **Planning**: Science planning with virtual telescope simulator
- **Testing**: Full direct control for subsystem testing
- **Administrative**: System utilization and scheduling inquiries only

## Observing Modes

### Interactive Observing
- Direct control through Observatory Control System (OCS)
- Visual user interface for viewing program changes
- Multiple station participation capability

### Queue-Based Observing
- Primary observation mode for efficient telescope use
- Fully automated observing programs with minimal human interaction
- Telescope simulator for program testing
- Flexible scheduling with interleaving of observing programs
- Dynamic queue reordering based on site conditions

### Remote Operations
- Remote observing, control, monitoring, and diagnostics
- Full operations capability from off-site locations
- Team observing with multiple observers at different sites
- Security mechanisms to restrict operations to specific remote sites
- Support for various bandwidth connections (ISDN, TCP/IP, Internet)

### Service Observing
- Gemini staff performs data collection on behalf of astronomers
- Automated observing programs executed by others
- Communication of special notes and instructions between astronomer and observer

## Functional Requirements

### Data Management
- **Control Information Flow**: Consistent command syntax across system with ACK/NAK protocol
- **Astronomical Data Flow**: Detector data storage using most effective technology methods
- **Video Information Flow**: Fast transmission of rough images (0.5 sec) and high-quality images (<20 sec)

### Asset Management
- Multi-telescope concept support (though not concurrent use as single facility)
- Multi-instrument context with parallel access to all mounted instruments
- Visitor instrument support with standardized interface subset
- Support for instruments as servers responding to upper-level commands

### User Management
- Role-based access control with privilege levels
- Dynamic resource allocation and assignment
- Multi-user context with simultaneous access from multiple locations
- Security protection against accidental interference

### System Operations
- Automatic procedures for startup and shutdown
- Dynamic reconfiguration of observing environment
- Concurrent operation support for multiple control nodes
- Built-in test (BIT) facilities for system verification

## Technical Requirements

### Performance
- Command acceptance/rejection within 2 seconds
- Status display update within 4 seconds at local stations
- Peak control information flow: 100 TPS with network bridging
- Data transfer rate: 20-40 Mbits/second on LAN

### Reliability and Availability
- Maximum 2% total system downtime due to failures (15 minutes per night or 1 night per month)
- Fault recovery and exception handling mechanisms
- Redundancy planning for critical subsystems
- Self-monitoring for safety and risk prevention

### Security
- Username/password authentication
- Access mode allocation system for resource protection
- Network security with firewall protection
- Interlock systems for hardware safety (7 levels from software limits to hard stops)

### Interfaces
- Standardized hardware interfaces with bus systems and interface cards
- EPICS-based software skeleton for real-time requirements
- FITS format for astronomical data transmission
- Support for commercial software packages (DBMS, image processing systems)

### Communications
- Ethernet IEEE 802.3 based control LAN
- FDDI backbone LAN for high bandwidth requirements
- TCP/IP protocol for WAN communications
- Time distribution systems for synchronization

## System Architecture

### Software Structure
- Modular design with strictly defined interfaces
- Table-driven applications using online databases
- EPICS (Experimental Physics and Industrial Control System) toolkit foundation
- Virtual telescope model for simulation and testing

### Hardware Environment
- Unix-based workstations (SUN SPARC) for development
- VxWorks real-time operating system for IOCs
- VME-based Input/Output Controllers (IOCs)
- Standardized VME cards and interface components

### Database Requirements
- Access times of 2-3 msec per access
- Asynchronous writes for concurrent operation
- Memory-based time-access critical information
- Consistent name-based access method
- Support for remote access and distributed data

## Maintenance and Support

### Maintenance Levels
- **Line Maintenance**: In-situ during observing sessions
- **Unit Replacement**: Repair by replacing computer systems or VME cards
- **Module Replacement**: At base facility during daytime
- **Module Repair**: At contractor/vendor site

### Testability
- Built-in test facilities for subsystem verification
- Three self-check levels: monitor, self-test, and system integration
- Continuous monitoring of active and inactive subsystems
- Error logging with time-stamping and traceability

### Life Cycle Aspects
- Structured development model with formal approval procedures
- Configuration and version management
- Cross-platform development environment
- Hardware and vendor independence

## Standards and Constraints

### Software Standards
- POSIX compliant Unix System V, Release 4
- X-windows (X11R5 or X11R6) for GUI systems
- Tcl/Tk as primary language for GUI development
- GNU software tool suite and CVS version control

### Development Methodology
- Ward/Mellor approach for real-time systems
- CASE tools for functional analysis
- Object-oriented design encouraged but not required
- Formal review and audit procedures

### Environmental Constraints
- High-altitude operation (Mauna Kea, Cerro Pachon)
- Humidity and temperature specifications compliance
- Reliability requirements for remote, unattended operation
- 30-day or longer programmed maintenance intervals

## Quality Attributes

### Simplicity
- Minimize complexity while meeting requirements
- User interfaces designed for ease of learning and use
- Clear separation of concerns in system architecture

### Expandability
- Modular design for easy extension and upgrades
- Technology evolution accommodation over 5-10 year lifecycle
- Standard interfaces for new instrument integration

### Maintainability
- Version control for all software components
- Automated consistency checking at boot time
- Table-driven software to avoid unnecessary compilations
- Detailed documentation and change logs

### Human Engineering
- Minimize stress effects and fatigue
- Feedback on operation tasks
- Appropriate procedures and training support
- Team interaction and organizational behavior considerations
