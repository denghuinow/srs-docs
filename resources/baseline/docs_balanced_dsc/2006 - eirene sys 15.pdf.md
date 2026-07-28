# Software Requirements Specification (SRS)
## European Integrated Railway Radio Enhanced Network (EIRENE) System
**Document Version:** 1.0  
**Date:** [Date of Generation]  
**Status:** Approved (Based on EIRENE Specification Version 15, 17 May 2006)

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the European Integrated Railway Radio Enhanced Network (EIRENE) system. It serves as a comprehensive guide for stakeholders, including GSM-R operators, network infrastructure providers, mobile equipment manufacturers, and railway personnel, to ensure the development and deployment of an interoperable, safe, and reliable digital railway communication system based on GSM technology.

#### 1.2 Scope
The EIRENE system provides standardized mobile communication for European railways to facilitate cross-border interoperability. The scope encompasses:
*   **Ground-to-Train Communications:** Voice and data communications between fixed network elements (controllers) and mobile equipment on trains (Cab Radios).
*   **Ground-to-Ground Mobile Communications:** Communications for trackside workers, station staff, and administrative personnel using General Purpose (GP) and Operational radios.
*   **Mandatory vs. Optional Features:** Clear distinction between core requirements essential for interoperability and optional features that must be implemented consistently if chosen.
*   **System Boundaries:** Includes mobile equipment (Cab, GP, Operational radios), GSM-R network infrastructure, and core network services (functional numbering, location-dependent routing). Interfaces with external systems like ERTMS/ETCS are defined but their internal workings are out of scope.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **Cab Radio** | Mobile station installed in a train driver's cab. |
| **eMLPP** | Enhanced Multi-Level Precedence and Pre-emption. GSM feature for call priority handling. |
| **EIRENE** | European Integrated Railway Radio Enhanced Network. |
| **ERTMS/ETCS** | European Rail Traffic Management System / European Train Control System. |
| **FN** | Functional Number. A role-based number (e.g., Train Number, Controller Number). |
| **GP Radio** | General Purpose mobile station for administrative and station staff. |
| **GSM-R** | GSM for Railways. |
| **IMSI** | International Mobile Subscriber Identity. |
| **LDA** | Location Dependent Addressing. |
| **MMI** | Man-Machine Interface. |
| **MS** | Mobile Station. |
| **MSISDN** | Mobile Station International Subscriber Directory Number. |
| **Operational Radio** | Robust mobile station for trackside and shunting personnel. |
| **USSD** | Unstructured Supplementary Service Data. |
| **VGCS** | Voice Group Call Service. |

#### 1.4 References
1.  EIRENE System Requirements Specification, Version 15 (17 May 2006).
2.  EN 301 515: "GSM Railway specific requirements".
3.  ENV 50121 series: "Railway applications - Electromagnetic compatibility".
4.  MORANE Specifications (Mobile Radio for Railways Networks in Europe).
5.  UIC Project EIRENE Functional Requirements Specification (FRS).

#### 1.5 Document Overview
This document is structured to present an overall description of the EIRENE system, followed by detailed specific requirements. It covers stakeholder needs, system features, data models, functional processes, and non-functional constraints.

### 2. Overall Description

#### 2.1 Product Perspective
The EIRENE system is a subsystem within the broader European railway telecommunications infrastructure. It interfaces with:
*   **External Systems:** ERTMS/ETCS (via EURORADIO FFFIS interface), national railway operational systems, and public switched telephone networks (PSTN).
*   **Users:** Train drivers, controllers, shunting teams, and maintenance staff.
*   **Operating Environment:** Harsh railway environments including extremes of temperature, vibration, shock, and electromagnetic interference.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Train Driver** | Operates Cab Radio. Requires simple, fast interactions under high cognitive load. | Single-action emergency calls, clear priority handling, intuitive shunting mode. |
| **Railway Controller** | Uses fixed terminal. Manages multiple simultaneous communications. | Automatic caller identification with location, unambiguous call priority indication, efficient group call management. |
| **Shunting Personnel** | Uses Operational Radio in depots/yards. Works in teams. | Secure team communication (dedicated group), rugged device, easy mode activation. |
| **Trackside Worker** | Uses Operational Radio. Works in isolated, high-risk areas. | Reliable emergency communication, functional number registration, durable device. |
| **Network Planner** | Designs GSM-R network. Technical expert. | Precise coverage and performance criteria, clear interface specifications. |
| **System Administrator** | Manages network and user data. | Tools for FN management, conflict resolution, and system monitoring. |

#### 2.3 Operating Environment
*   **Hardware:** GSM-R base stations, network switches, Cab/GP/Operational radios meeting specified power and environmental classes.
*   **Software:** GSM protocol stacks, EIRENE-specific applications (eMLPP, VGCS, USSD handlers), network management systems.
*   **Physical Environment:** Operational radios must be IP54 rated. Cab radios must withstand temperatures up to +70°C. All equipment must comply with railway EMC standards (ENV 50121).

#### 2.4 Design and Implementation Constraints
1.  **Regulatory:** Must operate within the UIC frequency band (876-880 MHz uplink / 921-925 MHz downlink) as allocated by national regulators.
2.  **Standards Compliance:** Mandatory compliance with referenced GSM (EN 301 515) and MORANE standards.
3.  **Interoperability:** Core functional requirements are mandatory for cross-border operation. Optional features, if implemented, must follow the specified standard to avoid fragmentation.
4.  **Legacy Systems:** Must minimize EMC interference with existing railway signaling and control systems.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** National frequency allocation will be completed per CEPT/ECC decisions.
*   **Assumption:** Bilateral agreements for cross-border network interconnection will be established.
*   **Dependency:** Successful integration with ERTMS/ETCS depends on the implementation of the standardized EURORADIO FFFIS interface.
*   **Dependency:** Manufacturer compliance is dependent on the availability of clear, testable type-approval specifications.

### 3. System Features and Requirements

#### 3.1 Feature: Mobile Registration and Attachment
**Description:** The mobile station shall automatically register with an authorized GSM-R network upon power-up.
*   **Requirement 3.1.1:** The MS shall perform a self-test upon power-on.
*   **Requirement 3.1.2:** The MS shall attempt GSM IMSI attach to a network based on a priority list stored on the SIM card.
*   **Requirement 3.1.3:** (Optional) The MS may support automatic network selection. If implemented, the user shall be able to deactivate it via simple MMI actions.

#### 3.2 Feature: Functional Number Management
**Description:** Users shall be able to register a role-based Functional Number (FN) which is mapped to their device's MSISDN for routing.
*   **Requirement 3.2.1:** The user shall be able to register and de-register a Functional Number via USSD commands.
*   **Requirement 3.2.2:** The network shall maintain a routing database that maps the active FN to the corresponding MSISDN.
*   **Requirement 3.2.3:** The system shall detect and resolve FN conflicts (e.g., duplicate train number registration) via validation and forced de-registration procedures, notifying the affected user.
*   **Requirement 3.2.4:** (Undecided) The system shall handle alphanumeric train numbers. Implementation may require terminal-level translation or national solutions.

#### 3.3 Feature: Call Setup and Arbitration
**Description:** The system shall support multiple call types (point-to-point, group, broadcast) with priority-based arbitration.
*   **Requirement 3.3.1:** The radio shall determine call type, priority (based on eMLPP), and destination based on MMI input (short code dialing or function key).
*   **Requirement 3.3.2:** For Cab Radios, incoming or new outgoing calls of higher priority shall pre-empt ongoing calls of lower priority according to defined eMLPP rules.
*   **Requirement 3.3.3:** Call setup time shall conform to specified limits based on eMLPP priority, with end-to-end network transit delays not exceeding 250ms.

#### 3.4 Feature: Railway Emergency Call
**Description:** A train driver must be able to instantly initiate a high-priority call to alert controllers and nearby trains.
*   **Requirement 3.4.1:** The Cab Radio shall have a dedicated, protected physical button for initiating a Railway Emergency Call.
*   **Requirement 3.4.2:** A single press of the emergency button shall initiate a VGCS call to a predefined emergency group with the highest eMLPP priority.
*   **Requirement 3.4.3:** The call shall be automatically re-attempted in case of setup failure.
*   **Requirement 3.4.4:** Upon call termination, a confirmation message shall be sent to the initiator's display after a network-controlled delay with a random offset to prevent congestion.
*   **Requirement 3.4.5:** The network shall provide the controller's terminal with the caller's Functional Number and location (minimum: current GSM cell ID) for all emergency calls.

#### 3.5 Feature: Shunting Mode Operation
**Description:** Provides secure group communication for personnel involved in shunting operations.
*   **Requirement 3.5.1:** The user shall be able to manually activate "Shunting Mode."
*   **Requirement 3.5.2:** Upon activation, the radio shall automatically register a shunting Functional Number and join a common shunting coordination VGCS.
*   **Requirement 3.5.3:** Through coordination on the common channel, the user shall be able to join a dedicated shunting group call (Group ID 501-520).
*   **Requirement 3.5.4:** The dedicated shunting group call shall maintain a Link Assurance Signal (tone) to confirm channel integrity.

#### 3.6 Feature: Location-Dependent Addressing (LDA)
**Description:** Short code dialing (e.g., "0" for controller) shall route the call to the correct destination based on the caller's geographical location.
*   **Requirement 3.6.1:** The network shall route short code dialed calls based on the GSM cell in which the caller is currently registered.
*   **Requirement 3.6.2:** (Optional) The system may support enhanced LDA (eLDA) using external location data (e.g., from a train's odometer) for more precise routing, provided it complies with eLDA specifications.

#### 3.7 Feature: Direct Mode Operation (DMO)
**Description:** Allows mobile-to-mobile communication without network infrastructure, used as a fallback or in coverage gaps.
*   **Requirement 3.7.1:** (Optional) DMO is an optional feature. If implemented by a manufacturer or network, it shall strictly follow the specified channel arrangements and protocol requirements.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Cab Radio MMI:** Must include a dedicated, hard-wired emergency button, a display for Functional Number and call status, and intuitive controls for shunting mode and priority call management.
*   **Operational Radio MMI:** Must be operable with gloves, include an emergency button, and provide clear audio in high-noise environments.

#### 4.2 Hardware Interfaces
*   **Cab Radio:** Must provide a standardized interface (e.g., FFFIS) for connection to on-train systems such as ERTMS/ETCS.
*   **All Radios:** SIM card interface compliant with GSM standards.

#### 4.3 Software/Protocol Interfaces
*   **Air Interface:** GSM Phase 2+ protocols with EIRENE-specific extensions for eMLPP, VGCS, and USSD.
*   **Network-Network Interface (NNI):** For cross-border interconnection, based on standardized GSM MAP and ISUP protocols.
*   **EURORADIO Interface:** Defined FFFIS for safe data transmission to/from ERTMS/ETCS.

#### 4.4 Communication Interfaces
*   **GSM-R Um Interface:** Between MS and BTS in the UIC frequency band.
*   **Direct Mode Interface:** Specified radio interface for optional DMO operation.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   **Coverage & Reliability:** The network shall provide 95% coverage probability at the specified minimum field strength levels (-98 dBm for 95% of time, 95% of locations). Handover success rate shall be ≥99.5% under design load conditions.
*   **Call Setup Time:** As defined by eMLPP priority levels, with full authentication and ciphering. Network transit delay shall be <250ms.
*   **Battery Life:** Handheld Operational/GP radios shall have a minimum battery life of 8 hours under a defined duty cycle (5% transmit, 5% receive, 90% standby). Cab radios shall provide backup power for 6 hours upon main power failure.

#### 5.2 Safety & Environmental Requirements
*   **Environmental Tolerance:**
    *   Cab Radio: Operational from -20°C to +70°C.
    *   GP/Operational Radio: Operational from -20°C to +55°C.
    *   All equipment shall withstand railway-specific vibration and shock profiles.
    *   Operational Radios shall meet at least IP54 ingress protection.
*   **EMC Compliance:** All equipment shall comply with the ENV 50121 series for railway EMC. GSM transmission masks shall take precedence within the GSM operating band.

#### 5.3 Interoperability & Compliance Requirements
*   **Mandatory Compliance:** The system shall comply with all mandatory requirements of EN 301 515 and the MORANE specifications for services, interfaces, and protocols.
*   **Optional Feature Consistency:** If an optional feature (e.g., DMO, eLDA) is implemented, it shall be implemented in full compliance with the relevant EIRENE specification clauses.

### 6. Data Model and Domain Information
*(See Section 5 of the provided input for detailed entity definitions.)*
The system shall manage the following core data entities:
*   **Mobile Station (MS)**
*   **Functional Number (FN)**
*   **Train Journey**
*   **Shunting Group**
*   **Network Cell**
*   **Emergency Call Record**

### 7. Appendices

#### 7.1 Risk Log
| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| Interoperability Failure | Medium | High | Strict adherence to mandatory specs; formal certification testing process. |
| Network Coverage Gaps | Medium | High | Careful planning against field strength criteria; allow DMO as fallback. |
| Emergency Call Congestion | Low | Critical | Use of eMLPP pre-emption; confirmation message delay with random offset. |
| Functional Number Conflict | Medium | Medium | Implement robust registration validation and forced de-registration procedures. |

#### 7.2 Undecided and Open Issues
1.  **Alphanumeric Train Numbers:** Final handling method pending (terminal translation vs. national solution).
2.  **Automatic Network Selection:** Optional for implementation.
3.  **Direct Mode (DMO):** Optional feature with strict implementation rules if used.
4.  **Text Messaging (SMS):** No international application standardization; left for national implementation.
5.  **Enhanced LDA (eLDA):** Optional feature dependent on external location data.
6.  **Controller Location Display:** Optional feature. If provided, must at minimum display current GSM cell.

---
*This SRS document is derived from the approved EIRENE System Requirements Specification (Version 15) and is intended to guide subsequent design, development, and testing activities.*