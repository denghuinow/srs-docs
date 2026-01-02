# Software Requirements Specification (SRS)
## Standardized Wind Turbine Communication System (SWTCS)

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Standardized Wind Turbine Communication System (SWTCS). The purpose of SWTCS is to establish a vendor-independent, standardized protocol and interface for the secure and reliable exchange of operational data and commands between individual wind turbine controllers and remote Supervisory Control and Data Acquisition (SCADA) systems, for both single turbines and entire wind farms.

#### 1.2 Document Conventions
*   **Requirements IDs:** Follow the format `FR-XXX` for Functional Requirements and `NFR-XXX` for Non-Functional Requirements.
*   **Keywords:** `MUST`, `SHALL`, `REQUIRED` indicate mandatory requirements. `SHOULD`, `RECOMMENDED` indicate desirable but not mandatory features. `MAY`, `OPTIONAL` indicate permissible actions.
*   **Priority:** `P0` (Critical), `P1` (High), `P2` (Medium), `P3` (Low).

#### 1.3 Intended Audience and Reading Suggestions
*   **Project Sponsors & Management:** Review Sections 1 (Introduction) and 2 (Overall Description).
*   **System Architects & Developers:** Review entire document, focusing on Sections 3 (Specific Requirements).
*   **QA/Test Engineers:** Use Section 3 to derive test cases and validation criteria.
*   **Technical Writers:** Use this document as the basis for user and administrator manuals.

#### 1.4 Project Scope
The SWTCS encompasses the software components, communication protocols, data models, and APIs necessary for standardized remote monitoring and control. It explicitly **excludes**:
*   Safety-critical control logic internal to the turbine controller (e.g., emergency overspeed shutdown, blade pitch fail-safe mechanisms).
*   The physical hardware of the turbine controller or SCADA server.
*   Proprietary vendor-specific algorithms for performance optimization.

**In-Scope Diagram:**
```
[Wind Turbine Controller] <--(SWTCS Protocol)--> [Gateway/Adapter] <--(SWTCS Protocol)--> [Remote SCADA System]
         ^                                                                                         ^
         |                                                                                         |
(Internal Safety Systems - OUT OF SCOPE)                                           (External Parties e.g., Vendors - IN SCOPE for defined interfaces)
```

### 2. Overall Description

#### 2.1 Product Perspective
The SWTCS is a middleware communication layer. It integrates with the existing turbine controller's internal data bus and provides a unified, external-facing interface. It must coexist with and, via gateways, translate to/from legacy proprietary protocols.

#### 2.2 Product Functions (Summary)
1.  Provide real-time and historical data from turbines to SCADA.
2.  Transmit control commands from SCADA to individual or groups of turbines.
3.  Manage and propagate alarms and operational events.
4.  Support system administration functions (security, time sync, diagnostics).
5.  Ensure reliable operation in harsh environmental conditions.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Primary Use Case |
| :--- | :--- | :--- |
| **Wind Turbine Operator/Owner** | Technical staff, monitors farm health, optimizes production. | Daily monitoring, performance analysis, manual control interventions, alarm acknowledgment. |
| **Electrical Network Operator** | Manages grid stability, may have legal authority for control. | Monitoring power output, receiving grid-related alarms, issuing set-point commands for grid support. |
| **External Parties (e.g., Vendor Service)** | Remote service engineers, requires limited, secure access. | Diagnostic data retrieval, firmware update support, performance report generation. |

#### 2.4 Operating Environment
*   **Hardware Environment (Turbine Side):** Industrial PC/PLC within nacelle or tower base. Exposed to temperatures from -30°C to +70°C, high humidity, salt spray (coastal), and constant vibration.
*   **Software Environment:** Real-time Operating System (RTOS) or lightweight Linux distribution on the turbine controller. Standard OS (Windows/Linux) on the SCADA server side.
*   **Network Environment:** Intermittent or low-bandwidth links (e.g., cellular, microwave, fiber). Supports typical wind farm network topologies (star, ring).

#### 2.5 Design and Implementation Constraints
1.  **C1:** The system **MUST NOT** be used as a primary channel for safety-critical functions (IEC 61400-25-1).
2.  **C2:** The core protocol **MUST** be based on open, internationally recognized standards (e.g., IEC 61400-25, OPC UA, MQTT Sparkplug).
3.  **C3:** All external interfaces (connectors, cabinets) **MUST** be designed to IP65 rating or equivalent to withstand specified environmental conditions.
4.  **C4:** The response time for time-critical commands (e.g., immediate stop, set-point change) **MUST** be ≤ 500 ms end-to-end (SCADA HMI to turbine actuator confirmation).
5.  **C5:** The architecture **SHALL** provide a well-defined gateway specification to interface with legacy proprietary turbine protocols.

#### 2.6 Assumptions and Dependencies
*   **A1:** The turbine's internal controller provides a stable and secure internal data API.
*   **A2:** A network connection, however intermittent, will be available between the turbine and the SCADA system.
*   **D1:** Development depends on the selection of a specific underlying open standard (e.g., OPC UA Information Model definition for wind turbines).

### 3. Specific Requirements

#### 3.1 External Interface Requirements
**3.1.1 User Interfaces**
*   `NFR-UI-01`: The SCADA HMI (not part of SWTCS core but its client) **SHOULD** present turbine data using standardized symbols and nomenclature per IEC 61400-25-2.

**3.1.2 Hardware Interfaces**
*   `NFR-HI-01`: The turbine-side communication module **MUST** support at least one Ethernet port (10/100/1000BASE-T) with optional fiber SFP module.
*   `NFR-HI-02`: The module **MUST** operate reliably within the environmental ranges specified in Section 2.4.

**3.1.3 Software Interfaces**
*   `FR-SI-01`: The system **SHALL** provide an OPC UA Server interface (or equivalent standard) exposing a wind turbine information model.
*   `FR-SI-02`: The system **SHALL** provide a RESTful API for historical data and log retrieval, using JSON data format.
*   `FR-SI-03`: The system **SHALL** specify a gateway adapter interface to map proprietary protocol `X` to/from the SWTCS standard.

**3.1.4 Communications Interfaces**
*   `FR-CI-01`: The protocol **SHALL** support secure communication using TLS 1.2 or higher for all client-server connections.
*   `FR-CI-02`: The protocol **SHALL** support both client-initiated and server-initiated (publish/subscribe) data exchanges.

#### 3.2 Functional Requirements
**3.2.1 Remote Supervision**
*   `FR-SUP-01 (P0)`: The system **SHALL** allow a remote SCADA client to read real-time measurements (e.g., active power, wind speed, rotor RPM, bearing temperature) from any configured turbine.
*   `FR-SUP-02 (P0)`: The system **SHALL** allow a remote SCADA client to read the current operational status (e.g., running, stopped, faulted, service mode) of any turbine.

**3.2.2 Remote Control**
*   `FR-CTL-01 (P0)`: The system **SHALL** allow an authorized remote client to issue a `START` and `STOP` command to a turbine.
*   `FR-CTL-02 (P1)`: The system **SHALL** allow an authorized remote client to set a power or torque reference set-point within the turbine's allowable operating range.
*   `FR-CTL-03 (P0)`: The system **SHALL** require a two-step authentication/confirmation for any control command that changes the turbine's operational state.

**3.2.3 Alarm and Event Management**
*   `FR-AE-01 (P0)`: The system **SHALL** immediately push alarm notifications (timestamp, source, severity, description) to subscribed SCADA clients upon detection by the turbine controller.
*   `FR-AE-02 (P1)`: The system **SHALL** log all alarms and events with a unique sequence number in a persistent, circular buffer on the turbine side.
*   `FR-AE-03 (P1)`: The system **SHALL** allow a remote client to acknowledge specific alarms.

**3.2.4 Historical Data & Log Retrieval**
*   `FR-HIS-01 (P1)`: The system **SHALL** store min, max, average values for key measurements at configurable intervals (e.g., 10-minute statistics) for a minimum of 90 days.
*   `FR-HIS-02 (P2)`: The system **SHALL** allow a remote client to retrieve historical data sets for a specified turbine, variable, and time range.

**3.2.5 System Management**
*   `FR-MGT-01 (P1)`: The system **SHALL** support network time synchronization (NTP or PTP) to ensure timestamps are consistent across all turbines and the SCADA server.
*   `FR-MGT-02 (P0)`: The system **SHALL** implement role-based access control (RBAC) with at least three roles: `Viewer`, `Operator`, `Administrator`.
*   `FR-MGT-03 (P1)`: The system **SHALL** provide a heartbeat/device health status message from each turbine at a configurable interval.

#### 3.3 Non-Functional Requirements

**3.3.1 Performance Requirements**
*   `NFR-PER-01`: The response time for time-critical control commands (FR-CTL-01) **MUST** be ≤ 500 ms as defined in Constraint C4.
*   `NFR-PER-02`: The update rate for high-priority real-time measurements (FR-SUP-01) **SHALL** be configurable up to a minimum of 1 Hz.
*   `NFR-PER-03`: The system **SHALL** support concurrent monitoring connections from at least 5 different clients to a single turbine server.

**3.3.2 Safety Requirements**
*   `NFR-SAF-01`: The system **SHALL** include a hardware watchdog timer on the turbine side that resets the communication module if the software fails, without impacting the failsafe turbine controller.
*   `NFR-SAF-02`: All remote control commands **SHALL** be validated against the turbine's current operational state and physical limits before execution.

**3.3.3 Security Requirements**
*   `NFR-SEC-01`: All user access **MUST** require authentication. Passwords **SHALL** be stored using strong, salted hashing algorithms.
*   `NFR-SEC-02`: The system **SHALL** audit and log all login attempts, control commands issued, and configuration changes.
*   `NFR-SEC-03`: Communication **MUST** be encrypted in transit as per `FR-CI-01`.

**3.3.4 Reliability, Availability, and Maintainability**
*   `NFR-RAM-01`: The turbine-side communication module **SHALL** have a Mean Time Between Failures (MTBF) of > 100,000 hours.
*   `NFR-RAM-02`: The system **SHALL** be capable of buffering at least 24 hours of alarm and event data locally in case of network failure.
*   `NFR-RAM-03`: Firmware updates to the communication module **SHALL** be possible remotely via a secure and rollback-capable mechanism.

**3.3.5 Portability & Interoperability**
*   `NFR-INT-01`: The standardized data model (per `FR-SI-01`) **SHALL** be publicly documented to enable third-party SCADA vendors to develop compatible clients.
*   `NFR-INT-02`: The gateway specification (per `FR-SI-03`) **SHALL** allow the integration of at least two major legacy turbine control systems.

---
### Appendix A: Glossary
| Term | Definition |
| :--- | :--- |
| **SCADA** | Supervisory Control and Data Acquisition. |
| **OPC UA** | Open Platform Communications Unified Architecture (IEC 62541). |
| **IEC 61400-25** | International standard for communications for monitoring and control of wind power plants. |
| **Set-point** | A target value for a controlled variable (e.g., active power output). |
| **Gateway** | A device/software that translates between the SWTCS protocol and a proprietary protocol. |

### Appendix B: To Be Determined (TBD)
1.  Selection of the core open standard (OPC UA vs. MQTT Sparkplug vs. pure IEC 61400-25-4).
2.  Complete list of mandatory data points in the information model.
3.  Specific cybersecurity certification targets (e.g., IEC 62443-4-2 SL2).