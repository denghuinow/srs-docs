Purpose & Scope  
The system provides the physical interface between WIDAR Correlator hardware and the EVLA Monitor & Control system, enabling configuration, operation, and servicing of the correlator. It does not perform data processing or scientific analysis. Critical failure results in astronomical data loss.  

Product Background / Positioning  
Integrated into the EVLA M&C structure as the primary correlator gateway via the Virtual Correlator Interface (VCI). Isolates correlator hardware from the broader EVLA environment through a Master/Slave network topology.  

Core Functional Overview  
- Translate EVLA M&C configuration requests into correlator hardware settings.  
- Monitor correlator health and autonomously recover from faults.  
- Output real-time data (e.g., auto-correlation products) to backend systems.  
- Process and transfer dynamic control data (models, filter parameters).  
- Provide debugging tools for remote system access and testing.  

Key Users & Usage Scenarios  
Array operators receive status/error messages. Engineers perform fault tracing and remote maintenance. Software developers require remote access for troubleshooting. Web users have limited, restricted access.  

Major External Interfaces  
Ethernet (100 Mbps+) for CMIB/MCCC/CPCC communication. Fiber optic for MCCC-EVLA M&C interface. Redundant RS-232c for MCCC-CPCC.  

Key Non-functional Requirements  
99.9% uptime for correlator operations. Redundant MCCC with <5-minute failover. Role-based access control (admin, engineer, developer, web user). All error messages timestamped with UTC and wall clock time.  

Constraints, Assumptions & Dependencies  
Critical application: Correlator unavailability causes data loss. Hardware must be modular for fault isolation. Backend systems must accept CMCS output rates (assumed valid).  

Priorities & Acceptance Approach  
Reliability and uptime are highest priority. Acceptance requires: (1) Autonomous recovery from all listed faults, (2) Zero data loss during control data queue exhaustion, (3) Role-based access enforcement.