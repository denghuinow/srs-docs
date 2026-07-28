# Software Requirements Specification (SRS)
## Triangulation Games Platform
**Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Triangulation Games software. The system is a cross-platform application designed to play, explore, and extend combinatorial triangulation games. It serves as both an entertainment platform for players and a research/development tool for academics and game developers. This SRS is intended for use by the project stakeholders, development team, and testers.

#### 1.2 Scope
The Triangulation Games software will provide:
*   A graphical interface for playing predefined triangulation games (Constructing, Transforming, Marking) in solitaire, human-vs-human, or human-vs-AI modes.
*   A game engine capable of managing game state, enforcing rules, detecting end conditions, and scoring.
*   A configuration system for setting up games, including selection of game type, opening position, and player types.
*   A persistence system for saving and loading game sessions.
*   An extensibility framework allowing the dynamic loading of new game definitions and AI player implementations from external files without recompilation of the core application.
*   Integrated help and documentation.

**Out of Scope:**
*   Network/multiplayer functionality over a network.
*   Creation of a game definition/AI integrated development environment (IDE).
*   Advanced graphics or animation beyond basic Swing components.
*   User account management or online leaderboards.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **AI:** Artificial Intelligence. A computer-controlled player.
*   **GUI:** Graphical User Interface.
*   **JRE:** Java Runtime Environment.
*   **SRS:** Software Requirements Specification.
*   **Triangulation:** A maximal planar graph, the fundamental game board for all games in this system.
*   **Game Session:** A single instance of gameplay, from setup to conclusion.
*   **Opening Position:** The initial state of the triangulation graph at the start of a game.

#### 1.4 References
*   Project Charter: "Balanced Summary: Triangulation Games Software Requirements"
*   Theoretical basis: [Reference to academic research article on combinatorial triangulation games]

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements. Appendices may contain supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
The Triangulation Games Platform is a standalone, desktop application built in Java. It relies on the Java Swing library for its GUI and uses a modular architecture to separate the core engine, GUI, game definitions, and AI modules. It interacts with the user and reads/writes configuration and game state files from the local filesystem.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Player / Basic User** | Seeks entertainment. May have limited technical expertise. Uses standard workstation. | Intuitive interface, clear game rules, responsive gameplay, ability to play vs. AI or friend. |
| **Researcher** | Academic focus. Requires precision and scientific correctness. | Accurate implementation of game theory, consistent interface for analysis, ability to explore edge cases. |
| **Game Developer** | Technically proficient, possibly non-programmer. Interested in game design. | Well-documented extensibility framework, simple file formats for defining games/AIs, clear error feedback. |
| **Development Team** | Software engineers building the system. | Clear requirements, modular design, maintainable codebase. |

#### 2.3 Operating Environment
*   **Software:** Must run on any operating system (Windows, Linux, macOS) with a JRE version 1.4 or later and a graphical desktop environment installed.
*   **Hardware:** Must be operable on low-end workstations typical of academic settings (circa 2004 specifications: ~1GHz CPU, 512MB RAM).

#### 2.4 Design and Implementation Constraints
1.  The application shall be developed in Java to ensure cross-platform compatibility.
2.  The GUI shall be implemented using the standard Java Swing toolkit.
3.  The system shall not require an external database; all data shall be stored in flat files.
4.  Core application code shall not require modification to add new games or AIs.

#### 2.5 User Documentation
The system shall include integrated, context-sensitive help accessible from the main interface. Comprehensive external documentation shall be provided for:
*   End-users: Game rules and interface guide.
*   Game Developers: Specification for the game definition file format.
*   AI Developers: API specification for implementing AI plug-ins.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** Users have basic familiarity with using mouse and keyboard-driven desktop applications.
*   **Dependency:** Correct functionality depends on the presence of a compatible JRE.
*   **Dependency:** Game logic depends on the theoretical correctness of the referenced academic paper's definitions.

### 3. System Features (Functional Requirements)

#### 3.1 Feature: System Startup and Main Interface
**Description:** The system shall present a main graphical window upon application launch.
**Requirements:**
*   **FR-1.1:** The main window shall contain a menu bar (File, Game, Options, Help), a central game visualization area, and a status/score panel.
*   **FR-1.2:** The system shall automatically scan designated directories (e.g., `./games/`, `./ais/`) for valid external game definition and AI implementation files at startup.

#### 3.2 Feature: Game Configuration and Setup
**Description:** The user shall be able to configure a new game session.
**Requirements:**
*   **FR-2.1:** The user shall be able to select a game type from a list of all loaded games (default and external).
*   **FR-2.2:** For the selected game, the user shall be able to choose an opening position from a list of supported positions (e.g., "Empty Triangle", "Fully Triangulated", "Random").
*   **FR-2.3:** The user shall be able to assign a player type (**Human** or **AI**) to each player in the game (typically two players).
*   **FR-2.4:** If **AI** is selected, the user shall be able to choose from a list of available AI implementations that support the selected game type.
*   **FR-2.5:** Upon confirming the configuration, the system shall initialize a new game session and display the starting triangulation in the game area.

#### 3.3 Feature: Core Gameplay
**Description:** Players take turns making valid moves according to the rules of the selected game.
**Requirements:**
*   **FR-3.1:** The system shall visually highlight the player whose turn it is.
*   **FR-3.2:** For a **Human** player, the system shall accept moves via mouse interaction (e.g., clicking vertices/edges) or designated keyboard shortcuts.
*   **FR-3.3:** For an **AI** player, the system shall automatically invoke the selected AI implementation to calculate and execute a move.
*   **FR-3.4:** The system shall validate every move against the current game's rules before accepting it.
*   **FR-3.5:** After a valid move, the system shall update the game state, the visual display, player scores, and the turn order.
*   **FR-3.6:** The system shall maintain a complete history of moves for the current session.

#### 3.4 Feature: Dynamic Player Control
**Description:** The user shall be able to change a player's type during an active game.
**Requirements:**
*   **FR-4.1:** The user shall be able to select an option to "Switch Player to AI" or "Switch Player to Human" for the current or opposing player.
*   **FR-4.2:** Upon switching to AI, the user shall be prompted to select an AI implementation.
*   **FR-4.3:** The switch shall occur without resetting the game state; the new player (AI or Human) will take the next turn from the current game state.

#### 3.5 Feature: Game State Persistence
**Description:** The user shall be able to save the current game session to a file and later load it to resume play.
**Requirements:**
*   **FR-5.1:** The user shall be able to initiate a save action, prompting for a file location and name.
*   **FR-5.2:** The saved file shall contain all necessary information to reconstruct the game session: game type, opening position, current game state, move history, player types/AI assignments, and scores.
*   **FR-5.3:** The user shall be able to initiate a load action, select a valid save file, and resume the game session exactly as it was saved.
*   **FR-5.4:** The system shall request user confirmation before overwriting an existing file during a save operation.

#### 3.6 Feature: End-of-Game Processing
**Description:** The system shall detect when the game's ending condition is met and conclude the session.
**Requirements:**
*   **FR-6.1:** After each move, the system shall evaluate the game state against the ending condition defined for the current game type.
*   **FR-6.2:** When the ending condition is met, the system shall prevent further moves, declare the winner (or draw), display final scores prominently, and log the result.
*   **FR-6.3:** The user shall be given the option to start a new game or return to the main menu.

#### 3.7 Feature: Extensibility (Game Definitions)
**Description:** New game types shall be loadable from external definition files.
**Requirements:**
*   **FR-7.1:** A game definition file shall specify: a unique game ID, display name, rules logic, valid move patterns, scoring algorithm, and ending condition.
*   **FR-7.2:** The core engine shall interpret this definition file to enforce rules, validate moves, and manage game progression without code changes.
*   **FR-7.3:** Newly placed game definition files in the designated directory shall appear in the game selection list after application restart or a "Refresh Games" action.

#### 3.8 Feature: Extensibility (AI Implementations)
**Description:** New AI player strategies shall be loadable from external implementation files (e.g., JAR files with a specific interface).
**Requirements:**
*   **FR-8.1:** The system shall define a public API (Java Interface) that all AI plug-ins must implement (e.g., `calculateMove(GameState state)`).
*   **FR-8.2:** AI implementation files shall declare which game types they support.
*   **FR-8.3:** Newly placed AI implementation files shall appear in the AI selection list for supported games after application restart or a "Refresh AIs" action.

#### 3.9 Feature: Help System
**Description:** The user shall have access to guidance on using the software and game rules.
**Requirements:**
*   **FR-9.1:** A "Help" menu shall provide access to "Contents", "Game Rules", and "About".
*   **FR-9.2:** Selecting "Game Rules" shall display the rules for the currently loaded or selected game type.

### 4. Non-Functional Requirements

#### 4.1 Usability
*   **NFR-U1:** All primary application functions shall be accessible via both mouse and keyboard controls.
*   **NFR-U2:** The time for a novice user to successfully configure and start a default game shall be less than 2 minutes after initial installation.
*   **NFR-U3:** The visual representation of the triangulation and game elements (marked vertices, colored edges) shall be clear and unambiguous.

#### 4.2 Performance
*   **NFR-P1:** The default, bundled AI shall compute a move for a standard game on a default opening position within **10 seconds** on the minimum hardware specification.
*   **NFR-P2:** The GUI shall remain responsive (no freezing) during AI computation.
*   **NFR-P3:** Application startup time shall be less than 15 seconds on the minimum hardware specification.

#### 4.3 Reliability
*   **NFR-R1:** The application shall not crash due to invalid user input; it shall display an appropriate error message.
*   **NFR-R2:** Corrupted or malformed external game/AI files shall be gracefully ignored (with a log message) rather than causing application failure.

#### 4.4 Supportability
*   **NFR-S1:** The system shall log significant events (errors, game start/end, file load failures) to a local log file to aid in debugging.
*   **NFR-S2:** The code shall be modular, with clear separation between the game engine, GUI, and plug-in systems.

#### 4.5 Implementation Constraints
*   **NFR-IC1:** The installation process shall consist of copying application files to a directory; no system registry changes or complex database setup shall be required.
*   **NFR-IC2:** The software shall be entirely self-contained within its installation directory, storing all user data (save files, configs) in a subdirectory within it or in the user's home directory.

#### 4.6 Interface Requirements
*   **NFR-IR1:** The graphical interface shall be consistent across supported operating systems, leveraging Java Swing's look-and-feel.

#### 4.7 Legal and Licensing
*   **NFR-L1:** All code and bundled resources shall comply with open-source licensing agreements as defined by the project.

---

### Appendix A: Open Issues / TBD
1.  Final specification for the **Game Definition File Format** (XML vs. JSON vs. custom DSL).
2.  Detailed design of the **AI Plug-in API** (Java interface and supporting classes).
3.  **Visual Design Specification:** Color schemes, icons, and layout guidelines for the usability document.
4.  Algorithm for **"Random Opening Position"** generation per game type.
5.  Content outline and format (HTML vs. plain text) for the **embedded help system**.
6.  Final prioritization and scheduling for low-priority game variants from the original project table.