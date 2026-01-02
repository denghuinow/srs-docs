**Purpose & Scope**: The system defines a standard C/C++ modeling interface (SCE-MI) to enable communication between untimed software models on a host workstation and a cycle-accurate hardware DUT model on an emulator, replacing proprietary APIs. The scope is restricted to the modeling interface specification, excluding features like debug or code coverage.

**Core Functions**:
*   Transport of untimed messages between software and hardware via configurable, bidirectional message channels.
*   Provide hardware-side interface macros (message ports, clock control, clock generation) for transactor and DUT integration.
*   Provide software-side C++/C API objects and methods for binding, sending, receiving messages, and servicing communication.
*   Support controlled clock generation and management, allowing transactors to stop DUT time for message processing.

**Key Users**: End users (integrating software testbenches with hardware DUTs), transactor implementors (creating abstraction bridge models), and SCE-MI infrastructure implementors (providing platform-specific implementations).

**Key Constraints**: The interface must be message/transaction-oriented (not event-oriented) to avoid communication bottlenecks that would throttle emulator performance. It must function in both single-threaded and multi-threaded software environments.