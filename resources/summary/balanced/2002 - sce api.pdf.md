# Balanced Summary: Standard Co-Emulation Modeling Interface (SCE-MI)

## Goals and Scope
The SCE-MI specification defines a high-performance, multichannel communication interface to bridge untimed software models (e.g., in SystemC) with cycle-accurate hardware models (e.g., RTL/gate-level DUTs) running on emulators or verification platforms. It aims to solve proprietary API proliferation and performance bottlenecks in co-emulation, enabling plug-and-play verification solutions for SoC design teams. The scope is restricted to the modeling interface (SCE-MI), which is one part of the broader SCE-API standard.

## Stakeholders and User Stories
**Stakeholders:**
- **End User:** SoC design team member who uses pre-built transactors and proxies to connect software testbenches to hardware DUTs without deep SCE-MI knowledge.
- **Transactor Implementor:** IP or tool vendor who creates transactor models (hardware side) and proxy models (software side) using SCE-MI macros and APIs.
- **SCE-MI Infrastructure Implementor:** EDA tool or emulator vendor who provides a compliant implementation of the SCE-MI software and hardware components.

**User Stories:**
1. As an end user, I want to use pre-built transactor models so that I can quickly bridge my untimed software testbench to my RTL DUT without writing SCE-MI code.
2. As an end user, I want the interface to avoid communication bottlenecks so that my emulator’s performance is not throttled during co-modeling.
3. As a transactor implementor, I want a standard hardware-side macro interface (e.g., message ports, clock control) so that I can create portable transactor models for different emulators.
4. As a transactor implementor, I want a software-side proxy API so that I can provide easy-to-use software models that hide SCE-MI complexity from end users.
5. As an infrastructure implementor, I want a clear functional specification of macros and APIs so that I can build a compliant and optimized SCE-MI implementation for my platform.
6. As an infrastructure implementor, I want parameters derived from the user’s netlist so that I can automatically configure the interface dimensions (e.g., clock ratios, port widths).

## Key Processes
1. **Software Model Compilation:** Compile software models (C/C++/SystemC) and link with the SCE-MI software-side library to create an executable. (Trigger: Start of build process.)
2. **Infrastructure Linkage:** Analyze the user’s hardware bridge netlist, extract parameters from SCE-MI macro instances, and generate a parameter file and final netlist for the emulator. (Trigger: Hardware netlist compilation.)
3. **Hardware Model Elaboration:** Download and elaborate the compiled netlist on the emulator, preparing it for binding. (Trigger: Emulator setup.)
4. **Software Model Construction and Binding:** Execute the software executable, construct models, and bind message port proxies to hardware ports using names from the parameter file. (Trigger: Software execution start.)
5. **Co-Modeling Execution:** Software models send/receive messages via proxies; the SCE-MI infrastructure transports messages between sides and services channels via the ServiceLoop. (Trigger: Simulation run.)
6. **Clock Control:** Transactors can freeze controlled clocks (via ReadyForCclock signals) during message composition/decomposition, synchronizing with the uncontrolled clock. (Trigger: Transactor operation needing DUT pause.)
7. **Shutdown:** Gracefully terminate the co-modeling session, calling registered close callbacks and decoupling hardware/software sides. (Trigger: Simulation completion.)

## Domain Data Elements
- **MessageInPort:** Primary Key: (TransactorName, PortName); Fields: PortWidth, ReceiveReady (input), TransmitReady (output), Message (output vector).
- **MessageOutPort:** Primary Key: (TransactorName, PortName); Fields: PortWidth, PortPriority, TransmitReady (input), ReceiveReady (output), Message (input vector).
- **ClockPort:** Primary Key: ClockName; Fields: ClockNum, RatioNumerator, RatioDenominator, DutyHi, DutyLo, Phase, ResetCycles, Cclock (output), Creset (output).
- **ClockControl:** Primary Key: (TransactorName, ClockNum); Fields: Uclock (output), Ureset (output), ReadyForCclock (input), CclockEnabled (output), ReadyForCclockNegEdge (input), CclockNegEdgeEnabled (output).
- **SceMiParameters:** Primary Key: ObjectKind; Fields: Attribute values (integer/string) for objects like MessageInPort, MessageOutPort, Clock, ClockBinding.
- **SceMiMessageData:** Primary Key: N/A (message instance); Fields: Data array (words), WidthInBits, WidthInWords, CycleStamp.

## Non-Functional Requirements
1. **Performance:** The interface must avoid inherent bottlenecks to not throttle emulator performance; message channels are transaction-oriented to allow many hardware events per software message.
2. **Compatibility:** Must work with multi-threaded (e.g., SystemC) and single-threaded C/C++ environments; provides both C++ and C APIs.
3. **Portability:** Hardware-side macros are defined as empty Verilog/VHDL models with clear ports/parameters, allowing implementation across different HDLs and platforms.
4. **Error Handling:** Provides flexible error handling via error callbacks or traditional status returns for fatal errors; also supports informational/warning messages.
5. **Ease of Use:** For end users, complexity is hidden behind transactor and proxy models; binding uses intuitive name-based rendezvous.
6. **Extensibility:** Parameter system allows implementation-specific parameters; SCE-API may expand to include debug, control, coverage features.

## Milestones and External Dependencies
1. Formation of SCE-API consortium with founding participants (Aptix, CoWare, Ikos, Mentor Graphics, ST Microelectronics, Synopsys, TransEDA).
2. Completion and ratification of SCE-MI specification (target Version 1.0).
3. Availability of compliant SCE-MI implementations from infrastructure implementors (emulator/tool vendors).
4. Availability of transactor/proxy IP from transactor implementors for common interfaces (e.g., PCI, Ethernet).
5. Adoption by SoC design teams for verification projects, demonstrating improved productivity and ROI.

## Risks and Mitigation Strategies
1. **Risk:** Slow adoption due to existing proprietary APIs. **Mitigation:** Consortium-driven standardization and demonstrating clear performance/productivity benefits.
2. **Risk:** Implementation complexity leading to non-compliant or inefficient versions. **Mitigation:** Detailed specification, reference examples (like Routed tutorial), and compliance testing.
3. **Risk:** Deadlocks in co-modeling due to improper use of service loop or clock control. **Mitigation:** Clear documentation, best practices, and tutorial showing correct usage in multi-threaded contexts.
4. **Risk:** Performance not meeting expectations due to physical layer limitations. **Mitigation:** Specification optimized for message-oriented communication; implementors can optimize transport.
5. **Risk:** Difficulty in debugging co-modeling sessions. **Mitigation:** Future extensions to SCE-API for debug features; use of cycle stamping and info messages.

## Undecided Issues
1. Specific format and location of the parameter file generated by the infrastructure linker (implementation-defined).
2. Handling of more sophisticated reset sequences beyond the default controlled reset (may require custom reset transactors).
3. Full details of multi-clock alignment semantics in corner cases (e.g., phase shifts > duty cycle).
4. Priority arbitration semantics when multiple output ports with same priority contend on the same uclock.
5. Memory allocation/deallocation responsibilities for certain internal data structures (clarifications needed beyond basic rules).
6. Support for RTL C (SystemC) modeling on hardware side beyond Verilog/VHDL macros (mentioned as possible future).