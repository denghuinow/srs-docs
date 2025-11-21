**Purpose & Scope**  
The system provides a regional traffic data repository and communication infrastructure connecting existing Traffic Management Centers (TMCs) across the Dallas/Fort Worth Metroplex. It enables standardized exchange of traffic data and device control between agencies using ITS standards, without building new physical traffic infrastructure. Excludes direct traffic signal control or real-time vehicle navigation.

**Product Background / Positioning**  
Serves as a regional extension of the Texas Department of Transportation’s (TxDOT) Center-to-Center (C2C) project. Integrates with existing TMCs and ITS field devices (e.g., DMS, CCTV, ramp meters) via standardized interfaces, creating a reusable foundation for statewide traffic management systems.

**Core Functional Overview**  
- Centralized traffic data repository for roadway, incident, and device status.  
- Web-based map visualization of traffic conditions and incidents.  
- Incident reporting and lane closure management via GUI.  
- Remote control of ITS devices (DMS, LCS, CCTV, ramp meters, HAR).  
- Real-time network device status monitoring (e.g., DMS, CCTV, traffic signals).  
- Support for multi-agency data sharing and interoperability.

**Key Users & Usage Scenarios**  
Primary users: Traffic agencies without formal TMCs (using web GUI) and regional TMC operators (using remote control GUI). Agencies report incidents via GUI; TMCs remotely control devices across networks. Permission levels differentiate data access and control capabilities.

**Major External Interfaces**  
Interfaces with existing ITS systems via ITS standards (TMDD, DATEX/ASN) over TCP/IP. Includes device-specific protocols for traffic signals, DMS, CCTV, and sensor data. No custom protocols for new ITS-compliant systems.

**Key Non-functional Requirements**  
Operates in two modes: normal (data aggregation) and test (data logging). Must support 24/7 availability for traffic operations. Relies on standardized data formats (TMDD) for interoperability.

**Constraints, Assumptions & Dependencies**  
Depends on all connected TMCs adopting ITS standards (TMDD) for data exchange. Requires existing TMCs to provide standardized data feeds. Assumes network infrastructure supports TCP/IP communications.

**Priorities & Acceptance Approach**  
Top priority: Data repository functionality and web map visualization. Secondary: Incident reporting and remote device control. Acceptance requires successful operation in normal mode with all specified interfaces exchanging data per TMDD standards.