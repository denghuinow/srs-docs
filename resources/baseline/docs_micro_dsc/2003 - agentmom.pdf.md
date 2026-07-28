# Software Requirements Specification (SRS)
## For agentMom Framework Communication Extension
**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for extending the **agentMom multi-agent framework (version 1.2)**. The primary purpose is to augment the framework's communication capabilities by introducing broadcast, multicast, and secured unicast messaging paradigms. This document is intended for use by the project stakeholders, developers, testers, and project managers.

#### 1.2 Scope
The scope of this project is to develop and integrate a new communication module into the existing agentMom 1.2 framework. The extension will:
*   Provide APIs for agents to send and receive unicast, multicast, and broadcast messages.
*   Manage multicast group membership (join/leave operations).
*   Integrate optional encryption and decryption for unicast messages.
*   Maintain full backward compatibility with the existing agentMom 1.2 API and agent lifecycle.

**Out of Scope:**
*   Modification of the core agent lifecycle, creation, or migration logic of agentMom 1.2.
*   Guaranteed delivery protocols for multicast or broadcast messages.
*   Modification of the underlying physical network configuration to enable multicast support.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **agentMom:** The existing multi-agent framework being extended.
*   **Unicast:** Point-to-point communication between a single sender and a single receiver agent.
*   **Multicast:** One-to-many communication where a message is sent to a specific group of agents.
*   **Broadcast:** One-to-all communication where a message is sent to all active agents within the framework's domain.
*   **Multicast Group:** A logical addressing group that agents can dynamically join or leave to receive multicast messages.
*   **Best-Effort Delivery:** A network service that makes a reasonable attempt to deliver messages but provides no guarantees against loss, duplication, or out-of-order delivery.
*   **API:** Application Programming Interface.

#### 1.4 References
*   agentMom Framework Version 1.2 Core Documentation.
*   RFC 1112 - Host Extensions for IP Multicasting.
*   Project Charter: "agentMom Communication Enhancement Project."

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a high-level description of the product and its interaction with the existing framework. Section 3 details specific functional requirements. Section 4 outlines non-functional requirements, including performance, security, and compatibility.

---

### 2. Overall Description

#### 2.1 Product Perspective
This extension is a new module that integrates seamlessly with the agentMom 1.2 framework. It acts as an enhanced communication layer sitting atop the existing messaging infrastructure.

```
[Agent A] -> [Extended Comm Module] -> [Network/Platform Layer] -> [Extended Comm Module] -> [Agent B]
        (Unicast)                                                            (Unicast)
        (Secure Unicast)                                                     (Secure Unicast)
        (Multicast to Group G) -> ---------------> [Multicast Group G] -> -> [Agent C]
        (Broadcast) -> --------------------------> [All Agents] ---------> -> [Agent D]
                                                                               [Agent ...]
```
*Figure 1: High-Level System Context Diagram*

#### 2.2 Product Functions
The key functions of the extension are:
1.  **Message Transmission:** Send unicast, multicast, and broadcast messages.
2.  **Message Reception:** Receive messages sent via any of the three paradigms.
3.  **Group Management:** Allow agents to dynamically join and leave multicast groups.
4.  **Security Service:** Optionally encrypt the payload of unicast messages and decrypt them upon receipt.

#### 2.3 User Characteristics
The end-users of this framework are **agent developers**. They are assumed to be proficient programmers familiar with the agentMom 1.2 paradigm and basic network communication concepts.

#### 2.4 Constraints
1.  **Compatibility Constraint:** The extension must be fully backward compatible with the public API and agent behavior of agentMom 1.2. Existing agents must continue to function without modification.
2.  **Network Constraint:** Multicast functionality is contingent upon the underlying host environment and network supporting the IP multicast protocol (e.g., IGMP). The framework will not emulate multicast in non-supporting environments.
3.  **Delivery Constraint:** Multicast and broadcast messaging will be implemented as a **best-effort service**. The framework does not guarantee message delivery, ordering, or duplicate prevention for these message types.
4.  **Encryption Scope:** Message encryption/decryption is an optional feature applicable **only to unicast** messages.

#### 2.5 Assumptions and Dependencies
*   It is assumed that the hosting operating system and network infrastructure provide the necessary APIs and configuration to support IP multicast when that feature is used.
*   The project depends on the continued stability and availability of the agentMom 1.2 core codebase.

---

### 3. Specific Requirements

#### 3.1 External Interface Requirements
**3.1.1 User Interfaces**
Not applicable. This is a software library/framework extension.

**3.1.2 Programming Interfaces (API)**
The extension shall expose the following new or extended interfaces to the agent developer:

*   `Message sendMessage(AgentID recipient, Message msg, boolean encrypt)`
    *   **Description:** Sends a unicast message to a specific agent.
    *   **Parameters:** `recipient` (target agent ID), `msg` (message object), `encrypt` (if true, payload is encrypted).
    *   **Returns:** A message receipt or status object.

*   `void multicastMessage(GroupID group, Message msg)`
    *   **Description:** Sends a message to all agents currently members of the specified multicast group.
    *   **Parameters:** `group` (logical multicast group identifier), `msg` (message object).

*   `void broadcastMessage(Message msg)`
    *   **Description:** Sends a message to all active agents known to the framework.
    *   **Parameters:** `msg` (message object).

*   `boolean joinMulticastGroup(GroupID group)`
    *   **Description:** Registers the calling agent to receive messages multicast to the specified group.
    *   **Parameters:** `group` (logical multicast group identifier).
    *   **Returns:** `true` if successful, `false` otherwise (e.g., group invalid, network error).

*   `boolean leaveMulticastGroup(GroupID group)`
    *   **Description:** Deregisters the calling agent from the specified multicast group.
    *   **Parameters:** `group`.
    *   **Returns:** `true` if successful, `false` otherwise.

*   **Event/Listener Interface:** The existing agent message handler (e.g., `onMessage(Message msg)`) shall be enhanced to receive metadata indicating the message type (unicast/multicast/broadcast) and, for unicast, its encryption status.

#### 3.2 Functional Requirements

**FR-1: Unicast Messaging**
*   **FR-1.1:** The framework shall allow an agent to send a message to a uniquely identified recipient agent.
*   **FR-1.2:** The framework shall deliver a unicast message to its intended recipient agent's message handler.
*   **FR-1.3:** If the `encrypt` flag is set for a unicast message, the framework shall encrypt the message payload using a pre-configured symmetric encryption algorithm (e.g., AES) before transmission and decrypt it upon reception.

**FR-2: Multicast Messaging**
*   **FR-2.1:** The framework shall allow an agent to send a message addressed to a logical multicast group.
*   **FR-2.2:** The framework shall deliver a multicast message to the message handler of every agent that is currently a member of the target group.
*   **FR-2.3:** Delivery of multicast messages shall be on a best-effort basis as defined in the constraints (Section 2.4).

**FR-3: Broadcast Messaging**
*   **FR-3.1:** The framework shall allow an agent to send a message to all active agents within the framework's domain.
*   **FR-3.2:** The framework shall deliver a broadcast message to the message handler of every active agent.
*   **FR-3.3:** Delivery of broadcast messages shall be on a best-effort basis.

**FR-4: Multicast Group Management**
*   **FR-4.1:** The framework shall allow an agent to dynamically join a logical multicast group.
*   **FR-4.2:** The framework shall allow an agent to dynamically leave a logical multicast group.
*   **FR-4.3:** The framework shall maintain an internal registry of group memberships.
*   **FR-4.4:** An agent that joins a group shall start receiving multicast messages for that group. An agent that leaves a group shall stop receiving them.

**FR-5: Backward Compatibility**
*   **FR-5.1:** All existing agent code written for agentMom 1.2 that uses the original messaging API shall compile and execute without error or behavioral change.
*   **FR-5.2:** The default behavior of the existing send message API shall remain unicast, non-encrypted communication.

#### 3.3 Non-Functional Requirements

**3.3.1 Performance Requirements**
*   **PER-1:** The overhead of the new communication module shall not increase unicast latency by more than 10% compared to the baseline agentMom 1.2 for non-encrypted messages.
*   **PER-2:** The latency for multicast and broadcast sends should be sub-linear relative to the number of recipient agents.

**3.3.2 Security Requirements**
*   **SEC-1:** When enabled, unicast message encryption shall use a strong, industry-standard algorithm (e.g., AES-256-GCM).
*   **SEC-2:** Encryption keys shall be managed by a configurable keystore/provider and shall not be hard-coded in the framework.
*   **SEC-3:** Multicast and broadcast messages shall **not** be encrypted by the framework due to key management complexity and performance overhead.

**3.3.3 Reliability & Availability**
*   **REL-1:** The failure of the multicast subsystem (e.g., due to lack of network support) shall not crash the framework or prevent unicast communication.
*   **REL-2:** The framework shall log appropriate warnings if multicast operations are attempted in an unsupported environment.

**3.3.4 Compatibility Requirement**
*   **COM-1:** The extended framework must be binary and source compatible with agents developed for the public API of agentMom version 1.2.

---

### 4. Appendices

#### 4.1 Sample Usage Code
```java
// Example agent code using the new API
public class SampleAgent extends Agent {

    private static final GroupID LOG_GROUP = new GroupID("LOG_AGENTS");

    @Override
    public void onStart() {
        // Join a multicast group
        joinMulticastGroup(LOG_GROUP);

        // Send a secure unicast message
        Message secureMsg = new Message("Confidential data");
        sendMessage(someAgentID, secureMsg, true);

        // Send a multicast message
        Message logMsg = new Message("System event occurred");
        multicastMessage(LOG_GROUP, logMsg);

        // Send a broadcast message
        Message alertMsg = new Message("System shutdown in 5 min");
        broadcastMessage(alertMsg);
    }

    @Override
    public void onMessage(Message msg, MessageMetadata meta) {
        // meta contains type: UNICAST/MULTICAST/BROADCAST
        // and for UNICAST, encryption status
        if (meta.isEncrypted()) {
            // msg payload is already decrypted by the framework
            process(msg.getContent());
        }
    }

    @Override
    public void onStop() {
        // Leave the multicast group
        leaveMulticastGroup(LOG_GROUP);
    }
}
```

#### 4.2 Open Issues
*   The specific symmetric encryption algorithm and key exchange mechanism for unicast security are to be finalized in the design phase.
*   The mechanism for defining the "domain" for broadcast messages (e.g., all agents on a host, in a subnet) requires further specification.

---
*Document End*