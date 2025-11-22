Of course. Below is a comprehensive Software Requirements Specification (SRS) document for the EIRENE system, structured according to professional standards (IEEE Std 830-1998) and formatted in Markdown.

***

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

---

## 1. Introduction

### 1.1 Purpose
This document provides a detailed Software Requirements Specification (SRS) for the EIRENE (European Integrated Railway Radio Enhanced Network) system. It describes the functional and non-functional requirements necessary to deliver a standardized, interoperable GSM-R based digital radio network for European railways. This SRS is intended for system architects, developers, testers, and project managers involved in the implementation and validation of the EIRENE system.

### 1.2 Scope
The EIRENE system is a core network infrastructure that enables secure, reliable, and interoperable voice and data communications across national borders for European railway operations. It supports critical applications including operational communications, railway emergency calls, and data exchange for train control systems (ERTMS/ETCS).

**In-Scope:**
*   GSM-R core network and base station subsystems.
*   Call management and control functions (voice and data).
*   Functional and location-dependent addressing services.
*   Interfaces with ERTMS/ETCS, controller equipment, and other train-borne systems.
*   Management of call priorities and shunting operations.

**Out-of-Scope:**
*   Design and manufacture of end-user terminals (e.g., cab radios, operational radios).
*   Public communications services for non-railway purposes.

### 1.3 Definitions, Acronyms, and Abbreviations
| Acronym | Definition |
| :--- | :--- |
| **EIRENE** | European Integrated Railway Radio Enhanced Network |
| **GSM-R** | Global System for Mobile Communications – Railway |
| **UIC** | International Union of Railways |
| **ERTMS** | European Rail Traffic Management System |
| **ETCS** | European Train Control System |
| **FRS** | Functional Requirements Specification |
| **SRS** | Software Requirements Specification |
| **LAS** | Link Assurance Signal |

### 1.4 References
*   UIC Fiche 751-3: "Specifications for an International Radio System for the Railways"
*   EIRENE Functional Requirements Specification (FRS)
*   IEEE Std 830-1998: IEEE Recommended Practice for Software Requirements Specifications

### 1.5 Overview
This document is structured in three main sections: Introduction, Overall Description, and Specific Requirements. The Specific Requirements section details the external interfaces, functional capabilities, and performance criteria that the system must satisfy.

## 2. Overall Description

### 2.1 Product Perspective
The EIRENE system is a cornerstone of the European Railway Traffic Management System (ERTMS). It is designed to replace disparate national analog radio systems to achieve seamless cross-border interoperability for high-speed and conventional rail traffic. It operates as a closed, railway-dedicated network that interfaces with critical safety and operational systems.

### 2.2 Product Functions
The core functions of the EIRENE system include:
*   **Railway Emergency Calls:** High-priority voice calls initiated in both train-running and shunting modes.
*   **Functional Addressing:** Dynamic mapping of calls to a user based on their current role (e.g., "Driver of Train 1234").
*   **Location-Dependent Addressing:** Routing calls to the correct controller based on the train's geographical location.
*   **Shunting Mode:** A dedicated operational mode with a Link Assurance Signal (LAS) to confirm continuous radio communication.
*   **Multi-Driver Communications:** Enabling communication between multiple drivers within the same train consist.
*   **Priority-Based Call Handling:** Management of five distinct call priority levels, with pre-emption capabilities.
*   **Voice Group and Broadcast Calls:** One-to-many voice communication for operational coordination.
*   **Direct Mode Operation (DMO):** Local, set-to-set communication independent of the network infrastructure.

### 2.3 User Characteristics
| User Role | Description | Primary Use Case |
| :--- | :--- | :--- |
| **Train Driver** | Operates the train; uses a Cab Radio. | Emergency calls, receiving movement authorities, operational communication with controllers. |
| **Controller (Primary/Secondary)** | Manages train traffic in a control center. | Issuing movement authorities, coordinating train paths, handling emergencies. |
| **Shunting Team** | Personnel involved in shunting maneuvers. | Local coordination using shunting mode and DMO. |
| **Operational Staff** | Maintenance and trackside staff. | Coordinating maintenance activities and line-side operations. |
| **General Staff** | Other railway employees. | General administrative and logistical communications. |

### 2.4 Constraints
*   The system **must** achieve mandatory interoperability for international rail traffic.
*   Functional addressing **must** be implemented consistently across all national network segments.
*   Integration with the ERTMS/ETCS Level 2 and 3 train control systems is **required**.
*   The shunting mode with Link Assurance Signal is a **mandatory** feature.
*   The system **must** support all five defined priority levels for call handling.

### 2.5 Assumptions and Dependencies
*   It is assumed that a GSM-R license and frequency spectrum are available in all operational territories.
*   The system's performance is dependent on the underlying GSM-R infrastructure and its deployment coverage.
*   Successful operation assumes that external systems (e.g., ERTMS/ETCS) provide data via the defined standardized interfaces.

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 Hardware Interfaces
*   **HWI-001:** The system shall interface with GSM-R Base Transceiver Stations (BTS).
*   **HWI-002:** The system shall interface with railway controller workstations and consoles.
*   **HWI-003:** The system shall provide a data interface to train-borne systems, including the Driver Safety Device and the On-Board Recorder.

#### 3.1.2 Software Interfaces
*   **SWI-001:** The system shall interface with the ERTMS/ETCS Radio Block Centre (RBC) for the exchange of train control messages.
*   **SWI-002:** The system shall provide standardized data interfaces (e.g., APIs) for external railway applications.
*   **SWI-003:** The system shall support a gateway interface to public networks (e.g., PSTN/ISDN) for authorized calls.

#### 3.1.3 Communications Interfaces
*   **CI-001:** The system shall operate on the standardized GSM-R frequency bands as defined by the UIC.
*   **CI-002:** The system shall support all mandatory GSM-R protocols for voice and data services.

### 3.2 Functional Requirements

#### 3.2.1 Call Management
*   **FUNC-001:** The system shall establish a Railway Emergency Call with a priority that pre-empts all other ongoing calls.
    *   *Priority: Mandatory*
*   **FUNC-002:** The system shall support Functional Addressing, allowing a call to be placed to a role (e.g., "Driver of Train XYZ") rather than a physical device.
    *   *Priority: Mandatory*
*   **FUNC-003:** The system shall implement Location-Dependent Addressing to route a driver's call to the correct line controller based on the train's current position.
    *   *Priority: Mandatory*
*   **FUNC-004:** The system shall manage five distinct call priority levels (e.g., Emergency, High, Normal, Low).
    *   *Priority: Mandatory*
*   **FUNC-005:** The system shall allow authorized users to initiate Voice Group Calls and Broadcast Calls to predefined groups.
    *   *Priority: High*

#### 3.2.2 Shunting Operations
*   **FUNC-006:** The system shall provide a dedicated "Shunting Mode" for users involved in shunting activities.
    *   *Priority: Mandatory*
*   **FUNC-007:** In Shunting Mode, the system shall generate a periodic Link Assurance Signal (LAS) to provide audible confirmation of an active radio link.
    *   *Priority: Mandatory*

#### 3.2.3 Direct Mode Operation
*   **FUNC-008:** The system shall support Direct Mode Operation (DMO), allowing terminals to communicate directly when outside network coverage.
    *   *Priority: High*

### 3.3 Non-Functional Requirements

#### 3.3.1 Performance Requirements
*   **PERF-001:** The call set-up time for a Railway Emergency Call shall be less than 2 seconds (95th percentile).
    *   *Priority: Mandatory*
*   **PERF-002:** The call set-up time for a Group Call between drivers shall be less than 5 seconds (95th percentile).
    *   *Priority: High*
*   **PERF-003:** The system shall maintain radio coverage over 95% of the designated railway operational area for 95% of the time.
    *   *Priority: Mandatory*
*   **PERF-004:** The system shall maintain all communication services for trains traveling at speeds up to 500 km/h.
    *   *Priority: High*
*   **PERF-005:** 95% of all calls shall be established within their respective required set-up times; 99% of calls shall be established within 1.5 times the required set-up time.
    *   *Priority: High*

#### 3.3.2 Reliability & Availability
*   **RELY-001:** The core network subsystems shall achieve an availability of 99.999% (Five Nines).
    *   *Priority: High*

#### 3.3.3 Safety & Security
*   **SEC-001:** The system shall implement authentication mechanisms to prevent unauthorized network access.
    *   *Priority: Mandatory*
*   **SEC-002:** The system shall ensure the integrity and confidentiality of data communications with the ERTMS/ETCS system.
    *   *Priority: Mandatory*

#### 3.3.4 Operational Requirements
*   **OPER-001:** End-user terminals (outside the scope of this SRS but dependent on the network) shall have a minimum battery life of 8 hours under a standard usage profile (20% talk time, 60% group call reception, 20% standby).
    *   *Priority: High*

---
**Document Approval:**

| Name | Role | Signature | Date |
| :--- | :--- | :--- | :--- |
| | Project Manager | | |
| | Lead System Architect | | |
| | Quality Assurance Manager | | |
***