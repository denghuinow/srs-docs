# Balanced Summary

- **Goals and scope**: THEMAS is an independent energy management system designed to monitor and control heating/cooling units in a building. It focuses on maintaining temperature within defined limits while managing simultaneous unit usage. The scope is limited to software requirements running on Windows NT.

- **Roles and user stories**:
  - As a Supervisor, I want to view system reports so that I can monitor efficiency and performance.
  - As a Supervisor, I want to change thermostat settings so that I can adjust temperature preferences.
  - As a Supervisor, I want to receive alarm notifications so that I can respond to temperature anomalies.
  - As a System, I want to validate temperature readings so that I can ignore out-of-range values.
  - As a System, I want to manage heating/cooling unit queues so that I can enforce utilization limits.

- **Key processes**:
  1. System initialization (trigger: system startup)
  2. Load operational parameters from initialization file (trigger: initialization)
  3. Validate temperature readings (trigger: new temperature data)
  4. Monitor temperature against trigger/overtemp values (trigger: valid temperature)
  5. Determine heating/cooling mode (trigger: temperature status change)
  6. Manage heating/cooling unit utilization (trigger: H/C request)
  7. Generate reports and alarms (trigger: supervisor request or system event)

- **Domain data elements**:
  - Thermostat (primary key: thermostat ID; fields: current temperature, temperature setting, status, location)
  - H/C Unit (primary key: unit ID; fields: unit type, status, associated thermostat, floor, quadrant)
  - Event (primary key: event ID; fields: event type, timestamp, description, thermostat ID)
  - Operational Parameters (primary key: parameter set ID; fields: trigger values, overtemp values, valid temp range)
  - Report (primary key: report ID; fields: report type, date range, statistics, generated date)

- **Non-functional requirements**:
  - Runs on Microsoft Windows NT operating system
  - Maximum 3°F temperature deviation tolerance
  - Real-time temperature monitoring with no delays
  - Supervisor interface with clear, non-confusing status displays
  - Event logging to Microsoft Access database
  - Audible alarm system with distinct frequency patterns

- **Milestones and external dependencies**:
  - Completion of hardware interface specifications (TBD)
  - Microsoft Windows NT platform availability
  - Thermostat hardware providing temperature data
  - Heating/cooling unit control interface
  - Microsoft Access database for event storage

- **Risks and mitigation strategies**:
  - Hardware interface undefined: specify interface requirements early
  - Temperature sensor failures: implement validation and alarm system
  - Unit overutilization: implement LIFO queue for denied requests
  - Invalid temperature readings: establish valid range checking
  - Supervisor alarm fatigue: provide distinct alarm patterns for different events

- **Undecided issues**:
  - Specific hardware interface implementation
  - Database performance optimization
  - Report format customization options
  - Alarm reset automation vs manual only
  - Queue management algorithm refinements
  - Not mentioned