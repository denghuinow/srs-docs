# Software Requirements Specification (SRS)
## Temperature Control and Management System (TCMS)
**Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Temperature Control and Management System (TCMS). It is intended for use by the project stakeholders, including developers, testers, project managers, and system architects, to ensure a common understanding of the system to be developed.

#### 1.2 Scope
The TCMS is a software application designed to automatically manage the heating and cooling units within a building to maintain ambient temperature within user-defined setpoints. The system monitors temperature inputs from one or more thermostats, makes logic-based decisions to activate or deactivate HVAC units, and maintains logs of all significant events and system actions for reporting and audit purposes.

**In-Scope:**
*   Software for temperature monitoring and unit control logic.
*   Event logging and report generation functionality.
*   User interface for configuration and monitoring.
*   System operation within the defined hardware and software constraints.

**Out-of-Scope:**
*   Manufacturing or maintenance of physical thermostats or HVAC units.
*   Network infrastructure or communication protocols for thermostats/units (assumed as given).
*   Advanced predictive maintenance or AI-based optimization.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **TCMS:** Temperature Control and Management System.
*   **HVAC:** Heating, Ventilation, and Air Conditioning.
*   **Setpoint:** The desired target temperature for a zone.
*   **Deadband:** A temperature range around the setpoint where neither heating nor cooling is activated to prevent short-cycling.
*   **Utilization Limit:** The maximum number of heating or cooling units allowed to operate simultaneously.
*   **SRS:** Software Requirements Specification.

#### 1.4 References
*   IEEE Std 830-1998: IEEE Recommended Practice for Software Requirements Specifications.
*   Project Charter: TCMS-PC-1.0.

#### 1.5 Overview
The remainder of this SRS is organized as follows: Section 2 provides a general description of the product. Section 3 details all specific requirements, including functional, interface, and non-functional requirements.

---

### 2. Overall Description

#### 2.1 Product Perspective
The TCMS is a standalone control software that interfaces with existing building hardware. It acts as the central decision-making component between sensor inputs (thermostats) and actuator outputs (HVAC units). The system does not receive feedback from the units, operating on an "open-loop" control basis for unit activation.

#### 2.2 Product Functions (Summary)
1.  **Temperature Monitoring:** Continuously read temperature data from configured thermostats.
2.  **Setpoint Management:** Allow configuration of temperature setpoints and deadbands for controlled zones.
3.  **Control Logic:** Determine the need for heating or cooling by comparing current temperature to setpoints.
4.  **Unit Management:** Activate or deactivate specific heating/cooling units based on control logic and system-wide utilization limits.
5.  **Event Logging:** Record all system events (e.g., temperature readings, unit state changes, alarms, user actions).
6.  **Reporting:** Generate and display operational reports based on logged event data.
7.  **System Configuration:** Provide an interface for setting system parameters (setpoints, limits, thermostat/unit mappings).

#### 2.3 User Characteristics
*   **Facility Manager:** Primary user. Technically proficient, responsible for system configuration, monitoring system status, and generating reports.
*   **Maintenance Technician:** Secondary user. Uses the system to view logs and diagnose potential issues.

#### 2.4 Constraints
1.  **Platform Constraint:** The system shall be developed to run on the Microsoft Windows NT operating system.
2.  **Hardware Feedback Constraint:** The heating and cooling units provide no status feedback (e.g., confirmation of on/off, fault conditions) to the TCMS. The system assumes command execution is successful.
3.  **Concurrency Constraint:** A configurable maximum number of heating/cooling units can be active concurrently to prevent electrical overload.
4.  **Legacy System Interface:** The system must interface with existing thermostat and unit control hardware using predefined communication protocols (to be specified in the Design Document).

#### 2.5 Assumptions and Dependencies
*   Thermostats provide accurate and timely temperature readings.
*   Commands sent to HVAC units are executed reliably by the underlying hardware controllers.
*   The system has exclusive control over the HVAC units it manages.
*   A failure of the TCMS software will result in no new commands being sent to HVAC units; existing unit states will persist.

---

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 User Interfaces
*   **UI-FR-1:** The system shall provide a graphical user interface (GUI) for all configuration and monitoring tasks.
*   **UI-FR-2:** The main dashboard shall display real-time temperature readings from all thermostats and the status (ON/OFF, as assumed by TCMS) of all managed units.
*   **UI-FR-3:** The interface shall provide forms to configure temperature setpoints, deadbands, and system-wide utilization limits.

##### 3.1.2 Hardware Interfaces
*   **HW-FR-1:** The system shall interface with digital thermostats via a specified serial/network protocol (e.g., Modbus RTU, BACnet MS/TP) to read temperature values.
*   **HW-FR-2:** The system shall interface with HVAC unit relay controllers via a specified digital output protocol to send ON/OFF commands.

##### 3.1.3 Software Interfaces
*   **OS-FR-1:** The system shall utilize Windows NT system APIs for file I/O (logging) and system time.
*   **OS-FR-2:** The system shall run as a Windows Service to ensure background operation and automatic startup.

#### 3.2 Functional Requirements

##### 3.2.1 Temperature Monitoring
*   **FUNC-1:** The system shall poll all configured thermostats at a configurable interval (default: 60 seconds).
*   **FUNC-2:** The system shall validate received temperature data against a plausible range (e.g., -10°C to 60°C) and log an error for invalid readings.

##### 3.2.2 Temperature Control Logic
*   **FUNC-3:** For each controlled zone, the system shall compare the current temperature (`T_current`) to the heating setpoint (`T_heat`) and cooling setpoint (`T_cool`), considering the deadband (`DB`).
*   **FUNC-4:** If `T_current < (T_heat - DB/2)`, the system shall determine that heating is required for that zone.
*   **FUNC-5:** If `T_current > (T_cool + DB/2)`, the system shall determine that cooling is required for that zone.
*   **FUNC-6:** If `T_current` is within the deadband range `[T_heat - DB/2, T_cool + DB/2]`, the system shall determine that no action is required for that zone.

##### 3.2.3 Unit Activation Management
*   **FUNC-7:** The system shall maintain a prioritized list of available heating units and cooling units.
*   **FUNC-8:** When heating/cooling is required, the system shall activate units from the appropriate list in priority order.
*   **FUNC-9:** The system shall never exceed the globally configured **Utilization Limit** for active units. If a new unit activation request would exceed this limit, the request shall be queued until a unit becomes inactive.
*   **FUNC-10:** The system shall implement a minimum runtime (e.g., 5 minutes) and minimum off-time (e.g., 3 minutes) for each unit to prevent short-cycling.
*   **FUNC-11:** When a zone's temperature returns to within the deadband, the system shall deactivate the associated unit(s) after the minimum runtime has been satisfied.

##### 3.2.4 Logging and Reporting
*   **FUNC-12:** The system shall log all significant events with a timestamp, event type, and relevant details to a persistent, rolling log file.
    *   Event types include: `TEMPERATURE_READ`, `UNIT_ACTIVATE`, `UNIT_DEACTIVATE`, `CONFIG_CHANGE`, `SYSTEM_ERROR`.
*   **FUNC-13:** The system shall provide a report generation feature that can filter logs by date/time range and event type.
*   **FUNC-14:** The system shall generate a daily summary report showing total runtime per unit and energy consumption estimates (based on unit power ratings).

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance Requirements
*   **PERF-1:** The control loop (poll temperature, execute logic, send commands) shall complete within 10 seconds for a system managing up to 50 units and 20 thermostats.
*   **PERF-2:** The user interface shall respond to any user input within 2 seconds.

##### 3.3.2 Safety Requirements
*   **SAFE-1:** Under no condition shall the system activate heating and cooling units for the same zone simultaneously.
*   **SAFE-2:** The system shall include a manual "System Override" mode to deactivate all automated control and allow manual unit operation.

##### 3.3.3 Reliability & Availability
*   **RELY-1:** The system shall have a mean time between failures (MTBF) of not less than 720 hours (30 days) of continuous operation.
*   **RELY-2:** The system service shall automatically restart upon an unexpected termination, as configured by the Windows Service Control Manager.

##### 3.3.4 Security Requirements
*   **SEC-1:** Access to the configuration interface shall be protected by a username and password.
*   **SEC-2:** Log files shall be append-only from the application's perspective to prevent tampering.

##### 3.3.5 Portability
*   **PORT-1:** The system is required to run only on the Microsoft Windows NT operating system, as per the key constraint.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Architect | | | |
| QA Manager | | | |