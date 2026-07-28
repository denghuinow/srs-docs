# **Software Requirements Specification (SRS)**
## **Standard Co-Emulation Modeling Interface (SCE-MI)**

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

## **1. Introduction**

### **1.1 Purpose**
This document defines the functional and non-functional requirements for the Standard Co-Emulation Modeling Interface (SCE-MI). The purpose of SCE-MI is to provide a vendor-neutral, high-performance communication standard between untimed software verification environments and timed hardware models running on emulation platforms. This specification enables interoperability, eliminates proprietary lock-in, and maximizes emulation throughput.

### **1.2 Scope**
This SRS covers the definition of the hardware-side interface macros, the software-side C/C++ API, and the message-oriented communication model. It specifies the mechanisms for transaction-level communication, clock control, and system initialization.

**In-Scope Items:**
*   Hardware-side macro definitions for message ports and clock control within transactors.
*   Software-side API for binding proxy objects, managing communication channels, and handling errors.
*   Definition of message-based communication channels optimized for transaction abstraction.
*   Support for both single-threaded (C) and multi-threaded (e.g., SystemC) software execution environments.
*   Specification for clock generation, ratio configuration, duty cycle, and reset semantics.

**Out-of-Scope Items:**
*   Debug, control plane, and code coverage interfaces (planned for future SCE-API expansions).
*   Interconnection and synchronization between software models (handled by native environments like SystemC).
*   Event-based or sub-cycle accurate simulation bridging.
*   Physical transport layer implementation or infrastructure linker tooling details.

### **1.3 Definitions, Acronyms, and Abbreviations**
| Term | Definition |
| :--- | :--- |
| **DUT** | Design Under Test. The hardware model (RTL/gate-level) being verified. |
| **Transactor** | A hardware model acting as an abstraction "gasket," converting message-level transactions into/from cycle-accurate DUT signal activity. |
| **Proxy** | A software object that provides a transactional interface to a corresponding hardware transactor. |
| **Message Port** | A unidirectional, message-oriented communication endpoint (Input or Output) connecting a software proxy to a hardware transactor. |
| **Infrastructure Linker** | A tool (vendor-specific) that extracts SCE-MI parameters from the hardware netlist and configures the communication infrastructure. |
| **Service Loop** | The software mechanism that polls for and processes incoming messages from hardware. |
| **Controlled Clock** | A clock domain generated and managed by the SCE-MI infrastructure, which can be globally frozen by transactors. |

### **1.4 References**
*   IEEE Std 1666-2011 - SystemC Language Reference Manual
*   IEEE Std 1800-2017 - SystemVerilog Unified Hardware Design, Specification, and Verification Language
*   IEEE Std 1076-2008 - VHDL Language Reference Manual

### **1.5 Document Overview**
This document is structured as follows: Section 2 provides an overall description of the product and its operating context. Section 3 details specific system features and requirements. Section 4 outlines non-functional requirements. Appendices provide supplementary information.

## **2. Overall Description**

### **2.1 Product Perspective**
SCE-MI is an interface standard, not a standalone product. It exists as a layer between:
1.  **Software Verification Environment:** Untimed testbenches written in C/C++/SystemC.
2.  **Hardware Emulation Platform:** Running structural HDL models (Verilog/VHDL DUTs).
3.  **Vendor Infrastructure:** The proprietary hardware/software communication stack provided by an EDA or emulator vendor.

SCE-MI defines the contract between these components to ensure interoperability.

### **2.2 User Classes and Characteristics**
| User Class | Characteristics | Key Goals |
| :--- | :--- | :--- |
| **End User (SoC Design/Verification Engineer)** | Integrates pre-built transactors and proxies into their verification environment. Seeks high performance and ease of use. | Connect testbench to DUT on emulator without vendor lock-in. Send/receive transaction messages. |
| **Transactor Implementor (IP Provider)** | Creates reusable verification IP (transactors and proxies). Expert in SCE-MI macros and API. | Develop IP that works across different vendor platforms using standardized interfaces. |
| **Infrastructure Implementor (EDA/Emulator Vendor)** | Implements the underlying SCE-MI-compliant communication stack. Expert in low-level software/hardware integration. | Provide a compliant, high-performance implementation of the SCE-MI specification. |

### **2.3 Operating Environment**
*   **Hardware Environment:** Emulation platforms (e.g., ZeBu, Palladium, Veloce, Protium) or FPGA-based prototyping systems.
*   **Software Environment:** Host machine running Linux/Unix. Software models may be compiled as C/C++ applications or SystemC simulations.
*   **Hardware Modeling Languages:** Verilog (IEEE 1800) and VHDL (IEEE 1076).
*   **Software Languages:** C (C99) and C++ (C++11 or later, including SystemC).

### **2.4 Design and Implementation Constraints**
1.  **Performance:** The interface must use message-oriented (not event-driven) communication to avoid emulation performance bottlenecks.
2.  **Language Support:** Must provide equivalent macro/functionality for both Verilog and VHDL.
3.  **Concurrency:** The software API must be safe for use in multi-threaded environments (e.g., SystemC threads) while also supporting simple single-threaded C programs.
4.  **Global Clock Control:** Any transactor must be able to issue a command to freeze all SCE-MI controlled clocks globally to safely compose/decompose transactions.
5.  **Parameter Extraction:** All configuration parameters (message port widths, clock ratios) must be defined in the hardware netlist in a way that can be extracted automatically by an infrastructure linker.

### **2.5 Assumptions and Dependencies**
*   It is assumed the infrastructure linker tool exists to handle parameter extraction and infrastructure configuration.
*   The physical communication link (e.g., PCIe, Ethernet) between host and emulator is provided by the vendor and is transparent to the SCE-MI user.
*   Software and hardware models are compiled and linked using vendor-provided tools that understand SCE-MI constructs.

## **3. System Features and Requirements**

### **3.1 Feature: Hardware-Side Interface Macros**

#### **3.1.1 Description**
Macros to be used within HDL (Verilog/VHDL) transactor code to define message ports, instantiate clock generators, and control clock freezing.

#### **3.1.2 Requirements**
*   **REQ-HW-001:** The specification shall provide a `SCEMI_INPUT_PORT` macro to declare a message input port (hardware receives from software).
*   **REQ-HW-002:** The specification shall provide a `SCEMI_OUTPUT_PORT` macro to declare a message output port (hardware sends to software).
*   **REQ-HW-003:** Each port macro shall define a parameter for bit-width (`n`) and a unique identifier (`port_id`).
*   **REQ-HW-004:** The specification shall provide a `SCEMI_CLOCK_GEN` macro to instantiate a controlled clock with configurable ratio, duty cycle, and initial state.
*   **REQ-HW-005:** The specification shall provide a `SCEMI_CLOCK_FREEZE` macro/function that, when called by any transactor, freezes all SCE-MI controlled clocks globally.
*   **REQ-HW-006:** The specification shall provide a `SCEMI_CLOCK_UNFREEZE` macro/function to resume all frozen clocks.
*   **REQ-HW-007:** All macros shall have semantically equivalent implementations for both Verilog and VHDL.

### **3.2 Feature: Software-Side C/C++ API**

#### **3.2.1 Description**
An API for software proxies to bind to hardware message ports, send/receive messages, manage the service loop, and handle errors.

#### **3.2.2 Requirements**
*   **REQ-SW-010:** The API shall provide a function `scemi_bind_input_proxy()` to create and bind a software proxy object to a specific hardware input port (software sends).
*   **REQ-SW-011:** The API shall provide a function `scemi_bind_output_proxy()` to create and bind a software proxy object to a specific hardware output port (software receives), registering a user-defined callback function.
*   **REQ-SW-012:** The API shall provide a non-blocking function `scemi_message_send()` for an input proxy to transmit a message to hardware.
*   **REQ-SW-013:** The API shall provide a function `scemi_service_loop_start()` to initiate the background polling mechanism for incoming messages.
*   **REQ-SW-014:** The API shall provide a function `scemi_service_loop_stop()` to gracefully terminate the message service loop.
*   **REQ-SW-015:** The API shall be thread-safe, allowing calls from multiple SystemC threads or POSIX threads.
*   **REQ-SW-016:** The API shall define a set of error codes (e.g., `SCEMI_OK`, `SCEMI_ERROR_PORT_NOT_FOUND`, `SCEMI_ERROR_TIMEOUT`) and an error reporting function.

### **3.3 Feature: Message-Oriented Communication**

#### **3.3.1 Description**
A channel model where data is transferred as discrete, atomic messages rather than per-cycle signal events.

#### **3.3.2 Requirements**
*   **REQ-COM-020:** Communication shall be transaction-oriented, where a single message corresponds to a high-level verification command or response.
*   **REQ-COM-021:** The infrastructure shall guarantee message ordering from a single software thread to a single hardware port.
*   **REQ-COM-022:** Message delivery shall be reliable; no messages shall be lost or corrupted in transit.
*   **REQ-COM-023:** The interface shall support message sizes up to a minimum of 64 kilobytes per port, as defined by the port's bit-width parameter.

### **3.4 Feature: Clock and Reset Control**

#### **3.4.1 Description**
Mechanisms to define, generate, and control clock signals for the DUT, and to manage reset sequencing.

#### **3.4.2 Requirements**
*   **REQ-CLK-030:** Clock generation shall be configurable with a ratio defined as `M:N` (software clock cycles : hardware clock cycles).
*   **REQ-CLK-031:** The duty cycle and initial phase (high/low) of a controlled clock shall be configurable.
*   **REQ-CLK-032:** The specification shall define a default "controlled reset" sequence that is synchronized with the controlled clocks.
*   **REQ-CLK-033:** The global clock freeze/unfreeze mechanism (REQ-HW-005, REQ-HW-006) shall have a corresponding software API call for diagnostic purposes.

### **3.5 Feature: System Initialization and Configuration**

#### **3.5.1 Description**
The process by which the software and hardware components discover each other and establish communication based on parameters extracted from the netlist.

#### **3.5.2 Requirements**
*   **REQ-INIT-040:** The infrastructure linker shall generate a machine-readable parameter file (format TBD) containing all SCE-MI port IDs, widths, and clock configurations.
*   **REQ-INIT-041:** The software API shall provide an initialization function `scemi_initialize()` that takes the parameter file path as an argument and configures the communication layer.
*   **REQ-INIT-042:** The hardware infrastructure shall be self-configuring based on parameters embedded in the netlist during the linking process.

## **4. Non-Functional Requirements**

### **4.1 Performance Requirements**
*   **REQ-PERF-050:** The communication latency for a single message shall be deterministic and documented by the infrastructure implementor.
*   **REQ-PERF-051:** The message throughput shall be sufficient to not become the bottleneck for emulation performance, targeting >90% utilization of the physical link's bandwidth for sustained transaction streams.

### **4.2 Safety and Reliability Requirements**
*   **REQ-REL-060:** The software API shall not crash or cause undefined behavior if called before `scemi_initialize()` or after `scemi_service_loop_stop()`.
*   **REQ-REL-061:** The system shall gracefully handle a disconnection of the physical link, allowing for re-initialization.

### **4.3 Compatibility Requirements**
*   **REQ-COMP-070:** SCE-MI transactors and proxies written to this specification shall be source-code compatible across different vendor implementations.
*   **REQ-COMP-071:** The software API shall be callable from pure C, C++, and SystemC contexts.

### **4.4 Design Requirements**
*   **REQ-DES-080:** The hardware macros shall synthesize to standard, vendor-agnostic logic, not relying on proprietary primitives.
*   **REQ-DES-081:** The software API shall be object-oriented in design (for C++) while maintaining a flat C-compatible interface.

## **5. Appendices**

### **5.1 User Stories Mapping to Requirements**

| User Story | Mapped Requirements |
| :--- | :--- |
| 1. Connect testbench to DUT without lock-in. | REQ-COMP-070, REQ-SW-010, REQ-SW-011 |
| 2. Create cross-platform transactors. | REQ-HW-001, REQ-HW-002, REQ-HW-007, REQ-COMP-070 |
| 3. Clear spec for implementors. | All REQ-HW-* and REQ-SW-* requirements. |
| 4. Send messages to hardware. | REQ-HW-001, REQ-SW-010, REQ-SW-012, REQ-COM-020 |
| 5. Receive messages via callbacks. | REQ-HW-002, REQ-SW-011, REQ-SW-013 |
| 6. Control clock freezing. | REQ-HW-005, REQ-HW-006, REQ-CLK-033 |

### **5.2 Undecided Issues and TBD**
1.  **Infrastructure Linker & Parameter File:** The exact format (XML, JSON, custom) and extraction methodology for the parameter file remains to be defined.
2.  **Extended Debug Interface:** Requirements for a standardized debug and control plane interface are deferred to a future version (SCE-API).
3.  **Advanced Reset Sequences:** Handling of complex, multi-phase, or asynchronous reset sequences beyond the basic controlled reset is not specified and may be vendor-extended.

---
*Document End*