# Software Requirements Specification (SRS)
## MultiMahjong Client-Server Game
**Version:** 1.0
**Date:** [Date of Document Creation]
**Authors:** K-Team
**Client:** Steve Goschnick, Managing Director, Solid Software Pty Ltd
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the MultiMahjong system. It is intended to serve as a complete description of the system to be developed, providing a basis for mutual understanding between the client (Solid Software Pty Ltd), the development team (K-Team), and other stakeholders. This document will guide the design, implementation, testing, and delivery phases of the project.

#### 1.2 Document Conventions
*   **Levels:** Features are categorized as Level 1 (Core), Level 2 (Enhanced), or Level 3 (Future). This SRS primarily details Level 1 requirements.
*   **Keywords:** `MUST`, `SHALL`, `REQUIRED` indicate mandatory requirements. `SHOULD`, `RECOMMENDED` indicate desirable but not mandatory features. `MAY`, `OPTIONAL` indicate permissible actions.
*   **Formatting:** Technical terms and entity names are presented in `code` font.

#### 1.3 Project Scope
The MultiMahjong project is a client-server computer game that enables users to play Chinese Mahjong in single-player (standalone) or multiplayer (networked) modes. The core system consists of two main components:
1.  **MultiMahjongServer:** Manages networked game sessions, player connections, and game state synchronization.
2.  **MultiMahjongClient:** Provides the user interface for players, enforces game rules locally, and communicates with the server or manages local Computer Opponents (COs).

**In-Scope (Level 1):**
*   Support for 1 to 4 players per game (mix of human players and client-side COs).
*   Adherence to standard Chinese Mahjong rules for move validation, scoring, and winning conditions.
*   TCP/IP-based network communication for multiplayer games.
*   A graphical user interface (GUI) for game interaction.
*   Basic error handling and user notification.

**Out-of-Scope / Deferred:**
*   Advanced network security (e.g., encryption) - Data privacy is not a requirement.
*   Multi-language support (Level 3).
*   Server-side Computer Opponent logic (Level 3).
*   Advanced features such as chat, complex animations, and a server admin GUI are designated as Level 2 or Level 3.

#### 1.4 References
*   Sun Microsystems Java Coding Standards.
*   JDK 1.2 API Documentation.
*   Standard reference for Chinese Mahjong rules (to be specified by client).

### 2. Overall Description

#### 2.1 Product Perspective
MultiMahjong is a new, self-contained software product. It will interact with the host operating system's networking stack and graphical subsystem. The architectural model is client-server for multiplayer games and standalone client for single-player games.

#### 2.2 User Classes and Characteristics
| Stakeholder | Role | Characteristics & Key Requirements |
| :--- | :--- | :--- |
| **Steve Goschnick** | Client / Sponsor | Provides commercial and high-level functional requirements. Responsible for final product acceptance. |
| **K-Team** | Developer | Designs, implements, tests, and delivers the system as per this SRS. |
| **Player (End User)** | Primary Actor | Uses the `MultiMahjongClient` to play the game. Requires an intuitive GUI and correct rule enforcement. Skill levels range from novice to expert. |
| **Server Administrator** | Secondary Actor | Operates the `MultiMahjongServer`. Requires clear setup, configuration, and troubleshooting documentation. |
| **Computer Opponent (CO)** | System Actor | An automated player entity. MUST follow game rules, calculate moves within performance constraints, and MUST NOT access hidden game state information (other players' concealed tiles). |

#### 2.3 Operating Environment
*   **Software:** Java Runtime Environment (JRE) version 1.2 or compatible.
*   **Platform:** The application SHALL be cross-platform, running on Windows, Mac OS, and Unix-based systems supporting JDK 1.2.
*   **Network:** TCP/IP network connectivity is required for multiplayer functionality.

#### 2.4 Design and Implementation Constraints
1.  The system SHALL be developed using Java, adhering to JDK 1.2 APIs.
2.  Code SHALL follow Sun Microsystems coding standards.
3.  The client-server communication SHALL use plain TCP/IP sockets without encryption.
4.  The Computer Opponent logic SHALL reside and execute solely on the client side.

#### 2.5 Assumptions and Dependencies
*   It is assumed the end-user's machine meets the minimum requirements for JDK 1.2.
*   For multiplayer games, a functional network connection to a running `MultiMahjongServer` is assumed.
*   The project's successful completion is dependent on the final sign-off of this SRS by the client.

### 3. System Features and Requirements

#### 3.1 Game Session Management
**Description:** This feature handles the creation, joining, configuration, and termination of Mahjong game sessions.

**3.1.1 Functional Requirements:**
*   **FR-1.1:** The client SHALL provide a main menu with options: "New Single Player Game," "New Multiplayer Game," and "Join Existing Game."
*   **FR-1.2:** When creating a new game (single or multiplayer), the user MUST be able to configure:
    *   Player name (required).
    *   Player icon (optional).
    *   Score limit for the game (required).
    *   Number and type of opponents (for single-player: 3 COs; for multiplayer: 0-3 human/CO mix).
*   **FR-1.3:** For "Join Existing Game," the client SHALL fetch and display a list of available games from the server. The user SHALL select a game and provide their name/icon to join.
*   **FR-1.4:** The server SHALL uniquely identify each game with a `gameID` and manage a list of active sessions (`ServerSession`).
*   **FR-1.5:** A standard game SHALL consist of four rounds, each associated with a prevailing wind (East, South, West, North). The game ends when the fourth round is complete or the score limit is reached.

#### 3.2 Core Gameplay & Rule Enforcement
**Description:** This feature manages the turn-based flow of the game, tile manipulation, and enforces all rules of Chinese Mahjong.

**3.2.1 Functional Requirements:**
*   **FR-2.1:** The system SHALL correctly initialize a game by randomizing a full set of 144 Mahjong tiles and assigning initial hands to players.
*   **FR-2.2:** The system SHALL manage a turn sequence where players, in clockwise order, can:
    *   Pick a tile from "The Wall."
    *   Discard a tile from their hand to the "Discard" pile.
    *   Claim another player's discard to form a Chow, Pung, Kong, or to declare Mahjong (winning hand), following standard Chinese Mahjong precedence rules.
*   **FR-2.3:** The `MultiMahjongClient` SHALL validate all player moves locally against Chinese Mahjong rules before sending them to the server (multiplayer) or applying them (single-player).
*   **FR-2.4:** The client SHALL clearly indicate to the user all eligible actions (e.g., Chow, Pung, Kong, Mahjong) when a discard is made or a tile is drawn.
*   **FR-2.5:** The system SHALL correctly calculate and update scores for all players after a hand is won.
*   **FR-2.6:** The game state, including all tile positions (`The Wall`, `Discard`, `Dead Tile`, `Exposed Set`, `Revealed Kong`), player hands, scores, and prevailing wind, SHALL be synchronized across all clients in a multiplayer session via the server.

#### 3.3 Computer Opponent (CO)
**Description:** This feature provides automated players for single-player games or to fill slots in multiplayer games.

**3.3.1 Functional Requirements:**
*   **FR-3.1:** The CO SHALL make all decisions (pick, discard, claim) based solely on publicly available information: its own hand, exposed sets on the table, and the discard pile.
*   **FR-3.2:** The CO SHALL NOT have access to the concealed tiles of other players or the unrevealed tiles in The Wall.
*   **FR-3.3:** The CO MUST calculate and execute its move within 1 minute of its turn becoming active.

#### 3.4 User Interface
**Description:** This feature provides the visual and auditory interface for the player.

**3.4.1 Functional Requirements:**
*   **FR-4.1:** The GUI SHALL display each player's seat, wind, score, and icon.
*   **FR-4.2:** The GUI SHALL visually represent the player's own hand (concealed), other players' exposed sets, the discard pile, and the remaining wall.
*   **FR-4.3:** The GUI SHALL update its state within 1 second of receiving new game state data from the server or local engine.
*   **FR-4.4:** The GUI SHALL provide clear visual or textual prompts for user actions.
*   **FR-4.5:** (Level 2) The GUI MAY support basic sound effects for game events.

#### 3.5 Networking & Communication
**Description:** This feature handles all data exchange between the `MultiMahjongClient` and `MultiMahjongServer`.

**3.5.1 Functional Requirements:**
*   **FR-5.1:** The client and server SHALL communicate via a persistent TCP/IP socket connection using a defined application-layer protocol.
*   **FR-5.2:** The server SHALL broadcast game state updates to all clients in a session following any valid move.
*   **FR-5.3:** The server SHALL be capable of handling up to 10 simultaneous game sessions (supporting up to 40 connected clients).

#### 3.6 Error Handling & Robustness
**Description:** This feature manages system errors and exceptional conditions gracefully.

**3.6.1 Functional Requirements:**
*   **FR-6.1:** The client SHALL display user-friendly dialogue boxes for both fatal and non-fatal errors, providing relevant troubleshooting information.
*   **FR-6.2:** In case of a network disconnection in a multiplayer game, the client SHALL attempt to reconnect and, if unsuccessful, inform the user and exit gracefully to the main menu.
*   **FR-6.3:** (Level 2) If a human player disconnects mid-game, the system MAY replace them with a Computer Opponent for the remainder of that game.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Graphical Client (MultiMahjongClient):** A windowed application with mouse and keyboard input. Specific graphical details (themes, tile artwork, layout) are to be finalized in the Software Design Document (SDD).
*   **Server Console (MultiMahjongServer):** A command-line interface for startup, shutdown, and basic logging output. (A Level 2 GUI for server admin is deferred).

#### 4.2 Hardware Interfaces
None specified.

#### 4.3 Software Interfaces
*   **JDK 1.2:** The system SHALL interface with the Java Development Kit version 1.2 for all core functionality, including AWT for GUI and `java.net` for TCP/IP communication.
*   **Operating System:** The Java runtime will interface with the host OS for window management, networking, and file I/O (for logs and preferences).

#### 4.4 Communication Interfaces
*   **Protocol:** A proprietary, plain-text or binary application protocol over TCP/IP.
*   **Port:** The `MultiMahjongServer` SHALL listen on a configurable TCP port (default to be specified in SDD).

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   **PER-1:** A Computer Opponent (CO) SHALL calculate and execute its move within **1 minute** of its turn starting.
*   **PER-2:** The client's local rule engine SHALL calculate all possible valid moves (Chow, Pung, Kong, Mahjong) for a player within **5 seconds** of a state change.
*   **PER-3:** The server SHALL support a minimum of **10 concurrent game sessions** with up to 4 players each, without critical degradation of performance.

#### 5.2 Reliability & Availability
*   **REL-1:** The client SHALL handle network failures gracefully, allowing the user to return to the main menu without application crash.
*   **REL-2:** (Level 2) The server SHALL maintain basic transaction logs to aid in troubleshooting.

#### 5.3 Security Requirements
*   **SEC-1:** The system is NOT REQUIRED to implement encryption for network traffic. Data transmitted is not considered private.
*   **SEC-2:** The system SHALL NOT store sensitive user data (e.g., passwords).

#### 5.4 Compliance
*   **COMP-1:** The game logic SHALL comply with the standard rules of Chinese Mahjong as specified by the agreed-upon reference.
*   **COMP-2:** The source code SHALL comply with Sun Microsystems Java Coding Standards.

### 6. Domain Model & Data Definitions
Key domain entities and their attributes are summarized below. Detailed class diagrams will be provided in the SDD.

*   **`Player`:** `name` (String, required), `icon` (Image), `score` (int), `windPosition` (Enum), `isHuman` (boolean).
*   **`Game`:** `gameID` (String, unique), `scoreLimit` (int, required), `currentRound` (int), `windOfRound` (Enum), `players` (List<Player>).
*   **`Tile`:** `tileID` (String, unique), `suit` (Enum: Character, Bamboo, Circle, Honor), `value` (int), `position` (Enum: InWall, InHand[player_ref], Discarded, InExposedSet, InRevealedKong).
*   **`Move`:** `type` (Enum: Pick, Discard, Chow, Pung, Kong, Mahjong), `tile` (reference to Tile), `player` (reference to Player), `timestamp` (DateTime).
*   **`ComputerOpponent`:** `abilityLevel` (int), `player` (reference to Player).
*   **`ServerSession`:** `sessionID` (String, unique), `connectedClients` (List<Socket>), `game` (reference to Game).

### 7. Acceptance Criteria
| ID | Scenario | Expected Outcome |
| :--- | :--- | :--- |
| **AC-1** | **Given** a user starts the client, **when** they choose "new single-player game," enter a name and score limit, **then** the game begins with three COs and all moves are validated according to Chinese Mahjong rules. | Game starts correctly. Rules are enforced. |
| **AC-2** | **Given** an active multiplayer game with four human players, **when** Player A discards a tile, **then** the other three clients are immediately notified and their interfaces enable claim buttons (Chow/Pung/Kong/Mahjong) only if their hand legally permits it. | Real-time sync and correct rule-based UI enabling. |
| **AC-3** | **Given** a game with an active CO, **when** it becomes the CO's turn, **then** the CO selects and executes a valid move within 60 seconds without any illegal access to hidden tiles. | Timely, legal autonomous move. |
| **AC-4** | **Given** a running multiplayer client, **when** a non-fatal network error (e.g., temporary timeout) occurs, **then** a descriptive dialogue box is shown to the user and the game attempts to continue once connectivity is restored. | Graceful error handling and recovery. |

### 8. Appendices

#### 8.1 Undecided Issues & TBD
The following detailed design decisions are deferred and will be addressed in the Software Design Document (SDD) or later phases. Responsibility lies with the K-Team.
1.  Graphical details of the GUI (tile artwork, board layout, animations).
2.  Internal `Tile` and `Hand` class structure and data representation.
3.  Implementation details for a "High Scores" list (Level 2).
4.  Sound effect file formats and playback library (Level 2).
5.  Use of animation for tile movement (Level 3).
6.  Framework for multi-language support and Unicode handling (Level 3).
7.  Design and protocol for in-game chat functionality (Level 3).
8.  Requirements and design for a server administration GUI (Level 2).

#### 8.2 Risk Register
| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| Network latency disrupts gameplay. | Medium | High | Optimize packet size/frequency; implement client-side prediction where possible; set reasonable timeouts. |
| CO algorithm is computationally slow (>1 min). | Medium | High | Implement strict limits on look-ahead depth; use efficient heuristics; profile and optimize code early. |
| Cross-platform issues with JDK 1.2 AWT. | Medium | Medium | Early and frequent testing on target platforms: Windows, Mac, and Unix. |
| Bugs due to complexity of Mahjong rules. | High | High | Develop a comprehensive suite of unit tests covering all rule permutations and edge cases. |
| GUI is not intuitive for novice players. | Medium | Medium | Conduct usability testing with participants of varying Mahjong skill levels during development. |

---
**Sign-off:**

**Approved by Client (Solid Software Pty Ltd):**
___________________________
Steve Goschnick, Managing Director
Date: _______________________

**Approved by Development Team (K-Team):**
___________________________
Lead Developer, K-Team
Date: _______________________