# Short Summary: Clarus Weather System Requirements

## Background and Objectives
The Clarus Initiative, sponsored by the Federal Highway Administration (FHWA), aims to create a nationwide system for collecting, quality-controlling, and disseminating surface transportation environmental data (weather, pavement, and hydrologic conditions). Its primary objectives are to enhance road safety and mobility, improve weather forecasting, support real-time operational responses, and enable better atmospheric modeling near the Earth's surface.

## In Scope
- Collecting, quality controlling, and disseminating environmental data from diverse sources including fixed/mobile sensors, vehicles, and manual reports.
- Implementing continuous quality control processes with automated checks and human override capabilities.
- Providing a standardized interface for data exchange, adhering to NTCIP ESS 1204 and other relevant standards.
- Supporting data queries by location, timestamp, quality, and source for service providers and other users.
- Operating as a 24/7 system with redundancy, security measures, and scalability across North America.

## Out of Scope
- Direct archiving of large volumes of historical environmental data for climatological research.
- Development of value-added decision support tools (these are a separate component of the Clarus Initiative).
- Assuming responsibility for the accuracy of data provided by contributors.
- Defining or enforcing regional boundaries for data coverage.
- Creating proprietary database tools beyond standard interfaces and management utilities.

## Stakeholders and Core Use Cases
**Stakeholders:**
- **Observation System Owners:** Federal, state, local, and private institutions that operate sensor networks and provide raw data.
- **Instrument/Platform Suppliers:** Entities that manufacture and supply environmental sensing equipment.
- **Direct Data Users:** System owners and their contractors who use quality-controlled data for operations.
- **Surface Transportation Weather Service Providers (STWSP):** Public and private entities that create value-added weather products for transportation.
- **NOAA/General Weather Service Providers:** Organizations that use data for public forecasting and broader meteorological services.
- **Research Community:** Academics and researchers studying surface transportation weather.
- **Climate Data Archives:** Entities interested in long-term environmental data storage.

**Core Use Cases:**
1. As a **State DOT maintenance engineer**, I want to receive quality flags on my sensor data so that I can identify and correct faulty equipment.
2. As a **Surface Transportation Weather Service Provider**, I want to query and subscribe to specific, quality-controlled environmental datasets so that I can generate accurate, localized forecasts for road conditions.
3. As a **Rail system operator**, I want to access pavement temperature and weather data along rail corridors so that I can anticipate and mitigate issues like frozen switches.
4. As an **Observation System Owner**, I want to submit data from my Environmental Sensor Stations (ESS) via a standard interface so that my data can be integrated into the national Clarus network.
5. As a **Research Scientist**, I want to access historical and real-time, quality-flagged atmospheric data so that I can develop improved boundary-layer weather models.
6. As a **System Administrator**, I want to manage user privileges and data access permissions so that I can enforce data sharing agreements and maintain system security.

## Success Metrics
- System responds to 95% of all data requests 95% of the time.
- New data is published within twenty minutes of receipt from providers.
- Automated quality control checks are completed within ten seconds of data receipt.

## Major Constraints
- The system must use non-proprietary, standards-based architecture and interfaces (e.g., NTCIP, ITS standards).
- Data ownership and dissemination rights are governed by agreements with providers, requiring flexible access controls.
- System must handle a high volume of concurrent users (600) and data points (supporting 470 million current observations).
- All data must include precise location (GPS coordinates to 50 feet) and time (UTC) metadata.
- The system must be hosted on redundant hardware and operate continuously (24/7).

## Undecided Issues
- The specific regional boundaries for applying certain quality control rules.
- The final standard interface protocol for data submission and retrieval.
- The long-term strategy and responsibility for archiving climatological data.
- The prioritization scheme for handling time-critical data versus standard data streams.
- The detailed implementation of security groups and privilege management.