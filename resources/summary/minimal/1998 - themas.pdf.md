**Purpose & Scope**
The system manages heating and cooling (H/C) units in a building based on thermostat data to maintain temperature settings and log events. It defines software requirements only, excluding detailed external system interfaces.

**Core Functions**
*   Monitor temperature from thermostats and determine if H/C action is required.
*   Determine H/C unit utilization, respecting a maximum concurrent unit limit.
*   Initialize system parameters and turn all H/C units to a known state.
*   Generate system reports from logged event data.

**Key Users**
*   Building system supervisor.

**Key Constraints**
*   Thermostats provide only temperature and setpoint data with no feedback capability.
*   H/C units receive on/off signals but provide no status confirmation to the system.
*   The software must operate on the Microsoft Windows NT operating system.