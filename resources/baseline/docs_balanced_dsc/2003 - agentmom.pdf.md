# Software Requirements Specification (SRS)
## Enhanced Communication Module for agentMom Framework
**Document Version:** 1.0  
**Date:** [Current Date]  
**Project:** agentMom Communication Extensions  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for extending the agentMom multi-agent framework (version 1.2) with broadcast, multicast, and secured unicast communication capabilities. The intended audience includes project stakeholders, developers, system administrators, and the project evaluation committee.

#### 1.2 Scope
This project extends the existing agentMom 1.2 framework by implementing reusable communication building blocks that support:
- **Broadcast Communication:** Agent-to-all-agent messaging within a local network segment.
- **Multicast Communication:** Efficient group-based messaging for dynamic agent collections.
- **Secured Unicast Communication:** Encrypted point-to-point messaging for sensitive communications.

The enhancements will maintain backward compatibility with existing agentMom 1.2 agent implementations. The system is implemented in Java and is intended for developers building distributed multi-agent systems.

#### 1.3 Definitions, Acronyms, and Abbreviations
- **agentMom:** The base multi-agent framework being extended.
- **MAS:** Multi-Agent System.
- **Unicast:** One-to-one directed communication.
- **Multicast:** One-to-many communication to a subscribed group.
- **Broadcast:** One-to-all communication within a network boundary.
- **TTL:** Time-To-Live for network packets.
- **TCP/IP:** Transmission Control Protocol/Internet Protocol.
- **UDP:** User Datagram Protocol.

#### 1.4 References
- agentMom Framework Documentation, Version 1.2
- Java Platform, Standard Edition Documentation, Version 1.4.0
- IETF RFC 1112 - Host Extensions for IP Multicasting

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product and its operating environment. Section 3 details specific requirements, including functional requirements, data models, and non-functional constraints. Appendices may include supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
This project is an enhancement module that integrates with the existing agentMom 1.2 framework. It operates as a middleware communication layer, sitting between the core agent logic and the underlying network transport.

#### 2.2 Product Functions
The enhanced framework shall provide the following high-level functions:
1.  Manage agent communication endpoints for unicast, multicast, and broadcast.
2.  Facilitate dynamic creation, joining, and leaving of multicast groups.
3.  Provide mechanisms for sending and receiving messages via the three communication patterns.
4.  Enable optional encryption and decryption of unicast messages.
5.  Maintain registry of agents, groups, and security keys.

#### 2.3 User Characteristics
- **Multi-Agent System Developers:** Proficient in Java and the agentMom API. They will use the new communication primitives to build agent behaviors.
- **System Administrators:** Responsible for configuring the network environment (e.g., enabling multicast routing, setting firewall permissions) to support the framework's operation.

#### 2.4 Constraints
1.  Must maintain compatibility with the public API of agentMom 1.2.
2.  Must operate within the Java 1.4.0 runtime environment.
3.  Dependent on underlying network infrastructure supporting IP multicast for full functionality.
4.  Broadcast communication may require specific system/network administrator privileges.

#### 2.5 Assumptions and Dependencies
- It is assumed that the network environment can be configured to support IP multicast if that feature is required by the application.
- The project assumes the continued existence and stability of the core agentMom 1.2 framework.
- External libraries for cryptography (if not implemented manually) must be compatible with Java 1.4.0.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Agent Communication Management
- **FR-1: Agent Initialization.** Upon startup, an agent shall initialize and register its communication interfaces (unicast socket, multicast sockets for subscribed groups).
- **FR-2: Message Transmission Decision.** The framework shall provide an API for the agent developer to specify the destination and let the framework select the appropriate protocol (Unicast/TCP, Multicast, Broadcast/UDP).
- **FR-3: Message Distribution.**
    - **FR-3.1:** Shall send unicast messages over a reliable TCP/IP connection.
    - **FR-3.2:** Shall send multicast messages to a specified IP multicast group address and port using UDP.
    - **FR-3.3:** Shall send broadcast messages to the local network broadcast address using UDP.
- **FR-4: Message Reception.** The framework shall listen on configured ports, receive incoming messages, and place them in a queue for the agent to process.

##### 3.1.2 Multicast Group Management
- **FR-5: Group Join.** An agent shall be able to join a multicast group by specifying a group address and port.
- **FR-6: Group Leave.** An agent shall be able to leave a multicast group.
- **FR-7: Group Notification.** The framework shall notify existing group members (via multicast) when a new agent joins or leaves, subject to encryption settings.

##### 3.1.3 Security
- **FR-8: Encryption Selection.** The agent developer shall be able to flag a unicast message for encryption before transmission.
- **FR-9: Secure Message Preparation.** When encryption is selected, the framework shall encrypt the message content using a shared key associated with the recipient agent or its organization before transmission.
- **FR-10: Secure Message Processing.** Upon receipt of a message with an encryption flag, the framework shall automatically attempt to decrypt it using available keys from the local `EncryptionKeyRegistry`.
- **FR-11: Key Management.** The framework shall provide an interface for managing (adding, removing, rotating) encryption keys in the local `EncryptionKeyRegistry`.

##### 3.1.4 Compatibility
- **FR-12: Backward Compatibility.** All existing agent implementations built for agentMom 1.2 that use standard unicast communication shall continue to function without modification.

#### 3.2 Use Cases / User Stories
The following user stories from the project summary are formalized as requirements:
1.  **US-1 (Broadcast Announcement):** *Implemented by FR-3.3.*
2.  **US-2 (Multicast Notification):** *Implemented by FR-3.2 and FR-5.*
3.  **US-3 (Secure Unicast):** *Implemented by FR-8, FR-9, FR-10.*
4.  **US-4 (Dynamic Group Management):** *Implemented by FR-5, FR-6, FR-7.*
5.  **US-5 (Encryption Choice):** *Implemented by FR-8.*
6.  **US-6 (Compatibility):** *Implemented by FR-12.*

#### 3.3 Data Models

##### 3.3.1 Class: `Agent`
- **Primary Key:** `AgentID` (String)
- **Attributes:**
    - `name` (String)
    - `capabilities` (List\<String>)
    - `organization` (OrgID)
    - `currentGroups` (List\<GroupAddress>)
    - `encryptionKeys` (Map\<KeyID, KeyValue>)

##### 3.3.2 Class: `Message`
- **Primary Key:** `MessageID` (UUID)
- **Attributes:**
    - `sender` (AgentID)
    - `recipients` (List\<AgentID> | GroupAddress | "BROADCAST")
    - `content` (Serializable Object)
    - `encryptionFlag` (Boolean)
    - `protocolType` (Enum: UNICAST, MULTICAST, BROADCAST)

##### 3.3.3 Class: `MulticastGroup`
- **Primary Key:** `GroupAddress` (InetAddress)
- **Attributes:**
    - `port` (int)
    - `timeToLive` (int) // Scope for multicast packets
    - `memberAgents` (Set\<AgentID>)
    - `encryptionKey` (KeyValue) // Optional, for group-level security

##### 3.3.4 Supporting Registries
- `OrganizationRegistry`: Maps `OrgID` to organizational structure and members.
- `NetworkConfiguration`: Stores `BroadcastAddress` and `MulticastSupport` flag.
- `EncryptionKeyRegistry`: Maps `KeyID` to `KeyValue`, `AuthorizedAgents`, and `ExpirationTime`.

#### 3.4 Non-Functional Requirements

1.  **NFR-1 (Compatibility):** The system shall be fully compatible with the agentMom 1.2 API. Existing agent code must not require changes.
2.  **NFR-2 (Delivery Semantics):** Multicast and broadcast messages shall be delivered on a *best-effort* basis. The framework does not guarantee delivery.
3.  **NFR-3 (Security Level):** The implemented encryption shall provide *basic confidentiality* for unicast messages but does not guarantee protection against determined, sophisticated attacks (e.g., it is not FIPS 140-2 compliant).
4.  **NFR-4 (Network Dependency):** Full multicast functionality is dependent on the host and network infrastructure supporting IP multicast (IGMP).
5.  **NFR-5 (Permissions):** Transmitting broadcast messages may require the application to have system/network administrator privileges, as dictated by the host OS.
6.  **NFR-6 (Platform):** The system shall run on any system with a Java 1.4.0 or later runtime environment (JRE).

#### 3.5 Design Constraints
- The implementation must use Java 1.4.0 compatible APIs (e.g., `java.net`, `java.security`).
- Multicast communication must be implemented using `java.net.MulticastSocket`.

#### 3.6 External Interface Requirements
- **Software Interface:** The extension shall integrate seamlessly with the `agentmom.agent` and `agentmom.message` base packages.
- **Communication Interface:** The system shall use standard IP protocols: TCP port [TBD] for unicast, UDP ports [TBD] for multicast/broadcast.
- **User Interface:** No graphical user interface is required. Configuration shall be file-based (properties file) or API-driven.

### 4. Appendices

#### 4.1 Risk Management
| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| Multicast not supported by network | Medium | High | Implement fallback logic to simulate multicast via multiple unicast messages. |
| Broadcast messages blocked | Low | Medium | Provide an alternative discovery protocol (e.g., a well-known unicast registry agent). |
| Encryption key compromise | Low | High | Implement key rotation mechanisms and key validity periods in the `EncryptionKeyRegistry`. |
| Loss of multicast/broadcast messages | High | Medium | Document the best-effort nature clearly. For critical notifications, recommend application-level acknowledgment protocols. |
| Performance degradation from encryption | Medium | Low | Ensure encryption is optional (FR-8). Profile and optimize cryptographic operations. |

#### 4.2 Open Issues
The following issues require resolution during the design phase:
1.  Selection of specific encryption algorithms (e.g., DES, 3DES, Blowfish) compatible with JCE in Java 1.4.
2.  Mechanism for secure distribution of shared keys for both unicast and multicast scenarios.
3.  Determination of default TTL values for multicast messages to control network scope.
4.  Strategy for handling network partitions (e.g., a multicast group member loses connectivity).
5.  Policy for handling message priority when an agent is involved in multiple simultaneous communication patterns.
6.  Detailed error recovery procedures (e.g., retry logic for failed unicast, handling of malformed encrypted messages).

---
*This document provides the foundation for the design, implementation, and testing of the agentMom communication enhancements.*