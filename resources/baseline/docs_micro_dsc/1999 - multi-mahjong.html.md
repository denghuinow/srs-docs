# Software Requirements Specification (SRS)
## Mahjong Client-Server Game
**Version:** 1.0
**Date:** October 26, 2023
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for a client-server based Mahjong game. The primary purpose is to provide a definitive specification for developers, testers, project managers, and stakeholders. This SRS will serve as the foundation for design, implementation, and verification activities.

#### 1.2 Document Conventions
*   Requirements are uniquely identified with labels (e.g., **FR-1**, **NFR-2**).
*   **Shall** indicates a mandatory requirement.
*   *Should* indicates a desirable but not mandatory feature.
*   Terms in **bold** are key domain terms defined in the glossary.

#### 1.3 Project Scope
The project encompasses the development of a networked **Mahjong** game application based on standard **Chinese Mahjong** rules. The system shall consist of a server application and one or more client applications. It shall support both single-player modes (with three computer-controlled opponents) and multiplayer modes (for 2-4 human players over a network). The scope includes game logic enforcement, network communication, a graphical user interface (GUI), and artificial intelligence (AI) for computer opponents. Development of account systems, persistent leaderboards, or in-game chat beyond basic turn/status messages is explicitly out of scope.

#### 1.4 References
*   JDK 1.2 API Documentation.
*   Standard Chinese Mahjong Rules (e.g., Hong Kong Old Style scoring).

### 2. Overall Description

#### 2.1 Product Perspective
This is a new, standalone product. It will operate in a standard desktop environment (Windows, Linux, macOS) capable of running Java applications. The system architecture follows a classic client-server model where the server acts as the authoritative source for game state and rule enforcement.

#### 2.2 Product Functions (High-Level)
1.  Manage game sessions (create, join, terminate).
2.  Enforce Chinese Mahjong rules for tile drawing, discarding, claiming, and winning.
3.  Render a graphical game board and player hands.
4.  Facilitate real-time communication between clients and the server.
5.  Simulate intelligent gameplay for computer-controlled opponents.
6.  Calculate and display scores at the end of each round/game.

#### 2.3 User Classes and Characteristics
*   **Player:** The primary user. Can be a human or a computer-controlled agent. Human players are assumed to have basic knowledge of Mahjong rules.
*   **Server Administrator:** Responsible for starting and stopping the server application. Has technical knowledge of network configuration.

#### 2.4 Operating Environment
*   **Software:** Java Development Kit (JDK) 1.2 or compatible Java Runtime Environment (JRE).
*   **Hardware (Client):** Must support a display resolution of 800x600 pixels with 16-bit (High Color) depth.
*   **Network:** TCP/IP network connectivity is required for multiplayer functionality.

#### 2.5 Design and Implementation Constraints
1.  The entire application **shall** be implemented using the Java programming language and APIs available in **JDK 1.2**.
2.  The client GUI **shall** be designed to fit and be fully functional within an **800x600 pixel** viewport.
3.  All graphical assets and interface rendering **shall** be compatible with a **16-bit color** palette.
4.  Computer opponent decision-making logic **shall** generate a response (discard, claim, declare win) within **one minute** of receiving game state from the server.

#### 2.6 Assumptions and Dependencies
*   It is assumed that the network connection between client and server is stable during a game session. The protocol will include basic handling for timeouts and disconnections.
*   The project depends on the availability of graphical tile assets compatible with the specified color and resolution constraints.

### 3. System Features and Requirements

#### 3.1 Game Session Management
**Description:** This feature handles the lifecycle of a Mahjong game, from creation to conclusion.

**Requirements:**
*   **FR-1:** The server **shall** allow a client to create a new game session, specifying it as "Single Player" or "Multiplayer."
*   **FR-2:** For a "Single Player" session, the server **shall** automatically create and manage three computer opponents to fill the table.
*   **FR-3:** For a "Multiplayer" session, the server **shall** allow up to three additional clients to join an existing session until four total players are present.
*   **FR-4:** The server **shall** enforce that a game can only start once exactly four players (human or computer) are present.
*   **FR-5:** The server **shall** notify all connected clients of changes in session state (e.g., player joined, game starting).

#### 3.2 Game Logic & Rule Enforcement
**Description:** This is the core system feature that implements the rules of Chinese Mahjong and validates all player actions.

**Requirements:**
*   **FR-6:** The server **shall** maintain the authoritative state of the game, including the wall, dead wall, discard pile, and each player's concealed and revealed tiles.
*   **FR-7:** The server **shall** enforce turn order, ensuring only the correct player can draw from the wall or claim a discard.
*   **FR-8:** The server **shall** validate all player actions (discard, chow, pung, kong, win) against standard Chinese Mahjong rules before updating the game state.
*   **FR-9:** The server **shall** detect a winning hand (Mahjong) and immediately halt the round.
*   **FR-10:** The server **shall** calculate scores for all players at the end of each round based on standard scoring rules and propagate results to all clients.

#### 3.3 Client Graphical User Interface (GUI)
**Description:** This feature provides the visual interface through which a human player interacts with the game.

**Requirements:**
*   **FR-11:** The client GUI **shall** display the player's own hand of tiles clearly and selectable.
*   **FR-12:** The client GUI **shall** display the central discard area.
*   **FR-13:** The client GUI **shall** display the revealed sets (chows, pungs, kongs) of all four players.
*   **FR-14:** The GUI **shall** provide clear visual indicators for the current turn, prevailing wind, and player wind.
*   **FR-15:** The GUI **shall** provide interactive controls for all valid actions (Discard, Chow, Pung, Kong, Declare Win) which are enabled/disabled based on game state.
*   **FR-16:** The entire game board and interface **shall** be renderable within a **800x600 pixel** window without requiring scrolling.

#### 3.4 Network Communication
**Description:** This feature manages the reliable exchange of game commands and state between client and server.

**Requirements:**
*   **FR-17:** The client and server **shall** communicate using a custom protocol over **TCP/IP** sockets.
*   **FR-18:** The server **shall** broadcast relevant game state updates to all connected clients after each valid action.
*   **FR-19:** The client **shall** send player action requests to the server for validation.

#### 3.5 Computer Opponent (AI)
**Description:** This feature simulates a player controlled by the system.

**Requirements:**
*   **FR-20:** The system **shall** provide computer opponents capable of playing a complete game of Mahjong, including drawing, discarding, and claiming tiles.
*   **FR-21:** The computer opponent **shall** make all decisions (discard selection, claim decisions) based on a non-trivial strategy (e.g., prioritizing potential winning hands).
*   **NFR-1 (Performance):** The computer opponent's decision-making process **shall** complete and send a response to the server within **60 seconds** of being prompted, under normal system load.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   The primary user interface is the graphical client described in Section 3.3.
*   The server may have a minimal console-based interface for startup, shutdown, and logging status.

#### 4.2 Hardware Interfaces
*   Standard keyboard and mouse input for the client.
*   Network interface card for TCP/IP communication.

#### 4.3 Software Interfaces
*   **Java JDK 1.2:** The application interfaces exclusively with the standard libraries provided in this JDK version (e.g., `java.net`, `java.awt`, `javax.swing`).

#### 4.4 Communications Interfaces
*   Protocol: Proprietary application-layer protocol over TCP.
*   Port: The server shall listen on a configurable port number (default specified in configuration).

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   **NFR-1:** Covered in Section 3.5 (AI response < 60 seconds).
*   **NFR-2:** The client GUI shall update to reflect new game state (e.g., a new discard) within 2 seconds of receiving the server broadcast.
*   **NFR-3:** The server shall be capable of handling multiple concurrent game sessions (minimum of 10).

#### 5.2 Safety Requirements
*   Not applicable for this entertainment software.

#### 5.3 Security Requirements
*   **NFR-4:** The server shall validate that all incoming messages conform to the expected protocol format to prevent simple malformed packet crashes. (Note: Advanced security like encryption is out of scope).

#### 5.4 Software Quality Attributes
*   **Maintainability:** Code shall be modular, with clear separation between game logic, network layer, and GUI components.
*   **Usability:** The GUI shall be intuitive for a user familiar with Mahjong. Tooltips or a simple help screen should explain control basics.

---

### Appendix A: Glossary

| Term | Definition |
| :--- | :--- |
| **Chow** | A claim of a discard to complete a sequence of three consecutive numbers in the same suit. |
| **Client** | The application run by a user that provides the GUI and communicates with the Server. |
| **Kong** | A set of four identical tiles. |
| **Mahjong** | The winning condition, a complete hand of 14 tiles arranged in four sets and a pair. |
| **Pung** | A claim of a discard to complete a set of three identical tiles. |
| **Server** | The central application that manages game sessions, enforces rules, and communicates with all Clients. |
| **Wall** | The shuffled stack of tiles from which players draw. |

### Appendix B: To Be Determined (TBD)
1.  Specific scoring table to be used (e.g., point values for different winning hands).
2.  Detailed wireframe mockups of the 800x600 client GUI.
3.  Exact specification of the TCP/IP message protocol (opcodes and data formats).