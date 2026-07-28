# Short Summary: Clarus Weather System Design – Detailed System Requirements Specification

## Background and Objectives
The Clarus Initiative, sponsored by the U.S. Department of Transportation, aims to create a nationwide system for collecting, quality-checking, and disseminating surface transportation weather and road condition observations. Its primary objectives are to enhance safety and mobility, maximize investments in environmental sensor stations, improve weather forecasting, and support real-time operational responses to weather.

## In Scope
- Collection, quality checking, and dissemination of environmental data (atmospheric, pavement, and hydrologic data as defined by NTCIP 1204).
- Implementation of automated and manual quality checking processes with configurable rules.
- Support for data acquisition from diverse sources including in-situ sensors, vehicles, railways, and remote sensing.
- Management of environmental metadata and data sharing agreements.
- Provision of a user interface for system administration and quality management.

## Out of Scope
- Development of value-added decision support tools (these are part of the broader Clarus Initiative but not this system).
- Long-term archiving of environmental data beyond a dynamic library (e.g., for climatological research).
- Direct replacement of existing operational systems; Clarus is an augmentation.
- Critical national security missions (security follows OMB Circular A-130).
- Definition of specific regional boundaries for data presentation; data is geo-referenced.

## Stakeholders and Core Use Cases
**Stakeholders:**
- **Observation System Owners:** Federal, state, local, and private institutions that provide data.
- **Instrument Suppliers:** Companies providing sensor and platform technology.
- **Direct Data Users:** System owners and their contractors who consume raw or quality-checked data.
- **Surface Transportation Weather Service Providers:** Entities creating value-added weather products for transportation.
- **NOAA & General Weather Service Providers:** Organizations using data for public forecasting and other weather services.
- **Research Community:** Academics and researchers improving transportation weather knowledge.

**Core Use Cases:**
1. As a **data contributor**, I want to submit environmental observations so that they can be quality-checked and shared under agreed terms.
2. As a **quality manager**, I want to manually flag data quality issues so that erroneous observations are marked.
3. As a **service provider**, I want to query and subscribe to specific, quality-checked environmental data so that I can create accurate forecasts.
4. As a **system administrator**, I want to configure quality rules and manage user access so that the system operates securely and effectively.
5. As a **maintenance personnel**, I want to access current pavement conditions so that I can plan treatments.
6. As a **research scientist**, I want to retrieve historical quality-checked data so that I can validate new models.

## Success Metrics
- Publish new quality-checked environmental data within 20 minutes of receipt.
- Respond to data queries within 1 minute and metadata queries within 5 minutes.
- Achieve 95% system availability to handle 600 concurrent users and 300 simultaneous data requests.

## Major Constraints
- System must use open, standards-based architecture and interfaces (e.g., NTCIP 1204, TMDD).
- Data dissemination must adhere to contributor-defined sharing agreements.
- All timestamps must use Coordinated Universal Time (UTC).
- System must support deployment across multiple physical hosts for scalability and redundancy.
- Must operate continuously (24x7) with high reliability and security as per federal IT guidelines.

## Undecided Issues
- Specific protocols for the "Clarus standard interface" for data acceptance.
- Final set of quality checking algorithms and their exact thresholds.
- Long-term data retention and archival strategy beyond the 7-day dynamic library.
- Mechanisms for integrating future vehicle-based sensor data (e.g., from VII).
- Detailed regional definitions for quality rule application.