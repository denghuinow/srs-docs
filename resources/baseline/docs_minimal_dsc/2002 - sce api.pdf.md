# Software Requirements Specification (SRS)
## Standard Co-Emulation Modeling Interface (SCE-MI)

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the software requirements for the Standard Co-Emulation Modeling Interface (SCE-MI). The purpose of SCE-MI is to provide a standardized, vendor-neutral interface specification that facilitates high-performance communication between untimed software models executing on a host workstation and cycle-accurate hardware Design Under Test (DUT) models running on an emulation platform. This specification aims to replace proprietary APIs, thereby improving interoperability, portability, and user productivity in hardware verification and validation flows.

#### 1.2 Scope
The scope of this SRS is strictly limited to the definition of the modeling interface itself. It includes:
*   The specification of software-side C/C++ Application Programming Interfaces (APIs).
*   The specification of hardware-side macro interfaces for integration into transactors and the DUT.
*   The definition of the message-passing semantics and clock control mechanisms.

This specification explicitly **excludes**:
*   Implementation details of the underlying communication transport layer.
*   Debug interfaces, profiling tools, or code coverage instrumentation.
*   Specific emulator platform or host workstation dependencies.
*   User-facing tools for configuration or management.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **API:** Application Programming Interface.
*   **DUT:** Design Under Test. The hardware design being verified.
*   **SCE-MI:** Standard Co-Emulation Modeling Interface.
*   **Transactor:** A bridge model that converts between untimed software-level transactions and cycle-accurate signal-level activity on the DUT interface.
*   **Message Channel:** A bidirectional, configurable communication path for transporting transactions.
*   **Host:** The workstation running the software testbench.
*   **Emulator:** The hardware acceleration or emulation platform running the DUT model.

#### 1.4 References
*   IEEE Std 1016-2009, IEEE Standard for Information Technology—Systems Design—Software Design Descriptions.
*   Project Charter: SCE-MI Standardization Initiative.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its functions, and its operating environment. Section 3 details the specific external interface and software functional requirements.

### 2. Overall Description

#### 2.1 Product Perspective
SCE-MI is a critical middleware layer that sits between the software verification environment (e.g., SystemVerilog/UVM testbench in C++) and the emulated hardware design. It abstracts the physical communication link (e.g., PCIe, Ethernet) and provides a transaction-level modeling paradigm that is essential for maintaining high emulation performance.

#### 2.2 Product Functions
The core functions of the SCE-MI specification are:
1.  **Message Transport:** Provide a mechanism for the reliable, untimed transport of structured messages (transactions) between software and hardware domains via configurable channels.
2.  **Hardware-Side Interface:** Define a set of macros and modules (e.g., `scemi_message_port`, `scemi_clock_control`) that transactor developers use to send/receive messages and manage DUT clock domains from within the hardware description language (e.g., SystemVerilog).
3.  **Software-Side Interface:** Define a C++/C API with objects and methods for software developers to bind to channels, send messages, receive messages, and service communication requests.
4.  **Clock Management:** Provide facilities for software transactors to control the advancement of DUT simulation time, specifically to stop clocks for asynchronous message processing and resume them afterward.

#### 2.3 User Characteristics
1.  **End User / Verification Engineer:** Integrates existing software testbenches with hardware DUT models. Primary activities include configuring SCE-MI channels, writing minimal glue code to connect the testbench to the SCE-MI API, and managing the co-emulation run.
2.  **Transactor Implementor:** Creates reusable bridge models (transactors). Requires deep understanding of both the SCE-MI hardware-side macros and the DUT protocol to implement correct message-to-signal conversion.
3.  **SCE-MI Infrastructure Implementor:** Develops the platform-specific library that realizes the SCE-MI specification for a particular host-emulator combination. This user is concerned with low-level transport efficiency and threading models.

#### 2.4 Constraints
1.  **Message/Transaction Orientation:** The interface **must** be designed around coarse-grained messages or transactions. It must **not** be an event-oriented or signal-level interface, as fine-grained communication would create a performance bottleneck, throttling emulator speed.
2.  **Concurrency Support:** The software-side API and infrastructure **must** be designed to function correctly in both single-threaded and multi-threaded software environments.
3.  **Performance:** The specification must enable implementations that minimize communication overhead to preserve emulation performance.
4.  **Language Compatibility:** The software API must be callable from both C and C++ code.

#### 2.5 Assumptions and Dependencies
*   It is assumed that a reliable, bidirectional data transport layer exists between the host and the emulator, though its specifics are outside this specification's scope.
*   The hardware DUT model is described in a language compatible with the target emulator (e.g., SystemVerilog, VHDL).
*   A compliant SCE-MI infrastructure implementation is available for the target host and emulator platform.

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 Software APIs (C/C++)
The system shall provide the following core API components:

*   **Context Object:** `scemi_context_t`
    *   Shall represent a handle to an initialized SCE-MI communication session.
    *   Shall be created via `scemi_create_context()`.
    *   Shall be destroyed via `scemi_destroy_context()`.

*   **Channel Object:** `scemi_channel_t`
    *   Shall represent a bidirectional message channel.
    *   Shall be retrieved/bound via `scemi_bind_channel(context, "channel_name")`.
    *   Shall support type-safe messaging based on pre-defined message types.

*   **Message Send Function:** `scemi_message_send()`
    ```c
    int scemi_message_send(scemi_channel_t *channel,
                           const void *message_struct,
                           unsigned int message_type_id);
    ```
    *   Shall transmit an untimed message from software to the bound hardware transactor port.
    *   Shall be non-blocking where possible, returning immediately after queuing the message.

*   **Message Receive Function:** `scemi_message_receive()`
    ```c
    int scemi_message_receive(scemi_channel_t *channel,
                              void *message_buffer,
                              unsigned int message_type_id,
                              long long timeout_ns);
    ```
    *   Shall attempt to receive a message from the hardware side.
    *   Shall support blocking (timeout = -1), non-blocking (timeout = 0), and timed wait semantics.

*   **Communication Service Function:** `scemi_service()`
    *   Shall be called periodically in single-threaded environments to process incoming/outgoing message traffic.
    *   May be handled automatically by a background thread in multi-threaded implementations.

##### 3.1.2 Hardware Macros (SystemVerilog Example)
The system shall provide the following macro-based interfaces for hardware description:

*   **Message Port Macro:** `SCE_MI_MESSAGE_PORT`
    *   Shall declare a hardware port connected to a SCE-MI message channel.
    *   Shall generate the necessary RTL and infrastructure for message I/O.
    ```systemverilog
    SCE_MI_MESSAGE_PORT my_input_port(  // Instantiate a port
        .clock   (clk),
        .reset   (rst_n),
        .message (rx_message),
        .valid   (rx_valid),
        .ready   (rx_ready)
    );
    ```

*   **Clock Control Macro:** `SCE_MI_CLOCK_CONTROL`
    *   Shall provide an interface for the software transactor to stop and start a DUT clock domain to safely process asynchronous messages.
    ```systemverilog
    SCE_MI_CLOCK_CONTROL my_clock_ctl(
        .clock          (dut_clk),
        .stop_request   (sw_stop_req),
        .stopped_status (clock_stopped)
    );
    ```

*   **Clock Generation Macro:** `SCE_MI_CLOCK_GEN`
    *   Shall allow a software transactor to define and drive a virtual clock into the DUT.

#### 3.2 Functional Requirements

##### 3.2.1 Message Channel Management (FR-MCM)
*   **FR-MCM-1:** The system shall allow the configuration of multiple independent, bidirectional message channels.
*   **FR-MCM-2:** Each channel shall be uniquely identified by a string name, used for binding on both software and hardware sides.
*   **FR-MCM-3:** Channels shall support configurable depth buffering to decouple software and hardware execution.

##### 3.2.2 Untimed Message Transport (FR-UMT)
*   **FR-UMT-1:** The system shall transport complete message data structures atomically between host and emulator.
*   **FR-UMT-2:** Message ordering shall be preserved per channel (FIFO semantics).
*   **FR-UMT-3:** The transport mechanism shall add no timing semantics to the messages; they are considered "untimed" from the DUT's perspective.

##### 3.2.3 Clock Domain Control (FR-CDC)
*   **FR-CDC-1:** A software transactor shall be able to request the stoppage of a specified DUT clock domain via the API.
*   **FR-CDC-2:** The hardware shall acknowledge the clock stop, guaranteeing no clock edges occur while the software processes messages.
*   **FR-CDC-3:** The software transactor shall be able to release the clock, allowing it to resume operation.

##### 3.2.4 Software Concurrency Models (FR-SCM)
*   **FR-SCM-1:** In a single-threaded model, calls to `scemi_service()` shall be required to progress communication.
*   **FR-SCM-2:** In a multi-threaded model, the infrastructure shall provide a thread-safe API. Message send/receive calls may be made from any user thread.
*   **FR-SCM-3:** The infrastructure shall manage internal threading for communication servicing without requiring explicit `scemi_service()` calls in the multi-threaded model.

##### 3.2.5 Initialization and Configuration (FR-IC)
*   **FR-IC-1:** The system shall be initialized by parsing a standardized configuration file (e.g., `scemi.params`) that defines channels, message types, and connection parameters.
*   **FR-IC-2:** Both software and hardware builds shall use the same configuration file to ensure consistent channel mapping.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Author |  |  |  |
| Reviewer |  |  |  |
| Approver |  |  |  |