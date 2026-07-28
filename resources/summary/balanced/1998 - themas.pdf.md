# Balanced Summary: The Energy Management System (THEMAS)

## Goals and Scope
THEMAS is an independent energy management system designed to monitor and control heating/cooling units in a multi-floor office building. Its primary goal is to maintain desired temperatures within defined limits while optimizing energy usage by limiting concurrent unit operation. The scope is confined to software requirements, assuming specific hardware interfaces and operation on Microsoft Windows NT.

## Stakeholders and User Stories
*   **Supervisor:** Maintains system efficiency, monitors alarms, and generates reports.
*   **Design Requirements Team:** Creates system design based on this SRS.
*   **Principle Software Architect:** Oversees the technical development of the system.
*   **Building Occupants (Indirect):** Experience controlled environmental conditions.

**User Stories:**
1.  As a **supervisor**, I want to **receive audible alarms for invalid or out-of-range temperatures** so that **I can respond to potential system failures.**
2.  As a **supervisor**, I want to **manually change the temperature setting for any thermostat** so that **I can adjust for occupant needs or special circumstances.**
3.  As a **supervisor**, I want to **generate operational history and statistical summary reports** so that **I can analyze system performance and efficiency.**
4.  As the **system**, I want to **validate all incoming temperature readings against a defined valid range** so that **I only process reliable data.**
5.  As the **system**, I want to **queue heating/cooling requests when the maximum number of concurrent units is reached** so that **I can manage energy utilization effectively.**
6.  As the **system**, I want to **log all system events (alarms, unit status changes, denied requests) to a database** so that **I can provide data for reporting and analysis.**

## Key Processes
1.  **System Initialization (Trigger: System startup):** Loads operational parameters from a file and sets all heating/cooling units to a known off state.
2.  **Temperature Validation (Trigger: New temperature data from thermostat):** Checks if reported temperatures and settings are within the pre-defined valid range.
3.  **Temperature Status Determination (Trigger: Valid temperature data):** Compares current temperature to settings to see if trigger or overtemperature limits are exceeded.
4.  **Heating/Cooling Mode Determination (Trigger: Temperature trigger exceeded):** Decides whether to request a heating or cooling unit based on the temperature deviation.
5.  **Utilization Management (Trigger: H/C Request):** Checks current unit status and utilization limits, approving, denying, or queuing the request.
6.  **Signal Generation (Trigger: Approved H/C Request):** Sends the control signal to turn a specific heating or cooling unit on or off.
7.  **Event & Alarm Handling (Trigger: Specific system events):** Generates audible alarms for critical conditions and logs all events to a database for reporting.

## Domain Data Elements
*   **Thermostat**
    *   **Primary Key:** Thermostat ID
    *   **Key Fields:** Current Temperature (T), Temperature Setting (TSET), Location (Floor/Quadrant), Status
*   **Heating/Cooling (H/C) Unit**
    *   **Primary Key:** H/C Unit ID
    *   **Key Fields:** Associated Thermostat ID, Unit Type (Heating/Cooling), Current Status (On/Off), Operational History
*   **Operational Parameters**
    *   **Primary Key:** Parameter Set ID
    *   **Key Fields:** Trigger Delta (TD), Overtemperature Delta (OD), Valid Temperature Range, Max Concurrent Units
*   **System Event**
    *   **Primary Key:** Event ID / Timestamp
    *   **Key Fields:** Event Type (Alarm, Status Change, Denied Request), Source (Thermostat ID / H/C Unit ID), Description, Timestamp
*   **Alarm**
    *   **Primary Key:** Alarm ID / Timestamp
    *   **Key Fields:** Alarm Type (Invalid Temp, Limit Exceeded), Source Thermostat ID, Status (Active/Reset)
*   **Report**
    *   **Primary Key:** Report ID / Generation Time
    *   **Key Fields:** Report Type (Operational, Statistical), Time Period, Data Summary, File Path

## Non-functional Requirements
1.  **Platform:** The system shall be designed to run on the Microsoft Windows NT operating system.
2.  **Reliability:** The system shall include a prototype simulated thermostat for verification and validation of reliability.
3.  **Usability:** The supervisor interface shall present system status clearly without excessive, confusing information.
4.  **Data Integrity:** All system events shall be recorded with a description and the current system time.
5.  **Interoperability:** Interfaces for thermostats and H/C units shall run on the Windows NT operating system.
6.  **Performance:** The system shall assume no real-time delay in data communication with thermostat and H/C unit hardware.

## Milestones and External Dependencies
1.  Completion of Software Requirements Specification (This Document).
2.  Finalization of hardware interface specifications for thermostats and heating/cooling units (External Dependency).
3.  Development and delivery of the simulated thermostat prototype for testing.
4.  Completion of the Software Design Document (SDD) based on this SRS.
5.  Availability of the Microsoft Windows NT development and deployment environment.

## Risks and Mitigation Strategies
1.  **Risk:** Hardware interfaces (thermostat, H/C unit control signals) are not yet defined ("TBD").
    *   **Mitigation:** Isolate interface-specific code, use abstraction layers, and define interface mock-ups early for parallel development.
2.  **Risk:** Assumption of no real-time delay in hardware communication may not hold.
    *   **Mitigation:** Design the system to be tolerant of minor delays and include timestamping of all incoming data for potential synchronization logic.
3.  **Risk:** The system cannot verify if a command sent to an H/C unit was successfully executed (no feedback).
    *   **Mitigation:** Implement robust logging and alerting for expected state changes, and consider periodic system "health checks" or manual verification procedures for the supervisor.
4.  **Risk:** The LIFO queuing strategy for denied H/C requests may not be optimal for occupant comfort.
    *   **Mitigation:** Document this as a design constraint and plan for the queuing algorithm to be a configurable parameter in future versions.
5.  **Risk:** Database (Microsoft Access) may not scale efficiently with high event volume over long periods.
    *   **Mitigation:** Implement report generation and archival processes to manage database size, and document potential migration paths for higher-scale deployments.

## Undecided Issues
1.  The exact format and protocol for the control signal sent to heating and cooling units (marked TBD in SRS-014).
2.  The specific mechanism and data format for the supervisor's interface window to reset alarms.
3.  The naming convention and default storage location for the generated ASCII report files.
4.  The process for adding or removing thermostats/H/C units from the system after initial configuration (dynamic reconfiguration).
5.  The specific list of "valid temperatures" presented to the supervisor for changing a thermostat setting.
6.  Handling of scenarios where the initialization file is missing or corrupted.