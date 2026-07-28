# Software Requirements Specification (SRS)
## Standard Co-Emulation Modeling Interface (SCE-MI)
### Version 1.0 Draft

**Document Status:** Draft  
**Date:** [Current Date]  
**Authors:** SCE-API Consortium  
**Confidentiality:** Consortium Members

---

## 1. Introduction

### 1.1 Purpose
This document defines the Software Requirements Specification (SRS) for the Standard Co-Emulation Modeling Interface (SCE-MI). SCE-MI is a standardized, high-performance communication interface designed to bridge untimed software models with cycle-accurate hardware models running on emulation or verification platforms. The purpose is to eliminate proprietary API proliferation and performance bottlenecks in co-emulation, enabling plug-and-play verification solutions for System-on-Chip (SoC) design teams.

### 1.2 Scope
The scope of this specification is restricted to the modeling interface (SCE-MI) itself, which is a core component of the broader SCE-API (Standard Co-Emulation API) standard. It includes:
*   Definition of hardware-side macro interfaces (Verilog/VHDL) for transactors.
*   Definition of software-side proxy APIs (C/C++/SystemC) for software models.
*   Specification of the communication protocol, clock control, and synchronization mechanisms.
*   The infrastructure required to link, bind, and execute co-modeling sessions.

Out of scope are:
*   The physical transport layer between host and emulator (implementation-defined).
*   Higher-level SCE-API features such as debug, control, and coverage (future extensions).
*   Specific transactor or proxy IP implementations.

### 1.3 Definitions, Acronyms, and Abbreviations
*   **API:** Application Programming Interface.
*   **Co-Emulation/Co-Modeling:** The concurrent execution of software models and hardware models for verification.
*   **DUT:** Design Under Test.
*   **EDA:** Electronic Design Automation.
*   **HDL:** Hardware Description Language (Verilog, VHDL).
*   **IP:** Intellectual Property.
*   **RTL:** Register Transfer Level.
*   **SCE-API:** Standard Co-Emulation Application Programming Interface.
*   **SCE-MI:** Standard Co-Emulation Modeling Interface (the subject of this document).
*   **SoC:** System-on-Chip.
*   **Transactor:** A hardware model that translates between message-level transactions and cycle-accurate signal-level activity.
*   **Proxy:** A software model that provides an API to software testbenches and communicates with its corresponding hardware transactor via SCE-MI.

### 1.4 References
*   SCE-API Consortium Charter and Goals Document.
*   SystemC Language Reference Manual.
*   IEEE Standard Verilog Hardware Description Language (IEEE Std 1364).
*   IEEE Standard VHDL Language Reference Manual (IEEE Std 1076).

### 1.5 Document Overview
This SRS is structured to provide stakeholders with a complete understanding of the SCE-MI requirements. It covers overall product perspective, specific functional and data requirements, external interfaces, non-functional requirements, and supporting information.

## 2. Overall Description

### 2.1 Product Perspective
SCE-MI is an intermediary layer within the co-emulation ecosystem. It sits between the user's software testbench (C/C++/SystemC) and the hardware DUT (RTL/gate-level) on the emulator. It relies on infrastructure provided by EDA/emulator vendors to handle the physical communication.

**System Context Diagram:**
```
[Software Testbench (C/C++/SystemC)]
        |
        | (Calls Proxy API)
        V
[SCE-MI Software-Side Library & Proxy Layer]
        |
        | (SCE-MI Message Protocol)
        V
[SCE-MI Infrastructure & Transport Layer]
        |
        | (Platform-specific Link)
        V
[SCE-MI Hardware-Side Macros & Transactors]
        |
        | (HDL Signals)
        V
[Hardware DUT on Emulator]
```

### 2.2 Stakeholders and User Classes
| Stakeholder Class | Description | Primary Goals |
| :--- | :--- | :--- |
| **End User** | SoC design/verification engineer. | Connect software testbench to hardware DUT quickly and reliably without deep SCE-MI expertise. Maximize emulation performance. |
| **Transactor Implementor** | IP or EDA tool vendor engineer. | Create portable, reusable transactor and proxy models using standard SCE-MI constructs. |
| **Infrastructure Implementor** | Emulator or EDA platform vendor engineer. | Provide a compliant, high-performance implementation of the SCE-MI software library and hardware macros for their platform. |

### 2.3 User Stories
1.  **US-1 (End User - Productivity):** As an end user, I want to use pre-built transactor models so that I can quickly bridge my untimed software testbench to my RTL DUT without writing SCE-MI code.
2.  **US-2 (End User - Performance):** As an end user, I want the interface to avoid communication bottlenecks so that my emulator’s performance is not throttled during co-modeling.
3.  **US-3 (Transactor Implementor - Portability):** As a transactor implementor, I want a standard hardware-side macro interface (e.g., message ports, clock control) so that I can create portable transactor models for different emulators.
4.  **US-4 (Transactor Implementor - Abstraction):** As a transactor implementor, I want a software-side proxy API so that I can provide easy-to-use software models that hide SCE-MI complexity from end users.
5.  **US-5 (Infrastructure Implementor - Clarity):** As an infrastructure implementor, I want a clear functional specification of macros and APIs so that I can build a compliant and optimized SCE-MI implementation for my platform.
6.  **US-6 (Infrastructure Implementor - Automation):** As an infrastructure implementor, I want parameters derived from the user’s netlist so that I can automatically configure the interface dimensions (e.g., clock ratios, port widths).

### 2.4 Operating Environment
*   **Software Side:** Host machine running Linux/Unix. Software models written in C, C++, or SystemC. Must support both single-threaded and multi-threaded execution models.
*   **Hardware Side:** Emulation platform (e.g., FPGA-based or processor-based emulator). Hardware models written in Verilog or VHDL (RTL or gate-level).
*   **Link:** Implementation-defined physical transport (e.g., PCIe, Ethernet, proprietary link).

### 2.5 Design and Implementation Constraints
1.  The hardware-side interface must be defined as synthesizable, empty HDL modules (macros) with well-defined ports and parameters.
2.  The software-side API must be provided in both C and C++ (with object-oriented wrappers) forms.
3.  The interface must be transaction-oriented (message-based), not signal-oriented, to maximize performance.
4.  The specification must allow for implementation-specific optimization of the transport layer.

### 2.6 Assumptions and Dependencies
*   **A-1:** The SCE-API consortium is formed and provides governing support.
*   **A-2:** Emulator vendors are willing to implement the SCE-MI infrastructure.
*   **A-3:** Users adopt a co-emulation flow that separates untimed software modeling from cycle-accurate hardware execution.
*   **D-1:** The specification depends on the existence of compliant HDL simulators and compilers for the target emulation platforms.

## 3. System Features and Requirements

### 3.1 Feature 1: Hardware-Side Macro Definition
**Description:** A set of standard, empty HDL modules (macros) that transactor implementors instantiate in their bridge netlist.

**Requirements:**
*   **REQ-HW-1:** The `MessageInPort` macro shall provide a channel for sending messages from hardware to software.
*   **REQ-HW-2:** The `MessageOutPort` macro shall provide a channel for receiving messages from software to hardware, with configurable priority.
*   **REQ-HW-3:** The `ClockPort` macro shall generate a controlled clock (`cclock`) and reset (`creset`) based on a ratio defined against an uncontrolled clock (`uclock`).
*   **REQ-HW-4:** The `ClockControl` macro shall allow a transactor to pause the controlled clock(s) via `ReadyForCclock` signals to synchronize with message processing.
*   **REQ-HW-5:** All macros shall have clearly defined, synthesizable ports and parameters as specified in Section 4 (Data Requirements).

### 3.2 Feature 2: Software-Side Proxy API
**Description:** A library providing C and C++ APIs for creating proxy models that communicate with hardware transactors.

**Requirements:**
*   **REQ-SW-1:** The API shall provide functions to initialize and shut down the SCE-MI infrastructure (`SceMiInit`, `SceMiClose`).
*   **REQ-SW-2:** The API shall provide object-oriented C++ classes (e.g., `SceMiMessageInPortProxy`, `SceMiMessageOutPortProxy`) to represent hardware ports.
*   **REQ-SW-3:** The API shall provide a `ServiceLoop()` function to service message channels, which must be called periodically in the software thread.
*   **REQ-SW-4:** The API shall support non-blocking (`trySend`, `tryReceive`) and blocking (`send`, `receive`) operations on message ports.
*   **REQ-SW-5:** The API shall provide a name-based binding mechanism to connect proxy objects to specific hardware port instances.

### 3.3 Feature 3: Infrastructure Linkage and Parameter Generation
**Description:** The toolflow that processes the user's hardware netlist, extracts SCE-MI configuration, and generates files necessary for binding.

**Requirements:**
*   **REQ-INF-1:** The infrastructure linker shall analyze the user's bridge netlist and identify all instantiated SCE-MI macros.
*   **REQ-INF-2:** The linker shall extract parameters (e.g., `PortWidth`, `ClockRatio`) from each macro instance.
*   **REQ-INF-3:** The linker shall generate a **Parameter File** containing a canonical representation of all SCE-MI objects (ports, clocks, bindings) and their attributes.
*   **REQ-INF-4:** The format and location of the Parameter File is implementation-defined **(Undecided Issue 1)**.
*   **REQ-INF-5:** The linker shall produce a final netlist suitable for the target emulator platform.

### 3.4 Feature 4: Co-Modeling Execution and Synchronization
**Description:** The runtime behavior that manages message transport, clock control, and synchronization between software and hardware domains.

**Requirements:**
*   **REQ-RT-1:** The infrastructure shall transport messages between software proxies and hardware transactors with low latency and high bandwidth.
*   **REQ-RT-2:** The software `ServiceLoop()` shall be responsible for dispatching incoming messages to proxy callbacks and polling for outgoing message completion.
*   **REQ-RT-3:** When a transactor asserts `ReadyForCclock=0`, the associated controlled clock(s) shall be paused in a low state within a defined number of `uclock` cycles.
*   **REQ-RT-4:** The infrastructure shall provide a cycle stamp with each message to aid in debugging and temporal analysis.
*   **REQ-RT-5:** The shutdown sequence shall call user-registered close callbacks and gracefully decouple hardware and software sides.

### 3.5 Feature 5: Error Handling and Diagnostics
**Requirements:**
*   **REQ-ERR-1:** The API shall support a global error callback mechanism for reporting fatal errors.
*   **REQ-ERR-2:** Functions shall also return traditional status codes (e.g., `SCEMI_OK`, `SCEMI_ERROR`).
*   **REQ-ERR-3:** The infrastructure shall support the logging of informational and warning messages.
*   **REQ-ERR-4:** Error messages shall be clear and indicate the SCE-MI object (port, clock) involved where possible.

## 4. Data Requirements

### 4.1 Logical Data Model
Key data entities for the SCE-MI infrastructure:

| Entity | Primary Key | Description & Key Fields |
| :--- | :--- | :--- |
| **MessageInPort** | (`TransactorName`, `PortName`) | Hardware->Software channel. Fields: `PortWidth`, `ReceiveReady` (input), `TransmitReady` (output), `Message` (output vector). |
| **MessageOutPort** | (`TransactorName`, `PortName`) | Software->Hardware channel. Fields: `PortWidth`, `PortPriority`, `TransmitReady` (input), `ReceiveReady` (output), `Message` (input vector). |
| **ClockPort** | `ClockName` | Clock generator. Fields: `ClockNum`, `RatioNumerator`, `RatioDenominator`, `DutyHi`, `DutyLo`, `Phase`, `ResetCycles`, `Cclock` (output), `Creset` (output). |
| **ClockControl** | (`TransactorName`, `ClockNum`) | Clock pausing interface. Fields: `Uclock` (output), `Ureset` (output), `ReadyForCclock` (input), `CclockEnabled` (output). |
| **SceMiParameters** | `ObjectKind` | Runtime configuration. Attribute values (integer/string) for all objects. |
| **SceMiMessageData** | *N/A* | Message instance. Fields: `Data` array, `WidthInBits`, `WidthInWords`, `CycleStamp`. |

### 4.2 Parameter File Schema (Conceptual)
The Parameter File must contain sufficient information to uniquely identify and bind to every SCE-MI object.
```yaml
# Example Conceptual Structure
SceMiVersion: "1.0"
MessageInPorts:
  - TransactorName: "pci_tx"
    PortName: "req"
    PortWidth: 64
    HardwareId: 0x0010 # Implementation-specific
MessageOutPorts:
  - TransactorName: "pci_rx"
    PortName: "rsp"
    PortWidth: 32
    PortPriority: 1
Clocks:
  - ClockName: "core_clk"
    ClockNum: 0
    RatioNumerator: 1
    RatioDenominator: 10
```
*(Specific format is implementation-defined - Undecided Issue 1)*

## 5. External Interface Requirements

### 5.1 User Interfaces
No direct graphical user interface is specified. The primary interfaces are programmatic (APIs and HDL modules).

### 5.2 Hardware Interfaces
*   **HDL Macros:** As defined in Section 3.1 and 4.1. These are the points of integration for user transactors.
*   **Physical Transport:** Defined by the Infrastructure Implementor. SCE-MI imposes no requirements other than it must support the logical message protocol.

### 5.3 Software Interfaces
*   **C API:** A set of `sceMi_*` functions and opaque handle types (e.g., `SceMi`, `SceMiMessageInPortHandle`).
*   **C++ API:** A set of classes (e.g., `SceMi`, `SceMiMessageInPortProxy`) wrapping the C API for ease of use.
*   **SystemC Compatibility:** The C++ API shall be usable within SystemC modules and threads.

### 5.4 Communication Interfaces
The logical SCE-MI message protocol is transaction-oriented. It assumes a reliable, in-order transport layer provided by the infrastructure.

## 6. Non-Functional Requirements

### 6.1 Performance
*   **NFR-PERF-1:** The interface design shall not be an inherent bottleneck. Emulator performance shall be limited by DUT complexity and physical transport, not by SCE-MI overhead.
*   **NFR-PERF-2:** Message channels shall be transaction-oriented to amortize software communication overhead over many hardware cycles.

### 6.2 Compatibility
*   **NFR-COMP-1:** Must support software models in single-threaded C/C++ and multi-threaded environments (e.g., SystemC).
*   **NFR-COMP-2:** Must provide both C and C++ language bindings.

### 6.3 Portability
*   **NFR-PORT-1:** Hardware-side macros shall be defined in a synthesizable subset of Verilog and VHDL, portable across different emulator platforms.
*   **NFR-PORT-2:** Software-side proxy code written to the SCE-MI API shall be source-code portable across different infrastructure implementations.

### 6.4 Reliability, Error Handling, and Fault Tolerance
*   **NFR-REL-1:** The infrastructure shall detect and report fatal configuration errors (e.g., binding failure, parameter mismatch) at initialization.
*   **NFR-REL-2:** The system shall be resilient to software model crashes where possible, allowing the emulator to be reset independently.

### 6.5 Usability
*   **NFR-USE-1:** For End Users, SCE-MI complexity shall be hidden behind pre-built transactor and proxy models.
*   **NFR-USE-2:** The binding process shall use intuitive name-based rendezvous, not low-level IDs.

### 6.6 Extensibility
*   **NFR-EXT-1:** The parameter system shall allow for implementation-specific parameters.
*   **NFR-EXT-2:** The SCE-MI design shall allow for future expansion within the SCE-API framework to include debug, control, and coverage features.

## 7. Other Requirements

### 7.1 Development Process & Milestones
1.  Formation of SCE-API consortium with founding participants.
2.  Completion and ratification of SCE-MI Version 1.0 specification (this document).
3.  Availability of compliant SCE-MI implementations from key infrastructure implementors.
4.  Availability of transactor/proxy IP from vendors for common interfaces (PCIe, Ethernet, AXI).
5.  Successful adoption and demonstrated ROI by SoC design teams.

### 7.2 Risks and Mitigation
| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| Slow adoption due to proprietary APIs | Medium | High | Consortium-driven standardization. Demonstrate clear performance/productivity benefits via benchmarks and tutorials. |
| Implementation complexity | High | Medium | Provide detailed specification, reference examples (e.g., "Routed" tutorial), and compliance test suites. |
| Deadlocks in co-modeling | Medium | High | Clear documentation and best practices for using `ServiceLoop()` and clock control in multi-threaded contexts. |
| Performance not meeting expectations | Medium | High | Specification is optimized for message-oriented communication. Allow implementors to optimize their transport layer. |
| Debugging difficulties | High | Medium | Future SCE-API extensions for debug. Promote use of cycle stamping and info messages in initial version. |

### 7.3 Undecided Issues (TBD)
1.  The specific format (XML, JSON, binary) and location of the generated parameter file.
2.  Handling of complex, multi-phase reset sequences beyond the default controlled reset.
3.  Full formal semantics for multi-clock alignment in all corner cases (phase shifts > duty cycle).
4.  Detailed arbitration semantics when multiple `MessageOutPorts` with identical priority contend.
5.  Clarification of memory ownership and deallocation responsibilities for certain internal data structures passed across the API.
6.  Support for RTL C (SystemC) as a hardware modeling language alongside Verilog/VHDL.

---
**Appendix A: Revision History**
| Version | Date | Author(s) | Description of Change |
| :--- | :--- | :--- | :--- |
| 0.1 | [Date] | Consortium | Initial Draft SRS created from balanced summary. |
| 1.0 Draft | [Date] | Consortium | First complete draft for consortium review. |

**Appendix B: Glossary**
*(To be populated with detailed terms from the specification.)*