# **EIRENE System Requirements Specification (SRS)**

**Document ID:** SRS-EIRENE-1.0
**Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

## **1. Introduction**

### **1.1 Purpose**
This document defines the comprehensive system requirements for the European Integrated Railway Radio Enhanced Network (EIRENE). It serves as the authoritative specification for vendors, system integrators, and railway administrations to design, implement, and deploy interoperable GSM-Railway (GSM-R) networks and mobile equipment across Europe.

### **1.2 Scope**
This SRS covers the requirements for a GSM-based digital mobile radio system tailored to the operational and safety-critical communications needs of European railways. The scope encompasses network infrastructure, mobile equipment, railway-specific services, and interoperability mechanisms necessary for cross-border operations.

**In-Scope Items:**
*   GSM-based core network and radio access network infrastructure.
*   Mobile Station (MS) equipment categories: Cab Radio, General Purpose Radio, Operational Radio.
*   Mandatory railway-specific supplementary services (e.g., Functional Addressing, Location Dependent Addressing, Railway Emergency Call).
*   Core GSM telephony and data services (e.g., voice calls, group calls, Short Message Service).
*   System-wide numbering plan and subscriber management for interoperability.
*   Environmental, mechanical, and electrical requirements for railway operational environments.

**Out-of-Scope Items:**
*   Handling of public emergency service calls (e.g., to "112").
*   Detailed design of national fixed telecommunication networks or interfaces to external public networks.
*   Specific hardware designs for controller/dispatcher workstations.
*   Definition of standard text messaging applications (left as optional national implementations).
*   Specification of Direct Mode Operation (DMO), defined as an optional feature.

### **1.3 Definitions, Acronyms, and Abbreviations**

| Term | Definition |
| :--- | :--- |
| **EIRENE** | European Integrated Railway Radio Enhanced Network |
| **GSM-R** | GSM for Railways |
| **MS** | Mobile Station |
| **Cab Radio** | Mobile equipment installed in a train driver's cab. |
| **REC** | Railway Emergency Call |
| **LDA** | Location Dependent Addressing |
| **FN** | Functional Number |
| **eMLPP** | enhanced Multi-Level Precedence and Pre-emption |
| **SMS** | Short Message Service |
| **VGCS** | Voice Group Call Service |
| **VBS** | Voice Broadcast Service |

### **1.4 References**
1.  GSM Technical Specifications (Series 01-12), ETSI.
2.  ITU-T Recommendation E.164: The international public telecommunication numbering plan.
3.  UIC Project EIRENE System Requirements Specification (Parent Document).
4.  Relevant European and national railway safety and operational regulations.

### **1.5 Document Overview**
This document is structured to present requirements in a logical sequence: overall system description, external interfaces, functional requirements (categorized by feature), non-functional requirements, and constraints.

## **2. Overall Description**

### **2.1 Product Perspective**
The EIRENE system is a specialized mobile communications subsystem integrated into the broader railway operational and control ecosystem. It interfaces with:
*   **External:** National railway control centers, signaling systems (for location data), and other GSM-R networks at borders.
*   **Users:** Railway operational staff (drivers, controllers, trackside workers).
*   **Environment:** Harsh railway operational environments (vibration, temperature extremes, electromagnetic interference).

### **2.2 Product Functions (Summary)**
The core functions of the EIRENE system are:
1.  **Safety-Critical Voice Communication:** Point-to-point and group calls with priority and pre-emption.
2.  **Railway-Specific Addressing:** Enabling calls to functions (e.g., "Train XYZ") or locations (e.g., "Signal 123") rather than physical devices.
3.  **Emergency Handling:** High-priority, widespread alerting via the Railway Emergency Call.
4.  **Operational Data Exchange:** Support for low-speed data services for operational applications.
5.  **Seamless Cross-Border Operation:** Automatic network registration and service continuity for trains crossing national borders.

### **2.3 User Characteristics**
| User Class | Characteristics / Skill Level |
| :--- | :--- |
| **Train Driver** | Professional operator; uses Cab Radio under high cognitive load; requires simple, intuitive interfaces for safety-critical functions. |
| **Controller/Traffic Manager** | Professional dispatcher; uses fixed or mobile terminal; manages multiple simultaneous communications; requires clear call management and presentation of caller context (e.g., location, function). |
| **Trackside Worker (Shunting/Maintenance)** | Field operative; uses ruggedized Operational Radio; often in groups; requires reliable group communication and direct mode capability. |
| **General Railway Staff** | Administrative or operational roles; uses General Purpose Radio; requires standard telephony and messaging features. |
| **System Administrator** | Technical staff; manages network and subscriber data; requires advanced configuration and diagnostic tools. |

### **2.4 Constraints**
1.  **Regulatory:** Must operate within the designated GSM-R frequency bands: **876-880 MHz (MS transmit)** and **921-925 MHz (Base Station transmit)**.
2.  **Technical:** Must maintain backward compatibility with the referenced baseline GSM standards (ETSI).
3.  **Environmental:** All mobile and trackside equipment must be designed to operate in ambient temperatures from **-20°C to +55°C** and withstand storage temperatures down to **-40°C**.
4.  **Operational:** Functional numbering schemes must be implementable within the structural limitations of the ITU-T E.164 numbering plan.
5.  **Performance:** Security procedures (authentication, ciphering) must be executed without causing call setup times to exceed the requirements defined in Section 3.6.

### **2.5 Assumptions and Dependencies**
*   It is assumed that national railway administrations will provide a location system (e.g., based on balises, GPS, or network cells) to enable Location Dependent Addressing (LDA).
*   System interoperability is dependent on all implementers adhering strictly to the mandatory requirements defined in this specification.
*   Successful cross-border operation depends on bilateral/multilateral agreements between network operators on roaming and handover.

## **3. Specific Requirements**

### **3.1 External Interface Requirements**
#### **3.1.1 User Interfaces**
*   **REQ-UI-001:** The Cab Radio shall provide a dedicated, physically protected, and prominently labeled button for initiating a Railway Emergency Call (REC).
*   **REQ-UI-002:** All radios shall provide clear visual and audible indications of call priority (e.g., REC incoming).
*   **REQ-UI-003:** The user interface shall allow selection of Functional Numbers (FN) from an on-board list or manual entry.

#### **3.1.2 Hardware Interfaces**
*   **REQ-HW-001:** The Cab Radio shall include interfaces for an external loudspeaker and microphone for hands-free operation in the driver's cab.
*   **REQ-HW-002:** Operational Radios shall include a Push-To-Talk (PTT) interface compatible with standard railway accessories.

#### **3.1.3 Communication Interfaces**
*   **REQ-COM-001:** The system shall implement the standard Um air interface as per GSM specifications in the defined railway frequency bands.
*   **REQ-COM-002:** The network shall support signaling interfaces (e.g., MAP, ISUP) for interconnection with other GSM-R networks at national borders.

### **3.2 Functional Requirements**

#### **3.2.1 Railway Emergency Call (REC)**
*   **REQ-FUNC-001:** A train driver shall be able to initiate a REC to all relevant controllers and trains in a specified area by pressing a single button.
*   **REQ-FUNC-002:** The REC shall be established using the highest priority level (eMLPP level 0) and shall pre-empt any ongoing lower-priority calls in the target cells.
*   **REQ-FUNC-003:** The network shall include the calling train's Functional Number and, if available, its location information in the REC setup signaling to the controller.
*   **REQ-FUNC-004:** An incoming REC shall provide a distinctive and urgent audible and visual alert on all recipient Cab Radios and controller terminals, overriding any other activity.

#### **3.2.2 Functional Addressing & Numbering**
*   **REQ-FUNC-010:** The system shall allow a user to place a call using a Functional Number (e.g., "Train 4502", "Station Master Basel").
*   **REQ-FUNC-011:** The network shall translate a dialed Functional Number to the current Mobile Subscriber ISDN Number (MSISDN) of the associated device before routing the call.
*   **REQ-FUNC-012:** The numbering plan shall be based on ITU-T E.164, with a dedicated country code for functional addressing.

#### **3.2.3 Location Dependent Addressing (LDA)**
*   **REQ-FUNC-020:** A train driver shall be able to initiate a call to the "responsible controller" for their current geographic location without knowing the controller's specific number.
*   **REQ-FUNC-021:** The Cab Radio or network shall use the train's current location (provided by an external system) to determine the correct destination number (e.g., a specific controller's FN) for an LDA call.

#### **3.2.4 Voice Group & Broadcast Calls**
*   **REQ-FUNC-030:** The system shall support Voice Group Call Service (VGCS) for communication within pre-defined groups (e.g., shunting team, maintenance group).
*   **REQ-FUNC-031:** The system shall support Voice Broadcast Service (VBS) where only the dispatcher can speak, and group members only listen (e.g., for announcements).
*   **REQ-FUNC-032:** Shunting mode shall utilize a specific VGCS group call, providing semi-duplex communication with fast call setup.

#### **3.2.5 Core GSM Services**
*   **REQ-FUNC-040:** The system shall provide full-duplex point-to-point telephony between any subscribers.
*   **REQ-FUNC-041:** The system shall support Short Message Service (SMS) for point-to-point alphanumeric messaging.
*   **REQ-FUNC-042:** The system shall support circuit-switched data services up to 9.6 kbps for operational applications.

### **3.3 Performance Requirements**
*   **REQ-PERF-001:** The call setup time for a Railway Emergency Call (REC) shall not exceed **2 seconds** under defined network load conditions (95th percentile).
*   **REQ-PERF-002:** The network shall provide coverage ensuring a **95% probability** that the received field strength exceeds the specified minimum level (e.g., -98 dBm for voice) along the track.
*   **REQ-PERF-003:** The handover success rate between cells shall be at least **99.5%** under design load conditions to ensure call continuity for high-speed trains.
*   **REQ-PERF-004:** The end-to-end transmission quality for voice calls shall meet a specified speech quality index (e.g., MOS >3.5) under nominal conditions.

### **3.4 System Attributes**

#### **3.4.1 Reliability & Availability**
*   **REQ-SYS-001:** The core network infrastructure shall achieve an availability of 99.95% or higher.
*   **REQ-SYS-002:** Mobile equipment (Cab Radio) shall have a Mean Time Between Failures (MTBF) of not less than 50,000 hours.

#### **3.4.2 Security**
*   **REQ-SYS-010:** The system shall authenticate all mobile stations attempting to register on the network.
*   **REQ-SYS-011:** The system shall support ciphering of signaling and user data over the air interface.
*   **REQ-SYS-012:** Access to management functions for Functional Number mapping shall be restricted to authorized administrators.

#### **3.4.3 Maintainability**
*   **REQ-SYS-020:** The system shall provide remote diagnostic and logging capabilities for network elements.
*   **REQ-SYS-021:** Software in mobile stations shall be upgradeable over-the-air (OTA) or via a physical interface.

### **3.5 Environmental & Physical Requirements**
*   **REQ-ENV-001:** Mobile equipment shall operate reliably in ambient temperatures from **-20°C to +55°C**.
*   **REQ-ENV-002:** Mobile equipment shall withstand vibrations and shocks consistent with relevant railway standards (e.g., EN 50155, EN 61373).
*   **REQ-ENV-003:** Equipment shall have a degree of protection against dust and water ingress of at least IP54 for trackside use and IP52 for cab installation.

### **3.6 Interoperability Requirements**
*   **REQ-INT-001:** A train registered in Network A shall be able to roam seamlessly into Network B and initiate/ receive all mandatory services (REC, FN, LDA, VGCS).
*   **REQ-INT-002:** All mandatory features defined in this SRS shall be implemented consistently by all vendors to ensure end-to-end functionality.

## **4. Appendices**

### **4.1 Undecided / TBD Issues**
The following items require further specification or are designated as optional:
1.  The detailed protocol and interface between the external location system and the network for LDA.
2.  National implementation rules for mapping alphanumeric train identifiers (e.g., "ICE 123") into the E.164-based Functional Numbering plan.
3.  Detailed network recovery procedures for scenarios where the Functional Number to MSISDN mapping database becomes corrupted or unavailable.
4.  Specific type-approval test suites for General Purpose and Operational Radios beyond the core GSM conformance tests.
5.  The implementation of directed network selection mechanisms to force a mobile station to prefer the home network.

### **4.2 Traceability Matrix**
(A table linking User Stories from the input to specific requirements in Section 3 would be maintained here.)

**Example:**
| User Story ID | Related Requirement IDs |
| :--- | :--- |
| 1 (Driver Emergency Call) | REQ-UI-001, REQ-FUNC-001, REQ-FUNC-002, REQ-PERF-001 |
| 4 (Location-Based Call) | REQ-FUNC-020, REQ-FUNC-021 |

---
*Document End*