**Purpose & Scope**: Extend the agentMom multi-agent system framework to support broadcast, multicast, and secured communication capabilities.

**Core Functions**:
*   Enable agents to send and receive unicast messages.
*   Enable agents to send and receive multicast messages, including joining/leaving groups.
*   Enable agents to send and receive broadcast messages within a local network.
*   Provide message encryption and decryption for unicast and multicast communication.

**Key Users**: Developers implementing multi-agent systems who have knowledge of Java, object-oriented programming, and Multi-Agent Systems Engineering.

**Key Constraints**:
*   Multicast and broadcast message delivery is best-effort and not guaranteed.
*   Network infrastructure must support multicast protocol.
*   System administrator privileges may be required to send broadcast messages.