# Short Summary

- **Background and objectives**: THEMAS is an independent energy management system designed to monitor building temperatures and control heating/cooling units efficiently. It aims to maintain temperature settings within defined limits while managing unit utilization.

- **In scope**:
  - Monitor temperature and determine heating/cooling mode
  - Control heating/cooling unit activation based on utilization limits
  - Generate system reports and alarm events
  - Initialize system parameters from configuration files
  - Validate temperature readings and thermostat settings

- **Out of scope**:
  - Detailed design of external thermostat or HVAC hardware interfaces
  - Real-time feedback from heating/cooling units
  - User interface design specifications
  - Database schema implementation details
  - Network communication protocols

- **Roles and core use cases**:
  - As a supervisor, I want to change thermostat settings so that I can adjust temperature requirements
  - As a supervisor, I want to generate operational reports so that I can analyze system performance
  - As a system maintainer, I want to initialize operational parameters so that the system starts in a known state

- **Success metrics**:
  - Temperature maintained within ±3°F of setting
  - Maximum concurrent unit utilization not exceeded
  - All system events properly logged and reportable

- **Major constraints**:
  - Must run on Microsoft Windows NT operating system
  - No feedback from heating/cooling units on command execution
  - Thermostats provide only temperature and setting data
  - Maximum deviation of 3°F from temperature setting
  - Database storage using Microsoft Access

- **Undecided issues**:
  - Specific hardware interface implementation for HVAC units
  - Network communication protocols with thermostats
  - User interface design details
  - Database performance optimization
  - Real-time monitoring display format