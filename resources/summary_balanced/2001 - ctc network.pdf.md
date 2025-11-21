# Balanced Summary

**Goals and scope**  
The C2C Communications Network aims to create a common repository for traffic information in the Dallas/Ft. Worth Metroplex and enable device control and status sharing between Traffic Management Centers. It uses ITS standards like TMDD to ensure extensibility and interoperability across regional and statewide partners.

**Roles and user stories**  
- As a Traffic Management Center operator, I want to share roadway network data so that regional traffic conditions are accurately represented.  
- As a TMC operator, I want to control remote Dynamic Message Signs so that traffic advisories can be displayed consistently.  
- As a TMC operator, I want to monitor CCTV camera status so that incident verification is possible.  
- As a user without a formal TMC, I want to input incident data via a GUI so that lane closures and incidents are reported.  
- As a system administrator, I want the system to operate in test mode so that development and logging activities are supported.

**Key processes**  
1. Trigger: Data received from connected systems → Convert data to TMDD standard format.  
2. Store standardized traffic and device data in the common repository.  
3. Transmit data between centers using DATEX/ASN over TCP/IP.  
4. Generate and update a web-based graphical map displaying traffic conditions and incidents.  
5. Allow remote users to submit device control commands via authentication.  
6. Process and route device control requests (e.g., DMS message updates).  
7. Operate in normal or test mode, with test mode enabling activity logging.

**Domain data elements**  
- Roadway Network: Network ID (primary key), Network name, Number of links, Number of nodes, List of link data  
- Incident: Incident ID (primary key), Location, Status, Affected lanes, Severity  
- Dynamic Message Sign (DMS): DMS ID (primary key), Location, Status, Current message, Beacons status  
- Lane Control Signal (LCS): LCS ID (primary key), Location, Status, Current pattern, Geometry  
- CCTV: CCTV ID (primary key), Location, Status, Lock holder, Current direction  
- Traffic Conditions: Link ID (primary key), Speed, Volume, Occupancy, Travel time  

**Non-functional requirements**  
- Execute in Microsoft Windows NT environment.  
- Use DATEX/ASN runtime library for communications.  
- Implement web maps with ESRI ARC Internet Map Server.  
- Support operation in both normal and test modes.  
- Use TCP/IP for data transmission between centers.  
- Develop Incident and Remote Control GUIs using C/C++ and ESRI Map Objects.

**Milestones and external dependencies**  
- Integration with NCTCOG Geo-Data warehouse for basemap data.  
- Compliance with evolving ITS TMDD and message set standards.  
- Dependence on DATEX/ASN and TCP/IP protocol implementations.  
- Coordination with multiple agencies for device and network data.  
- Use of ESRI ARC IMS and Map Objects for mapping and GUI components.

**Risks and mitigation strategies**  
- Risk: Inconsistent data from separate roadway and transit management systems. Mitigation: Define clear configuration management and update procedures.  
- Risk: Compatibility issues with legacy traffic management systems. Mitigation: Use standardized TMDD formats and configurable building blocks.  
- Risk: Network or device control failures during remote operations. Mitigation: Implement status monitoring and command timeframe controls.  
- Risk: Evolving ITS standards affecting system compliance. Mitigation: Design for modular updates and adherence to baseline standards.  
- Risk: Security vulnerabilities in public network operations. Mitigation: Incorporate user authentication and firewall considerations.

**Undecided issues**  
- Specific speed thresholds for map color coding (TBD MPH values).  
- Support for Momentary Pan/Tilt/Zoom/Iris/Focus commands in Fort Worth CCTVs.  
- Support for Tour video switch command in Dallas CCTVs.  
- Handling of link identifier inconsistencies between roadway and transit data.  
- Not mentioned  
- Not mentioned