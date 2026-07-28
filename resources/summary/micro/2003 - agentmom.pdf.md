**Purpose & Scope**
Extend the agentMom multi-agent framework to support broadcast, multicast, and secured unicast communication.

**Core Functions**
*   Enable agents to send and receive unicast, multicast, and broadcast messages.
*   Allow agents to join and leave multicast groups.
*   Provide optional message encryption and decryption.

**Key Constraints**
*   Multicast/broadcast message delivery is best-effort, not guaranteed.
*   Network environment must support multicast protocol for multicast functionality.
*   The new framework must be compatible with the existing agentMom 1.2.