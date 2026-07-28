# Software Requirements Specification (SRS)
## Triangulation Games Platform

**Document Version:** 1.0  
**Date:** [Current Date]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the "Triangulation Games Platform," a stand-alone software application for playing and defining combinatorial triangulation games based on academic research. It is intended for use by software developers, testers, project managers, and end-users to ensure a common understanding of the system to be built.

#### 1.2 Scope
The system is a desktop application that implements the games described in the article "Games on Triangulations." Its core purpose is twofold:
1.  To provide a playable environment for researchers and students to interact with these combinatorial games in solitaire, human-vs-human, or human-vs-computer modes.
2.  To serve as an extensible platform where new triangulation game types can be defined and loaded at runtime without modifying the core application source code.

**Out-of-Scope:**
*   Networked or online multiplayer functionality.
*   A built-in integrated development environment (IDE) for game development.
*   Support for game types unrelated to the combinatorial triangulation model described in the foundational article.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **Triangulation:** A subdivision of a geometric region into triangles, as defined in the foundational research article.
*   **Game Definition:** An external file (e.g., XML, JSON, or custom format) that specifies the rules, moves, and win conditions for a specific triangulation game.
*   **AI (Artificial Intelligence):** A software module that selects moves for a computer-controlled player.
*   **JRE:** Java Runtime Environment.
*   **Swing:** A Java GUI widget toolkit.
*   **GPL:** GNU General Public License.
*   **GUI:** Graphical User Interface.

#### 1.4 References
*   "Games on Triangulations" - [Author, Publication, Year] - The foundational academic article.
*   Java Platform Standard Edition Documentation, Version 1.4+.
*   GNU General Public License, Version 2 or later.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements, including performance, usability, and portability.

---

### 2. Overall Description

#### 2.1 Product Perspective
This product is a new, self-contained desktop application. It operates within the user's local Java runtime environment and interacts with the local file system to load game definitions, AI modules, and saved game states. The system architecture is modular, separating the core game engine, GUI, and pluggable game/AI definitions.

#### 2.2 Product Functions (High-Level)
*   **Game Management:** Create, start, and terminate game sessions.
*   **Gameplay Execution:** Enforce turn-based rules, validate moves, and detect end-game conditions.
*   **User Interaction:** Provide visual representation of triangulations and game state, accepting input via mouse and keyboard.
*   **Player Management:** Support human and AI players, allowing configuration and mid-game role switching.
*   **Definition Loading:** Dynamically load and interpret external files to define new game types.
*   **Configuration:** Allow users to select game types, opening positions, and player types.

#### 2.3 User Characteristics
*   **Primary User (Player):** Researchers or graduate students in mathematics, computer science, or related fields. They are computer-literate but not necessarily software developers. Their goal is to explore game strategies and properties.
*   **Secondary User (Game Developer):** Researchers or advanced users with technical proficiency. They understand the formal rules of triangulation games and can author structured definition files. They require no knowledge of Java to extend the system.

#### 2.4 Constraints
*   The application must be implemented in Java.
*   It must not rely on any platform-specific (Windows/Linux) native libraries.
*   The graphical interface must be built using standard Java Swing to ensure portability.
*   The final software must be released under the terms of the GNU GPL license.

#### 2.5 Assumptions and Dependencies
*   A Java Runtime Environment (JRE), version 1.4 or later, is installed on the user's machine.
*   The user's system provides a graphical display environment capable of supporting Java Swing.
*   Game definition files authored by **Game Developers** will conform to a specified, documented schema.

---

### 3. Specific Requirements

#### 3.1 External Interface Requirements

**3.1.1 User Interfaces**
*   **Main Game Window:** Displays the triangulation board, current game state, player information, and move history. It shall include a menu bar and/or toolbar for system functions (File, Game, View, Help).
*   **Dialog Windows:**
    *   **New Game Dialog:** For selecting game type, opening position (specific or random), and configuring Player 1 & Player 2 (Human/AI).
    *   **Player Configuration Dialog:** Accessible during a game to change the type (Human/AI) of any player.
    *   **File Operation Dialogs:** Standard "Open" and "Save" dialogs for game definitions and saved games.
    *   **Confirmation Dialog:** Presented before any file overwrite operation.
*   **Input Methods:** All gameplay actions and menu navigation must be achievable using only a mouse *or* only a keyboard (with standard mnemonics and accelerators).

**3.1.2 Hardware Interfaces**
*   None specified beyond standard PC hardware supported by Java.

**3.1.3 Software Interfaces**
*   **Java Runtime Environment (JRE):** Version 1.4 or higher.
*   **Java Swing Library:** For the GUI framework.
*   **Local File System:** For reading game definition files, AI modules (JAR/class files), and writing saved game files.

**3.1.4 Communications Interfaces**
*   None. This is a non-networked application.

#### 3.2 Functional Requirements

**3.2.1 Game Core & Session Management**
*   **FR1:** The system shall allow the user to start a new game session.
*   **FR2:** The system shall allow the user to terminate the current game session at any time.
*   **FR3:** The system shall load and initialize a game based on a user-selected game definition file.
*   **FR4:** The system shall allow the user to select an opening position from a pre-defined list specific to the loaded game type.
*   **FR5:** The system shall provide an option to generate a valid random opening position for the loaded game type.

**3.2.2 Gameplay & Rules Enforcement**
*   **FR6:** The system shall visually display the current triangulation and game state.
*   **FR7:** The system shall enforce turn-taking between two players.
*   **FR8:** The system shall validate all player moves against the rules defined in the active game definition.
*   **FR9:** The system shall detect and announce the end of the game when a win/loss/draw condition specified in the active game definition is met.
*   **FR10:** The system shall provide a visual or textual indication of which player's turn it is.

**3.2.3 Player Management**
*   **FR11:** The system shall support two players in a single game session.
*   **FR12:** Each player position shall be configurable as either a Human or an AI player at game start.
*   **FR13:** The system shall provide a "Default Random AI" that selects a move uniformly at random from the set of legal moves.
*   **FR14:** The user shall be able to change the type (Human ↔ AI) of any player during an active game session without restarting the game.

**3.2.4 Extensibility & Configuration**
*   **FR15:** The system shall load new game definitions from external files at application runtime without requiring a restart.
*   **FR16:** The system shall interpret the win/loss conditions and move rules from the loaded game definition file.

**3.2.5 Data Persistence (Lower Priority)**
*   **FR17:** The system may allow the user to save the complete state of the current game to a file.
*   **FR18:** The system may allow the user to load and resume a previously saved game from a file.
*   **FR19:** The system may allow dynamic loading of new AI implementations from external class or JAR files at runtime.

**3.2.6 Help System (Medium Priority)**
*   **FR20:** The system may provide an in-game help function explaining controls and game concepts.

#### 3.3 Non-Functional Requirements

**3.3.1 Performance Requirements**
*   **PERF-1:** The default random AI shall compute and execute its move within **10 seconds** for any valid game state on standard desktop hardware (c. 2004-2005 era).

**3.3.2 Safety Requirements**
*   **SAF-1:** Before overwriting any existing file during a "Save" operation, the system **must** present a confirmation dialog to the user and require explicit approval.

**3.3.3 Usability Requirements**
*   **USAB-1:** The system shall be fully operable using only a standard keyboard (via tab navigation, arrow keys, space/enter, and keyboard shortcuts).
*   **USAB-2:** The system shall be fully operable using only a standard mouse (pointing, clicking, standard menu interactions).
*   **USAB-3:** Menu items and dialog controls shall have clear, consistent labels.

**3.3.4 Portability Requirements**
*   **PORT-1:** The application shall run without modification on Microsoft Windows (2000/XP) and common Linux distributions (with a graphical environment) that support JRE 1.4+.

**3.3.5 Implementation Constraints**
*   **IMPL-1:** The source code shall be written in Java.
*   **IMPL-2:** The application shall rely solely on the standard Java libraries (JRE 1.4+) and the Swing toolkit for its GUI. No third-party or platform-native libraries are permitted.

**3.3.6 Licensing Requirement**
*   **LIC-1:** The final software product, including source code, shall be released under the GNU General Public License (GPL).

---

### 4. Prioritization and Acceptance

#### 4.1 Feature Priority
*   **High Priority (Must Have):** FR1-FR16, PERF-1, SAF-1, USAB-1, USAB-2, PORT-1, IMPL-1, IMPL-2. These constitute the minimum viable product (MVP).
*   **Medium Priority (Should Have):** FR14, FR20.
*   **Low Priority (Could Have):** FR17, FR18, FR19.

#### 4.2 Acceptance Criteria
The system will be considered acceptable when:
1.  All **High Priority** functional requirements (FR1-FR16) are implemented and verified through testing.
2.  All specified non-functional requirements (Performance, Safety, Usability, Portability, Constraints, and Licensing) are met, as demonstrated by:
    *   Performance tests confirming AI move time < 10s.
    *   Usability tests confirming full keyboard-only and mouse-only operation.
    *   Successful execution on both Windows and Linux test platforms.
    *   Code review confirming Java/Swing implementation and GPL compliance.
3.  The system successfully loads and plays the three initial game types (constructing, transforming, marking) from external definition files.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner | | | |
| Lead Developer | | | |
| QA Manager | | | |