# Short Summary: Standard Co-Emulation Modeling Interface (SCE-MI)

## Background and objectives
The SCE-MI specification addresses the urgent need for a standardized, high-performance interface to bridge untimed software models (e.g., in SystemC) with structural hardware models (e.g., RTL/gate-level DUTs) on emulation platforms. It aims to solve proprietary API proliferation, enable plug-and-play verification solutions, and fully leverage emulation performance without communication bottlenecks.

## In scope
- Definition of hardware-side interface macros (message ports, clock control) for transactor integration.
- Software-side C++/C API for message port proxy binding, error handling, and service loop management.
- Message-oriented communication channels (not event-based) optimized for transaction abstraction.
- Support for multi-threaded and single-threaded software environments.
- Clock generation and control with configurable ratios, duty cycles, and reset semantics.

## Out of scope
- Debug, control, and code coverage features (future expansions of SCE-API).
- Interconnection of software models to each other (handled by environments like SystemC).
- Event-based or sub-cycle accurate simulation bridging.
- Implementation details of the infrastructure linker or physical transport layer.

## Stakeholders and core use cases
- **End users**: SoC design teams who integrate pre-built transactors and proxies to bridge testbenches with DUTs.
- **Transactor implementors**: IP providers who create transactor models and software proxies using SCE-MI macros/API.
- **SCE-MI infrastructure implementors**: EDA tool/emulator vendors who implement the hardware/software interface components.

**User stories:**
1. As an end user, I want to connect my untimed SystemC testbench to an RTL DUT on an emulator using vendor-supplied transactors so that I can verify at high speed without API lock-in.
2. As a transactor implementor, I want to use standardized message port macros and clock control to create abstraction gaskets so that my IP works across different emulation platforms.
3. As an infrastructure implementor, I want a clear functional spec for hardware macros and software API so that I can provide a compliant, high-performance implementation.
4. As an end user, I want to send multi-bit messages from software to hardware via input port proxies so that transactors can decompose them into cycle-accurate DUT events.
5. As an end user, I want to receive output messages from hardware via callbacks so that I can process DUT responses in my software testbench.
6. As a transactor implementor, I want to control DUT clock freezing during message composition/decomposition so that I can safely handle transaction abstraction.

## Success metrics
- Elimination of proprietary emulator API dependencies for software verification models.
- Achievement of high emulation performance without communication throttling.
- Adoption by multiple EDA vendors and end users as a common co-emulation standard.

## Major constraints
- Must avoid event-oriented communication that could bottleneck emulator performance.
- Must support both Verilog and VHDL hardware modeling languages.
- Must be compatible with multi-threaded environments like SystemC while also working in single-threaded C programs.
- Clock control must allow any transactor to freeze all controlled clocks globally.
- Parameter definitions (port widths, clock ratios, etc.) must be extractable from the hardware netlist by an infrastructure linker.

## Undecided issues
- Specific implementation details of the infrastructure linker and parameter file format.
- Future expansions for debug and control interfaces.
- Handling of more complex reset sequences beyond the default controlled reset.