# Balanced Summary: Dallas/Ft. Worth Regional Center-to-Center Communications Network (C2C)

## Goals and Scope
The C2C project aims to establish a regional communications network for sharing traffic information and device control among Traffic Management Centers (TMCs) in the Dallas/Ft. Worth area. It will create a common data repository, provide web-based traffic condition maps, and enable remote control of ITS field devices using national ITS standards to ensure extensibility.

## Stakeholders and User Stories
*   **North Central Texas Council of Governments (NCTCOG) / Software Task Force:** Project owner and regional coordinator.
*   **Traffic Management Centers (TMCs) (e.g., TxDOT):** Primary operators providing data and controlling field devices.
*   **Agencies without formal TMCs:** Users needing access to shared traffic data and incident reporting.
*   **System Administrators:** Responsible for maintaining the C2C server and network infrastructure.
*   **Public/Information Consumers:** View traffic conditions via the public web map.

**User Stories:**
1.  As a **TMC operator**, I want to **send and receive standardized traffic and device status data** so that **regional traffic conditions are synchronized**.
2.  As a **TMC operator**, I want to **remotely control field devices (e.g., DMS, CCTV) in another agency's jurisdiction** so that **I can manage incidents affecting regional traffic flow**.
3.  As an **agency without a formal TMC**, I want to **input incident and lane closure data via a GUI** so that **this information is shared with the regional network**.
4.  As a **public user**, I want to **view a color-coded web map showing traffic speeds and incidents** so that **I can plan my travel**.
5.  As a **system administrator**, I want the **system to use configurable software building blocks** so that **it can be extended to new partners and regions**.
6.  As a **project developer**, I want to **operate the system in a test mode with activity logging** so that **I can debug and validate new features**.

## Key Processes
1.  **Data Collection & Conversion:** Triggered by data updates from connected TMCs; system-specific data is converted to the standard TMDD format.
2.  **Data Storage:** Converted data is deposited into the central C2C data repository (Data Collector).
3.  **Data Transmission:** Standardized data is exchanged between centers using DATEX/ASN over TCP/IP protocols.
4.  **Web Map Generation:** Triggered by user request; generates graphical maps from the repository data, showing traffic conditions and incidents.
5.  **Remote Device Command:** Triggered by an authorized GUI user; control commands are formatted and sent to the appropriate TMC for execution.
6.  **Incident/Lane Closure Reporting:** Triggered by a GUI user; allows manual entry of incident data directly into the C2C infrastructure.
7.  **Status Aggregation & Reporting:** System compiles and provides network-wide device status summaries.

## Domain Data Elements
*   **Roadway Network:** (Primary Key: Network Identifier) Key Fields: Network Name, List of Links, List of Nodes, Number of Links.
*   **Traffic Incident:** (Primary Key: Incident ID) Key Fields: Network Identifier, Location, Description, Status, Severity, Confirmed Time.
*   **Field Device (e.g., DMS, CCTV):** (Primary Key: Device Identifier) Key Fields: Network Identifier, Device Type, Location (Lat/Long), Status, Current State/Message.
*   **Traffic Condition Data:** (Primary Key: Link Identifier + Timestamp) Key Fields: Network Identifier, Speed, Volume, Occupancy, Travel Time.
*   **Lane Closure:** (Primary Key: Lane Closure ID) Key Fields: Network Identifier, Location, Description, Affected Lanes, Schedule (Start/End).
*   **User Command Request:** (Primary Key: Request ID) Key Fields: Username, Target Device, Command Parameters, Timestamp.

## Non-Functional Requirements
1.  **Interoperability:** System shall communicate using the ITS Traffic Management Data Dictionary (TMDD) standard and associated message sets.
2.  **Extensibility:** Software shall be built as configurable "building blocks" to allow cost-effective extension to new partners and regions.
3.  **Platform:** Core server components shall execute in a Microsoft Windows NT environment.
4.  **Implementation:** Core software shall be implemented in the C/C++ programming language.
5.  **Connectivity:** DATEX/ASN runtime libraries must be available on all communicating computers.
6.  **Operational Modes:** System must support both a normal operational mode and a test mode with activity logging.

## Milestones and External Dependencies
1.  Development and configuration of interfaces to existing, dissimilar traffic management systems.
2.  Establishment of the central C2C data repository and communication "cloud."
3.  Integration with the NCTCOG Geo-Data warehouse for base map data.
4.  Deployment of the Remote Control and Incident GUI applications to end-user agencies.
5.  Successful testing of device command/control between different centers (e.g., Dallas to Ft. Worth).

## Risks and Mitigation Strategies
1.  **Risk:** Complexity of interfacing with multiple, dissimilar legacy TMC systems.
    *   **Mitigation:** Use of a project-defined protocol adapter to convert system-specific data to the standard TMDD format.
2.  **Risk:** Data inconsistency when associating transit data (e.g., bus stops) with roadway network links managed by separate centers.
    *   **Mitigation:** Careful configuration management and clear ownership definitions; acknowledged as an inherent difficulty.
3.  **Risk:** Ensuring secure and authorized remote control of field devices across agency boundaries.
    *   **Mitigation:** Implementation of username/password authentication and device-specific command timeframe controls.
4.  **Risk:** Network connectivity issues through various agency firewalls and gateways.
    *   **Mitigation:** Use of standard TCP/IP; though noted that firewall traversal is not fully addressed by the software requirements alone.
5.  **Risk:** Scalability and performance as more centers and device types are added.
    *   **Mitigation:** Design based on configurable, reusable software building blocks to facilitate scaling.

## Undecided Issues
1.  Specific speed threshold values (TBD MPH) for color-coding traffic conditions (green/yellow/red) on the web map.
2.  Full support for certain CCTV control commands (e.g., Momentary Pan/Tilt) may vary by center (Ft. Worth noted as non-supporting).
3.  Support for the "Tour" video switch command for CCTVs is not supported by Dallas.
4.  The challenge of maintaining link identifier consistency between separately managed roadway and transit databases requires a procedural solution.
5.  Connectivity and network traversal through public networks (Internet) and various agency firewalls for the Remote Control GUI is noted but not fully specified.
6.  Detailed configuration parameters for the software "building blocks" when deployed for specific agencies.