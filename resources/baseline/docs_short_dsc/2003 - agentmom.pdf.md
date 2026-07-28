# Software Requirements Specification (SRS)
## Project: Enhanced Communication for agentMom Multi-Agent Framework
**Version:** 1.0
**Date:** October 26, 2023
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the requirements for extending the agentMom 1.2 multi-agent framework to include broadcasting, multicasting, and secured communication capabilities. It is intended for stakeholders, developers, and system administrators involved in the project's specification, implementation, and deployment.

#### 1.2 Scope
This project will enhance the agentMom framework by implementing three new communication paradigms (unicast, multicast, broadcast) with optional encryption, while ensuring full backward compatibility with existing agentMom 1.2 applications. The scope is limited to providing the communication mechanisms; it does not include guarantees of delivery, unbreakable security, or management of agent addressing logic.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **agentMom:** The existing multi-agent system framework, version 1.2.
*   **Unicast:** Point-to-point communication between two specific agents.
*   **Multicast:** One-to-many communication where a message is sent to a defined group of agents.
*   **Broadcast:** One-to-all communication where a message is sent to all agents reachable on the local network segment.
*   **TTL (Time-To-Live):** A counter or timestamp that limits the lifespan or reach of a packet in a network.
*   **SRS:** Software Requirements Specification.

#### 1.4 References
*   agentMom 1.2 Framework Documentation.
*   RFC 1112 - Host Extensions for IP Multicasting.
*   Project Charter: "Applying Broadcasting/Multicasting/Secured Communication to agentMom."

#### 1.5 Overview
The remainder of this SRS is organized as follows: Section 2 provides a general description of the product. Section 3 details the specific requirements, including functional, interface, and non-functional requirements.

### 2. Overall Description

#### 2.1 Product Perspective
This project is an extension module for the existing agentMom 1.2 framework. It integrates as a new communication layer, augmenting the framework's capabilities without altering its core architecture or breaking existing agent functionality.

#### 2.2 Product Functions
The enhanced framework shall:
1.  Enable agents to send and receive unicast messages.
2.  Enable agents to send messages to multicast groups and receive messages from groups they have joined.
3.  Enable agents to send broadcast messages to the local network.
4.  Provide mechanisms for encrypting message content before transmission and decrypting it upon receipt.
5.  Allow agents to dynamically join and leave multicast groups at runtime.
6.  Maintain the existing agentMom 1.2 API and functionality without modification.

#### 2.3 User Characteristics
*   **Multi-Agent System Developers:** Proficient in Java and the agentMom framework. They require clear APIs to utilize new communication modes.
*   **System Administrators:** Responsible for configuring the network environment (e.g., enabling multicast routing, granting broadcast privileges) to support the framework's operation.
*   **Project Advisors:** Technical evaluators who will assess the project against the stated requirements and success metrics.

#### 2.4 Constraints
1.  **Best-Effort Delivery:** Multicast and broadcast messages are delivered on a best-effort basis; reliable, guaranteed delivery is **out of scope**.
2.  **Security Limitation:** The provided encryption is a basic mechanism. The framework does **not** guarantee protection against determined, sophisticated attacks.
3.  **Network Dependency:** Multicast functionality requires underlying network and OS support. The framework will not emulate multicast in unsupported environments.
4.  **Privilege Requirement:** Sending broadcast messages may require the application/agent to possess system administrator privileges, depending on the OS.
5.  **Agent Addressing:** The agent developer is responsible for providing correct destination addresses (for unicast) or multicast group addresses.

#### 2.5 Assumptions and Dependencies
*   It is assumed the deployment environment's network is correctly configured by a system administrator to support the desired communication methods (especially multicast).
*   The project depends on the continued stability and availability of the base agentMom 1.2 framework.
*   Java Cryptography Architecture (JCA) libraries are available for encryption implementation.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Communication Methods
*   **FR-1 (UC-1): Unicast Communication*** <br>
    The system shall provide an API for an agent to send a message to a single, specifically addressed recipient agent.
*   **FR-2 (UC-2): Multicast Communication*** <br>
    The system shall provide an API for an agent to send a message to all agents currently joined to a specified multicast group address.
*   **FR-3 (UC-3): Broadcast Communication*** <br>
    The system shall provide an API for an agent to send a message to all agents reachable on the local network subnet.
*   **FR-4 (UC-5): Dynamic Group Management*** <br>
    The system shall provide APIs for an agent to join and leave a specified multicast group address during its lifecycle.

##### 3.1.2 Security Features
*   **FR-5 (UC-4): Message Encryption*** <br>
    The system shall provide an option to encrypt the payload of any message (unicast, multicast, or broadcast) before transmission using a configurable encryption algorithm.
*   **FR-6 (UC-4): Message Decryption** <br>
    The system shall automatically decrypt an incoming encrypted message if the receiving agent possesses the correct decryption key.

##### 3.1.3 Compatibility & Architecture
*   **FR-7 (UC-6): Backward Compatibility*** <br>
    The enhanced framework shall be fully backward compatible. All existing applications built for agentMom 1.2 shall compile and run without modification using the new version.
*   **FR-8: Architecture Support** <br>
    The system shall support both agent-controlled and component-controlled conversation architectures as defined in the base agentMom framework.

#### 3.2 Interface Requirements

##### 3.2.1 Software Interfaces
*   **SI-1:** The extension shall integrate seamlessly with the `agent.comm.Communication` class (or equivalent) of agentMom 1.2.
*   **SI-2:** New methods shall be added to the agent API, such as:
    ```java
    sendUnicast(AgentAddress dest, Message msg, boolean encrypt);
    sendMulticast(InetAddress group, Message msg, boolean encrypt);
    sendBroadcast(Message msg, boolean encrypt);
    joinMulticastGroup(InetAddress group);
    leaveMulticastGroup(InetAddress group);
    ```

##### 3.2.2 Hardware Interfaces
*   **HI-1:** The system requires standard network hardware (NIC, switches, routers). Multicast support requires routers configured for IGMP.

##### 3.2.3 Communications Interfaces
*   **CI-1:** Unicast shall use standard TCP or UDP point-to-point sockets.
*   **CI-2:** Multicast shall use IP multicast (UDP) as per RFC 1112.
*   **CI-3:** Broadcast shall use local IP broadcast (UDP).
*   **CI-4:** The system shall use a configurable port range for communication, defaulting to the port used by agentMom 1.2.

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance
*   **PER-1:** The overhead of optional encryption shall be documented for each communication type (unicast, multicast, broadcast).
*   **PER-2:** Multicast group join/leave operations shall complete within 100ms in a standard local network environment.

##### 3.3.2 Security
*   **SEC-1:** Encryption keys shall not be stored in plaintext within configuration files.
*   **SEC-2:** The system shall log attempts to send messages to invalid or unauthorized multicast addresses.

##### 3.3.3 Reliability & Availability
*   **REL-1:** The failure of a multicast/broadcast message delivery shall not crash the sending agent or the framework. Errors shall be logged.
*   **REL-2:** The unicast communication channel shall maintain the same level of reliability as in agentMom 1.2.

##### 3.3.4 Usability
*   **USA-1:** The new APIs shall be documented with Javadoc, including code examples for all core use cases.
*   **USA-2:** Configuration parameters for encryption and multicast TTL shall have sensible defaults and be easily adjustable.

### 4. Appendices

#### 4.1 Undecided Issues & Open Questions
The following items require further design decisions:
1.  **Encryption Algorithm:** Selection of default symmetric encryption algorithm (e.g., AES) and key exchange mechanism.
2.  **Multicast TTL:** Determination of a default TTL value for multicast packets and a configuration strategy for different network topologies.
3.  **Network Configuration Handling:** Strategy for detecting and reporting unsupported network configurations (e.g., multicast not enabled).
4.  **Performance Trade-offs:** Detailed analysis of the performance impact of encryption on high-frequency multicast messaging.
5.  **Error Handling:** Specific strategy for notifying agents of failed best-effort deliveries (e.g., callback, logged event).

#### 4.2 Success Metrics Validation
The project will be deemed successful upon the demonstration of the following:
1.  All functional requirements marked with an asterisk (*) are implemented and operational.
2.  A legacy agentMom 1.2 application executes without error or modification on the enhanced framework.
3.  A test suite successfully demonstrates agents using unicast, multicast, and broadcast communication, with and without encryption.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| System Architect | | | |