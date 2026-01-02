# Software Requirements Specification (SRS)
## European Train Control System (ETCS) Onboard Unit

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the European Train Control System (ETCS) Onboard Unit. The purpose of this system is to enable safe train and shunting movements by supervising speed and movement authorities, thereby preventing collisions, derailments, and overspeed incidents. This document serves as a definitive guide for developers, testers, project managers, and stakeholders.

#### 1.2 Scope
The scope of this system encompasses the software for the ETCS Onboard Unit (OBU) installed on locomotives and train sets. The system:
*   Supervises train movements up to a maximum speed of **500 km/h**.
*   Interfaces with trackside equipment (e.g., Eurobalises, Loop Lines, Radio Block Centres).
*   Must co-exist and be interoperable with compatible National Train Control Systems (National ATP).
*   Does **not** include requirements for trackside infrastructure hardware, national system logic, or rolling stock braking hardware (though interfaces to these are defined).

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **ETCS** | European Train Control System |
| **OBU** | Onboard Unit |
| **RBC** | Radio Block Centre |
| **ATP** | Automatic Train Protection |
| **MA** | Movement Authority |
| **EOA** | End of Authority |
| **MRSP** | Most Restrictive Speed Profile |
| **SBD** | Service Brake Demand |
| **EBD** | Emergency Brake Demand |
| **FS** | Full Supervision |
| **OS** | On Sight |
| **SH** | Shunting |
| **M** | Mandatory Requirement |

#### 1.4 References
*   ERA_ERTMS_015560: ERTMS/ETCS System Requirements Specification.
*   EN 50128: Railway applications – Software for railway control and protection systems.
*   EN 50129: Railway applications – Safety related electronic systems for signalling.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details all specific requirements, including functional, interface, and performance requirements.

---

### 2. Overall Description

#### 2.1 Product Perspective
The ETCS OBU is a safety-critical, embedded system component within the broader train control ecosystem. It acts as the "brain" onboard the train, receiving data from trackside and calculating safe movement parameters.

**System Interfaces:**
1.  **Trackside Interface:** Receives telegrams from Eurobalises (Euroloop) and wireless messages from the RBC via GSM-R.
2.  **Driver Machine Interface (DMI):** Provides information to and receives inputs from the Train Driver.
3.  **National System Interface:** Exchanges data with a compatible National ATP system.
4.  **Train Interface Unit (TIU):** Sends brake demands (Service, Emergency) and receives train configuration data (length, weight, brake percentage) and precise odometry/speed measurements.

#### 2.2 Product Functions
The high-level functions of the ETCS OBU are:
1.  **Movement Authority Supervision:** Monitor the train's position relative to the granted Movement Authority (MA) and intervene if the End of Authority (EOA) is violated.
2.  **Speed Supervision:** Continuously compare the train's actual speed against the Permitted Speed (from MA) and the Most Restrictive Speed Profile (MRSP). Issue brake demands if limits are exceeded.
3.  **Brake Curve Calculation & Monitoring:** Dynamically calculate service and emergency braking curves based on train characteristics, gradient, and infrastructure data. Supervise the train's deceleration against these curves.
4.  **Mode & Level Management:** Manage transitions between defined ETCS Modes (Full Supervision, On Sight, Shunting, etc.) and Levels (1, 2, 3) based on commands and system conditions.
5.  **Train Data Management:** Facilitate the entry and verification of critical train parameters before the start of a journey.
6.  **Emergency Stop Execution:** Process and execute an unconditional emergency stop command received from the trackside (RBC).

#### 2.3 User Characteristics
| User Class | Expertise | Key Interactions |
| :--- | :--- | :--- |
| **Train Driver** | Licensed train operator. Trained on ETCS DMI procedures. | Enters train data, acknowledges alerts, follows speed and distance indications, responds to brake interventions. |
| **Infrastructure Operator (RBC)** | Signaling and traffic management expert. | Issues Movement Authorities, sends emergency stop commands, monitors train status within their area of control. |
| **Maintenance Technician** | Certified technical personnel. | Performs software updates, retrieves logged data, runs diagnostic tests. |

#### 2.4 Constraints
1.  **Safety & Compliance:** All **Mandatory (M)** requirements as per baseline ETCS specifications shall be implemented without deviation.
2.  **Interoperability:** The system must not interfere with, and must not be interfered by, the operation of a compatible National ATP system when both are active.
3.  **Operational States:** The onboard equipment must be capable of supervising the full defined set of ETCS operational modes and states (e.g., Full, Partial, Shunting, On Sight, Staff Responsible, Unfitted, etc.).
4.  **National Adaptation:** The system architecture must support the configuration of "National Values" to allow adaptation to local operational rules and safety margins.
5.  **Performance:** Must process inputs and generate supervision outputs within hard real-time deadlines to ensure safe operation at 500 km/h.

#### 2.5 Assumptions and Dependencies
*   Trackside infrastructure (balises, RBC) is installed, operational, and compliant with ETCS standards.
*   The train's odometry system provides sufficiently accurate and reliable position/speed data.
*   The braking system is capable of executing EBD and SBD commands within specified performance limits.

---

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Speed and Movement Authority Supervision
| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-010** | The system shall continuously determine the train's current position and speed. | M |
| **FR-011** | The system shall supervise that the train does not exceed the Permitted Speed defined by the active Movement Authority. | M |
| **FR-012** | The system shall supervise that the train does not exceed the Most Restrictive Speed Profile (MRSP). | M |
| **FR-013** | The system shall supervise that the train does not pass the End of Authority (EOA). | M |
| **FR-014** | In case of an overspeed condition, the system shall first issue a Service Brake Demand (SBD). If the overspeed persists, it shall escalate to an Emergency Brake Demand (EBD). | M |
| **FR-015** | In case of an authority violation (passing EOA), the system shall immediately issue an Emergency Brake Demand (EBD). | M |

##### 3.1.2 Mode and State Management
| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-020** | The system shall operate in one of the following primary supervision modes at any time: Full Supervision (FS), On Sight (OS), Shunting (SH), Staff Responsible (SR), Unfitted (UN). | M |
| **FR-021** | The system shall manage transitions between modes based on driver input, trackside commands, and system conditions as defined in the ETCS mode transition table. | M |

##### 3.1.3 Brake Curve Calculation and Supervision
| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-030** | The system shall calculate a dynamic Service Braking Curve (SBD curve) and an Emergency Braking Curve (EBD curve) based on:<br>• Train characteristics (length, weight, brake percentage).<br>• Line data (gradient, speed restrictions).<br>• Adhesion model. | M |
| **FR-031** | The system shall supervise the train's actual deceleration against the calculated brake curves following a brake intervention to ensure adequacy. | M |

##### 3.1.4 Train Data Management
| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-040** | The system shall provide a procedure on the DMI for the driver to enter the Train Data before the start of a journey. | M |
| **FR-041** | The system shall verify the consistency of entered Train Data (e.g., brake percentage plausible for train type). | M |
| **FR-042** | The system shall prevent movement under ETCS supervision (e.g., transition to Full Supervision) if valid Train Data has not been entered and confirmed. | M |

##### 3.1.5 Emergency Stop Execution
| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-050** | Upon receipt of a valid "Emergency Stop" message from the RBC, the system shall immediately issue an unconditional Emergency Brake Demand (EBD). | M |
| **FR-051** | The emergency brake condition initiated by trackside shall only be revocable by a specific "Release Emergency Stop" message from the RBC or a system restart. | M |

#### 3.2 Interface Requirements

##### 3.2.1 Driver Machine Interface (DMI)
| ID | Requirement Description |
| :--- | :--- |
| **IR-010** | The system shall display the following primary information to the driver: Current Speed, Target Speed, Distance to Target, Active Mode, and Movement Authority status. |
| **IR-011** | The system shall provide audible and visual warnings for overspeed, approach to restriction, and brake intervention. |
| **IR-012** | The system shall accept driver inputs for: Train Data entry, mode acknowledgement, data validation, and shunting commands. |

##### 3.2.2 Trackside Interface
| ID | Requirement Description |
| :--- | :--- |
| **IR-020** | The system shall decode telegrams from Eurobalises conforming to UNISIG subset-036. |
| **IR-021** | The system shall maintain a secure communication session with the RBC via GSM-R, exchanging messages as defined in subset-093. |

##### 3.2.3 National System Interface
| ID | Requirement Description |
| :--- | :--- |
| **IR-030** | The system shall provide a defined, isolated data channel (logical or physical) for communication with a National ATP system. |
| **IR-031** | The system shall implement the "STANDBY" functionality to deactivate ETCS supervision when the National system is active, and vice-versa, ensuring no interference. |

#### 3.3 Performance Requirements
| ID | Requirement Description |
| :--- | :--- |
| **PR-010** | The system shall update the calculated braking curves and supervision logic at a minimum frequency of **4 Hz**. |
| **PR-011** | The latency between detecting a critical safety condition (e.g., EOA violation) and issuing the corresponding brake command shall not exceed **200 ms**. |
| **PR-012** | The system shall be capable of processing a new balise telegram or RBC message within **100 ms** of receipt. |

#### 3.4 Safety and Reliability Requirements
| ID | Requirement Description |
| :--- | :--- |
| **SR-010** | The system shall be designed to Safety Integrity Level **SIL 4** as per EN 50128 and EN 50129. |
| **SR-011** | The probability of a hazardous failure leading to a wrong-side failure (e.g., failing to brake when required) shall be less than **10⁻⁹ per hour**. |
| **SR-012** | The system shall implement a continuous self-testing routine to detect latent faults within the hardware and software. |

#### 3.5 Design Constraints
| ID | Requirement Description |
| :--- | :--- |
| **DC-010** | The software shall be developed using a language and toolchain compliant with EN 50128 for SIL 4 software. |
| **DC-011** | The system design shall allow for the configuration of National Values (NVs) without modification to the core application software. |

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Manager | | | |
| Lead Systems Engineer | | | |
| Safety Assurance Manager | | | |
| Client Representative | | | |