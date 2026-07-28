# Detailed Summary: Clarus Weather System Design

## Background and Scope
The Clarus Initiative, sponsored by the U.S. Department of Transportation, aims to create a nationwide system for collecting, quality-checking, and disseminating surface transportation weather and road condition observations. Its primary goals are to enhance safety and mobility, support weather forecasting, enable real-time operational responses, and improve atmospheric models. The system will handle atmospheric, pavement, and hydrologic data from various sources, including environmental sensor stations (ESS), vehicles, and rail systems. Non-goals include direct archiving of large historical data volumes and developing value-added decision support tools within this phase.

## Stakeholders Matrix and Use Cases
*   **Federal, State, and Local Agencies (RWIS operators/owners):** Provide and consume pavement-specific data for maintenance and operations decisions.
*   **Transit System Owners/Operators:** Contribute and receive data with emphasis on weather conditions along transit routes.
*   **Rail System Owners/Operators:** Contribute and receive data, focusing on route conditions and weather-induced hazards like frozen switches.
*   **Vehicle Data Contributors (future):** Provide emerging vehicle-based sensor data on weather and pavement conditions.
*   **Surface Transportation Weather Service Providers (STWSP):** Primary consumers; assimilate Clarus data with other sources to generate value-added products for transportation decision-makers.
*   **General Weather Service Providers (e.g., NOAA/NWS):** Consume meteorological and hydrologic components of Clarus data for public and private forecasting.
*   **Research Community:** Use data to improve knowledge and practice in surface transportation weather.
*   **Archival Entities:** Incorporate Clarus data into broader meteorological archives.

**Main Scenarios:** 1) Automated collection and quality checking of ESS data. 2) Service provider querying for qualified environmental data by location and time. 3) Administrator configuring quality checking rules. 4) Contributor receiving quality feedback on their data. 5) Manual override of quality flags by a quality manager. 6) Subscription-based data dissemination triggered by new data or schedule. 7) System watchdog detecting and restarting failed services.
**Exception Scenarios:** 1) Handling invalid or malformed data submissions from collectors.

## Business Process
**Main Process (Data Flow):**
1.  **Trigger/Input:** Scheduled request or data push from a contributor/collector.
2.  **Collector Services (CS)** retrieve environmental data (ED) from various sources (ESS, vehicles, rail).
3.  **CS** transforms ED into a standard internal format and stores it as unqualified data in the Qualified Environmental Data Cache (QEDC).
4.  **Schedule Service (SS)** initiates Quality Checking Services (QChS) based on configuration.
5.  **QChS** applies configured algorithms (range, spatial, temporal checks) to the data in QEDC, appending quality flags.
6.  **Qualified Environmental Data Services (QEDS)** fulfill requests or subscriptions by retrieving quality-checked data from QEDC.
7.  **QEDS** formats the data according to the requester's specification (e.g., netCDF, CSV).
8.  **Output:** Dissemination of qualified environmental data (QED) to service providers and other authorized users.

**Key Branch A (Configuration & Administration):**
1.  **Trigger:** Administrator action via Configuration & Administration User Interface (CAUI).
2.  **CAUI** sends requests to the Configuration & Administration Service (CAS).
3.  **CAS** manages system state, updates quality checking rules, metadata, and data sharing restrictions.
4.  **Output:** Updated configuration persisted and distributed to relevant services (QChS, CS, QEDS).

**Key Branch B (Manual Quality Intervention):**
1.  **Trigger:** Quality manager review via CAUI.
2.  **CAUI** allows application of manual quality flags to specific datasets or time ranges.
3.  **CAS** records manual flags and updates the QEDC.
4.  **Output:** Manually flagged data influencing subsequent quality assessments and dissemination.

## Domain Model (Key Entities)
*   **Observation:** Core entity storing a measured environmental value. *Fields:* Timestamp (required), Value (required), Quality Flag, Observation Type (reference), Station ID (reference).
*   **Station/Sensor:** Represents a data collection point. *Fields:* Station ID (unique), Geographic Coordinates (lat/lon/elev, required), Owner, Equipment List.
*   **Contributor:** Organization that provides data. *Fields:* Contributor ID (unique), Contact Info, Data Sharing Agreement Rules.
*   **Collector:** System or interface that gathers data from stations for submission. *Fields:* Collector ID (unique), Type, Data Format, Contributor ID (reference).
*   **Quality Checking Rule:** Defines a test to be applied. *Fields:* Rule ID (unique), Algorithm, Parameters, Applicable Observation Types.
*   **Subscription:** A standing request for data. *Fields:* Subscription ID (unique), Query Parameters, Delivery Format, Trigger (schedule/change), Recipient.
*   **Environmental Metadata:** Data describing stations, sensors, and contributors. *Fields:* Metadata ID, Type, Content, Valid Period.
*   **System Log:** Record of transactions and events. *Fields:* Log ID, Timestamp, Service, Event Type, Details.

## Interfaces and Integrations
*   **Collector Interface (Input):** System: Various ESS, RWIS databases, vehicle systems. Direction: Inbound. Theme: Pull or push of raw environmental data. Input: Data in native formats (NTCIP 1204, CSV, XML, CMML). Output: Internal standardized data format. SLA: Minimize acquisition latency; handle submission errors.
*   **Service Provider Interface (Output):** System: Weather service providers, researchers. Direction: Outbound. Theme: Query/response and subscription-based dissemination of qualified data. Input: Queries (spatial, temporal, by source). Output: Formatted data (netCDF, HDF, CSV). SLA: Respond to queries within 1 minute; publish new data within 20 minutes of receipt.
*   **Administration Interface (Human):** System: CAUI (Web-based). Direction: Bi-directional. Theme: System configuration, metadata management, manual quality control. Input: Configuration changes, manual flags. Output: Configuration status, logs, statistics. SLA: Support administrative workflows.
*   **Metadata Service Interface (Output):** System: External users/systems. Direction: Outbound. Theme: Provision of station, sensor, and contributor metadata. Input: Metadata queries. Output: Formatted metadata. SLA: Respond to requests within 5 minutes.

## Acceptance Criteria (Examples)
*   **Capability: Data Collection and Quality Flagging.**
    *   Given an ESS collector is configured and operational, when it pushes new observation data, then the data shall be stored in the QEDC with an initial "unqualified" flag within 5 minutes.
    *   Given new unqualified data is in the QEDC, when the scheduled QChS runs, then quality flags shall be applied and the data status updated to "qualified" within 10 seconds.
*   **Capability: Data Dissemination.**
    *   Given a service provider submits a spatial query for the last hour's temperature data, then QEDS shall return the qualified dataset in the requested format within 1 minute.
    *   Given a subscription for precipitation data when quality flag changes, when a station's precipitation observation is flagged as "failed", then a notification with the relevant data shall be sent to the subscriber.
*   **Capability: System Management.**
    *   Given an administrator applies a manual "failed" flag to a sensor's dataset, then all subsequent queries for that sensor's data shall reflect the manual flag.

## Non-Functional Metrics
*   **Performance:** Support 600 concurrent users and 300 simultaneous data requests. Publish data at 3x the collection rate.
*   **Reliability:** Achieve 95% uptime for responding to data requests. Automatically recover from unexpected service shutdowns.
*   **Security:** Operate according to OMB A-130, NIST, and U.S. DOT security guidelines. Mitigate denial-of-service attacks.
*   **Compliance:** Use NTCIP 1204 and ITE TMDD standards for data definitions. Employ standard Internet protocols.
*   **Observability:** Log all data transactions and system operations. Record statistics for operational reporting.

## Milestones and Release Strategy
1.  Finalize Detailed System Requirements Specification (This Document).
2.  Complete System Design Document (SDD) based on requirements.
3.  Develop and unit test core system components (CS, QChS, QEDS, CAS).
4.  Integrate components and conduct system testing in a designated test environment.
5.  Deploy proof-of-concept system with a limited set of contributors and service providers.
6.  Evaluate proof-of-concept, gather feedback, and plan for operational deployment.

## Risk List and Mitigation Strategies
1.  **Risk:** Low participation from data contributors or consumers reduces system value. **Mitigation:** Proactive outreach and demonstration of benefits; establish clear data sharing agreements.
2.  **Risk:** Inconsistent data quality or metadata (location, timestamp) from contributors. **Mitigation:** Implement robust validation in Collector Services; provide clear data submission standards and feedback.
3.  **Risk:** System cannot scale to handle projected data volumes or user loads. **Mitigation:** Design for distributed, modular architecture; conduct load testing during development.
4.  **Risk:** Quality checking algorithms produce excessive false positives/negatives. **Mitigation:** Use configurable, tunable rules; include manual override capability; iterative refinement based on operational feedback.
5.  **Risk:** Complexities in integrating diverse data formats and protocols. **Mitigation:** Develop extensible Collector Services; prioritize industry-standard formats.
6.  **Risk:** Security vulnerabilities exposing system or data. **Mitigation:** Adhere to federal IT security plans from project inception; regular security audits.
7.  **Risk:** Unclear long-term operational funding and sustainability. **Mitigation:** Develop a sustainable business model as part of the Clarus program planning.
8.  **Risk:** International data sharing agreements (Canada, Mexico) are complex. **Mitigation:** Engage U.S. Department of State early to facilitate agreement processes.

## Undecided Issues and Responsible Parties
1.  **Issue:** Final selection of specific quality checking algorithms and their parameter thresholds. **Responsible:** Clarus Initiative Technical Working Group.
2.  **Issue:** Detailed specification of the "Clarus standard interface" for data submission. **Responsible:** System Design Team.
3.  **Issue:** Policies for long-term data retention beyond the 7-day dynamic cache. **Responsible:** Clarus Initiative Management Team.
4.  **Issue:** Specific mechanisms and formats for providing quality feedback statistics to contributors. **Responsible:** Clarus Program Operations Team.
5.  **Issue:** Prioritization of which new data types (e.g., from VII, cameras) to integrate first. **Responsible:** Clarus Initiative Coordinating Committee.
6.  **Issue:** Detailed disaster recovery and business continuity procedures. **Responsible:** System Design Team & Operations Team.
7.  **Issue:** Fee structure (if any) for different classes of service providers or users. **Responsible:** Clarus Initiative Management Team.
8.  **Issue:** Final governance model for the operational Clarus program. **Responsible:** U.S. DOT FHWA.