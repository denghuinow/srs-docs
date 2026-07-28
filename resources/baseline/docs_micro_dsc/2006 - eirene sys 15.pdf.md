# Software Requirements Specification (SRS)
## Digital Railway Radio System (GSM-R)

**Document ID:** SRS-DRRS-GSMR-001  
**Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional, non-functional, and system requirements for a standardized, interoperable digital radio communication system for European railways. The system, based on the GSM standard (specifically GSM-Railway or GSM-R), is intended to replace legacy analog systems and provide a unified platform for mission-critical voice and data communications between ground personnel, train cabs, and operational control centers.

#### 1.2 Scope
The scope of this project encompasses the specification of the **core network infrastructure**, **mobile equipment**, and **associated software applications** required to deliver secure, reliable, and prioritized voice and data communications across European rail networks. This includes:
*   The definition of mandatory GSM services and railway-specific applications.
*   The specification of interfaces and performance criteria for mobile equipment (Cab Radios, General Purpose Radios, Operational Radios).
*   The system's operation within the designated Railway-GSM (R-GSM) frequency bands.
*   Support for functional and location-dependent call routing.

**Out of Scope:**
*   Detailed physical layer radio frequency (RF) engineering and site surveys.
*   Manufacturing specifications for hardware components.
*   Country-specific national implementation and deployment plans.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **GSM-R** | Global System for Mobile Communications – Railway. The standard for railway digital mobile communications. |
| **R-GSM** | Railway GSM. The specific paired frequency bands (876–880 MHz uplink / 921–925 MHz downlink) allocated for railway use in Europe. |
| **VGCS** | Voice Group Call Service. A GSM service for half-duplex group communications. |
| **VBS** | Voice Broadcast Service. A GSM service for one-way broadcast calls. |
| **eMLPP** | enhanced Multi-Level Precedence and Pre-emption. A GSM service providing call priority and pre-emption capabilities. |
| **Cab Radio** | Mobile terminal installed in the driver's cab of a train. |
| **Functional Addressing** | Addressing a user by their function (e.g., "Train 1234", "Station Master Paris East") rather than a fixed phone number. |
| **Location-Dependent Addressing** | Routing a call to the correct controller based on the geographical location of the caller. |
| **REC** | Railway Emergency Call. A highest-priority voice group call with mandatory confirmation. |
| **OSS** | Operations Support System. |

#### 1.4 References
1.  ETSI EN 301 515: "Global System for Mobile communication (GSM); Requirements for GSM operation on railways".
2.  ETSI TS 102 281: "Railway Telecommunications (RT); GSM-R interfaces".
3.  UIC Project EIRENE: "System Requirements Specification".
4.  IEEE Std 830-1998: "Recommended Practice for Software Requirements Specifications".

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a high-level description of the product and its operating environment. Section 3 details the specific system requirements, including external interfaces, functional capabilities, and non-functional constraints. Appendices contain supplementary information.

---

### 2. Overall Description

#### 2.1 Product Perspective
The GSM-R system is a large-scale, distributed mobile communication system integrated into the broader railway operational ecosystem. It interfaces with existing Railway Operations Centers, Signaling Systems, and OSS/BSS platforms. It is a successor to and must interoperate with legacy radio systems during transition periods.

#### 2.2 Product Functions (Summary)
1.  **Mission-Critical Voice Communications:** Support for individual, group (VGCS), and broadcast (VBS) voice calls with priority management (eMLPP).
2.  **Railway-Specific Addressing:** Dynamic mapping of functional identities (e.g., train number, staff role) to network identities and routing based on location.
3.  **Railway Emergency Call (REC) Handling:** Provision of a dedicated, high-priority call type with guaranteed setup and listener confirmation.
4.  **Data Services:** Support for circuit-switched and GPRS-based data applications (e.g., Euroradio for ETCS, shunting applications, automated train reporting).
5.  **Network Management:** Comprehensive OSS for fault, configuration, accounting, performance, and security (FCAPS) management.

#### 2.3 User Characteristics
| User Class | Characteristics |
| :--- | :--- |
| **Train Driver** | Primary user of Cab Radio. Requires simple, hands-free operation. Operates in a high-noise environment. Not a computer expert. |
| **On-Track Staff** | Uses General Purpose or Operational Radio. May be in harsh environmental conditions (rain, dust, shock). Requires ruggedized device. |
| **Dispatcher / Controller** | Uses fixed or dispatch terminal. Manages multiple simultaneous communications. Requires advanced call management features (setup, monitor, interrupt groups). |
| **Network Engineer** | Technical staff managing the GSM-R network via OSS. Highly skilled in telecommunications. |

#### 2.4 Constraints
1.  **Regulatory:** The system **must** operate within the **876–880 MHz (Mobile Tx)** and **921–925 MHz (Base Tx)** frequency bands as defined for R-GSM in CEPT/ERC decision (99)25.
2.  **Standards Compliance:** The core network **must** implement mandatory GSM Phase 2+ services as specified in EIRENE: VGCS, VBS, eMLPP, and ASCI.
3.  **Hardware Standards:** All mobile equipment (Cab, General Purpose, Operational) **must** conform to defined environmental (EN 50155 for rolling stock, EN 60529 for IP rating), electrical, and physical interface standards (e.g., for coupling with train antennas and control panels).
4.  **Interoperability:** The system **must** support cross-border operational communications without manual intervention by the driver.

#### 2.5 Assumptions and Dependencies
*   Adequate radio coverage will be provided along railway lines and in key operational areas.
*   National rail operators will provide and maintain a database linking functional numbers (e.g., train IDs) to physical network subscribers.
*   The system depends on the availability of standardized SIM cards for subscriber identity management.

---

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 Hardware Interfaces
*   **Cab Radio:** Must provide a standardized interface (e.g., defined per UIC 556) for connection to the external train antenna, driver's microphone/loudspeaker, and control panel/display unit.
*   **General Purpose Radio:** Must feature a 3.5mm jack for headset, a charging connector, and a robust physical PTT button.
*   **Network:** Base Station Subsystem must interface with core network switches (MSC) via standard A-bis and A interfaces.

##### 3.1.2 Software Interfaces
*   **Functional Number Database Interface:** The system shall provide an API or standardized protocol (e.g., based on LDAP or MAP) for real-time query and update of Functional Number to ISDN Number mappings.
*   **Location Register Interface:** The Home Location Register (HLR) shall support standard GSM MAP interfaces for subscriber data management and roaming.
*   **OSS Interface:** The OSS shall support SNMP and/or CORBA-based interfaces for integration with higher-level railway management systems.

##### 3.1.3 Communications Interfaces
*   **Air Interface:** Shall comply with GSM 05.05 and ETSI EN 301 502 for R-GSM power classes and modulation in the 900 MHz R-GSM band.
*   **Railway Emergency Call Protocol:** Shall use the standardized VGCS call setup with a dedicated, nationally unique Group ID (e.g., 299) and mandatory eMLPP priority level 0.

#### 3.2 Functional Requirements

##### 3.2.1 Voice Call Services
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FUN-VOICE-001** | The system shall support Voice Group Call Service (VGCS) as per 3GPP TS 43.068. | High |
| **FUN-VOICE-002** | The system shall support Voice Broadcast Service (VBS) as per 3GPP TS 43.069. | High |
| **FUN-VOICE-003** | The system shall implement eMLPP (3GPP TS 23.067) with at least priority levels 0 (highest) through 4. | High |
| **FUN-VOICE-004** | A call of priority level `n` shall be able to pre-empt an ongoing call of priority level `n+1` or lower on shared resources. | High |

##### 3.2.2 Railway-Specific Addressing & Routing
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FUN-ADDR-001** | The system shall allow a user to place a call by dialing a **Functional Number** (e.g., "91*1234" for Train 1234). | High |
| **FUN-ADDR-002** | The system shall dynamically translate a dialed Functional Number to the current Mobile Subscriber ISDN Number (MSISDN) of the target subscriber by querying the Functional Number Database. | High |
| **FUN-ADDR-003** | The system shall provide **Location-Dependent Addressing**. When a user dials a short code for a "local controller", the call shall be routed to the controller responsible for the geographic area where the caller is currently located. | High |

##### 3.2.3 Railway Emergency Call (REC)
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FUN-REC-001** | The system shall provide a dedicated, single-action method (e.g., a red button) on Cab and Operational Radios to initiate a Railway Emergency Call. | High |
| **FUN-REC-002** | A REC shall be established as a VGCS with eMLPP priority level 0 (highest). | High |
| **FUN-REC-003** | The system shall provide audible and visual confirmation to the REC initiator that the call has been successfully established and is being broadcast. | High |
| **FUN-REC-004** | All subscribed mobiles and dispatchers within the defined emergency call area shall receive the REC automatically, with pre-emption of other calls if necessary. | High |

##### 3.2.4 Data Services
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FUN-DATA-001** | The system shall support circuit-switched data connections up to 9.6 kbps for legacy applications. | Medium |
| **FUN-DATA-002** | The network shall support GPRS for packet-switched data as per 3GPP TS 43.064. | High |

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance Requirements
*   **Call Setup Time:** The call setup time for a point-to-point call shall be less than 1.5 seconds (95th percentile) under normal network load. For a VGCS, setup time shall be less than 2 seconds.
*   **Railway Emergency Call Setup Time:** The REC setup time shall not exceed 1 second (99th percentile).
*   **Handover Success Rate:** The handover success rate shall be greater than 99.5% to ensure call continuity along the track.
*   **Network Availability:** The core network subsystem shall achieve 99.95% availability per annum.

##### 3.3.2 Safety & Security Requirements
*   **Authentication:** The system shall perform GSM Authentication and Key Agreement (AKA) for all mobile network access.
*   **Data Integrity:** For safety-critical data applications (e.g., Euroradio), the system shall support end-to-end data integrity mechanisms as defined in relevant railway standards.
*   **Resilience:** Critical network nodes (MSC, HLR) shall be deployable in a geographically redundant, 1+1 configuration.

##### 3.3.3 Operational Requirements
*   **Mobile Equipment Environment:**
    *   Cab Radios shall comply with EN 50155 (rolling stock equipment) for temperature, humidity, and vibration.
    *   General Purpose Radios shall have a minimum ingress protection rating of IP54 (EN 60529).
*   **Power:** Cab Radios shall operate from the train's nominal battery supply (typically 24V, 48V, 72V, or 110V DC) with over-voltage and surge protection.

##### 3.3.4 Compliance Requirements
The delivered system **shall be certified** as compliant with the EIRENE System Requirements Specification and the relevant ETSI standards listed in Section 1.4.

---

### 4. Appendices

#### Appendix A: Glossary of Railway Terms
*(To be populated with specific railway operational terminology.)*

#### Appendix B: Call Flow Examples
*(Example call flows for Functional Addressing and Railway Emergency Call.)*

**B.1 Functional Addressing Call Flow:**
1.  Driver dials `91*5678` (Functional Number for "Train 5678").
2.  Cab Radio sends setup message to network with dialed digits.
3.  Network Gateway MSC queries the Functional Number Database with `91*5678`.
4.  Database returns the current MSISDN of the driver of Train 5678 (e.g., `+491234567890`).
5.  Gateway MSC routes the call to the MSISDN.
6.  Call is established with the Cab Radio of Train 5678.

---
**END OF DOCUMENT**