```markdown
# Software Requirements Specification
## WIDAR Correlator Interface System

**Document Version:** 1.0  
**Date:** [Current Date]  
**Status:** Draft

---

## Table of Contents
1. [Introduction](#1-introduction)
2. [Overall Description](#2-overall-description)
3. [System Features](#3-system-features)
4. [External Interface Requirements](#4-external-interface-requirements)
5. [Non-Functional Requirements](#5-non-functional-requirements)
6. [Constraints, Assumptions & Dependencies](#6-constraints-assumptions--dependencies)
7. [Acceptance Criteria](#7-acceptance-criteria)

---

## 1 Introduction

### 1.1 Purpose
This document specifies the requirements for the WIDAR Correlator Interface System, which serves as the physical interface between WIDAR Correlator hardware and the EVLA Monitor & Control system. The system enables configuration, operation, and servicing of the correlator without performing data processing or scientific analysis.

### 1.2 Scope
The system provides gateway functionality between EVLA M&C and correlator hardware, including:
- Configuration translation and command execution
- Health monitoring and autonomous fault recovery
- Real-time data output to backend systems
- Dynamic control data processing and transfer
- Remote debugging and maintenance capabilities

**Out of Scope:** Scientific data processing, astronomical analysis, and long-term data storage.

### 1.3 Definitions and Acronyms

| Acronym | Definition |
|---------|------------|
| WIDAR | Wideband Interferometric Digital ARchitecture |
| EVLA | Expanded Very Large Array |
| M&C | Monitor and Control |
| VCI | Virtual Correlator Interface |
| MCCC | Master Correlator Control Computer |
| CPCC | Correlator Pipeline Control Computer |
| CMIB | Correlator Monitor Interface Board |
| CMCS | Correlator Monitor and Control System |

## 2 Overall Description

### 2.1 Product Perspective
The system is integrated into the EVLA M&C infrastructure as the primary correlator gateway via the Virtual Correlator Interface (VCI). It employs a Master/Slave network topology to isolate correlator hardware from the broader EVLA environment, ensuring operational security and stability.

### 2.2 Product Functions
- **Configuration Management:** Translate EVLA M&C configuration requests into correlator hardware settings
- **Fault Management:** Monitor correlator health and autonomously recover from predefined faults
- **Data Output:** Stream real-time data products to backend systems
- **Control Processing:** Handle dynamic control data including models and filter parameters
- **Debugging Support:** Provide remote access tools for system testing and troubleshooting

### 2.3 User Characteristics

| User Role | Primary Responsibilities | Access Level |
|-----------|--------------------------|--------------|
| Array Operator | Monitor status, receive error messages | Read-only operational data |
| Engineer | Fault tracing, remote maintenance | System configuration and diagnostics |
| Software Developer | Troubleshooting, system debugging | Full system access with restrictions |
| Web User | Limited monitoring capabilities | Restricted, view-only access |

### 2.4 Operational Environment
- **Hardware:** Modular correlator hardware with fault isolation capabilities
- **Network:** Master/Slave topology with redundant communication paths
- **Criticality:** System failure results in immediate astronomical data loss

## 3 System Features

### 3.1 Configuration Translation
**3.1.1 Description**  
Translate EVLA M&C configuration requests into specific correlator hardware settings and commands.

**3.1.2 Requirements**
- `REQ-CONF-001`: The system shall accept configuration requests from EVLA M&C system
- `REQ-CONF-002`: The system shall validate configuration parameters before execution
- `REQ-CONF-003`: The system shall generate appropriate hardware commands for validated configurations
- `REQ-CONF-004`: The system shall provide configuration status feedback to EVLA M&C

### 3.2 Health Monitoring and Fault Recovery
**3.2.1 Description**  
Continuously monitor correlator health and autonomously recover from predefined fault conditions.

**3.2.2 Requirements**
- `REQ-MON-001`: The system shall monitor all critical correlator hardware components
- `REQ-MON-002`: The system shall detect and classify fault conditions according to severity
- `REQ-MON-003`: The system shall autonomously initiate recovery procedures for predefined faults
- `REQ-MON-004`: The system shall log all fault events with UTC and wall clock timestamps
- `REQ-MON-005`: The system shall notify operators of fault conditions and recovery actions

### 3.3 Real-time Data Output
**3.3.1 Description**  
Output real-time data products (including auto-correlation products) to designated backend systems.

**3.3.2 Requirements**
- `REQ-DATA-001`: The system shall generate auto-correlation products in real-time
- `REQ-DATA-002`: The system shall stream data to backend systems at specified rates
- `REQ-DATA-003`: The system shall ensure data integrity during transmission
- `REQ-DATA-004`: The system shall handle backend system unavailability gracefully

### 3.4 Dynamic Control Data Processing
**3.4.1 Description**  
Process and transfer dynamic control data including models and filter parameters.

**3.4.2 Requirements**
- `REQ-CTRL-001`: The system shall process dynamic control data updates
- `REQ-CTRL-002`: The system shall maintain control data queues with zero data loss during exhaustion
- `REQ-CTRL-003`: The system shall transfer updated parameters to correlator hardware
- `REQ-CTRL-004`: The system shall validate control data before application

### 3.5 Debugging and Maintenance Tools
**3.5.1 Description**  
Provide remote access and testing tools for system debugging and maintenance.

**3.5.2 Requirements**
- `REQ-DBG-001`: The system shall provide remote access capabilities for authorized users
- `REQ-DBG-002`: The system shall include diagnostic tools for fault tracing
- `REQ-DBG-003`: The system shall support testing modes without affecting production operations
- `REQ-DBG-004`: The system shall maintain audit logs of all remote access sessions

## 4 External Interface Requirements

### 4.1 Hardware Interfaces
- **Ethernet:** 100 Mbps+ for CMIB/MCCC/CPCC communication
- **Fiber Optic:** Primary interface between MCCC and EVLA M&C system
- **RS-232c:** Redundant serial communication for MCCC-CPCC interfaces

### 4.2 Software Interfaces
- **EVLA M&C System:** Primary command and control interface via VCI
- **Backend Data Systems:** Real-time data output consumers
- **Authentication Services:** Role-based access control integration

### 4.3 Communication Interfaces
- **Protocols:** Support for standard astronomical data protocols
- **Data Rates:** Capable of handling CMCS output rates as specified
- **Redundancy:** Failover capabilities for critical communication paths

## 5 Non-Functional Requirements

### 5.1 Reliability
- `REQ-REL-001`: System shall maintain 99.9% uptime during correlator operations
- `REQ-REL-002`: Redundant MCCC systems shall failover within 5 minutes of primary failure
- `REQ-REL-003`: System shall autonomously recover from all predefined fault conditions

### 5.2 Security
- `REQ-SEC-001`: System shall implement role-based access control with four defined roles (admin, engineer, developer, web user)
- `REQ-SEC-002`: All authentication attempts shall be logged
- `REQ-SEC-003`: Web user access shall be limited and restricted to view-only capabilities

### 5.3 Performance
- `REQ-PER-001`: System shall process configuration requests within specified time constraints
- `REQ-PER-002`: Real-time data output shall maintain required data rates without loss
- `REQ-PER-003`: Fault detection and classification shall occur within defined latency limits

### 5.4 Logging and Monitoring
- `REQ-LOG-001`: All error messages shall be timestamped with both UTC and wall clock time
- `REQ-LOG-002`: System shall maintain comprehensive audit trails of all operations
- `REQ-LOG-003`: Health monitoring data shall be available in real-time to authorized users

## 6 Constraints, Assumptions & Dependencies

### 6.1 Constraints
- **Criticality:** System unavailability directly causes astronomical data loss
- **Hardware:** Must maintain modular architecture for fault isolation
- **Legacy:** Must integrate with existing EVLA M&C infrastructure

### 6.2 Assumptions
- Backend systems are capable of accepting CMCS output data rates
- EVLA M&C system provides valid configuration requests
- Hardware modularity enables effective fault isolation

### 6.3 Dependencies
- **EVLA M&C System:** For configuration requests and system coordination
- **Correlator Hardware:** For physical interface and command execution
- **Network Infrastructure:** For reliable communication between components

## 7 Acceptance Criteria

### 7.1 Priority Requirements
Reliability and system uptime are the highest priority requirements. The system must demonstrate robust operation under normal and fault conditions.

### 7.2 Acceptance Tests
1. **Autonomous Recovery Verification**
   - System must demonstrate autonomous recovery from all predefined fault conditions
   - Recovery procedures must complete within specified time limits

2. **Data Integrity Validation**
   - Zero data loss must be demonstrated during control data queue exhaustion scenarios
   - Real-time data streams must maintain integrity during system stress tests

3. **Access Control Enforcement**
   - Role-based access control must be rigorously tested across all user roles
   - Unauthorized access attempts must be properly rejected and logged

4. **Uptime and Reliability**
   - System must demonstrate 99.9% uptime over extended operational testing
   - Failover between redundant MCCC systems must occur within 5 minutes

### 7.3 Performance Metrics
- Configuration request processing time: < 2 seconds
- Fault detection latency: < 1 second
- Data output consistency: 100% during normal operations
- Failover completion: < 5 minutes

---
**Document Approval**

| Role | Name | Signature | Date |
|------|------|------------|------|
| Project Manager | | | |
| Lead Engineer | | | |
| Quality Assurance | | | |
```