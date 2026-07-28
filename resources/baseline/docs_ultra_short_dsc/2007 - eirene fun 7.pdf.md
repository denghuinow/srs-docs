# Software Requirements Specification (SRS)
## European Integrated Railway Radio Enhanced Network (EIRENE)

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the European Integrated Railway Radio Enhanced Network (EIRENE). The primary purpose of this document is to provide a definitive description of the system for prospective suppliers, developers, and stakeholders, ensuring a common understanding of the capabilities, constraints, and goals of the EIRENE standard. It serves as the basis for system design, implementation, testing, and acceptance.

#### 1.2 Document Conventions
*   **Requirement IDs:** Functional requirements are prefixed with `FR-`. Non-functional requirements are prefixed with `NFR-`.
*   **Priority:** Requirements are categorized as:
    *   **Mandatory (M):** Essential for interoperability. Must be implemented.
    *   **Optional (O):** May be implemented to provide enhanced functionality.
    *   **Informative (I):** Provides context or explanation.
*   **Call Priority Levels:** Referenced as P1 (highest) to P5 (lowest) as defined in Section 3.6.1.

#### 1.3 Intended Audience and Reading Suggestions
*   **Project Managers & Stakeholders:** Focus on Sections 1 (Introduction), 2 (Overall Description), and 5 (Non-Functional Requirements) for scope, positioning, and key constraints.
*   **System Architects & Designers:** Focus on Sections 2 (Overall Description), 3 (Specific Requirements), and 4 (External Interface Requirements) for functional behavior, interfaces, and system context.
*   **Developers & Test Engineers:** Focus on Section 3 (Specific Requirements) for detailed functional and non-functional specifications.
*   **Quality Assurance & Validators:** Use the entire document, especially Section 3 and the acceptance criteria in Section 6, to develop test plans.

#### 1.4 Project Scope
The EIRENE system is a GSM-based digital radio communications standard for European railways. Its scope includes:
*   Defining requirements for the network infrastructure (core, base stations, management systems).
*   Defining requirements for mobile terminals (Cab Radio, Operational Radio, General Purpose Radio).
*   Specifying ground-to-train and ground-to-ground voice and data communication services for operational and support staff to ensure cross-border interoperability.

**Out of Scope:**
*   Detailed design of controller workstation equipment (only the network-side interface is specified).
*   Definition of national numbering plans.
*   Specification of commercial/public passenger information services.

### 2. Overall Description

#### 2.1 Product Perspective
EIRENE is a subsystem within the broader European Rail Traffic Management System (ERTMS) ecosystem. It is part of the Technical Specification for Interoperability (TSI) for the Control-Command and Signalling subsystem. It interfaces with existing railway systems and public networks as shown in the context diagram below.

```
[ERTMS/ETCS RBC] <----> [EIRENE Network] <----> [Private Railway Fixed Network]
       ^                          ^                          ^
       |                          |                          |
[Balise/Train Location]    [Mobile Terminals]         [Public Telephone Network]
       |                          |                          |
[Train-borne Systems]      [Controller Equipment]     [External Callers]
```

#### 2.2 Product Functions (Summary)
1.  Provide interoperable voice call services (point-to-point, group, broadcast, multi-party).
2.  Facilitate high-priority Railway Emergency Calls to ensure safety.
3.  Enable addressing based on user function and geographic location.
4.  Support dedicated Shunting Mode operations with link integrity monitoring.
5.  Provide a Direct Mode (fall-back) for off-network communication.
6.  Offer circuit-switched and packet-switched data bearer services for operational and safety-critical applications (e.g., ERTMS/ETCS).
7.  Manage calls with advanced features including multi-level pre-emption, closed user groups, and call forwarding.

#### 2.3 User Classes and Characteristics
| User Class | Description | Key Characteristics |
| :--- | :--- | :--- |
| **Driver (Cab Radio User)** | Primary user in locomotive cab. | Requires hands-free operation, high reliability, immediate access to emergency and controller calls. Operates at very high speeds. |
| **Operational Staff (Operational Radio User)** | Trackside workers, shunters, maintenance crews. | Often in harsh environments. Requires group communication (especially shunting), location-based services, and ability to initiate emergency calls (if authorized). |
| **General Staff (General Purpose Radio User)** | Administrative, station, depot personnel. | Requires standard voice and data services for support and logistics. Lower environmental robustness requirements. |
| **Controller (Fixed Terminal User)** | Traffic managers in control centers. | Manages multiple simultaneous calls, requires clear priority indication, call queue management, and authority to initiate wide-area calls. |

#### 2.4 Operating Environment
*   **Physical Environment:** Equipment must withstand conditions specified for railway use, including extreme temperatures, humidity, vibration, shock, and electromagnetic interference (EMC). Specific environmental classes are defined for Cab, Operational, and General Purpose terminals.
*   **Technical Environment:** The system is based on the ETSI GSM Phase 2+ standard, operating within designated railway frequency bands. It must interwork with legacy railway fixed networks (PABX, ISDN) and Public Land Mobile Networks (PLMN).

#### 2.5 Design and Implementation Constraints
1.  **MANDATORY:** The system must comply with relevant CENELEC railway standards (e.g., EN 50121, EN 50125) and ISO 9001 quality management principles.
2.  **MANDATORY:** National implementations may impose stricter environmental or performance requirements, but must not break cross-border interoperability.
3.  **ASSUMPTION:** The core network technology is assumed to be GSM as per ETSI standards. Migration paths to future technologies (e.g., 4G/5G) are not defined in this SRS.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** National railway authorities will define the supported languages for voice announcements and terminal menus.
*   **Dependency:** Seamless cross-border operation is dependent on bilateral commercial and technical agreements between adjacent national EIRENE network operators.
*   **Dependency:** Full support for ERTMS/ETCS safety-critical data transmission is dependent on the implementation and configuration of the ERTMS onboard and trackside equipment.

### 3. Specific Requirements

#### 3.1 Voice Call Services

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-1** | The system shall support **Point-to-Point Voice Calls** between any two authorized subscribers (mobile or fixed). | M |
| **FR-2** | The system shall support **Group Calls** where any member of a pre-defined group can talk, and all other members listen. | M |
| **FR-3** | The system shall support **Broadcast Calls** (one-way) from a designated caller (e.g., controller) to all members of a pre-defined group. | M |
| **FR-4** | The system shall support **Multi-party Calls** (conference calls) involving up to six parties, initiated by a subscriber. | O |

#### 3.2 Railway Emergency Call Service

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-10** | The system shall provide a **Railway Emergency Call (REC)** service with two distinct types: "Train Emergency" and "Shunting Emergency". | M |
| **FR-11** | Initiation of an REC shall be restricted to authorized user classes (e.g., Drivers, authorized Operational Staff). | M |
| **FR-12** | An initiated REC shall pre-empt any ongoing calls of lower priority (P2-P5) within its defined geographic area. | M |
| **FR-13** | The call setup time for an REC, from initiation to ringing indication at the called party/parties, shall be less than 2 seconds for 95% of attempts. | M |

#### 3.3 Addressing

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-20** | The system shall support **Functional Addressing**, allowing a user to call a role (e.g., "Driver of Train 1234", "Station Master at Paris Nord") rather than a physical terminal number. | M |
| **FR-21** | The system shall support **Location-Dependent Addressing**, where a call to a generic function (e.g., "Signalman") is routed to the person responsible for the caller's current geographic location. | M |

#### 3.4 Shunting Mode

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-30** | The system shall provide a dedicated **Shunting Mode** operation, which establishes a persistent group call among members of a shunting team. | M |
| **FR-31** | In Shunting Mode, the system shall provide a periodic **Link Assurance Signal** (audible tone) to all participants to confirm radio link integrity. | M |
| **FR-32** | Membership in a shunting group shall be controllable by the network (e.g., by a controller). | M |

#### 3.5 Direct Mode

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-40** | Mobile terminals shall support **Direct Mode Operation (DMO)** for direct radio-to-radio communication without network infrastructure. | M |
| **FR-41** | DMO shall support at least group calls and shall be usable as a fall-back when network coverage is unavailable. | M |

#### 3.6 Call Management & Priority

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-50** | The system shall implement a five-level call priority scheme: <br>1. P1: Railway Emergency <br>2. P2: Control-command (e.g., critical data) <br>3. P3: Public Emergency / Driver Group <br>4. P4: Railway Operation <br>5. P5: Railway Information | M |
| **FR-51** | A higher priority call shall be able to **pre-empt** resources (e.g., traffic channels) used by a lower priority call. | M |
| **FR-52** | The system shall support **Closed User Groups (CUGs)** to restrict communication to defined groups of subscribers. | M |
| **FR-53** | The system shall support call features including Call Forwarding (Unconditional, on Busy, No Reply), Call Hold, Call Waiting, and Call Barring. | O |

#### 3.7 Data Services

| ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-60** | The system shall provide transparent **Circuit-Switched Data** bearer services for general applications. | M |
| **FR-61** | The system shall provide **Packet-Switched Data** bearer services (where implemented by the network). | O |
| **FR-62** | The system shall support the transport of safety-critical data for the **ERTMS/ETCS** train control system with defined quality of service. | M |
| **FR-63** | The system may support Short Message Service (SMS) and Fax services. | O |

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Mobile Terminal UI:** Shall provide clear visual and audible indications for call priority, emergency calls, shunting mode, and link assurance signal.
*   **Controller Terminal UI:** Shall present a call queue with clear visual coding of call priority (P1-P5) and caller identity/function.

#### 4.2 Hardware Interfaces
*   **Mobile Terminal Data Port:** Shall provide a standard data interface (e.g., RS-232, Ethernet, USB) for connection to external train-borne equipment (e.g., ERTMS onboard unit, driver safety device, event recorder).
*   **Location Input:** Mobile terminals shall have an interface to receive location data from external systems (e.g., GPS, balise readers) for functional and location-dependent addressing.

#### 4.3 Software/Communication Interfaces
*   **Interface to Railway Fixed Network (ISDN/PABX):** Shall use standard ISDN PRI or analog interfaces for interconnection with railway telephone networks.
*   **Interface to Public Operator Network (PSTN/PLMN):** Shall use standard SS7 or equivalent signaling for interconnection to public networks.
*   **Interface to ERTMS Radio Block Centre (RBC):** Shall provide a secure, reliable data link for transmission of ETCS messages.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements

| ID | Requirement Description | Verification Criteria |
| :--- | :--- | :--- |
| **NFR-1** | The system shall support reliable communication with mobile terminals traveling at speeds up to **500 km/h**. | M |
| **NFR-2** | The call setup time for a Group Call between drivers shall be less than **5 seconds for 95%** of attempts, and shall not exceed 10 seconds for 99% of attempts. | M |
| **NFR-3** | The network shall provide coverage such that a vehicle-mounted radio can establish and maintain a call **95% of the time over 95% of the geographic area** of designated lines. | M |

#### 5.2 Safety, Reliability & Availability
*   **NFR-10:** System design shall follow relevant CENELEC safety standards (e.g., EN 50126, EN 50128, EN 50129) for safety-related functions (e.g., Emergency Calls, ETCS data).
*   **NFR-11:** Network and mobile equipment shall meet defined Reliability, Availability, and Maintainability (RAM) targets, typically requiring system availability greater than 99.9%.

#### 5.3 Interoperability & Compatibility
*   **NFR-20 (MANDATORY):** A mobile terminal certified as EIRENE-compliant shall be able to register, make, and receive calls on any other EIRENE-compliant network in Europe.
*   **NFR-21 (MANDATORY):** Mobile terminals shall be capable of operating in public GSM networks within the allocated railway frequency bands (where national regulation permits).

### 6. Acceptance Criteria

Acceptance of an EIRENE-compliant system or component shall be based on the following:

1.  **Mandatory Requirement Compliance:** All requirements marked as **Mandatory (M)** in this SRS must be successfully verified.
2.  **Performance Validation:** Key performance indicators (KPIs) such as call setup times (FR-13, NFR-2) and coverage (NFR-3) must be demonstrated to meet the specified statistical targets (95%/99%).
3.  **Functional Testing:** Core services—Voice Calls (FR-1-4), Railway Emergency Calls (FR-10-13), Functional Addressing (FR-20), and Shunting Mode (FR-30-32)—must be validated through end-to-end test scenarios.
4.  **Environmental Testing:** Mobile terminals must pass type-approval tests for the environmental conditions (climatic, mechanical, EMC) specified for their class (Cab, Operational, General Purpose).
5.  **Interoperability Testing:** Successful completion of multi-vendor interoperability test sessions, demonstrating seamless operation between terminals and networks from different suppliers.

---
*This document is a formal specification for the EIRENE system. Any implementation claiming compliance must adhere to the Mandatory requirements herein.*