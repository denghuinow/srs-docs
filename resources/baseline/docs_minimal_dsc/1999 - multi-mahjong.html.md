# Software Requirements Specification (SRS)
## Mahjong Game System

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Approved for Development

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Mahjong Game System. This document is intended to be used by the project development team, testers, and project managers to guide the design, implementation, and verification of the system.

#### 1.2 Scope
The system is a software application that enables users to play Mahjong according to standard Chinese rules. The system supports two primary modes:
1.  **Single-Player Mode:** A user plays a standalone game against three computer-controlled opponents.
2.  **Multiplayer Mode:** Up to four human players can connect via a TCP/IP network to play together, coordinated by a central game server.

The system includes a client application with a graphical user interface (GUI) and a dedicated server application for managing multiplayer sessions. The scope excludes features such as in-game chat, player statistics persistence, monetization, or alternative rule sets (e.g., Japanese Riichi Mahjong).

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **GUI:** Graphical User Interface.
*   **JVM:** Java Virtual Machine.
*   **JDK:** Java Development Kit.
*   **TCP/IP:** Transmission Control Protocol/Internet Protocol, a suite of communication protocols used to interconnect network devices.
*   **AI:** Artificial Intelligence, referring to the computer-controlled opponents.
*   **Tile:** The fundamental playing piece in Mahjong.
*   **Hand:** A player's collection of tiles.
*   **Mahjong:** The winning condition where a player's hand forms a valid, complete set of combinations.

#### 1.4 References
*   JDK 1.2 Specification
*   Standard Chinese Mahjong Rules

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details the specific requirements, including functional, interface, and non-functional requirements.

---

### 2. Overall Description

#### 2.1 Product Perspective
The Mahjong Game System is a new, self-contained application. It operates in two primary configurations:
*   **Standalone Client:** For single-player games, the client runs independently, containing all game logic and AI.
*   **Client-Server Network:** For multiplayer games, multiple client instances connect to a central server application. The server acts as the authoritative source for game state, rule enforcement, and message routing between clients.

#### 2.2 Product Functions
The high-level functions of the system are:
1.  Manage game sessions (create, join, start, conclude).
2.  Enforce Chinese Mahjong rules throughout gameplay.
3.  Render a graphical representation of the game board, player hands, and discarded tiles.
4.  Accept and process player input via the GUI.
5.  Simulate competent gameplay for computer opponents (AI).
6.  Facilitate network communication for multiplayer games.

#### 2.3 User Characteristics
**Key User:** The typical end-user is a person interested in playing Mahjong who possesses basic computer operation skills. They are expected to:
*   Understand the fundamental rules of Chinese Mahjong.
*   Be able to use a mouse and keyboard.
*   Have basic knowledge of starting applications and navigating menus.
No advanced networking or system administration skills are required.

#### 2.4 Constraints
1.  **Implementation Language:** The system must be implemented using Java, specifically JDK 1.2.
2.  **Platform Compatibility:** The client and server applications must run on any operating system (Windows, Mac OS, Unix) that supports a compatible Java Virtual Machine (JVM).
3.  **Performance:** Computer opponents (AI) must calculate and execute their turn (discard, claim a tile, declare Mahjong) within **one minute** of receiving control.
4.  **Scalability:** The central game server must be capable of supporting up to **10 simultaneous multiplayer games** (i.e., up to 40 connected clients) without degradation of performance as defined in section 3.5.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** Users have a pre-existing understanding of Mahjong rules; the system will not include a comprehensive tutorial.
*   **Dependency:** The target machines for end-users must have a compatible JVM (version 1.2 or later) installed.
*   **Dependency:** For multiplayer games, clients must have network connectivity to the machine hosting the server application.

---

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Game Session Management
*   **FR1.1 (Single-Player Start):** The system shall allow a user to start a new single-player game from the client application's main menu.
*   **FR1.2 (Multiplayer Server Hosting):** The system shall allow a user to start the server application, which will listen for incoming client connections on a configurable TCP port.
*   **FR1.3 (Multiplayer Game Creation):** A connected client shall be able to create a new multiplayer game lobby, specifying a game name.
*   **FR1.4 (Multiplayer Game Joining):** A connected client shall be able to view a list of available game lobbies and join an existing lobby with an empty seat.
*   **FR1.5 (Game Start):** The creator of a multiplayer game lobby shall be able to start the game once the lobby has between 2 and 4 players.

##### 3.1.2 Core Gameplay & Rule Enforcement
*   **FR2.1 (Tile Management):** The system shall correctly initialize, shuffle, and deal 136 tiles (standard Chinese set) to four wall stacks and subsequently to four players.
*   **FR2.2 (Turn Flow):** The system shall enforce the correct turn sequence: drawing from the wall or claiming a discard, then discarding a tile.
*   **FR2.3 (Discard Pile):** The system shall maintain a visible, ordered discard pile for each player.
*   **FR2.4 (Tile Claims):** The system shall detect when a discarded tile completes a Pong, Kong, or Chow for another player and give that player priority to claim it according to Mahjong rules.
*   **FR2.5 (Winning Hand Detection):** The system shall automatically detect when a player's hand meets the criteria for a standard Mahjong (four sets and a pair) and declare that player the winner.
*   **FR2.6 (Score Calculation):** Upon a win, the system shall calculate the basic score for the winning hand based on standard Chinese scoring rules.

##### 3.1.3 User Interface
*   **FR3.1 (Board Rendering):** The GUI shall display all game elements: each player's hand (concealed from others), the discard area, the wall, and the current player's indicator.
*   **FR3.2 (Tile Interaction):** The user shall be able to select a tile from their hand by clicking on it with the mouse.
*   **FR3.3 (Action Controls):** The GUI shall provide clear buttons or prompts for actions such as "Discard Selected Tile," "Declare Pong/Kong/Chow," and "Declare Mahjong."
*   **FR3.4 (Game State Feedback):** The system shall display status messages to inform the player of game events (e.g., "Player East discarded 5 Bamboo," "It's your turn," "Player South has declared Mahjong!").

##### 3.1.4 Computer Opponent (AI)
*   **FR4.1 (Autonomous Play):** The AI shall be able to perform all standard game actions without human intervention: draw, discard, claim discards for Pong/Kong/Chow, and declare Mahjong.
*   **FR4.2 (Rule-Based Strategy):** The AI shall employ a basic rule-based strategy for tile discarding and claim decisions, prioritizing the completion of its hand.

##### 3.1.5 Network Communication
*   **FR5.1 (Client Connection):** The client shall establish and maintain a persistent TCP socket connection to the server for the duration of a multiplayer session.
*   **FR5.2 (State Synchronization):** The server shall broadcast game state changes (tile draws, discards, claims) to all clients in a game to keep their GUIs synchronized.
*   **FR5.3 (Input Relay):** The client shall send player actions to the server, which shall validate and relay them to other clients.

#### 3.2 External Interface Requirements

##### 3.2.1 User Interfaces
*   The client shall present a main menu with options: "Single Player," "Join Multiplayer Game," "Host Server," and "Exit."
*   Game screen layout shall be intuitive, with a central board view and a clear, non-obtrusive control panel.

##### 3.2.2 Hardware Interfaces
*   The system requires standard input devices (mouse, keyboard).
*   The server requires a network interface card for TCP/IP communication.

##### 3.2.3 Software Interfaces
*   **Platform:** JDK 1.2 APIs for GUI (`java.awt`), networking (`java.net`), and core functionality.
*   **Protocol:** The client and server shall communicate using a proprietary application-layer protocol over TCP sockets, with messages for actions, game state, and chat.

##### 3.2.4 Communications Interfaces
*   The server shall listen for client connections on TCP port `10500` (configurable via command line argument).
*   Communication shall use a text-based or lightweight binary protocol for efficiency.

#### 3.3 System Features
*(This section would typically elaborate on high-priority features by repeating FRs from 3.1 in a more narrative, scenario-driven format. For brevity, it is omitted here as the FRs are already detailed.)*

#### 3.4 Non-Functional Requirements

##### 3.4.1 Performance Requirements
*   **PR1:** The AI response time shall not exceed **60 seconds** for any game decision (as per constraint).
*   **PR2:** The GUI shall respond to local user input (e.g., highlighting a tile) within **100 milliseconds**.
*   **PR3:** In multiplayer mode, the time between a player's action and its visual effect on all other clients shall be less than **2 seconds** under normal network conditions.

##### 3.4.2 Safety & Security Requirements
*   The system does not require user authentication or handle sensitive personal data. No specific safety/security requirements are defined beyond basic network stability.

##### 3.4.3 Software Quality Attributes
*   **Maintainability:** The code shall be modular, with clear separation between GUI, game logic, AI, and network modules.
*   **Portability:** The system shall function identically across Windows, Mac OS, and Unix platforms with a compatible JVM, as per constraint.
*   **Reliability:** The client application shall not crash due to invalid user input. The server shall be able to handle a client disconnection gracefully, pausing the game or replacing the player with an AI.

#### 3.5 Design & Implementation Constraints
1.  The entire codebase must be written in **Java (JDK 1.2)**.
2.  The server architecture must be capable of handling **10 concurrent game sessions** (40 connected clients) as a minimum scalability target.
3.  Third-party libraries or native code are not permitted unless explicitly included in the JDK 1.2 specification.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Manager | | | |
| Lead Developer | | | |
| QA Lead | | | |