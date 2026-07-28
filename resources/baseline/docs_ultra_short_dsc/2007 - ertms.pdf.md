# Software Requirements Specification (SRS)
## European Train Control System (ETCS) - Onboard Subsystem

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the European Train Control System (ETCS) Onboard Subsystem. It serves as a comprehensive description of the system's intended capabilities, external interfaces, and performance characteristics for system designers, developers, testers, project managers, and stakeholders. The document focuses on *what* the system shall do, not *how* it will be implemented.

#### 1.2 Scope
This SRS covers the functional requirements for the ETCS onboard equipment as part of the European Rail Traffic Management System (ERTMS). The scope includes:
*   Supervision of train speed and movement authorities.
*   Management of application levels and operational modes/states.
*   Braking curve calculation and enforcement.
*   Driver-Machine Interface (DMI) functionality.
*   Data recording and system protection functions.
*   Interfaces with trackside equipment, vehicle systems, and national systems.

**Out of Scope:**
*   Detailed technical specifications for hardware components.
*   Implementation plans or software architecture details.
*   Trackside equipment design (e.g., RBC, balises), except for defined interfaces.
*   Training procedures or maintenance manuals.
*   Commercial or procurement aspects.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **ETCS** | European Train Control System |
| **ERTMS** | European Rail Traffic Management System |
| **CCS TSI** | Control-Command and Signalling Technical Specification for Interoperability |
| **STM** | Specific Transmission Module |
| **RBC** | Radio Block Centre |
| **GSM-R** | Global System for Mobile Communications – Railway |
| **DMI** | Driver-Machine Interface |
| **MA** | Movement Authority |
| **M** | Mandatory Requirement |
| **O** | Optional Requirement |

#### 1.4 References
*   CCS TSI (Commission Regulation (EU) 2016/919)
*   ERA_ERTMS_015560 - ERTMS/ETCS System Requirements Specification (Subset-026)

#### 1.5 Document Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details all specific requirements, including functional, interface, and non-functional requirements.

### 2. Overall Description

#### 2.1 Product Perspective
ETCS is a standardized, interoperable train control system designed to replace disparate national systems across Europe. The onboard subsystem is a critical component that interacts with multiple external entities:
*   **Trackside Systems:** Receives data via balises, Euroloops, or GSM-R radio from RBCs.
*   **National Systems:** Interfaces via the STM for backward compatibility.
*   **Vehicle:** Interfaces with the braking system, odometry, and other sensors.
*   **Driver:** Communicates via the DMI.

The system must operate seamlessly across national borders, adapting to nationally specific parameters without mutual interference with legacy systems.

#### 2.2 Product Functions (High-Level)
1.  **Train Supervision:** Continuously monitor and enforce speed and movement limits.
2.  **Mode & Level Management:** Operate in defined ETCS application levels (0, 1, 2, 3, STM) and operational modes (Full Supervision, Shunting, On Sight, etc.), managing transitions between them.
3.  **Braking Curve Management:** Calculate dynamic service and emergency braking curves based on train characteristics, track data, and MA.
4.  **Driver Interaction:** Present vital information, warnings, and prompts to the driver and accept inputs.
5.  **Data Recording:** Continuously record a defined set of data for performance monitoring and incident analysis.
6.  **System Protection:** Initiate emergency braking and enforce trip stops in case of safety-critical rule violations or system failures.

#### 2.3 User Characteristics
| User Class | Characteristics | Key Interactions |
| :--- | :--- | :--- |
| **Train Driver** | Primary operator. Licensed professional trained in ETCS procedures. | Enters train data, acknowledges system messages and warnings, monitors DMI for supervision information, responds to audible and visual alerts. |
| **Maintenance Technician** | Secondary user. Technical staff with access to diagnostic tools. | Retrieves recorded data via download interface, performs system diagnostics, supports troubleshooting. |

#### 2.4 Constraints
1.  **Interoperability:** Must comply with the CCS TSI and be compatible with listed national systems without adverse interference.
2.  **Requirement Classification:** All requirements are classified as Mandatory (M) or Optional (O). M requirements are unconditionally required for compliance.
3.  **External Dependencies:** Functionality is dependent on correct and timely provision of infrastructure data (e.g., gradients, speed profiles, MA) from trackside systems.
4.  **Legacy Compatibility:** Must interface with national systems through a standardized STM interface.

#### 2.5 Assumptions and Dependencies
*   The onboard system stores a set of harmonized default values (e.g., default braking parameters).
*   National values and specific infrastructure data will be provided by the trackside.
*   The vehicle interface (brakes, odometry) provides accurate and reliable data.
*   The system will be used within the defined operational environment of European railways.

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 Track-to-Train Interfaces
*   **IF-1 (Balise Interface):** The system shall (M) receive and process telegrams from Eurobalises.
*   **IF-2 (Loop Interface):** The system may (O) receive data from Euroloops.
*   **IF-3 (Radio Interface - GSM-R):** The system shall (M) establish and maintain a secure communication session with the Radio Block Centre (RBC) for Levels 2 & 3, exchanging application messages (e.g., Movement Authorities, system information).

##### 3.1.2 Vehicle Interfaces
*   **IF-4 (Braking Interface):** The system shall (M) issue service brake and emergency brake commands to the vehicle's braking system.
*   **IF-5 (Odometry Interface):** The system shall (M) receive accurate speed, distance, and direction data from the vehicle's odometry subsystem.

##### 3.1.3 Specific Transmission Module (STM) Interface
*   **IF-6 (STM Interface):** The system shall (M) interface with an STM to receive and process information from compatible national train control systems.

##### 3.1.4 Driver-Machine Interface (DMI)
*   **IF-7 (DMI Interface):** The system shall (M) provide all supervision data, warnings, and prompts to the DMI for display and shall receive driver inputs from the DMI.

#### 3.2 Functional Requirements

##### 3.2.1 System Management & Start-Up
*   **FR-1:** The onboard equipment shall (M) perform an automatic self-test at power-up.
*   **FR-2:** The system shall (M) allow the driver to enter and confirm train data (e.g., length, braking capability, max speed).

##### 3.2.2 Level and Mode Management
*   **FR-3:** The system shall (M) operate in the following ETCS Application Levels: 0, 1, 2, 3, and STM.
*   **FR-4:** The system shall (M) support transitions between different application levels according to predefined rules.
*   **FR-5:** The system shall (M) manage the following primary operational modes/states: Full Supervision (FS), On Sight (OS), Shunting (SH), Unfitted (UN), Stand By (SB), and Non-Leading (NL).
*   **FR-6:** The system shall (M) enforce transition rules between operational modes, ensuring the supervision condition is at least as protective as the least restrictive state involved in the transition.

##### 3.2.3 Movement Supervision
*   **FR-7:** The system shall (M) calculate a dynamic braking curve (Service Brake and Emergency Brake) based on:
    *   Train data (entered by driver).
    *   Infrastructure data (received from trackside).
    *   Current Movement Authority (MA).
*   **FR-8:** The system shall (M) continuously supervise the current train speed against the permitted speed profile and the braking curve.
*   **FR-9:** If the train speed exceeds the service brake intervention curve, the system shall (M) automatically apply the service brake.
*   **FR-10:** If the train speed exceeds the emergency brake intervention curve, the system shall (M) automatically apply the emergency brake.

##### 3.2.4 Driver Information and Interaction
*   **FR-11:** The system shall (M) present on the DMI at minimum:
    *   Current speed and target speed.
    *   Permitted speed.
    *   Distance to target (e.g., end of MA).
    *   Current operating level and mode.
    *   System messages and warnings.
*   **FR-12:** The system shall (M) require driver acknowledgment for specific system messages and mode transitions.

##### 3.2.5 Data Recording
*   **FR-13:** The system shall (M) record a defined set of data (JRU - Juridical Recording Unit functionality), including but not limited to:
    *   Received balise telegrams and RBC messages.
    *   Driver inputs.
    *   System commands (e.g., brake interventions).
    *   Changes in level, mode, and MA.
*   **FR-14:** The recorded data shall (M) be outputtable via a standardized physical interface for analysis.

##### 3.2.6 Protection Functions
*   **FR-15:** In case of a detected onboard equipment failure that compromises safety, the system shall (M) initiate an immediate emergency brake application.
*   **FR-16:** The system shall (M) implement a "Train Trip" function to enforce a stop if the train passes a signal indicating "Stop" (e.g., in Level 1).

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance Requirements
*   **PER-1:** The system shall be fully functional and maintain specified safety integrity for train speeds up to **500 km/h**.
*   **PER-2:** The system shall update displayed information and supervision calculations with a latency that ensures timely intervention within the defined braking model.

##### 3.3.2 Safety Requirements
*   **SAF-1:** The system shall be designed according to Safety Integrity Level **SIL 4** (as per EN 50128/50129) for safety-critical functions.
*   **SAF-2:** Any single failure within a safety-critical function shall lead to a safe state (e.g., brake application).
*   **SAF-3:** The system shall be fail-safe.

##### 3.3.3 Reliability, Availability, and Maintainability
*   **RAM-1:** The system shall perform a power-up self-test (see FR-1).
*   **RAM-2:** The Mean Time Between Critical Failures (MTBCF) shall exceed a defined threshold (to be specified based on subsystem design).
*   **RAM-3:** Recorded data shall be retrievable for a minimum of 48 hours of operation to support maintenance and incident investigation.

##### 3.3.4 Security Requirements
*   **SEC-1:** Communication with the RBC (GSM-R) shall be protected against unauthorized access and message manipulation (integrity and authentication).
> *Note: Detailed security requirements (e.g., encryption standards, key management) are specified in relevant subsystem documents.*

#### 3.4 Design and Implementation Constraints
1.  All requirements marked as **(M)** in this document are mandatory for any compliant implementation.
2.  Requirements marked as **(O)** are optional. If an optional feature is implemented, it must conform to the specified requirement.
3.  The system design shall allow for the storage and management of nationally specific parameters received from trackside.

### 4. Acceptance Criteria
Acceptance of an ETCS onboard subsystem implementation shall be based on:
1.  Full conformity with all **Mandatory (M)** requirements specified in Section 3.
2.  Verification that all implemented **Optional (O)** requirements conform to their specification.
3.  Successful demonstration of safety reactions, including emergency brake application upon simulated safety-critical failures.
4.  Validation of performance up to the specified maximum speed of 500 km/h under simulated conditions.
5.  Successful testing of interoperability with standardized trackside simulators and interfaces.