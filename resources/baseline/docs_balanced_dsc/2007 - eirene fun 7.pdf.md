# Software Requirements Specification (SRS)
## European Integrated Railway Radio Enhanced Network (EIRENE)

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the EIRENE digital radio communication system. It serves as a comprehensive guide for stakeholders, including system manufacturers, network operators, and railway administrators, to ensure the development and deployment of an interoperable, reliable, and safe mobile communication network for European railways.

#### 1.2 Scope
The EIRENE system provides a standardized digital radio communication platform for:
*   **Ground-to-Train Communications:** Voice and data communications between controllers and train drivers/cabs.
*   **Ground-to-Ground Mobile Communications:** Communications for trackside workers, station staff, shunting teams, and administrative personnel.
*   **Cross-Border Interoperability:** Seamless communication for trains operating on international routes.
*   **Safety-Critical and Operational Communications:** Including Railway Emergency Calls (REC), group calls, and shunting operations.

**Out of Scope:** The specification of underlying radio transmission technology (e.g., GSM-R), detailed hardware design, and national legacy system migration strategies, except where they interface with EIRENE requirements.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **Cab Radio:** Fixed mobile terminal installed in a train driver's cab.
*   **Controller:** Railway operational staff responsible for managing train movements (Primary, Secondary, Power).
*   **Direct Mode Operation (DMO):** Communication directly between mobiles without network infrastructure.
*   **EIRENE:** European Integrated Railway Radio Enhanced Network.
*   **ERTMS/ETCS:** European Rail Traffic Management System / European Train Control System.
*   **Functional Number (FN):** A number representing a role (e.g., "Driver of Train XYZ") rather than a physical device.
*   **GSM-R:** GSM for Railways (the bearer technology for EIRENE).
*   **Link Assurance Signal (LAS):** Periodic tone transmitted during shunting to confirm radio link integrity.
*   **REC:** Railway Emergency Call.
*   **Shunting:** Low-speed train movement for assembly or disassembly.

#### 1.4 References
*   EIRENE System Requirements Specification (SRS) – UIC Project EIRENE.
*   GSM-R Functional Requirements Specification (FRS) – UIC Project EIRENE.
*   Relevant ETSI and IEC standards for railway communications and environmental resilience.

#### 1.5 Overview
This document is structured to present overall product perspective, followed by specific functional and non-functional requirements, data models, and external interfaces. It concludes with appendices covering user stories, open issues, and analysis models.

### 2. Overall Description

#### 2.1 Product Perspective
EIRENE is a subsystem within the broader railway operational and control ecosystem. It interfaces with:
*   **External Systems:** ERTMS/ETCS (for train control data), Public Switched Telephone Networks (PSTN), and national legacy radio systems during transition.
*   **Users:** Drivers, controllers, trackside staff via mobile stations (MS) and dispatcher terminals.
*   **Environment:** Must operate under stringent railway conditions (vibration, temperature, electromagnetic interference).

#### 2.2 Product Functions (Summary)
1.  Voice Call Establishment and Management (Individual, Group, Broadcast).
2.  Railway Emergency Call (REC) initiation, handling, and termination.
3.  Functional Number registration and management.
4.  Call pre-emption and priority handling.
5.  Shunting Mode operation with Link Assurance Signal.
6.  Direct Mode Operation for off-network communication.
7.  Short Message Service (SMS) and data transfer.
8.  Automatic and manual network selection, especially for border crossing.
9.  Location-dependent addressing and call routing.

#### 2.3 User Characteristics
| User Class | Primary Role | Key Characteristics |
| :--- | :--- | :--- |
| **Railway Driver** | Operate train, respond to signals/controllers. | Uses Cab Radio. Requires simple, fast, and reliable interface, especially for emergency calls. May operate cross-border. |
| **Controller** | Manage train movements in a defined area. | Uses fixed or mobile dispatcher terminal. Requires ability to manage multiple concurrent calls, group communications, and handle emergencies. |
| **Trackside Worker** | Perform maintenance, shunting, inspections. | Uses handheld or vehicle-mounted Operational Radio. Often works at track level; may require DMO. |
| **Network Operator** | Maintain and administer EIRENE network. | Technical staff. Requires management tools for subscriber data, priority levels, group definitions, and network monitoring. |
| **System Manufacturer** | Develop compliant mobile and infrastructure equipment. | Engineering teams. Requires precise, unambiguous specifications for implementation. |

#### 2.4 Constraints
1.  **Regulatory:** Must comply with national and European railway safety and telecommunications regulations.
2.  **Technical:** Based on GSM-R standards. Must ensure backward compatibility where required and interoperability at borders.
3.  **Operational:** System availability and performance are critical for safety. Degraded modes of operation (e.g., DMO) must be supported.
4.  **Environmental:** All equipment must meet specified climatic (temperature, humidity), mechanical (shock, vibration), and ElectroMagnetic Compatibility (EMC) requirements for railway use.

#### 2.5 Assumptions and Dependencies
*   A GSM-R network infrastructure is deployed and operational in the coverage area.
*   Bilateral/multilateral agreements exist for network interconnection and roaming at international borders.
*   A standardized numbering plan (for telephone numbers and functional numbers) is implemented by all participating networks.
*   National authorities will define the implementation of optional features to ensure minimum interoperability is not compromised.

### 3. Specific Requirements

#### 3.1 Functional Requirements
##### 3.1.1 Voice Call Services
*   **FR-001: Individual Call.** The system shall allow a user to establish a point-to-point voice call to another user by dialing their telephone number or functional number.
*   **FR-002: Group Call.** The system shall allow a user (e.g., a controller) to establish a one-to-many voice call to a pre-defined group of users (e.g., all drivers in an area).
*   **FR-003: Broadcast Call.** The system shall allow a controller to establish a one-way voice announcement to all mobiles in a specific geographical area.
*   **FR-004: Railway Emergency Call (REC).** The system shall provide a dedicated, single-action means (e.g., button) for a driver to initiate an REC.
    *   **FR-004.1:** Upon initiation, the REC shall pre-empt any ongoing lower-priority calls in the target group/area.
    *   **FR-004.2:** A distinctive warning tone shall be played to all recipients before the speech phase.
    *   **FR-004.3:** The call shall be established to a pre-defined group (e.g., relevant controller and all trains in the area).
*   **FR-005: Call Priority and Pre-emption.** The system shall manage calls based on a multi-level priority scheme.
    *   **FR-005.1:** An incoming higher-priority call shall be able to pre-empt an ongoing lower-priority call on a shared resource (e.g., radio channel).
    *   **FR-005.2:** The user of the pre-empted call shall receive a clear indication.

##### 3.1.2 Registration and Management Services
*   **FR-006: Functional Number Registration.** The system shall allow a mobile station (e.g., Cab Radio) to register its current functional number (e.g., train number) with the network.
*   **FR-007: Location-Dependent Addressing.** The network shall be capable of routing calls made to a functional number (e.g., "signalman at location X") based on the caller's or callee's current location.

##### 3.1.3 Operational Modes
*   **FR-008: Shunting Mode.** The system shall support a shunting operational mode.
    *   **FR-008.1:** In this mode, a dedicated group call shall be established between the shunting leader and the driver.
    *   **FR-008.2:** A periodic Link Assurance Signal (LAS) shall be transmitted to confirm channel integrity.
*   **FR-009: Direct Mode Operation (DMO).** Mobile stations shall be able to communicate directly with each other without network infrastructure when outside network coverage or for local working.

##### 3.1.4 Data Services
*   **FR-010: Text Message Transfer.** The system shall support the transfer of short text messages between users and applications.
*   **FR-011: Data Transmission.** The system shall provide circuit-switched and packet-switched bearer services for other railway applications (e.g., ERTMS/ETCS).

##### 3.1.5 Mobility Management
*   **FR-012: Network Selection.** The mobile station shall automatically select and attach to an authorized EIRENE network.
    *   **FR-012.1:** At power-up, it shall select the home network or a preferred network.
    *   **FR-012.2:** When crossing a border, it shall automatically attempt to register with the new national EIRENE network (subject to **Undecided Issue #1**).

#### 3.2 Non-Functional Requirements
##### 3.2.1 Performance Requirements
*   **NFR-001: Call Setup Time.** Railway Emergency Calls shall be established within **2 seconds** for 95% of attempts. Group calls between drivers shall be established within **5 seconds** for 95% of attempts.
*   **NFR-002: Text Message Transfer Time.** A short message segment shall be transferred end-to-end within **30 seconds** for 95% of attempts.
*   **NFR-003: Operational Speed.** The system shall maintain communication with mobile stations traveling at speeds up to **500 km/h**.
*   **NFR-004: Coverage Availability.** For vehicle-mounted radios, a radio connection shall be available for at least **95% of the time** over **95% of the designated operational area**.

##### 3.2.2 Reliability, Availability, and Maintainability
*   **NFR-005: Battery Life.** Handheld mobile stations shall have a minimum battery life of **8 hours** under a defined typical usage cycle.
*   **NFR-006: System Availability.** Network infrastructure shall have an availability target of 99.95% or higher (to be defined by network operator).

##### 3.2.3 Safety and Security
*   **NFR-007: Safety Integrity.** Safety-related functions (e.g., REC) shall be designed to appropriate Safety Integrity Levels (SIL) as per railway standards.
*   **NFR-008: Access Security.** The system shall authenticate mobile stations and prevent unauthorized access to network services.

##### 3.2.4 Environmental Requirements
*   **NFR-009: Climatic & Mechanical Resilience.** All equipment shall withstand railway environmental conditions as per EN 50125 (climatic), EN 61373 (vibration/shock), and EN 50121 (EMC).

#### 3.3 Data Requirements
Key persistent data entities shall include:
*   **Subscriber Profile:** (Telephone Number, Functional Number(s), Priority Level, Group Memberships, Access Rights).
*   **Group Definitions:** (Group ID, Service Area, Member List, Call Type).
*   **Train Registry:** (Train Number, Engine ID, Registered Cab Radio ID, Active Functional Number).
*   **Call Records:** (Call ID, Call Type, Originator, Recipients, Timestamps, Priority, Clear Reason) – especially for RECs.

#### 3.4 External Interface Requirements
*   **EI-001: ERTMS/ETCS Interface.** The Cab Radio shall provide a standardized data interface (e.g., according to FFFIS) for the transmission of Euroradio messages for train control.
*   **EI-002: Dispatcher Terminal Interface.** The network shall provide an interface for controller workstations to initiate calls, manage groups, and view subscriber status.
*   **EI-003: PSTN/ISDN Interface.** The network shall interface with public telephony networks for calls to/from non-railway parties.

### 4. Appendices

#### Appendix A: User Stories Mapping
| User Story ID | From Section 1.2 | Mapped Functional Requirements |
| :--- | :--- | :--- |
| US-01 | Driver - Emergency Call | FR-004, FR-004.1, FR-004.2, FR-004.3 |
| US-02 | Controller - Group Call | FR-002, FR-012.2 (location-based) |
| US-03 | Shunter - Link Assurance | FR-008, FR-008.1, FR-008.2 |
| US-04 | Worker - Direct Mode | FR-009 |
| US-05 | Operator - Management | Implied by data requirements and management tools. |
| US-06 | Driver - Border Crossing | FR-012, FR-012.1, FR-012.2 |

#### Appendix B: Undecided Issues and TBDs
1.  **Automatic Network Selection at Borders:** Decision required on whether selection is fully automatic (directed by network) or requires manual driver confirmation.
2.  **Alphanumeric Train Number Support:** Standardization required to ensure cross-border interoperability of functional number registration.
3.  **High-Percentile Call Setup Times:** Specific maximum time for 99% of calls needs to be defined (e.g., < 3s for REC, < 7.5s for group calls).
4.  **Controller Role Harmonization:** National variations in Primary/Secondary controller responsibilities may impact call routing logic.
5.  **Optional Feature Implementation:** Risk that national choices on optional features (text messaging, fax) create service inconsistencies. A minimum mandatory set for borders is recommended.
6.  **Enhanced Location Accuracy:** Method for providing more precise location data (e.g., GPS integration with FN registration) for improved location-dependent addressing.

#### Appendix C: Analysis Models (Optional - Placeholder)
*   **Use Case Diagrams:** For key processes: REC Initiation, Shunting Mode, Functional Registration.
*   **State Diagrams:** For mobile station states (e.g., idle, call active, DMO, network searching).
*   **Sequence Diagrams:** For call setup with pre-emption, border crossing registration.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Architect | | | |
| Quality Assurance | | | |