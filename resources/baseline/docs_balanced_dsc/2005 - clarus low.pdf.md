# Software Requirements Specification (SRS)
## Clarus Weather System
**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Clarus Weather System. The system is a nationwide initiative to collect, quality-check, and disseminate surface transportation environmental data. This SRS serves as a contract between the Clarus Initiative Management Team and the development team, providing a complete description of the system's intended behavior.

#### 1.2 Document Conventions
*   Requirements are uniquely identified using the format `[FR-XXX]` for Functional Requirements and `[NFR-XXX]` for Non-Functional Requirements.
*   **Bold** text indicates key terms or system components.
*   *Italic* text is used for emphasis.

#### 1.3 Project Scope
The Clarus System will operate as a "network of networks," integrating environmental data (weather, pavement, water conditions) from autonomous providers (e.g., State DOTs, mobile fleets) across North America. Its core functions are:
1.  **Ingestion:** Collecting raw data from heterogeneous sources via standardized interfaces.
2.  **Quality Control:** Applying automated and manual quality checks to all incoming observations.
3.  **Storage:** Caching qualified data in a readily accessible repository.
4.  **Dissemination:** Providing secure, role-based access to quality-flagged data via queries and subscriptions.
5.  **Management:** Configuring system behavior, rules, and data sharing agreements.

**Out of Scope:**
*   Creation of commercial weather forecast products.
*   Direct control of contributor-owned sensor hardware.
*   Long-term archival and deep historical data warehousing (subject to Undecided Issues).

#### 1.4 References
*   NTCIP 1204: Environmental Sensor Stations (ESS) Standard
*   Clarus Initiative Concept of Operations (ConOps)
*   Data Sharing Agreement Templates

### 2. Overall Description

#### 2.1 Product Perspective
The Clarus System is a standalone, server-based application that interacts with external data providers and consumers. It will include web-based administrative portals and machine-to-machine (M2M) Application Programming Interfaces (APIs).

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Observation System Owner** (e.g., State DOT) | Provides data; technical staff; interested in data quality feedback. | Automated quality reports, reliable data submission interface. |
| **Service Provider** (e.g., Weather Company) | Consumer of bulk data; uses data to create value-added products. | High-volume, reliable data feeds; flexible query/subscription APIs. |
| **Transportation Operator** (e.g., Maintenance Manager) | Operational decision-maker; uses a portal or simple API. | Real-time, easy-to-understand visualizations of conditions. |
| **Research Community** | Academic or government researcher; needs historical datasets. | Access to historical, quality-flagged data for analysis. |
| **System Administrator** | IT professional; manages system health and configuration. | Tools to monitor, configure, and restart system components. |
| **Quality Manager** | Domain expert (e.g., meteorologist); ensures data usability. | Ability to review and manually override automated quality flags. |

#### 2.3 Operating Environment
*   **Hardware:** To be deployed on scalable, fault-tolerant server infrastructure (cloud or on-premises data center).
*   **Software:** Will run on a modern, supported operating system (e.g., Linux). Core components will be containerized for modular deployment.
*   **Networks:** Must operate over the public internet, interfacing with contributor networks across North America.

#### 2.4 Design and Implementation Constraints
1.  **Standards Compliance:** Must support data interchange formats including, but not limited to, netCDF and CSV, and protocols per NTCIP 1204 where applicable.
2.  **Modular Architecture:** System must be built as discrete, loosely coupled services to satisfy maintainability requirements.
3.  **Security:** Must comply with federal IT security guidelines (e.g., FISMA, NIST SP 800-53).

#### 2.5 Assumptions and Dependencies
*   **Assumption:** Data providers will adhere to agreed-upon standards for metadata (location, timestamp, sensor ID).
*   **Dependency:** Finalization of Clarus Data Sharing Agreements is a prerequisite for full system deployment.
*   **Dependency:** The Clarus Initiative Management Team will provide ongoing policy and technical guidance.

### 3. System Features and Requirements

#### 3.1 Feature: Data Ingestion & Normalization
**Description:** The system shall collect environmental data from registered contributors on a scheduled or on-demand basis and convert it into a standard internal format.

**Requirements:**
*   `[FR-101]` The system shall provide a configurable **Collector Service** for each registered data contributor.
*   `[FR-102]` Each Collector Service shall be schedulable (e.g., poll every 5 minutes) or triggerable on-demand.
*   `[FR-103]` The Collector Service shall transform ingested data from its native format into the standard internal Clarus data model.
*   `[FR-104]` Upon successful ingestion and transformation, the system shall store the raw observation value and all source metadata in the **Qualified Environmental Data Cache (QEDC)**.

#### 3.2 Feature: Automated Quality Checking
**Description:** The system shall apply a suite of configurable quality checking algorithms to all new observations and assign appropriate quality flags.

**Requirements:**
*   `[FR-201]` The **Quality Checking Service (QChS)** shall process new data records placed in the QEDC.
*   `[FR-202]` The QChS shall apply rules configurable by a Quality Manager, including but not limited to:
    *   `[FR-202.1]` **Range Test:** Flag data outside predefined min/max values for a parameter.
    *   `[FR-202.2]` **Step Test:** Flag implausibly large changes between consecutive observations.
    *   `[FR-202.3]` **Spatial Consistency Test:** Compare observation to nearby stations.
*   `[FR-203]` The system shall store quality flags (e.g., "Pass," "Fail," "Suspect") in the QEDC linked to the original observation without altering the original value.
*   `[FR-204]` The system shall log all quality check actions and results for audit purposes.

#### 3.3 Feature: Manual Quality Override
**Description:** Authorized Quality Managers shall be able to review and manually override system-assigned quality flags.

**Requirements:**
*   `[FR-301]` The system shall provide a web interface for Quality Managers to query observations by station, time, and parameter.
*   `[FR-302]` The interface shall display the original observation value, all automated quality flags, and the source metadata.
*   `[FR-303]` A Quality Manager shall be able to apply a manual override flag (e.g., "Manager Approved," "Manager Rejected") with a required text justification.
*   `[FR-304]` The manual override flag shall take precedence over any automated flag for dissemination purposes.

#### 3.4 Feature: Data Query & Subscription
**Description:** The system shall provide mechanisms for users and applications to retrieve quality-controlled data via direct queries or persistent subscriptions.

**Requirements:**
*   `[FR-401]` The **Qualified Environmental Data Service (QEDS)** shall provide a public API for querying data.
*   `[FR-402]` Query filters shall include: geographic bounding box, time range, parameter type, station ID, and quality flag status.
*   `[FR-403]` The system shall allow authorized users to create persistent **Data Subscriptions**.
*   `[FR-404]` A subscription shall define: data filter parameters, delivery schedule or change-based trigger, and output format (e.g., netCDF, CSV).
*   `[FR-405]` The QEDS shall enforce data sharing restrictions based on the contributor's agreement and the requester's privileges before returning any data.

#### 3.5 Feature: System Administration & Monitoring
**Description:** The system shall provide tools for administrators to configure, monitor, and ensure the health of all system components.

**Requirements:**
*   `[FR-501]` System Administrators shall be able to start, stop, and restart individual system services (Collectors, QChS, QEDS) via a management interface.
*   `[FR-502]` A **Watchdog Service** shall continuously monitor the health of all critical components and automatically restart any that fail.
*   `[FR-503]` Administrators shall be able to configure data collection schedules, quality checking rule parameters, and user access permissions.
*   `[FR-504]` The system shall maintain a comprehensive **System Log** of all major transactions, errors, and administrative actions.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Administrative Portal:** Web-based interface for System Administrators and Quality Managers (see FR-301, FR-501).
*   **Data Portal/Web API:** A basic web interface or API documentation portal for Transportation Operators and Researchers to explore and access data.

#### 4.2 Hardware Interfaces
None specified. The system interfaces with contributor hardware only via network protocols.

#### 4.3 Software Interfaces
*   **Contributor Ingest Interface:** M2M API (e.g., HTTPS, SOAP) or support for standard protocols (e.g., NTCIP) to pull data from provider systems.
*   **Data Dissemination Interface:** RESTful API for queries and subscription management. Support for push delivery via HTTPS POST, SFTP, etc.
*   **Internal Interfaces:** Inter-service communication will use lightweight protocols (e.g., AMQP, REST) within a controlled service mesh.

#### 4.4 Communications Interfaces
All external communications shall occur over secure channels (TLS 1.2+). Authentication for all APIs is required.

### 5. Non-Functional Requirements

#### 5.1 Performance
*   `[NFR-001]` **Data Latency:** The system shall publish new data (ingested, quality-checked, and available for query) within 20 minutes of receipt from the contributor 95% of the time.
*   `[NFR-002]` **Query Response:** The system shall respond to data queries within 1 minute 95% of the time, excluding large historical dataset requests.

#### 5.2 Reliability, Availability, and Maintainability
*   `[NFR-003]` **Availability:** The system shall achieve 99.5% operational availability, excluding scheduled maintenance windows.
*   `[NFR-004]` **Recovery:** The system shall support automatic recovery from unexpected service shutdowns, with core services resuming within 5 minutes of a failure.
*   `[NFR-005]` **Maintainability:** The system shall be designed with modular components, allowing individual services to be updated, replaced, or scaled independently.

#### 5.3 Scalability
*   `[NFR-006]` The architecture shall support data ingestion from sensor networks across North America (estimated 10,000+ stations).
*   `[NFR-007]` The system shall support up to 600 concurrent user/application sessions.

#### 5.4 Security
*   `[NFR-008]` The system shall implement role-based access control (RBAC) for all functions and data access.
*   `[NFR-009]` Data dissemination shall be filtered based on contributor-defined sharing restrictions stored in formal data sharing agreements.
*   `[NFR-010]` All system access shall require authentication. All external data transmissions shall be encrypted in transit.

#### 5.5 Interoperability
*   `[NFR-011]` The system shall ingest and disseminate data using industry-standard formats (e.g., netCDF, CSV) and standard protocols where defined.

### 6. Data Model
The core domain entities and their key attributes are defined below. This is a logical model, not a physical database schema.

```yaml
Observation:
  observation_id: PK
  timestamp: UTC
  station_id: FK -> Station
  parameter_type: String (e.g., "air_temperature")
  value: Float
  unit: String
  quality_flag_auto: String
  quality_flag_manual: String
  manual_override_justification: Text

Station:
  station_id: PK
  name: String
  latitude: Float
  longitude: Float
  elevation: Float
  contributor_id: FK -> Contributor
  pavement_type: String (Optional)

Contributor:
  contributor_id: PK
  organization_name: String
  contact_email: String
  data_sharing_restriction_level: String

QualityCheckingRule:
  rule_id: PK
  parameter_type: String
  algorithm: String (e.g., "RangeTest")
  threshold_values: JSON
  applicable_region: Geometry (Optional)

DataSubscription:
  subscription_id: PK
  requester_id: FK -> User
  query_parameters: JSON
  delivery_trigger: String
  output_format: String
  active: Boolean
```

### 7. Appendices

#### Appendix A: Glossary
*   **QEDC (Qualified Environmental Data Cache):** The primary operational database storing observations and their quality flags.
*   **Quality Flag:** A metadata tag indicating the assessed validity of an observation (e.g., Pass, Fail, Suspect, Manually Overridden).
*   **Contributor:** An organization that provides environmental data to the Clarus System.

#### Appendix B: Undecided Issues (To Be Resolved)
1.  The technical specification and implementation timeline for a long-term **data archiving** system.
2.  Final ratified list of all **standard data interchange formats**.
3.  Geospatial definition files for **regional boundaries** used in quality checking rules.
4.  The complete, detailed specification and default parameters for all **quality checking algorithms**.
5.  The formal operational procedure and criteria for **rejecting data from a contributor** for persistent non-compliance.
6.  Selection and deployment plan for specific **network management and customer service tooling**.

---
*This document is considered the authoritative source for the functional and non-functional requirements of the Clarus Weather System.*