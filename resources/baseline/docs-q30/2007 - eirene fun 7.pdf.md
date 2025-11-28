Of course. Below is a comprehensive Software Requirements Specification (SRS) document for the EIRENE system, structured according to professional standards (IEEE 830) and formatted in Markdown.

```markdown
# Software Requirements Specification (SRS) for the EIRENE System

**Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft

---

## Table of Contents

1. [Introduction](#1-introduction)
    1.1 [Purpose](#11-purpose)
    1.2 [Scope](#12-scope)
    1.3 [Definitions, Acronyms, and Abbreviations](#13-definitions-acronyms-and-abbreviations)
    1.4 [References](#14-references)
    1.5 [Overview](#15-overview)
2. [Overall Description](#2-overall-description)
    2.1 [Product Perspective](#21-product-perspective)
    2.2 [Product Functions](#22-product-functions)
    2.3 [User Characteristics](#23-user-characteristics)
    2.4 [Constraints](#24-constraints)
    2.5 [Assumptions and Dependencies](#25-assumptions-and-dependencies)
3. [Specific Requirements](#3-specific-requirements)
    3.1 [External Interface Requirements](#31-external-interface-requirements)
    3.2 [Functional Requirements](#32-functional-requirements)
    3.3 [Non-Functional Requirements](#33-non-functional-requirements)
    3.4 [System Attributes](#34-system-attributes)

---

## 1. Introduction

### 1.1 Purpose
This document provides a detailed description of the requirements for the **EIRENE (European Integrated Railway Radio Enhanced Network) System**. It specifies the functional and non-functional requirements necessary to deliver a standardized, interoperable GSM-R based digital radio network for European railways. This SRS is intended for system architects, developers, testers, and project managers involved in the implementation and validation of the EIRENE system.

### 1.2 Scope
The EIRENE system is a core network and service platform that enables interoperable voice and data communications for railway operational needs across national borders in Europe.

*   **In-Scope:**
    *   GSM-R based digital radio network infrastructure.
    *   Core voice services (e.g., emergency calls, group calls).
    *   Data communication services for train control applications (e.g., ERTMS/ETCS).
    *   Functional and location-dependent addressing.
    *   Call handling with multiple priority levels.
    *   Interfaces to train control systems and other railway subsystems.

*   **Out-of-Scope:**
    *   Design and manufacture of end-user terminals (e.g., cab radios, handheld radios).
    *   Provision of non-railway public communications services.

### 1.3 Definitions, Acronyms and Abbreviations

| Acronym | Definition |
| :--- | :--- |
| **EIRENE** | European Integrated Railway Radio Enhanced Network |
| **GSM-R** | Global System for Mobile Communications – Railway |
| **UIC** | International Union of Railways |
| **ERTMS** | European Rail Traffic Management System |
| **ETCS** | European Train Control System |
| **FRS** | Functional Requirements Specification |
| **SRS** | Software Requirements Specification |

### 1.4 References
*   UIC Fiche 751-3: "Specifications of the Radio Transmission System for the International Union of Railways (UIC)"
*   EIRENE Functional Requirements Specification (FRS)
*   ERTMS/ETCS System Requirements Specification

### 1.5 Overview
This document is structured in three main parts: Introduction, Overall Description, and Specific Requirements. The Specific Requirements section contains the detailed, verifiable requirements for the system.

## 2. Overall Description

### 2.1 Product Perspective
The EIRENE system is a key component of the modern European railway infrastructure. It is developed under the UIC Project EIRENE to replace disparate national radio systems, thereby enabling seamless international interoperability for high-speed and conventional rail traffic. It acts as the communication backbone, integrating directly with the ERTMS/ETCS train control system and serving as the foundation for future railway digital communications.

### 2.2 Product Functions
The core functions of the EIRENE system include:
*   **Railway Emergency Calling:** Initiation and management of high-priority emergency calls in both train-running and shunting operational modes.
*   **Functional Addressing:** Dynamic mapping of calls to a user based on their current role (e.g., "Driver of Train 1234") rather than a static phone number.
*   **Location-Dependent Addressing:** Routing of calls to the appropriate controller based on the geographical location of the train.
*   **Shunting Mode Operation:** A dedicated communication mode for shunting operations, including a mandatory link assurance signal.
*   **Multi-Driver Communication:** Support for communication between multiple drivers within the same train consist.
*   **Priority-Based Call Handling:** Management of call queues and pre-emption based on five distinct priority levels.
*   **Voice Group and Broadcast Calls:** Establishment and management of one-to-many voice communications.
*   **Direct Mode Operation (DMO):** Allowance for direct radio-to-radio communication without network infrastructure, for local operations.

### 2.3 User Characteristics
| User Role | Description | Primary Use Case |
| :--- | :--- | :--- |
| **Train Driver** | Operates the train; uses a Cab Radio. | Routine operations, receiving movement authorities, initiating emergency calls. |
| **Controller (Primary/Secondary)** | Manages train traffic in a control center. | Issuing commands, managing traffic flow, responding to emergencies. |
| **Power Supply Controller** | Manages electrical power for traction. | Coordinating power supply with train movements. |
| **Shunting Team** | Personnel involved in shunting maneuvers. | Local coordination using shunting mode and direct mode. |
| **Operational Staff** | Maintenance and infrastructure staff. | Coordinating track-side work and maintenance activities. |
| **General Staff** | Other railway employees. | General administrative and logistical communications. |

### 2.4 Constraints
*   The system **must** provide mandatory interoperability for international rail traffic.
*   Functional addressing **must** be implemented consistently across all national network segments.
*   Integration with the ERTMS/ETCS train control system is **mandatory**.
*   The shunting mode with a continuous link assurance signal is a **mandatory** feature.
*   The system **must** support all five defined priority levels for call handling.

### 2.5 Assumptions and Dependencies
*   It is assumed that national railway infrastructures will provide the necessary physical sites and backhaul connectivity for GSM-R base stations.
*   The system's performance is dependent on the availability and correct functioning of the underlying GSM-R radio access network.
*   Successful operation assumes that end-user terminals (radios) comply with the EIRENE terminal specifications.

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 Hardware Interfaces
*   **EIRENE-IF-001:** The system shall interface with ERTMS/ETCS onboard units for the transmission of train control data.
*   **EIRENE-IF-002:** The system shall interface with the Driver Safety Device to acknowledge safety-critical information.
*   **EIRENE-IF-003:** The system shall provide a data output interface to the Train-Borne Recorder for logging communication events.

#### 3.1.2 Software Interfaces
*   **EIRENE-IF-004:** The system shall provide standardized data interfaces (e.g., APIs) for external applications requiring railway operational data.
*   **EIRENE-IF-005:** The system shall interface with Public Switched Telephone Networks (PSTN) and Public Land Mobile Networks (PLMN) for calls to/from public networks, subject to security policies.

#### 3.1.3 Communications Interfaces
*   **EIRENE-IF-006:** The system shall operate on the standardized GSM-R frequency bands as defined in the EIRENE FRS.
*   **EIRENE-IF-007:** The system shall support all signaling protocols required for GSM-R operation (e.g., customized applications for mobile network enhanced logic - CAMEL).

### 3.2 Functional Requirements

#### 3.2.1 Call Management
*   **EIRENE-FUNC-001:** The system shall allow a user to initiate a Railway Emergency Call.
*   **EIRENE-FUNC-002:** The system shall establish a Railway Emergency Call with a higher priority than any other call type, pre-empting ongoing calls if necessary.
*   **EIRENE-FUNC-003:** The system shall set up a Railway Emergency Call to the appropriate controller in less than 2 seconds.
*   **EIRENE-FUNC-004:** The system shall support Functional Addressing, allowing a call to be placed to a functional number (e.g., "Driver of Train XYZ").
*   **EIRENE-FUNC-005:** The system shall resolve Location-Dependent Addressing, routing a call made to a generic "Dispatcher" number to the controller responsible for the caller's current geographical section.

#### 3.2.2 Shunting Mode
*   **EIRENE-FUNC-006:** The system shall provide a dedicated "Shunting Mode" operational state.
*   **EIRENE-FUNC-007:** In Shunting Mode, the system shall provide a continuous Link Assurance Signal to indicate that the communication link is active and of sufficient quality.

#### 3.2.3 Group Communication
*   **EIRENE-FUNC-008:** The system shall allow authorized users to establish Voice Group Calls to a pre-defined group of users.
*   **EIRENE-FUNC-009:** The system shall set up a Group Call between drivers in less than 5 seconds.
*   **EIRENE-FUNC-010:** The system shall support Voice Broadcast Calls (one-way communication to a group).

#### 3.2.4 Direct Mode
*   **EIRENE-FUNC-011:** The system shall support Direct Mode Operation (DMO), allowing terminals to communicate directly with each other when outside network coverage or for local coordination.

### 3.3 Non-Functional Requirements

#### 3.3.1 Performance Requirements
*   **EIRENE-PERF-001:** Railway Emergency Call set-up time shall be less than 2 seconds (95th percentile).
*   **EIRENE-PERF-002:** Group Call set-up time between drivers shall be less than 5 seconds (95th percentile).
*   **EIRENE-PERF-003:** 95% of all call set-ups shall be completed within their required maximum time; 99% shall be completed within 1.5 times the required maximum time.
*   **EIRENE-PERF-004:** The system shall maintain communication with trains traveling at speeds of up to 500 km/h.

#### 3.3.2 Reliability & Availability
*   **EIRENE-RELY-001:** The system shall achieve a radio coverage rate of ≥95% over ≥95% of the designated railway operational area.

#### 3.3.3 Usability
*   **EIRENE-USE-001:** The system's functional addressing shall be transparent to the user, who shall only need to know the functional role of the person they are calling.

### 3.4 System Attributes

#### 3.4.1 Security
*   **EIRENE-SEC-001:** The system shall implement authentication mechanisms to prevent unauthorized access to the network.
*   **EIRENE-SEC-002:** The system shall provide encryption for voice and data communications to ensure confidentiality.

#### 3.4.2 Portability
*   **EIRENE-PORT-001:** The system shall be designed to be deployable across different national railway networks without core functional modifications.

#### 3.4.3 Operational
*   **EIRENE-OPER-001:** End-user terminals (e.g., handheld radios) shall have a minimum battery life of 8 hours under a standard usage profile (20% talk time, 60% group call reception, 20% standby).
```