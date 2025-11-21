Purpose & Scope: Clarus is a U.S. DOT initiative to create a network for collecting, quality checking, and sharing surface transportation environmental data (atmospheric, pavement, and hydrologic). It provides a one-stop portal for environmental observations, enables continuous quality checking with feedback to data providers, and supports integration with existing weather data sources. The system does not handle long-term data archiving or replace existing operational systems.

Product Background / Positioning: Clarus positions itself as the next step in integrating surface transportation weather observations with broader weather community efforts. It serves as a network connecting independent data collection systems to enhance data coverage, improve meteorological support services, and provide guidance to data source owners regarding data quality. The system is designed to be open and standards-based, using non-proprietary interfaces.

Core Functional Overview: 
- Collect environmental data from diverse sources (ESS, vehicles, cameras)
- Apply automated and manual quality checking with flags
- Publish data with quality flags through standardized interfaces
- Manage data sharing agreements between providers and consumers
- Support spatial and temporal queries for data retrieval
- Disseminate data within 20 minutes of receipt
- Handle 300 simultaneous data requests

Key Users & Usage Scenarios: Primary users include state DOTs, weather service providers (NOAA, private), research organizations, and transportation operators. Key usage scenarios involve real-time data access for operational decisions, quality checking feedback to data providers, integration with forecasting models, and support for value-added weather products. Data sharing agreements determine access rights for each user group.

Major External Interfaces: Interfaces with environmental sensor stations (using NTCIP 1204 standard), weather service providers (e.g., ASOS/AWOS), and data contributors. Uses standard Internet protocols for data dissemination. Data must include location, timestamp, and source metadata with UTC time reference.

Key Non-functional Requirements: Must publish new data within 20 minutes of receipt, respond to data requests within one minute, handle 300 simultaneous requests, complete automated quality checks within 10 seconds, support 470 million current observations, and maintain 24x7 operations. System must use non-proprietary interfaces and be standards-based.

Constraints, Assumptions & Dependencies: System is not critical to existing operations (not a national security mission). Requires data sharing agreements for all data providers. Data must follow NTCIP 1204 standards. Timestamps must use UTC. System must support data from across North America (US, Canada, Mexico). Data must include location, timestamp, and source metadata.

Priorities & Acceptance Approach: Top priority is timeliness (20-minute data publication, 1-minute response time). Secondary priority is quality checking (10-second automated checks). Acceptance requires meeting performance metrics and implementing standardized interfaces. System must be available 24x7 with reliable recovery from failures.