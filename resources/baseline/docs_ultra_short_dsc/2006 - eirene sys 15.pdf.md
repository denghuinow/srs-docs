# Software Requirements Specification (SRS)
## European Integrated Railway Radio Enhanced Network (EIRENE)

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the European Integrated Railway Radio Enhanced Network (EIRENE). The primary purpose of this document is to provide a complete description of the system's capabilities, interfaces, and performance characteristics to ensure interoperability across European national borders. It serves as a contractual basis between stakeholders, including railway undertakings, infrastructure managers, and system suppliers, and as a reference for developers, testers, and project managers.

#### 1.2 Scope
The EIRENE system is a standardized digital radio communications platform for European railways. Its scope encompasses:
*   Ground-to-train and ground-to-mobile voice and data communications for operational, safety, and administrative purposes.
*   Provision of a secure and reliable radio bearer for the European Rail Traffic Management System / European Train Control System (ERTMS/ETCS).
*   Mobile equipment (cab radios, operational radios, general-purpose radios) and the logical network services required for their operation.
*   Defined interfaces to external systems, including fixed networks and on-train equipment.

**Out of Scope:**
*   Detailed specification of the fixed network infrastructure (Base Station Subsystem, Network Switching Subsystem).
*   Specification of controller/dispatcher workstation hardware and software.
*   National implementation-specific configurations beyond the interoperability baseline.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **BSS** | Base Station Subsystem |
| **Cab Radio** | Mobile station installed in a train driver's cab |
| **EC** | Emergency Call |
| **eMLPP** | enhanced Multi-Level Precedence and Pre-emption |
| **ERTMS/ETCS** | European Rail Traffic Management System / European Train Control System |
| **ETSI** | European Telecommunications Standards Institute |
| **EURORADIO** | The specified protocol for ERTMS/ETCS data transmission over GSM-R |
| **FFFIS** | Form Fit Functional Interface Specification |
| **Functional Number** | A number representing a role (e.g., train number, shunting team ID) rather than a physical device |
| **GPRS** | General Packet Radio Service |
| **GSM** | Global System for Mobile Communications |
| **GSM-R** | GSM for Railways (the common name for EIRENE) |
| **ISDN** | Integrated Services Digital Network |
| **Location Dependent Addressing** | Automatic routing of a call based on the geographic location of the caller |
| **MSISDN** | Mobile Station International Subscriber Directory Number |
| **NSS** | Network Switching Subsystem |
| **PSTN** | Public Switched Telephone Network |
| **R-GSM** | Railway GSM frequency band |
| **SMS** | Short Message Service |
| **UIC** | International Union of Railways |
| **Um Interface** | GSM Air Interface |
| **VBS** | Voice Broadcast Service |
| **VGCS** | Voice Group Call Service |

#### 1.4 References
1.  ETSI EN 301 515: "Global System for Mobile communication (GSM); Requirements for GSM operation on railways"
2.  ETSI GSM Specifications Series 01-12
3.  UIC Project EIRENE System Requirements Specification (SRS)
4.  EURORADIO FFFIS (Subset-037)

#### 1.5 Overview
The remainder of this document is structured as follows:
*   **Section 2:** Overall Description - Provides context, user characteristics, and general constraints.
*   **Section 3:** Specific Requirements - Details all functional, interface, and non-functional requirements.
*   **Appendix A:** Priority and Acceptance Criteria.

---

### 2. Overall Description

#### 2.1 Product Perspective
EIRENE is a subsystem within the broader European railway telecommunications architecture. It is based on the commercial GSM standard but incorporates critical railway-specific enhancements. It interfaces with existing national railway fixed networks, public telephone networks, on-train systems (via the Cab Radio), and the ERTMS/ETCS train control system. It is designed to replace disparate national analog radio systems to create a seamless, interoperable communications platform.

#### 2.2 Product Functions (Summary)
The core functions of the EIRENE system are:
1.  Railway-specific group and broadcast voice calls (VGCS/VBS).
2.  Functional addressing (calls to a role, e.g., "Train 1234").
3.  Location-dependent addressing (automatic call routing based on train location).
4.  High-priority Railway Emergency Calls.
5.  Dedicated Shunting Mode operations.
6.  Direct Mode Operation (DMO) for off-network communications.
7.  Standard GSM services: telephony, SMS, and circuit-switched/packet-switched data.

#### 2.3 User Characteristics
| User Class | Description | Key Characteristics |
| :--- | :--- | :--- |
| **Train Drivers (Cab Radio Users)** | Primary mobile users for safety-critical and operational communications. | Use functional addressing (train number). Initiate location-dependent calls to controllers. Require simple, reliable HMI, often in high-noise environments. |
| **Controllers/Dispatchers** | Fixed network users managing train movements within a control area. | Receive location-dependent calls from drivers. Initiate group broadcasts to multiple trains/staff. Use sophisticated workstation interfaces. |
| **Trackside Staff (Operational Radio Users)** | Mobile users performing shunting, maintenance, and engineering work. | Use group calls for team coordination. Utilize Shunting Mode. Operate in harsh outdoor environments. |
| **General Railway Staff** | Mobile users for administrative, station, and support communications. | Use standard telephony and group call features. Requirements similar to commercial cellular users but within the private railway network. |
| **ERTMS/ETCS System** | Non-human user (system-to-system). | Uses the GSM-R data bearer (GPRS or circuit-switched) for transmission of safety-critical train control messages via the EURORADIO protocol. |

#### 2.4 Constraints
1.  **Backwards Compatibility:** The system must be compatible with specified versions of underlying GSM standards (ETSI GSM 01-12 series).
2.  **Interoperability Rule:** All requirements marked as mandatory **(M)** in the referenced standards must be implemented. If optional features are implemented, they must conform fully to the standard.
3.  **Regulatory:** National railways are responsible for obtaining public MSISDN number ranges from national regulatory authorities.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** Location information for implementing Location Dependent Addressing is primarily provided by the GSM Cell ID.
*   **Dependency:** The system relies on the commercial availability and correct operation of GSM network infrastructure components (BSS, NSS, GPRS core).
*   **Dependency:** The provision of the fixed network and controller equipment is outside the scope of this SRS but is a prerequisite for system operation.

---

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Voice Group and Broadcast Calls (VGCS/VBS)
*   **FR-1.1 (M):** The system shall support Voice Group Call Service (VGCS) as defined in GSM standards, allowing multiple users to participate in a half-duplex group conversation.
*   **FR-1.2 (M):** The system shall support Voice Broadcast Service (VBS), allowing a single speaker to broadcast to a predefined group of listeners.
*   **FR-1.3 (M):** Group and broadcast calls shall be established using predefined group IDs stored in the network.

##### 3.1.2 Functional Addressing
*   **FR-2.1 (M):** A mobile station (especially a Cab Radio) shall be able to register a Functional Number (e.g., a train running number) with the network.
*   **FR-2.2 (M):** A user shall be able to initiate a call by dialing a Functional Number (e.g., calling "Train 5678").
*   **FR-2.3 (M):** The network shall translate the dialed Functional Number to the current Mobile Station ISDN (MSISDN) for call routing.

##### 3.1.3 Location Dependent Addressing (LDA)
*   **FR-3.1 (M):** When a Cab Radio user initiates a call to a predefined "Controller" short code, the network shall automatically route the call to the controller responsible for the geographic area (Cell ID) where the train is currently located.
*   **FR-3.2 (M):** The mapping between Cell ID and the appropriate controller's telephone number shall be managed by network databases.

##### 3.1.4 Railway Emergency Calls
*   **FR-4.1 (M):** The system shall provide a dedicated, high-priority "Railway Emergency Call" function, distinct from public emergency calls.
*   **FR-4.2 (M):** An emergency call shall be established as a VGCS to a predefined group (e.g., all controllers and drivers in the area).
*   **FR-4.3 (M):** Emergency calls shall be signaled with a distinctive and mandatory audible indication (e.g., a specific ring tone) to all called parties.
*   **FR-4.4 (M):** The call shall use the highest eMLPP priority level (Level 0) and shall be capable of pre-empting any ongoing lower-priority calls.

##### 3.1.5 Shunting Mode
*   **FR-5.1 (M):** The system shall provide a "Shunting Mode" operational state for mobile stations.
*   **FR-5.2 (M):** In Shunting Mode, the mobile station shall automatically join a predefined shunting group call upon entering a designated shunting area (identified by Cell ID).
*   **FR-5.3 (M):** The primary communication in Shunting Mode shall be via the dedicated shunting group call.

##### 3.1.6 Direct Mode Operation (DMO)
*   **FR-6.1 (M):** Mobile stations shall support Direct Mode Operation, allowing direct mobile-to-mobile voice communication without the use of network infrastructure.
*   **FR-6.2 (M):** DMO shall be available when the mobile station is out of network coverage or when explicitly selected by the user.

##### 3.1.7 Basic GSM Services
*   **FR-7.1 (M):** The system shall support full-duplex point-to-point telephony calls between any subscribers within the GSM-R network and to/from connected fixed networks (PSTN/ISDN, private railway network).
*   **FR-7.2 (M):** The system shall support Short Message Service (SMS).
*   **FR-7.3 (M):** The system shall support circuit-switched data services.
*   **FR-7.4 (M):** The system shall support GPRS packet-switched data services.

#### 3.2 External Interface Requirements

##### 3.2.1 Air Interface (Um)
*   **IR-1.1 (M):** The mobile equipment shall comply with the GSM air interface (Um) specifications as defined in the referenced ETSI standards for the R-GSM band.

##### 3.2.2 ERTMS/ETCS Interface (EURORADIO)
*   **IR-2.1 (M):** The Cab Radio shall provide a specified data interface (e.g., RS-422/485, Ethernet) for connection to the EURORADIO unit.
*   **IR-2.2 (M):** The system shall transport EURORADIO FFFIS (Subset-037) messages transparently over the GSM-R data bearer (GPRS preferred).

##### 3.2.3 Fixed Network Interfaces
*   **IR-3.1 (M):** The core network shall interface to Public Switched Telephone Networks (PSTN/ISDN) using standard ISDN User Part (ISUP) signaling.
*   **IR-3.2 (M):** The core network shall interface to private railway fixed networks (e.g., PABX) using appropriate signaling (e.g., Q.SIG, CorNet).

##### 3.2.4 On-Train Interfaces (via Cab Radio)
*   **IR-4.1:** The Cab Radio may provide interfaces for a Train Interface Unit (TIU), public address system, driver's safety device, or on-train recorder. The specification of these interfaces is nationally determined.

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance Requirements
*   **NFR-1.1 (Coverage):** The radio network shall provide a coverage probability of 95% for a minimum received field strength of **-98 dBm** for voice services along the track. For lines with speeds ≤220 km/h where ERTMS/ETCS is deployed, the minimum field strength for data services shall be **-95 dBm**.
*   **NFR-1.2 (Call Setup Time):** Call setup times shall be guaranteed according to the eMLPP priority level, with all security features (authentication, ciphering) enabled. (Specific times are defined in referenced standards, e.g., ≤2 seconds for high-priority calls).
*   **NFR-1.3 (Handover):** The handover success rate within the GSM-R network shall be at least **99.5%** under design load conditions.

##### 3.3.2 Technical Requirements
*   **NFR-2.1 (Frequency):** The system shall operate in the Railway GSM (R-GSM) frequency band:
    *   Uplink (Mobile to Base): 876 – 915 MHz
    *   Downlink (Base to Mobile): 921 – 960 MHz
    *   A dedicated subset (876-880 MHz / 921-925 MHz) is allocated by the UIC.
*   **NFR-2.2 (Reliability):** In case of a failed Railway Emergency Call setup attempt, the mobile equipment shall automatically and repeatedly retry the call setup for a period of up to **30 seconds**.

##### 3.3.3 Environmental & Safety Requirements
*   **NFR-3.1 (Temperature):**
    *   Mobile Equipment (Handheld/Portable): Operational from **-20°C to +55°C**.
    *   Cab Radio Equipment: Operational from **-20°C to +70°C**.
*   **NFR-3.2 (Robustness):** All mobile equipment shall be designed to withstand vibration, shock, and mechanical stress as defined in relevant railway application standards (e.g., EN 50155, EN 61373).
*   **NFR-3.3 (EMC & Safety):** All equipment shall comply with railway-specific Electromagnetic Compatibility (EMC) and electrical safety standards (e.g., EN 50121, EN 60950).

##### 3.3.4 Priority & Pre-emption
*   **NFR-4.1 (eMLPP):** The system shall implement the enhanced Multi-Level Precedence and Pre-emption (eMLPP) feature with the following mandatory priority levels mapped to railway services:
    *   **Level 0:** Railway Emergency Call
    *   **Level 2:** Public Emergency Call, Driver Group Calls
    *   **Level 3:** Railway Operational Calls
    *   **Level 4:** Railway Information Calls, all other calls
*   **NFR-4.2 (Pre-emption):** A call attempt of a higher priority level shall be able to pre-empt resources (e.g., traffic channels) allocated to a call of a lower priority level.

#### 3.4 System Attributes

##### 3.4.1 Security
*   **SA-1 (M):** The system shall support subscriber authentication.
*   **SA-2 (M):** The system shall support ciphering (encryption) of signaling and user data over the air interface.

##### 3.4.2 Interoperability
*   **SA-2 (M):** Compliance with every mandatory requirement marked **(M)** in this document and its referenced standards is the fundamental condition for achieving cross-border and multi-vendor interoperability.

---

### Appendix A: Priority and Acceptance

#### A.1 Requirement Priority
All requirements in Section 3 marked with **(M)** are **Mandatory** for interoperability. Unmarked requirements are conditional or provide explanatory context.

#### A.2 Acceptance Approach
Acceptance of an EIRENE-compliant system or component shall be based on:
1.  **Conformance Testing:** Formal testing against the mandatory requirements of this SRS and the referenced ETSI and UIC standards (e.g., ETSI EN 301 515).
2.  **Interoperability Testing:** Successful cross-connection and operation with other certified EIRENE systems from different suppliers.
3.  **Documentation:** Provision of all required user, maintenance, and technical documentation specifying compliance.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Author | | | |
| Reviewer | | | |
| Approver | | | |