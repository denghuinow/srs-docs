# Software Requirements Specification (SRS)
## The Energy Management System (THEMAS)

**Document Version:** 1.0
**Date:** October 26, 2023
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for The Energy Management System (THEMAS). It is intended to serve as a complete description of the system's intended capabilities, behavior, and constraints for the Design Requirements Team, Principle Software Architect, developers, testers, and project managers.

#### 1.2 Scope
THEMAS is an independent software system designed to monitor and control heating and cooling (H/C) units in a multi-floor office building. Its primary objectives are:
1.  To maintain desired temperatures within defined comfort and safety limits.
2.  To optimize overall energy usage by limiting the number of H/C units operating concurrently.

The scope of this document is confined to the software requirements. It assumes the existence of specific hardware interfaces for thermostats and H/C units and specifies that the software will operate on the Microsoft Windows NT operating system.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **H/C Unit:** Heating or Cooling Unit.
*   **TD (Trigger Delta):** The temperature deviation from the setting (TSET) that triggers a request for heating or cooling.
*   **OD (Overtemperature Delta):** The temperature deviation from the setting (TSET) that triggers a system alarm.
*   **TSET:** The desired temperature setting for a specific thermostat.
*   **T:** The current temperature reading from a thermostat.
*   **LIFO:** Last-In, First-Out (a queuing strategy).
*   **SRS:** Software Requirements Specification.
*   **SDD:** Software Design Document.

#### 1.4 References
*   Hardware Interface Specifications for Thermostats and H/C Units (TBD - External Document).
*   Microsoft Windows NT System Documentation.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its stakeholders, and operating environment. Section 3 details the specific functional and non-functional requirements. Appendices may contain supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
THEMAS is a standalone supervisory control and data acquisition (SCADA) application. It interfaces with physical thermostats (for input) and H/C unit controllers (for output) within the building's infrastructure. The system maintains an internal state and log database (Microsoft Access) to manage operations and provide reporting.

#### 2.2 Product Functions (Summary)
1.  System initialization and configuration loading.
2.  Continuous monitoring and validation of thermostat data.
3.  Automated determination of heating/cooling needs.
4.  Management of H/C unit activation within concurrency limits.
5.  Generation of control signals for H/C units.
6.  Audible alarm generation for fault conditions.
7.  Comprehensive logging of all system events.
8.  Supervisor interface for monitoring, manual override, and report generation.

#### 2.3 User Characteristics
| Stakeholder | Role & Interaction |
| :--- | :--- |
| **Supervisor** | Primary user. Responsible for monitoring system status, responding to alarms, manually adjusting settings, and generating reports. Has general technical proficiency. |
| **Design Requirements Team** | Uses this SRS to create the system design (SDD). |
| **Principle Software Architect** | Uses this SRS to oversee technical development and ensure architectural alignment. |
| **Building Occupants** | Indirect users. Experience the environmental conditions controlled by THEMAS. No direct interaction with the software. |

#### 2.4 Constraints
1.  **Platform:** Must operate on Microsoft Windows NT.
2.  **Database:** Must utilize Microsoft Access for event logging.
3.  **Hardware Assumption:** Assumes no real-time delay in communication with thermostat and H/C unit hardware.
4.  **Feedback:** The system cannot receive confirmation feedback from H/C units upon command execution.
5.  **Queuing:** Initial implementation uses a LIFO queue for managing denied H/C requests.

#### 2.5 Assumptions and Dependencies
*   The hardware interface specifications for thermostats and H/C units will be provided externally and are a critical dependency for detailed design.
*   A simulated thermostat prototype will be developed for system testing.
*   The Windows NT development and deployment environment will be available.

### 3. Specific Requirements

#### 3.1 External Interface Requirements
**3.1.1 User Interfaces**
*   **SRS-UI-001:** The system shall provide a graphical supervisor interface window.
*   **SRS-UI-002:** The interface shall display a clear status overview, including active alarms, number of H/C units currently running, and system mode.
*   **SRS-UI-003:** The interface shall provide a mechanism for the supervisor to view a list of all thermostats and their current temperature (T), setting (TSET), and status.
*   **SRS-UI-004:** The interface shall allow the supervisor to manually change the TSET for any selected thermostat from a list of valid temperatures.
*   **SRS-UI-005:** The interface shall provide a clear button or command to reset active audible alarms.
*   **SRS-UI-006:** The interface shall provide functions to generate and save operational history and statistical summary reports.

**3.1.2 Hardware Interfaces**
*   **SRS-HI-001:** The system shall interface with building thermostats to receive current temperature (T) and setting (TSET) data. *(Protocol TBD)*.
*   **SRS-HI-002:** The system shall interface with H/C unit controllers to send ON/OFF control signals. *(Protocol TBD)*.

**3.1.3 Software Interfaces**
*   **SRS-SI-001:** The system shall read operational parameters (TD, OD, Valid Range, Max Concurrent Units) from an initialization file at startup.
*   **SRS-SI-002:** The system shall write all system events to a Microsoft Access database.
*   **SRS-SI-003:** The system shall generate report files in ASCII format.

#### 3.2 Functional Requirements
**3.2.1 System Initialization & Configuration**
*   **SRS-FUNC-001:** Upon startup, the system shall load all operational parameters from a predefined initialization file.
*   **SRS-FUNC-002:** Upon startup, the system shall initialize all H/C units to an OFF state.
*   **SRS-FUNC-003:** If the initialization file is missing or corrupted, the system shall log a critical error, generate an audible alarm, and terminate operation.

**3.2.2 Data Acquisition & Validation**
*   **SRS-FUNC-004:** The system shall periodically poll/receive temperature data (T, TSET) from all configured thermostats.
*   **SRS-FUNC-005:** The system shall validate that all incoming temperature values (T and TSET) are within the defined "Valid Temperature Range."
*   **SRS-FUNC-006:** If an invalid temperature is detected, the system shall generate an "Invalid Temperature" audible alarm, log the event, and ignore the invalid data for processing.

**3.2.3 Temperature Processing & Decision Logic**
*   **SRS-FUNC-007:** For valid data, the system shall calculate the difference between T and TSET (ΔT = T - TSET).
*   **SRS-FUNC-008:** If |ΔT| > OD, the system shall generate an "Overtemperature Limit Exceeded" audible alarm and log the event.
*   **SRS-FUNC-009:** If |ΔT| > TD, the system shall initiate a request for a Heating or Cooling unit.
*   **SRS-FUNC-010:** The mode (Heating/Cooling) shall be determined by the sign of ΔT: If ΔT < -TD, request Heating. If ΔT > TD, request Cooling.

**3.2.4 H/C Unit Utilization Management**
*   **SRS-FUNC-011:** The system shall maintain a count of currently active H/C units.
*   **SRS-FUNC-012:** Before approving an H/C request, the system shall check if the count of active units is below the "Max Concurrent Units" limit.
*   **SRS-FUNC-013:** If below the limit, the request shall be approved, the unit count incremented, and a control signal generated.
*   **SRS-FUNC-014:** If the limit is reached, the request shall be denied and placed into a LIFO queue. This denial shall be logged.
*   **SRS-FUNC-015:** When an H/C unit is turned off, the system shall decrement the active unit count and check the queue. If requests are queued, the most recently denied request (LIFO) shall be processed and approved.

**3.2.5 Control & Actuation**
*   **SRS-FUNC-016:** For an approved Heating request where ΔT < -TD, the system shall send an ON signal to the Heating unit associated with the source thermostat.
*   **SRS-FUNC-017:** For an approved Cooling request where ΔT > TD, the system shall send an ON signal to the Cooling unit associated with the source thermostat.
*   **SRS-FUNC-018:** When T returns to within the TD limit (|ΔT| <= TD), the system shall send an OFF signal to the corresponding H/C unit.

**3.2.6 Event Logging & Reporting**
*   **SRS-FUNC-019:** The system shall log all events (Alarms, H/C Unit Status Changes: ON/OFF, Denied Requests, Manual TSET Changes) to the database.
*   **SRS-FUNC-020:** Each log entry shall include: a unique Event ID, Timestamp (system time), Event Type, Source (Thermostat or H/C Unit ID), and a Description.
*   **SRS-FUNC-021:** The system shall provide a function to generate an **Operational History Report** for a user-specified time period, listing all logged events in chronological order.
*   **SRS-FUNC-022:** The system shall provide a function to generate a **Statistical Summary Report** for a user-specified time period, including metrics such as: total H/C unit runtime, number of alarms, number of denied requests, and energy usage estimates.

**3.2.7 Supervisor Functions**
*   **SRS-FUNC-023:** The supervisor shall be able to manually change the TSET for any thermostat. The new TSET must be chosen from a predefined list of valid temperatures.
*   **SRS-FUNC-024:** The supervisor shall be able to acknowledge and reset any active audible alarm via the interface.
*   **SRS-FUNC-025:** The supervisor shall be able to command the generation and saving of reports (SRS-FUNC-021, SRS-FUNC-022) to a specified file location.

#### 3.3 Non-Functional Requirements
*   **SRS-NFR-001 (Platform):** The system shall be designed and implemented to run on the Microsoft Windows NT operating system.
*   **SRS-NFR-002 (Reliability):** A prototype simulated thermostat shall be developed and delivered for verification and validation of system reliability.
*   **SRS-NFR-003 (Usability):** The supervisor interface shall present information clearly and concisely, avoiding information overload and confusing layouts.
*   **SRS-NFR-004 (Data Integrity):** All system events shall be recorded with a consistent description and the current system time. Log entries shall be immutable once written.
*   **SRS-NFR-005 (Interoperability):** The software interfaces for thermostats and H/C units shall be compatible with the Windows NT operating system.
*   **SRS-NFR-006 (Performance):** The system architecture shall be based on the assumption of no real-time delay in hardware communication. Internal processing of valid data shall occur within one second of receipt.

#### 3.4 Data Model (Entity Summary)
The system will manage the following core data entities:
*   **Thermostat:** ID (PK), Current Temp (T), Temp Setting (TSET), Location, Status.
*   **H/C Unit:** ID (PK), Associated Thermostat ID (FK), Type (Heat/Cool), Status (On/Off).
*   **Operational Parameters:** Parameter Set (PK), TD, OD, Valid Temp Range (Min, Max), Max Concurrent Units.
*   **System Event:** Event ID/Timestamp (PK), Type, Source ID, Description, Timestamp.
*   **Alarm:** Alarm ID/Timestamp (PK), Type, Source Thermostat ID, Status.
*   **Report:** Report ID/GenTime (PK), Type, Time Period, Data Summary, File Path.

### 4. Appendices

#### 4.1 Risks and Mitigation Strategies
| Risk | Mitigation Strategy |
| :--- | :--- |
| Undefined hardware interfaces. | Isolate interface code using abstraction layers (e.g., Device Drivers). Develop interface mock-ups for parallel development and testing. |
| Assumption of no communication delay may be invalid. | Timestamp all incoming data. Design core logic to be state-based rather than purely sequential, allowing for minor timing variances. |
| No feedback from H/C units on command execution. | Implement detailed logging of command signals and expected state changes. Design supervisor procedures for manual system health verification. |
| LIFO queuing may impact comfort. | Document as a known constraint/limitation in Version 1.0. Architect the queuing module to allow for pluggable algorithms (e.g., FIFO, Priority) in future versions. |
| Microsoft Access may not scale. | Implement automated report generation and data archival policies. Document the database schema to facilitate future migration to a more scalable RDBMS (e.g., SQL Server). |

#### 4.2 Undecided Issues (TBD)
1.  The exact format, protocol, and API for thermostat and H/C unit control signals (SRS-HI-001, SRS-HI-002).
2.  The specific GUI control (e.g., button, menu) and data structure for the alarm reset function (SRS-UI-005).
3.  The file naming convention (e.g., `Report_Ops_YYYYMMDD_HHMM.txt`) and default directory for generated ASCII report files (SRS-FUNC-025).
4.  The process and interface for dynamically adding or removing thermostats/H/C units from the system configuration post-deployment.
5.  The definitive list of "valid temperatures" (e.g., increments of 0.5°C between 18°C and 26°C) presented to the supervisor for manual TSET change (SRS-FUNC-023).
6.  Detailed error handling and recovery procedures for a corrupted initialization file beyond SRS-FUNC-003.

---
*This document has been prepared based on the provided project summary and constitutes the formal Software Requirements Specification for THEMAS.*