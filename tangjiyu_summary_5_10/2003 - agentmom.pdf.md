# Applying Broadcasting/Multicasting/Secured Communication to agentMom in Multi-Agent Systems - Software Requirements Specification

## 1. Introduction

### 1.1 Purpose
This document describes functionality and behavior of the new agentMom framework. It covers software requirements for the project "Applying Broadcasting/Multicasting/Secured Communication to agentMom in Multi-Agent Systems".

### 1.2 Scope
This project will be a framework that provides reusability of agent's communication. It is implemented in Java and provides basic building blocks for building agents, conversations between agents, and messages passed in conversations.

### 1.3 Definitions
- agentMom 1.2: Current implementation of agentMom
- New agentMom: Project including agentMom with capability of broadcasting, multicasting and secured communication
- Unicast: One-to-one communication from single Internet host to unique location of another Internet host
- Multicast: One-to-many communication from single Internet host to multiple receivers within same multicast address
- Broadcast: One-to-many communication from single Internet host to all receivers within same local network
- Organization: Set of agents
- Group: Set of agents who agree to use same multicast address to subscribe group message
- Time-To-Live (TTL): Number of hops that multicast message is allowed to remain in network before discarded by router

## 2. Overall Description

### 2.1 Product Perspective
Framework implemented in Java providing reusability of agent's communication. Provides basic building blocks for building agents, conversations between agents, and messages passed in conversations.

#### 2.1.1 Software Interface
Java version 1.4.0 required to use software.

#### 2.1.2 Communication Interface
- TCP/IP for unicast message
- Multicast protocol for multicast message
- UDP for broadcast message

### 2.2 Product Functions
1. Enable agents to broadcast message to all agents within same local network
2. Enable agents to multicast message to all agents within same multicast address
3. Enable agents to unicast message to other agents within organization
4. Allow agents to choose among unicast, multicast and broadcast communication
5. Allow agents to join and leave multicast group
6. Provide message encryption and decryption techniques for secured communication
7. Allow agents to choose to encrypt or not to encrypt message

### 2.3 User Characteristics
Users implementing multi-agent systems based on this framework expected to have general knowledge of Java programming, object-oriented programming and Multi-Agent Systems Engineering Methodology.

### 2.4 Constraints
1. Reliable message delivery: Multicast/broadcast packets delivered with best effort. Packet may be delivered to all specified agents or none.
2. Security: Basic mechanisms for security such as message encryption provided. No guarantee that others cannot decrypt encrypted messages.
3. Multicast Protocol: Network environment such as router, network card and operating systems must support multicast protocol.
4. Broadcast Message: In many networks, only system administrator is allowed to send broadcast message.

### 2.5 Assumptions and Dependencies
1. Each agent knows address of destinating agents to send unicast message
2. Each agent has enough knowledge to decide best way to communicate with other agents
3. In case of secured multicast communication, there is an agent whom each agent can request for same encryption and decryption key
4. Each agent knows multicast address to send multicast message

## 3. Specific Requirements

### 3.1 Use Cases
1. Notify join/leave multicast group: Agents can send notify to join/leave multicast group with optional message encryption/decryption
2. Send/Receive Unicast: Agents can send unicast message to another agent with optional encryption/decryption
3. Send/Receive Multicast: Agents can send multicast message to group with optional encryption/decryption
4. Send/Receive Broadcast: Agents can send message to everyone in same local network

### 3.2 Specific Requirements

#### 3.2.1 Unicast Communication
- agentMom shall support ability to send and receive unicast message
- Unicast message shall only be received by specified address
- Unicast message shall arrive at specified address and in order

#### 3.2.2 Multicast Communication
- agentMom shall support ability to send and receive multicast message
- agentMom shall support ability to send request to join and leave multicast group
- agentMom shall not allow receiving multicast message from group before joining or after leaving
- agentMom shall support ability to set time-to-live for multicast message
- agentMom shall support ability to set multicast address and port for sending and receiving multicast message
- agentMom shall support ability to receive multicast message from multiple groups

#### 3.2.3 Broadcast Communication
- agentMom shall support ability to send and receive broadcast message
- Broadcast message shall be sent to all possible hosts under same local network

#### 3.2.4 Security
- agentMom shall support ability to encrypt and decrypt unicast message
- agentMom shall allow agent to decide whether or not to encrypt message
- agentMom shall automatically decrypt encrypted message
- agentMom shall support ability to encrypt and decrypt multicast message

#### 3.2.5 Architecture
- agentMom shall support use of architecture that agent directly controls conversations
- agentMom shall support use of architecture that agent's components control conversations

#### 3.2.6 Compatibility
- New built agentMom shall be compatible with agentMom 1.2

Note: The " * " indicates Driving Requirements that need to be demonstrated by end of phase II.
