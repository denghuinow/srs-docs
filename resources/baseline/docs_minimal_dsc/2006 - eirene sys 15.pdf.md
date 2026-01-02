# Software Requirements Specification (SRS)
## European Railway GSM-R Interoperability System

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for a digital radio communication system based on the GSM standard, specifically engineered for European railway operations. The primary purpose is to establish a unified specification ensuring seamless mobile communications interoperability across national borders for railway infrastructure and rolling stock. This document serves as the authoritative source for system developers, network engineers, procurement agencies, and validators.

#### 1.2 Scope
The system, herein referred to as the GSM-R Interoperability System, encompasses:

*   **In Scope:**
    *   Ground-to-train voice and data communication services.
    *   Mobile communication services for all operational railway personnel (trackside, station, depot, administrative).
    *   Definition of mandatory GSM services adapted for railway operational needs.
    *   Specification of railway-specific supplementary services.
    *   Network and subscriber equipment requirements for cross-border interoperability.
    *   Performance and coverage criteria for voice, data, and associated train control services.

*   **Out of Scope:**
    *   The design of specific hardware components (e.g., radio unit circuit boards).
    *   National railway operational procedures not affecting radio communication protocols.
    *   Non-GSM-R communication systems used by railways (e.g., legacy analog, public cellular networks for non-operational use).

#### 1.3 Definitions, Acronyms, and Abbreviations

| Term | Definition |
| :--- | :--- |
| **GSM-R** | Global System for Mobile Communications – Railway |
| **EIRENE** | European Integrated Railway Radio Enhanced Network |
| **SRS** | System Requirements Specification |
| **VGCS** | Voice Group Call Service |
| **VBS** | Voice Broadcast Service |
| **ETCS** | European Train Control System |
| **R-GSM** | Railway GSM frequency band |
| **Cab Radio** | Fixed mobile terminal installed in a train driver's cabin |
| **Functional Addressing** | Addressing a user by their role (e.g., "Driver of Train XYZ") |
| **Location-Dependent Addressing** | Routing a call based on the geographical location of the caller or callee |

#### 1.4 References
1.  EIRENE System Requirements Specification (SRS), Version 16.
2.  ETSI EN 301 515: "Global System for Mobile communication (GSM); Requirements for GSM operation on railways".
3.  UIC Project EIRENE – Functional Requirements Specification (FRS).

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the system, its users, and operating environment. Section 3 details the specific functional and non-functional requirements, which form the core of this specification.

### 2. Overall Description

#### 2.1 Product Perspective
The GSM-R system is a critical, safety-relevant component of modern European railway infrastructure. It interfaces with:
*   **Users:** Via Cab Radios, General Purpose Radios, and dispatcher consoles.
*   **External Systems:** Primarily the European Train Control System (ETCS) for data transmission related to signaling and train control.
*   **Legacy Systems:** May need to coexist with or phase out existing national railway radio systems.

It is a standalone mobile network but must be interoperable with other GSM-R networks operated by neighboring national railway infrastructures.

#### 2.2 User Classes and Characteristics
| User Class | Device | Key Characteristics & Requirements |
| :--- | :--- | :--- |
| **Train Driver** | Cab Radio (Fixed Mobile Terminal) | Requires hands-free, high-reliability operation. Must initiate/receive high-priority emergency calls, group calls with controllers, and use functional numbers. |
| **Railway Controller / Signaller** | Dispatcher Console (Fixed Terminal) | Manages voice group calls, broadcasts, and individual calls to multiple drivers/staff. Requires call pre-emption and priority management capabilities. |
| **Operational Staff** | General Purpose / Operational Radio (Portable) | Includes shunting teams, maintenance workers, and station staff. Requires group communication within a local area, point-to-point calls, and emergency functionality. |

#### 2.3 Operating Environment
*   **Physical Environment:** The system must operate reliably in extreme environmental conditions typical of European railways, including tunnels, deep cuttings, urban canyons, remote rural areas, and major railway stations.
*   **Technical Environment:** The core network shall be based on GSM Phase 2+ standards. Mobile stations shall operate in the R-GSM frequency band.

#### 2.4 Design and Implementation Constraints
1.  **Regulatory & Standards Constraint:** The entire system shall comply with the mandatory GSM services and protocols as specified in the **EIRENE SRS** to guarantee European interoperability.
2.  **Regulatory & Physical Constraint:** The system **must** operate within the designated **Railway-GSM (R-GSM) frequency band**:
    *   Mobile Station (Train, Portable) Transmit: **876 – 915 MHz**
    *   Base Station (Network) Transmit: **921 – 960 MHz**
3.  **Performance Constraint:** Network coverage and field strength must meet or exceed the minimum levels defined for:
    *   Voice Services (as per EIRENE QoS specifications)
    *   Data Services (for ETCS and other applications)
    *   Specifically along the track, in stations, and in depots.

#### 2.5 Assumptions and Dependencies
*   It is assumed that national railway infrastructure managers will procure and deploy network elements compliant with this SRS.
*   The system's ability to support ETCS Level 2 & 3 is dependent on the guaranteed performance of the underlying data services (GPRS/CSD).

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Mandatory GSM Voice Services
*   **FR-001: Telephony Service**
    *   **Description:** The system shall provide full-duplex, circuit-switched point-to-point voice calls between any two subscribers on the GSM-R network.
    *   **Priority:** Mandatory

*   **FR-002: Voice Group Call Service (VGCS)**
    *   **Description:** The system shall support half-duplex voice calls where one speaker addresses a predefined group of subscribers in a "push-to-talk" manner. Listeners shall be able to join an ongoing group call.
    *   **Priority:** Mandatory

*   **FR-003: Voice Broadcast Service (VBS)**
    *   **Description:** The system shall support half-duplex voice calls where one speaker (typically a controller) addresses a predefined group of subscribers in a broadcast (listen-only) mode.
    *   **Priority:** Mandatory

##### 3.1.2 Railway-Specific Supplementary Services
*   **FR-010: Functional Addressing**
    *   **Description:** The system shall allow a user to be called using a number that represents their current functional role (e.g., "Driver of Train 1234") rather than a personal ID. The mapping between functional number and physical MSISDN shall be managed by the network.
    *   **Priority:** High

*   **FR-011: Location-Dependent Addressing**
    *   **Description:** When a user makes a call to a short number (e.g., "0" for local controller), the system shall route the call to the appropriate geographical controller based on the caller's current location.
    *   **Priority:** High

*   **FR-012: High-Priority Railway Emergency Call**
    *   **Description:** The system shall provide a mechanism for any user (especially drivers) to initiate an emergency call with the highest possible priority. This call shall pre-empt any other ongoing calls on the relevant channel and be immediately presented to the appropriate controller.
    *   **Inputs:** Emergency button press or dedicated emergency number dial.
    *   **Priority:** Highest

##### 3.1.3 Interoperability Services
*   **FR-020: Cross-Border Communication**
    *   **Description:** A train or staff member crossing from a GSM-R network in Country A to a GSM-R network in Country B shall maintain the ability to use all mandatory and railway-specific services without manual intervention. This includes seamless authentication, registration, and service continuity for group calls where applicable.
    *   **Priority:** Mandatory

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance Requirements
*   **NFR-001: Call Setup Time**
    *   **Description:** The call setup time for a point-to-point railway emergency call shall not exceed 1.5 seconds (95th percentile) under normal network load.
*   **NFR-002: Coverage Field Strength**
    *   **Description:** The minimum received field strength for reliable voice and ETCS data services shall be **≥ 41 dBµV/m** (95% time and place probability) along the track. Specific values for tunnels and stations are defined in the referenced EIRENE SRS.
*   **NFR-003: System Availability**
    *   **Description:** The core network infrastructure shall achieve an availability of 99.95% or higher.

##### 3.2.2 Safety & Security Requirements
*   **NFR-010: Secure Authentication**
    *   **Description:** The system shall authenticate all mobile terminals (Cab Radios, portables) using GSM authentication algorithms (A3/A8) and railway-specific key management to prevent unauthorized network access.
*   **NFR-011: Call Integrity & Priority**
    *   **Description:** The system shall guarantee that a high-priority emergency call cannot be dropped or interrupted by a lower-priority call. A pre-defined, non-modifiable call priority hierarchy shall be enforced.

##### 3.2.3 Compliance Requirements
*   **NFR-100: Standards Compliance**
    *   **Description:** All network and mobile equipment **must** demonstrate compliance with the mandatory services and interfaces defined in the **EIRENE SRS**.
*   **NFR-101: Frequency Band Compliance**
    *   **Description:** All radio transmission equipment **must** operate exclusively within the R-GSM band (876-915 MHz uplink, 921-960 MHz downlink) and comply with national and European radio spectrum regulations.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Systems Engineer | | | |
| Quality Assurance | | | |