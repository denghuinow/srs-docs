# **Software Requirements Specification (SRS)**
## **EIRENE (European Integrated Railway Radio Enhanced Network) Functional Requirements Specification**

**Document Version:** 1.0
**Date:** [Date of Generation]
**Status:** Draft for Review

---

### **1. Introduction**

#### **1.1 Purpose**
This document defines the functional requirements for the EIRENE system, a GSM-based digital radio communication system for European railways. Its primary purpose is to specify the capabilities, interfaces, and performance criteria necessary to ensure interoperability across international borders and to enable manufacturing economies of scale. This SRS serves as the authoritative source for system developers, network operators, and railway administrators.

#### **1.2 Scope**
This specification covers the functional requirements for:
*   **Voice Services:** Point-to-point, Railway Emergency, Broadcast, Group, and Multi-party calls.
*   **Data Services:** Short Message Service (SMS), General data applications, Fax, and Train Control data transmission.
*   **Railway-Specific Services:** Functional Addressing, Location-Dependent Addressing, and Shunting Mode operations.
*   **Mobile Equipment:** Three defined types: Cab Radio, General Purpose Radio, and Operational Radio.
*   **Network Infrastructure:** Core requirements for coverage, performance (e.g., call setup times), and interoperability.

**Out of Scope:**
*   Detailed mechanical or electrical specifications for controller equipment interfaces.
*   Definition of specific pre-packaged messaging applications (e.g., for maintenance reporting).
*   Handling of public emergency calls (e.g., dialing '112').
*   Detailed specification of national control/command system interfaces.
*   Comprehensive environmental specifications (e.g., detailed IP ratings, specific shock profiles), though core requirements are defined as constraints.

#### **1.3 Definitions, Acronyms, and Abbreviations**
| Term | Definition |
| :--- | :--- |
| **Cab Radio** | Mobile radio installed in the train driver's cab for operational and safety-critical communications. |
| **EIRENE** | European Integrated Railway Radio Enhanced Network. |
| **Functional Addressing** | A method of addressing users by their role (e.g., "Train 1234", "Signalman Sector A") rather than by a device-specific number. |
| **General Purpose Radio** | Mobile radio used by general railway staff for support and administrative communications. |
| **GSM** | Global System for Mobile Communications. |
| **Link Assurance Signal (LAS)** | A periodic signal transmitted during shunting to confirm the communication link is active. |
| **Operational Radio** | Robust, often handheld, radio used for shunting and other trackside operations. |
| **Railway Emergency Call** | The highest priority call type, initiated with a single action, alerting all relevant controllers and drivers in an area. |

#### **1.4 References**
*   CENELEC EN 50126: Railway applications - The specification and demonstration of Reliability, Availability, Maintainability and Safety (RAMS).
*   CENELEC EN 50128: Railway applications - Communication, signalling and processing systems - Software for railway control and protection systems.
*   EIRENE System Requirements Specification (SRS) - MORANE.
*   GSM Technical Specifications (ETSI/3GPP).

#### **1.5 Document Overview**
This document is structured to present an overall description of the product, followed by specific functional and non-functional requirements. It concludes with appendices for supporting information.

---

### **2. Overall Description**

#### **2.1 Product Perspective**
The EIRENE system is a subsystem within the broader railway control and communication architecture. It interfaces with:
*   **External Systems:** National GSM-R networks, Train Control Systems (via defined interfaces), and potentially balises for location-triggered functions.
*   **Users:** Various railway staff through the defined mobile radio terminals.
*   **Standards:** Must operate within the regulatory and technical framework defined by European railway standards (CENELEC) and allocated frequency bands.

#### **2.2 Product Functions (Summary)**
*   High-priority voice call establishment and management.
*   Railway-specific call types (Emergency, Shunting, Broadcast).
*   Dynamic user addressing based on function and location.
*   Seamless cross-border network handover.
*   Data communication for operational and control purposes.
*   Direct Mode Operation (DMO) for off-network communication.

#### **2.3 User Characteristics**
| Stakeholder | Role & Characteristics |
| :--- | :--- |
| **Train Driver** | Primary user of Cab Radio. Requires simple, fast, and unambiguous interface for safety-critical communications. May be under high cognitive load. |
| **Primary/Secondary Controller** | Manages train movements in a control center. Requires ability to initiate group calls, handle emergency calls, and address drivers functionally. |
| **Shunting Team Member** | Uses Operational Radio in harsh environments. Requires hands-free operation and LAS capability. |
| **General Railway Staff** | Uses General Purpose Radio for logistical and support tasks. Typical mobile radio user. |
| **Network Operator** | Maintains the GSM-R network infrastructure. Requires standards-compliant performance for interoperability. |

#### **2.4 Constraints**
1.  **Regulatory:** Must comply with CENELEC standards for safety and Human-Machine Interface (HMI).
2.  **Environmental:** Equipment must be designed to operate reliably under typical railway conditions: temperature extremes, high vibration, and electromagnetic interference (EMC).
3.  **Operational:** Five distinct call priority levels (including "Railway Emergency") must be implemented consistently across all networks.
4.  **Technical:** Functional numbers (e.g., train IDs) must be uniquely managed across all participating networks.
5.  **Technical:** System must operate within the designated railway frequency bands (e.g., 876-880 MHz uplink / 921-925 MHz downlink in Europe).

#### **2.5 Assumptions and Dependencies**
*   National railway administrations will implement the core EIRENE specifications to ensure interoperability.
*   Underlying GSM network technology provides the fundamental bearer services.
*   Functional numbering plans are administered and synchronized across borders.

---

### **3. Specific Requirements**

#### **3.1 Functional Requirements**

##### **3.1.1 Voice Call Services**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-V-01** | The system shall allow a user to initiate a **Point-to-Point** voice call to another user by entering a Functional Number, ISDN number, or from an address book. | High |
| **FR-V-02** | The Cab Radio shall provide a dedicated, single-action control (e.g., button) for initiating a **Railway Emergency Call**. | High |
| **FR-V-03** | A Railway Emergency Call, once initiated, shall establish a voice connection to all relevant controllers and drivers in the calling train's area within **2 seconds** (see success metric). | High |
| **FR-V-04** | The system shall allow an authorized controller to initiate a **Broadcast Call** to all mobile stations in a defined geographical area. | High |
| **FR-V-05** | The system shall support **Group Calls**, allowing a user to speak to a pre-defined group of users. | High |
| **FR-V-06** | The system shall support **Multi-party Calls**, allowing a user to conference in multiple other users dynamically. | Medium |

##### **3.1.2 Data Services**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-D-01** | The system shall support the sending and receiving of **Short Messages (SMS)** between subscribers. | High |
| **FR-D-02** | The system shall provide a transparent data bearer service for **General Applications** (e.g., database queries, e-mail). | Medium |
| **FR-D-03** | The system shall support **Group 3 Fax** transmission. | Low |
| **FR-D-04** | The system shall provide a secure, high-availability data channel for **Train Control** system information. | High |

##### **3.1.3 Railway-Specific Services**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-R-01** | The system shall support **Functional Addressing**. A user shall be reachable via a number representing their function (e.g., train number, signal box ID). | High |
| **FR-R-02** | The system shall support **Location-Dependent Addressing**. A call to a functional number (e.g., "Signalman") shall be routed to the user currently responsible for the caller's geographical location. | High |
| **FR-R-03** | The Operational Radio shall support a **Shunting Mode**. In this mode, the radio shall automatically transmit a periodic **Link Assurance Signal (LAS)** to the driver's Cab Radio when the Push-to-Talk (PTT) is not activated. | High |
| **FR-R-04** | The Cab Radio shall provide clear visual and/or audible indication of the receipt of a valid LAS. | High |

##### **3.1.4 Mobility Management**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-M-01** | The mobile station shall **automatically select and register** on the appropriate EIRENE network as the train moves, including when crossing international borders, without driver intervention. | High |
| **FR-M-02** | The system shall maintain voice and data connectivity for trains traveling at speeds up to **500 km/h**. | High |
| **FR-M-03** | The system shall support **Direct Mode Operation (DMO)**, allowing mobile stations to communicate directly when outside network coverage. | Medium |

#### **3.2 Non-Functional Requirements**

##### **3.2.1 Performance Requirements**
| ID | Requirement |
| :--- | :--- |
| **NFR-PER-01** | **Railway Emergency Call Setup Time:** ≥95% of calls shall be established end-to-end within **2 seconds**. |
| **NFR-PER-02** | **Group Call Setup Time:** ≥95% of calls within the same area shall be established within **5 seconds**. |
| **NFR-PER-03** | **Network Coverage:** The system shall provide continuous voice service along all designated railway lines, with handover performance sufficient to support seamless communication at 500 km/h. |

##### **3.2.2 Safety & Reliability**
| ID | Requirement |
| :--- | :--- |
| **NFR-SAF-01** | The design of the Cab Radio HMI shall comply with CENELEC standards (e.g., EN 50128) for safety-related applications. |
| **NFR-SAF-02** | The system shall implement five distinct, network-enforced **Call Priority Levels**. A higher priority call shall pre-empt resources from a lower priority call. |
| **NFR-REL-01** | Mobile equipment shall meet minimum MTBF (Mean Time Between Failures) targets suitable for 24/7 railway operation. |

##### **3.2.3 Usability Requirements**
| ID | Requirement |
| :--- | :--- |
| **NFR-USA-01** | The Cab Radio interface shall be designed for use while driving, with large, tactile controls and clear visual displays under all lighting conditions. |
| **NFR-USA-02** | The system shall support a minimum of **10 languages** for user interface and announcements. |

#### **3.3 System Interface Requirements**
*   **Air Interface:** Shall be based on GSM standards in the designated railway frequency bands.
*   **Network-to-Network Interface (NNI):** Shall support the MAP (Mobile Application Part) signaling protocol for cross-border mobility and call routing.
*   **Data Interface:** Shall provide a standard interface (e.g., X.25, IP-based) for connection to external Train Control and data application systems.

---

### **4. Appendices**

#### **Appendix A: Use Case Elaboration**
**Use Case UC-01: Initiate Railway Emergency Call**
*   **Actor:** Train Driver
*   **Precondition:** Cab Radio is powered on and registered on the network.
*   **Main Flow:**
    1.  Driver identifies an emergency situation.
    2.  Driver presses the dedicated, red Railway Emergency Call button.
    3.  System immediately seizes the radio channel with the highest priority.
    4.  System establishes a call to all predefined recipients (controllers, other drivers in area).
    5.  System provides clear confirmation (audible and visual) that the emergency call is active.
*   **Postcondition:** An all-party emergency voice channel is active.

**Use Case UC-04: Automatic Cross-Border Network Selection**
*   **Actor:** Mobile Station (Cab Radio)
*   **Precondition:** Train is operating on Network A.
*   **Main Flow:**
    1.  As the train approaches the border, the mobile station monitors broadcast channels from neighboring networks.
    2.  Based on pre-configured operator preferences and signal strength, the mobile station selects the correct EIRENE network (Network B).
    3.  The mobile station performs a location update/registration with Network B.
    4.  Registration occurs without interrupting any ongoing call (if handover is supported) or transparently during idle mode.
*   **Postcondition:** The mobile station is registered on Network B and is reachable via its functional number.

#### **Appendix B: Undecided Issues & TBDs**
1.  **UC-02 Implementation:** The technical mechanism for "automatic joining for calls to all drivers in same area" requires further network architecture specification.
2.  **Language Support:** National implementations may choose to support more than the mandated 10 languages.
3.  **Service Classes:** A decision is pending on whether to define different QoS classes for rural vs. high-traffic areas.
4.  **Controller Responsibilities:** The precise operational split of duties between Primary and Secondary Controllers is to be defined nationally.
5.  **Directed Network Selection:** The requirement and method for network selection triggered by external devices (e.g., balises) needs further definition.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| **Product Manager** | | | |
| **Lead System Architect** | | | |
| **Quality Assurance** | | | |