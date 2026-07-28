# Software Requirements Specification (SRS)
## Mahjong Network Game System
**Document Version:** 1.0  
**Date:** [Current Date]  
**Prepared for:** Solid Software Pty Ltd  
**Prepared by:** [Your Name/Team]

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Mahjong Network Game System. This document is intended to be used by the development team, project managers, testers, and stakeholders of Solid Software Pty Ltd to guide the design, implementation, and verification of the system.

#### 1.2 Scope
The system is a computer-based implementation of the Chinese Mahjong game, consisting of a client application for end-users and a central server application for managing multiplayer sessions. The core capabilities include:
*   Supporting single-player games against three computer-controlled opponents.
*   Facilitating multiplayer games for up to four human players over a TCP/IP network.
*   Enforcing the standard rules of Chinese Mahjong.
*   Managing all game state logic and communication between clients.

**Out-of-Scope:**
*   Data encryption for network traffic.
*   Support for network protocols other than TCP/IP.
*   Integration with external user account systems or payment gateways.
*   Support for other regional Mahjong rule variants.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **SRS:** Software Requirements Specification
*   **TCP/IP:** Transmission Control Protocol/Internet Protocol
*   **GUI:** Graphical User Interface
*   **JVM:** Java Virtual Machine
*   **JDK:** Java Development Kit
*   **CO:** Computer Opponent
*   **Chow:** A meld of three consecutive tiles in the same suit.
*   **Pung:** A meld of three identical tiles.
*   **Kong:** A meld of four identical tiles.
*   **Mahjong:** The winning hand (comprising four melds and a pair).

#### 1.4 References
*   JDK 1.2 Specification
*   Standard Chinese Mahjong Rules (Assumed knowledge per Constraint 1.4)

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details all specific requirements, including functional, interface, and non-functional requirements.

---

### 2. Overall Description

#### 2.1 Product Perspective
This is a new, self-contained product. The system follows a client-server model:
*   **Server Application:** To be hosted on Solid Software Pty Ltd's infrastructure. It acts as a game lobby and state relay, managing multiple concurrent game sessions.
*   **Client Application:** To be commercially sold to end-users. It provides the game interface, local game logic, and network communication stub.

#### 2.2 Product Functions
The high-level functions of the system are:
1.  Multiplayer Game Management: Creation, listing, joining, and state synchronization of 4-player games.
2.  Single-Player Game: Provision of a full game with one human and three computer opponents.
3.  Rule Enforcement: Validation of all player actions (draw, discard, Chow, Pung, Kong, Mahjong) according to Chinese Mahjong rules.
4.  Move Assistance: Automatic calculation and highlighting of valid special moves (Chow, Pung, Kong, Mahjong) following a discard.
5.  Computer Opponent: Provision of an AI player that can participate by the rules.
6.  State Relay: Broadcasting game events (discards, melds, wins) to all participants in a session.

#### 2.3 User Characteristics
The primary end-users are individuals with an interest in Mahjong. They are assumed to:
*   Have basic familiarity with standard Chinese Mahjong rules.
*   Possess basic operational knowledge of their PC/Mac/Unix operating system.
*   Have a computer configured for TCP/IP network connectivity (for multiplayer mode).

The server operator (Solid Software Pty Ltd staff) requires knowledge of server administration and network configuration.

#### 2.4 Constraints
1.  **Implementation Language:** The system must be implemented using Java, targeting JDK 1.2.
2.  **Network Protocol:** Communication must use TCP/IP. Other protocols are not supported.
3.  **Client Environment:** The client application must run on any system with a JVM compatible with JDK 1.2.
4.  **Server Environment:** The server requires a machine with a unique IP address.

#### 2.5 Assumptions and Dependencies
*   End-user machines are correctly configured for TCP/IP networking.
*   The reader of this SRS is familiar with Chinese Mahjong terminology and rules.
*   Solid Software Pty Ltd will provide and maintain the necessary server hardware and network infrastructure.
*   No firewall or network address translation (NAT) issues will prevent client-server communication (or such issues are the responsibility of the end-user to resolve).

---

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 User Interfaces
*   **Client GUI:** A graphical interface rendered within an 800x600 pixel window using 16-bit color.
*   **Game Lobby View:** Displays a list of available multiplayer games on the server, with options to "Join" or "Create New Game."
*   **Game Creation Dialog:** Allows the user to specify a game name and select the type for each of the four player slots (Human or Computer).
*   **Game Table View:** The main game screen displaying:
    *   The user's hand of tiles.
    *   The current discard pile.
    *   The exposed melds (Chow, Pung, Kong) of all players.
    *   The wall of remaining tiles.
    *   Visual indicators for valid moves (e.g., highlighted tiles or buttons for Chow, Pung, Kong, Mahjong).
    *   Game status information (current player, wind, scores).

##### 3.1.2 Hardware Interfaces
*   **Client:** Standard input (keyboard, mouse). Standard output (display supporting 800x600 in 16-bit color).
*   **Server:** Network Interface Card for TCP/IP communications.

##### 3.1.3 Software Interfaces
*   **Network Interface:** The client and server shall communicate via a proprietary application-layer protocol over TCP/IP sockets.
*   **JVM:** The client software interface is the Java Virtual Machine, version compatible with JDK 1.2.

##### 3.1.4 Communications Interfaces
*   **Protocol:** TCP/IP.
*   **Function:** The interface supports messaging for: authentication (simple), game list updates, game join/create commands, and all game action commands (draw, discard, declare meld, win).

#### 3.2 Functional Requirements
Requirements are prioritized as Level 1 (Essential), Level 2 (Highly Desirable), or Level 3 (Future).

##### 3.2.1 Client Application Requirements
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **C.1** | The client shall allow the user to connect to a specified server address and port. | 1 |
| **C.2** | The client shall request and display a list of available multiplayer games from the server. | 1 |
| **C.3** | The client shall provide a dialog to create a new game, allowing the user to name the game and set each player slot as Human or Computer. | 1 |
| **C.4** | The client shall allow the user to join an existing, available game from the list. | 1 |
| **C.5** | The client shall launch a single-player game with three Computer Opponents without requiring a network server connection. | 1 |
| **C.6** | The client shall display a graphical representation of the Mahjong tile set. | 1 |
| **C.7** | The client shall accept user input to draw a tile from the wall and add it to the user's hand. | 1 |
| **C.8** | The client shall accept user input to discard a tile from the user's hand to the discard pile. | 1 |
| **C.9** | Following any player's discard, the client shall calculate and visually indicate if the user has a valid Chow, Pung, Kong, or Mahjong opportunity. | 1 |
| **C.10** | The client shall accept user input to declare a valid Chow, Pung, Kong, or Mahjong when it is indicated. | 1 |
| **C.11** | The client shall enforce game rules locally, preventing illegal user moves (e.g., discarding a tile not in hand, declaring an invalid meld). | 1 |
| **C.12** | The client shall relay all valid user actions (draw, discard, meld declaration, win) to the server in multiplayer mode. | 1 |
| **C.13** | The client shall receive and process game state updates (other players' discards, melds, wins) from the server and update the GUI accordingly. | 1 |
| **C.14** | The client shall host the Computer Opponent (CO) logic for any player slot set to "Computer." | 1 |
| **C.15** | The CO shall be capable of performing all legal game actions: drawing, discarding, and declaring Chow, Pung, Kong, and Mahjong according to the rules. | 1 |
| **C.16** | The CO shall determine its move within 60 seconds of its turn becoming active. | 1 |
| **C.17** | The client shall calculate and indicate possible moves for the user within 5 seconds of a tile being discarded. | 1 |
| **C.18** | The client GUI shall fit entirely within an 800x600 pixel resolution display. | 1 |

##### 3.2.2 Server Application Requirements
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **S.1** | The server shall listen for incoming TCP/IP connections on a configurable port. | 1 |
| **S.2** | The server shall maintain a list of active game sessions. | 1 |
| **S.3** | The server shall accept requests from clients to create a new game session, registering its name and configuration. | 1 |
| **S.4** | The server shall provide a list of available (non-full) game sessions to connecting clients upon request. | 1 |
| **S.5** | The server shall accept requests from clients to join a specific available game session. | 1 |
| **S.6** | The server shall manage the state of each game session, including player order, current wind, and the initial tile wall. | 1 |
| **S.7** | The server shall relay a player's valid action (discard, meld declaration, win) to all other clients in the same game session. | 1 |
| **S.8** | The server shall handle up to 10 simultaneous game sessions (supporting up to 40 connected clients). | 1 |
| **S.9** | The server shall detect client disconnections and update the affected game state (e.g., pause game, mark player as inactive). | 2 |
| **S.10**| The server shall log game events and connection activity for administrative purposes. | 3 |

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance Requirements
1.  **NFR.PER.1:** The Computer Opponent shall compute and execute its move within **60 seconds** of its turn becoming active.
2.  **NFR.PER.2:** The server shall be designed to handle a load of **10 simultaneous games** (40 concurrent players) without degradation of service (e.g., message relay latency > 2 seconds).
3.  **NFR.PER.3:** The client shall perform move possibility calculation (for Chow, Pung, Kong, Mahjong) and provide user indication within **5 seconds** of a discard event.

##### 3.3.2 Software Quality Attributes
*   **Portability:** The client application must run on any operating system (e.g., Windows 95+, Mac OS 8, Solaris) with a Java Virtual Machine supporting JDK 1.2.
*   **Usability:** The graphical user interface shall be designed to fit within an **800x600 pixel** resolution using **16-bit color** depth. Controls shall be intuitive for a user familiar with Mahjong.

##### 3.3.3 Safety & Security Requirements
*   *Note: Data encryption is explicitly out of scope. No specific safety or security requirements are defined at this stage.*

#### 3.4 Acceptance Criteria
The product will be considered accepted by Solid Software Pty Ltd upon successful verification that **all Level 1 (Priority 1)** requirements specified in Section 3.2 have been correctly and fully implemented.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner | | | |
| Lead Developer | | | |
| QA Manager | | | |