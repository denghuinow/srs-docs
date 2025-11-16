# Balanced Summary

**Goals and Scope**  
The SCE-MI standard aims to provide a high-performance, multichannel communication interface between software models on a host workstation and hardware models (e.g., RTL netlists) running on emulation platforms. It addresses the need for a common API to replace proprietary emulator interfaces, enabling plug-and-play verification solutions and improving productivity for SoC design teams.

**Roles and User Stories**  
- *End User*: I want to bridge untimed software testbenches with RTL DUTs using pre-built transactors so that I can verify designs without SCE-MI implementation details.  
- *Transactor Implementor*: I want to create abstraction gaskets using SCE-MI macros and proxies so that end users can easily connect models across abstraction levels.  
- *Infrastructure Implementor*: I want to provide compliant SCE-MI implementations for specific verification platforms so that customers can use standardized co-emulation.  
- *Software Developer*: I want to bind message port proxies and handle callbacks so that my C++/SystemC models can communicate with hardware.  
- *Hardware Designer*: I want to instantiate SCE-MI macros in transactors so that I can control clocks and transfer messages to/from software.

**Key Processes**  
1. *Trigger: Infrastructure linkage* – Analyze hardware netlist to extract SCE-MI parameters (e.g., clocks, ports).  
2. *Trigger: Software initialization* – Initialize SCE-MI using parameters file and bind message port proxies.  
3. *Trigger: Simulation start* – Transactors decompose input messages into cycle-accurate DUT events.  
4. *Trigger: Output events* – Transactors compose DUT events into messages for software.  
5. *Trigger: ServiceLoop call* – Dispatch arriving messages and input-ready notifications via callbacks.  
6. *Trigger: Clock control* – Transactors freeze controlled time during message processing.  
7. *Trigger: Shutdown* – Gracefully terminate co-modeling session and release resources.

**Domain Data Elements**  
- *MessageInPort* (Primary Key: PortName; Fields: TransactorName, PortWidth, ReceiveReady, TransmitReady, Message)  
- *MessageOutPort* (Primary Key: PortName; Fields: TransactorName, PortWidth, PortPriority, TransmitReady, ReceiveReady, Message)  
- *ClockPort* (Primary Key: ClockName; Fields: ClockNum, RatioNumerator, RatioDenominator, DutyHi, DutyLo, Phase, ResetCycles)  
- *ClockControl* (Primary Key: ClockNum; Fields: Uclock, Ureset, ReadyForCclock, CclockEnabled)  
- *Transactor* (Primary Key: TransactorName; Fields: AssociatedClockNums, ContainedPorts)  
- *MessageData* (Primary Key: N/A; Fields: PayloadBits, CycleStamp, WidthInBits)

**Non-Functional Requirements**  
- High-performance message transport to avoid emulator bottlenecks.  
- Compatibility with multi-threaded environments (e.g., SystemC).  
- Support for multiple controlled clocks with configurable ratios/duty cycles.  
- Error handling via callbacks or status returns for fatal errors.  
- Modular transactor design for abstraction bridging.  
- Portable C/C++ API with consistent memory allocation semantics.

**Milestones and External Dependencies**  
- Infrastructure linker must generate parameters file from hardware netlist.  
- Software models must link with SCE-MI library and call ServiceLoop periodically.  
- Emulator/platform must support SCE-MI hardware-side component integration.  
- Relies on SystemC or similar environment for untimed software modeling.  
- Requires standardized macro definitions for Verilog/VHDL.

**Risks and Mitigation Strategies**  
- *Risk*: Proprietary API fragmentation limits adoption. *Mitigation*: Industry consortium to maintain standard.  
- *Risk*: Inefficient message transport throttles emulator performance. *Mitigation*: Transaction-oriented (not event-oriented) channels.  
- *Risk*: Clock domain mismatches cause synchronization errors. *Mitigation*: Explicit clock control handshakes and alignment rules.  
- *Risk*: Software-hardware binding failures. *Mitigation*: Name-based rendezvous with detailed error reporting.  
- *Risk*: Transactor complexity hinders usability. *Mitigation*: Pre-built transactor IP for common protocols.

**Undecided Issues**  
- Debug and control interface extensions (future SCE-API parts).  
- Code coverage integration methods.  
- Specific physical layer implementation for message transport.  
- Tool support for deriving clock ratios from frequencies.  
- Handling of non-fatal errors in info callback semantics.  
- Not mentioned: Long-term evolution process for the standard.