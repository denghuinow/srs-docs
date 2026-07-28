**Purpose & Scope**
The system extends the agentMom multi-agent framework to support broadcast, multicast, and secured unicast communication. It provides a reusable Java framework for building agents and their conversations. It does not guarantee reliable delivery for multicast/broadcast, provide unbreakable encryption, or function in network environments lacking multicast protocol support.

**Product Background / Positioning**
This is an enhancement to the existing agentMom 1.2 framework. It operates within a multi-agent system context, providing the foundational communication building blocks upon which specific agent applications are built.

**Core Functional Overview**
*   Enable agents to send and receive unicast messages within an organization.
*   Enable agents to send and receive broadcast messages within a local network.
*   Enable agents to send and receive multicast messages within a subscribed group.
*   Allow agents to join and leave multicast groups.
*   Provide message encryption and decryption for unicast and multicast communication.
*   Allow an agent to choose whether to encrypt a given message.
*   Maintain compatibility with the existing agentMom 1.2 framework.

**Key Users & Usage Scenarios**
The primary users are developers implementing multi-agent systems, requiring knowledge of Java and agent concepts. Agents communicate directly (unicast), announce themselves to a local network (broadcast), or efficiently communicate with a defined subgroup (multicast), with optional message encryption.

**Major External Interfaces**
The system interfaces via standard network protocols: TCP/IP for unicast, UDP for broadcast, and IP Multicast protocol for multicast. It requires a Java 1.4.0 runtime environment.

**Key Non-functional Requirements**
*   Unicast messages must arrive at the specified address and in order.
*   Multicast/broadcast message delivery is on a best-effort basis (no reliability guarantee).
*   The system must be compatible with agentMom 1.2.
*   Network routers, cards, and OS must support the multicast protocol for that feature to work.
*   System administrator privileges may be required to send broadcast messages on many networks.

**Constraints, Assumptions & Dependencies**
*   Each agent must know destination addresses for unicast and multicast addresses for group communication.
*   For secured multicast, a trusted key management agent must exist to distribute encryption keys.
*   The framework assumes agents have the knowledge to choose the appropriate communication method.

**Priorities & Acceptance Approach**
Driving requirements (marked in the SRS) must be demonstrated by the end of phase II. These include core send/receive functions for all communication types, join/leave group operations, basic encryption/decryption, and architectural support. Acceptance will involve demonstrating these capabilities.