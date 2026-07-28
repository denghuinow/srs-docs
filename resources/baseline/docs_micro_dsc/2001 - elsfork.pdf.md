# Software Requirements Specification (SRS)
## Wind Turbine to SCADA Communication System (WTSCS)

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Wind Turbine to SCADA Communication System (WTSCS). The purpose of this system is to provide a standardized, reliable, and secure communication framework for data exchange between individual wind turbine controllers or entire wind farms and remote Supervisory Control and Data Acquisition (SCADA) systems. This document is intended for use by project managers, system architects, software developers, testers, and stakeholders.

#### 1.2 Scope
The WTSCS will be a software-based communication layer that facilitates bidirectional data transfer. It will be applicable to deployments ranging from a single wind turbine to large-scale wind power plants. The system will reside logically between the turbine/farm controller(s) and the remote SCADA system, handling protocol translation, data marshaling, and network communication.

**In-Scope:**
*   Definition of data models for operational data, commands, and system management.
*   Implementation of communication protocols and interfaces.
*   Management of data transmission priorities and timing.
*   Handling of communication faults and reconnection logic.
*   Security features for data integrity and access control.

**Out-of-Scope:**
*   The internal logic of the wind turbine controller.
*   The internal logic of the remote SCADA system (beyond its defined interface).
*   The physical network infrastructure (e.g., cabling, routers, firewalls), though requirements will be placed upon it.
*   The user interface of the SCADA system.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **SCADA** | Supervisory Control and Data Acquisition. |
| **WTSCS** | Wind Turbine to SCADA Communication System (this system). |
| **WTC** | Wind Turbine Controller. |
| **WPP** | Wind Power Plant (wind farm). |
| **Operational Data** | Real-time measurements (e.g., power output, wind speed, temperature) and status information. |
| **Time-Critical Data** | Data where the total time from generation at the source to processing at the destination must not exceed a specified limit (0.5 seconds). |
| **Open Standard** | A publicly available, consensus-driven specification maintained by a recognized standards body (e.g., IEC, IEEE, OPC Foundation). |

#### 1.4 References
*   IEC 61400-25 Series: Communications for monitoring and control of wind power plants.
*   IEC 60870-5-104: Network access for telecontrol.
*   IEC 61850: Communication networks and systems for power utility automation.
*   OPC UA (Unified Architecture): Platform-independent service-oriented architecture.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details the specific requirements, including functional, interface, performance, and design constraints.

### 2. Overall Description

#### 2.1 Product Perspective
The WTSCS is a middleware component within the broader wind energy management ecosystem. It acts as a bridge, insulating the proprietary or vendor-specific interfaces of Wind Turbine Controllers (WTCs) from the SCADA system by providing a standardized, consistent interface.

**System Context Diagram:**
```
[Remote SCADA System] <---(Standardized Protocol)---> [WTSCS] <---(Adapted Protocol)---> [Wind Turbine Controller(s)]
         ^                                                          ^
         |                                                          |
    (Control Commands)                                      (Operational Data & Alarms)
```

#### 2.2 Product Functions
The core functions of the WTSCS are:
1.  **Data Acquisition & Reporting:** Periodically and/or on-change collection of operational data (measurements, statuses) and alarm/event notifications from WTCs and transmission to the SCADA system.
2.  **Command Execution:** Secure reception of control commands and setpoints from the SCADA system, validation, and reliable forwarding to the target WTC.
3.  **System Management:** Provision of services for remote configuration, software updates (of the WTSCS itself), and precise time synchronization across all connected devices.
4.  **Communication Management:** Establishment, maintenance, and recovery of communication sessions with both upstream (SCADA) and downstream (WTCs) systems.

#### 2.3 User Characteristics
The primary "users" of the WTSCS are other systems:
*   **SCADA System:** An automated client requiring high availability, low latency for commands, and a well-defined data model.
*   **Wind Turbine Controller:** A data server that may use various industrial protocols.
*   **System Administrator (Indirect User):** Configures the WTSCS, monitors its health, and performs updates via management interfaces.

#### 2.4 Constraints
1.  **Open Standards Constraint:** The system's external interfaces and internal data modeling shall be based on open, widely accepted international standards (e.g., OPC UA, IEC 61400-25).
2.  **Safety Constraint:** A fault or failure in the WTSCS communication link must not cause a hazardous malfunction or unsafe state in an individual wind turbine. The turbine must default to a safe, autonomous operational mode.
3.  **Performance Constraint:** The end-to-end transfer time for time-critical function data (e.g., emergency stop command, critical grid support setpoint) shall not exceed **500 milliseconds** under normal operating conditions.
4.  **Regulatory Constraint:** The system shall comply with relevant grid codes and cybersecurity regulations for critical energy infrastructure.

#### 2.5 Assumptions and Dependencies
*   It is assumed a stable IP-based network connection with sufficient bandwidth is available between all components.
*   The wind turbine controllers provide a minimum level of machine-readable data interface.
*   The SCADA system is capable of integrating with the standardized protocol chosen for the upstream interface.

### 3. Specific Requirements

#### 3.1 Functional Requirements

**3.1.1 Data Transfer from Wind Power Plant**
*   **FR-01:** The system shall acquire the following operational data from each configured WTC at a configurable sampling rate (1-60 seconds):
    *   Active power output (kW/MW)
    *   Wind speed (m/s)
    *   Rotor speed (RPM)
    *   Generator temperature (°C)
    *   Grid voltage and frequency
*   **FR-02:** The system shall acquire status information (e.g., running, stopped, faulted, service mode) from each WTC immediately upon change (event-driven).
*   **FR-03:** The system shall acquire alarm and event messages from each WTC with timestamp, severity, and description immediately upon generation.
*   **FR-04:** The system shall buffer acquired data locally to prevent loss during temporary communication outages with the SCADA system.

**3.1.2 Command Transfer to Wind Power Plant**
*   **FR-05:** The system shall receive and acknowledge the following control commands from the SCADA system:
    *   Start Turbine
    *   Stop Turbine (Normal)
    *   Emergency Stop (Time-Critical)
    *   Set Active Power Reference
    *   Set Reactive Power Reference
*   **FR-06:** The system shall validate all received commands for target availability and parameter limits before forwarding to the WTC.
*   **FR-07:** The system shall provide positive or negative acknowledgment for every command received from the SCADA, indicating success or failure at the WTSCS layer.

**3.1.3 System Management Functions**
*   **FR-08:** The system shall allow remote configuration of its communication parameters (IP addresses, polling intervals, data points) via a secure interface.
*   **FR-09:** The system shall support network time protocol (NTP) or equivalent to synchronize its internal clock and distribute time to downstream WTCs if supported.
*   **FR-10:** The system shall provide a health status interface, reporting on its own performance, communication link states, and error logs.

#### 3.2 Interface Requirements

**3.2.1 SCADA Interface (Upstream)**
*   **IR-01:** The upstream interface shall implement the **OPC UA** server specification (or **IEC 61400-25-4** MMS mapping) as the primary standardized interface.
*   **IR-02:** The data model exposed shall be structured according to the **IEC 61400-25-2** logical node classes.
*   **IR-03:** The interface shall support secure communication using encryption (TLS 1.2 or higher) and authentication.

**3.2.2 Wind Turbine Controller Interface (Downstream)**
*   **IR-04:** The system shall include protocol adapters for at least two common industrial protocols (e.g., Modbus TCP, IEC 60870-5-104, proprietary vendor protocol X).
*   **IR-05:** The downstream interface shall be configurable to define data point mappings between the WTC's native data addresses and the standardized IEC/OPC UA data model.

#### 3.3 Performance Requirements
*   **PR-01:** The end-to-end latency for **time-critical data** (as identified in FR-05: Emergency Stop) shall be ≤ **500 ms** (95th percentile).
*   **PR-02:** The system shall support concurrent communication with at least **100 wind turbines** from a single instance.
*   **PR-03:** For non-critical operational data, the system shall sustain a data refresh rate to the SCADA of up to **1-second intervals** without exceeding 70% CPU utilization on reference hardware.
*   **PR-04:** Upon recovery of a communication link, the system shall re-establish connections and resume normal data flow within **30 seconds**.

#### 3.4 Design Constraints
*   **DC-01:** The software shall be developed using a language and framework that supports deployment on both Windows and Linux platforms.
*   **DC-02:** The architecture shall be modular, allowing new protocol adapters (IR-04) to be added without modifying the core communication logic.
*   **DC-03:** The system shall have no single point of failure that would disrupt communication for all turbines. Redundancy options shall be design considerations.

#### 3.5 Safety & Reliability Requirements
*   **SR-01:** The system shall implement a watchdog mechanism to detect internal hangs and restart itself automatically.
*   **SR-02:** In case of loss of communication with the SCADA system, the WTSCS shall continue to acquire and buffer data from WTCs but shall **not** forward any pending control commands until the link is validated as restored. (Supports Key Constraint #2).
*   **SR-03:** The mean time between failures (MTBF) for the WTSCS software shall be greater than **10,000 hours**.

#### 3.6 Security Requirements
*   **SEC-01:** All external communication interfaces shall require authentication.
*   **SEC-02:** All data transmitted upstream to the SCADA shall be encrypted in transit.
*   **SEC-03:** The system shall support role-based access control (RBAC) for configuration and management functions, differentiating between operator and administrator roles.

---
*Document End*