# Detailed Summary: Dallas/Ft. Worth Regional Center-to-Center Communications Network (C2C)

## Background and Scope
This project establishes a regional Center-to-Center (C2C) communications network for the Dallas/Ft. Worth metroplex, based on an initial Texas Department of Transportation (TxDOT) project. Its primary goal is to create a common repository for traffic data and a mechanism for exchanging device control information between disparate Traffic Management Centers (TMCs) and agencies. The system will be built using Intelligent Transportation Systems (ITS) standards, specifically the Traffic Management Data Dictionary (TMDD), to ensure extensibility and future cost-effective expansion to local, regional, and statewide levels. A key non-goal is the direct integration of new, standards-based systems via the project's custom protocol; such systems would instead connect natively using the ITS standards.

## Stakeholders Matrix and Use Cases
*   **North Central Texas Council of Governments (NCTCOG) / Software Task Force:** The project sponsor and governing body responsible for regional coordination and requirements definition.
*   **Traffic Management Centers (TMCs) (e.g., TxDOT Dallas/Ft. Worth):** Primary operators who provide traffic data and accept remote control commands for their field devices via the C2C infrastructure.
*   **Agencies without formal TMCs:** Secondary users who input incident data and potentially issue device control requests via provided GUI applications.
*   **System Administrators:** Personnel responsible for configuring, deploying, and maintaining the C2C server software and its building blocks.
*   **Public/Web Users:** End-users who access the web-based map to view real-time traffic conditions, incidents, and device statuses.

**Main Scenarios:**
1.  A TMC automatically publishes real-time traffic condition data (speed, volume) for its roadway links to the common repository.
2.  An agency user reports a new traffic incident via the Incident GUI, which is propagated to the repository and displayed on the web map.
3.  A remote operator uses the Remote Control GUI to send a command to change the message on a Dynamic Message Sign (DMS) located in another agency's jurisdiction.
4.  The web map application retrieves consolidated data from the repository to display color-coded traffic speeds and incident icons to the public.

**Exception Scenarios:**
1.  A device control command is rejected because it was issued outside the pre-configured timeframe during which the owning center accepts remote commands.
2.  The connection to a participating center is lost; the C2C infrastructure logs the failure and continues operating with data from remaining centers.
3.  An attempt is made to control a CCTV camera with a command type (e.g., Momentary Pan/Tilt) that the owning center's system does not support.

## Business Process
**Main Process: Regional Data Aggregation & Dissemination**
1.  **Trigger:** A participating center's system generates new data (e.g., updated link speed, new incident).
2.  **Input:** Raw data in the center's native format.
3.  The center's local interface converts the data into the standard TMDD/DATEX-ASN format.
4.  The formatted data is transmitted via TCP/IP to the C2C infrastructure's Data Collector.
5.  The Data Collector validates and stores the data in the common repository.
6.  **Output:** The updated repository.
7.  Subscribed applications (e.g., Web Map, other centers) are notified of or poll for the updated data.
8.  Applications process and present the data (e.g., update map colors, populate status lists).

**Key Branch A: Remote Device Control**
1.  **Trigger:** An authenticated user submits a device command via the Remote Control GUI.
2.  **Input:** Command details (device ID, action, credentials).
3.  The GUI formats the command into a TMDD control message and sends it to the target center via the C2C infrastructure.
4.  The target center validates credentials and command timeframe, executes the command on its local system, and returns a status response.

**Key Branch B: Direct Data Input via GUI**
1.  **Trigger:** An agency user enters a new incident or lane closure via the Incident GUI.
2.  **Input:** Incident/location details (description, location, lanes affected).
3.  The GUI application formats the data and submits it directly to the C2C repository.
4.  The repository stores the data and makes it available for dissemination like any other data source.

## Domain Model
Core entities managed within the C2C repository include:
1.  **Network:** Represents a participating agency's roadway system. *(Fields: identifier (unique), name, owner (required))*
2.  **Link:** A segment of roadway. *(Fields: identifier (unique), network (reference), start/end node (reference), direction, speed limit)*
3.  **Node:** A point in the network (e.g., intersection). *(Fields: identifier (unique), network (reference), latitude/longitude (required))*
4.  **Traffic Condition:** Real-time data for a link. *(Fields: link (reference), timestamp (required), speed, volume)*
5.  **Incident:** A reported traffic event. *(Fields: identifier (unique), network (reference), location, description (required), status, severity)*
6.  **Device:** A generic field device. *(Fields: identifier (unique), network (reference), type (e.g., DMS, CCTV), location, status (required))*
7.  **Device Command:** A request to control a device. *(Fields: device (reference), username (required), requested action, timeframe)*
8.  **User:** An entity that can input data or issue commands. *(Fields: username (unique), role, associated network (reference))*

## Interfaces and Integrations
1.  **System:** Participating Traffic Management Centers | **Direction:** Inbound | **Interaction:** Data Publication & Command Reception | **Input Key Points:** Native-format traffic data, device statuses. | **Output Key Points:** TMDD-formatted data/acknowledgments. | **SLA Key Points:** Data transmission frequency, command response time.
2.  **System:** C2C Data Collector | **Direction:** Outbound | **Interaction:** Data Provisioning | **Input Key Points:** Query for consolidated data. | **Output Key Points:** Standardized traffic, incident, and device status data. | **SLA Key Points:** Data availability, query performance.
3.  **System:** Web Map Server | **Direction:** Outbound | **Interaction:** Map Data Feed | **Input Key Points:** Requests for geographic data and current conditions. | **Output Key Points:** Map tiles, incident lists, device icons. | **SLA Key Points:** Map refresh rate, user concurrency support.
4.  **System:** Incident GUI Application | **Direction:** Inbound | **Interaction:** Direct Data Input | **Input Key Points:** User-entered incident/lane closure details. | **Output Key Points:** Confirmation of data acceptance. | **SLA Key Points:** Application responsiveness offline/online.
5.  **System:** Remote Control GUI Application | **Direction:** Bi-directional | **Interaction:** Device Command & Control | **Input Key Points:** User credentials, device selection, command parameters. | **Output Key Points:** Command status responses. | **SLA Key Points:** Authentication/authorization check time.
6.  **System:** NCTCOG Geo-Data Warehouse | **Direction:** Inbound (Initial) | **Interaction:** Basemap Data Source | **Input Key Points:** Request for roadway geometry. | **Output Key Points:** Base geographic layers. | **SLA Key Points:** Data currency (periodic updates).

## Acceptance Criteria
**Capability: Real-Time Traffic Display**
*   **Given** the Web Map is loaded and traffic data is flowing from multiple centers,
*   **When** a user views a major highway segment,
*   **Then** the link is color-coded (green/yellow/red) based on current speed data from the repository.
*   **Given** a new incident is entered into the system via the Incident GUI,
*   **When** the Web Map refreshes,
*   **Then** an icon for the incident appears at the correct location on the map.

**Capability: Cross-Jurisdictional Device Control**
*   **Given** an authenticated user of the Remote Control GUI has selected a DMS in another agency's network,
*   **When** the user submits a valid message change command during the accepted timeframe,
*   **Then** the system sends the command and displays a confirmation that the owning center accepted the request.
*   **Given** a user attempts to issue a CCTV command that is unsupported by the target center (e.g., Momentary Pan to Ft. Worth),
*   **When** the command is processed,
*   **Then** the GUI displays a failure status indicating the command type is not supported.

## Non-Functional Metrics
*   **Performance:** The Web Map shall refresh displayed traffic data at least every 5 minutes. The Data Collector shall process and store incoming TMDD messages with sub-second latency under normal load.
*   **Reliability:** The C2C server software shall achieve 99.5% uptime during operational hours. The system shall continue partial operation if connectivity to one participating center is lost.
*   **Security:** All device control commands must be authenticated with a username and password. Communication between major components shall be via defined protocols (TCP/IP) over secured networks.
*   **Compliance:** The system's center-to-center data exchange shall comply with the TMDD standard and use DATEX/ASN encoding.
*   **Observability:** The system must log all device control commands and their outcomes. In test mode, detailed activity logging for debugging shall be available.

## Milestones and Release Strategy
1.  Finalize and baseline SRS (Version 3.0).
2.  Complete detailed design for core C2C infrastructure and interfaces to initial centers (TxDOT TMCs).
3.  Develop and unit test core Data Collector, Data Transmission, and Web Map components.
4.  Integrate and test with initial participating centers (Dallas and Ft. Worth TxDOT TMCs).
5.  Develop, test, and deploy the Incident GUI and Remote Control GUI applications.
6.  Pilot deployment and operational acceptance with a subset of device types (e.g., DMS, CCTV, incidents) before full rollout.

## Risk List and Mitigation Strategies
1.  **Risk:** Participating centers have heterogeneous and legacy systems, making interface development complex.
    *   **Mitigation:** Use the "building block" approach with configurable adapters to translate between native formats and the TMDD standard.
2.  **Risk:** Network latency or outages could delay critical device control commands.
    *   **Mitigation:** Implement command timeframes and clear status feedback to operators; design for graceful degradation.
3.  **Risk:** Evolving ITS standards (TMDD) may change after system deployment.
    *   **Mitigation:** Isolate standard-specific encoding/decoding logic to facilitate future updates.
4.  **Risk:** Associating transit data (e.g., bus stops) with roadway network links is configurationally complex and prone to inconsistency.
    *   **Mitigation:** Clearly document the challenge and implement robust configuration management tools and validation checks.
5.  **Risk:** Security of remote device commands over public networks (Internet).
    *   **Mitigation:** Require authentication for all commands and rely on network-level security (firewalls, VPNs) as part of deployment.
6.  **Risk:** Insufficient processing capacity for region-wide real-time data.
    *   **Mitigation:** Design for scalability using multiple instances of building blocks and performance testing with projected data volumes.

## Undecided Issues and Responsible Parties
1.  The specific speed thresholds (in MPH) for color-coding links on the Web Map (Green/Yellow/Red). *(Responsible: NCTCOG Software Task Force)*
2.  The definitive list of days and times (command timeframes) each center will accept remote control commands for each device type. *(Responsible: Individual Participating Centers)*
3.  Resolution strategy for inconsistencies between roadway network links (managed by one center) and associated transit data links (managed by another). *(Responsible: NCTCOG & Affected Agency Architects)*
4.  Specific firewall and gateway configuration details to allow the Remote Control GUI to communicate from the public internet to the C2C infrastructure. *(Responsible: System Integrator & Agency IT)*