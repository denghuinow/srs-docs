**Purpose & Scope**: Defines a standard C/C++ modeling interface (SCE-MI) to connect untimed software models on a host workstation to a structural hardware netlist (DUT) on a verification platform via message channels.

**Core Functions**:
*   Provide multiple message channels between software proxies and hardware ports.
*   Enable transactors to decompose/compose messages into/from clocked events for the DUT.
*   Supply controlled clock generation and reset with transactor-managed clock control.

**Key Constraints**:
*   Interface must prevent communication bottlenecks that compromise emulator performance.
*   Hardware-side interface is defined by four specific, parametrized macros (MessageInPort, MessageOutPort, ClockPort, ClockControl).
*   Software-side API must provide C++ and C bindings for initialization, port proxy binding, message transfer, and a service loop function.