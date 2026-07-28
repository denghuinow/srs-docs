# Software Requirements Specification (SRS)
## European Rail Traffic Management System / European Train Control System (ERTMS/ETCS)
### Based on Functional Requirements Specification (FRS) v5.00
**Document Version:** 1.0  
**Date:** [Current Date]  
**Reference:** FRS v5.00 (21 June 2007)

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document provides a comprehensive, detailed description of the functional and non-functional requirements for the European Rail Traffic Management System / European Train Control System (ERTMS/ETCS). It serves as the definitive guide for system integrators, suppliers, developers, and validators involved in the design, implementation, testing, and certification of ETCS onboard and trackside components. This SRS translates the high-level goals of the FRS into specific, verifiable system requirements.

### 1.2 Scope
The system defined in this SRS is a standardized, interoperable train control system designed for deployment across the European rail network. Its core purpose is to supervise train and shunting movements to ensure safety, provide movement authorities and information to the driver, and support interoperability between different national rail systems.

**In-Scope:**
*   Onboard Unit (OBU) software functions, including supervision, braking curve calculation, and Driver-Machine Interface (DMI) logic.
*   Trackside system interfaces (Radio Block Centre - RBC, Eurobalise, Euroloop, GSM-R).
*   Functional behavior across defined ETCS application levels (0, 1, 2, 3).
*   Management of operational modes (e.g., Full Supervision, Shunting, On Sight).
*   Failure handling and fall-back procedures.
*   Juridical Recording Unit (JRU) functionality.

**Out-of-Scope:**
*   Detailed hardware design specifications for onboard or trackside equipment.
*   Specific physical design of the Driver-Machine Interface (DMI) layout.
*   Comprehensive RAMS analysis and target values.
*   Detailed environmental specifications (e.g., temperature, vibration, EMC).
*   Training program content for personnel.
*   Implementation of legacy national systems (handled via Specific Transmission Modules - STMs).

### 1.3 Definitions, Acronyms, and Abbreviations

| Term | Definition |
| :--- | :--- |
| **ERTMS** | European Rail Traffic Management System |
| **ETCS** | European Train Control System |
| **RBC** | Radio Block Centre |
| **DMI** | Driver-Machine Interface |
| **MA** | Movement Authority |
| **STM** | Specific Transmission Module |
| **OBU** | Onboard Unit |
| **JRU** | Juridical Recording Unit |
| **GSM-R** | Global System for Mobile Communications – Railway |
| **RAMS** | Reliability, Availability, Maintainability, Safety |
| **TSI** | Technical Specification for Interoperability |
| **Fail-safe** | A design principle where any failure leads the system to a predefined, safe state. |

### 1.4 References
*   ERTMS/ETCS Functional Requirements Specification (FRS), Subset-026, v5.00, 21 June 2007.
*   Relevant UNISIG (Union of Signalling Industry) specifications.
*   ERA (European Union Agency for Railways) Technical Specifications for Interoperability (TSIs).

### 1.5 Overview
The remainder of this document is structured as follows:
*   **Section 2:** Overall Description - Provides context, user characteristics, and constraints.
*   **Section 3:** System Features - Details specific functional requirements.
*   **Section 4:** External Interface Requirements - Defines hardware, software, and communication interfaces.
*   **Section 5:** Non-Functional Requirements - Specifies safety, performance, and other quality attributes.
*   **Section 6:** Other Requirements - Covers design constraints, documentation, and assumptions.

## 2. Overall Description

### 2.1 Product Perspective
ERTMS/ETCS is a distributed, safety-critical system comprising major subsystems:
1.  **Onboard Subsystem:** Installed on the train, including the ETCS Onboard Unit (OBU), DMI, Juridical Recorder (JRU), odometry sensors, and balise antennas.
2.  **Trackside Subsystem:** Includes Radio Block Centres (RBCs), Eurobalises, Euroloops, and GSM-R radio infrastructure.
3.  **Legacy Interface:** Specific Transmission Modules (STMs) allow the ETCS OBU to interface with national legacy train control systems.

The system operates across multiple application levels, with Levels 1 & 2 being primary. Data exchange occurs via spot transmission (balises) and continuous transmission (GSM-R).

### 2.2 User Characteristics
| User Role | Expertise / Characteristics | Key Interaction |
| :--- | :--- | :--- |
| **Driver** | Licensed train driver, trained on ETCS DMI. Not a computer expert. | Primary user of the DMI for data entry, receiving information, and acknowledging warnings. |
| **Maintenance Technician** | Technical staff trained on ETCS maintenance procedures. | Uses diagnostic interfaces for system health checks, troubleshooting, and data retrieval from JRU. |
| **Infrastructure Manager (Staff)** | Railway operations and signaling staff. | Configures and monitors RBCs, inputs movement authorities and track data into the trackside system. |
| **Train Operator (Manager)** | Operational management staff. | Responsible for ensuring correct train data is available and managing recorded operational data. |

### 2.3 Operating Environment
*   **Physical Environment:** Equipment must operate in harsh railway environments (subject to shock, vibration, wide temperature ranges, and electromagnetic interference). Specific limits are defined in separate hardware specifications.
*   **System Environment:** The software shall run on dedicated, safety-certified hardware platforms (OBU, RBC). It must interface with real-time sensors (odometry, balise reader) and communication networks (GSM-R).
*   **Support Environment:** Development, testing, and maintenance tools as provided by the system integrator.

### 2.4 Design and Implementation Constraints
1.  **Safety Standards:** Development must comply with CENELEC railway safety standards (EN 50126, EN 50128, EN 50129).
2.  **Fail-Safe Principle:** The system architecture shall be fail-safe. Any detected failure shall lead to a restrictive reaction (e.g., application of brakes, transition to a more restrictive mode).
3.  **Interoperability:** The system shall implement all mandatory (M) functions as defined in Subset-026. Optional (O) functions may be implemented based on national deployment choices.
4.  **Backward Compatibility:** Onboard systems shall be capable of operating over lines equipped with lower ETCS application levels.

### 2.5 Assumptions and Dependencies
*   **Assumption:** National values (e.g., default braking parameters, timers) are defined and provided to the system.
*   **Assumption:** Accurate and reliable time synchronization (UTC) is available to the onboard system.
*   **Dependency:** The availability of a GSM-R network for ETCS Levels 2 & 3.
*   **Dependency:** Correct installation and calibration of trackside balises and loops.
*   **Dependency:** The train's braking system provides a reliable interface for service and emergency brake commands.

## 3. System Features

### 3.1 Feature: System Initialization and Self-Test
**Description:** The onboard system shall perform automatic checks upon power-up to verify its operational health before permitting movement.
**Requirements:**
*   **FR-001:** Upon application of power, the OBU shall initiate an automatic self-test of its vital functions.
*   **FR-002:** The DMI shall display the self-test progress and its final result (Pass/Fail) to the driver.
*   **FR-003:** If the self-test fails, the OBU shall enter a failure state, inhibit movement authority supervision, and indicate the failure on the DMI.

### 3.2 Feature: Train Data Management
**Description:** The driver shall input or confirm key train parameters required for the ETCS supervision calculations.
**Requirements:**
*   **FR-010:** The system shall prompt the driver to enter/confirm train data before transitioning to a supervised mode.
*   **FR-011:** The system shall accept and store the following minimum train data: Train Identification, Maximum Speed, Train Length, Brake Percentage (or equivalent parameters).
*   **FR-012:** The system shall validate entered data against plausible ranges (where possible) and request confirmation for out-of-range entries.
*   **FR-013:** All driver entries and confirmations of train data shall be recorded in the JRU with a timestamp.

### 3.3 Feature: Movement Authority (MA) Supervision
**Description:** The core function where the OBU receives movement authorities, calculates braking curves, and supervises the train's speed and position.
**Requirements:**
*   **FR-020:** The OBU shall receive Movement Authorities (MA) and associated track data (static speed profiles, gradients) from trackside via balise or RBC.
*   **FR-021:** The OBU shall calculate a dynamic braking curve based on the received MA, track data, and train characteristics.
*   **FR-022:** The system shall continuously supervise the current train speed against the permitted speed profile (Intervention and Warning limits).
*   **FR-023:** The system shall supervise the distance to the end of the Movement Authority (EOA) or to a target location.
*   **FR-024:** The DMI shall clearly display to the driver: current speed, permitted speed, distance to target, and current mode.

### 3.4 Feature: Brake Intervention
**Description:** The system shall automatically apply brakes if supervision limits are violated.
**Requirements:**
*   **FR-030:** If the train speed exceeds the Service Brake Intervention Limit (SBIL), the system shall command a service brake application.
*   **FR-031:** If the train speed exceeds the Emergency Brake Intervention Limit (EBIL), or if the train passes the End of Authority (EOA), the system shall command an emergency brake application.
*   **FR-032:** Prior to a service brake intervention, the DMI shall provide a clear and timely acoustic and visual warning to the driver (e.g., 5 seconds before intervention, where applicable).
*   **FR-033:** The brake intervention and the reason for it shall be immediately recorded in the JRU.

### 3.5 Feature: Mode and Level Management
**Description:** The system shall manage transitions between different operational modes (e.g., Full Supervision, Shunting) and application levels.
**Requirements:**
*   **FR-040:** The system shall support the following primary modes: Full Supervision (FS), On Sight (OS), Shunting (SH), Staff Responsible (SR), and Stand By (SB).
*   **FR-041:** Transitions between modes shall occur based on predefined triggers (driver action, trackside command, system condition) and often require explicit driver acknowledgement.
*   **FR-042:** The system shall manage transitions between ETCS application levels (e.g., Level 1 to Level 2) during movement, including safe handover between RBCs.
*   **FR-043:** The current mode and level shall be permanently displayed on the DMI.

### 3.6 Feature: Juridical Recording
**Description:** The system shall record safety-critical data for incident analysis and performance monitoring.
**Requirements:**
*   **FR-050:** The Juridical Recording Unit (JRU) shall continuously record a defined set of data, including: speed, distance, mode, driver inputs, received MA, system messages, and brake commands.
*   **FR-051:** All recorded data shall be timestamped with synchronized UTC and linked to location (odometry position).
*   **FR-052:** Recorded data shall be stored in a non-volatile memory, protected against unauthorized modification.
*   **FR-053:** A minimum of 24 hours of operational data shall be retained. Data related to safety incidents (e.g., brake interventions) shall be marked and retained until explicitly downloaded.

### 3.7 Feature: Failure Detection and Handling
**Description:** The system shall detect internal and external failures and execute predefined safe reactions.
**Requirements:**
*   **FR-060:** The OBU shall continuously monitor the status of its vital subsystems (odometry, balise antenna, processor) and communication links (GSM-R).
*   **FR-061:** Upon detection of a critical failure (e.g., odometry fault, loss of communication with RBC), the system shall initiate a predefined safety reaction. This reaction shall be based on **National Values** and may include: immediate emergency brake, continuation to the end of the current MA followed by stop, or transition to a degraded mode (e.g., On Sight).
*   **FR-062:** Any detected failure and the subsequent reaction shall be immediately indicated to the driver via the DMI and recorded in the JRU.

## 4. External Interface Requirements

### 4.1 User Interfaces
*   **DMI (Driver-Machine Interface):** The primary user interface. Requirements defined in **Subset-041**. The SRS requires that the DMI software presents information clearly, supports multiple selectable languages, and provides unambiguous visual/acoustic warnings.

### 4.2 Hardware Interfaces
*   **Odometry Sensors:** Interface to receive pulses from tachometers/radar for speed and distance calculation.
*   **Balise Antenna:** Interface to receive telegrams from Eurobalises.
*   **Loop Antenna:** Interface to receive data from Euroloops (where applicable).
*   **Brake Interface:** Vital output to command service and emergency brake applications.
*   **GSM-R Radio:** Interface for continuous data communication with the RBC.

### 4.3 Software Interfaces
*   **RBC Communication:** Protocol for safe data exchange with the Radio Block Centre as defined in **Subset-037**.
*   **Balise Telegram:** Decoding of Eurobalise telegrams as defined in **Subset-036**.
*   **STM Interface:** Standardized interface for connecting Specific Transmission Modules (for national systems).

### 4.4 Communication Interfaces
*   **GSM-R:** Relies on GSM-R network for voice and ETCS data communication (Levels 2 & 3). The OBU shall implement the GSM-R air interface and network registration procedures.

## 5. Non-Functional Requirements

### 5.1 Safety Requirements
*   **NFR-SAF-001:** The system shall be designed to SIL 4 (Safety Integrity Level 4) as per EN 50128 for all vital safety functions (supervision, brake intervention).
*   **NFR-SAF-002:** The system shall be fail-safe. Any single failure shall not prevent a safe state from being achieved (e.g., brake application).
*   **NFR-SAF-003:** The system shall implement safe communication protocols (e.g., with RBC) to protect against data corruption, loss, insertion, and replay.

### 5.2 Performance Requirements
*   **NFR-PER-001:** The system shall be capable of correct functional operation at train speeds from 0 km/h up to 500 km/h.
*   **NFR-PER-002:** The odometry subsystem shall maintain a defined location accuracy (e.g., +/- 5m under normal conditions, +/- 10m with expected slippage) which shall be accounted for in braking curve calculations.
*   **NFR-PER-003:** The system reaction time from detecting a supervision limit violation to issuing a brake command shall be less than [X] milliseconds.

### 5.3 Usability Requirements
*   **NFR-USA-001:** The DMI shall be designed for use by a driver under workload and stress. Critical information shall be prominent and unambiguous.
*   **NFR-USA-002:** The system shall support a minimum of [5] European languages for driver interaction.
*   **NFR-USA-003:** Acoustic warnings shall have distinct and prioritized patterns for different alert levels (information, warning, immediate danger).

### 5.4 Reliability, Availability, and Maintainability (RAMS)
*   **NFR-RAM-001:** The system design shall adhere to the principles of EN 50126. Specific MTBF (Mean Time Between Failures) and availability targets are defined in project-specific RAMS plans.
*   **NFR-RAM-002:** The system shall support remote and local diagnostic functions to aid maintenance.

### 5.5 Data Integrity and Security
*   **NFR-SEC-001:** Juridically recorded data shall be protected against tampering or accidental erasure after the recording event.
*   **NFR-SEC-002:** Access to configuration and diagnostic functions shall be protected by access controls (e.g., maintenance keys/passwords).

## 6. Other Requirements

### 6.1 Design and Development Constraints
*   The software shall be developed using a language and toolchain suitable for SIL 4 development (e.g., as defined in EN 50128).
*   The software architecture shall support independent testing of vital and non-vital functions.

### 6.2 Certification Requirements
*   The final system must obtain approval from a National Safety Authority (NSA) or a Notified Body for deployment on the mainline railway.

### 6.3 Open Issues
1.  Final selection of national values and default parameters.
2.  Detailed performance requirements for the GSM-R data exchange (packet loss, latency).
3.  Specific algorithms for adhesion factor adaptation.

### 6.4 Appendix: Traceability to FRS User Stories
| SRS Requirement | FRS User Story |
| :--- | :--- |
| FR-010, FR-011, FR-012 | #1: Driver entering train data |
| FR-032 | #2: Clear warnings before brake intervention |
| FR-020 | #3: Infrastructure sending MA/track data |
| FR-050, FR-051, FR-053 | #4: Recording operational data |
| FR-001, FR-002 | #5: Automatic self-test at startup |
| FR-060, FR-061 | #6: Defined failure modes |

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| **Author** | | | |
| **Reviewer** | | | |
| **Approver** | | | |