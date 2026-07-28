# Software Requirements Specification (SRS)
## For
# The Energy Management System (THEMAS)

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft for Review  
**Prepared For:** Principle Requirements/Design/Implementation Architects  
**Prepared By:** THEMAS Development Team  
**Standard:** ANSI/IEEE STD 830-1984

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for The Energy Management System (THEMAS). It serves as a comprehensive agreement between the stakeholders and the development team, providing a basis for design, implementation, verification, and project management.

### 1.2 Scope
THEMAS is an independent software system designed to monitor and control Heating, Ventilation, and Air Conditioning (HVAC) units across a three-floor office building with four quadrants per floor. Its primary functions are:
*   Continuously monitor thermostat data (temperature and setting).
*   Automatically activate/deactivate HVAC units based on configurable temperature thresholds.
*   Enforce concurrency limits on active HVAC units to manage energy load.
*   Generate audible alarms for fault conditions.
*   Provide a supervisor interface for monitoring, configuration, and reporting.
*   Log all system events to a persistent database for audit and analysis.

**Non-Goals (Out of Scope):**
*   Detailed specification of hardware interfaces for thermostats or HVAC units.
*   Implementation of thermostat feedback mechanisms or real-time status verification from HVAC equipment.
*   Physical installation or maintenance of hardware components.

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **HVAC** | Heating, Ventilation, and Air Conditioning. |
| **THEMAS** | The Energy Management System. |
| **SLA** | Service Level Agreement. |
| **GUI** | Graphical User Interface. |
| **T** | Current Temperature reading from a thermostat. |
| **TSET** | Temperature Setting (desired setpoint) on a thermostat. |
| **TD** | Trigger Delta. The configurable threshold that triggers a heating/cooling request. |
| **OD** | Overtemperature Delta. The configurable safety limit that triggers an alarm. |
| **LIFO** | Last-In, First-Out. A queue processing policy. |
| **SRS** | Software Requirements Specification. |
| **SDD** | Software Design Document. |

### 1.4 References
*   ANSI/IEEE Std 830-1984, IEEE Guide to Software Requirements Specifications.

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general product description. Section 3 details specific requirements, including functional capabilities, interfaces, and constraints. Appendices may contain supplementary information.

## 2. Overall Description

### 2.1 Product Perspective
THEMAS is a standalone supervisory control system. It interfaces with existing building thermostats (data source) and HVAC unit controllers (control target). It provides a dedicated interface for a building supervisor and maintains a historical record of all operations in a Microsoft Access database.

### 2.2 Product Functions (High-Level)
1.  **System Initialization:** Load configuration parameters and establish a known system state.
2.  **Continuous Temperature Monitoring:** Poll/receive data from all building thermostats.
3.  **Intelligent HVAC Control:** Generate and manage heating/cooling requests based on temperature deviations, subject to concurrency limits.
4.  **Fault Detection & Alarming:** Identify invalid data or overtemperature conditions and activate persistent audible alarms.
5.  **Supervisor Interaction:** Provide an interface for system monitoring, thermostat setting adjustment, alarm acknowledgment, and report generation.
6.  **Comprehensive Logging:** Record all significant events (alarms, unit state changes, denied requests) to a database.
7.  **Report Generation:** Produce operational history and statistical summary reports on demand.

### 2.3 User Characteristics
| Stakeholder | Role & Interaction |
| :--- | :--- |
| **Supervisor** | Primary user. Monitors system status, responds to and resets alarms, adjusts thermostat settings (TSET), and requests reports. Assumed to have basic computer literacy. |
| **Building Maintenance Personnel** | Secondary user. Consumes generated reports to optimize HVAC performance and schedule preventive maintenance. |
| **THEMAS Development Team** | Designs, develops, and tests the system against this SRS. |
| **Principle Architects** | Approve this SRS, subsequent designs, and the final implementation. |

### 2.4 Constraints
*   **Hardware Interface:** The specific protocols for communicating with thermostats and HVAC control units are not defined and will be provided by a hardware/integration team.
*   **Database:** The system must use Microsoft Access as the event logging database.
*   **Policy:** Request queueing must initially implement a LIFO policy.
*   **Deployment:** The system must manage a fixed topology of 3 floors x 4 quadrants.

### 2.5 Assumptions and Dependencies
*   Thermostats provide reliable, periodic data in a predefined format.
*   HVAC units correctly respond to ON/OFF control signals.
*   The supervisor's computer has audio output capabilities for alarms.
*   The Microsoft Access database is accessible and has sufficient capacity.

## 3. Specific Requirements

### 3.1 Functional Requirements

#### 3.1.1 System Initialization (FR-INIT)
*   **FR-INIT-1:** Upon startup, THEMAS shall load all operational parameters (`TriggerDelta`, `OvertempDelta`, `ValidTempRange`) and utilization parameters (`MaxConcurrentUnits`) from a configuration file.
*   **FR-INIT-2:** Upon startup, THEMAS shall initialize the status of all HVAC units to "Off".
*   **FR-INIT-3:** Upon startup, THEMAS shall establish connections to the thermostat data source, the HVAC control interface, and the event database.

#### 3.1.2 Temperature Monitoring & Validation (FR-MON)
*   **FR-MON-1:** THEMAS shall periodically acquire the current temperature (T) and setting (TSET) for each thermostat in the building.
*   **FR-MON-2:** For each reading, THEMAS shall validate T against the configured `ValidTempRange`.
*   **FR-MON-3:** If T is outside `ValidTempRange`, THEMAS shall trigger an "Invalid Temperature" alarm (see FR-ALARM).
*   **FR-MON-4:** If T is valid, THEMAS shall calculate the absolute difference between T and TSET.

#### 3.1.3 HVAC Control Logic (FR-CTRL)
*   **FR-CTRL-1:** If `|T - TSET| > TriggerDelta (TD)`, THEMAS shall create a Heating or Cooling Request. The mode (Heat/Cool) is determined by whether T is below or above TSET, respectively.
*   **FR-CTRL-2:** Before approving a request, THEMAS shall check the current count of active (`Status = On`) HVAC units against `MaxConcurrentUnits`.
*   **FR-CTRL-3:** If the active unit count is less than `MaxConcurrentUnits`, THEMAS shall approve the request, send an ON signal to the corresponding HVAC unit, update the unit's status to "On", and log a "Unit Activated" event.
*   **FR-CTRL-4:** If the active unit count is equal to or greater than `MaxConcurrentUnits`, THEMAS shall deny the request, log a "Request Denied" event, and place the request into a LIFO queue.
*   **FR-CTRL-5:** When an active HVAC unit's associated thermostat reports `|T - TSET| <= TD`, THEMAS shall send an OFF signal to that unit, update its status to "Off", log a "Unit Deactivated" event, and check the queue for pending requests.
*   **FR-CTRL-6:** Upon a unit deactivation (FR-CTRL-5), if the queue is not empty, THEMAS shall process the most recently queued (LIFO) request as per FR-CTRL-3.

#### 3.1.4 Alarm Management (FR-ALARM)
*   **FR-ALARM-1:** Upon detection of an invalid temperature (FR-MON-3), THEMAS shall immediately activate a distinct, audible "Invalid Temperature" alarm pattern on the supervisor's computer.
*   **FR-ALARM-2:** If a valid temperature T exceeds `TSET ± OvertempDelta (OD)`, THEMAS shall immediately activate a distinct, audible "Overtemperature Limit Exceeded" alarm.
*   **FR-ALARM-3:** Any activated alarm shall persist audibly and be logged as an "Active" alarm event until manually reset by the Supervisor via the UI.
*   **FR-ALARM-4:** The system shall provide a visual indicator in the Supervisor UI for all active alarms.

#### 3.1.5 Supervisor User Interface (FR-UI)
*   **FR-UI-1:** THEMAS shall provide a graphical interface displaying the status (On/Off) of all HVAC units and thermostats, organized by floor and quadrant.
*   **FR-UI-2:** The Supervisor shall be able to select any thermostat and input a new, valid TSET value. THEMAS shall update the thermostat's setting and immediately re-evaluate the need for heating/cooling (FR-MON-4, FR-CTRL-1).
*   **FR-UI-3:** The Supervisor shall be able to view a list of active alarms and have the capability to acknowledge/reset any individual alarm, silencing its audible alert.
*   **FR-UI-4:** The Supervisor shall be able to initiate report generation by selecting a report type and providing necessary parameters (e.g., date range).

#### 3.1.6 Reporting (FR-REP)
*   **FR-REP-1:** THEMAS shall generate an **Operational History Report** containing a chronological list of all logged events (alarms, unit activations/deactivations, denied requests) for a user-specified time period.
*   **FR-REP-2:** THEMAS shall generate a **Monthly Statistical Report** containing, for a selected month:
    *   Runtime percentage for each HVAC unit.
    *   Ratio of granted vs. denied heating/cooling requests.
    *   Count and type of alarms triggered.
*   **FR-REP-3:** All reports shall be generated as ASCII text files and saved to a filesystem location specified by the Supervisor at the time of the request.

#### 3.1.7 Event Logging (FR-LOG)
*   **FR-LOG-1:** THEMAS shall log the following events to the Microsoft Access database in real-time:
    *   Alarm Activation and Reset (with type and thermostat ID)
    *   HVAC Unit Status Change (On/Off with unit ID)
    *   Heating/Cooling Request Denial (with thermostat ID and reason)
*   **FR-LOG-2:** Each log entry shall include a unique EventID, a precise timestamp, the event type, a description, and relevant entity IDs (ThermostatID, UnitID).

### 3.2 External Interface Requirements

#### 3.2.1 Thermostat Data Interface
*   **Type:** Inbound, Software Interface.
*   **Purpose:** To receive current temperature and setpoint data.
*   **Data Input:** `ThermostatID`, `CurrentTemperature (T)`, `TemperatureSetting (TSET)`.
*   **SLA:** Data must be provided in a defined format at a near real-time frequency (specific frequency TBD by Software Design Team).

#### 3.2.2 HVAC Control Interface
*   **Type:** Outbound, Hardware/Software Interface.
*   **Purpose:** To send ON/OFF control signals to physical HVAC units.
*   **Data Output:** `UnitID`, `Command (ON/OFF)`.
*   **SLA:** A control signal must be issued within **5 seconds** of the system's decision to change a unit's state. The exact protocol is TBD by the Hardware/Integration Team.

#### 3.2.3 Supervisor GUI
*   **Type:** Bidirectional, User Interface.
*   **Purpose:** To provide system oversight and control to the Supervisor.
*   **Input:** Mouse/Keyboard commands from Supervisor, including new thermostat settings.
*   **Output:** Graphical display of system status, alarm indicators, and report file generation.
*   **SLA:** The interface shall respond to user actions within **2 seconds**.

#### 3.2.4 Event Database Interface
*   **Type:** Outbound, Database Interface.
*   **Purpose:** To persist all system event logs.
*   **Data Output:** Formatted event records conforming to the database schema.
*   **SLA:** 100% of critical events (Alarms, Status Changes) must be successfully written to the database. The interface shall use Microsoft Access.

### 3.3 Domain Model (Data Requirements)
Key entities and their critical attributes:
```yaml
Thermostat:
  - ID: String, Unique, Required
  - CurrentTemperature: Float
  - TemperatureSetting: Float
  - AssignedFloor: Integer
  - AssignedQuadrant: Integer

HVAC_Unit:
  - ID: String, Unique, Required
  - Type: Enum{Heating, Cooling}, Required
  - AssignedThermostatID: String, Foreign Key, Required
  - Status: Enum{On, Off}

Operational_Parameters:
  - TriggerDelta: Float, Required
  - OvertempDelta: Float, Required
  - ValidTempRange: {Min: Float, Max: Float}, Required

Utilization_Parameters:
  - MaxConcurrentUnits: Integer, Required

Event_Log:
  - EventID: Integer, Unique, Auto-generated
  - Timestamp: DateTime, Required
  - Type: Enum{Alarm, StatusChange, DeniedRequest}, Required
  - Description: String
  - AssociatedThermostatID: String, Foreign Key
  - AssociatedUnitID: String, Foreign Key

Alarm:
  - AlarmID: Integer, Unique, Auto-generated
  - Type: Enum{InvalidTemp, LimitExceeded}, Required
  - Status: Enum{Active, Reset}, Required
  - TriggerTimestamp: DateTime, Required
  - ResetTimestamp: DateTime

Request_Queue:
  - QueuePosition: Integer
  - ThermostatID: String, Foreign Key
  - RequestType: Enum{Heat, Cool}
  - Timestamp: DateTime # Used for LIFO ordering
```

### 3.4 Non-Functional Requirements

#### 3.4.1 Performance
*   **PERF-1:** The system shall complete one full cycle of reading all thermostats, processing data, and making control decisions within **10 seconds** under normal load.
*   **PERF-2:** Generating a Monthly Statistical Report for a 12-month period shall complete within **3 minutes**.

#### 3.4.2 Reliability & Availability
*   **REL-1:** The software shall be designed for continuous, unattended operation with a target uptime of 99.5% in a normal office environment.
*   **REL-2:** Event logging shall guarantee zero data loss for alarm activation and HVAC unit status change events. The system shall implement write retries and failure notification for the database connection.

#### 3.4.3 Security
*   **SEC-1:** Access to the functionality for changing thermostat settings (TSET) and generating reports shall be controlled by a login mechanism restricted to the Supervisor role.
*   **SEC-2:** The configuration file containing operational parameters shall be readable only by the THEMAS application and system administrators.

#### 3.4.4 Observability & Maintainability
*   **OBS-1:** All system state changes, user actions, and fault conditions shall be logged with an accurate timestamp and sufficient context for debugging and audit trails.
*   **OBS-2:** The `MaxConcurrentUnits` parameter shall be configurable via the initialization file without requiring code changes.

### 3.5 Acceptance Criteria
*   **AC-1 (Temperature Control):** Given thermostat `T-1F1` with `TSET=22°C` and `TD=2°C`, when `T` is reported as `19°C` (`|Δ|=3°C`), then a Heating Request for the associated unit is generated.
*   **AC-2 (Concurrency Limit):** Given `MaxConcurrentUnits=5` and 5 units already active, when a new Heating Request is generated, then the request is denied, logged, and placed in the queue.
*   **AC-3 (Invalid Temp Alarm):** Given the `ValidTempRange` is `10°C to 40°C`, when thermostat `T-2F3` reports `T=5°C`, then an Invalid Temperature alarm is immediately activated and logged.
*   **AC-4 (Supervisor Setting Change):** Given the Supervisor selects thermostat `T-3F4` via the UI and sets a new `TSET=24°C`, then the system updates `TSET` for `T-3F4` and re-evaluates its temperature condition.
*   **AC-5 (Report Generation):** Given the Supervisor requests a Monthly Statistical Report for January 2024, then an ASCII file is created containing the runtime percentage for each unit and the grant/deny ratio for that month.

## 4. Appendices

### 4.1 Risk Management
| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| Undefined HVAC hardware interface. | High | High | Develop with a mock interface. Engage hardware team early for protocol specification. |
| Inaccurate thermostat readings. | Medium | Medium | Implement robust validation and alarming. Design reports to highlight potential faulty sensors. |
| LIFO queue starvation. | Low | Medium | Monitor denial logs. Design queue policy to be configurable for future changes. |
| Database performance degradation. | Medium | Medium | Design reports to summarize/archive old data. Define regular DB maintenance procedures. |

### 4.2 Undecided Issues & TBDs
1.  **Exact protocol and signal specification for HVAC unit control interface.** *(Responsible: Hardware/Integration Team)*
2.  **Frequency of polling thermostats for temperature data.** *(Responsible: Software Design Team)*
3.  **Specific data format and schema for the Microsoft Access event database.** *(Responsible: Database Designer)*
4.  **Detailed design of the supervisor graphical user interface (GUI).** *(Responsible: UI Designer)*
5.  **Mechanism for the system to detect and recover from a software crash.** *(Responsible: Software Architect)*

---
**Document Approval:**

| Role/Title | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Principle Requirements Architect | | | |
| Principle Design Architect | | | |
| Principle Implementation Architect | | | |
| Project Manager | | | |