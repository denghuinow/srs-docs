# Software Requirements Specification (SRS)
## THEMAS Energy Management System

**Document Version:** 1.0  
**Date:** [Current Date]  
**Status:** Draft  
**Author:** [Author Name/Team]

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the THEMAS (Thermal Heating and Energy Management Automation System) Energy Management System. The intended audience includes the THEMAS development team, project managers, quality assurance personnel, and stakeholders.

#### 1.2 Scope
THEMAS is an independent software system designed to automate the monitoring and control of heating and cooling units within a three-floor office building, with four quadrants (zones) per floor, resulting in twelve distinct control zones. The system's primary objectives are to maintain desired temperature settings efficiently and to enforce limits on the simultaneous operation of HVAC units to prevent electrical overload and optimize energy consumption. Core functionalities include temperature monitoring, automated unit control based on configurable rules, alarm generation, and comprehensive reporting.

**In-Scope Items:**
*   Temperature monitoring and validation against configurable thresholds.
*   Automated control of heating/cooling units with enforcement of concurrent operation limits.
*   System initialization and configuration via external files.
*   Generation of supervisor alarms for temperature anomalies.
*   Event logging for all significant system actions.
*   Generation of operational history and statistical reports.

**Out-of-Scope Items:**
*   Implementation details of hardware interfaces for unit control (to be defined as TBD).
*   Mechanisms for receiving feedback (e.g., confirmation, fault signals) from heating/cooling units.
*   Modeling or compensation for real-time communication delays with thermostats.
*   Support for operating systems other than Windows NT.
*   Detailed specification of user interface components, layouts, and graphics.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **THEMAS:** Thermal Heating and Energy Management Automation System
*   **HVAC:** Heating, Ventilation, and Air Conditioning
*   **SRS:** Software Requirements Specification
*   **TBD:** To Be Determined
*   **Zone:** A uniquely controllable area of the building (e.g., Floor 1, Quadrant B).
*   **Overtemperature:** A condition where the measured temperature deviates from the setpoint beyond a permitted threshold.
*   **Concurrent Operation Limit:** The maximum number of HVAC units allowed to be active simultaneously.

#### 1.4 References
*   Project Charter: THEMAS Energy Management System
*   Stakeholder Interview Summaries

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its users, and constraints. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements, including performance, safety, and security.

### 2. Overall Description

#### 2.1 Product Perspective
THEMAS is a standalone supervisory control application. It interfaces with:
1.  **Thermostats (Input):** Provides temperature readings and user-defined setpoints for each zone. *(Interface: TBD - e.g., serial, network)*.
2.  **HVAC Units (Output):** Sends ON/OFF control signals to individual heating/cooling units. *(Interface: TBD - e.g., relay board, industrial I/O)*.
3.  **Configuration Files (Input):** Used for system initialization, setting parameters like thresholds and limits.
4.  **Supervisor (I/O):** Presents a user interface for monitoring, receiving alarms, adjusting settings, and generating reports.
5.  **Log/Report Files (Output):** Generates persistent ASCII files for event history and statistics.

#### 2.2 Product Functions (Summary)
*   **F1:** Periodically poll and validate temperature data from all 12 zones.
*   **F2:** Compare measured temperature against zone setpoint and configurable thresholds.
*   **F3:** Determine need for heating or cooling action per zone.
*   **F4:** Manage a queue of pending HVAC requests to enforce a global concurrent operation limit.
*   **F5:** Send control signals to activate/deactivate specific HVAC units.
*   **F6:** Log all system events (temperature readings, setpoint changes, unit activations, alarms).
*   **F7:** Detect overtemperature conditions and trigger audible alarms for the supervisor.
*   **F8:** Generate monthly utilization and historical reports in ASCII format.
*   **F9:** Provide a supervisor interface for real-time monitoring, setpoint adjustment, and report generation.

#### 2.3 User Characteristics
| Stakeholder | Role | Expertise / Expectations |
| :--- | :--- | :--- |
| **Supervisor** | Primary Operator | Building facilities manager. Not a software expert. Needs clear alarms, simple controls, and reliable reports. |
| **Building Occupants** | End Beneficiary | Office workers. Expect a comfortable and consistent temperature in their workspace. No direct system interaction. |
| **THEMAS Team** | Developer/Maintainer | Software engineers. Require clear, testable requirements and maintainable system design. |
| **HVAC Technician** | Service Personnel | Services physical units. May need to correlate system logs with physical unit behavior. |

#### 2.4 Core Use Cases
1.  **UC-1: Respond to Temperature Anomaly**
    *   **Actor:** Supervisor, System
    *   **Description:** The system detects a temperature deviation exceeding the overtemperature threshold and triggers an audible alarm to alert the supervisor.
2.  **UC-2: Generate Monthly Utilization Report**
    *   **Actor:** Supervisor
    *   **Description:** The supervisor commands the system to produce a report detailing HVAC unit runtimes, energy consumption estimates (if data available), and temperature compliance statistics for a selected month.
3.  **UC-3: Adjust Thermostat Setting**
    *   **Actor:** Supervisor
    *   **Description:** The supervisor changes the desired temperature setpoint for a specific zone via the THEMAS interface.
4.  **UC-4: Validate Temperature Reading**
    *   **Actor:** System
    *   **Description:** The system checks a raw temperature reading from a thermostat for validity (e.g., within a plausible range, not a sensor fault value) before processing it.
5.  **UC-5: Queue and Process HVAC Request**
    *   **Actor:** System
    *   **Description:** When a zone requires heating/cooling, the system places the request in a queue. It processes requests in order, ensuring the number of simultaneously active units never exceeds the configured maximum.
6.  **UC-6: Log Operational Event**
    *   **Actor:** System
    *   **Description:** The system records a timestamped entry for any significant event (setpoint change, unit activation, alarm) to a persistent log.

#### 2.5 Constraints
1.  **Platform:** Must be developed to run on the Windows NT operating system.
2.  **Hardware Feedback:** The system will receive **no feedback** (acknowledgment, status, fault) from HVAC units after sending a control signal.
3.  **Thermostat Data:** Thermostats provide only current temperature and setpoint data. No unit-on/off status is available.
4.  **Temperature Deviation:** An "overtemperature" alarm must be triggered if the measured temperature deviates from the setpoint by more than ±3°F.
5.  **Report Format:** All generated reports (logs, statistics) must be in plain ASCII text format.

#### 2.6 Assumptions and Dependencies
*   **A1:** Thermostats and HVAC unit control interfaces will be available and their communication protocols will be specified later (TBD).
*   **A2:** The system clock will be accurate and used for timestamping all events.
*   **A3:** The configuration file will be present and correctly formatted at system startup.
*   **D1:** The project depends on the timely definition of the hardware interface specifications.

### 3. Specific Requirements

#### 3.1 External Interface Requirements
**3.1.1 User Interfaces**
*   **UI-1:** A graphical supervisor console shall display real-time temperature and setpoint for all 12 zones.
*   **UI-2:** The console shall provide a visual and audible indicator for any active alarm.
*   **UI-3:** The console shall allow the supervisor to modify the setpoint for any selected zone.
*   **UI-4:** The console shall provide a button or menu option to generate monthly reports.
*(Detailed layout and design are TBD).*

**3.1.2 Hardware Interfaces**
*   **HW-1:** The system shall interface with thermostats to read temperature and setpoint data. *(Protocol and physical interface: TBD)*.
*   **HW-2:** The system shall interface with HVAC unit controllers to send ON and OFF signals. *(Protocol and physical interface: TBD)*.

**3.1.3 Software Interfaces**
*   **SI-1:** The system shall read an initialization file (`themas.config` or similar) at startup. *(Format: TBD)*.
*   **SI-2:** The system shall write event logs to an ASCII file (`event.log` or similar).
*   **SI-3:** The system shall write monthly reports to ASCII files (`report_YYYY_MM.txt`).

**3.1.4 Communications Interfaces**
*(To be defined once hardware interface protocols are specified).*

#### 3.2 Functional Requirements
**3.2.1 Temperature Monitoring & Validation**
*   **FR-1:** The system shall poll temperature and setpoint data from each of the 12 zones at a configurable interval (default: 5 minutes).
*   **FR-2:** The system shall validate each temperature reading. If a reading is outside a plausible range (e.g., -40°F to 150°F) or is a known error code, it shall be flagged as invalid and not used for control decisions.
*   **FR-3:** The system shall calculate the deviation between the measured temperature and the zone setpoint.

**3.2.2 Alarm Management**
*   **FR-4:** If the temperature deviation for any zone exceeds the configurable overtemperature threshold (default: ±3°F), the system shall trigger an overtemperature alarm.
*   **FR-5:** Upon triggering, the alarm shall activate an audible sound on the supervisor's console and a persistent visual alert until acknowledged/reset. *(Reset mechanism: TBD)*.
*   **FR-6:** All alarm events (trigger, acknowledgment) shall be logged.

**3.2.3 HVAC Unit Control**
*   **FR-7:** If the temperature deviation is beyond a configurable "trigger" threshold (e.g., ±2°F) but within the overtemperature alarm limit, the system shall generate a request to activate the appropriate HVAC unit (heating or cooling).
*   **FR-8:** The system shall maintain a configurable global maximum for simultaneously active HVAC units (e.g., 4 units).
*   **FR-9:** The system shall manage a First-In-First-Out (FIFO) queue for pending HVAC activation requests.
*   **FR-10:** The system shall only send an activation signal if the current count of active units is below the maximum. Otherwise, the request shall wait in the queue.
*   **FR-11:** When a unit is activated, a timer shall be started for a configurable minimum run time (e.g., 10 minutes) during which the unit cannot be deactivated by the system.
*   **FR-12:** After the minimum run time has elapsed, the system shall re-evaluate the zone temperature. If the deviation has corrected to within the "trigger" threshold, the system shall send a deactivation signal to the unit.
*   **FR-13:** All unit activation and deactivation commands shall be logged.

**3.2.4 Data Logging**
*   **FR-14:** The system shall log the following events with a timestamp and relevant data (zone ID, temperature, setpoint, etc.):
    *   Polled temperature readings (valid and invalid).
    *   Setpoint changes.
    *   HVAC unit activation/deactivation commands.
    *   Alarm triggers and acknowledgments.
    *   System startup and shutdown.

**3.2.5 Reporting**
*   **FR-15:** The system shall generate a monthly utilization report in ASCII format upon supervisor request. The report shall include, at a minimum:
    *   Total runtime per HVAC unit.
    *   Number of activation cycles per unit.
    *   Percentage of time each zone temperature was within ±1°F, ±2°F, and ±3°F of its setpoint.
    *   Count of overtemperature alarms per zone.
*   **FR-16:** The system shall be able to generate reports for any month within the past 12 months from the stored event log data.

**3.2.6 Configuration & Initialization**
*   **FR-17:** The system shall read all operational parameters (polling interval, trigger threshold, overtemperature threshold, max concurrent units, etc.) from an external configuration file at startup.

#### 3.3 Non-Functional Requirements

**3.3.1 Performance Requirements**
*   **PER-1:** The system shall process a polling cycle for all 12 zones and make control decisions within 10 seconds.
*   **PER-2:** The supervisor interface shall update displayed temperatures within 15 seconds of a polling cycle completing.
*   **PER-3:** The system shall support the generation of a 30-day monthly report within 60 seconds.

**3.3.2 Safety Requirements**
*   **SAF-1:** The system shall include a manual "System Override" or "Emergency Stop" function in the supervisor console to immediately halt all HVAC control signals.
*   **SAF-2:** The control logic shall prevent simultaneous heating and cooling requests for the same zone.

**3.3.3 Security Requirements**
*   **SEC-1:** Adjusting system configuration parameters (via file or UI) shall require supervisor-level authentication.
*   **SEC-2:** Log files shall be append-only from the application's perspective to prevent tampering.

**3.3.4 Software Quality Attributes**
*   **REL-1:** The system shall achieve 99.5% operational uptime during building hours.
*   **MAIN-1:** All configuration parameters shall be modifiable without requiring code recompilation.
*   **USAB-1:** A trained supervisor shall be able to perform all common tasks (acknowledge alarm, adjust setpoint, generate report) with no more than 3 mouse clicks or menu navigations.

### 4. Appendices

#### 4.1 Success Metrics
*   Maintain zone temperatures within ±3°F of their setpoints for ≥95% of operational time during normal conditions.
*   Successfully enforce the concurrent operation limit with 100% compliance (no instances of exceeding the limit).
*   100% accuracy in logged events compared to actual system actions.
*   All generated reports are complete, accurate, and in the specified ASCII format.

#### 4.2 Undecided Issues (TBD)
1.  Hardware interface specification for thermostat communication.
2.  Hardware interface specification for HVAC unit control signals.
3.  Detailed database schema or file structure for event storage.
4.  Specific design, layout, and controls of the supervisor interface windows.
5.  Exact format and syntax of the initialization configuration file.
6.  Detailed mechanism for the supervisor to acknowledge and reset an audible alarm.

---
*This document is considered a living specification and may be updated as requirements are clarified and TBD items are resolved.*