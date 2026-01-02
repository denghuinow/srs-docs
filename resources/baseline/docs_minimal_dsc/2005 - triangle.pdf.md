# Software Requirements Specification (SRS)
## Triangulation Game Platform (TGP)

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Triangulation Game Platform (TGP). The TGP is a software application designed to serve two primary purposes: 1) as an interactive environment for playing combinatorial triangulation games, and 2) as an extensible platform allowing the creation of new triangulation game types without modifying the core application source code. This SRS is intended for use by the project stakeholders, developers, testers, and technical writers.

#### 1.2 Scope
The *in-scope* features of the TGP include:
*   A graphical user interface (GUI) for game interaction.
*   Support for multiple, pre-defined triangulation games.
*   A mechanism to load external game definition files to introduce new game types.
*   Configurable player types: Human (local), Computer AI (including a default random AI).
*   Game state persistence (save/load).
*   Compliance with specified technical constraints (Java, cross-platform).

The following are explicitly *out of scope*:
*   Network or online multiplayer functionality.
*   An integrated game definition file editor (files must be created externally).
*   Advanced AI beyond a default random move generator (though the architecture must support pluggable AI).
*   Audio or complex multimedia effects.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **TGP:** Triangulation Game Platform.
*   **Combinatorial Game:** A game with perfect information, no chance elements, and usually two players taking turns.
*   **Triangulation:** The division of a geometric shape (e.g., a polygon) into triangles, often by drawing non-intersecting diagonals between vertices.
*   **Game Definition File:** An external file (e.g., XML, JSON, or custom format) that specifies the rules, board configuration, and win conditions for a specific triangulation game.
*   **AI:** Artificial Intelligence. In this context, a software component that selects moves for a computer player.
*   **JRE:** Java Runtime Environment.
*   **GUI:** Graphical User Interface.
*   **SRS:** Software Requirements Specification.

#### 1.4 References
*   Java Platform, Standard Edition Documentation (for JRE 1.4+ compatibility guidelines).
*   Project Charter: "Triangulation Game Platform" (Internal Document).

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a high-level description of the product, its user classes, and operating environment. Section 3 details the specific functional requirements. Section 4 outlines the non-functional requirements, including performance, design constraints, and quality attributes.

---

### 2. Overall Description

#### 2.1 Product Perspective
The TGP is a standalone, desktop application. It is not a component of a larger system. It interacts with the user through its GUI and with the file system to read game definitions and read/write saved game states.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Goals |
| :--- | :--- | :--- |
| **Player** | Casual or dedicated game enthusiast. Familiar with basic GUI interactions. May have varying knowledge of combinatorial games. | Play games solitaire, against AI, or with a friend locally. Save and resume games. Select from available games. |
| **Game Developer** | Technically proficient user with understanding of combinatorial game rules and basic file editing. Not necessarily a Java programmer. | Define new triangulation game types using the external definition system. Test new game definitions within the platform. |

#### 2.3 Operating Environment
*   **Software:** Must run on any operating system (Windows, macOS, Linux, etc.) equipped with a Java Runtime Environment (JRE) version 1.4 or later.
*   **Hardware:** Must run on any hardware capable of supporting the aforementioned JRE. No specific minimum CPU, memory, or graphics requirements are imposed beyond those of the JRE itself.
*   **Dependencies:** The application shall depend only on standard Java libraries (Java SE). It must **not** depend on any platform-specific (native) libraries or non-standard third-party libraries that would compromise cross-platform compatibility.

#### 2.4 Design and Implementation Constraints
1.  **Implementation Language:** The system shall be implemented in Java.
2.  **Cross-Platform Compatibility:** The software must be entirely cross-platform, relying solely on the standard Java APIs available in JRE 1.4+.
3.  **Extensibility Architecture:** The core game engine and GUI must be designed to be data-driven. Adding a new game type must be possible by creating and supplying a new game definition file, **without** recompiling the core application code.
4.  **User Interface:** Must provide a graphical user interface (GUI) that is fully operable using both a mouse and a keyboard.

#### 2.5 Assumptions and Dependencies
*   It is assumed that the JRE is properly installed on the user's system.
*   Game definition files created by Game Developers are assumed to be well-formed and adhere to the published schema/format. The application should handle malformed files gracefully with informative error messages but is not required to correct them.

---

### 3. System Features and Requirements

#### 3.1 Feature: Game Management
**Description:** The system shall allow users to select, configure, and start a triangulation game.

**Requirements:**
*   **REQ-GM-1:** The system shall present a list of available triangulation games upon startup or via a main menu. Available games shall include both built-in games and games loaded from external definition files.
*   **REQ-GM-2:** The user shall be able to select a game from the list to play.
*   **REQ-GM-3:** Upon game selection, the user shall be presented with a configuration dialog or screen to set:
    *   Number of players (e.g., 1 for solitaire vs. AI, 2).
    *   Player type (Human or Computer AI) for each player seat.
    *   Game-specific parameters (e.g., board size, if defined by the game).
*   **REQ-GM-4:** The system shall start a new game instance based on the user's configuration.

#### 3.2 Feature: Core Gameplay & GUI
**Description:** The system shall provide an interactive graphical interface for playing the selected game.

**Requirements:**
*   **REQ-CG-1:** The GUI shall display the game board (e.g., a polygon triangulation state) clearly and accurately according to the current game state.
*   **REQ-CG-2:** The GUI shall visually indicate the current player's turn.
*   **REQ-CG-3:** For a human player's turn, the system shall accept legal moves via both mouse (e.g., clicking vertices/edges) and keyboard (e.g., via shortcut keys or menu navigation).
*   **REQ-CG-4:** The system shall prevent a human player from making an illegal move as defined by the active game's rules.
*   **REQ-CG-5:** The GUI shall update immediately after a move is made to reflect the new game state.
*   **REQ-CG-6:** The system shall detect and announce the end of the game (win, loss, draw) according to the active game's victory conditions.

#### 3.3 Feature: Player Types & AI
**Description:** The system shall support different types of players, including computer-controlled AI.

**Requirements:**
*   **REQ-AI-1:** The system shall include a "Human" player type, where moves are input via the GUI.
*   **REQ-AI-2:** The system shall include a default "Computer AI" player type that selects moves at random from the set of legal moves available on its turn.
*   **REQ-AI-3:** The system architecture shall allow for the integration of more sophisticated AI player implementations (e.g., via a plug-in interface or configuration), though specific advanced AIs are not required for initial release.
*   **REQ-AI-4:** When it is a Computer AI player's turn, the system shall automatically calculate and execute a move after a short, configurable delay for visibility.

#### 3.4 Feature: Game State Persistence
**Description:** The system shall allow users to save the current state of a game to a file and later load it to resume play.

**Requirements:**
*   **REQ-GS-1:** The user shall be able to initiate a "Save Game" action from within an active game session.
*   **REQ-GS-2:** The system shall prompt the user for a file location and name to save the game state.
*   **REQ-GS-3:** The saved file shall contain all information necessary to reconstruct the game exactly, including game type, board state, player configurations, and whose turn it is.
*   **REQ-GS-4:** The user shall be able to initiate a "Load Game" action from the main application menu.
*   **REQ-GS-5:** The system shall prompt the user to select a valid saved game file and shall restore the game session to the exact state it was in when saved.

#### 3.5 Feature: External Game Definition
**Description:** The system shall be extensible by loading game rules and configurations from external files.

**Requirements:**
*   **REQ-EG-1:** The system shall be capable of reading game definition files from a specified directory (e.g., a `games/` folder) at startup.
*   **REQ-EG-2:** The game definition file format shall be documented and shall allow specification of, at a minimum:
    *   Game name and description.
    *   Initial board configuration (e.g., polygon vertex count).
    *   Legal move definitions.
    *   Victory/termination conditions.
*   **REQ-EG-3:** Games successfully loaded from external definition files shall appear in the game selection list identically to built-in games (REQ-GM-1).
*   **REQ-EG-4:** If an external game definition file is malformed or contains errors, the system shall log an informative error message and skip loading that specific game, without crashing the application.

---

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
*   **PRF-1:** The GUI shall remain responsive (no freezing) during human interaction. A perceived response time of < 200ms for UI feedback is desired.
*   **PRF-2:** The random AI shall compute and make a move within 2 seconds on hardware meeting the minimum JRE specifications, for any supported game state.

#### 4.2 Safety & Security Requirements
*   **SEC-1:** The application shall not require any special system permissions to install or run.
*   **SEC-2:** When loading external game definition files or saved games, the application shall perform basic sanity checks to prevent crashes from malformed data but is not required to provide a security sandbox against maliciously crafted files.

#### 4.3 Software Quality Attributes
*   **QA-1 Maintainability:** The code shall be modular, separating core game logic, GUI components, AI interfaces, and file I/O modules. This is to facilitate the addition of new AI types or future GUI enhancements.
*   **QA-2 Usability:** The GUI shall be intuitive for a Player user class. Common actions (new game, make move, save) should be easily discoverable.
*   **QA-3 Reliability:** The application shall not crash under normal use, including when loading invalid (but non-malicious) external files. Graceful error handling is required.
*   **QA-4 Portability:** As per the key constraint, the application must function identically across all platforms supported by JRE 1.4+.

#### 4.4 Design Constraints
*   **DC-1:** The software shall be developed in Java.
*   **DC-2:** The software shall only use APIs available in the standard Java Development Kit (JDK) version 1.4 or the version specified for the project. No third-party or native libraries are allowed.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner | | | |
| Lead Developer | | | |
| QA Lead | | | |