# Software Requirements Specification (SRS)
## Standard C/C++ Emulation Modeling Interface (SCE-MI)

**Document ID:** SRS-SCEMI-001  
**Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the software requirements for the Standard C/C++ Emulation Modeling Interface (SCE-MI). The primary purpose of SCE-MI is to provide a standardized, high-performance interface for connecting untimed software models executing on a host workstation to a structural hardware netlist (Device Under Test - DUT) running on a verification platform (e.g., emulator, FPGA prototype). Communication is established via message-passing channels, enabling transaction-level co-emulation.

#### 1.2 Scope
This specification covers the complete interface definition, including:
- The software-side Application Programming Interface (API) with both C++ and C language bindings.
- The hardware-side interface definition as implemented through a set of parameterized macros.
- The architectural model for message channels, transactors, and clock control.
- Performance constraints and design rules to prevent communication bottlenecks.

**Out of Scope:**
- Implementation details of specific verification platforms or emulators.
- The internal design of software models or hardware DUTs.
- Lower-level transport protocols between host and verification platform.

#### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
|------|------------|
| **SCE-MI** | Standard C/C++ Emulation Modeling Interface |
| **DUT** | Device Under Test (hardware netlist on the verification platform) |
| **Transactor** | A component that decomposes high-level messages into low-level signal transitions (or vice versa) |
| **Proxy** | A software object representing a hardware port, providing the API for message exchange |
| **Message Channel** | A unidirectional, point-to-point communication path between a software proxy and a hardware port |
| **Service Loop** | The primary software function that services hardware requests and advances simulation time |

#### 1.4 References
* IEEE Std 1014-1987, IEEE Standard for a Versatile Backplane Bus: VMEbus
* Accellera SCE-MI 2.3 Standard (Informative Reference)
* ISO/IEC 14882:2017, Programming languages — C++

#### 1.5 Document Overview
The remainder of this document details the overall description of the product, specific requirements for the software and hardware interfaces, and performance constraints. Requirements are categorized functionally and presented with unique identifiers.

### 2. Overall Description

#### 2.1 Product Perspective
SCE-MI is a middleware interface layer that sits between host-based software models and platform-based hardware simulation. It is part of a larger co-emulation environment, which includes:
1. **Host Workstation:** Runs untimed C/C++ software models (e.g., stimulus generators, reference models, checkers).
2. **Verification Platform:** Runs a cycle-accurate or event-driven simulation of the DUT.
3. **Communication Link:** Physical/interconnect layer (e.g., PCIe, Ethernet) connecting host and platform.
4. **SCE-MI Infrastructure:** Provides the channel abstraction, synchronization, and clock management defined herein.

#### 2.2 Product Functions
The core functions of the SCE-MI interface are:
1. **Multi-Channel Messaging:** Establish and manage multiple, concurrent message channels between software and hardware.
2. **Transactor Support:** Provide the framework for transactors to convert between message-level and cycle-accurate signal-level transactions.
3. **Clock and Reset Control:** Generate controlled clocks for the DUT and provide a mechanism for transactors to manage clock activation.
4. **Initialization and Binding:** Initialize the interface and bind software proxy objects to specific hardware ports.
5. **Service Management:** Execute a service loop to handle hardware requests, message delivery, and time advancement.

#### 2.3 User Characteristics
The intended users are:
- **Software Verification Engineers:** Develop C/C++ models that use the SCE-MI API to send/receive transactions.
- **Hardware Verification Engineers:** Integrate the SCE-MI hardware macros into their DUT testbenches to connect to message ports.
- **Platform/Tool Developers:** Implement the underlying SCE-MI infrastructure for a specific verification platform.

#### 2.4 Constraints
1. **Performance Constraint:** The interface design must prevent communication bottlenecks that could compromise the performance of the emulator/verification platform.
2. **Hardware Interface Constraint:** The hardware-side interface must be definable exclusively through four provided, parameterized macros.
3. **Software API Constraint:** The software-side must offer both object-oriented (C++) and procedural (C) API bindings for key functions.
4. **Determinism:** The interface must support deterministic execution models for reproducible verification results.

#### 2.5 Assumptions and Dependencies
- The verification platform provides a reliable, in-order transport layer for data between host and DUT.
- The host workstation and verification platform share a synchronized notion of simulation time.
- The DUT's clocking and reset structure is compatible with the SCE-MI clock control model.

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 Software API (C++)
The C++ API shall provide a class-based interface for key functionalities.

**3.1.1.1 Initialization**
```cpp
// REQ-API-001
namespace scemi {
    class Infrastructure {
    public:
        static void initialize(int argc, char* argv[]);
        static void shutdown();
    };
}
```
*Purpose:* Bootstrap and cleanly terminate the SCE-MI infrastructure.

**3.1.1.2 Port Proxy Binding**
```cpp
// REQ-API-002
template<typename MessageType>
class MessageInPortProxy {
public:
    MessageInPortProxy(const std::string& portName);
    bool receive(MessageType& msg); // Non-blocking
    void receiveBlocking(MessageType& msg); // Blocking
};

template<typename MessageType>
class MessageOutPortProxy {
public:
    MessageOutPortProxy(const std::string& portName);
    bool send(const MessageType& msg); // Non-blocking
    void sendBlocking(const MessageType& msg); // Blocking
};
```
*Purpose:* Allow software models to obtain proxies for hardware ports and exchange typed messages.

**3.1.1.3 Service Loop**
```cpp
// REQ-API-003
namespace scemi {
    class Service {
    public:
        static void run(); // Main service loop
        static bool poll(); // Non-blocking poll
        static void advanceTime(uint64_t cycles); // Request time advance
    };
}
```
*Purpose:* Service hardware requests, deliver messages, and manage simulation time.

##### 3.1.2 Software API (C)
The C API shall provide a functional equivalent to the C++ API.

**3.1.2.1 Core Functions**
```c
// REQ-API-010
void scemi_initialize(int argc, char* argv[]);
void scemi_shutdown();

// REQ-API-011
void* scemi_bind_message_in_port(const char* portName, size_t messageSize);
void* scemi_bind_message_out_port(const char* portName, size_t messageSize);
int scemi_receive(void* portHandle, void* messageBuffer);
int scemi_send(void* portHandle, const void* message);

// REQ-API-012
void scemi_service_loop(void);
int scemi_service_poll(void);
```

##### 3.1.3 Hardware Interface Macros
The hardware-side interface shall be instantiated using the following macros. Their implementation is platform-dependent but their signature is standardized.

**3.1.3.1 MessageInPort**
```systemverilog
// REQ-HW-001
`MessageInPort(port_name, message_type, buffer_depth)
```
*Inputs:* Port name identifier, C-compatible message struct type, depth of input buffer.
*Behavior:* Creates a hardware port that can receive messages from a software proxy. The port shall provide handshake signals (`ready`, `valid`) and a data bus of width derived from `message_type`.

**3.1.3.2 MessageOutPort**
```systemverilog
// REQ-HW-002
`MessageOutPort(port_name, message_type, buffer_depth)
```
*Behavior:* Creates a hardware port that can send messages to a software proxy.

**3.1.3.3 ClockPort**
```systemverilog
// REQ-HW-003
`ClockPort(clock_name, reset_name, clock_period_high, clock_period_low)
```
*Behavior:* Instantiates a clock generator and associated reset signal for the DUT. The clock shall be controllable via the `ClockControl` macro.

**3.1.3.4 ClockControl**
```systemverilog
// REQ-HW-004
`ClockControl(control_interface_name)
```
*Behavior:* Provides a hardware interface that allows a transactor to start, stop, and query the status of clocks generated by `ClockPort`. This enables transactor-managed clock gating.

#### 3.2 Functional Requirements

##### 3.2.1 Message Channel Management
- **REQ-FUNC-010:** The system shall support a configurable number of simultaneous, independent message channels.
- **REQ-FUNC-011:** Each channel shall be unidirectional (InPort or OutPort).
- **REQ-FUNC-012:** Channels shall guarantee in-order message delivery.
- **REQ-FUNC-013:** Channels shall implement configurable buffering to decouple software and hardware execution, preventing stalls.

##### 3.2.2 Transactor Support
- **REQ-FUNC-020:** The interface shall allow a transactor (on the hardware side) to decompose a received message into a sequence of cycle-accurate signal manipulations on the DUT interface.
- **REQ-FUNC-021:** The interface shall allow a transactor to compose a sequence of DUT signal activities into a single message for transmission to the software.
- **REQ-FUNC-022:** The clock control mechanism shall be accessible to transactors to enable pausing clocks while processing multi-cycle transactions (`REQ-HW-004`).

##### 3.2.3 Clock and Reset Generation
- **REQ-FUNC-030:** The infrastructure shall generate one or more free-running clocks based on the `ClockPort` specification.
- **REQ-FUNC-031:** A global or domain-specific reset signal shall be asserted during initialization and upon request.
- **REQ-FUNC-032:** Transactors shall be able to temporarily stop clocks via the `ClockControl` interface to synchronize with slow message processing, ensuring determinism.

##### 3.2.4 Initialization and Binding
- **REQ-FUNC-040:** The software infrastructure shall parse configuration (e.g., from command line or file) to identify available hardware ports.
- **REQ-FUNC-041:** Binding a proxy to a non-existent port shall result in a well-defined error during initialization.
- **REQ-FUNC-042:** Both blocking and non-blocking communication modes shall be supported for sending and receiving messages.

#### 3.3 Performance Requirements
- **REQ-PERF-001:** The communication overhead per message shall not become the bottleneck for emulator performance. Target latency shall be documented per platform.
- **REQ-PERF-002:** The interface shall support a minimum message throughput of [TBD] messages/second per channel, as measured on a reference platform.
- **REQ-PERF-003:** The software service loop (`scemi_service_poll`) shall have a minimal overhead when no messages are pending, to avoid starving host CPU.

#### 3.4 Design Constraints
- **REQ-CONST-001:** The hardware interface shall be strictly defined by the four macros in Section 3.1.3. No other hardware-side modifications shall be required to use SCE-MI.
- **REQ-CONST-002:** The software API shall be compatible with C++11 and ANSI C99 standards.
- **REQ-CONST-003:** The system shall be designed to avoid internal locking or contention points that could serialize parallel message channels.

#### 3.5 Software Quality Attributes
- **REQ-QUAL-001 Reliability:** The interface shall ensure no message loss or corruption during transmission.
- **REQ-QUAL-002 Determinism:** For identical software model inputs and DUT behavior, the combined system execution shall be bit-accurate reproducible.
- **REQ-QUAL-003 Debuggability:** The infrastructure shall provide optional logging/tracing of message flow and clock control events.

### 4. Appendices

#### Appendix A: Example Usage Snippet
```cpp
// Software Model (C++)
#include <scemi.h>

struct MyTransaction { uint32_t addr; uint32_t data; };

int main(int argc, char* argv[]) {
    scemi::Infrastructure::initialize(argc, argv);

    MessageOutPortProxy<MyTransaction> stimPort("dut_stimulus");
    MessageInPortProxy<MyTransaction> monPort("dut_monitor");

    MyTransaction tx{0x1000, 0xDEADBEEF};
    stimPort.sendBlocking(tx); // Send to DUT

    scemi::Service::run(); // Enter service loop
    // ... (model would typically run in a thread)

    scemi::Infrastructure::shutdown();
    return 0;
}
```

```systemverilog
// Hardware Testbench (SystemVerilog)
`MessageInPort(dut_stimulus, my_transaction_t, 4)
`MessageOutPort(dut_monitor, my_transaction_t, 4)
`ClockPort(clk, rst_n, 5, 5)
`ClockControl(clock_ctrl)

// Transactor module instantiation
stimulus_transactor i_transactor (
    .clk(clk),
    .rst_n(rst_n),
    .scemi_message_in(dut_stimulus),
    .scemi_message_out(dut_monitor),
    .clock_ctrl(clock_ctrl),
    .dut_if(my_dut_interface)
);
```

#### Appendix B: Message Flow Diagram
*(Conceptual diagram would be inserted here showing: Host Software -> Proxy -> SCE-MI Channel -> Hardware Port -> Transactor -> DUT Signals)*

#### Appendix C: Revision History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2023-10-27 | SCE-MI WG | Initial Draft |

---
*This document is considered proprietary information. Distribution is limited.*