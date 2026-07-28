# Short Summary: Applying Broadcasting/Multicasting/Secured Communication to agentMom in Multi-Agent Systems

## Background and Objectives
This project aims to extend the agentMom multi-agent framework by adding broadcasting, multicasting, and secured communication capabilities. The objective is to enhance agent communication flexibility and security while maintaining compatibility with the existing agentMom 1.2 system.

## In Scope
- Implementing unicast, multicast, and broadcast communication methods for agents.
- Providing message encryption and decryption for secure communication.
- Enabling agents to join and leave multicast groups dynamically.
- Supporting both agent-controlled and component-controlled conversation architectures.
- Ensuring backward compatibility with agentMom 1.2.

## Out of Scope
- Guaranteeing reliable delivery of multicast/broadcast messages (best-effort only).
- Providing unbreakable encryption security.
- Supporting multicast in environments without multicast protocol support.
- Allowing broadcast messages without system administrator privileges.
- Managing agent knowledge about destination addresses or communication decisions.

## Stakeholders and Core Use Cases
**Stakeholders:**
- **Project Advisor/Committee Members:** Review and evaluate the project requirements and implementation.
- **Multi-Agent System Developers:** Use the extended framework to build agent-based applications with enhanced communication capabilities.
- **System Administrators:** Configure network environments to support multicast/broadcast communication requirements.

**Core Use Cases:**
1. As a developer, I want agents to send unicast messages so that they can communicate directly with specific agents.
2. As a developer, I want agents to send multicast messages to groups so that they can efficiently communicate with multiple agents simultaneously.
3. As a developer, I want agents to send broadcast messages so that they can announce their presence to all agents in the local network.
4. As a developer, I want agents to encrypt messages so that communication remains secure from unauthorized access.
5. As a developer, I want agents to join/leave multicast groups so that they can dynamically reorganize based on mission requirements.
6. As a developer, I want to use the enhanced framework so that I can maintain compatibility with existing agentMom 1.2 applications.

## Success Metrics
- Successful demonstration of all driving requirements marked with "*" in the specification.
- Maintenance of backward compatibility with agentMom 1.2.
- Support for all three communication methods (unicast, multicast, broadcast) with optional encryption.

## Major Constraints
- Multicast/broadcast messages are delivered with best effort only (no delivery guarantees).
- Basic encryption mechanisms are provided without guarantees against decryption by unauthorized parties.
- Multicast protocol support depends on network environment configuration.
- Broadcast message sending often requires system administrator privileges.
- Each agent must know destination addresses for unicast and multicast addresses for group communication.

## Undecided Issues
- Specific encryption algorithms and key management implementation details.
- Default Time-To-Live (TTL) values for multicast messages.
- Handling of network configuration variations across different deployment environments.
- Performance implications of encryption on different communication methods.
- Error handling strategies for failed multicast/broadcast deliveries.