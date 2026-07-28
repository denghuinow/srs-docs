**Purpose & Scope**
The system provides the physical link and primary interface to configure, operate, and service the WIDAR Correlator hardware for the EVLA. It translates configuration data from the EVLA Monitor & Control system, handles real-time monitor/control data, monitors hardware health, and performs limited real-time data processing. It does not include the correlator hardware itself or the backend data processing system.

**Product Background / Positioning**
The Correlator Monitor and Control System is an integrated component of the overall EVLA Monitor and Control structure. It acts as a modularizing abstraction layer, isolating the correlator hardware from the broader EVLA environment. Its primary external interfaces are with the EVLA M&C system and the Correlator Backend Data Processing system.

**Core Functional Overview**
1.  Translate EVLA M&C configuration data into specific hardware configuration commands.
2.  Monitor all correlator subsystem states and health.
3.  Process and transfer dynamic control data and monitor data to/from the hardware.
4.  Automatically attempt recovery from hardware and computing system faults.
5.  Provide real-time data probing tools (e.g., display auto-correlation products).
6.  Output specific data sets to the Backend Data Processing System.
7.  Accept external data feeds for models, time standards, and phase corrections.

**Key Users & Usage Scenarios**
*   **Array Operators:** Primarily receive status and error messages channeled through the EVLA M&C system.
*   **Engineers & Technicians:** Perform maintenance, diagnosis, and repair using tools for remote inspection and fault tracing to specific hardware modules.
*   **Software Developers:** Require remote access for development, troubleshooting, and ensuring proper system function.
*   **Administrators:** Have unrestricted access to all system aspects for user and security management.

**Major External Interfaces**
*   **EVLA M&C System:** Interface over a dedicated, physically separate Ethernet/fiber network for configuration and high-level control.
*   **Correlator Backend Data Processing System:** Interface over a secondary virtual network for outputting specific data sets (e.g., auto-correlations).
*   **Correlator Hardware:** Interface via CMIB modules connected to carrier boards via PCI/ISA or serial/parallel busses.

**Key Non-functional Requirements**
*   **Reliability/Availability:** The system is critical; its unavailability causes astronomical data loss. It must self-monitor and auto-correct failures (processor, OS, comms). Software must run between maintenance windows without total restart.
*   **Performance:** Must meet all data processing deadlines and respond to hardware interrupts deterministically to avoid data loss/corruption.
*   **Security:** All users must login with unique identification. Access is restricted to authorized personnel, with an administrator role having full control.
*   **Maintainability:** All hardware must be readily accessible for repair/replacement. Software must be debuggable, with processes killable/restartable with minimal operational impact.
*   **Serviceability:** Designed with modular, hot-swappable components where possible to allow partial shutdowns for upgrades without full system outage.

**Constraints, Assumptions & Dependencies**
*   **Constraints:** The system is a critical component; data loss occurs if it is unavailable. It must use a master/slave network topology with isolated networks.
*   **Assumptions:** Configuration data received from EVLA M&C is unambiguous and valid. All required auxiliary data (delay models, etc.) is provided by external systems. External systems can accept the CMCS output data rates.
*   **Dependencies:** Functionality depends on the stability of the CMCS network and control computers. Requires specific external data feeds from the EVLA M&C or dedicated servers.

**Priorities & Acceptance Approach**
Core functions of configuration translation, monitoring, and fault recovery are critical. High availability, reliability, and security are paramount. Acceptance will involve verifying the system meets real-time performance deadlines, operates within specified reliability metrics, enforces security access controls, and successfully interfaces with the EVLA M&C and Backend systems.