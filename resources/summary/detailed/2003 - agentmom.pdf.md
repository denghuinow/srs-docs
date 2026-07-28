# Detailed Summary

## Background and Scope
This project extends the agentMom multi-agent system framework to support broadcasting, multicasting, and secured communication capabilities. The goal is to enhance agent communication by providing flexible, one-to-many messaging options and basic encryption for sensitive exchanges. The scope includes implementing unicast, multicast, and broadcast message transmission, group management for multicast, and optional message encryption/decryption. Non-goals include guaranteeing reliable delivery for multicast/broadcast, providing unbreakable encryption, and modifying core agent logic beyond communication mechanisms.

## Stakeholders Matrix and Use Cases
*   **Project Advisor & Committee Members:** Review project requirements and deliverables for academic evaluation.
*   **Multi-Agent System Developer:** Uses the extended agentMom framework to build agents with enhanced communication capabilities.
*   **Agent (as a system actor):** Sends and receives messages using the new communication modes and manages group membership.

**Main Scenarios:**
1.  An agent sends a unicast message to a specific recipient (optionally encrypted).
2.  An agent sends a multicast message to all members of a subscribed group (optionally encrypted).
3.  An agent sends a broadcast message to all agents on the local network.
4.  An agent requests to join or leave a multicast group.

**Exception Scenarios:**
1.  An agent attempts to receive a multicast message without having joined the group (message is not delivered).
2.  Network or system constraints prevent multicast/broadcast message delivery (best-effort delivery fails).
3.  An encrypted message is received but decryption fails (message cannot be processed).

## Business Process
**Main Process: Agent Sends a Message**
1.  **Trigger:** An agent needs to communicate information.
2.  **Input:** Message content, destination specifier (agent address, group address, or broadcast flag), encryption flag.
3.  The agent selects communication mode (unicast, multicast, broadcast).
4.  If encryption is chosen and required keys are available, the message is encrypted.
5.  The framework transmits the message using the appropriate network protocol (TCP/IP, Multicast, UDP).
6.  The message traverses the network (subject to TTL for multicast).
7.  The destination agent(s) receive the message.
8.  **Output:** If the message was encrypted, it is decrypted automatically and delivered to the recipient agent's logic.

**Key Branch A: Join/Leave Multicast Group**
1.  **Trigger:** Agent needs to subscribe/unsubscribe from group messages.
2.  Agent sends a join/leave notification to the multicast address.
3.  The network multicast routing updates membership.
4.  The agent subsequently receives/stops receiving multicast messages for that group.

**Key Branch B: Secured Group Communication Setup**
1.  **Trigger:** Agents require a shared key for encrypted group communication.
2.  Agents request encryption/decryption keys from a designated key manager agent.
3.  The key manager verifies the requesting agent is authorized and provides the key.
4.  Agents use the shared key for subsequent encrypted multicast communication.

## Domain Model
*   **Agent:** (ID: unique, Name, NetworkAddress: required)
*   **Message:** (ID: unique, Content: required, SenderID: required/reference Agent, Timestamp: required)
*   **UnicastMessage:** (inherits Message, RecipientID: required/reference Agent)
*   **MulticastMessage:** (inherits Message, GroupAddress: required, TTL)
*   **BroadcastMessage:** (inherits Message)
*   **MulticastGroup:** (GroupAddress: unique/required, Port: required)
*   **EncryptionKey:** (KeyID: unique, KeyValue: required, AssociatedGroupAddress: reference MulticastGroup)

## Interfaces and Integrations
*   **Java Runtime Environment:** Internal, Required, Version 1.4.0.
*   **Network Stack (TCP/IP):** Internal, Outbound/Inbound, Unicast transmission. Input: Serialized message. Output: Network packets. SLA: Reliable, in-order delivery.
*   **Network Stack (Multicast Protocol):** Internal, Outbound/Inbound, Multicast transmission. Input: Serialized message & group address. Output: Multicast packets. SLA: Best-effort delivery, depends on network support.
*   **Network Stack (UDP):** Internal, Outbound/Inbound, Broadcast transmission. Input: Serialized message. Output: Broadcast packets. SLA: Best-effort delivery, may require admin privileges.
*   **Key Manager Agent:** External, Outbound/Inbound, Key distribution for secure multicast. Input: Key request. Output: Encryption key. SLA: Must maintain authorized agent list.

## Acceptance Criteria
**Capability: Multicast Communication**
*   Given an agent has joined a multicast group, When it sends a multicast message, Then all other agents in the same group receive the message.
*   Given an agent has not joined a multicast group, When a message is sent to that group, Then the agent does not receive the message.

**Capability: Secured Unicast**
*   Given two agents possess a shared key, When one sends an encrypted unicast message, Then the recipient receives and successfully decrypts the message.
*   Given an agent chooses not to encrypt a message, When it sends a unicast message, Then the message is transmitted in plain text.

## Non-Functional Metrics
*   **Performance:** Support sending/receiving messages concurrently from multiple agents. Multicast TTL should be configurable to control network scope.
*   **Reliability:** Unicast messages must be delivered reliably and in order; multicast/broadcast is best-effort.
*   **Security:** Provide mechanisms for message encryption and decryption (no strength guarantee).
*   **Compliance:** Framework must be compatible with existing agentMom 1.2 implementations.
*   **Observability:** Logging of major communication events (send, receive, join, leave, encrypt/decrypt status).

## Milestones and Release Strategy
1.  Finalize detailed design for communication modules and encryption integration.
2.  Implement and unit test unicast, multicast, and broadcast communication layers.
3.  Implement and test group join/leave management.
4.  Integrate and test optional message encryption/decryption feature.
5.  Conduct system integration testing with the core agentMom framework.
6.  Deliver final framework and demonstration to project committee.

## Risk List and Mitigation Strategies
1.  **Risk:** Multicast protocol not supported in target network environment.
    *   **Mitigation:** Document the requirement clearly; provide fallback to multiple unicasts for critical functions.
2.  **Risk:** Broadcast messages blocked by network policies (admin rights required).
    *   **Mitigation:** Use broadcast only for non-essential discovery; rely on multicast/unicast for core operations.
3.  **Risk:** Encryption mechanism is too weak or easily broken.
    *   **Mitigation:** Use standard, well-vetted encryption libraries; clearly document that security is "best-effort."
4.  **Risk:** Key management for secure multicast becomes a single point of failure.
    *   **Mitigation:** Design key manager agent for simplicity and reliability; document its critical role.
5.  **Risk:** Integration breaks compatibility with existing agentMom 1.2 agents.
    *   **Mitigation:** Maintain strict API backward compatibility; extensive compatibility testing.
6.  **Risk:** Increased network traffic from broadcast/multicast degrades system performance.
    *   **Mitigation:** Implement configurable TTL for multicast; advise developers to use broadcast sparingly.

## Undecided Issues and Responsible Parties
1.  **Specific encryption algorithm/library to be used.** (Responsible: Developer/Advisor)
2.  **Detailed API design for the new communication methods exposed to the agent developer.** (Responsible: Developer)
3.  **Mechanism for an agent to discover available multicast groups dynamically.** (Responsible: Developer)
4.  **Default TTL value for multicast messages.** (Responsible: Developer)
5.  **Handling of malformed or malicious messages (beyond encryption).** (Responsible: Developer/Advisor)
6.  **Detailed logging format and configuration.** (Responsible: Developer)