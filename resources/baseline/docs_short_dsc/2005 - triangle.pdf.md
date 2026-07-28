# Software Requirements Specification (SRS)
## For Triangulation Games Application
**Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Triangulation Games application. It is intended for use by the development team, project stakeholders, and future maintainers to ensure a common understanding of the system's capabilities and constraints.

#### 1.2 Document Conventions
- Requirements are uniquely identified with tags (e.g., `FR-1`, `NFR-1`).
- **Shall** indicates a mandatory requirement.
- **Should** indicates a desirable but not mandatory requirement.
- *Italicized text* provides explanatory notes.

#### 1.3 Project Scope
The Triangulation Games application is a Java-based desktop program that allows users to play, create, and analyze combinatorial games based on triangulations. Its core value is providing an accessible platform for both entertainment and academic exploration without requiring users to modify the application's source code.

**In-Scope Features:**
- Cross-platform graphical user interface (GUI).
- Multiple pre-defined triangulation games (constructing, transforming, marking).
- Gameplay modes: Human vs. Human, Human vs. AI, Solitaire.
- Dynamic player assignment (Human/AI) at start and mid-game.
- External definition of new game rules via configuration files.
- Save and load game states.
- Integrated help system.

**Out-of-Scope Features:**
- Network or online multiplayer functionality.
- Sophisticated AI algorithms (beyond a provided random move generator).
- Platform-native libraries or external database dependencies.
- User accounts, authentication, or profile storage.
- Performance optimization for computationally intensive AI.

#### 1.4 References
- Project Charter: "Triangulation Games Software Requirements" (provided).
- Java Platform, Standard Edition 1.4 API Specification.
- GNU General Public License (GPL) v2 or later.

### 2. Overall Description

#### 2.1 Product Perspective
This is a standalone, installable desktop application. It interacts with users through a GUI and reads game definitions from external files. It does not communicate with other systems or services.

#### 2.2 Product Functions (High-Level)
1.  **Game Management:** Launch, configure, save, load, and exit games.
2.  **Gameplay Engine:** Enforce game rules, manage game state, validate moves, and detect win/loss conditions.
3.  **AI Module:** Provide at least one AI player capable of making legal random moves for any two-player game.
4.  **User Interface:** Render game boards, accept user input, and display game information.
5.  **Game Definition Interpreter:** Parse external files to create new, playable game types within the application.
6.  **Help System:** Provide accessible documentation on game rules and application usage.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Player / Basic User** | Seeks entertainment. May have limited technical expertise. Uses standard consumer hardware. | Intuitive interface, clear rules, ability to play against AI or a friend, low barrier to entry. |
| **Game Developer** | Creates new triangulation games. Has logical/mathematical understanding but not necessarily programming skills. | Well-documented, simple file format for defining games. Ability to quickly test new game definitions. |
| **Researcher** | Studies combinatorial game theory. Values precision and adherence to mathematical models. | Scientifically accurate game implementation, support for various initial configurations, ability to observe game states. |
| **System Maintainer** | Maintains and extends the application codebase. | Clean, modular code architecture. Comprehensive documentation. |

#### 2.4 Operating Environment
*   **Software:** Java Runtime Environment (JRE) 1.4 or higher.
*   **Hardware:** Standard PC with a minimum 450 MHz processor and sufficient RAM to run a Java GUI application.
*   **OS:** Any operating system capable of running JRE 1.4+ (e.g., Windows 98/2000/XP, Linux, Mac OS X).

#### 2.5 Design and Implementation Constraints
1.  `CON-1` The application **shall** be implemented in Java.
2.  `CON-2` The application **shall not** rely on platform-specific native libraries.
3.  `CON-3` The core game logic **shall** be decoupled from the GUI to allow for potential future integration of other interfaces.
4.  `CON-4` The default provided AI **shall** be capable of playing any valid two-player game defined in the system.
5.  `CON-5` All game logic and win conditions **shall** be determinable from external definition files.
6.  `CON-6` The source code **shall** be released under the GNU General Public License (GPL).

#### 2.6 User Documentation
The application **shall** include:
*   Integrated, context-sensitive help accessible from the GUI.
*   A user manual detailing how to play pre-defined games.
*   A developer guide explaining the syntax and structure for creating external game definition files.

#### 2.7 Assumptions and Dependencies
*   The user has a compatible Java Runtime Environment installed.
*   Game definition files will be created correctly according to the published specification.
*   The random move AI's performance (within 10 seconds) is dependent on the complexity of the game state and the host machine's performance.

### 3. System Features

#### 3.1 Feature: Game Setup and Management
**Description:** This feature encompasses all activities required to initialize a game session.

**Requirements:**
*   `FR-1.1` The system **shall** present a main menu from which a user can start a new game, load a saved game, access help, or exit.
*   `FR-1.2` When starting a new game, the system **shall** allow the user to select from a list of available game types (e.g., pre-defined and user-loaded).
*   `FR-1.3` For the selected game type, the system **shall** allow the user to choose an opening position from a pre-defined list or select a "random" valid opening.
*   `FR-1.4` The system **shall** allow the user to assign each player in the game (e.g., Player 1, Player 2) as either a "Human" or "AI" player before the game starts.
*   `FR-1.5` The system **shall** allow the user to save the current state of any active game to a file.
*   `FR-1.6` The system **shall** allow the user to load a previously saved game file and resume play from the exact saved state.

#### 3.2 Feature: Core Gameplay
**Description:** This feature handles the interactive play of a triangulation game.

**Requirements:**
*   `FR-2.1` The system **shall** display a graphical representation of the current game board (triangulation).
*   `FR-2.2` The system **shall** clearly indicate the current player's turn.
*   `FR-2.3` The system **shall** accept moves from a human player via both mouse clicks and keyboard shortcuts.
*   `FR-2.4` The system **shall** validate all moves against the rules of the current game type before accepting them.
*   `FR-2.5` The system **shall** automatically execute moves for AI players.
*   `FR-2.6` The system **shall** detect and announce the end of the game (win, loss, draw) based on the rules defined for the current game type.
*   `FR-2.7` The system **shall** provide an option to change any human player to an AI player during an active game.

#### 3.3 Feature: Artificial Intelligence (AI)
**Description:** This feature provides computer-controlled opponents.

**Requirements:**
*   `FR-3.1` The system **shall** include a default "Random AI" that selects a legal move at random from all available moves for the current game state.
*   `FR-3.2` The Random AI **shall** complete its move selection within 10 seconds on the minimum specified hardware (450 MHz).
*   `NFR-1` *The system architecture should be designed to allow for the future integration of more advanced AI modules without major refactoring.*

#### 3.4 Feature: External Game Definition
**Description:** This feature allows the creation of new triangulation games without modifying the application's source code.

**Requirements:**
*   `FR-4.1` The system **shall** be able to load the definition of a new game from an external file (format TBD - e.g., XML).
*   `FR-4.2` The definition file **shall** specify: game name, player count, initial board configuration(s), legal moves, and victory/termination conditions.
*   `FR-4.3` Once loaded, a user-defined game **shall** appear in the game selection list and be playable with all standard features (vs. human, vs. AI, save/load).
*   `NFR-2` The file format for game definitions **should** be human-readable and require no programming knowledge to author, only logical specification.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   The GUI **shall** be built using standard Java Swing or AWT components to ensure cross-platform compatibility.
*   The interface **shall** be navigable and fully functional using both mouse and keyboard.
*   Visual feedback **shall** be provided for all user interactions (e.g., hover effects, selected elements).

#### 4.2 Hardware Interfaces
None required beyond standard input/output devices (mouse, keyboard, monitor).

#### 4.3 Software Interfaces
**Java Runtime Environment (JRE):** The application interfaces with JRE 1.4+ for all core functionality.

#### 4.4 Communications Interfaces
None. Network communication is explicitly out of scope.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-3` The application **shall** start in under 15 seconds on the minimum specified hardware.
*   `NFR-4` The GUI **shall** respond to user input (e.g., clicking a menu) within 1 second.
*   `NFR-5` AI move calculation is bounded by `FR-3.2`.

#### 5.2 Safety Requirements
Not applicable. This is a non-critical entertainment/educational application.

#### 5.3 Security Requirements
Minimal. The application does not handle sensitive user data. Security is limited to the safe handling of user-provided files to prevent application crashes from malformed data.

#### 5.4 Software Quality Attributes
*   **Usability:** The interface shall be intuitive enough for a first-time user to start a basic game within 5 minutes of launching the application.
*   **Maintainability:** The code shall be modular, with clear separation between the game engine, AI, GUI, and file parser modules.
*   **Portability:** The application shall function identically on Windows and Linux operating systems with a compatible JRE.
*   **Reliability:** The application shall not crash due to valid user actions or well-formed external game definition files.

### 6. Other Requirements

#### 6.1 Appendices
*Appendix A: Glossary*
*   **Triangulation:** A subdivision of a geometric region into triangles.
*   **Combinatorial Game:** A two-player game with perfect information and no chance elements.
*   **Game Definition File:** An external file that describes the rules, components, and conditions of a playable game.

*Appendix B: To Be Determined (TBD) / Undecided Issues*
1.  The specific schema and file format (XML, JSON, custom text) for external game definitions.
2.  The complete list of pre-defined opening positions for each shipped game.
3.  The detailed content and structure of the in-game help system and user manual.
4.  The priority and implementation mechanism for allowing custom AI scripts to be loaded from files.
5.  Detailed GUI style guides, including color schemes and iconography.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| Quality Assurance | | | |