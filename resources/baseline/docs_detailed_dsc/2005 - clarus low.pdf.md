# Software Requirements Specification (SRS)
## Clarus Weather System
**Document Version:** 1.0  
**Date:** October 26, 2023  
**Prepared for:** U.S. Department of Transportation, Federal Highway Administration  
**Prepared by:** Clarus Initiative System Design Team  
**Status:** Draft for Review

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the Clarus Weather System. It serves as the authoritative specification for system developers, testers, project managers, and stakeholders, ensuring a common understanding of the system's capabilities, constraints, and behavior.

### 1.2 Scope
The Clarus Weather System is a nationwide data system designed to collect, quality-check, and disseminate surface transportation weather and road condition observations. The system integrates data from diverse sources—including Environmental Sensor Stations (ESS), vehicles, and rail systems—to enhance roadway safety, mobility, and weather forecasting.

**In-Scope:**
*   Automated collection and ingestion of atmospheric, pavement, and hydrologic data.
*   Application of configurable, automated quality checks.
*   Provision of manual quality control override capabilities.
*   Dissemination of quality-flagged data to authorized consumers via query and subscription.
*   Management of system configuration, metadata, and data sharing rules.
*   Operational monitoring and logging.

**Out-of-Scope (Non-Goals):**
*   Long-term archival of large historical data volumes (beyond a dynamic operational cache).
*   Development of value-added decision support tools or forecast products.
*   Direct control or maintenance of contributor-owned field sensors.
*   Real-time alerting to the traveling public.

### 1.3 Definitions, Acronyms, and Abbreviations

| Term | Definition |
| :--- | :--- |
| **CAS** | Configuration & Administration Service |
| **CAUI** | Configuration & Administration User Interface |
| **CS** | Collector Service(s) |
| **ED** | Environmental Data |
| **ESS** | Environmental Sensor Station |
| **FHWA** | Federal Highway Administration |
| **NTCIP** | National Transportation Communications for ITS Protocol |
| **QChS** | Quality Checking Service(s) |
| **QED** | Qualified Environmental Data |
| **QEDC** | Qualified Environmental Data Cache |
| **QEDS** | Qualified Environmental Data Service(s) |
| **RWIS** | Road Weather Information System |
| **SLA** | Service Level Agreement |
| **SS** | Schedule Service |
| **STWSP** | Surface Transportation Weather Service Provider |
| **U.S. DOT** | United States Department of Transportation |

### 1.4 References
*   OMB Circular A-130, Managing Information as a Strategic Resource
*   NIST Cybersecurity Framework
*   NTCIP 1204: Object Definitions for Environmental Sensor Stations (ESS)
*   ITE TMDD: Traffic Management Data Dictionary

### 1.5 Document Overview
This SRS is organized into sections describing overall product perspective, specific functional requirements, external interfaces, and non-functional characteristics.

## 2. Overall Description

### 2.1 Product Perspective
The Clarus System is a middleware data hub positioned between data contributors (e.g., state DOTs, transit agencies) and data consumers (e.g., weather service providers, researchers). It is a new, independent system that must integrate with numerous existing external systems via defined interfaces.

### 2.2 Stakeholders and User Classes

| User Class | Primary Interest / Role |
| :--- | :--- |
| **Data Contributor** (Agency, Rail, Transit) | Provides raw environmental data; receives quality feedback. |
| **System Administrator** | Configures system parameters, manages users, monitors health. |
| **Quality Manager** | Reviews automated quality flags and applies manual overrides. |
| **Service Provider / Consumer** (STWSP, NOAA, Researcher) | Queries and subscribes to receive quality-checked data. |
| **System Operator** | Monitors performance, manages service restarts, handles failures. |
| **Archival Entity** | Receives bulk data for permanent meteorological archives. |

### 2.3 Operating Environment
*   **Hardware:** To be deployed on scalable, federal-compliant data center infrastructure.
*   **Software:** Component-based services likely deployed on application servers; relational or time-series database for QEDC; web server for CAUI.
*   **Networks:** Operates over standard Internet protocols (HTTP/S, FTP/S). Must comply with U.S. DOT security zones.

### 2.4 Design and Implementation Constraints
1.  **Security:** Must conform to OMB A-130, NIST SP 800-53, and U.S. DOT IT security policies.
2.  **Standards:** Must support data definitions per NTCIP 1204 and ITE TMDD standards.
3.  **Data Formats:** Must ingest data in NTCIP 1204, CSV, XML, and CMML formats. Must disseminate data in netCDF, HDF, and CSV formats.
4.  **Protocols:** Must use standard Internet protocols for all external interfaces.

### 2.5 Assumptions and Dependencies
*   Contributors will provide reasonably accurate metadata (e.g., sensor location).
*   A sustainable funding and governance model for long-term operations will be established.
*   Data sharing agreements with contributors and international partners (Canada, Mexico) will be in place.

## 3. System Features and Requirements

### 3.1 Feature: Data Acquisition and Ingestion
**Description:** The system shall acquire environmental data from various contributors via Collector Services, transform it into a standard internal format, and store it in the cache.

**Requirements:**
*   **REQ-INGEST-001:** The system shall accept data pushes from configured collectors on a schedule or ad-hoc basis.
*   **REQ-INGEST-002:** Collector Services shall transform incoming data from native formats (NTCIP 1204, CSV, XML, CMML) into the defined Clarus internal format.
*   **REQ-INGEST-003:** Upon successful ingestion, data shall be stored in the QEDC with an initial quality flag of "Unqualified."
*   **REQ-INGEST-004:** The system shall reject and log data submissions that are malformed or fail schema validation.
*   **REQ-INGEST-005:** Data shall be stored in the QEDC within 5 minutes of successful receipt from a collector.

### 3.2 Feature: Automated Quality Checking
**Description:** The system shall apply a suite of configurable quality checking algorithms to unqualified data and append appropriate quality flags.

**Requirements:**
*   **REQ-QC-001:** The Schedule Service (SS) shall initiate Quality Checking Services (QChS) based on a configurable schedule (e.g., every 5 minutes).
*   **REQ-QC-002:** QChS shall apply quality checking rules (e.g., range, step, spatial consistency, temporal persistence) as defined in the active configuration.
*   **REQ-QC-003:** Each applied rule shall result in a quality flag (e.g., "Passed", "Failed", "Suspect") being appended to the observation record in the QEDC.
*   **REQ-QC-004:** The system shall update the overall status of an observation to "Qualified" once all applicable automated checks are complete.
*   **REQ-QC-005:** The quality checking process for a batch of data shall complete within 10 seconds of initiation.

### 3.3 Feature: Manual Quality Control
**Description:** Authorized quality managers shall be able to review and manually override automated quality flags.

**Requirements:**
*   **REQ-MQC-001:** The CAUI shall provide a interface for quality managers to query and view data along with its automated quality flags.
*   **REQ-MQC-002:** A quality manager shall be able to apply a manual quality flag (e.g., "Manually Failed", "Manually Approved") to a specific observation, a sensor's dataset, or a dataset for a specific time range.
*   **REQ-QC-003:** Manual flags shall take precedence over automated flags in all subsequent data retrievals and disseminations.
*   **REQ-MQC-004:** All manual overrides shall be logged with the user ID, timestamp, and justification.

### 3.4 Feature: Data Query and Retrieval
**Description:** Authorized consumers shall be able to request qualified environmental data using spatial, temporal, and source-based filters.

**Requirements:**
*   **REQ-QUERY-001:** The QEDS shall provide an interface for consumers to query the QEDC for qualified data.
*   **REQ-QUERY-002:** Query filters shall include geographic bounding box, time range, observation type, station ID, and contributor ID.
*   **REQ-QUERY-003:** QEDS shall format the result set into the consumer's requested standard format (netCDF, HDF, or CSV).
*   **REQ-QUERY-004:** The system shall respond to a standard data query within 1 minute of request receipt.

### 3.5 Feature: Subscription-Based Dissemination
**Description:** Consumers shall be able to establish standing subscriptions to receive data based on a schedule or an event trigger.

**Requirements:**
*   **REQ-SUB-001:** The system shall allow a consumer to create a subscription specifying query parameters, delivery format, trigger (schedule or data change), and recipient endpoint.
*   **REQ-SUB-002:** For schedule-triggered subscriptions, QEDS shall execute the query and disseminate data at the defined interval.
*   **REQ-SUB-003:** For event-triggered subscriptions (e.g., "on new data" or "on quality flag change"), QEDS shall disseminate relevant data within 20 minutes of the triggering event.
*   **REQ-SUB-004:** The system shall provide subscription management capabilities (create, read, update, delete) via the administration interface.

### 3.6 Feature: System Configuration and Administration
**Description:** Administrators shall configure system behavior, manage metadata, and control user access.

**Requirements:**
*   **REQ-ADMIN-001:** The CAS, via the CAUI, shall allow administrators to create, update, and disable quality checking rules and their parameters.
*   **REQ-ADMIN-002:** The system shall allow management of metadata for Stations/Sensors, Contributors, and Collectors.
*   **REQ-ADMIN-003:** The system shall enforce data sharing restrictions based on contributor agreements (e.g., limit data access to specific consumers).
*   **REQ-ADMIN-004:** Configuration changes shall be persisted and distributed to all relevant services (CS, QChS, QEDS) without requiring a full system restart.

### 3.7 Feature: Operational Monitoring and Logging
**Description:** The system shall log transactions and system events to support auditing, debugging, and operational reporting.

**Requirements:**
*   **REQ-LOG-001:** The system shall log all data ingestion transactions, including source, timestamp, volume, and success/failure status.
*   **REQ-LOG-002:** The system shall log all data dissemination transactions, including recipient, query parameters, and volume.
*   **REQ-LOG-003:** The system shall log all configuration changes and manual quality interventions.
*   **REQ-LOG-004:** The system shall record performance and health statistics (e.g., service uptime, request latency, cache size) for operational reporting.
*   **REQ-LOG-005:** A watchdog service shall detect failed core services (CS, QChS, QEDS, CAS) and attempt automatic restart.

## 4. External Interface Requirements

### 4.1 User Interfaces
*   **CAUI (Configuration & Administration User Interface):** A secure, role-based web application for administrators and quality managers. It shall provide forms, dashboards, and data viewers for all configuration, monitoring, and manual QC tasks.

### 4.2 Hardware Interfaces
None specified. Hardware dependencies are abstracted by the operating environment.

### 4.3 Software Interfaces
*   **Collector Interface (Input):** API/service endpoint accepting data in NTCIP 1204, CSV, XML, or CMML formats over HTTPS or FTPS. Must handle authentication/authorization of contributors.
*   **Service Provider Interface (Output):** API/service endpoint for query/response (RESTful/SOAP) and subscription callbacks (webhook). Returns data in netCDF, HDF, or CSV.
*   **Metadata Service Interface (Output):** API endpoint for querying static metadata about stations, sensors, and contributors. Responds within 5 minutes.

### 4.4 Communications Interfaces
All external communications shall use encrypted channels (TLS 1.2+). Standard HTTP/S and FTP/S protocols will be employed.

## 5. Non-Functional Requirements

### 5.1 Performance Requirements
*   The system shall support **600 concurrent users** of the CAUI.
*   The system shall handle **300 simultaneous data requests/queries**.
*   The data dissemination throughput shall be capable of publishing data at **three times** the maximum anticipated collection rate.
*   Query response time: < 1 minute (REQ-QUERY-004).
*   Data publication latency (event trigger): < 20 minutes (REQ-SUB-003).

### 5.2 Reliability and Availability
*   The system shall achieve **95% uptime** for core data request/response functionality.
*   The system shall automatically recover from unexpected service shutdowns (REQ-LOG-005).

### 5.3 Security Requirements
*   The system shall comply with all applicable U.S. Federal security guidelines (OMB A-130, NIST).
*   The system shall implement role-based access control (RBAC) for all functions.
*   The system shall include mechanisms to mitigate denial-of-service (DoS) attacks.

### 5.4 Compliance Requirements
*   Data definitions shall align with **NTCIP 1204** and **ITE TMDD** standards.
*   All external interfaces shall use **standard Internet protocols**.

### 5.5 Observability Requirements
*   All system transactions and state changes shall be logged (See REQ-LOG-001 to 005).
*   System health and performance metrics shall be exposed for monitoring tools.

## 6. Appendices

### 6.1 Acceptance Criteria (Detailed Examples)

| ID | Scenario | Acceptance Test |
| :--- | :--- | :--- |
| **AC-DC-01** | Data Collection | Given a configured ESS collector, when it pushes new data, then the data is stored in the QEDC with an "Unqualified" flag within 5 minutes. |
| **AC-QC-01** | Quality Checking | Given unqualified data in the QEDC, when the QChS runs, then quality flags are applied and status is "Qualified" within 10 seconds. |
| **AC-DISS-01** | Data Query | Given a spatial query for the last hour's temperature, then QEDS returns the qualified dataset in the requested format within 1 minute. |
| **AC-MGMT-01** | Manual Override | Given an administrator applies a manual "Failed" flag, then all subsequent queries for that data reflect the manual flag. |

### 6.2 Domain Model (Entity-Attribute Summary)

```yaml
Observation:
  - observation_id (PK)
  - timestamp (Required)
  - value (Required)
  - quality_flags (Array: automated, manual)
  - observation_type (FK)
  - station_id (FK)

Station:
  - station_id (PK)
  - latitude (Required)
  - longitude (Required)
  - elevation
  - owner_contributor_id (FK)

Contributor:
  - contributor_id (PK)
  - name
  - contact_info
  - data_sharing_agreement_id

QualityCheckingRule:
  - rule_id (PK)
  - algorithm_name
  - parameters (JSON)
  - applicable_observation_types (Array)
```

### 6.3 Open Issues and Decisions Pending
1.  **Issue:** Final selection and parameter tuning of quality checking algorithms.
    *   **Responsible:** Clarus Technical Working Group.
2.  **Issue:** Specification of the "Clarus standard interface" for data submission.
    *   **Responsible:** System Design Team.
3.  **Issue:** Long-term data retention policy beyond the 7-day operational cache.
    *   **Responsible:** Clarus Management Team.
4.  **Issue:** Detailed disaster recovery and business continuity plan.
    *   **Responsible:** System Design & Operations Team.

---
*This document is subject to change upon review and approval by the Clarus Initiative stakeholders.*