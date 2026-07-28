# Software Requirements Specification (SRS)
## For MultiMahjong Project
**Version:** 1.0  
**Date:** [Current Date]  
**Authors:** K-Team  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the MultiMahjong system. The intended audience includes the project stakeholders—Steve Goschnick (Client), Anthony Senyard (Supervisor), the K-Team (Development Team), and future maintainers. This document serves as the foundation for design, implementation, testing, and project acceptance.

#### 1.2 Project Scope
MultiMahjong is a commercial, client-server computer game that enables single-player and multiplayer Mahjong over TCP/IP networks. The system comprises a `MultiMahjongServer` and a `MultiMahjongClient`. The client will be sold to end-users, while the server will be hosted by the client (user) for multiplayer sessions.

**In-Scope:**
*   Client-server architecture supporting up to four players (human or computer-controlled) per game over TCP/IP.
*   Single-player mode featuring one human player and three computer opponents.
*   Gameplay adhering to standard Chinese Mahjong rules, including tile drawing, discarding, claiming (Chow, Pung, Kong), hand formation, and scoring.
*   A basic graphical user interface (GUI) for the client application, designed for an 800x600 screen resolution.
*   Essential user and administrator documentation covering installation and operation.

**Out-of-Scope:**
*   Advanced artificial intelligence for computer opponents (e.g., look-ahead, strategic planning).
*   Real-time chat functionality between players.
*   Multi-language or Unicode support.
*   Graphical administration interface for the server.
*   Complex animations or advanced sound effects within the client.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **SRS:** Software Requirements Specification
*   **TCP/IP:** Transmission Control Protocol/Internet Protocol
*   **GUI:** Graphical User Interface
*   **JDK:** Java Development Kit
*   **Chow:** Claiming a discarded tile to form a sequence of three consecutive numbers in the same suit.
*   **Pung:** Claiming a discarded tile to form a set of three identical tiles.
*   **Kong:** Claiming a discarded tile or drawing from the wall to form a set of four identical tiles.
*   **Mahjong:** The winning condition, a complete hand of four sets and one pair.

#### 1.4 References
*   Sun Microsystems Java Coding Standards (for JDK 1.2)
*   Standard Chinese Mahjong Rule Set (to be specified in detail in a separate game rules appendix).

#### 1.5 Document Overview
The remainder of this document details the overall description of the product, its specific requirements, and appendices. Specific requirements are organized by system features and external interfaces.

### 2. Overall Description

#### 2.1 Product Perspective
MultiMahjong is a new, self-contained software product. It operates in a networked environment where the server component manages game sessions and the client component provides the user interface. The system interacts with the host operating system and the network stack.

#### 2.2 Product Functions (High-Level)
1.  **Game Session Management:** Create, join, and manage multiplayer game sessions over a network.
2.  **Single-Player Simulation:** Facilitate a complete Mahjong game against three computer-controlled opponents.
3.  **Gameplay Engine:** Enforce Chinese Mahjong rules, manage the tile wall, player turns, discards, claims, and score calculation.
4.  **User Interaction:** Provide a visual representation of the game state (player's hand, discards, exposures) and accept player input.
5.  **Network Communication:** Facilitate reliable, state-synchronized communication between clients and the server.

#### 2.3 User Characteristics
*   **End-User / Player:** Expected to have basic computer literacy and familiarity with Mahjong rules. No advanced technical knowledge is required to play.
*   **Server Administrator:** Requires knowledge of TCP/IP networking to configure hostnames, IP addresses, and ports for server setup. Technical proficiency is assumed.

#### 2.4 Constraints
1.  **Technical:** Must be developed using JDK 1.2, adhering to Sun Microsystems coding standards.
2.  **Platform:** Must be compatible with Windows 95/98/NT, Macintosh OS 8, and Unix (Solaris).
3.  **Hardware:** Must run on minimum hardware: 100 MHz processor, 32 MB RAM, 10 MB disk space, and a display supporting 800x600 resolution.
4.  **Network:** Multiplayer functionality is dependent on a functional TCP/IP network connection.
5.  **Project:** All Level 1 (Priority 1) requirements outlined in this document are mandatory for project acceptance.

#### 2.5 Assumptions and Dependencies
*   A valid TCP/IP network connection is available for multiplayer games.
*   The Java Runtime Environment (JRE) compatible with JDK 1.2 is installed on target systems.
*   End-users possess a fundamental understanding of Chinese Mahjong rules.

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 User Interfaces
*   **Client GUI:** A graphical interface within an 800x600 window. It shall include:
    *   A visual representation of the player's hand (14 tiles).
    *   A view of the current discard pile.
    *   A view of exposed sets (Chow, Pung, Kong) for all players.
    *   Indicators for current turn, player wind, and game wind.
    *   Controls for drawing/discarding a tile and declaring Chow, Pung, Kong, or Mahjong.
    *   A game log or status area for system messages.
    *   Menu options for "New Game," "Join Game," "Exit," and "Help."
*   **Server Interface:** A command-line interface (CLI) for startup, shutdown, and basic status reporting (e.g., "Server started on port X," "Game Y created").

##### 3.1.2 Hardware Interfaces
The software shall operate on the specified minimum hardware configuration without specialized hardware.

##### 3.1.3 Software Interfaces
*   **Operating System:** JDK 1.2 APIs for file I/O, networking, and GUI (AWT).
*   **Network:** TCP/IP sockets for all client-server communication.

##### 3.1.4 Communications Interfaces
The `MultiMahjongServer` shall listen for incoming TCP connections on a configurable port (default: e.g., 12345). Clients shall connect to the server using its IP address/hostname and port number. A proprietary application-layer protocol will be defined to transmit game commands and state.

#### 3.2 Functional Requirements

##### 3.2.1 Game Session Management
*   **FR1: Create Multiplayer Game.** The client shall allow a user to host a new game by specifying a game name. The server shall create the game session and assign the creator as Player 1 (East Wind).
*   **FR2: Join Multiplayer Game.** The client shall allow a user to browse a list of available games on a server and join one as a vacant player (human or computer slot).
*   **FR3: Start Game.** The hosting player shall be able to start the game once four players (human or computer) have joined.
*   **FR4: Single-Player Game.** The client shall allow a user to start a local game immediately with three computer opponents without network interaction.

##### 3.2.2 Core Gameplay
*   **FR5: Tile Management.** The system shall correctly initialize, shuffle, and manage a wall of 144 Mahjong tiles according to Chinese rules.
*   **FR6: Turn Progression.** The system shall manage turn order, including drawing from the wall, discarding a tile, and transitioning turns based on claims.
*   **FR7: Claim Validation.** Upon a discard, the system shall calculate and notify downstream players of valid claims (Chow, Pung, Kong, Mahjong) according to rule priority.
*   **FR8: Move Execution.** The system shall allow a player to execute a valid move (Draw, Discard, Chow, Pung, Kong, Declare Mahjong) and update the game state for all participants.
*   **FR9: Score Calculation.** The system shall automatically calculate scores for the winning hand based on standard Chinese Mahjong scoring rules and update player totals.

##### 3.2.3 User Interface & Feedback
*   **FR10: State Display.** The client shall continuously and accurately display the user's hand, the discard pile, all players' exposed sets, and the current game status (turn, winds, scores).
*   **FR11: Move Notification.** The client shall prominently notify the user when they have a valid claim opportunity and provide a clear method to act upon it.
*   **FR12: Game Log.** The client shall maintain a log of significant game events (e.g., "Player East discarded 5 Bamboo," "Player North declared Pung").

##### 3.2.4 Computer Opponent (Basic)
*   **FR13: Autonomous Play.** The computer opponent shall be able to perform all basic game actions (draw, discard) without human intervention.
*   **FR14: Basic Claiming.** The computer opponent shall recognize and execute valid Chow, Pung, Kong, and Mahjong claims based on a simple rule set (e.g., always claim Mahjong, claim Pung/Kong if available).

##### 3.2.5 Server Administration
*   **FR15: Server Execution.** The server shall run as a persistent process, accepting client connections on the specified TCP port.
*   **FR16: Game Lifecycle Management.** The server shall manage the lifecycle of multiple simultaneous games (creation, active play, termination).

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance Requirements
*   **PERF1:** Computer opponents shall respond with a discard or claim decision within **60 seconds** of their turn becoming active.
*   **PERF2:** The server shall support up to **10 simultaneous games** (40 connected clients) without significant degradation in responsiveness (e.g., network latency < 500ms for game state updates).
*   **PERF3:** The client shall calculate and display all possible valid claims for the human player within **5 seconds** of a tile being discarded.

##### 3.3.2 Safety & Security Requirements
*   (Not a primary concern for this release. Basic network error handling is covered under Reliability.)

##### 3.3.3 Software Quality Attributes
*   **Reliability:** The client shall gracefully handle server disconnection. The server shall not crash due to a single client disconnecting.
*   **Availability:** The server shall be available to accept connections whenever the host process is running.
*   **Maintainability:** Code shall adhere to Sun Microsystems Java coding standards for JDK 1.2.
*   **Portability:** The system shall execute identically on Windows 95/98/NT, Mac OS 8, and Solaris without code modification.

### 4. Success Metrics
The project will be deemed successful upon verification of the following:
1.  All Level 1 (Priority 1) functional requirements are implemented and tested.
2.  The performance requirements (PERF1, PERF2, PERF3) are met under standard test conditions.
3.  The software operates correctly on all three target platforms (Windows, Mac, Solaris).
4.  Essential user and administrator documentation is delivered and deemed satisfactory by the stakeholder (Steve Goschnick).

### 5. Undecided Issues / Open Items
The following items require future resolution but are not required for the initial release:
1.  Finalized GUI layout, control placement, and graphic design.
2.  Specific internal data structures for tile and game state management.
3.  Inclusion of "Undo" or "Save Game" features in single-player mode.
4.  Support for user-uploaded custom tile icons or background images.
5.  Implementation of alternative Mahjong rule variations (e.g., Hong Kong, Japanese).

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Client | Steve Goschnick | | |
| Supervisor | Anthony Senyard | | |
| Development Lead | K-Team Representative | | |