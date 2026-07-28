# Detailed Summary: Clarus Weather System Requirements

## Background and Scope
The Clarus Initiative, sponsored by the Federal Highway Administration (FHWA), aims to create a nationwide system for collecting, quality-controlling, and disseminating surface transportation environmental data (weather, pavement, and hydrologic conditions). Its primary goals are to enhance road safety and mobility, improve weather forecasting, support real-time operational responses, and enable better predictive models. The system will function as a "network of networks," interconnecting autonomous environmental data collection systems. Non-goals include directly archiving large volumes of historical data for climatological research and replacing existing critical operational systems.

## Stakeholders Matrix and Use Cases
*   **Observation System Owners (Federal/State/Local/Private):** Provide raw environmental data from their sensor networks and may receive quality feedback.
*   **Instrument & Platform Suppliers:** Provide sensor technology and may contribute data formats or integration standards.
*   **Direct Data Users (e.g., Agency Contractors):** Retrieve and use quality-controlled environmental data for analysis or reporting.
*   **Surface Transportation Weather Service Providers (STWSP):** Primary consumers who integrate Clarus data with other sources to create value-added weather products and forecasts for transportation.
*   **NOAA / General Weather Service Providers:** Use Clarus data to enhance general-purpose weather forecasting and public advisories.
*   **Research Community:** Access data for studies on meteorology, transportation, and climate.
*   **Climate Data Archives:** May ingest Clarus data for long-term storage and climate trend analysis.

**Main Scenarios:** 1) A State DOT's RWIS automatically submits pavement temperature data. 2) A private weather service provider queries for all atmospheric data in a specific region. 3) The system detects an out-of-range humidity value and flags it. 4) A researcher requests historical data for a specific sensor station.
**Exception Scenarios:** 1) A data provider's submission fails due to an invalid format. 2) A sensor station goes offline, and no data is received. 3) A quality control rule cannot be applied due to missing metadata. 4) A user requests data from a source restricted by a sharing agreement.

## Business Process
**Main Process: Data Ingestion, Quality Control, and Publication**
1.  **Trigger/Input:** Environmental data observations become available from autonomous collector networks.
2.  Acquire data via standard or native interfaces from ESS, vehicles, images, etc.
3.  Validate data includes required metadata (location, timestamp, source, known units).
4.  Apply automated quality control checks and algorithms (range checks, spatial/temporal consistency, historical comparison).
5.  Attach quality flags to observations without modifying original data.
6.  Store qualified data and metadata in the dynamic library.
7.  **Output:** Publish/disseminate data to subscribers (service providers, data collectors) based on queries or subscriptions.
8.  Notify data collectors of quality conditions and log all transactions.

**Key Branch A: Quality Control Override**
1.  System flags data based on automated rules.
2.  Authorized human user reviews the flag.
3.  User decides to override the automated assessment.
4.  System records the override method and updates the quality flag accordingly.

**Key Branch B: New Data Provider Onboarding**
1.  Potential data provider requests permission to submit data.
2.  Clarus program establishes a data sharing agreement.
3.  System administrator configures system to accept data from the approved source.
4.  Provider begins data submission through the standard interface.

## Domain Model
*   **Observation** (required: timestamp(UTC), location(GPS coordinates), source ID, data value, unit; unique: composite key)
*   **Sensor Station / ESS** (required: station ID, location, type; reference: Provider)
*   **Data Provider** (required: provider ID, agreement status; unique: provider ID)
*   **Service Provider / User** (required: user ID, access privileges; unique: user ID)
*   **Quality Flag** (required: flag code, rule applied, timestamp; reference: Observation)
*   **Metadata** (required: for sensor configuration, measurement type, platform details; reference: Sensor Station)
*   **Data Subscription** (required: user ID, query parameters, delivery method; reference: User)
*   **Transaction Log** (required: timestamp, action, user/provider ID, details)

## Interfaces and Integrations
*   **Data Provider Interface (Inbound):** System: Various ESS/RWIS/Vehicle networks. Direction: Into Clarus. Theme: Standardized data acquisition. Input: Environmental observations with metadata. Output: Receipt acknowledgment/error. SLA: Collect data within 5 minutes of availability.
*   **Service Provider Interface (Outbound):** System: STWSP, NOAA, Research systems. Direction: Out of Clarus. Theme: Data query and dissemination. Input: Spatio-temporal queries, subscription requests. Output: Quality-flagged environmental datasets. SLA: Respond to requests within one minute; publish new data within 20 minutes of receipt.
*   **Quality Feedback Interface (Outbound):** System: Data Provider systems. Direction: Out of Clarus. Theme: Notification of data quality conditions. Input: Quality flagging event. Output: Quality alerts/reports. SLA: As part of standard processing.
*   **Administration Interface (Bi-directional):** System: Clarus management console. Direction: User to System. Theme: User, provider, and security management. Input: Configuration changes, access requests. Output: System status, logs. SLA: N/A (internal).
*   **NWS Integration (Inbound):** System: National Weather Service. Direction: Into Clarus. Theme: Acquisition of watches/warnings/advisories. Input: Hazard reports. Output: Stored for dissemination. SLA: Based on NWS publication cycle.

## Acceptance Criteria
**Capability: Ingest and Quality-Check ESS Data**
*   Given a functioning Environmental Sensor Station (ESS) configured to the NTCIP 1204 standard, when it submits a valid observation with complete metadata, then the Clarus system shall accept the data, apply quality control checks, store it with a quality flag, and make it available for dissemination.
*   Given an ESS submission missing location metadata, when the data is received, then the Clarus system shall reject the submission and record a transaction error.

**Capability: Provide Data to Service Providers**
*   Given a registered Service Provider with a valid subscription for pavement data in Kansas, when they query the Clarus system, then they shall receive all relevant, quality-flagged pavement observations within one minute.
*   Given a request for data from a provider with a restrictive sharing agreement, when the query is executed, then the system shall return only the data permitted under that agreement.

## Non-functional Metrics
*   **Performance:** Support 600 concurrent users and 300 simultaneous data requests; complete automated quality control within 10 seconds of data receipt.
*   **Reliability:** Respond to 95% of all data requests 95% of the time; support automatic recovery from unexpected shutdowns.
*   **Security:** Operate according to OMB A-130 and NIST guidelines; mitigate denial-of-service attacks.
*   **Compliance:** Use UTC timestamps and GPS coordinates; adhere to NTCIP 1204 and ITE TMDD standards where applicable.
*   **Observability:** Log all data transactions; record system operation statistics.

## Milestones and Release Strategy
1.  Finalize and approve high-level system requirements specification.
2.  Complete detailed system design and architecture selection (centralized vs. decentralized).
3.  Develop and test core data acquisition, quality control, and dissemination modules.
4.  Establish initial data sharing agreements with pilot data providers (e.g., select State DOTs).
5.  Deploy initial operational capability (IOC) with a limited set of data providers and consumers.
6.  Full operational deployment and onboarding of additional providers and service providers.

## Risk List and Mitigation Strategies
1.  **Risk:** Low participation from data providers or consumers reduces system value. **Mitigation:** Proactively develop data sharing agreements and demonstrate value to potential users.
2.  **Risk:** Inconsistent or poor-quality metadata from providers hampers quality control. **Mitigation:** Define clear metadata requirements in sharing agreements and provide validation at ingestion.
3.  **Risk:** System cannot handle the anticipated volume or velocity of data. **Mitigation:** Design for scalability and use modular, distributed architecture; conduct load testing.
4.  **Risk:** Evolving sensor technologies create integration challenges. **Mitigation:** Adopt flexible, standards-based data definitions and interfaces.
5.  **Risk:** Security vulnerabilities compromise system integrity. **Mitigation:** Adhere to federal IT security plans and conduct regular security audits.
6.  **Risk:** Legal liability concerns over data accuracy. **Mitigation:** Implement clear data disclaimers and define responsibilities in sharing agreements.
7.  **Risk:** Regional data needs conflict with non-uniform sensor coverage. **Mitigation:** Manage user expectations that data is location-based, not region-uniform.
8.  **Risk:** Project dependencies on external standards development. **Mitigation:** Engage with standards bodies and plan for adaptability.

## Undecided Issues and Responsible Parties
1.  **Specific data dissemination protocols and standards** (Clarus System Designers).
2.  **Detailed quality control algorithms and regional rule sets** (Clarus Program & Meteorological Experts).
3.  **Long-term data archival strategy and partnership with external archives** (FHWA & Clarus Program Management).
4.  **Final architecture selection (centralized vs. federated)** (System Architects).
5.  **Pricing or cost-recovery model for operational sustainability** (FHWA & Program Management).
6.  **Specific mechanisms for integrating vehicle-based sensor data (VII)** (Technical Team & Vehicle Industry Partners).
7.  **Detailed user interface design for the administrative portal** (UI/UX Designers).
8.  **Definitive list of "time-critical" data for prioritization** (Stakeholder Committee).