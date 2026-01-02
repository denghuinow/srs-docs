# Software Requirements Specification (SRS)
## Heating and Cooling (H/C) Unit Management System

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Heating and Cooling (H/C) Unit Management System. The intended audience includes project stakeholders, software developers, testers, and the building system supervisor. This document serves as the foundation for system design, implementation, and verification.

#### 1.2 Scope
The system is a software application that autonomously manages a building's heating and cooling infrastructure. It monitors thermostat data, makes logic-based decisions to activate or deactivate H/C units within defined constraints, maintains an event log, and provides reporting capabilities. This specification covers software requirements only; detailed hardware interfaces for thermostats and H/C units are excluded.

**In-Scope:**
*   Software logic for temperature monitoring and H/C unit control.
*   Management of concurrent unit limits.
*   System initialization and state management.
*   Event logging and report generation.
*   User interface for the building system supervisor.

**Out-of-Scope:**
*   Design and specification of thermostat or H/C unit hardware.
*   Low-level communication drivers or protocols.
*   Physical installation or network configuration.
*   Operating system development or modification.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **H/C Unit:** A single Heating or Cooling unit (e.g., furnace, chiller, AC unit).
*   **Setpoint:** The desired temperature configured for a specific thermostat zone.
*   **Deadband:** A temperature range around the setpoint where no H/C action is taken to prevent short-cycling.
*   **Concurrent Limit:** The maximum number of H/C units allowed to operate simultaneously.
*   **Supervisor:** The primary user, the Building System Supervisor.
*   **Windows NT:** The specified Microsoft Windows NT operating system.

#### 1.4 References
*   IEEE Std 830-1998: Recommended Practice for Software Requirements Specifications.
*   Project Charter: H/C Management System, Version 1.0.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details the specific functional and non-functional requirements. Appendices may include supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
The system is a standalone, operator-controlled software application. It acts as the central decision-making component between input devices (thermostats) and output devices (H/C units). The system has no feedback loop from the H/C units, operating on an "open-loop" control basis.

#### 2.2 Product Functions (Summary)
1.  **Temperature Monitoring & Decision Making:** Continuously poll thermostats, compare current temperature to setpoint, and determine if heating or cooling action is required.
2.  **Unit Allocation & Limiting:** Select specific H/C units to activate, ensuring the total number running concurrently never exceeds a configurable maximum.
3.  **System Initialization:** Set all configurable parameters and force all H/C units to a known 'off' state on startup or command.
4.  **Event Logging:** Record all significant system events (e.g., temperature deviations, unit activations/deactivations, errors).
5.  **Reporting:** Generate, display, and export reports based on the logged event data for analysis.

#### 2.3 User Characteristics
*   **Primary User: Building System Supervisor.**
    *   **Expertise:** Has deep knowledge of the building's HVAC infrastructure and operational policies.
    *   **Tasks:** Configure system parameters (setpoints, limits, deadbands), initialize the system, monitor status, and generate/analyze reports.
    *   **Frequency:** Daily monitoring, weekly reporting, occasional parameter adjustment.

#### 2.4 Constraints
1.  **Hardware Interface Constraint:** Thermostats are read-only sensors providing only `(Temperature, Setpoint)` data pairs. The system cannot send commands to thermostats.
2.  **Hardware Interface Constraint:** H/C units accept simple `ON`/`OFF` commands. The system receives no status, confirmation, or fault feedback from the units.
3.  **Software Constraint:** The application must be developed to run on the **Microsoft Windows NT** operating system.
4.  **Design Constraint:** Control logic must account for the lack of H/C unit feedback, incorporating safety timers and assumptions about unit state.

#### 2.5 Assumptions and Dependencies
*   It is assumed thermostats provide accurate and timely data.
*   It is assumed H/C units respond reliably to `ON`/`OFF` signals.
*   The system depends on a stable and correctly configured hardware communication layer (e.g., serial, network) to interact with thermostats and H/C units, though its specification is outside this document.
*   The Windows NT system will have sufficient processing power and memory to run the application.

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 User Interfaces
*   **UI-1:** A graphical main console showing real-time status of all thermostats (temp, setpoint, deviation) and H/C units (commanded state: ON/OFF).
*   **UI-2:** A configuration dialog for setting global and zone-specific parameters (see FR-2).
*   **UI-3:** A report generation interface allowing selection of date ranges and report types (see FR-7).
*   **UI-4:** An initialization/panic button to immediately execute the initialization sequence (FR-4).

##### 3.1.2 Hardware Interfaces (Logical)
*   **HI-1:** The system shall have a method to read a data stream containing identifiers, current temperature, and setpoint for all configured thermostats.
*   **HI-2:** The system shall have a method to send a discrete `ON` or `OFF` command to any individually addressable H/C unit.

#### 3.2 Functional Requirements

##### **FR-1: Temperature Monitoring & Analysis**
*   **FR-1.1:** The system shall poll data from all configured thermostats at a configurable interval (default: 60 seconds).
*   **FR-1.2:** For each thermostat, the system shall calculate the difference between the current temperature and its setpoint.
*   **FR-1.3:** The system shall employ a configurable deadband (±0.5°C default). If the temperature is below (setpoint - deadband), a heating demand shall be registered for that zone. If above (setpoint + deadband), a cooling demand shall be registered.

##### **FR-2: System Configuration**
*   **FR-2.1:** The system shall allow the supervisor to configure, store, and load:
    *   Polling interval.
    *   Global deadband value.
    *   Maximum concurrent H/C units allowed.
    *   Thermostat-to-H/C unit zone mappings.
    *   Individual thermostat setpoints.

##### **FR-3: H/C Unit Control Logic**
*   **FR-3.1:** Upon identifying a heating or cooling demand (FR-1.3), the system shall determine the appropriate H/C unit(s) assigned to that zone.
*   **FR-3.2:** Before activating a unit, the system shall check the current count of commanded-`ON` units.
*   **FR-3.3:** If activating a new unit would exceed the **Maximum Concurrent Limit**, the system shall not activate it and shall log a "Unit Activation Throttled" event.
*   **FR-3.4:** The system shall implement a minimum run-time and minimum off-time (e.g., 5 minutes) for each H/C unit to prevent short-cycling, based on its own commanded state history.

##### **FR-4: System Initialization**
*   **FR-4.1:** On application startup or upon supervisor command, the system shall load the saved configuration.
*   **FR-4.2:** The system shall send an `OFF` command to every configured H/C unit to establish a known baseline state.
*   **FR-4.3:** The system shall clear its internal unit state timers and begin the monitoring cycle.

##### **FR-5: Event Logging**
*   **FR-5.1:** The system shall log all significant events with a timestamp, event type, and relevant details (e.g., zone ID, unit ID, temperature).
*   **FR-5.2:** Required log events include, but are not limited to:
    *   System start/stop/initialization.
    *   Temperature poll and detected demand.
    *   H/C unit `ON`/`OFF` command issued.
    *   Concurrent limit reached (throttling event).
    *   Configuration change.

##### **FR-6: Data Persistence**
*   **FR-6.1:** The system shall persistently store configuration parameters to a local file or database.
*   **FR-6.2:** The system shall persistently store event log data to a local file or database, protected from loss on application restart.

##### **FR-7: Reporting**
*   **FR-7.1:** The system shall generate a **Unit Utilization Report** showing total runtime per H/C unit over a selected period.
*   **FR-7.2:** The system shall generate a **Temperature Deviation Report** showing instances and durations where zones were outside their deadband.
*   **FR-7.3:** The system shall generate an **Event Summary Report** listing all logged events filtered by date and type.
*   **FR-7.4:** Reports shall be viewable within the application and exportable to a common format (e.g., CSV, PDF).

#### 3.3 Non-Functional Requirements

##### **3.3.1 Performance Requirements**
*   **PER-1:** The system shall process a poll cycle for up to 50 thermostats and decide on necessary H/C actions within 10 seconds of receiving all thermostat data.
*   **PER-2:** The user interface shall respond to supervisor inputs (clicks, keystrokes) within 2 seconds.

##### **3.3.2 Safety Requirements**
*   **SAF-1:** Due to lack of feedback, the system shall maintain an internal "assumed state" for each H/C unit and shall not issue a new command to a unit until its minimum runtime or offtime timer (FR-3.4) has expired.
*   **SAF-2:** The initialization function (FR-4) shall be always accessible to allow the supervisor to force all units to a safe `OFF` state.

##### **3.3.3 Software Quality Attributes**
*   **REL-1:** The core control and monitoring service shall have an uptime requirement of 99.5% during scheduled building operation hours.
*   **USC-1:** All configuration and reporting functions shall be accomplishable with no more than three dialog layers from the main console.
*   **MAI-1:** All configurable parameters shall be modifiable without requiring a code change or system recompilation.

##### **3.3.4 Platform Requirement**
*   **PLAT-1:** The software application shall be designed, built, and tested to operate correctly on the **Microsoft Windows NT** operating system.

---
***End of Document***