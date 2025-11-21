Purpose & Scope
The SCE-MI standard provides a C/C++ interface for connecting untimed software models on a host workstation to a device under test (DUT) represented as a structural hardware netlist on an emulator or verification platform. It specifically addresses the need for a common interface to replace proprietary emulator APIs, enabling high-performance verification of SoC designs. The interface does not support event-based simulation or bridging software models to each other.

Product Background / Positioning
SCE-MI addresses critical industry problems with proprietary emulator APIs that restrict software portability and reduce verification productivity. Developed by a consortium of EDA customers and suppliers including Synopsys, Mentor Graphics, and Ikos Systems, it aims to become the standard interface for co-emulation verification, replacing legacy solutions like PLI.

Core Functional Overview
- Provides message-based communication channels between software models and hardware DUTs
- Supports bidirectional message flow with input and output channels
- Enables clock control for freezing time during message processing
- Offers parameterized message port widths and priorities
- Implements multi-clock support with configurable ratios and phases
- Includes infrastructure for binding software models to hardware components
- Provides C++ and C API interfaces for software side access

Key Users & Usage Scenarios
End users connect untimed testbenches to RTL DUTs with minimal effort, relying on transactor models to hide interface complexity. Transactor implementors create plug-and-play models for specific hardware interfaces. Infrastructure implementors provide SCE-MI implementations on verification platforms, enabling seamless co-emulation between software testbenches and hardware DUTs.

Major External Interfaces
Hardware side interfaces include message port macros (SceMiMessageInPort, SceMiMessageOutPort) and clock control macros (SceMiClockControl, SceMiClockPort). Software side interfaces consist of C++ and C APIs with message port proxy classes and binding methods. The interface requires infrastructure linkage to analyze bridge netlists and generate parameter files.

Key Non-functional Requirements
The interface must prevent communication bottlenecks with emulators, ensuring performance matches native emulator capabilities. It must maintain reliable message delivery between software and hardware sides. The interface must support multi-clock synchronization with precise alignment of clock edges across all controlled clocks.

Constraints, Assumptions & Dependencies
The interface depends on correct instantiation of hardware side macros within bridge netlists. It assumes end users will employ SystemC for untimed models. Infrastructure linkage must generate parameter files to bind software models to hardware components. The interface requires compatible emulation platforms supporting the SCE-MI infrastructure.

Priorities & Acceptance Approach
Highest priority is enabling untimed-to-RTL bridging with no performance degradation compared to proprietary interfaces. Second priority is robust multi-clock support with correct synchronization. Acceptance is validated by successful connection of untimed testbench to RTL DUT with message delivery and clock control functioning as specified.