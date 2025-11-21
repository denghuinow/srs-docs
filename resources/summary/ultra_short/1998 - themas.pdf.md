Purpose & Scope: The system manages temperature monitoring and HVAC control in office buildings, specifically for software controlling thermostat interactions and HVAC unit activation. It excludes hardware design, HVAC unit feedback mechanisms, and external system integration beyond thermostat data.  

Product Background / Positioning: Operates as a standalone software layer between thermostats and HVAC hardware, requiring no external system dependencies. Interfaces solely with thermostats for temperature data and HVAC units for control signals, with all hardware assumptions documented.  

Core Functional Overview:  
- Monitor temperature against valid range and overtemp limits (±3°F from setting).  
- Manage HVAC unit utilization (max concurrent units, request queuing).  
- Initialize system state (turn off units, load parameters, set triggers).  
- Generate audible alarms for invalid temperatures or overtemp conditions.  
- Produce operational reports (historical logs, monthly utilization stats).  
- Enable supervisor to adjust thermostat temperature settings.  

Key Users & Usage Scenarios: Only building supervisors interact with the system. They view real-time status, adjust thermostat settings via interface, and review reports. No external user intervention required beyond supervisor actions.  

Major External Interfaces: Thermostats (provide temperature/setting data), HVAC units (receive on/off control signals), supervisor interface (for settings/reports). All interfaces operate via software-defined protocols on Windows NT.  

Key Non-functional Requirements:  
- Temperature validation: Reject values outside ±3°F of valid range.  
- System must run exclusively on Microsoft Windows NT.  
- No feedback from HVAC units to the system (units cannot confirm signal receipt).  

Constraints, Assumptions & Dependencies:  
- Thermostats must provide real-time temperature/setting data without delay.  
- HVAC units cannot report their own on/off status.  
- System assumes all initialization data (unit definitions, triggers) is pre-configured.  

Priorities & Acceptance Approach: Critical path: Temperature monitoring, alarm generation, and HVAC control. Acceptance requires validated temperature range compliance, successful alarm triggering, and correct report generation per specified formats.