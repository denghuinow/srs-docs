# Software Requirements Specification (SRS)
## Standard Co-Emulation Modeling Interface (SCE-MI)

**Document Version:** 1.0  
**Date:** [Date of Generation]  
**Status:** Draft for Review  
**Authors:** SCE-API Consortium

---

### 1. Introduction

#### 1.1 Purpose
This document defines the Software Requirements Specification (SRS) for the Standard Co-Emulation Modeling Interface (SCE-MI). The purpose of SCE-MI is to provide a standardized, high-performance message-passing interface that enables transaction-level communication between untimed software models executing on a host workstation and structural hardware models (e.g., RTL netlists) executing on verification platforms such as hardware emulators. This specification aims to eliminate proprietary lock-in and foster an ecosystem of interoperable transactor models.

#### 1.2 Scope
The scope of this SRS encompasses the definition of:
*   The hardware-side interface, defined as HDL macros for Verilog and VHDL.
*   The software-side interface, defined as C++ and C APIs.
*   The message-passing semantics and channel establishment mechanisms.
*   The clock generation and reset control for the hardware Design Under Test (DUT).
*   The configuration and binding mechanisms.

**Out of Scope:**
*   Software-to-software communication.
*   Event-based simulation synchronization.
*   Debug, profiling, or control-plane features.
*   The internal implementation of the infrastructure on any specific verification platform.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **SCE-MI** | Standard Co-Emulation Modeling Interface. |
| **DUT** | Design Under Test. The hardware model (typically RTL) being verified. |
| **Transactor** | A hardware model (in HDL) that translates between transaction-level messages and cycle-accurate signal-level activity. |
| **Proxy** | A software model (in C/C++) that provides the transaction-level API to the software testbench and communicates with its paired hardware transactor. |
| **Message Port** | The endpoint of a unidirectional message channel, instantiated in HDL. |
| **Infrastructure Linker** | A tool provided by the EDA vendor that analyzes the hardware netlist, extracts SCE-MI parameters, and generates the configuration file. |
| **Service Loop** | The software-side mechanism that processes incoming messages and manages interface operations. |
| **RTL** | Register Transfer Level. |
| **SoC** | System-on-Chip. |
| **EDA** | Electronic Design Automation. |

#### 1.4 References
*   SCE-API Consortium Charter and Goals.
*   IEEE Std 1666-2011 (SystemC Language Reference Manual) – Informative.
*   Related proprietary emulator API documentation (for context).

#### 1.5 Document Overview
This SRS is structured to first provide an overall product perspective, followed by detailed specific requirements for the interface's external behavior, functionality, and constraints. It is intended for three primary audiences: End Users, Transactor Implementors, and SCE-MI Infrastructure Implementors.

### 2. Overall Description

#### 2.1 Product Perspective
SCE-MI is a component of the broader SCE-API standardization effort. It acts as the critical bridge layer between the software verification environment (testbench, scoreboard, stimulus generators) and the hardware verification platform. It is independent of, but designed to work seamlessly with, SystemC and major emulation systems.

#### 2.2 Product Functions
The core functions of the SCE-MI system are:
1.  **Channel Management:** Establish and manage high-performance, transaction-oriented message channels between software proxies and hardware transactors.
2.  **Data Marshaling:** Serialize complex, untimed software data structures into flat bit vectors for hardware transport, and deserialize received bit vectors back into software data structures.
3.  **Time Control:** Generate and control clock signals for the hardware DUT and provide a mechanism for global reset.
4.  **Time Freeze:** Allow a transactor to temporarily "freeze" the controlled clock domain(s) while it composes or decomposes a multi-cycle message, maintaining synchronization.
5.  **Service Provisioning:** Provide a service loop mechanism compatible with both single-threaded and multi-threaded (e.g., SystemC) software environments.
6.  **Dynamic Binding:** Enable software proxies to bind to specific hardware message ports using symbolic names.
7.  **Error Handling:** Report fatal errors and informational messages to the software environment through a consistent mechanism.
8.  **Dual Language API:** Expose its functionality through both an object-oriented C++ API and a procedural C API.

#### 2.3 User Characteristics
| User Role | Characteristics & Expectations |
| :--- | :--- |
| **End User (SoC Design/Verification Engineer)** | Integrates pre-built transactor/proxy pairs into their testbench. Primary concern is ease of use, performance, and reliability. Does not need deep knowledge of SCE-MI internals. |
| **Transactor Implementor (IP Developer)** | Creates reusable transactor and proxy models. Expert in the application domain (e.g., PCIe, Ethernet). Uses SCE-MI macros and APIs as a toolkit. Requires a clear, consistent, and powerful API. |
| **SCE-MI Infrastructure Implementor (EDA Tool Vendor)** | Implements the SCE-MI specification for a specific verification platform (emulator, FPGA prototype). Expert in low-level platform communication. Requires an unambiguous specification of macros, APIs, and expected behaviors. |

#### 2.4 Constraints
*   The hardware-side interface **must** be specified as empty HDL macros (templates) with well-defined ports and parameters. The infrastructure implementation is responsible for expanding these macros into functional logic.
*   The software-side interface **must** be provided in both C++ (primary) and C (secondary) forms.
*   The interface is designed for transaction-level, message-passing communication; it is not optimized for single-signal or cycle-by-cycle interaction.

#### 2.5 Assumptions and Dependencies
*   **Primary Use Case:** Bridging untimed (TLM) software models to cycle-accurate (RTL) hardware models.
*   **Dependencies:**
    1.  A compliant **Infrastructure Linker** is required to generate the necessary configuration file (`scemi_params.dat` or equivalent).
    2.  A verification platform (emulator) with a communication link to a host workstation.
    3.  A host workstation with a standard C/C++ compilation environment.

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 Hardware-Side Interface (HDL Macros)
*   **REQ-HW-001:** The interface shall provide Verilog (`scemi_`) and VHDL (`SCEMI_`) macro definitions for message ports.
*   **REQ-HW-002:** A message port macro shall define the necessary signals for message transfer (e.g., `data`, `valid`, `ready`, `size`).
*   **REQ-HW-003:** The interface shall provide a clock control macro (`scemi_clock_control`) to be instantiated in the top-level testbench to generate and manage DUT clocks.
*   **REQ-HW-004:** The interface shall provide a clock port macro (`scemi_clock_port`) to be instantiated in transactors that need to request a time freeze.
*   **REQ-HW-005:** All macros shall use parameters to configure port widths, clock domain associations, and instance identifiers.

##### 3.1.2 Software-Side Interface (C++/C API)
*   **REQ-SW-001:** A C++ API shall be provided, centered around classes such as `MessageInPortProxy`, `MessageOutPortProxy`, and `SceMi`.
*   **REQ-SW-002:** A C API shall be provided, offering functional equivalents to the primary C++ class methods (e.g., `scemi_global_bind`, `scemi_message_send`).
*   **REQ-SW-003:** The API shall include functions to initialize the SCE-MI infrastructure (`SceMi::Init`), start the service loop (`SceMi::ServiceLoop`), and shut down (`SceMi::Shutdown`).

##### 3.1.3 Parameter/Configuration Interface
*   **REQ-CFG-001:** The system shall be configured via a file (e.g., `scemi_params.dat`) generated by the Infrastructure Linker.
*   **REQ-CFG-002:** The configuration file shall describe all message ports, their types (input/output), bit widths, associated clock domains, and binding names.

#### 3.2 Functional Requirements

##### 3.2.1 Initialization and Binding
*   **REQ-FUN-001:** The software infrastructure shall be initialized by reading the configuration file.
*   **REQ-FUN-002:** The software proxy shall be able to bind to a hardware message port using a unique string name defined in the configuration file.
*   **REQ-FUN-003:** Binding shall be possible before starting the service loop.

##### 3.2.2 Message Passing
*   **REQ-FUN-010:** A software proxy shall be able to send a message to its bound hardware transactor. The call shall block until the message is accepted by the hardware interface or a timeout occurs.
*   **REQ-FUN-011:** A software proxy shall be able to check for and receive a message from its bound hardware transactor (non-blocking and blocking variants).
*   **REQ-FUN-012:** The infrastructure shall handle the serialization of a software message object into a bit vector for transmission.
*   **REQ-FUN-013:** The infrastructure shall handle the deserialization of a received bit vector into a software message object.

##### 3.2.3 Clock and Reset Control
*   **REQ-FUN-020:** The infrastructure shall generate one or more free-running clocks for the DUT as configured.
*   **REQ-FUN-021:** The infrastructure shall provide a mechanism for the software to assert and de-assert a global hardware reset signal.
*   **REQ-FUN-022:** A hardware transactor shall be able to request a "time freeze" on its associated clock domain(s) via the `scemi_clock_port` mechanism.

##### 3.2.4 Service Loop
*   **REQ-FUN-030:** The infrastructure shall provide a `ServiceLoop()` function that processes pending message transfers, clock control, and other internal operations.
*   **REQ-FUN-031:** The service loop shall be designed to be integrable into an external event loop (e.g., SystemC kernel `sc_start`).
*   **REQ-FUN-032:** The service loop shall have a mechanism to run for a specified number of hardware clock cycles or until a specified condition is met.

##### 3.2.5 Error Handling
*   **REQ-FUN-040:** The API shall provide a function to register a user-defined error handler callback.
*   **REQ-FUN-041:** Fatal errors (e.g., communication failure, internal inconsistency) shall be reported via the registered error handler and/or as a return status from API calls.
*   **REQ-FUN-042:** The interface shall not attempt to recover from fatal errors; the session is considered terminated.

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance
*   **REQ-NFR-001:** The communication interface shall be designed to minimize host workstation interaction and shall not become the primary bottleneck in a co-emulation session.
*   **REQ-NFR-002:** Message channels shall be transaction-oriented, batching data where possible to maximize throughput and minimize latency overhead.

##### 3.3.2 Compatibility
*   **REQ-NFR-010:** The software-side API shall be compatible with single-threaded C/C++ applications.
*   **REQ-NFR-011:** The software-side API shall be compatible with multi-threaded environments, specifically allowing safe integration with the SystemC simulation kernel.

##### 3.3.3 Reliability
*   **REQ-NFR-020:** The interface shall provide deterministic behavior for a given hardware design and software test sequence.
*   **REQ-NFR-021:** All fatal error conditions shall be clearly identified and reported.

##### 3.3.4 Maintainability & Usability
*   **REQ-NFR-030:** The specification shall clearly delineate requirements and responsibilities for the three user roles (End User, Transactor Implementor, Infrastructure Implementor).
*   **REQ-NFR-031:** The API and macro definitions shall be consistent and follow common industry naming conventions.

### 4. Verification and Acceptance

#### 4.1 Acceptance Criteria
A compliant SCE-MI implementation will be accepted upon satisfying the following:
1.  **Functional Compliance:** All APIs and HDL macros behave as specified in this document.
2.  **Interoperability Success:** Transactor/proxy models developed for one compliant implementation function correctly with another compliant implementation ("plug-and-play").
3.  **Performance Validation:** In a representative co-emulation benchmark, the SCE-MI interface does not introduce a significant performance bottleneck (>5% overhead) compared to the underlying platform's raw communication capability.
4.  **Consortium Validation:** Successful execution of a suite of conformance tests defined and approved by the SCE-API consortium members.

#### 4.2 Priority
The highest development priority is **REQ-NFR-001 (Performance)** and **REQ-FUN-010/011 (Core Message Passing)**, as they directly address the primary goal of replacing proprietary high-performance interfaces. Standardization and ease of use (**REQ-NFR-030, REQ-FUN-002**) are also of critical importance.

---
*This document is the proprietary work of the SCE-API Consortium. Distribution is limited to member organizations.*