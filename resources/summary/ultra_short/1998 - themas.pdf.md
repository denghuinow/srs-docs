**Purpose & Scope**
The system is an Energy Management System (THEMAS) that autonomously controls heating and cooling units in a building based on thermostat readings. Its purpose is to maintain desired temperatures while limiting the number of concurrently active units. It does not receive feedback from the heating/cooling units to confirm command execution.

**Product Background / Positioning**
THEMAS is a standalone system comprising separate hardware and software components. This specification covers only the software portion. It interfaces with thermostats and heating/cooling unit hardware but operates independently of other building systems.

**Core Functional Overview**
*   Monitor temperature from thermostats and validate readings against a defined range.
*   Determine when a heating or cooling unit must be activated or deactivated based on temperature deviations.
*   Manage a limited pool of available heating/cooling units, queuing requests when the maximum concurrent usage is reached.
*   Generate audible alarms for invalid temperature readings or critically exceeded temperature limits.
*   Log all system events (e.g., unit activations, denied requests, alarms) to a database.
*   Allow a supervisor to manually change individual thermostat settings.
*   Generate operational history and statistical summary reports from the event log.

**Key Users & Usage Scenarios**
The primary user is a building supervisor responsible for system maintenance. The supervisor monitors the system, responds to alarms, manually adjusts thermostat settings, and generates reports. The system otherwise operates automatically without user intervention.

**Major External Interfaces**
The system interfaces with thermostats (for temperature data and settings), heating/cooling unit hardware (for control signals), a supervisor's computer (for the user interface and alarms), and a Microsoft Access database (for event logging).

**Key Non-functional Requirements**
*   The software must run on the Microsoft Windows NT operating system.
*   The system must ensure a reported temperature does not deviate from its setting by more than 3 degrees Fahrenheit before triggering a critical alarm.
*   Alarms must be audible tones with specified frequencies and durations until manually acknowledged.
*   All event data must be stored persistently in the specified database.

**Constraints, Assumptions & Dependencies**
*   Thermostats provide temperature data and settings in the correct format with no delay.
*   Heating/Cooling units cannot report their status back to THEMAS.
*   The control signal interface to the heating/cooling units is to be determined (TBD).
*   The system is designed for a specific building layout (four quadrants per floor, three floors).

**Priorities & Acceptance Approach**
Core priorities are reliable temperature monitoring, enforcement of the unit utilization limit, and correct alarm generation. Acceptance will involve verifying system behavior against the defined temperature trigger/overtemperature logic and validating report generation from the event database. A simulated thermostat will be used for reliability testing.