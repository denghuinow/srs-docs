```markdown
# Software Requirements Specification (SRS)
## EIRENE GSM-R System

**Document Version:** 1.0  
**Date:** [Current Date]  
**Status:** Draft

---

## 1. Introduction

### 1.1 Purpose
This document specifies the requirements for the EIRENE (European Integrated Railway Radio Enhanced Network) GSM-R system, which provides standardized GSM-based voice and data communications for European railway operations. The SRS serves as a comprehensive guide for developers, testers, and stakeholders to ensure the system meets railway operational and safety requirements.

### 1.2 Scope
The EIRENE system encompasses:
- Ground-to-train voice and data communications
- Mobile communications for railway staff including trackside workers, station personnel, and administrative staff
- Cross-border interoperability for international train operations
- Integration with existing railway control and safety systems

**Out of Scope:**
- Physical implementation of radio equipment
- Mobile equipment specifications (handled separately)

### 1.3 Definitions and Acronyms

| Term | Definition |
|------|------------|
| GSM-R | GSM for Railways |
| VGCS | Voice Group Call Service |
| VBS | Voice Broadcast Service |
| eMLPP | Enhanced Multi-Level Precedence and Pre-emption |
| ERTMS/ETCS | European Rail Traffic Management System/European Train Control System |
| UIC | International Union of Railways |
| MSISDN | Mobile Station International Subscriber Directory Number |
| BSS | Base Station Subsystem |
| NSS | Network Switching Subsystem |
| TIU | Train Interface Unit |

## 2. Overall Description

### 2.1 Product Perspective
EIRENE extends standard GSM technology with railway-specific enhancements to ensure technical interoperability for cross-border operations. The system integrates with existing railway infrastructure and serves as a critical communication backbone for railway operations and safety systems.

### 2.2 Product Functions
- Railway-specific voice communication services
- Priority-based call handling and pre-emption
- Functional and location-dependent addressing
- Emergency call handling with automatic confirmation
- Fallback communication modes for network failures
- Integration with train control and safety systems

### 2.3 User Characteristics

| User Role | Primary Functions | Priority Level |
|-----------|-------------------|----------------|
| Train Driver | Operational communications, emergency calls, multiple driver communications | Level 2 |
| Primary Controller | Train movement coordination | Level 3 |
| Secondary Controller | Support coordination | Level 3 |
| Shunting Team Leader | Shunting operations | Level 2 |
| Trackside Workers | Maintenance and operational communications | Level 4 |
| Station Staff | Station operations and passenger communications | Level 4 |

### 2.4 Constraints
- Must comply with ETSI EN 301 515 GSM standards
- Requires implementation of eMLPP across all network elements
- Dependent on standardized numbering plans (National and International EIRENE Numbers)
- Requires interoperability between national railway networks
- Cell-dependent routing as primary location addressing method

### 2.5 Assumptions and Dependencies
- GSM network infrastructure is available and operational
- ERTMS/ETCS systems are properly integrated
- Standardized numbering plans are implemented across participating railways
- National railway networks maintain GMSC interconnections

## 3. System Features and Requirements

### 3.1 Voice Communication Services

#### 3.1.1 Voice Group Call Service (VGCS)
**Requirement ID:** VGCS-001  
**Description:** The system shall support Voice Group Call Service for group communications among railway personnel.  
**Priority:** High  
**Verification:** Functional testing, integration testing

#### 3.1.2 Voice Broadcast Service (VBS)
**Requirement ID:** VBS-001  
**Description:** The system shall support Voice Broadcast Service for one-to-many communications.  
**Priority:** High  
**Verification:** Functional testing

### 3.2 Priority Handling System

#### 3.2.1 Enhanced Multi-Level Precedence and Pre-emption (eMLPP)
**Requirement ID:** eMLPP-001  
**Description:** The system shall implement eMLPP for priority-based call handling across all railway operations.  
**Priority:** Critical  
**Verification:** Performance testing, priority scenario testing

#### 3.2.2 Priority Level Implementation
**Requirement ID:** PRIO-001  
**Description:** The system shall support the following priority levels consistently across all networks:

| Priority Level | Usage | Pre-emption Capability |
|----------------|-------|------------------------|
| Level 0 | Railway emergency calls | Full pre-emption |
| Level 2 | Railway operation calls | Limited pre-emption |
| Level 3 | Controller communications | Limited pre-emption |
| Level 4 | Railway information calls | No pre-emption |

**Priority:** Critical  
**Verification:** Cross-network interoperability testing

### 3.3 Addressing Systems

#### 3.3.1 Functional Addressing
**Requirement ID:** FUNC-ADDR-001  
**Description:** The system shall allow calls to be placed by role (e.g., train number, driver) rather than specific user identifiers.  
**Priority:** High  
**Verification:** Functional testing with role-based calling scenarios

#### 3.3.2 Location-Dependent Addressing
**Requirement ID:** LOC-ADDR-001  
**Description:** The system shall route calls based on train location within the railway network using cell-dependent routing.  
**Priority:** High  
**Verification:** Location-based routing tests, handover testing

### 3.4 Emergency Call Handling

#### 3.4.1 Railway Emergency Calls
**Requirement ID:** EMERG-001  
**Description:** The system shall process railway emergency calls with highest priority (level 0) to stop train movements in safety-critical situations.  
**Priority:** Critical  
**Verification:** Safety-critical scenario testing

#### 3.4.2 Emergency Call Confirmation
**Requirement ID:** EMERG-002  
**Description:** The system shall automatically send emergency call confirmation to the confirmation center using UUS1.  
**Priority:** Critical  
**Verification:** Confirmation message testing, failure scenario testing

#### 3.4.3 Automatic Retry on Failure
**Requirement ID:** EMERG-003  
**Description:** The system shall implement automatic retry mechanisms for emergency calls in case of transmission failure.  
**Priority:** Critical  
**Verification:** Network failure simulation testing

### 3.5 Specialized Operation Modes

#### 3.5.1 Shunting Mode
**Requirement ID:** SHUNT-001  
**Description:** The system shall provide specialized communication functionality during train shunting operations.  
**Priority:** Medium  
**Verification:** Shunting operation scenario testing

#### 3.5.2 Direct Mode
**Requirement ID:** DIRECT-001  
**Description:** The system shall support direct mode as fallback communication without network infrastructure.  
**Constraints:** 1W maximum transmit power, simplex operation  
**Priority:** Medium  
**Verification:** Direct mode functionality testing, power level verification

## 4. External Interface Requirements

### 4.1 Hardware Interfaces

| Interface | Description | Requirements |
|-----------|-------------|--------------|
| GSM Network Infrastructure | BSS, NSS for standard mobile services | Standard GSM interface compliance |
| ERTMS/ETCS Systems | Train control and safety communications | Secure data exchange protocols |
| Public Address Systems | Passenger announcements | Audio interface compatibility |
| UIC Intercom | On-train communication | Standard railway intercom interface |
| Driver's Safety Device | Alertness monitoring | Data interface for alert status |
| Train Borne Recorder | Call logging | Data logging interface |
| Train Interface Unit (TIU) | On-train systems to radio connection | Standard TIU interface protocol |

### 4.2 Software Interfaces
- GSM protocol stack implementation
- eMLPP priority handling software
- Functional number to MSISDN translation services
- Location-based routing algorithms
- Emergency call processing modules

### 4.3 Communication Interfaces
- GSM-R air interface compliant with ETSI standards
- Inter-network signaling for cross-border operations
- Data communication protocols for ETCS integration
- Direct mode radio communication protocols

## 5. Non-Functional Requirements

### 5.1 Performance Requirements

#### 5.1.1 Coverage Requirements
**Requirement ID:** PERF-COV-001  
**Description:** The system shall provide 95% probability coverage at 38.5 dBµV/m for voice communications.  
**Priority:** High  
**Verification:** Field strength measurements, coverage mapping

**Requirement ID:** PERF-COV-002  
**Description:** The system shall provide 95% probability coverage at 41.5 dBµV/m for ETCS levels 2/3 data communications.  
**Priority:** Critical  
**Verification:** ETCS-specific coverage testing

#### 5.1.2 Handover Performance
**Requirement ID:** PERF-HO-001  
**Description:** The system shall maintain minimum 99.5% handover success rate over all train routes.  
**Priority:** High  
**Verification:** Handover success rate monitoring, route testing

#### 5.1.3 Call Setup Time
**Requirement ID:** PERF-SETUP-001  
**Description:** All call setup times must be achieved with authentication and ciphering enabled.  
**Priority:** High  
**Verification:** Call setup timing tests with security features active

#### 5.1.4 Alerting Duration
**Requirement ID:** PERF-ALERT-001  
**Description:** The system shall maintain maximum 60 seconds alerting duration for priority calls.  
**Priority:** Medium  
**Verification:** Alert timing tests under various network conditions

### 5.2 Reliability Requirements
**Requirement ID:** REL-001  
**Description:** The system shall maintain 99.95% availability for critical communication functions.  
**Priority:** Critical  
**Verification:** Availability monitoring, failure analysis

### 5.3 Safety Requirements
**Requirement ID:** SAFE-001  
**Description:** Emergency call functionality shall maintain operational status under all network conditions.  
**Priority:** Critical  
**Verification:** Safety case analysis, failure mode testing

### 5.4 Security Requirements
**Requirement ID:** SEC-001  
**Description:** The system shall implement authentication and ciphering for all communications.  
**Priority:** High  
**Verification:** Security protocol testing, vulnerability assessment

### 5.5 Operational Requirements
**Requirement ID:** OPS-001  
**Description:** Mobile equipment shall provide minimum 8 hours battery life based on specified usage profile.  
**Priority:** Medium  
**Verification:** Battery life testing under operational conditions

## 6. System Attributes

### 6.1 Availability
- 99.95% availability for critical communication functions
- Redundant network elements for high availability
- Automatic failover mechanisms

### 6.2 Interoperability
- Cross-border interoperability between national railway networks
- Standardized interfaces with ERTMS/ETCS systems
- Consistent implementation across all participating railways

### 6.3 Maintainability
- Remote monitoring and diagnostic capabilities
- Standardized maintenance procedures
- Comprehensive logging and reporting functions

## 7. Acceptance Criteria

### 7.1 Coverage Acceptance
- 95% probability coverage at 38.5 dBµV/m for voice communications
- 95% probability coverage at 41.5 dBµV/m for ETCS levels 2/3

### 7.2 Performance Acceptance
- Minimum 99.5% handover success rate over train routes
- Call setup time requirements met with security features enabled
- Maximum 60 seconds alerting duration for priority calls

### 7.3 Functional Acceptance
- All priority levels consistently implemented across networks
- Emergency call confirmation automatically sent using UUS1
- Functional addressing working correctly across all user roles
- Location-dependent routing functioning as specified

### 7.4 Safety Acceptance
- Railway emergency calls processed immediately with level 0 priority
- Automatic retry functionality operational for emergency calls
- Direct mode available as reliable fallback communication

## 8. Appendix

### 8.1 References
- ETSI EN 301 515: GSM Railway specific requirements
- UIC Project EIRENE specifications
- ERTMS/ETCS technical specifications

### 8.2 Glossary
- **Functional Addressing:** Calling by role rather than individual identifier
- **Cell-dependent Routing:** Location-based call routing using GSM cell information
- **eMLPP:** Enhanced Multi-Level Precedence and Pre-emption for priority handling
- **VGCS/VBS:** Group and broadcast voice services for railway operations

---

**Document Approval**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Manager | | | |
| Technical Lead | | | |
| Quality Assurance | | | |
| Customer Representative | | | |
```