**Purpose & Scope**
The Clarus system is a nationwide initiative to collect, quality control, and disseminate surface transportation environmental data (atmospheric, pavement, and hydrologic) from multiple independent networks. It aims to improve road safety, mobility, and weather forecasting. The system itself does not create value-added forecast products or directly archive data for long-term climatological use.

**Product Background / Positioning**
Clarus acts as a centralized "network of networks" or meta-librarian, sitting between autonomous data collection systems (e.g., state DOT sensor networks) and service providers (e.g., weather forecasters). It consolidates data from disparate sources to provide a single, quality-controlled data resource without replacing the functions of the contributing systems.

**Core Functional Overview**
1.  Collect environmental observations from a wide variety of fixed and mobile sources, including road/rail sensors, vehicles, and manual reports.
2.  Perform continuous, automated quality control on all incoming data, applying configurable rules and generating quality flags.
3.  Disseminate quality-controlled data and metadata to authorized service providers and data consumers.
4.  Support queries for data based on location, timestamp, data source, and quality.
5.  Manage user privileges and data access in accordance with data sharing agreements.
6.  Provide feedback on data quality to the original data collectors.
7.  Maintain a dynamic library of recently collected data (at least seven days).

**Key Users & Usage Scenarios**
Primary users are data providers (e.g., state/local transportation agencies, rail operators) and data consumers (e.g., Surface Transportation Weather Service Providers, NOAA, researchers). Providers submit sensor data and receive quality feedback. Consumers query and retrieve consolidated datasets to create forecasts or support operational decisions. System administrators manage access and configurations.

**Major External Interfaces**
The system interfaces with external data collection systems (Environmental Sensor Stations, agency databases) to acquire data and with service providers to disseminate data. Interfaces must support standard Internet protocols and industry data standards (e.g., NTCIP). A user interface is required for system administration.

**Key Non-functional Requirements**
*   Performance: Must collect data within 5 minutes of availability, complete quality checks within 10 seconds of receipt, and publish new data within 20 minutes of receipt. Must support 600 concurrent users and respond to data requests within one minute.
*   Reliability/Availability: Must operate 24x7 with redundant hardware and communications. Must be able to automatically recover from an unexpected shutdown.
*   Security: Must operate according to federal IT security requirements (OMB A-130, NIST guidelines) and mitigate denial-of-service attacks.
*   Capacity: Must be able to handle 470 million current observations and publish data at three times the collection volume rate.
*   Data Standards: Core data types and definitions must align with the NTCIP 1204 standard.

**Constraints, Assumptions & Dependencies**
*   Success depends on participation from multiple data providers and consumers.
*   The system is "open," using non-proprietary, standards-based architecture and interfaces.
*   All location data must use GPS coordinates (to nearest 50 feet); all timestamps must use Coordinated Universal Time (UTC).
*   Data providers retain ownership; FHWA and providers do not guarantee data accuracy.
*   The system does not modify original observations, only appends quality flags.

**Priorities & Acceptance Approach**
High-priority requirements center on core data collection, quality control, and dissemination functions, along with performance, reliability, and security constraints. Acceptance will be based on verifying the system meets the specified functional capabilities and quantitative performance metrics under operational conditions.