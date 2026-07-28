# Detailed Summary: Standard Co-Emulation Modeling Interface (SCE-MI)

## Background and Scope
This document proposes the Standard Co-Emulation Modeling Interface (SCE-MI), a high-performance API designed to bridge untimed software models on a host workstation with structural hardware models (e.g., RTL netlists) on verification platforms like emulators. It addresses industry needs for a common, efficient interface to replace proprietary APIs, enabling plug-and-play verification solutions. The scope is restricted to the modeling interface, focusing on message-based communication channels and clock control, excluding debug, coverage, and other future potential extensions. Non-goals include supporting event-based or sub-cycle accurate simulation bridging, as the interface is optimized for untimed-to-cycle-accurate abstraction.

## Stakeholders Matrix and Use Cases
*   **End User (SoC Design Team):** Uses pre-built transactor and proxy models to connect their software testbench to the hardware DUT without needing deep SCE-MI API knowledge.
*   **Transactor Implementor (IP/Model Provider):** Develops and supplies the hardware transactor models and software proxy models that encapsulate the SCE-MI interface details for specific protocols or DUT interfaces.
*   **SCE-MI Infrastructure Implementor (EDA Tool/Platform Vendor):** Provides the compliant implementation of the SCE-MI software and hardware infrastructure for their specific verification platform (e.g., emulator, simulator).

**Main Scenarios:**
1.  **System Configuration:** An end user compiles software models, links them with the SCE-MI software side, and uses an infrastructure linker to compile a hardware bridge netlist containing transactors, DUT, and SCE-MI macros.
2.  **Co-Modeling Session Initialization:** The software executable initializes, binds message port proxies to hardware ports via name association, and begins simulation.
3.  **Untimed-to-Cycle-Accurate Transaction:** A software model sends a message via an input port proxy; the SCE-MI transports it; the transactor decomposes it into cycle-accurate events for the DUT.
4.  **Cycle-Accurate-to-Untimed Transaction:** The DUT produces events; a transactor composes them into a message sent via an output port; the SCE-MI delivers it to the software proxy's registered callback.
5.  **Controlled Clock Operation:** A transactor de-asserts `ReadyForCclock` to freeze the DUT clock while processing a message, then re-asserts it to resume.
6.  **Service Loop Execution:** The application (or a dedicated thread) calls `SceMi::ServiceLoop()` to allow the infrastructure to service message channels and dispatch callbacks.

**Exception Scenarios:**
7.  **Error Handling:** An irrecoverable error occurs in the SCE-MI infrastructure, triggering the registered error handler or filling a provided `SceMiEC` structure.
8.  **Binding Failure:** A `BindMessageInPort` call fails because the specified transactor or port name is not found in the parameters derived from the hardware netlist.

## Business Process
**Main Process: Co-Modeling Session Setup and Execution**
1.  **Trigger:** User initiates a co-modeling session.
2.  **Software Model Compilation:** User compiles C/C++ software models (testbench, proxies) and links with the SCE-MI software-side library.
3.  **Infrastructure Linkage:** Infrastructure linker analyzes the user's hardware bridge netlist (containing SCE-MI macros, transactors, DUT), extracts parameters (port counts, widths, clock specs), and generates a platform-specific executable/netlist and a parameter file.
4.  **Hardware Model Elaboration:** The compiled hardware model is loaded onto the emulator/verification platform.
5.  **Software Initialization & Binding:** Software executable starts, initializes the SCE-MI (`SceMi::Init`), constructs software models, which then bind their message port proxies to the hardware using names from the parameter file.
6.  **Simulation Execution:** Application runs, software models send/receive messages via proxies. The `ServiceLoop()` is called periodically to service channels.
7.  **Transaction Flow:** Messages are serialized, transported, and decomposed/composed by transactors between abstraction levels.
8.  **Shutdown:** Simulation completes, `SceMi::ShutDown()` is called, terminating the session gracefully.

**Key Branch A: Multi-threaded Software Environment**
*   Step 6a: A dedicated autonomous thread (e.g., `SceMiDispatcher`) repeatedly calls `ServiceLoop()`.
*   Step 6b: Other application threads run concurrently, interacting with message port proxies.
*   Step 6c: Callbacks from `ServiceLoop()` (e.g., message receive) trigger processing in slave threads.

**Key Branch B: Single-threaded Software Environment**
*   Step 6a: The application strategically places calls to `ServiceLoop()` within its main execution flow.
*   Step 6b: All processing, including callback execution, occurs within the single thread.

## Domain Model
*   **SceMi** (Singleton): The main interface object. Fields: version (required), parameters reference (required).
*   **SceMiParameters:** Container for interface configuration. Fields: object database (required).
*   **SceMiMessageInPortProxy:** Represents a software-side endpoint for sending messages to hardware. Fields: transactorName (required, unique binding), portName (required, unique binding), portWidth (required), binding context/callbacks.
*   **SceMiMessageOutPortProxy:** Represents a software-side endpoint for receiving messages from hardware. Fields: transactorName (required, unique binding), portName (required, unique binding), portWidth (required), binding context/callbacks (receive callback required).
*   **SceMiMessageData:** Holds serialized message payload. Fields: data array (size derived from port width, required), cycleStamp (output messages only).
*   **Transactor (Hardware Module):** User-defined module containing SCE-MI macros. Fields: hierarchical path name (required, unique), contains `SceMiClockControl` macro (at least one required).
*   **Message Port (Hardware Macro):** Instantiation of `SceMiMessageInPort` or `SceMiMessageOutPort`. Fields: hierarchical path name (required, unique), portWidth (required), PortPriority (output port only).
*   **Clock Port (Hardware Macro):** Instantiation of `SceMiClockPort`. Fields: clockName (instance label, required, unique), ClockNum (required, unique), ratio/duty/phase/reset parameters (required).

## Interfaces and Integrations
*   **Software Models <-> SCE-MI C++/C API (Internal):** Direction: Bi-directional. Interaction: Models call API for initialization, binding, sending messages, and registering callbacks. Input: Model data, function pointers. Output: Proxy object handles, callback invocations with message data. SLA: API calls must be non-blocking where specified; error handling must be immediate or via callback.
*   **SCE-MI Software Side <-> SCE-MI Hardware Side (External/Platform):** Direction: Bi-directional. Theme: High-speed message transport and clock control synchronization. Input: Serialized message data from proxies, clock control signals from transactors. Output: Message data to hardware ports, clock enable/edge signals to transactors. SLA: Transport mechanism is implementation-defined but must avoid bottlenecks; clock control handshake must be honored.
*   **Infrastructure Linker <-> Hardware Netlist (Internal):** Direction: Linker reads netlist. Interaction: Parses user netlist to discover SCE-MI macro instances and parameters. Input: HDL source files (Verilog/VHDL). Output: Augmented platform netlist, parameter file. SLA: Must correctly identify all SCE-MI constructs and parameters.
*   **SCE-MI Software Side <-> Parameter File (Internal):** Direction: Software reads file. Interaction: `SceMiParameters` object loads data from the file generated by the linker. Input: File path/name. Output: Populated parameter database accessible via API. SLA: File format is implementation-specific, but the API must provide access to the required parameter set.

## Acceptance Criteria
**Capability: Message Channel Communication**
*   Given a bound message input port proxy and a transactor ready to receive (`ReceiveReady` asserted), when the software model calls `Send()` with a `SceMiMessageData` object, then the message data appears on the `Message` vector of the corresponding `SceMiMessageInPort` macro on the next appropriate uclock edge.
*   Given a transactor asserting `TransmitReady` with message data on a `SceMiMessageOutPort`, when the output channel is ready (`ReceiveReady` asserted), then the message is transported and the registered `Receive` callback is invoked on the software side during a subsequent `ServiceLoop()` call.

**Capability: Controlled Clock Operation**
*   Given a transactor that needs to process a message, when it de-asserts its `ReadyForCclock` signal, then the associated controlled clock's next posedge is disabled (CclockEnabled goes low), freezing the DUT.
*   Given multiple transactors controlling the same clock, when any one de-asserts `ReadyForCclock`, then the clock is disabled for all transactors (`CclockEnabled` goes low for all associated `SceMiClockControl` macros).

**Capability: System Initialization and Binding**
*   Given a valid parameter file generated from the hardware netlist, when the software calls `SceMi::Init()` and then `BindMessageInPort()` with correct transactor and port names, then a proxy object is returned, establishing a channel to the specified hardware port.

## Non-Functional Metrics
*   **Performance:** Message transport latency should be minimized to avoid throttling emulator performance. The interface should support burst message transfers where possible.
*   **Reliability:** The interface must guarantee message delivery between proxy and port. Error handling must provide clear, actionable information for fatal errors.
*   **Compatibility:** The API must function correctly in both single-threaded and multi-threaded (e.g., SystemC) software environments.
*   **Observability:** The parameter access API must allow inspection of the interface configuration. Info/Error handlers provide runtime status and fault reporting.

## Milestones and Release Strategy
1.  **API Specification Finalization:** Ratification of the SCE-MI 1.0 functional specification by the consortium.
2.  **Reference Implementation:** Development of a compliant software and hardware infrastructure by one or more implementors.
3.  **Transactor IP Development:** Creation of example and commercial transactor/proxy models by IP providers.
4.  **End-User Pilot Projects:** Initial adoption and testing by design teams on representative SoC verification tasks.
5.  **Toolchain Integration:** Incorporation of the infrastructure linkage process into vendor tool flows.
6.  **Widespread Deployment:** Availability of compliant platforms and models from multiple vendors for general use.

## Risk List and Mitigation Strategies
1.  **Risk:** Implementation-specific transport layers may not meet performance goals, bottlenecking the emulator.
    *   **Mitigation:** Specification provides design guidelines (message-oriented, avoid event-level); implementors must benchmark and optimize.
2.  **Risk:** Proliferation of incompatible parameter file formats between implementors.
    *   **Mitigation:** The `SceMiParameters` API abstracts the file format; only the accessor interface is standardized.
3.  **Risk:** Complex multi-clock systems with phase shifts and "don't care" duty cycles may behave differently across platforms.
    *   **Mitigation:** Specification provides precise semantics for clock alignment and control; implementors must verify compliance.
4.  **Risk:** Deadlocks in software due to improper use of `ServiceLoop()` or callback protocols.
    *   **Mitigation:** Tutorial and documentation provide clear use models (e.g., dedicated dispatcher thread); API is designed for clean integration.
5.  **Risk:** Transactor designers may incorrectly implement the dual-ready handshake or clock control semantics.
    *   **Mitigation:** Detailed macro specifications, waveform examples, and tutorial code (e.g., Destination transactor) are provided.
6.  **Risk:** Software model memory management errors (e.g., deleting API-allocated objects).
    *   **Mitigation:** Clear memory allocation semantics are defined in the specification (user deletes user-constructed objects).
7.  **Risk:** Slow adoption due to legacy investment in proprietary APIs.
    *   **Mitigation:** Consortium-driven standard addresses customer pain points (locked-in solutions, low ROI); demonstrates value through pilot projects.
8.  **Risk:** The standard may not evolve to cover new requirements (e.g., debug, coverage).
    *   **Mitigation:** Scope is explicitly defined for modeling interface; document states that SCE-API may be expanded with additional parts in the future.

## Undecided Issues and Responsible Parties
1.  **Formal Conformance Test Suite:** Definition and ownership of a suite to verify implementor compliance. (Responsible: SCE-API Consortium)
2.  **Standardized Parameter File Format:** Whether to define a portable, text-based format in addition to the API. (Responsible: SCE-API Technical Committee)
3.  **Support for RTL C (SystemC) Hardware Models:** While mentioned as possible, the macro definitions are for Verilog/VHDL. Defining equivalent constructs for SystemC RTL. (Responsible: SCE-API Technical Committee / SystemC community liaison)
4.  **Detailed Performance Metrics and Benchmarks:** Specific latency/throughput targets for the message channels. (Responsible: SCE-API Consortium / Implementors)
5.  **Mechanism for Software-Initiated Controlled Reset:** The spec mentions a custom reset transactor would be needed; a standard method could be considered. (Responsible: SCE-API Technical Committee)
6.  **Formal Definition of "Message" vs. "Transaction" Layers:** The spec notes they are often used interchangeably but hints at a possible distinction. (Responsible: SCE-API Technical Committee)
7.  **Handling of Very Wide Message Ports (>1024 bits):** Potential implementation challenges. (Responsible: Implementors)
8.  **Version Negotiation Protocol Details:** The `::Version()` method is described; the exact compatibility rules need precise definition. (Responsible: SCE-API Technical Committee)