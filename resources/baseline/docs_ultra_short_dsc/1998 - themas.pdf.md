# Software Requirements Specification (SRS)
## For THEMAS (Thermostat-based Heating & Cooling Management Autonomous System)

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the software requirements for the THEMAS (Thermostat-based Heating & Cooling Management Autonomous System). It is intended to serve as a comprehensive specification for developers, testers, project managers, and stakeholders. The primary purpose is to ensure a common understanding of the system's capabilities, constraints, and external interfaces.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Keywords:** "Shall" indicates a mandatory requirement. "Should" indicates a recommendation.
*   **Priority:** (H) High, (M) Medium, (L) Low.

#### 1.3 Project Scope
THEMAS is a software system designed to autonomously manage a limited pool of heating and cooling units within a building based on real-time thermostat readings. Its core functions are to maintain desired zone temperatures, enforce a concurrency limit on active units, generate alarms for fault conditions, log all operational events, and provide a supervisory interface for monitoring and control. The system does not receive status feedback from the HVAC units it controls.

**Out of Scope:**
*   Design or specification of thermostat or HVAC unit hardware.
*   Integration with other building management systems (e.g., lighting, security).
*   Network infrastructure or communication protocol design (beyond specified interfaces).
*   Software for the supervisor's computer operating system or other applications.

#### 1.4 References
*   Project Charter: THEMAS-2023-PC-01
*   Interface Control Document (Draft): THEMAS-ICD-01 (TBD for HVAC control signals)

### 2. Overall Description

#### 2.1 Product Perspective
THEMAS is a standalone software component within a larger hardware-software system. It acts as the central control logic, interfacing with external entities as shown in the context diagram below.

```
[Thermostats (x12)] <---Temp Data/Settings---> [THEMAS Software] ---Control Signals---> [HVAC Units (Pool of N)]
       ^                                                  |
       |                                                  |
       |                                            [Supervisor UI] ---Audible Alarm---> [Speaker]
       |                                                  |
       |                                                  V
[Setting Changes]                                  [MS Access Database]
```

**2.1.1 System Interfaces**
*   **Thermostat Interface:** Provides temperature readings and accepts setting updates.
*   **HVAC Unit Control Interface:** Sends ON/OFF control signals to heating/cooling units.
*   **Supervisor User Interface:** Provides a console for monitoring, alarm acknowledgment, manual overrides, and report generation.
*   **Database Interface:** Logs all system events to a persistent Microsoft Access database.
*   **Audible Alarm Interface:** Generates specific frequency tones through the system speaker.

**2.1.2 User Interfaces**
A graphical or text-based user interface shall be provided on the supervisor's computer, allowing the supervisor to:
*   View current status of all thermostats (ID, location, setting, current temp, associated unit status).
*   Acknowledge and silence active alarms.
*   Manually change the desired temperature setting for any thermostat.
*   Request and view operational history and summary reports.

**2.1.3 Hardware Interfaces**
The software shall communicate via defined hardware ports/drivers for:
*   Reading serial/network data from thermostats.
*   Sending digital control signals to HVAC unit relays (interface TBD).
*   Accessing the local file system for the MS Access database.

**2.1.4 Software Interfaces**
*   **Operating System:** Microsoft Windows NT 4.0 (or later).
*   **Database:** Microsoft Access (version to be determined). The software shall use ODBC or a direct driver for all database transactions.
*   **Drivers:** Appropriate communication drivers for thermostat and control hardware.

**2.1.5 Communications Interfaces**
Communication protocols for thermostat data and control signals are to be determined (TBD) but will be abstracted by device drivers.

#### 2.2 Product Functions (High-Level)
1.  **Continuous Monitoring:** Poll thermostats for temperature readings at a defined interval.
2.  **Temperature Validation & Logic:** Validate readings and determine need for heating/cooling action based on deviations from the setpoint.
3.  **Resource Pool Management:** Manage a limited pool of HVAC units, activating/deactivating them based on logic output and queueing requests when the pool is exhausted.
4.  **Alarm Management:** Detect fault conditions (invalid data, critical temperature deviation) and trigger persistent audible alarms.
5.  **Event Logging:** Record all significant system events with a timestamp to a persistent database.
6.  **Supervisory Control:** Provide an interface for manual setting adjustment and alarm acknowledgment.
7.  **Reporting:** Generate reports from the logged event data.

#### 2.3 User Characteristics
*   **Primary User: Building Supervisor.**
    *   **Skill Level:** Technically proficient, familiar with basic building management concepts.
    *   **Responsibilities:** System monitoring, alarm response, manual overrides, generating reports for maintenance review.
    *   **Frequency of Use:** Intermittent monitoring (e.g., hourly), active interaction during alarms or manual changes.

#### 2.4 Constraints
*   **Platform:** Must operate on Microsoft Windows NT.
*   **Feedback:** No status feedback loop from HVAC units. Control is "open-loop."
*   **Building Layout:** The system is configured for a fixed layout: 3 floors, 4 quadrants per floor (12 zones/thermostats total).
*   **Database:** Must use the provided Microsoft Access database schema.

#### 2.5 Assumptions and Dependencies
*   Thermostats provide accurate, correctly formatted data without transmission delays.
*   HVAC units respond correctly to ON/OFF control signals.
*   The hardware interfaces (thermostat reader, control signal board) are provided and functional.
*   The specific control signal interface protocol will be defined prior to implementation.

### 3. Specific Requirements

#### 3.1 External Interface Requirements
**3.1.1 Thermostat Interface**
*   `FR-010` (H): The system shall read temperature and current setting data from all 12 thermostats at a configurable interval (default: 60 seconds).
*   `FR-011` (H): The system shall be able to send a new desired temperature setting to any individual thermostat upon supervisor command.

**3.1.2 HVAC Unit Control Interface**
*   `FR-020` (H): The system shall send an "ACTIVATE" signal to a heating or cooling unit.
*   `FR-021` (H): The system shall send a "DEACTIVATE" signal to a heating or cooling unit.
*   *Note: The physical signal type (e.g., relay closure, voltage) is TBD.*

**3.1.3 Database Interface**
*   `FR-030` (H): The system shall establish a connection to the designated MS Access database file at startup.
*   `FR-031` (H): The system shall insert a new record into the `EventLog` table for every event defined in section 3.2.4.

**3.1.4 User Interface**
*   `FR-040` (M): The UI shall display a real-time status grid showing for each thermostat: Zone ID, Current Temperature, Setpoint Temperature, Deviation, and Associated HVAC Unit Status (Active/Inactive/Queued).
*   `FR-041` (M): The UI shall provide a form for selecting a thermostat and entering a new setpoint temperature.

**3.1.5 Audible Alarm Interface**
*   `FR-050` (H): The system shall generate a 2000 Hz tone for 500 ms, repeating every 2 seconds, for a critical over-temperature alarm.
*   `FR-051` (H): The system shall generate a 800 Hz continuous tone for an invalid data alarm.

#### 3.2 Functional Requirements

**3.2.1 Temperature Monitoring & Validation**
*   `FR-100` (H): The system shall compare each received temperature reading against a valid physical range (e.g., -40°F to 150°F).
*   `FR-101` (H): If a reading is outside the valid range, the system shall flag it as `Invalid Data`, trigger the corresponding alarm (`FR-051`), and log an `InvalidData` event. No control action shall be taken for this zone based on invalid data.

**3.2.2 Temperature Control Logic**
*   `FR-110` (H): For each zone with valid data, the system shall calculate the deviation: `Current Temp - Setpoint Temp`.
*   `FR-111` (H): **Heating Trigger:** If the deviation is ≤ -2°F, the system shall request a heating unit for that zone.
*   `FR-112` (H): **Cooling Trigger:** If the deviation is ≥ +2°F, the system shall request a cooling unit for that zone.
*   `FR-113` (H): **Deactivation:** If an active unit is assigned to a zone and the deviation moves within ±0.5°F of the setpoint, the system shall deactivate the unit.
*   `FR-114` (H): **Critical Alarm:** If the deviation exceeds ±3.0°F, the system shall trigger the critical over-temperature alarm (`FR-050`) for that zone, regardless of unit status.

**3.2.3 HVAC Unit Pool Management**
*   `FR-120` (H): The system shall be configured with a maximum number of HVAC units that can run concurrently (e.g., 4 units).
*   `FR-121` (H): If a heating/cooling request is made (`FR-111`/`FR-112`) and an inactive unit is available in the pool, the system shall immediately activate it for the requesting zone.
*   `FR-122` (H): If the maximum number of units are already active, the system shall place the new request into a First-In-First-Out (FIFO) queue.
*   `FR-123` (H): When a unit is deactivated (`FR-113`), the system shall check the queue. If pending requests exist, it shall activate a unit for the next request in the queue.
*   `FR-124` (H): The system shall log `UnitActivated`, `UnitDeactivated`, and `RequestQueued` events.

**3.2.4 Event Logging**
*   `FR-130` (H): The system shall log the following event types with a timestamp, zone/unit ID, and relevant data (e.g., temperature, deviation):
    *   `TemperatureReading`
    *   `InvalidData`
    *   `HeatingRequested` / `CoolingRequested`
    *   `UnitActivated` / `UnitDeactivated`
    *   `RequestQueued` / `RequestDequeued`
    *   `AlarmTriggered` (type) / `AlarmAcknowledged`
    *   `SetpointChanged` (including old and new value, and initiator 'System' or 'Supervisor')

**3.2.5 Supervisory Functions**
*   `FR-140` (M): The supervisor shall be able to acknowledge any active alarm via the UI, which shall silence the audible tone and log an `AlarmAcknowledged` event.
*   `FR-141` (M): The supervisor shall be able to manually change the setpoint temperature for any zone. This change shall be sent to the thermostat and logged as a `SetpointChanged` event (initiator: 'Supervisor').

**3.2.6 Reporting**
*   `FR-150` (M): The system shall generate an **Operational History Report** for a user-specified date range, listing all logged events in chronological order.
*   `FR-151` (M): The system shall generate a **Statistical Summary Report** for a user-specified date range, including:
    *   Total unit runtime (per unit and aggregate).
    *   Number of times the queue was utilized.
    *   Count of alarms by type.
    *   Average temperature deviation per zone.

#### 3.3 Non-Functional Requirements

**3.3.1 Performance Requirements**
*   `NFR-001`: The system shall process a polling cycle (read all thermostats, process logic, execute control actions) within 10 seconds.

**3.3.2 Safety & Reliability**
*   `NFR-010`: The system shall not allow the concurrent activation of units exceeding the defined hardware safety limit (configurable parameter).
*   `NFR-011`: In the event of a software failure, the system shall fail in a safe state (i.e., not send continuous "ACTIVATE" signals). A watchdog process may be required.

**3.3.3 Usability**
*   `NFR-020`: A supervisor shall be able to acknowledge an alarm within two interactions from the main UI screen.

**3.3.4 Supportability**
*   `NFR-030`: All configuration parameters (polling interval, trigger thresholds, max concurrent units, alarm frequencies) shall be stored in a configuration file, not hard-coded.

### 4. System Evolution
*   Future versions may incorporate HVAC unit status feedback for closed-loop control.
*   Support for additional building layouts may be added.
*   A web-based remote supervisor interface is a potential future enhancement.

---
### Appendix A: Glossary
*   **HVAC:** Heating, Ventilation, and Air Conditioning.
*   **Setpoint:** The desired temperature for a specific zone.
*   **Deviation:** The difference between the current temperature and the setpoint (Current - Setpoint).
*   **Zone:** A specific area of the building controlled by one thermostat (e.g., Floor 1, Quadrant A).
*   **Pool:** The finite collection of physical heating/cooling units available for assignment.

### Appendix B: Analysis Models (To Be Developed)
*   State Transition Diagram for HVAC Unit (Idle, Active, Queued-Assigned).
*   Entity-Relationship Diagram for the Event Log database.
*   Use Case Diagrams for Supervisor interactions.