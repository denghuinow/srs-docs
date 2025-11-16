# EVLA Correlator Monitor & Control System Requirements Specification

## 1. Introduction

### 1.1 Purpose
This document provides a complete and accurate list of requirements for the EVLA Correlator Monitor & Control System. The primary audience includes project leaders, system designers and developers, and end users.

### 1.2 Scope
The Correlator Monitor & Control System provides the physical link between the WIDAR Correlator hardware and the EVLA monitor & control system. It is the primary interface by which the correlator is configured, operated, and serviced.

Primary functions:
- Receive configuration information from the EVLA M&C system and translate this info into a physical correlator hardware configuration
- Process and transfer dynamic control data and monitor data
- Monitor Correlator and correlator subsystem health and take corrective action autonomously
- Perform limited amounts of real-time data processing and probing
- Allow for easy system access to aid testing and debugging

## 2. Overall Description

### 2.1 Product Perspective
The EVLA Correlator Monitor and Control System is responsible for correlator configuration, real-time monitor/control, and hardware testing/servicing. The CMCS exists as an integrated part of the overall EVLA Monitor and Control Structure.

The CMCS is designed as a Master/Slave network with one computer system coordinating the activities of multiple "intelligent" hardware control processors. The Master handles the bulk of the monitor/control interface with the outside world whereas the slaves are only concerned with the correlator hardware systems under their direct control.

### 2.2 Product Functionality

#### 2.2.1 Monitoring
- Provide EVLA system wide access to all correlator system states
- Present information on a time synchronous basis as required by other systems
- Provide fully observable system with limits only imposed by hardware, bandwidth, and/or security restrictions
- Provide error and status messages in a concise time/location referenced format

#### 2.2.2 Control
- Receive correlator configurations and control instructions from the EVLA M&C system
- Translate requests into specific goal-oriented hardware configuration tables
- Provide human GUI interface for configuration through the Virtual Correlator Interface (VCI)

#### 2.2.3 Data Output
- Provide specific data sets required by the Backend Data Processing System in a timely and robust fashion
- Spool ancillary monitor data such that temporary loss of network communication will not result in loss of monitor data
- Allow full control of data sample rates and contents via either the EVLA M&C or Backend processing controller

#### 2.2.4 Data Input
- Accept external data feeds for models, time standards, fiber-link phase corrections and other required data
- Package data with control data delivered to the correlator hardware

#### 2.2.5 Recovery
- Attempt recovery from failure or hot-swapped hardware devices
- Issue alert notices for non-recoverable CMIB subsystem failures
- Automatically restart and reconfigure failed subsystems
- Monitor MCCC health with automatic activation of backup MCCC system
- Maintain full CMCS state information in both primary and secondary MCCC systems
- Monitor CPCC health through watchdog processes

### 2.3 User Characteristics
All use of the Correlator Monitor and Control System is through the VCI or MCCC. Software tools are provided to assist users at all access levels.

#### 2.3.1 Array Operator
Primary contact with array operations is via status and error messages channeled through the Monitor and Control System.

#### 2.3.2 Engineers and Technicians
Responsible for corrective and preventive maintenance, performance tests, and upgrades. Need tools to inspect and monitor individual CMIB layer devices remotely and fault trace to specific hot-swappable subsystems.

#### 2.3.3 Software Developer
Require remote access to the system for troubleshooting away from the EVLA and during non-working hours.

#### 2.3.4 Web User
A few authorized individuals may be allowed access to restricted parts of the system.

### 2.4 Constraints

#### 2.4.1 Criticality of the Application
The Correlator Monitor and Control is a critical component in the Astronomical data path. If unavailable, incoming astronomical data will be lost.

#### 2.4.2 Computer Hardware Limitations
Reliability and availability depend on the stability of the CMCS network and control computers. Functionality needs to be modularized for easy fault detection and repair.

#### 2.4.3 Computer Software Limitations
Ease of use and flexibility are rooted in the CMCS software. Full access is required with high level of data integration for a logical and coherent interface.

### 2.5 Assumptions

#### 2.5.1 Configuration Data Stream
Configuration data is unambiguous and results in a convergent hardware configuration.

#### 2.5.2 Auxiliary Data
All auxiliary data needed for real-time update of correlator parameters will be provided by the EVLA M&C system or dedicated servers.

#### 2.5.3 Outgoing Data Stream
Backend data processing and EVLA M&C systems are capable of accepting output data rates generated by the CMCS.

## 3. Specific Requirements

### 3.1 Communication Network Interface Requirements

#### 3.1.1 Correlator CMIB, MCCC, CPCC Interface
- Interface between CMIB, MCCC, and CPCC shall be Ethernet (IEEE 802.3 compliant) of 100 Mbits/sec or better
- Network topology shall be transformer coupled copper twisted pair unless other materials are required
- Network switches shall be employed to distribute traffic within a correlator rack
- MCCC-CMIB, MCCC-CPCC, and MCCC-EVLA M&C networks shall be on separate physical interfaces
- Redundant communication path (serial RS-232c or equivalent) between MCCC and CPCC for remote reboot

#### 3.1.2 MCCC to EVLA M&C Interface
- Interface between MCCC and external networks shall be Ethernet (IEEE 802.3 compliant) of 100 Mbits/sec or better
- Pathways penetrating the correlator shielded room shall be fiber optic or low RFI material
- Network routers/switches shall be employed at the MCCC-EVLA M&C interface level for security

#### 3.1.3 CMIB to Correlator Hardware Interface
- CMIB shall communicate with correlator carrier boards via PCI or ISA buses or serial/parallel connection
- CMIB shall read a 16-bit identifier from the host correlator board for unique IP addressing
- CMIB shall read back contents of all writeable hardware control registers where meaningful
- CMIB shall have control of hardware "warm boots" with option to force hardware warm boot
- Carrier board shall have externally visible indicator (LED) for CMIB operational status

### 3.2 Computer Functional Requirements

#### 3.2.1 General
- All computers and peripherals shall be powered through UPS devices with sufficient capacity for safe system shutdown
- All computers shall have ability for authorized users to directly access individual systems for maintenance and monitoring
- Each computer system shall have hardware based watchdog timer configured to reboot system in case of hang

#### 3.2.2 CMIB
- Shall conform to PC104+ standards
- Shall contain 64 Mbytes or greater of SDRAM, IDE hard disk interface, serial and parallel interfaces, PCI/ISA buses, 100BaseT network interface
- Shall boot and run a generic COTS operating system in near real-time environment from local non-volatile storage

#### 3.2.3 MCCC
- Shall be a high availability general-purpose computer supporting multiple Ethernet interfaces and COTS operating systems
- Shall have all required disk and file system facilities installed locally for stand-alone operation
- May exist as hot swappable or redundant CPU device capable of self-healing

#### 3.2.4 CPCC
- Shall be a high availability general-purpose computer capable of accepting external hardware status signals
- Shall have all required disk and file system facilities installed locally for stand-alone operation
- May exist as hot swappable or redundant CPU device capable of self-healing

### 3.3 Performance Requirements

#### 3.3.1 Hardware
- CMCS processors shall meet all data processing deadlines and anticipated future requirements
- CMCS processors shall respond to correlator hardware inputs in deterministic fashion to avoid data loss

#### 3.3.2 Software
- All lower system error and debug messages shall be present at the MCCC layer
- System error and debug messages shall be categorized for filtering by content, detail, and message rate
- All messages shall have UTC and wall clock time stamp information
- Software shall be provided allowing authorized user full access to all messaging, monitor, and control traffic
- Graphical User Interface shall be provided for CMCS test software

### 3.4 Reliability/Availability
- Self-monitoring with capability to detect, report on and automatically remedy abnormal conditions
- Software shall perform without total system restart between maintenance windows
- Hardware shall perform indefinitely without complete loss of service
- System shall continue processing correlator configuration/control events until queues are exhausted
- System shall sit at idle and resume operations with minimal delay

### 3.5 Serviceability
- All system processing and interconnect hardware shall be readily accessible for maintenance
- All systems and application source code shall be available
- All software application modules shall be debuggable
- All software processes shall be killable, restartable, debuggable and testable

### 3.6 Maintainability
- Software tools with complete diagnostic package and customer support
- Operating system software with source code available or sufficient diagnostics and customer support

### 3.7 Scalability
- I/O, communications, and processing hardware shall be easily expandable and reconfigurable
- Accomplished in manner transparent to processing, communications and I/O software functions
- Accomplished in a manner seamless to hardware modules or software functionality at interfaces

### 3.8 Security
- Robust security mechanism restricting access to authorized users
- All users uniquely identified via username and associated password scheme
- All login attempts done in secure manner
- System administrator with unrestricted access
- Each user has system access properties defining privileges
- Administrator can create, remove, edit users and block access

### 3.9 Installation and Upgrades
- System shall continue operations during partial shutdowns for maintenance
- Modular design principles with maximal use of "hot-swappable" devices

### 3.10 Documentation
- Complete and comprehensible hardware systems specifications available
- Well documented software system and application code in familiar language
- Code written in readable style with minimal confusion
