# Short Summary: THEMAS Energy Management System

## Background and Objectives
THEMAS is an independent energy management system designed to monitor and control heating/cooling units in a three-floor office building with four quadrants per floor. The system aims to maintain temperature settings efficiently while limiting simultaneous unit operation through automated monitoring and reporting.

## In Scope
- Temperature monitoring and validation against configurable trigger/overtemperature thresholds
- Heating/cooling unit control with concurrent operation limits
- System initialization from configuration files
- Supervisor alarm generation for temperature anomalies
- Event logging and report generation (operational history and statistics)

## Out of Scope
- Hardware interface implementation details (marked TBD)
- Heating/cooling unit feedback mechanisms
- Real-time thermostat communication delays
- Non-Windows NT operating systems
- Detailed user interface specifications

## Stakeholders and Core Use Cases
**Stakeholders:**
- Supervisor: Maintains system efficiency and responds to alarms
- Building Occupants: Experience controlled temperature environments
- THEMAS Team: Develops and maintains the software system
- Heating/Cooling Technicians: Service physical units referenced by the system

**Core Use Cases:**
1. As a supervisor, I want to receive audible alarms for temperature anomalies so that I can respond to critical conditions
2. As a supervisor, I want to generate monthly utilization reports so that I can analyze system efficiency
3. As a supervisor, I want to adjust thermostat settings so that I can accommodate changing occupancy needs
4. As the system, I want to validate temperature readings so that I only process reasonable values
5. As the system, I want to queue heating/cooling requests so that I maintain concurrent operation limits
6. As the system, I want to log all operational events so that I can generate historical reports

## Success Metrics
- Maintain temperatures within ±3°F of settings during normal operation
- Limit simultaneous heating/cooling unit operation per configurable maximum
- Generate accurate operational reports covering 12-month history

## Major Constraints
- Must run on Windows NT operating system
- No feedback from heating/cooling units regarding command execution
- Thermostats provide only temperature and setting data (no status feedback)
- Maximum 3°F deviation allowed before overtemperature alarms
- ASCII format required for all generated reports

## Undecided Issues
- Specific hardware interface implementation for unit control signals
- Database schema details for event storage
- Supervisor interface window design and layout
- Initialization file format specifications
- Alarm reset mechanism implementation details