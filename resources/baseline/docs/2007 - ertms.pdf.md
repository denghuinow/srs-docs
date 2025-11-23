Of course. Below is a comprehensive Software Requirements Specification (SRS) document for the described European Rail Traffic Management System / European Train Control System (ERTMS/ETCS) On-Board Unit (OBU), structured professionally and formatted in Markdown.

***

# Software Requirements Specification (SRS)
## For the ERTMS/ETCS On-Board Unit (OBU)
**Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft

---

## 1. Introduction

### 1.1 Purpose
This document provides a detailed description of the Software Requirements Specification for the European Rail Traffic Management System / European Train Control System (ERTMS/ETCS) On-Board Unit. It specifies the functional and non-functional requirements necessary to ensure the safe control and supervision of train movements across European railways. This SRS is intended for system architects, software developers, testers, and validators involved in the implementation and certification of the ETCS onboard system.

### 1.2 Scope
The system defined in this SRS, the ETCS On-Board Unit (OBU), is responsible for the safe supervision and control of train movements. Its core functions include:

*   Supervising train speed up to 500 km/h.
*   Managing and transitioning between defined operational states (e.g., Full Supervision, Shunting).
*   Ensuring compatibility with national train control systems via the Specific Transmission Module (STM).
*   Enforcing movement authorities and applying emergency brakes when necessary.

**Out of Scope:** This specification does not define the implementation methods (hardware or software design) nor does it cover non-train-control functions such as passenger information systems or entertainment services.

### 1.3 Definitions, Acronyms, and Abbreviations

| Acronym | Definition |
| :--- | :--- |
| **CCS TSI** | Control Command and Signalling Technical Specifications for Interoperability |
| **ERTMS** | European Rail Traffic Management System |
| **ETCS** | European Train Control System |
| **OBU** | On-Board Unit |
| **RBC** | Radio Block Centre |
| **STM** | Specific Transmission Module |
| **SRS** | Software Requirements Specification |

### 1.4 References
*   ERA/ERTMS/033281 - ERTMS/ETCS System Requirements Specification
*   Commission Regulation (EU) No 2016/919 - CCS TSI

## 2. Overall Description

### 2.1 Product Perspective
The ERTMS/ETCS OBU is a key component within the broader European railway interoperability framework. It is designed to replace fragmented national systems, facilitating cross-border traffic. The OBU operates within the CCS TSI framework and interfaces with existing national infrastructure through the STM. It acts as the central processing unit onboard the train, receiving information from trackside and RBC, and providing commands and information to the driver.

### 2.2 Product Functions
The core functions of the ETCS OBU include:
*   Management and enforcement of mandatory train data entry prior to movement.
*   Supervision of Movement Authorities and speed profiles.
*   Management of driver-acknowledged transitions between operational modes.
*   Execution of shunting operations without the need for track data.
*   Monitoring of train integrity and managing handovers between Radio Block Centres (RBCs).
*   Controlling reversing operations with national-specific supervision values.
*   Applying emergency brakes for critical safety violations (e.g., passing a stop signal).

### 2.3 User Characteristics

| User Class | Description | Key Interactions |
| :--- | :--- | :--- |
| **Train Driver** | Primary user, responsible for operating the train under system supervision. | Enters train data; acknowledges alarms and mode transitions; monitors speed and authority information; responds to brake interventions. |
| **RBC Operator** | Manages train movement authorities and traffic flow from the control center. | Issues and revokes movement authorities; monitors train positions and status. |
| **Train Operator / Maintainer** | Responsible for system configuration, data retrieval, and maintenance. | Configures national system parameters via STM; downloads operational and accident data for analysis. |

### 2.4 Constraints
*   The system **must** support all ETCS application levels (0, 1, 2, and 3).
*   The system **must** maintain backward compatibility with national systems through the STM interface.
*   Full functionality is dependent on the availability of external trackside infrastructure (e.g., balises, loops, RBC communication).
*   All national parameters must use harmonized default values as defined in the baseline specifications.

### 2.5 Assumptions and Dependencies
*   It is assumed that trackside equipment (balises, RBC) functions correctly and provides accurate data.
*   The system depends on a functional STM for integration with national legacy systems.
*   The train's braking system is assumed to be responsive and capable of performing interventions as commanded by the OBU.

## 3. System Features and Requirements

### 3.1 Train Data Management

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FUNC-TDM-001** | The system shall require the driver to enter mandatory train data (e.g., length, braking characteristics, max speed) before movement can be initiated. | M |
| **FUNC-TDM-002** | The system shall verify the consistency of entered train data and prevent movement if the data is invalid or incomplete. | M |

### 3.2 Operational Mode Management

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FUNC-MODE-001** | The system shall define and manage the following operational modes (non-exhaustive): Full Supervision, Partial Supervision, Shunting, On-Sight, and Stand-by. | M |
| **FUNC-MODE-002** | All transitions between operational modes that require driver awareness shall necessitate a positive acknowledgment from the driver. | M |
| **FUNC-MODE-003** | In Shunting mode, the system shall permit train movement without reference to track data or a movement authority, but shall enforce a low-speed limit. | M |

### 3.3 Movement and Speed Supervision

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FUNC-SUP-001** | The system shall continuously supervise the current train speed against the permitted speed profile and the limits of the Movement Authority. | M |
| **FUNC-SUP-002** | The system shall provide a warning to the driver at least 5 seconds before an automatic brake intervention is triggered due to an impending speed limit exceedance. | M |
| **FUNC-SUP-003** | The system shall apply the service brake automatically if the driver does not respond to the warning and the train is about to exceed its speed profile. | M |
| **FUNC-SUP-004** | The system shall apply the emergency brake immediately in case of a "train trip" event (e.g., passing a stop signal). | M |

### 3.4 Safety and Integrity Management

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FUNC-SAF-001** | The system shall monitor train integrity (as required by the application level) and apply emergency brakes if a loss of integrity is detected. | M |
| **FUNC-SAF-002** | The system shall provide roll-away protection by applying brakes if an unintended movement is detected while the train is stationary. | M |

### 3.5 Communication and Handover

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FUNC-COM-001** | The system shall manage the handover of communication and control from one Radio Block Centre (RBC) to another during train movement without loss of supervision. | M |
| **FUNC-COM-002** | The system shall interface with national train control systems via the STM using standardized protocols. | M |

### 3.6 Reversing Operation

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FUNC-REV-001** | The system shall allow a reversing operation under system supervision. | M |
| **FUNC-REV-002** | During reversing, the system shall enforce a supervised speed and distance limit based on nationally defined values. | M |

## 4. External Interface Requirements

### 4.1 RBC Interface
*   **Protocol:** Standardized ETCS protocols (Euroradio / GSM-R).
*   **Data:** The interface shall be used for receiving Movement Authorities and transmitting train position/integrity data.

### 4.2 Trackside Interface
*   **Protocol:** Standardized ETCS telegram formats.
*   **Data:** The interface shall read intermittent data from balises and loops to update the train's position and receive line-specific information.

### 4.3 STM Interface
*   **Protocol:** National system protocols, encapsulated via the STM.
*   **Data:** The interface shall allow the OBU to receive supervision and authority data from national train control systems.

## 5. Non-Functional Requirements

### 5.1 Performance Requirements

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **PERF-001** | The system shall be capable of supervising train speeds up to 500 km/h. | M |
| **PERF-002** | The system shall calculate and issue a brake intervention command with sufficient lead time to ensure braking begins at least 5 seconds before the supervised speed limit is exceeded. | M |

### 5.2 Safety Requirements
*   The system architecture shall be designed to SIL 4 (Safety Integrity Level 4) as per EN 50128 and EN 50129 standards for all safety-critical functions.
*   All safety-critical commands (especially emergency brake) shall be protected by redundancy and cross-checking.

### 5.3 Data Retention Requirements

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **DATA-001** | The system shall retain all data related to a safety-critical incident or accident for a minimum of 24 hours. | M |
| **DATA-002** | The system shall retain general operational data (e.g., mode changes, driver inputs) for a minimum of 1 week. | M |

### 5.4 Compliance Requirements
*   The system shall mandatorily use the harmonized default values for national parameters as specified in the applicable ETCS baseline.

## 6. Acceptance Approach
All requirements marked with priority **(M)** are mandatory. The system will be considered acceptable only upon full and verified compliance with every mandatory requirement stated in this document and its referenced lower-level ETCS specifications. There are no optional features, and no acceptance criteria exist beyond the complete fulfillment of these mandatory requirements. Verification shall be achieved through a combination of testing, analysis, and inspection as defined in the associated verification and validation plan.