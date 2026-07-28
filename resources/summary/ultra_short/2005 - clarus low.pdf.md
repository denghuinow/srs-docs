**Purpose & Scope**
The Clarus system is a nationwide initiative to collect, quality-check, and disseminate surface transportation environmental data (atmospheric, pavement, and hydrologic) from across North America. It acts as a central "network of networks" to enhance data coverage and utility for transportation agencies and weather services. The system itself does not create value-added weather products or decision support tools; those are separate initiative components. It also does not directly archive climatological data.

**Product Background / Positioning**
Clarus is positioned as an intermediary data management layer between autonomous data collection networks (e.g., state DOT sensor systems) and service providers (e.g., weather forecasters). It integrates with existing systems by accepting data from various collectors and providing quality-controlled data back to providers and contributors. Its success is dependent on participation from multiple data providers and consumers.

**Core Functional Overview**
1.  Collect environmental data from diverse sources (ESS, vehicles, railways, images) via multiple standard and native interfaces.
2.  Apply automated quality checking (QC) algorithms to incoming data and attach quality flags.
3.  Allow manual review and flagging of data quality by authorized personnel.
4.  Store qualified data and associated metadata.
5.  Disseminate quality-checked data and metadata to authorized users and subscribers in response to queries or schedules.
6.  Manage system configuration, user security, data sharing rules, and collection/QC schedules.

**Key Users & Usage Scenarios**
*   **Data Contributors:** Federal/state/local agencies, rail/transit operators who provide sensor data. They can receive quality feedback on their data.
*   **Service Providers:** Public/private weather service providers who use Clarus data to create forecasts and value-added products.
*   **System Administrators & Quality Managers:** Personnel who configure the system, manage user access, and perform manual quality reviews.
*   **Typical Scenario:** A state DOT's sensor data is automatically collected, run through spatial and range checks, flagged, and then made available within minutes for a private weather company to ingest into its forecast model.

**Major External Interfaces**
*   **Data Input Interfaces:** Interfaces to collect data from Environmental Sensor Stations (ESS), RWIS databases, vehicles, and other collectors. Supports multiple protocols (e.g., NTCIP 1204, XML, CSV).
*   **Data Output Interfaces:** Interfaces for service providers and contributors to query and subscribe to data and metadata. Uses standard Internet protocols.
*   **Administrative Interface:** A user interface for system configuration, security management, and manual quality control.

**Key Non-functional Requirements**
*   **Performance:** Must publish new data within 20 minutes of receipt. Must respond to data queries within 1 minute and metadata queries within 5 minutes. Must support 600 concurrent users and 300 simultaneous data requests.
*   **Reliability/Availability:** The operational program must maintain 24x7 continuous system availability with redundant hardware and communications.
*   **Capacity:** Must support 470 million current observations in its dynamic cache and maintain data for at least 7 days.
*   **Security:** Must manage user privileges and restrict data publication based on source, adhering to data sharing agreements and federal IT security requirements.
*   **Maintainability:** System must be modular, use industry-standard interfaces, and allow new observation types and QC algorithms to be added.

**Constraints, Assumptions & Dependencies**
*   **Constraints:** System must use open, standards-based architecture and interfaces (e.g., NTCIP 1204 for data definitions). All timestamps must use UTC.
*   **Assumptions:** Data contributors can provide observations with location, timestamp, and source metadata. The system's value depends on broad participation from data providers and consumers.
*   **Dependencies:** Requires established data sharing agreements with each data provider. Relies on the operational program to provide 24x7 support, uninterrupted power, and network management.

**Priorities & Acceptance Approach**
The highest priority ("H" criticality) requirements center on core data pipeline functionality: collection, quality checking, and dissemination with defined performance timeliness. Security, configuration management, and operational reliability are also high priority. Acceptance will be based on verifying that the system meets the specified performance metrics (e.g., 20-minute publication latency), correctly applies quality flags, enforces data sharing rules, and satisfies the capacity and concurrent user loads.