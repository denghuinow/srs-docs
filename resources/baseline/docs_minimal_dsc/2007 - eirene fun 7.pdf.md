# Software Requirements Specification (SRS)
## GSM-Railway (GSM-R) Interoperable Communications System

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the GSM-Railway (GSM-R) Interoperable Communications System. It is intended to serve as a comprehensive reference for developers, testers, project managers, and stakeholders involved in the design, implementation, verification, and deployment of the system.

#### 1.2 Scope
The GSM-R system is a pan-European, interoperable mobile voice and data communications network based on GSM technology, specifically designed for railway operations. The primary purpose is to ensure seamless cross-border interoperability on international rail lines and to replace disparate national legacy systems.

**In-Scope:**
*   Core network infrastructure (MSC, BSC, BTS) and associated software.
*   Mobile equipment: Cab Radios (for drivers) and Operational Radios (for staff).
*   Fixed equipment: Dispatcher terminals for Primary and Secondary Controllers.
*   Voice communication services (emergency, group, broadcast, point-to-point).
*   Dedicated shunting mode functionality.
*   Functional and location-dependent addressing services.
*   Data bearer service for external safety-critical applications (specifically ERTMS/ETCS).
*   System management and provisioning interfaces.

**Out-of-Scope:**
*   The design of the external ERTMS/ETCS train control application.
*   Physical track-side infrastructure construction (e.g., tower erection, trenching).
*   National legacy system migration planning (detailed strategy).
*   End-user device hardware manufacturing specifications.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **GSM-R** | Global System for Mobile Communications – Railway |
| **ERTMS/ETCS** | European Rail Traffic Management System / European Train Control System |
| **MSC** | Mobile Switching Centre |
| **BSC** | Base Station Controller |
| **BTS** | Base Transceiver Station |
| **REC** | Railway Emergency Call |
| **LAS** | Link Assurance Signal |
| **M** | Mandatory (as per TSI) |
| **TSI** | Technical Specification for Interoperability |
| **Cab Radio** | Mobile terminal installed in the train driver's cabin. |
| **Operational Radio** | Hand-portable or mobile terminal used by trackside staff. |

#### 1.4 References
*   EU Commission Regulation (EU) No 2019/776 on the technical specification for interoperability relating to the ‘control-command and signalling’ subsystems.
*   EIRENE System Requirements Specification (SRS) – UNISIG Subset-093.
*   GSM Phase 2+ Technical Specifications (ETSI).

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its users, and operating environment. Section 3 details the specific requirements, including functional, interface, performance, and design constraints.

### 2. Overall Description

#### 2.1 Product Perspective
The GSM-R system is a standalone but critically interconnected subsystem of the modern European railway ecosystem. It interfaces directly with the **ERTMS/ETCS** train control system as a secure data bearer. It serves as the primary communication layer replacing legacy analog radio systems and must integrate with national railway operational procedures and existing telecommunications backhaul networks.

#### 2.2 Product Functions (Summary)
1.  **High-Priority Emergency Calling:** Initiate, manage, and prioritize Railway Emergency Calls.
2.  **Voice Communication Services:** Facilitate point-to-point, group (VGCS), and broadcast (VBS) voice calls.
3.  **Shunting Operations:** Provide a dedicated mode with continuous Link Assurance Signal for safety during shunting.
4.  **Intelligent Addressing:** Enable calls based on functional number (e.g., "Driver of Train 12345") and location.
5.  **Data Bearer Service:** Provide a reliable, circuit-switched data path for safety-critical signaling data (ERTMS/ETCS).
6.  **System Management:** Configure, monitor, and provision network elements and subscribers.

#### 2.3 User Characteristics
| User Class | Expertise | Key Characteristics |
| :--- | :--- | :--- |
| **Train Driver** | Expert in train operation. Limited radio/IT training. | Uses a dedicated Cab Radio interface. Operates in a high-speed, high-stress environment. Requires simple, unambiguous controls, especially for emergencies. |
| **Primary Controller** | Expert in traffic management and procedures. | Uses a sophisticated dispatcher terminal. Manages multiple simultaneous communications. Requires fast call setup and clear group/broadcast capabilities. |
| **Secondary Controller / Signaller** | Trained in operational procedures. | Supports primary controller. May use a similar or slightly reduced terminal feature set. |
| **Operational Staff** (Shunter, Trackside) | Trained in safety procedures. | Uses portable Operational Radio. Often works in harsh environments. Requires robust device and simple operation (e.g., push-to-talk). |
| **Network Administrator** | Expert in GSM and IT systems. | Manages the core network. Requires advanced O&M interfaces. |

#### 2.4 Constraints
1.  **Regulatory & Compliance:** The entire system **must** comply with all Mandatory (M) requirements defined in the relevant Technical Specifications for Interoperability (TSIs).
2.  **Performance:** Call setup for Railway Emergency Calls must be ≤ 2 seconds in 95% of statistical cases.
3.  **Environmental:** Mobile network coverage must support reliable communication for trains traveling at speeds up to **500 km/h**.
4.  **Technical:** All radio equipment must operate exclusively within the designated GSM-R frequency bands (**876-880 MHz for uplink, 921-925 MHz for downlink**).
5.  **Safety:** The system is classified as safety-critical. Design must adhere to relevant CENELEC standards (e.g., EN 50126, EN 50128, EN 50129).

#### 2.5 Assumptions and Dependencies
*   Assumes the existence of adequate power and transmission infrastructure at base station sites.
*   Dependent on national radio spectrum regulators allocating and protecting the GSM-R bands.
*   The external ERTMS/ETCS system will provide data in the expected format and protocol.

### 3. Specific Requirements

#### 3.1 Functional Requirements

**3.1.1 Railway Emergency Call (REC)**
*   **FR-1.1:** The Cab Radio shall provide a single, dedicated, and physically protected button (e.g., guarded) to initiate a Railway Emergency Call.
*   **FR-1.2:** Upon REC initiation, the system shall pre-empt any ongoing call of lower priority on the involved mobile and network resources.
*   **FR-1.3:** The REC shall be established as a voice group call to the relevant controller group and all trains in the designated geographical area (emergency area).
*   **FR-1.4:** The call setup time (from button press to ringing indication at controller terminal) shall be less than 2 seconds, achieving a 95% statistical probability.
*   **FR-1.5:** The system shall provide a distinct and urgent audible and visual indication for incoming RECs at controller terminals.

**3.1.2 Voice Communication Services**
*   **FR-2.1:** The system shall support Voice Group Call Service (VGCS) allowing a user to speak to a predefined group of subscribers.
*   **FR-2.2:** The system shall support Voice Broadcast Service (VBS) allowing a user (typically a controller) to speak to all subscribers in a predefined area, with listen-only access for mobiles.
*   **FR-2.3:** The system shall support point-to-point voice calls between any two subscribers (mobile or fixed).
*   **FR-2.4:** The system shall implement a configurable call priority scheme (e.g., REC > Shunting Call > Operational Group Call > Point-to-Point Call).

**3.1.3 Shunting Mode**
*   **FR-3.1:** The Cab Radio and Operational Radio shall provide a user-selectable "Shunting Mode."
*   **FR-3.2:** In Shunting Mode, the radio shall establish a continuous, point-to-point link with the designated shunting manager and transmit a periodic Link Assurance Signal (LAS).
*   **FR-3.3:** If the link is lost or the LAS is interrupted for more than a configurable period (e.g., 2 seconds), the radio shall immediately provide a clear **audible and visual warning** to both the shunter and the manager.

**3.1.4 Functional Addressing**
*   **FR-4.1:** The system shall allow a user to place a call using a Functional Number (e.g., "Train 12345 Driver", "Signalman at KM 55.2") instead of a phone number.
*   **FR-4.2:** The network shall translate the Functional Number into the current Mobile Subscriber ISDN Number (MSISDN) of the target device based on a real-time mapping database.
*   **FR-4.3:** The mapping database shall be updated dynamically based on train numbering, scheduling, and location information.

**3.1.5 Data Bearer Service for ERTMS/ETCS**
*   **FR-5.1:** The system shall provide a circuit-switched data connection (up to 9.6 kbps) between the Cab Radio and the Radio Block Centre (RBC).
*   **FR-5.2:** This data connection shall be highly reliable, with a Bit Error Rate (BER) better than 10^-4.
*   **FR-5.3:** The system shall guarantee resources for this data connection, prioritizing it above non-safety-related data traffic.

#### 3.2 External Interface Requirements

**3.2.1 User Interfaces**
*   **UI-1 Cab Radio:** Physical push buttons for REC, shunting mode, volume control. A digital display for call status, functional number, and signal strength. Audio via loudspeaker/microphone.
*   **UI-2 Controller Terminal:** Graphical User Interface (GUI) with call control panels, group lists, geographical display of trains, and prominent REC alert panels.

**3.2.2 Hardware Interfaces**
*   **HW-1:** Cab Radio must interface with the train's external antenna and power supply (typically 110V DC).
*   **HW-2:** Cab Radio must have a standard serial (e.g., RS-422) or Ethernet interface for connection to the onboard ERTMS/ETCS European Vital Computer (EVC).

**3.2.3 Communication Interfaces**
*   **CI-1:** Air interface compliant with GSM Phase 2+ in the 900 MHz GSM-R band.
*   **CI-2:** Core network interfaces (e.g., A-interface between BSC and MSC) compliant with GSM standards.
*   **CI-3:** SS7 signaling network interface for interconnection with Public Switched Telephone Networks (PSTN) where required.

#### 3.3 Performance Requirements
*   **PR-1:** The network shall maintain a call drop rate of < 2% for high-speed (up to 500 km/h) mobile scenarios.
*   **PR-2:** Handover execution time between adjacent cells shall be less than 300ms to maintain service continuity at very high speed.
*   **PR-3:** The system shall support a minimum traffic capacity of 50,000 subscribers per network with defined call busy hour profiles.
*   **PR-4:** End-to-end voice transmission delay shall not exceed 150ms.

#### 3.4 Design Constraints
*   **DC-1:** All software for safety-related functions (e.g., REC handling, Shunting Mode, ETCS data bearer) shall be developed to SIL 2 or higher as per EN 50128.
*   **DC-2:** System architecture shall be redundant at critical points (MSC, BSC, transmission links) to achieve 99.99% annual availability.
*   **DC-3:** Mobile device software shall be stored in non-volatile memory and be resistant to corruption from power cycles.

#### 3.5 Safety and Security Requirements
*   **SSR-1:** Unauthorized access to network management functions shall be prevented via authentication and role-based access control.
*   **SSR-2:** The system shall protect against eavesdropping on safety-critical communications (e.g., REC, shunting).
*   **SSR-3:** The system shall implement measures to prevent fraudulent use of the network (e.g., cloned terminals).

#### 3.6 Compliance Requirements
*   **CR-1:** The final system shall be accompanied by a formal declaration of verification against all applicable Mandatory (M) TSI requirements.
*   **CR-2:** All mobile and fixed equipment shall carry the EC declaration of conformity and the CE marking.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Manager | | | |
| Lead System Architect | | | |
| Quality Assurance | | | |
| Client Representative | | | |