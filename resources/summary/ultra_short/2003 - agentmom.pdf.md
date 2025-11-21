Purpose & Scope  
This system extends agentMom to enable secure broadcasting, multicasting, and unicast communication in multi-agent systems. It handles message delivery within local networks (broadcast), predefined agent groups (multicast), and direct agent pairs (unicast). It does not guarantee message delivery, provide advanced security beyond encryption, or support non-local network broadcasting.  

Product Background / Positioning  
The system integrates as a Java-based communication framework within multi-agent applications, building on agentMom 1.2. It replaces unicast-only communication with enhanced modes while maintaining compatibility with existing agentMom 1.2 implementations.  

Core Functional Overview  
- Broadcast messages to all agents in the local network.  
- Multicast messages to agents subscribed to a specific group address.  
- Unicast messages to individual agents within an organization.  
- Agent choice between broadcast, multicast, or unicast communication modes.  
- Join/leave multicast groups dynamically.  
- Toggle encryption for all message types.  
- Set multicast TTL and group addresses.  

Key Users & Usage Scenarios  
Users are Java developers with multi-agent systems experience. Agents must know destination addresses (unicast), multicast group addresses, or local network context to send messages. Scenarios include task completion notifications (multicast), new agent announcements (broadcast), and direct agent coordination (unicast).  

Major External Interfaces  
Requires TCP/IP for unicast, multicast protocol for group messaging, and UDP for broadcast. Interfaces with network infrastructure (routers, OS) supporting multicast and broadcast.  

Key Non-functional Requirements  
Multicast/broadcast packets delivered best-effort (no guarantee of delivery). Broadcast messages restricted to system administrators. Multicast requires network support (routers, OS, NIC).  

Constraints, Assumptions & Dependencies  
Multicast delivery depends on network infrastructure support. Broadcast restricted to administrators. Agents must know destination addresses for unicast and multicast groups. Security relies on basic encryption with no guarantee against decryption.  

Priorities & Acceptance Approach  
Must-haves: Core communication modes (broadcast/multicast/unicast), encryption toggle, group join/leave, and agent compatibility. Acceptance requires demonstration of all "driving requirements" (asterisked in SRS).