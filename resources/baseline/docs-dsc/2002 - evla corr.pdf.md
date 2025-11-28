```markdown
# Software Requirements Specification (SRS)
# EVLA Correlator Monitor & Control System

**Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft  
**Authors:** [Your Name/Team]  

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
   3.3 [Performance Requirements](#33-performance-requirements)  
   3.4 [Design Constraints](#34-design-constraints)  
   3.5 [Software System Attributes](#35-software-system-attributes)  
   3.6 [Other Requirements](#36-other-requirements)  

4. [Appendices](#4-appendices)  
   4.1 [Major Risks and Undecided Issues](#41-major-risks-and-undecided-issues)  

---

## 1 Introduction

### 1.1 Purpose

This document provides a detailed description of the Software Requirements Specification (SRS) for the **EVLA Correlator Monitor & Control (M&C) System**. The system serves as the critical physical link between the WIDAR Correlator hardware and the EVLA monitor and control infrastructure. It is intended for stakeholders, developers, testers, and project managers to ensure a common understanding of the system's requirements, constraints, and functionality.

### 1.2 Scope

The EVLA Correlator M&C System is a software and hardware integration layer responsible for configuring, operating, and servicing the WIDAR Correlator within the Expanded Very Large Array (EVLA). The system translates high-level observational configurations into low-level hardware commands, facilitates real-time monitoring and control data transfer, ensures subsystem health, and performs limited real-time data processing. It is a mission-critical component, and its failure directly results in astronomical data loss.

### 1.3 Definitions, Acronyms, and Abbreviations

| Acronym/Term | Definition                                                                 |
|--------------|-----------------------------------------------------------------------------|
| **EVLA**     | Expanded Very Large Array                                                  |
| **M&C**      | Monitor & Control                                                          |
| **WIDAR**    | Wideband Interferometric Digital ARchitecture (Correlator type)            |
| **CPCC**     | Correlator Primary Control Computer (a key component of this system)       |
| **MVP**      | Minimum Viable Product                                                     |
| **SRS**      | Software Requirements Specification                                        |
| **TBD**      | To Be Determined                                                           |

### 1.4 References

*   EVLA Project Documentation
*   WIDAR Correlator Hardware Specifications
*   EVLA M&C System Interface Control Document (ICD)

### 1.5 Overview

The remainder of this SRS is structured as follows: Section 2 provides an overall description of the product, its context, and general capabilities. Section 3 details the specific technical, functional, and non-functional requirements. Appendices contain information on risks and unresolved issues.

## 2 Overall Description

### 2.1 Product Perspective

The EVLA Correlator M&C System is a subsystem within the larger EVLA instrumentation framework. It acts as a middleware bridge, isolating the high-level observatory control system from the complexities of the low-level WIDAR correlator hardware.

**System Context Diagram:**

```
+------------------------+     Configuration & Control     +-----------------------------+
|                        | <------------------------------> |                             |
|   EVLA M&C System      |                                  |   Correlator M&C System     |
|    (External System)   |                                  |      (This System)          |
|                        | <------------------------------> |                             |
+------------------------+     Monitor Data & Health        +-----------------------------+
                                                                       /|\
                                                                        |
                                                            +-----------|-----------+
                                                            |           |           |
                                                  +----------------+ +----------------+
                                                  | WIDAR Hardware | | Other Subsystems|
                                                  |  (Correlator)  | |   (e.g., CPCC)  |
                                                  +----------------+ +----------------+
```

### 2.2 Product Functions

The core functions of the system, derived from the MVP, are:

1.  **Configuration Translation:** Receive observational configuration parameters from the EVLA M&C system and translate them into specific, executable commands for the WIDAR correlator hardware.
2.  **Data Processing and Transfer:** Manage the bidirectional flow of dynamic control data (to the hardware) and monitor data (from the hardware).
3.  **Health Monitoring and Autonomous Correction:** Continuously monitor the status of the correlator and its computing subsystems. Automatically diagnose and attempt to correct detected hardware and software faults without human intervention where possible.
4.  **Real-time Data Probing:** Perform limited, real-time processing on data streams, such as computing and displaying auto-correlation products for diagnostic and verification purposes.

### 2.3 User Characteristics

The primary users of this system are:
*   **Astronomers/Operators:** Use the system to configure and initiate observations. They require a high-level, logical interface.
*   **Support Engineers:** Require detailed access to monitor data, system health, and fault logs for maintenance and debugging.
*   **System Administrators:** Responsible for the overall health of the computing infrastructure underlying the M&C system.

### 2.4 Constraints

1.  **Critical Availability:** The system is a critical component in the astronomical data path. Any unavailability directly leads to irretrievable data loss, mandating high reliability and fault tolerance.
2.  **Modular Design:** The system architecture must be modular to facilitate rapid fault detection, isolation, and repair. Components must be able to fail and be restarted/replaced without bringing down the entire system.
3.  **User Interface Coherence:** The system must provide a unified and coherent user interface that integrates all monitor and control data, presenting it logically to the user regardless of the underlying modular complexity.

### 2.5 Assumptions and Dependencies

*   The EVLA M&C system will provide configuration data in a predefined, stable format.
*   The WIDAR correlator hardware interfaces and protocols are well-defined and stable.
*   The underlying computing and network infrastructure is reliable and provides sufficient bandwidth and low latency.

## 3 Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 User Interfaces
*   **GUI:** A graphical user interface for operators and engineers to monitor system status, view data products (e.g., auto-correlation plots), and initiate manual control actions.
*   **CLI:** A command-line interface for administrative tasks and scripted operations.

#### 3.1.2 Hardware Interfaces
*   The system shall interface with the WIDAR correlator hardware boards and supporting electronics via specified communication protocols (e.g., Ethernet, custom serial, or PCIe).
*   The system shall interface with sensors for monitoring hardware health (e.g., temperature, voltage).

#### 3.1.3 Software Interfaces
*   **EVLA M&C System:** The system shall implement a defined API (e.g., CORBA, XML-RPC, or a custom TCP protocol) for receiving configuration and sending status/monitor data.
*   **Data Archive:** The system shall interface with the EVLA data archive to log specific monitor points and fault records.

#### 3.1.4 Communications Interfaces
*   The system shall communicate over the observatory's local area network using standard IP protocols.

### 3.2 Functional Requirements

#### **FR-1: Configuration Management**
*   **FR-1.1:** The system shall receive a complete observation configuration block from the EVLA M&C system.
*   **FR-1.2:** The system shall validate the received configuration for syntactic and semantic correctness.
*   **FR-1.3:** The system shall translate the validated high-level configuration into a sequence of low-level hardware register writes and commands for the WIDAR correlator.
*   **FR-1.4:** The system shall confirm the successful application of the hardware configuration back to the EVLA M&C system.

#### **FR-2: Data Processing and Transfer**
*   **FR-2.1:** The system shall process and send dynamic control data (e.g., phase switches, gain adjustments) to the correlator hardware during an observation.
*   **FR-2.2:** The system shall read, packetize, and transfer monitor data (e.g., power levels, system voltages) from the hardware to the EVLA M&C system at a specified rate.
*   **FR-2.3:** The system shall buffer data to handle transient network or processing delays.

#### **FR-3: Health Monitoring and Fault Management**
*   **FR-3.1:** The system shall continuously monitor the state of all correlator hardware components and the M&C software processes.
*   **FR-3.2:** The system shall compare monitor points against predefined thresholds to detect faults.
*   **FR-3.3:** Upon detecting a fault, the system shall log the event with a timestamp and severity.
*   **FR-3.4:** The system shall attempt autonomous corrective actions for predefined, recoverable faults (e.g., restarting a software process, resetting a board).
*   **FR-3.5:** The system shall escalate unrecoverable faults to the EVLA M&C system and alert operators.

#### **FR-4: Real-time Data Processing**
*   **FR-4.1:** The system shall have the capability to tap into the correlator data stream.
*   **FR-4.2:** The system shall compute auto-correlation spectra from a selected subset of data in real-time.
*   **FR-4.3:** The system shall display the computed auto-correlation products via the GUI for quick-look analysis.

### 3.3 Performance Requirements

*   **PR-1:** The system shall apply a new correlator configuration within `X` seconds of receipt (TBD based on operational needs).
*   **PR-2:** The latency for transferring critical monitor data from hardware to the M&C system shall be less than `Y` milliseconds.
*   **PR-3:** The system shall be available for `99.9%` of scheduled observing time.
*   **PR-4:** The system must be able to process and display auto-correlation products with a latency of less than `Z` seconds from the time the data is generated.

### 3.4 Design Constraints

*   The software shall be developed in `[Programming Language, e.g., C++, Python, Java]`.
*   The system shall use a modular, service-oriented architecture (SOA) or a microservices architecture.
*   The system shall run on the `[Specified OS, e.g., RHEL]` operating system.

### 3.5 Software System Attributes

#### **Reliability**
*   The system shall implement watchdog processes to detect and recover from hung software components.
*   The system shall have a mean time between failures (MTBF) of no less than `[TBD]` hours.

#### **Availability**
*   The system must meet the `99.9%` availability requirement as stated in PR-3. This will be achieved through redundancy, hot-swappable modules, and rapid fault recovery.

#### **Maintainability**
*   The system shall provide comprehensive logging for all significant actions and errors.
*   The system shall expose diagnostic interfaces for all modules to facilitate debugging.

#### **Portability**
*   While initially targeted for a specific OS, the system should be designed with abstraction layers to minimize the cost of porting to a new OS in the future.

### 3.6 Other Requirements

*   **Security:** The system shall implement access control mechanisms to prevent unauthorized configuration changes.
*   **Logging:** All system events, especially faults and configuration changes, shall be logged to a persistent store with millisecond timestamps.

## 4 Appendices

### 4.1 Major Risks and Undecided Issues

1.  **CPCC Hard Failure Escalation:** The actions to be taken by external systems (e.g., the main EVLA M&C system, telescope control) upon a complete, unrecoverable failure of the Correlator Primary Control Computer (CPCC) are **To Be Determined (TBD)**. This is a critical risk to system reliability and operational procedures.
2.  **Quantitative Performance Metrics:** Specific values for performance requirements (PR-1, PR-2, PR-4) need to be finalized based on detailed analysis of hardware capabilities and scientific requirements.
3.  **Detailed Hardware Interface Protocols:** The exact specifications for low-level communication with some WIDAR hardware components may require further elaboration.
```