**Purpose & Scope**
The system is the Dallas/Ft. Worth Regional Center-to-Center Communications Network. It creates a common repository for regional traffic information and enables the exchange of device control commands between different Traffic Management Centers. It does not directly interface with field devices; it connects existing, dissimilar traffic management systems.

**Product Background / Positioning**
The system extends a Texas Department of Transportation C2C project to interconnect multiple agency Traffic Management Centers in the DFW metroplex. It sits between these existing centers, acting as a standardized data hub and command router.

**Core Functional Overview**
1.  Collect and store standardized traffic data (roadway networks, conditions, incidents) from multiple centers.
2.  Transmit device status data (for DMS, LCS, CCTV, ramp meters, traffic signals, etc.) between centers.
3.  Allow remote command/control of field devices (DMS, LCS, CCTV, ramp meters, etc.) across center boundaries.
4.  Provide a web-based graphical map displaying traffic conditions, incidents, and device locations.
5.  Provide a standalone GUI for agencies to input and manage incident and lane closure data.
6.  Provide a remote control GUI for authorized users to issue device commands over a public network.

**Key Users & Usage Scenarios**
Primary users are traffic operators and managers at various Traffic Management Centers (e.g., TxDOT, city agencies). They use the system to view a consolidated regional traffic picture, coordinate incident response, and request control of devices owned by other agencies (e.g., changing a message sign on a different jurisdiction's highway).

**Major External Interfaces**
The system interfaces with the backend systems of multiple Traffic Management Centers. It also provides a web interface for the public map and client GUI applications for incident entry and remote device control.

**Key Non-functional Requirements**
The system shall utilize the ITS Traffic Management Data Dictionary (TMDD) standard and DATEX/ASN over TCP/IP for all data transmission. The server components shall execute in a Microsoft Windows NT environment.

**Constraints, Assumptions & Dependencies**
The system is constrained to using specific commercial software: ESRI's ARC Internet Map Server and Map Objects. It depends on each connected center providing data in a project-defined protocol or being based on ITS standards.

**Priorities & Acceptance Approach**
Core priorities are establishing the standardized data repository and enabling basic device status sharing and control. Acceptance will involve verifying data flows correctly between centers, the web map displays integrated data, and remote device commands are properly routed and executed.