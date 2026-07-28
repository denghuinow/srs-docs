# Software Requirements Specification (SRS)
## MultiMahjong Client-Server Game
**Version:** 1.0
**Date:** [Date of Creation]
**Prepared for:** Steve Goschnick, Managing Director, Solid Software Pty Ltd
**Prepared by:** K-Team Development Team
**Supervisor:** Anthony Senyard

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the MultiMahjong system. It is intended to serve as a complete description of the system to be developed, providing a basis for design, implementation, testing, and project management. The primary audiences for this document are the K-Team developers, the client (Solid Software Pty Ltd), and the academic supervisor.

#### 1.2 Document Conventions
This document uses standard SRS formatting conventions. Requirements are uniquely identified with labels (e.g., `FR-001`, `NFR-001`). User stories are referenced as `US-001`. Markdown is used for structure, with headers, lists, and tables for clarity.

#### 1.3 Project Scope
MultiMahjong is a client-server computer game that enables single-player and multiplayer Mahjong over TCP/IP networks. The system comprises a central **MultiMahjongServer** application that manages game sessions and logic, and **MultiMahjongClient** applications that provide the user interface. The game supports up to four human players, with computer opponents (COs) automatically filling empty slots in single-player or partially filled multiplayer games. The product is targeted at Mahjong enthusiasts with basic computer skills and will be commercially distributed by Solid Software Pty Ltd.

**In-Scope:**
*   Implementation of standard Chinese Mahjong rules.
*   Single-player mode with up to three computer opponents.
*   Multiplayer mode over a network for 2-4 human players.
*   Client GUI supporting mouse and keyboard input at 800x600 resolution.
*   Server application for session management and state synchronization.
*   Persistent storage of user preferences and high scores.
*   Comprehensive user and administrator documentation.

**Out-of-Scope:**
*   Support for other Mahjong variants (e.g., Japanese Riichi, American).
*   Peer-to-peer networking without a central server.
*   A web-based or mobile client interface.
*   Advanced social features (e.g., friend lists, player profiles).
*   In-game monetization or microtransactions.

#### 1.4 References
*   Official Chinese Mahjong Competition Rules.
*   Java Development Kit (JDK) 1.2 API Documentation.
*   Project Charter and initial statement of work from Solid Software Pty Ltd.

### 2. Overall Description

#### 2.1 Product Perspective
MultiMahjong is a new, standalone desktop application. It is not a component of a larger system but must interoperate with standard TCP/IP networks. The server-client architecture is depicted below:

```
[Client 1] <-----> [MultiMahjongServer] <-----> [Client 2]
[Client 3] <-----> (Game Session Mgmt,   <-----> [Client 4]
                     State Synchronization,
                     Computer Opponent Logic)
```

#### 2.2 Product Functions (High-Level)
*   **Game Session Management:** Create, list, join, and terminate multiplayer game sessions.
*   **Rule Enforcement:** Validate all player moves according to Chinese Mahjong rules.
*   **Turn-Based Play:** Manage game flow, player turns, and win conditions.
*   **Computer Opponents:** Provide AI players of configurable difficulty for single-player games.
*   **State Synchronization:** Maintain a consistent game state across all connected clients via the server.
*   **User Preference Management:** Save and load user settings (name, icon, audio, default game type).
*   **High Score Tracking:** Record and display top scores for single and multiplayer games.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Player** | Mahjong enthusiast with basic PC skills (mouse, keyboard). May play alone or with friends. | Intuitive interface, clear rule guidance, ability to play against AI or humans. |
| **Multiplayer Game Creator** | A Player who initiates a new multiplayer session. | Ability to configure game parameters (player count, score limit). |
| **Server Administrator** | Technical personnel responsible for deploying the server. | Easy installation, clear logging, stable operation, and management of concurrent games. |

#### 2.4 Operating Environment
*   **Software:**
    *   **Client & Server:** Java Runtime Environment (JRE) from JDK 1.2 or later.
    *   **Operating Systems:** Microsoft Windows 95/98/NT, Apple Mac OS 8, Sun Solaris.
*   **Hardware:**
    *   **Client:** PC capable of running the above OSes with 800x600 display (16-bit color), mouse, keyboard, and network interface card (NIC).
    *   **Server:** A dedicated or shared machine on the network with a stable IP address and sufficient RAM/CPU to handle the scalability requirement (see Section 3.5).

#### 2.5 Design and Implementation Constraints
1.  The application must be written in Java to ensure cross-platform compatibility.
2.  Communication between client and server must use TCP/IP sockets.
3.  The client graphical user interface (GUI) must be designed to fit within an 800x600 pixel window.
4.  All game logic and rule validation must reside on the server to prevent cheating.

#### 2.6 User Documentation
1.  **MultiMahjong User Guide:** Electronic (PDF) and printed manual covering game installation, client usage, game rules overview, and preference settings.
2.  **MultiMahjong Server Administrator Guide:** Electronic (PDF) and printed manual covering server installation, network configuration, troubleshooting, and log file interpretation.

#### 2.7 Assumptions and Dependencies
*   **Assumption:** Target users have a fundamental understanding of Mahjong rules.
*   **Assumption:** Network firewalls will be configured to allow traffic on the server's designated port.
*   **Dependency:** The Java JDK 1.2 must be available and installable on all target operating systems.

### 3. System Features

This section details the functional requirements derived from user stories and key processes.

#### 3.1 Feature: Game Session Management
*   **Description:** Allows users to create new games or join existing ones.
*   **Stimulus/Response:** User selects "New Game" or "Join Game" from the client main menu.
*   **Functional Requirements:**
    *   `FR-001` The client shall allow the user to choose between "Single Player" and "Multiplayer" game modes. *(Links to US-001)*
    *   `FR-002` In "Multiplayer" > "New Game" mode, the client shall allow the creator to set the total player count (2-4) and a score limit for the session. *(Links to US-002)*
    *   `FR-003` The client shall send a game creation request to the server, which shall generate a unique GameID and set the session status to "Waiting."
    *   `FR-004` In "Multiplayer" > "Join Game" mode, the client shall retrieve and display a list of available game sessions (GameID, creator, player count) from the server.
    *   `FR-005` The server shall manage a list of active and waiting game sessions.
    *   `FR-006` For single-player games, the server shall automatically create a session with one human player and three computer opponents.

#### 3.2 Feature: Gameplay & Rule Enforcement
*   **Description:** Manages the core turn-based gameplay, including tile manipulation and rule validation.
*   **Stimulus/Response:** Player attempts a move (draw, discard, claim a tile for Pong/Kong/Chow, declare Mahjong).
*   **Functional Requirements:**
    *   `FR-007` The game shall follow standard Chinese Mahjong rules for a 4-player game with 136 tiles.
    *   `FR-008` The client shall provide visual indicators (e.g., highlighting, cursor change) for tiles that are valid move targets based on the current game state and active player. *(Links to US-003)*
    *   `FR-009` Upon any player action, the client shall send the move attempt to the server.
    *   `FR-010` The server shall validate every move attempt against the official game rules and current state before execution. *(Links to Key Process 4)*
    *   `FR-011` The server shall process valid moves, update the central game state, and broadcast the state change to all connected clients in the session. *(Links to US-004, Key Process 5)*
    *   `FR-012` The client shall update its display to reflect the new synchronized game state received from the server.
    *   `FR-013` The server shall manage turn order, determining the active player after each move. *(Links to Key Process 3)*

#### 3.3 Feature: Computer Opponent (CO)
*   **Description:** Provides AI players for single-player or incomplete multiplayer games.
*   **Stimulus/Response:** It becomes a CO's turn, or a CO has a reaction opportunity (e.g., claiming a discard).
*   **Functional Requirements:**
    *   `FR-014` The server shall host the logic for all computer opponents. *(Links to US-005)*
    *   `FR-015` When a game session requires a CO, the server shall instantiate a CO agent with a difficulty setting (Beginner/Intermediate/Advanced).
    *   `FR-016` The CO shall make moves (draw, discard, claim) based on the visible game state (its own hand, discards, and known melds).
    *   `FR-017` The CO's decision-making process shall complete and a move shall be sent to the game engine within 60 seconds under normal conditions.

#### 3.4 Feature: User Preferences & Data Persistence
*   **Description:** Saves user settings and game history between application sessions.
*   **Stimulus/Response:** User changes a setting or a game ends with a high score.
*   **Functional Requirements:**
    *   `FR-018` The client shall allow users to set a player name, select an icon, adjust sound volume/on/off, and set a default game type. *(Links to US-006)*
    *   `FR-019` The client shall save these preferences locally (e.g., to a file or registry) and reload them upon subsequent startups.
    *   `FR-020` At the end of a game, the client shall submit the player's name and score to the server for high score consideration.
    *   `FR-021` The server shall maintain a persistent high score list, storing `EntryID, PlayerName, Score, DateAchieved, GameType`.
    *   `FR-022` The client shall be able to request and display the top N high scores from the server.

#### 3.5 Feature: Server Administration & Reliability
*   **Description:** Ensures the server operates stably and provides information for administration.
*   **Functional Requirements:**
    *   `FR-023` The server shall relay all game state and chat data between clients in a session. *(Links to US-004)*
    *   `FR-024` The server shall support up to 10 simultaneous game sessions (up to 40 total connected clients). *(Links to NFR-002)*
    *   `FR-025` The server shall log operational events (startup, shutdown, game creation, errors) to a file with a configurable detail level.
    *   `FR-026` The system shall implement clear error handling, distinguishing between fatal errors (e.g., server cannot bind to port) and non-fatal errors (e.g., invalid move, network timeout). *(Links to NFR-005)*
    *   `FR-027` The server shall implement connection timeout and keep-alive mechanisms to handle disconnected clients gracefully.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   The client GUI shall be designed for 800x600 screen resolution with 16-bit color depth.
*   Primary navigation shall be via mouse click; keyboard shortcuts shall be available for common actions.
*   The interface shall include:
    *   A main menu (Single Player, Multiplayer, Preferences, High Scores, Exit).
    *   A game lobby for multiplayer session listing/creation.
    *   A game table view showing all player winds, scores, discards, and the current player's hand.
    *   Clear status messages and dialogs for errors and game events.

#### 4.2 Hardware Interfaces
*   Standard mouse and keyboard input are required.
*   A network interface card (NIC) is required for multiplayer functionality.

#### 4.3 Software Interfaces
*   **Java JDK 1.2:** The application shall interface with the Java Abstract Window Toolkit (AWT) for the GUI and `java.net` package for TCP/IP communication.
*   **Operating System:** The Java application shall run within the JVM provided by the host OS (Windows 95/98/NT, Mac OS 8, Solaris).

#### 4.4 Communications Interfaces
*   The client and server shall communicate via a proprietary application-layer protocol over TCP/IP.
*   The server shall listen on a user-configurable port (default: 17777).
*   The communication protocol shall be designed to serialize game state objects (Players, Tiles, Moves) and handle message types for moves, chat, and control commands.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-001`: The server shall validate a player's move and broadcast the result within 5 seconds under normal network load.
*   `NFR-002`: The server shall be scalable to support 10 concurrent game sessions (40 players) without significant degradation in response time.
*   `NFR-003`: Computer opponents shall calculate and submit their move within 60 seconds.

#### 5.2 Safety Requirements
*   Not applicable (this is a non-critical entertainment application).

#### 5.3 Security Requirements
*   The system is not designed for high-security environments. Basic security considerations include:
    *   The server should validate all incoming data to prevent malformed packets from crashing the service.
    *   No personal user data beyond player name and high scores is stored.

#### 5.4 Software Quality Attributes
*   **Usability (`NFR-004`):** The interface shall be usable by a Mahjong-literate person with minimal instruction. All game controls must be accessible via mouse.
*   **Reliability (`NFR-005`):** The server shall have an uptime goal of 99% during scheduled operation. Client errors shall not crash the server.
*   **Portability (`NFR-006`):** The client and server applications, delivered as Java bytecode (.class files or .jar), must execute identically on Windows 95/98/NT, Mac OS 8, and Solaris platforms with JDK 1.2 installed.
*   **Maintainability:** Code shall be well-commented and follow a documented architectural design.

### 6. Data Model (Domain Elements)
The core persistent entities of the system are summarized below. These inform database design or object serialization.

```java
// Conceptual Data Classes
class Player {
    String playerID; // Key
    String name;
    String iconPath;
    int score;
    WindPosition wind; // East, South, West, North
    ConnectionStatus status; // Connected, Disconnected
}

class GameSession {
    String gameID; // Key
    String creatorID;
    int scoreLimit;
    int playerCount;
    int roundNumber;
    SessionStatus status; // Waiting, Active, Finished
}

class Tile {
    String tileID; // Key
    TileType type; // Suit, Honor
    Suit suit; // Bamboo, Character, Circle (if type=Suit)
    int value; // 1-9 (if type=Suit)
    TilePosition position; // Wall, Hand, Discard, Meld
    String ownerPlayerID; // Null if in wall or discard
}

class Move {
    String moveID; // Key
    String playerID;
    String tileID;
    ActionType action; // Draw, Discard, Pong, Kong, Chow, Mahjong
    Timestamp timestamp;
    boolean valid;
}

class Preferences {
    String userID; // Key (may be machine-specific)
    String playerName;
    String iconPath;
    boolean soundEnabled;
    DefaultGameType defaultType;
}

class HighScore {
    int entryID; // Key
    String playerName;
    int score;
    Date dateAchieved;
    GameType gameType; // SinglePlayer, Multiplayer
}
```

### 7. Appendices

#### 7.1 Glossary
*   **CO:** Computer Opponent. An AI-controlled player.
*   **JDK:** Java Development Kit.
*   **JRE:** Java Runtime Environment.
*   **Mahjong:** The standard Chinese tile-based game implemented by this system.
*   **TCP/IP:** Transmission Control Protocol/Internet Protocol, the network communication standard used.

#### 7.2 Analysis Models
*(UML Use Case, Sequence, or State Diagrams would be included here in a full SRS.)*

#### 7.3 Issues List (Undecided/To Be Resolved)
1.  The specific algorithms and decision trees for Computer Opponent difficulty levels (Beginner/Intermediate/Advanced).
2.  The detailed specification of animation sequences for tile drawing, discarding, and melding.
3.  The exact format, fields, and rotation policy for the server log file.
4.  The implementation details for in-game chat functionality (UI, commands, filtering).
5.  The specific sound effects to be associated with game actions (draw, discard, win, error).
6.  The complete set and style of graphical icons available for player selection.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Client Representative | Steve Goschnick | _________________ | ________ |
| Development Lead | [K-Team Lead Name] | _________________ | ________ |
| Academic Supervisor | Anthony Senyard | _________________ | ________ |