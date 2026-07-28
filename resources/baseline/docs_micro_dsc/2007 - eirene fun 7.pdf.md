# Software Requirements Specification (SRS)
## European Railway Digital Radio System (ERDRS)

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review  
**Authors:** [System Engineering Team]

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the European Railway Digital Radio System (ERDRS). The primary audience for this document includes system architects, software developers, test engineers, project managers, and stakeholders from European railway networks and regulatory bodies. This document serves as the definitive source of requirements for system development, testing, and validation.

#### 1.2 Scope
The ERDRS is a mission-critical, interoperable digital radio communication system designed for European railways. It will facilitate secure and reliable voice and data communications between:
*   Ground infrastructure and trains (Ground-Train).
*   Ground-based mobile units (e.g., maintenance crews, station staff, security).

The system in scope includes:
*   On-board mobile equipment (Train-borne Radio).
*   Fixed network infrastructure (Base Stations, Controllers, Management Systems).
*   Core network services (Call Control, Mobility Management, Addressing).
*   Interfaces to external systems (e.g., ERTMS/ETCS, Railway Operation Centers).

Out of scope are:
*   The design of the ERTMS/ETCS application layer itself.
*   Physical layer radio component design (though performance constraints are specified).
*   National legacy system migration strategies.

#### 1.3 Definitions, Acronyms, and Abbreviations

| Term | Definition |
| :--- | :--- |
| **ERTMS/ETCS** | European Rail Traffic Management System / European Train Control System |
| **P2P** | Point-to-Point (Call) |
| **GDC** | Group Direct Call |
| **REC** | Railway Emergency Call |
| **FN** | Functional Number |
| **LDN** | Location Dependent Number |
| **QoS** | Quality of Service |
| **HLR/HSS** | Home Location Register / Home Subscriber Server |
| **MTBF** | Mean Time Between Failures |
| **MTTR** | Mean Time To Repair |

#### 1.4 References
*   EU Directive XYZ/2015 on Railway Interoperability.
*   ETSI EN 300 392-x: Terrestrial Trunked Radio (TETRA) series (as a technical reference).
*   ERA Technical Specification for Rail Radio System Interoperability.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a high-level description of the product and its operating environment. Section 3 details specific system requirements, categorized as functional, interface, performance, and constraints. Section 4 covers non-functional requirements including reliability, security, and maintainability.

---

### 2. Overall Description

#### 2.1 Product Perspective
The ERDRS is a standalone but integrable system. It acts as a bearer network for higher-layer railway applications. Key system interfaces include:
*   **I1:** Interface to On-Train Consist Network (for ERTMS data).
*   **I2:** Interface to Railway Operation and Control Centers.
*   **I3:** Interface to Public Emergency Services (for critical calls).
*   **I4:** Management and Provisioning Interface.

#### 2.2 Product Functions (Summary)
1.  **Voice Communication Services:** Establish and manage mandatory voice call types.
2.  **Data Bearer Services:** Provide reliable packet-switched data channels.
3.  **Railway Addressing & Management:** Translate functional and location-based addresses to network identities.
4.  **Mobility Management:** Handle seamless handovers for trains at very high speeds.
5.  **Security & Priority Management:** Enforce call priorities, especially for emergency communications.
6.  **System Management:** Fault, configuration, accounting, performance, and security (FCAPS) management.

#### 2.3 User Characteristics
*   **Train Drivers:** Primary users of voice services (P2P, REC) and beneficiaries of data services (ERTMS). Require simple, hands-free operation.
*   **Signallers/Controllers:** Initiate group and broadcast calls, monitor status.
*   **Trackside Staff:** Use handheld or vehicle-mounted radios for group communication.
*   **System Administrators:** Configure network, manage subscribers, monitor performance.

#### 2.4 Constraints
1.  **Regulatory:** Must comply with European Railway Agency (ERA) mandates for interoperability.
2.  **Technical:** Must support seamless communication for trains traveling at speeds **up to 500 km/h**.
3.  **Performance:** Mandatory call set-up times must be statistically guaranteed (95th percentile).
4.  **Implementation:** All mandatory features specified in the applicable Technical Specifications must be implemented without deviation for core interoperability.

#### 2.5 Assumptions and Dependencies
*   Adequate radio site infrastructure (masts, power, backhaul) is provided by the deploying entity.
*   National frequency allocations for the system are secured.
*   ERTMS/ETCS application data is presented with appropriate QoS tagging.

---

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Voice Communication Services
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **VOC-001** | The system shall allow a user to initiate a **Point-to-Point (P2P)** voice call to another individual user by entering their Functional Number (FN) or Short Subscriber Identity. | High |
| **VOC-002** | The system shall allow an authorized user (e.g., signaller) to initiate a **Group Direct Call (GDC)** to a pre-defined group of users (e.g., all drivers in a sector). | High |
| **VOC-003** | The system shall allow an authorized user to initiate a **Broadcast Call** to all users within a specific geographical area or network-wide. | High |
| **VOC-004** | The system shall provide a dedicated, pre-emptive mechanism for initiating a **Railway Emergency Call (REC)**. This call shall have the highest priority in the system. | Highest |
| **VOC-005** | For an REC, the system shall automatically include pre-defined users/groups (e.g., relevant signaller, emergency responders) and provide clear audible/visual indication to all parties. | Highest |

##### 3.1.2 Data Bearer Services
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **DAT-001** | The system shall provide a **guaranteed bit-rate, low-latency data bearer** for ERTMS/ETCS Level 2 and 3 telegrams. | Highest |
| **DAT-002** | The system shall provide **packet-switched data bearers** (e.g., IP-based) for non-critical railway applications (e.g., CCTV upload, passenger information systems). | Medium |
| **DAT-003** | The system shall support QoS differentiation between critical train control data and other application data. | High |

##### 3.1.3 Addressing and Management
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **ADM-001** | The system shall support **Functional Number (FN) addressing**, allowing calls to be placed to a role (e.g., "Driver of Train XYZ") rather than a physical device. | High |
| **ADM-002** | The system shall support **Location Dependent Number (LDN) addressing**, routing calls to the user currently occupying a specific geographic location (e.g., "Signalman at Station A"). | High |
| **ADM-003** | The system shall resolve FN and LDN to the current network subscriber identity in real-time. | High |

#### 3.2 Interface Requirements
| ID | Requirement |
| :--- | :--- |
| **INT-001** | The On-Board Mobile Unit shall provide a standardized, secure Ethernet (IEEE 802.3) interface for the ERTMS/ETCS onboard unit. |
| **INT-002** | The Network Core shall provide an API (RESTful or SOAP) for Railway Operation Centers to query subscriber status and initiate broadcast calls. |

#### 3.3 Performance Requirements
| ID | Requirement | Verification Method |
| :--- | :--- | :--- |
| **PER-001** | The system shall support continuous communication for mobile terminals traveling at speeds **up to 500 km/h**. | Simulation & Field Test |
| **PER-002** | The call set-up time for a **Railway Emergency Call (REC)** shall be less than **2.0 seconds** in **95%** of attempts under full network load. | Statistical Analysis |
| **PER-003** | The call set-up time for a Point-to-Point voice call shall be less than **1.5 seconds** in 95% of attempts. | Statistical Analysis |
| **PER-004** | The end-to-end latency for critical ERTMS/ETCS data packets shall not exceed **500 ms** (99th percentile). | Measurement |
| **PER-005** | The packet loss ratio for the critical data bearer shall be less than **10⁻⁵**. | Measurement |

#### 3.4 Design Constraints
| ID | Constraint |
| :--- | :--- |
| **CON-001** | The system architecture shall adhere to the **reference architecture** defined in ERA Technical Specification ABC-123. |
| **CON-002** | All cryptographic algorithms used for air interface and core network security shall be from the suite approved by EU Agency for Cybersecurity (ENISA). |

---

### 4. Non-Functional Requirements

#### 4.1 Reliability, Availability, and Maintainability
*   **Availability:** The core network subsystem shall achieve 99.999% ("five nines") availability.
*   **MTBF:** The base station equipment shall have an MTBF of not less than 100,000 hours.
*   **MTTR:** The system shall support remote diagnostics, with a target MTTR of less than 2 hours for critical faults.

#### 4.2 Security Requirements
*   **Authentication:** Mutual authentication shall be required between the mobile terminal and the network before any service is granted.
*   **Encryption:** Voice and critical signaling traffic shall be encrypted over the air interface using strong encryption (minimum 128-bit AES).
*   **Integrity:** Data bearers for train control shall employ message integrity protection.
*   **Resilience:** The system shall be resilient to common denial-of-service (DoS) attacks.

#### 4.3 Safety Requirements
*   The system shall be designed to SIL (Safety Integrity Level) 2 as per IEC 62278 for functions directly supporting train control data transmission.
*   A failure of the radio system shall cause the ERTMS/ETCS to revert to a defined safe state (e.g., brake application).

---
**APPROVAL**

| Name | Role | Signature | Date |
| :--- | :--- | :--- | :--- |
| | Project Sponsor | | |
| | Lead System Architect | | |
| | Quality Assurance Manager | | |

*Document End*