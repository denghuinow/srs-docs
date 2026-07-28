# Detailed Summary: The Energy Management System (THEMAS)

## Background and Scope
THEMAS is an independent energy management system designed to monitor and control heating/cooling units across a three-floor office building with four quadrants per floor. The system continuously reads thermostat data, determines when to activate HVAC units based on configurable thresholds, enforces concurrency limits, and generates alarms/reports. Non-goals include detailed hardware interface specifications, thermostat feedback mechanisms, and real-time unit status verification from HVAC equipment.

## Stakeholders Matrix and Use Cases
*   **Supervisor:** Monitors system operation, responds to alarms, adjusts thermostat settings, and generates reports for maintenance efficiency.
*   **Building Maintenance Personnel:** Relies on system reports to optimize HVAC performance and perform preventive maintenance.
*   **THEMAS Development Team:** Designs, implements, and validates software against specified requirements.
*   **Principle Requirements/Design/Implementation Architects:** Approve specifications, designs, and final implementation.

**Main Scenarios:**
1.  System initializes by loading parameters and setting all units to a known off state.
2.  Valid temperature reading triggers a heating/cooling request based on trigger values.
3.  Request is approved if under concurrency limit, else queued.
4.  Approved request generates a control signal to the HVAC unit.
5.  Invalid or out-of-range temperature triggers an audible alarm.
6.  Supervisor changes a thermostat setting via the interface.
7.  Supervisor generates an operational history or statistical report.
8.  All system events (alarms, unit status changes, denied requests) are logged to a database.

## Business Process
**Main Process: Temperature Monitoring & Control Loop**
1.  **Trigger:** System initialization completes.
2.  **Input:** Continuous stream of temperature data (T) and settings (TSET) from thermostats.
3.  Validate temperature against the pre-loaded valid range.
4.  If valid, determine if T exceeds overtemperature (OD) or trigger (TD) deltas relative to TSET.
5.  If trigger delta is exceeded, determine required heating/cooling mode and create H/C Request.
6.  Check current unit status and concurrency limit against utilization parameters.
7.  If limit not reached, approve request and generate H/C signal; otherwise, log denied request and queue it.
8.  **Output:** Control signals to HVAC units, status updates, and logged events.

**Key Branch A: Alarm Generation**
1.  **Trigger:** Invalid temperature or overtemperature limit exceeded.
2.  Determine alarm type (invalid temp or limit exceeded).
3.  Activate corresponding audible alarm pattern on supervisor's computer.
4.  Log alarm event; alarm persists until manual reset.

**Key Branch B: Report Generation**
1.  **Trigger:** Supervisor requests a report.
2.  Supervisor selects report type (operational history or monthly statistics).
3.  System queries event database, formats data.
4.  **Output:** ASCII report file at a supervisor-specified location.

## Domain Model
*   **Thermostat:** ID (unique, required), CurrentTemperature, TemperatureSetting, AssignedQuadrant/Floor.
*   **HVAC Unit:** ID (unique, required), Type (Heating/Cooling, required), AssignedThermostatID (reference, required), Status (On/Off).
*   **Operational Parameters:** TriggerDelta (required), OvertempDelta (required), ValidTempRange (required).
*   **Utilization Parameters:** MaxConcurrentUnits (required).
*   **Event:** EventID (unique), Timestamp (required), Type (Alarm/StatusChange/DeniedRequest, required), Description, AssociatedThermostatID (reference), AssociatedUnitID (reference).
*   **Alarm:** AlarmID (unique), Type (InvalidTemp/LimitExceeded, required), Status (Active/Reset), TriggerTimestamp.
*   **Report:** ReportID (unique), Type (History/Statistics, required), Period, GeneratedTimestamp.
*   **Request Queue:** QueueID, ThermostatID (reference), RequestType, Timestamp (LIFO order).

## Interfaces and Integrations
*   **Thermostat Interface (Inbound):** System polls/receives temperature (T) and setting (TSET) data. Input: Thermostat ID, T, TSET. Output: Data to validation module. SLA: Near real-time, correct data format.
*   **HVAC Control Interface (Outbound):** System sends ON/OFF signals to heating/cooling units. Input: Unit ID, Command. Output: Physical control signal. SLA: Signal issued within seconds of decision; interface TBD.
*   **Supervisor UI (Bidirectional):** Provides alarm display/reset, thermostat setting adjustment, and report initiation. Input: Supervisor commands, new temperature settings. Output: System status, alarm indicators, report files. SLA: Responsive to user input.
*   **Event Database (Outbound):** System logs all events to a Microsoft Access database. Input: Formatted event data. Output: Database record. SLA: All events persisted reliably.

## Acceptance Criteria
**Capability: Maintain Temperature within Bounds**
*   Given a thermostat with a valid temperature setting, When the reported temperature exceeds the trigger delta (TSET ± TD), Then a corresponding heating or cooling request is generated.
*   Given a heating/cooling request, When the number of active units is below the maximum, Then an approved request signal is sent to the corresponding HVAC unit.

**Capability: Handle System Faults**
*   Given a thermostat reporting a temperature outside the valid range, When the temperature is validated, Then an invalid temperature alarm is activated and logged.
*   Given a heating/cooling request, When the maximum number of units is already active, Then the request is denied, logged as an event, and placed in a LIFO queue.

**Capability: Provide Supervisor Oversight**
*   Given the supervisor selects a thermostat, When a new valid temperature setting is chosen, Then the system updates the thermostat's setting and re-evaluates the need for heating/cooling.
*   Given the supervisor requests a monthly statistical report, When a month is selected, Then an ASCII file is generated containing unit runtime percentages and request grant/deny ratios.

## Non-functional Metrics
*   **Performance:** System shall process temperature readings and make control decisions within a defined cycle time (e.g., seconds). Report generation for a 12-month history shall complete within a reasonable timeframe (e.g., minutes).
*   **Reliability:** Software shall operate continuously without manual intervention under normal conditions. Event logging shall have zero data loss for alarm and status change events.
*   **Security/Compliance:** Access to change thermostat settings and generate reports shall be restricted to the supervisor role. Design follows ANSI/IEEE STD 830-1984 guidelines for SRS.
*   **Observability:** All system state changes and alarm conditions shall be logged with timestamps for audit and reporting purposes.

## Milestones and Release Strategy
1.  Finalize SRS approval with all architects.
2.  Complete software design document (SDD).
3.  Implement core monitoring, control, and alarm modules.
4.  Implement supervisor UI, reporting, and database modules.
5.  Integrate components and conduct system verification testing.
6.  Deploy initial release for validation in a simulated environment.

## Risk List and Mitigation Strategies
1.  **Risk:** Undefined hardware control interface for HVAC units.
    *   **Mitigation:** Define a mock interface for development and testing; collaborate with hardware team early to specify the final protocol.
2.  **Risk:** Inaccurate temperature readings from thermostats.
    *   **Mitigation:** Implement robust validation and alarming as specified; consider adding diagnostic reporting for thermostat health.
3.  **Risk:** Queue starvation if LIFO policy consistently delays certain requests.
    *   **Mitigation:** Monitor denied request logs; design queueing policy (LIFO) to be configurable for future changes if needed.
4.  **Risk:** Database performance degradation with long-term event storage.
    *   **Mitigation:** Implement report generation that can archive or summarize old data; specify database maintenance procedures.
5.  **Risk:** Supervisor unable to respond to alarms promptly.
    *   **Mitigation:** Ensure alarm is audible and persistent; log all alarms for later review.
6.  **Risk:** Concurrency limit is set too low for building needs.
    *   **Mitigation:** Make the utilization parameter (MaxConcurrentUnits) easily configurable via the initialization file.

## Undecided Issues and Responsible Parties
1.  **Exact protocol and signal specification for HVAC unit control interface.** (Responsible: Hardware/Integration Team)
2.  **Frequency of polling thermostats for temperature data.** (Responsible: Software Design Team)
3.  **Specific data format and schema for the Microsoft Access event database.** (Responsible: Database Designer)
4.  **Detailed design of the supervisor graphical user interface (GUI).** (Responsible: UI Designer)
5.  **Mechanism for the system to detect and recover from a software crash.** (Responsible: Software Architect)