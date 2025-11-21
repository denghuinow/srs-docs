Of course. As an expert in Software Requirements Specification (SRS) documents, I will generate a comprehensive and professional SRS for the ERTMS/ETCS system based on the provided information. The document will adhere to standard IEEE SRS structure, utilize markdown formatting, and maintain a high level of technical accuracy suitable for a safety-critical system.

***

# Software Requirements Specification (SRS)
## For the European Rail Traffic Management System / European Train Control System (ERTMS/ETCS) - On-Board Unit (OBU)

**Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft  
**Author:** [Your Name/Department]

---

### Table of Contents
1. [Introduction](#1-introduction)
    1.1 [Purpose](#11-purpose)
    1.2 [Scope](#12-scope)
    1.3 [Definitions, Acronyms, and Abbreviations](#13-definitions-acronyms-and-abbreviations)
    1.4 [References](#14-references)
2. [Overall Description](#2-overall-description)
    2.1 [Product Perspective](#21-product-perspective)
    2.2 [Product Functions](#22-product-functions)
    2.3 [User Characteristics](#23-user-characteristics)
    2.4 [Constraints](#24-constraints)
    2.5 [Assumptions and Dependencies](#25-assumptions-and-dependencies)
3. [System Features and Requirements](#3-system-features-and-requirements)
    3.1 [Driver Information Interface (DMI)](#31-driver-information-interface-dmi)
    3.2 [Train Movement Supervision](#32-train-movement-supervision)
    3.3 [High-Speed Performance](#33-high-speed-performance)
    3.4 [Specific Transmission Module (STM) Interface](#34-specific-transmission-module-stm-interface)
4. [External Interface Requirements](#4-external-interface-requirements)
    4.1 [User Interfaces](#41-user-interfaces)
    4.2 [Hardware Interfaces](#42-hardware-interfaces)
    4.3 [Communications Interfaces](#43-communications-interfaces)
5. [Non-Functional Requirements](#5-non-functional-requirements)
    5.1 [Safety Requirements](#51-safety-requirements)
    5.2 [Performance Requirements](#52-performance-requirements)
    5.3 [Technical Compliance & Compatibility](#53-technical-compliance--compatibility)

---

### 1. Introduction

#### 1.1 Purpose
This document describes the functional and non-functional requirements for the On-Board Unit (OBU) of the European Rail Traffic Management System (ERTMS) and its core component, the European Train Control System (ETCS). This SRS serves as a definitive specification for system architects, software developers, testers, and validators involved in the design, implementation, and certification of the ETCS trainborne equipment.

#### 1.2 Scope
This specification covers the software and integrated system requirements for the ETCS On-Board Unit. The system in scope is responsible for supervising train movements, providing critical safety information to the driver, and ensuring interoperability across European rail networks. The scope includes interfaces with national legacy systems via the Specific Transmission Module (STM). The underlying track-side infrastructure (RBC, Balises, etc.) and detailed mechanical designs are outside the primary scope of this document.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Acronym | Definition |
| :--- | :--- |
| **ERTMS** | European Rail Traffic Management System |
| **ETCS** | European Train Control System |
| **OBU** | On-Board Unit |
| **STM** | Specific Transmission Module |
| **DMI** | Driver Machine Interface |
| **RBC** | Radio Block Centre |
| **CCS TSI** | Control Command and Signalling Technical Specification for Interoperability |
| **M** | Mandatory (Requirement) |
| **SRS** | Software Requirements Specification |

#### 1.4 References
*   ERA/ERTMS/033281: System Requirements Specification (SUBSET-026)
*   Commission Regulation (EU) No 2016/919 of 27 May 2016 on the technical specification for interoperability relating to the ‘control-command and signalling’ subsystems

### 2. Overall Description

#### 2.1 Product Perspective
The ETCS OBU is a critical, safety-enhancing component within the broader ERTMS ecosystem. It interacts with external systems to form a complete train control solution. Key interactions include:
*   **Track-side Systems:** Receives movement authorities and line data via Eurobalises and GSM-R radio from the RBC.
*   **National Systems (via STM):** Interfaces with legacy national train control systems (e.g., LZB, TVM, etc.).
*   **Train Interface:** Receives inputs from tachometers, radar, and other train-borne sensors.
*   **Driver:** Presents information and receives inputs via the Driver Machine Interface (DMI).

#### 2.2 Product Functions
The high-level functions of the ETCS OBU are:
1.  **Supervision:** Continuously monitor and supervise train speed and movement authority.
2.  **Information Presentation:** Provide the driver with clear, unambiguous information for safe train operation.
3.  **Interoperability:** Seamlessly operate across national borders by interfacing with both ETCS and legacy national systems.
4.  **Enforcement:** Initiate automatic braking if the train exceeds its permitted movement authority or speed profile.

#### 2.3 User Characteristics
The primary user of the system is the **Train Driver**, who is expected to be a licensed professional trained in the operation of ETCS/ERTMS. The driver is not expected to have software engineering expertise but must be proficient in interpreting the DMI and responding to its alerts and commands.

#### 2.4 Constraints
1.  **Mandatory Requirements:** Any requirement in the CCS TSI marked as Mandatory (M) shall be implemented and respected in every ETCS application level without exception.
2.  **Backward Compatibility:** The ETCS OBU shall be compatible with all existing national train control systems explicitly listed in the latest version of the CCS TSI.
3.  **Default Value Handling:** If the on-board system has no valid, location-specific national system values (e.g., from an STM), it shall revert to a predefined set of safe default values.

#### 2.5 Assumptions and Dependencies
*   It is assumed that the track-side infrastructure (balises, radio) is installed, operational, and compliant with the relevant TSI.
*   The system's performance is dependent on the accuracy of inputs from train sensors (e.g., tachometer, radar).
*   The STM hardware and its proprietary software are provided and certified separately, and the ETCS OBU only requires a standardized interface to it.

### 3. System Features and Requirements

#### 3.1 Driver Information Interface (DMI)
**Description:** This feature encompasses all functionalities related to presenting information to the driver and receiving inputs.

| ID | Requirement |
| :--- | :--- |
| **DMI-001** | The system **shall** display the current permitted speed to the driver. |
| **DMI-002** | The system **shall** display the target speed and distance to the target point (e.g., end of movement authority). |
| **DMI-003** | The system **shall** provide a clear and unambiguous warning to the driver in case of an overspeed or approach to a movement authority limit. |
| **DMI-004** | The system **shall** display the current operating mode (e.g., Full Supervision, On-Sight, Shunting). |

#### 3.2 Train Movement Supervision
**Description:** This feature covers the core logic for supervising both mainline and shunting movements to ensure they remain within safe limits.

| ID | Requirement |
| :--- | :--- |
| **SUP-001** | The system **shall** continuously calculate a braking curve based on the train's characteristics, line data, and movement authority. |
| **SUP-002** | The system **shall** supervise the train's speed to ensure it does not exceed the permitted speed at any location. |
| **SUP-003** | The system **shall** supervise the train's movement to ensure it does not exceed its Movement Authority. |
| **SUP-004** | The system **shall** be capable of supervising shunting movements according to predefined shunting profiles. |
| **SUP-005** | If the train exceeds the supervised speed or distance, the system **shall** initiate a service or emergency brake application automatically. |

#### 3.3 High-Speed Performance
**Description:** This feature defines the performance requirements for high-speed rail operations.

| ID | Requirement |
| :--- | :--- |
| **PER-001** | The system **shall** be fully functional and maintain all safety and supervision functions at train speeds from 0 km/h up to and including 500 km/h. |
| **PER-002** | All system response times (e.g., for brake intervention, data processing) **shall** be calculated and validated to be effective at the maximum operational speed of 500 km/h. |

#### 3.4 Specific Transmission Module (STM) Interface
**Description:** This feature manages the interface with national legacy train control systems.

| ID | Requirement |
| :--- | :--- |
| **STM-001** | The ETCS OBU **shall** be capable of receiving and interpreting information from national train control systems via the STM interface. |
| **STM-002** | The system **shall** be able to seamlessly transition between ETCS and national system supervision where the infrastructure requires it. |
| **STM-003** | When operating via an STM, the system **shall** apply the national system's specific rules and speed profiles for train supervision. |

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   The Driver Machine Interface (DMI) shall be a graphical screen with dedicated keys, compliant with ERA/ERTMS/033281 (SUBSET-041).

#### 4.2 Hardware Interfaces
*   The system shall interface with **Juridical Recording Unit** for data logging.
*   The system shall interface with **Balise Transmission Module** for receiving track-side telegrams.
*   The system shall interface with **Euroradio** for GSM-R communication with the RBC.
*   The system shall interface with the **STM** hardware unit.

#### 4.3 Communications Interfaces
*   The communication with the RBC shall use the **ETCS Packet Radio** protocol over GSM-R, as defined in SUBSET-093.
*   The communication with balises shall use the **Eurobalise** transmission protocol, as defined in SUBSET-036.
*   The interface with the STM shall follow the standardized **STM Interface** specification.

### 5. Non-Functional Requirements

#### 5.1 Safety Requirements
*   The system shall be designed to meet Safety Integrity Level **SIL 4** as per the CENELEC EN 5012x standards (e.g., EN 50126, EN 50128, EN 50129).
*   The system architecture shall be fault-tolerant, with no single point of failure leading to a hazardous situation.

#### 5.2 Performance Requirements
*   The system shall process all incoming balise telegrams with a latency of less than 100ms.
*   The update rate for the calculation of the dynamic braking curve shall be sufficient to ensure safety at 500 km/h.

#### 5.3 Technical Compliance & Compatibility
*   The entire system shall be fully compliant with the latest version of the **CCS TSI**.
*   All mandatory (M) requirements defined in SUBSET-026 shall be implemented.

---
**Document Approval:**

| Name | Role | Signature | Date |
| :--- | :--- | :--- | :--- |
| | Project Manager | | |
| | Lead System Architect | | |
| | Quality Assurance | | |