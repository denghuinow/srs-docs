# Software Requirements Specification (SRS)
## For the agentMom Communication Extension Module

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for extending the **agentMom** multi-agent system framework. The primary purpose is to augment the framework's communication layer with **broadcast**, **multicast**, and **secured communication** capabilities, thereby enabling more flexible and robust interaction patterns among distributed software agents.

#### 1.2 Scope
This project will extend the existing agentMom framework (assumed to have basic agent lifecycle management and unicast communication) by implementing new communication primitives and a security layer. The extension will be delivered as an integrated module within the framework's core communication package.

**In-Scope:**
*   Design and implementation of APIs for broadcast, multicast, and secure unicast/multicast messaging.
*   Management of multicast group membership (join/leave).
*   Provision of symmetric encryption/decryption utilities for message payloads.
*   Documentation and example code for the new features.

**Out-of-Scope:**
*   Modification of existing agent lifecycle management or core scheduling logic.
*   Guaranteed delivery protocols for multicast/broadcast.
*   Public Key Infrastructure (PKI) or asymmetric encryption.
*   Communication across wide-area networks (WAN) or over the public internet.
*   Graphical user interfaces or administrative tools.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **agentMom**: The existing Java-based multi-agent system framework being extended.
*   **Agent**: An autonomous software entity within the agentMom framework.
*   **Unicast**: Point-to-point message transmission to a single, specific agent.
*   **Multicast**: One-to-many message transmission to a defined group of agents.
*   **Broadcast**: One-to-all message transmission to all reachable agents on a local network segment.
*   **Best-Effort Delivery**: The network will attempt to deliver the message but does not guarantee success, order, or duplicate prevention.
*   **SRS**: Software Requirements Specification.

#### 1.4 References
*   agentMom Framework Core Documentation (Assumed).
*   Java Platform, Standard Edition (Java SE) API Specification.
*   RFC 1112 - Host Extensions for IP Multicasting.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its user characteristics, and constraints. Section 3 details the specific functional and non-functional requirements.

### 2. Overall Description

#### 2.1 Product Perspective
This extension is a new module within the agentMom framework. It will interact with the existing **MessageDispatcher** or equivalent component to handle outgoing and incoming messages using new protocols (UDP Multicast/Broadcast) alongside existing ones (e.g., TCP/UDP Unicast). The security features will act as a middleware layer, encrypting payloads before transmission and decrypting them upon receipt.

#### 2.2 Product Functions
The high-level functions of the extension are:
1.  **Unicast Messaging Enhancement:** Integrate security into existing unicast pathways.
2.  **Multicast Messaging:** Enable agents to send to and receive from multicast groups, with dynamic membership management.
3.  **Broadcast Messaging:** Enable agents to send and receive broadcast messages within their local subnet.
4.  **Message Security:** Provide a simple API for agents to encrypt and decrypt message content using a shared secret key for relevant communication types.

#### 2.3 User Characteristics
The primary users of this extension are **Software Developers** with the following expertise:
*   Proficient in Java programming and object-oriented design.
*   Familiar with concurrent and distributed systems concepts.
*   Understanding of basic Multi-Agent Systems (MAS) engineering principles.
*   Working knowledge of network programming (sockets, protocols) is beneficial but not mandatory, as the API will abstract lower-level details.

#### 2.4 Constraints
1.  **Delivery Guarantee:** Multicast and broadcast message delivery is **best-effort**. The framework will not implement reliable delivery protocols (e.g., acknowledgments, retransmissions) for these message types.
2.  **Network Infrastructure:** Successful multicast operation requires that the underlying network hardware (routers, switches) and host operating systems support and are configured for the IP multicast protocol (IGMP).
3.  **Operating System Privileges:** On some operating systems (e.g., Unix-based systems), sending raw socket broadcasts may require the application or user to have **system administrator (root) privileges**.
4.  **Framework Dependency:** This module is entirely dependent on the existing agentMom framework architecture and cannot operate as a standalone library.

#### 2.5 Assumptions and Dependencies
*   It is assumed the base agentMom framework provides a stable API for agent registration, message passing hooks, and agent addressing (e.g., Agent ID).
*   The development and runtime environment is Java SE 8 or later.
*   Target deployment environments have compatible Java Runtime Environments (JREs) and network permissions as outlined in constraints.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Unicast Communication
*   **FR-UC-1:** The system shall provide an API for an agent to send a unicast message to another specific agent identified by a unique address (e.g., `AgentID`).
*   **FR-UC-2:** The system shall deliver incoming unicast messages to the intended recipient agent via its standard message handling method.

##### 3.1.2 Multicast Communication
*   **FR-MC-1:** The system shall provide an API for an agent to join a named multicast group.
    ```java
    // Example API Signature
    boolean joinMulticastGroup(String groupName);
    ```
*   **FR-MC-2:** The system shall provide an API for an agent to leave a named multicast group.
    ```java
    // Example API Signature
    boolean leaveMulticastGroup(String groupName);
    ```
*   **FR-MC-3:** The system shall provide an API for an agent to send a message to all members of a specified multicast group.
*   **FR-MC-4:** The system shall deliver messages sent to a multicast group to all local agents that are currently members of that group.
*   **FR-MC-5:** The system shall map logical `groupName` to a valid IP multicast address (e.g., within the administratively scoped 239.x.x.x range).

##### 3.1.3 Broadcast Communication
*   **FR-BC-1:** The system shall provide an API for an agent to send a broadcast message to all reachable agents on the local network subnet.
*   **FR-BC-2:** The system shall deliver incoming broadcast messages to all active agents within the local agentMom instance.
*   **FR-BC-3:** The broadcast scope shall be limited to the local subnet (e.g., using IP limited broadcast address `255.255.255.255` or subnet-directed broadcast).

##### 3.1.4 Secure Communication
*   **FR-SC-1:** The system shall provide an API to encrypt the content of a message using a provided symmetric key (e.g., AES) before transmission.
    ```java
    // Example API Signature
    SecureMessage encryptMessage(Message plainMessage, SecretKey key);
    ```
*   **FR-SC-2:** The system shall provide an API to decrypt the content of an encrypted message using the corresponding symmetric key.
    ```java
    // Example API Signature
    Message decryptMessage(SecureMessage encryptedMessage, SecretKey key) throws SecurityException;
    ```
*   **FR-SC-3:** The security APIs shall be usable for both unicast and multicast message payloads. Broadcast security is optional due to its open nature.
*   **FR-SC-4:** Encryption shall encompass the message payload (content). Message headers (sender, recipient, group, timestamp) may remain in plaintext for routing purposes.
*   **FR-SC-5:** The system shall throw a defined `SecurityException` if decryption fails (e.g., due to an invalid key or corrupted data).

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance
*   **NFR-PER-1:** The overhead of the encryption/decryption layer for unicast messages shall not increase latency by more than 15% compared to unsecured unicast.
*   **NFR-PER-2:** Multicast and broadcast message transmission shall be non-blocking; the sending agent shall not wait for delivery confirmation.

##### 3.2.2 Reliability & Availability
*   **NFR-REL-1:** The failure of a multicast or broadcast transmission (e.g., due to network issues) shall not crash the sending agent or the framework. Errors shall be logged.
*   **NFR-REL-2:** The unicast communication channel, including its secured variant, shall maintain a reliability parity with the base agentMom framework.

##### 3.2.3 Security
*   **NFR-SEC-1:** The encryption module shall use strong, industry-standard algorithms (e.g., AES with GCM mode for confidentiality and integrity).
*   **NFR-SEC-2:** Secret keys shall **not** be stored or managed by the framework. Key management is the responsibility of the application developer.
*   **NFR-SEC-3:** The system shall be resistant to common network-based attacks on multicast/broadcast, such as ignoring malformed packets.

##### 3.2.4 Usability
*   **NFR-USE-1:** The new communication APIs shall be consistent in style and naming conventions with the existing agentMom API.
*   **NFR-USE-2:** Comprehensive Javadoc documentation shall be provided for all new public classes and methods.
*   **NFR-USE-3:** At least one functional example program demonstrating multicast group chat and secured unicast communication shall be included in the distribution.

##### 3.2.5 System
*   **NFR-SYS-1:** The extension shall be compatible with any operating system that supports standard Java SE networking and where the JVM has the necessary network permissions.
*   **NFR-SYS-2:** The module shall not introduce mandatory dependencies on third-party libraries outside the Java Standard Edition.

---
**Document Approval:**

*   Prepared By: ________________________ Date: _______________
*   Reviewed By: ________________________ Date: _______________
*   Approved By: ________________________ Date: _______________