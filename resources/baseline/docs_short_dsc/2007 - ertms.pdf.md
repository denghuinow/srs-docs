# Software Requirements Specification (SRS)
## ERTMS/ETCS Functional Requirements Specification (FRS) - Version 5.00

**Document ID:** SRS-ERTMS-ETCS-FRS-5.00  
**Version:** 1.0  
**Date:** [Date of Generation]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document formally defines the functional requirements for the European Rail Traffic Management System / European Train Control System (ERTMS/ETCS) as per the Functional Requirements Specification (FRS) version 5.00. It serves as the authoritative source for system integrators, developers, safety assessors, and stakeholders to understand the mandatory and optional operational capabilities required for interoperability and safe train control across European and national rail networks.

#### 1.2 Document Conventions
*   **Mandatory (M):** Requirements tagged with **(M)** are compulsory for all implementations.
*   **Optional (O):** Requirements tagged with **(O)** may be implemented based on national or project-specific needs.
*   Keywords such as **SHALL**, **SHOULD**, and **MAY** are used in accordance with IETF RFC 2119.
*   All requirements are uniquely identified (e.g., `FR-XXX`).

#### 1.3 Intended Audience and Reading Suggestions
*   **System Integrators & Suppliers:** Focus on Sections 2 (Overall Description), 3 (Specific Requirements), and 5 (Constraints).
*   **Safety Regulators & Assessors:** Focus on Sections 1.4 (Scope), 3 (Specific Requirements - particularly failure handling), and 4 (Success Metrics).
*   **Project Managers & Stakeholders:** Focus on Sections 1 (Introduction), 2.3 (User Characteristics), and 6 (Undecided Issues).
*   **Test Engineers:** Focus on Section 3 (Specific Requirements) to derive test cases.

#### 1.4 Project Scope
This SRS covers the **functional and operational requirements** for ETCS onboard and trackside equipment. It defines *what* the system must do, not *how* it is to be implemented.

**In-Scope Items:**
*   Definition of ETCS application levels (0, 1, 2, 3, STM) and operational modes/states (e.g., Full Supervision, Shunting).
*   Core supervision functions: Train data entry, speed profile calculation, Movement Authority (MA) supervision, train location determination.
*   Driver-Machine Interface (DMI) functional requirements for information display (speed, distance, warnings, system status).
*   Failure management and fall-back procedures for transmission interruptions or onboard equipment failures.
*   Compatibility and interfacing with existing national train control systems via Specific Transmission Modules (STMs).

**Out-of-Scope Items:**
*   Detailed technical design, data structures, or algorithms (covered in the System Requirements Specification).
*   Physical implementation processes or hardware specifications.
*   Training materials, environmental conditions, and detailed RAMS analyses.
*   Detailed DMI ergonomic design, screen layouts, or color schemes.
*   Functions not explicitly listed within the FRS.

#### 1.5 References
*   ERA_ERTMS_015560: ERTMS/ETCS Functional Requirements Specification (FRS), Version 5.00.
*   IEEE Std 830-1998: Recommended Practice for Software Requirements Specifications.
*   IEC 62278: Railway applications – Specification and demonstration of Reliability, Availability, Maintainability and Safety (RAMS).

### 2. Overall Description

#### 2.1 Product Perspective
ETCS is a component of the larger ERTMS, acting as the automatic train protection (ATP) system. It interfaces with:
*   **Trackside Equipment:** For receiving Movement Authorities and track data.
*   **National Systems (via STM):** For backward compatibility.
*   **Train Interfaces:** For braking, odometry, and other vital inputs.
*   **The Driver (via DMI):** For information display and input.

#### 2.2 Product Functions (Summary)
1.  **Train Supervision:** Continuously monitors train speed and position against the permitted Movement Authority and speed profile.
2.  **Data Management:** Handles entry, storage, and validation of train parameters and national system values.
3.  **Interface Management:** Presents information to the driver (DMI) and communicates with trackside/other systems.
4.  **Mode & Level Management:** Controls transitions between different ETCS application levels and operational modes.
5.  **Failure Management:** Detects, reacts to, and reports system failures to maintain a safe state.
6.  **Recording:** Logs key system events and data for analysis and investigation.

#### 2.3 User Characteristics
| Stakeholder | Primary Role | Key Interaction with ETCS |
| :--- | :--- | :--- |
| **Driver** | Safe train operation. | Uses DMI for information; acknowledges prompts; operates under ETCS supervision. |
| **Railway Infrastructure Manager** | Manages track capacity and safety. | Provides trackside data (MA, gradients, speed limits) to the onboard unit. |
| **Train Operator / Crew** | Prepares train for service. | Enters and verifies train data (length, braking capability, etc.) into the onboard unit. |
| **Maintenance Personnel** | Maintains system availability. | Responds to fault indications; performs isolation and testing procedures. |
| **Safety Regulator** | Ensures system safety compliance. | Reviews system against mandatory requirements and safety cases. |
| **System Integrator** | Implements and deploys ETCS. | Configures system for specific levels, national values, and vehicle interfaces. |

#### 2.4 Operating Environment
*   **Physical:** Railway rolling stock and trackside locations across Europe, subject to varying climatic conditions.
*   **Technical:** Must interoperate with legacy national ATP systems (e.g., LZB, TVM, KVB) through STMs.
*   **Operational:** Functions at train speeds from 0 km/h to a maximum of **500 km/h**.

#### 2.5 Design and Implementation Constraints
1.  **(M) Mandatory Requirements:** Every requirement classified as Mandatory **SHALL** be implemented in every ETCS application.
2.  **Safety during Transitions:** Transitions between operational modes/states **SHALL** maintain a level of protection at least equal to that of the least restrictive state involved in the transition.
3.  **National Values:** National system parameters (e.g., default speeds, timers) **SHALL** be applicable to defined geographical areas and stored permanently in the onboard non-volatile memory.
4.  **Default Values:** A harmonized set of default values **SHALL** be used by the onboard equipment when national values for a specific area are unavailable.
5.  **Non-Interference:** ETCS **SHALL NOT** interfere with the operation of existing national systems, and vice versa.

#### 2.6 Assumptions and Dependencies
*   It is assumed that trackside data provided to ETCS is correct and timely.
*   The system depends on accurate inputs from odometry and balise readers for position determination.
*   Successful interoperability depends on all parties implementing the standardized protocols and interfaces defined in the relevant subset specifications.

### 3. Specific Requirements

#### 3.1 External Interface Requirements
##### 3.1.1 Driver-Machine Interface (DMI)
*   **FR-DMI-001 (M):** The DMI **SHALL** display the following primary information continuously: current speed, target speed/permitted speed, distance to target, and current ETCS level/mode.
*   **FR-DMI-002 (M):** The DMI **SHALL** provide audible and visual warnings for overspeed, approach to movement authority end, and system failures.
*   **FR-DMI-003 (M):** The DMI **SHALL** allow the driver to acknowledge specific system requests (e.g., level transitions, data entry confirmations).

##### 3.1.2 Trackside Interface
*   **FR-TSI-001 (M):** The onboard unit **SHALL** be capable of receiving and processing Movement Authority messages from RBC (Level 2/3) or via Eurobalises (Level 1).
*   **FR-TSI-002 (M):** The system **SHALL** be capable of interfacing with national systems via a standardized STM interface.

#### 3.2 Functional Requirements
##### 3.2.1 Train Data Management
*   **FR-FUN-001 (M):** The system **SHALL** provide a means for the driver/train operator to enter and confirm train data (e.g., length, maximum speed, braking characteristics) before the start of a mission.
*   **FR-FUN-002 (M):** The onboard unit **SHALL** use the entered train data to calculate dynamic braking curves and speed profiles.

##### 3.2.2 Movement Authority and Speed Supervision
*   **FR-FUN-010 (M):** The system **SHALL** continuously supervise that the train does not exceed the permitted speed profile derived from the Movement Authority and static speed restrictions.
*   **FR-FUN-011 (M):** The system **SHALL** apply the service brake if the train speed exceeds the permitted speed plus a defined margin, and the emergency brake if a more severe overspeed threshold is breached.
*   **FR-FUN-012 (M):** The system **SHALL** supervise the train's movement against the end of its Movement Authority (EOA) and initiate braking to ensure the train stops before the EOA.

##### 3.2.3 Level and Mode Management
*   **FR-FUN-020 (M):** The system **SHALL** support the defined ETCS application levels (0, 1, 2, 3, STM) and operational modes (Full Supervision, On Sight, Shunting, etc.).
*   **FR-FUN-021 (M):** Transitions between levels and modes **SHALL** be managed either automatically by the system or require driver acknowledgment as specified.

##### 3.2.4 Failure Handling and Fall-back
*   **FR-FUN-030 (M):** Upon detection of a critical onboard failure, the system **SHALL** transition to a safe state (e.g., trip or isolation) and inform the driver via the DMI.
*   **FR-FUN-031 (M):** In case of a complete loss of communication with the RBC (Level 2/3), the system **SHALL** initiate a defined failure reaction, such as triggering a brake application after a timeout, unless an alternative safe procedure is defined.
*   **FR-FUN-032 (M):** The system **SHALL** perform an automatic self-test of vital functions upon startup without requiring driver intervention.

#### 3.3 Performance Requirements
*   **FR-PER-001:** The system **SHALL** perform all supervision functions correctly at train speeds from 0 km/h to 500 km/h.
*   **FR-PER-002:** The system startup self-test **SHALL** be completed within a defined timeframe specified in the national values.
*   **FR-PER-003:** The reaction time from detection of an overspeed condition to the initiation of braking **SHALL** be within specified, safety-critical limits.

#### 3.4 System Recording Requirements
*   **FR-REC-001 (M):** The onboard system **SHALL** record a minimum set of data including, but not limited to: mode/level transitions, brake interventions, driver acknowledgments, and system failures.
*   **FR-REC-002 (M):** Recorded data related to a safety-critical incident **SHALL** be retained for at least 24 hours. General operational data **SHALL** be retained for at least one week.

### 4. Verification and Success Metrics
The successful implementation of this SRS shall be measured against the following criteria:

1.  **Speed Compliance:** Verification that all supervision functions operate as specified across the entire speed range (0-500 km/h) under test conditions.
2.  **Self-Test Automation:** Validation that the onboard equipment performs its automatic self-test sequence upon every startup without any mandatory driver action.
3.  **Data Recording Completeness:** Audit of the recording function to confirm that all event types listed in FR-REC-001 are captured and retained for the mandated minimum periods.
4.  **Interoperability Test Success:** Successful execution of standardized interoperability test suites across different implementations of onboard and trackside equipment.

### 5. Appendices

#### 5.1 User Stories Mapping
| User Story | Mapped Functional Requirements |
| :--- | :--- |
| 1. Driver needs clear DMI info. | FR-DMI-001, FR-DMI-002 |
| 2. Driver acknowledges transitions. | FR-DMI-003, FR-FUN-021 |
| 3. Infrastructure manager sends data. | FR-TSI-001 |
| 4. Train operator enters data. | FR-FUN-001 |
| 5. Maintenance sees faults. | FR-DMI-002, FR-FUN-030 |
| 6. Integrator ensures STM compatibility. | FR-TSI-002 |

#### 5.2 Undecided Issues and TBDs
The following issues require resolution, typically by a relevant authority (e.g., ERA, national safety agency) or project-specific decision:
1.  The specific safety and operational conditions under which **Optional (O) functions** become mandatory for a given project.
2.  The definitive selection and detailed procedure for **transmission failure reactions** (options 1-3 referenced in the source FRS).
3.  The **exact data retention periods** for the onboard recording device beyond the stated minimums (24 hours, one week).
4.  Clear rules for the **prioritization of multiple application levels** when more than one is technically available on a line section.
5.  The mechanism for providing **language support for non-predefined, free-text messages** sent from trackside to the DMI.

---
*This document is based on the provided project summary and is intended as a template. For authoritative requirements, always consult the official ERA FRS version 5.00 document.*