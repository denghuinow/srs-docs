# Software Requirements Specification (SRS)
## Clarus Weather System
### Version 1.0

**Document Status:** Draft  
**Prepared For:** U.S. Department of Transportation, Clarus Initiative  
**Date:** October 26, 2023

---

## 1. Introduction

### 1.1 Purpose
This document defines the detailed software requirements for the Clarus Weather System. It is intended for use by the project stakeholders, including system architects, developers, testers, and project managers, to ensure a common understanding of the system's capabilities, constraints, and interfaces.

### 1.2 Scope
The Clarus Weather System is a nationwide software platform designed to collect, quality-check, and disseminate surface transportation weather and road condition observations. The system serves as a central hub for environmental data, enhancing safety, mobility, and operational decision-making for transportation agencies and service providers.

**In-Scope Elements:**
*   Core data pipeline: ingestion, quality control (automated and manual), and dissemination.
*   Management of environmental metadata and data sharing agreements.
*   Administrative and quality management user interfaces.
*   Support for data from diverse sources (in-situ sensors, vehicles, railways, remote sensing).

**Out-of-Scope Elements:**
*   Development of value-added decision support or forecasting tools.
*   Long-term climatological archiving (beyond a dynamic operational library).
*   Replacement of existing agency operational systems.
*   Definition of presentation-specific regional boundaries.

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **Clarus** | The U.S. DOT initiative to create a national surface transportation weather observing system. |
| **ESS** | Environmental Sensor Station. A fixed installation of sensors measuring atmospheric, pavement, and/or hydrologic conditions. |
| **NTCIP 1204** | National Transportation Communications for ITS Protocol, Object Definitions for Environmental Sensor Stations. The standard data model for ESS data. |
| **TMDD** | Traffic Management Data Dictionary. A standard for transportation data exchange. |
| **QC** | Quality Control / Quality Checking. |
| **UTC** | Coordinated Universal Time. The primary time standard for the system. |
| **VII** | Vehicle Infrastructure Integration. (Referenced as a potential future data source). |
| **OMB A-130** | Office of Management and Budget Circular A-130, governing federal information system security. |

### 1.4 References
1.  NTCIP 1204 v03.15: Environmental Sensor Station (ESS) Objects
2.  TMDD v3.0: Traffic Management Data Dictionary
3.  OMB Circular A-130: Managing Information as a Strategic Resource
4.  Clarus Initiative Concept of Operations (Reference Document)

### 1.5 Overview
The remainder of this SRS is organized as follows:
*   **Section 2:** Overall Description – Provides context, user characteristics, constraints, and assumptions.
*   **Section 3:** Specific Requirements – Details functional, data, external interface, non-functional, and other requirements.
*   **Appendix A:** Undecided Issues – Lists items requiring future resolution.

## 2. Overall Description

### 2.1 Product Perspective
The Clarus Weather System is an independent, augmentative system that interfaces with existing transportation agency systems, sensor networks, and end-user applications. It acts as a middleware layer, standardizing and enriching data for broader consumption.

### 2.2 Product Functions (Summary)
1.  **Data Ingestion:** Accept environmental observations from diverse contributors via standard interfaces.
2.  **Quality Control:** Apply automated, configurable QC rules and enable manual QC flagging.
3.  **Data Management:** Store raw and quality-checked data in a dynamic library with associated metadata and sharing agreements.
4.  **Data Dissemination:** Provide query, subscription, and bulk access to quality-checked data based on user permissions and data agreements.
5.  **System Administration:** Manage users, roles, QC rules, and system configuration.

### 2.3 User Characteristics
| Stakeholder / Actor | Description | Technical Proficiency |
| :--- | :--- | :--- |
| **Data Contributor** | Agency or private entity submitting data. | High. Familiar with data transmission protocols (e.g., NTCIP). |
| **Quality Manager** | User responsible for monitoring and manually overriding QC flags. | Medium. Understands data quality concepts, uses web UI. |
| **Service Provider / Data User** | Consumer of quality-checked data for forecasts or operations. | Medium to High. Uses API for query/subscription. |
| **System Administrator** | Manages system configuration, users, and security. | High. IT professional. |
| **Maintenance Personnel** | Accesses current pavement condition data for treatment planning. | Low to Medium. Uses simple web or mobile interface. |
| **Research Scientist** | Retrieves historical datasets for analysis. | Medium. Uses query/export tools. |

### 2.4 Constraints
1.  **Architectural:** Must employ open, standards-based architecture and interfaces (NTCIP 1204, TMDD).
2.  **Legal/Policy:** Data dissemination must strictly adhere to contributor-defined sharing agreements.
3.  **Technical:** All timestamps must be in UTC. System must support deployment across multiple physical hosts for scalability and redundancy.
4.  **Operational:** Must operate 24x7 with high reliability. Security must comply with federal IT guidelines (OMB A-130).

### 2.5 Assumptions and Dependencies
*   Data contributors will have the capability to transmit data in or convertible to the defined standard formats.
*   Sufficient network bandwidth will be available for data ingestion and dissemination.
*   The system will be hosted in a secure federal or compliant cloud environment.

## 3. Specific Requirements

### 3.1 Functional Requirements

#### 3.1.1 Data Ingestion (F-ING)
*   **F-ING-001:** The system shall accept environmental observation data conforming to the NTCIP 1204 data model.
*   **F-ING-002:** The system shall support ingestion via a "Clarus standard interface" (protocol TBD – see Appendix A).
*   **F-ING-003:** The system shall validate the basic syntax and schema of all incoming data messages.
*   **F-ING-004:** The system shall acknowledge receipt of data to the contributor.
*   **F-ING-005:** The system shall associate incoming data with pre-registered metadata (sensor ID, location, owner, sharing agreement).

#### 3.1.2 Quality Control (F-QC)
*   **F-QC-001:** The system shall apply a configurable suite of automated QC algorithms to each incoming observation (specific algorithms TBD – see Appendix A).
*   **F-QC-002:** The system shall assign a QC flag (e.g., "Pass," "Suspect," "Fail," "Manual Override") to each data value.
*   **F-QC-003:** The system shall provide a web-based interface for Quality Managers to view data and manually change QC flags.
*   **F-QC-004:** The system shall log all manual QC overrides, including user ID, timestamp, and reason.
*   **F-QC-005:** The system shall allow System Administrators to configure parameters and thresholds for automated QC rules via a management interface.

#### 3.1.3 Data Storage & Management (F-DSM)
*   **F-DSM-001:** The system shall store all raw ingested data.
*   **F-DSM-002:** The system shall store the corresponding QC-applied data as the authoritative version.
*   **F-DSM-003:** The system shall maintain a dynamic data library with a minimum retention period of 7 days for high-performance access.
*   **F-DSM-004:** The system shall manage metadata for all sensors, stations, and data contributors.
*   **F-DSM-005:** The system shall enforce data sharing agreements at the point of data query and dissemination.

#### 3.1.4 Data Dissemination (F-DIS)
*   **F-DIS-001:** The system shall provide a standard API for querying quality-checked environmental data based on parameters (location, time range, sensor type, QC flag).
*   **F-DIS-002:** The system shall support a subscription service where users can request periodic data pushes for specific criteria.
*   **F-DIS-003:** The system shall disseminate data in standard formats (e.g., NTCIP 1204, XML, JSON).
*   **F-DIS-004:** The system shall respond to data queries within 1 minute (performance requirement).
*   **F-DIS-005:** The system shall respond to metadata queries within 5 minutes.

#### 3.1.5 System Administration (F-ADM)
*   **F-ADM-001:** The system shall provide a secure web interface for user and role management (create, read, update, disable).
*   **F-ADM-002:** The system shall allow administrators to manage data sharing agreements.
*   **F-ADM-003:** The system shall provide tools for monitoring system health, performance, and data throughput.

### 3.2 Data Requirements

#### 3.2.1 Data Model
*   The core data model shall be an extension of NTCIP 1204, encompassing:
    *   Atmospheric Data (air temp, dew point, wind speed/direction, precipitation, visibility, etc.)
    *   Pavement Data (surface temp, subsurface temp, condition - dry/wet/icy, chemical concentration, etc.)
    *   Hydrologic Data (water level, precipitation accumulation)
*   Each observation shall be stored with mandatory metadata:
    *   Unique Sensor/Station ID
    *   Geographic Coordinates (latitude, longitude, elevation)
    *   Timestamp (UTC)
    *   Data Contributor ID
    *   Applicable Sharing Agreement ID
    *   QC Flag Value
    *   Ingestion Timestamp (UTC)

### 3.3 External Interface Requirements

#### 3.3.1 User Interfaces
*   **UI-ADMIN:** A secure, role-based web application for system administrators and quality managers.
*   **UI-QUERY:** A web-based query interface for casual data users (e.g., maintenance personnel) to view current conditions via map and table formats.
*   **API:** A RESTful API with comprehensive documentation for programmatic access by service providers and researchers.

#### 3.3.2 Hardware Interfaces
*   The system shall be host-agnostic, capable of running on standard virtualized or physical servers in a data center or cloud environment.

#### 3.3.3 Software Interfaces
*   **Data Ingestion Interface:** Protocol and format to be determined (See Appendix A).
*   **Data Dissemination Interface:** RESTful API returning JSON/XML, supporting OAuth 2.0 or similar authentication.

#### 3.3.4 Communications Interfaces
*   Communication shall occur over HTTPS/TLS 1.2+ for all external interfaces.

### 3.4 Non-Functional Requirements

#### 3.4.1 Performance Requirements
*   **PERF-001:** The system shall publish new quality-checked data for dissemination within 20 minutes of receipt.
*   **PERF-002:** The system shall support 600 concurrent users and 300 simultaneous data requests.
*   **PERF-003:** Query response times shall meet F-DIS-004 and F-DIS-005.

#### 3.4.2 Availability & Reliability
*   **AVAIL-001:** The system shall achieve 95% availability over a calendar month, excluding scheduled maintenance windows.
*   **RELI-001:** The system shall be designed for 24x7 continuous operation.

#### 3.4.3 Security Requirements
*   **SEC-001:** The system shall comply with security controls as per OMB Circular A-130.
*   **SEC-002:** All access to system functions and data shall require authentication.
*   **SEC-003:** Role-Based Access Control (RBAC) shall be implemented to enforce least privilege.
*   **SEC-004:** All data in transit shall be encrypted using industry-standard protocols.

#### 3.4.4 Scalability
*   **SCAL-001:** The system architecture shall support horizontal scaling across multiple hosts to manage increased load.

## Appendix A: Undecided Issues (TBD)

The following issues require resolution in subsequent project phases and may impact detailed design:

1.  **A1. Data Ingestion Protocol:** The specific protocol(s) (e.g., HTTPS POST, Message Queue, SOAP) for the "Clarus standard interface" must be finalized.
2.  **A2. QC Algorithms:** The final set of automated quality checking algorithms (e.g., range checks, rate-of-change checks, spatial consistency checks) and their exact configurable thresholds must be defined.
3.  **A3. Long-Term Retention:** The strategy for archiving data beyond the 7-day dynamic library for potential research or audit purposes needs to be determined.
4.  **A4. Vehicle Data Integration:** Mechanisms for ingesting and processing high-volume, mobile data from future systems like Vehicle Infrastructure Integration (VII) require further study.
5.  **A5. Regional Rule Application:** Detailed definitions of how geographic regions are defined for the application of specific QC rules (e.g., mountain region vs. coastal region thresholds) are needed.

---
*Document End*