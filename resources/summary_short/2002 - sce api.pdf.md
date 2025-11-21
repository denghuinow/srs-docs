# Short Summary

- **Background and objectives**: This document proposes the Standard Co-Emulation Modeling Interface (SCE-MI) to address the need for a high-performance, multichannel communication interface between software models on a host workstation and hardware models (DUT) on emulators or verification platforms, overcoming proprietary API limitations and enabling efficient system-level verification.

- **In scope**:
  - Specification of hardware-side interface macros (message ports, clock control).
  - Software-side C++ and C APIs for message port proxy binding and communication.
  - Infrastructure linkage process for parameter derivation and hardware compilation.
  - Support for multi-threaded and single-threaded software environments.
  - Controlled and uncontrolled clock semantics for time management.

- **Out of scope**:
  - Event-based or sub-cycle accurate simulation bridging.
  - Interconnection of software models to each other (handled by environments like SystemC).
  - Debug, control, and code coverage features (potential future expansions).
  - Implementation details of SCE-MI infrastructure components.
  - Specific data structures for message serialization/deserialization.

- **Roles and core use cases**:
  - As an **end user**, I want to bridge untimed software testbenches to RTL hardware models so that I can verify designs without detailed SCE-MI knowledge.
  - As a **transactor implementor**, I want to create plug-and-play transactor and proxy models using SCE-MI interfaces so that end users can easily connect abstraction levels.
  - As an **SCE-MI infrastructure implementor**, I want to provide compliant SCE-MI implementations on verification platforms so that customers achieve high-performance co-modeling.

- **Success metrics**:
  - Elimination of communication bottlenecks that throttle emulator performance.
  - Compatibility with multi-threaded environments like SystemC without inherent API limitations.
  - Industry adoption as a common standard for emulation interfaces.

- **Major constraints**:
  - Must avoid proprietary API dependencies to encourage third-party tool integration.
  - Interface must not inherently slow down emulators due to communication overhead.
  - Support for multiple controlled clocks with configurable ratios, duty cycles, and phases.
  - Hardware-side macros must be empty shells with defined ports/parameters for implementation flexibility.
  - Error handling must support both traditional and callback-based approaches for fatal errors.

- **Undecided issues**:
  - Specific parameter file format for infrastructure linkage (implementation-defined).
  - Additional SCE-API parts for debug, control, or coverage (future expansions).
  - Default values and overrides for implementation-specific parameters (tool-dependent).
  - Handling of non-fatal errors and warnings beyond the defined info callback.
  - Not mentioned: Long-term evolution and versioning strategy for the standard.