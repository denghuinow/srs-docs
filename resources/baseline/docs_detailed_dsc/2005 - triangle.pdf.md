# Software Requirements Specification (SRS)
## Triangulation Games Platform
**Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the Triangulation Games software. This Java-based application provides a platform for playing, defining, and researching combinatorial triangulation games as described in the article "Games on Triangulations." The intended audience includes stakeholders, developers, testers, and project managers.

#### 1.2 Scope
The system will be a desktop application that enables users to:
*   Play predefined triangulation games in solitaire, human vs. computer, or two-player modes.
*   Define new triangulation games through external configuration files without modifying the application source code.
*   Configure players as human or AI (with a default random AI provided).
*   Save and load game states.

**Out of Scope:**
*   Network or online multiplayer functionality.
*   High-end graphics, animations, or 3D rendering.
*   Development of complex, strategic AI beyond a basic random move generator.
*   User account management or data persistence beyond game state and definitions.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **SRS**: Software Requirements Specification.
*   **GUI**: Graphical User Interface.
*   **JRE**: Java Runtime Environment.
*   **AI**: Artificial Intelligence. In this context, refers to a computer-controlled player.
*   **XML**: Extensible Markup Language.
*   **GPL**: GNU General Public License.

#### 1.4 References
*   "Games on Triangulations" - The foundational academic article for the game logic.
*   Java Platform Standard Edition Documentation.
*   GNU General Public License, version 2 or later.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its stakeholders, and operating environment. Section 3 details the specific functional and non-functional requirements. Appendices may contain supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
The Triangulation Games Platform is a standalone, installable desktop application. It interacts with the host operating system's file system to load game definitions, AI modules, and save files. It relies on a Java Runtime Environment (JRE 1.4+) for execution.

#### 2.2 Stakeholder Matrix
| Stakeholder | Primary Goal | Key Requirements |
| :--- | :--- | :--- |
| **Researchers** | Study theoretical problems in combinatorial game theory. | Consistent, scientifically accurate program behavior and layout. |
| **Basic User / Game Player** | Entertainment and intellectual challenge. | Intuitive interface, runs on low-end hardware, easy to learn. |
| **Game Developer** | Prototype and test new triangulation game variants. | Easy process for defining new games via external files; clear documentation. |
| **Development Team** | Deliver a functional, maintainable application and gain experience. | Well-structured code, use of standard tools (Java, Swing), clear requirements. |

#### 2.3 User Classes and Characteristics
*   **End-User:** Familiar with basic computer use. May have no programming knowledge. Uses the application to play games.
*   **Advanced User/Game Designer:** Has basic technical literacy (able to edit structured text/XML files). Uses the application to create and test new game rules.
*   **System Administrator:** Responsible for installing the application and JRE on end-user machines.

#### 2.4 Operating Environment
*   **Software:** Must operate on any system with a Java Runtime Environment (JRE) version 1.4 or later installed.
*   **Hardware:** Must be performant on low-end workstations (target benchmark: 450 MHz CPU).
*   **Operating Systems:** Primary support for Microsoft Windows and Linux distributions.

#### 2.5 Design and Implementation Constraints
1.  The application shall be developed in Java.
2.  The GUI shall be implemented using the Java Swing toolkit to ensure cross-platform compatibility.
3.  The source code shall be released under the GNU General Public License (GPL).
4.  Game logic must be separable from core application logic to allow user-defined games.

#### 2.6 Assumptions and Dependencies
*   A suitable JRE is installed on the end-user's machine.
*   Users defining new games will have access to and understanding of the provided game definition documentation.
*   The core game logic described in the referenced academic paper is correct and implementable.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Game Management
*   **FR-001: Application Startup**
    *   **Description:** The system shall present a main GUI window upon successful launch.
    *   **Exception:** If a fatal error occurs during initialization (e.g., corruption of core game files), the system shall display a user-friendly error message and terminate gracefully.
*   **FR-002: Game Selection**
    *   **Description:** The system shall provide a list of all available games (pre-installed and user-defined) from which the user can select to start a new session.
*   **FR-003: Opening Position Configuration**
    *   **Description:** For a selected game, the system shall allow the user to choose a starting position from a list of predefined positions or select a randomly generated valid position.
*   **FR-004: Player Configuration**
    *   **Description:** The system shall allow the user to assign a type (Human or AI) to each player role in the game before starting.
*   **FR-005: AI Selection**
    *   **Description:** When a player is configured as AI, the user shall be able to select from available AI modules (e.g., "Default Random AI").

##### 3.1.2 Game Session Execution
*   **FR-006: Move Input & Validation**
    *   **Description:** The system shall accept move input from human players (via GUI) and AI players, and validate each move against the current game's rules before applying it.
*   **FR-007: Game State Management**
    *   **Description:** The system shall maintain the complete state of the current game session, including board configuration, player turn, and move history.
*   **FR-008: Turn Management**
    *   **Description:** The system shall correctly sequence turns between players according to game rules and player type (immediately processing AI turns).
*   **FR-009: End Condition Detection**
    *   **Description:** The system shall continuously evaluate the game state against the defined ending conditions. When an end condition is met, the game shall stop, and the results (winner, score) shall be displayed prominently to the user.

##### 3.1.3 Session Modification & Persistence
*   **FR-010: Mid-Game Player Substitution**
    *   **Description:** The user shall be able to replace any human player with an AI player (or vice-versa) during an active game session. The change shall take effect from the next turn of the affected player.
*   **FR-011: Save Game State**
    *   **Description:** The user shall be able to save the complete state of the current game session to a file. The system shall prompt for confirmation before overwriting an existing file.
*   **FR-012: Load Game State**
    *   **Description:** The user shall be able to load a previously saved game state file and resume the session from the exact saved position.

##### 3.1.4 System Extensibility
*   **FR-013: Dynamic Game Discovery**
    *   **Description:** The system shall, on startup, automatically scan a predefined directory for valid game definition files and load them, making them available in the game selection list (FR-002).
*   **FR-014: Game Definition Loading**
    *   **Description:** The system shall be able to parse a user-created game definition file (format TBD, e.g., XML). If the file is invalid, the system shall log an error, inform the user via the GUI, and not load the defective game.

#### 3.2 External Interface Requirements

##### 3.2.1 User Interfaces
*   **UI-001: Main Application Window**
    *   A Java Swing-based window containing a menu bar, a game board visualization panel, a game state/information panel, and a control panel.
*   **UI-002: Game Board Display**
    *   A clear visual representation of the triangulation game state, updated after every valid move.
*   **UI-003: Dialog Boxes**
    *   Consistent Swing dialogs for game selection, player configuration, file operations (open/save), and error messages.

##### 3.2.2 Hardware Interfaces
*   None specified. Standard keyboard and mouse input are assumed.

##### 3.2.3 Software Interfaces
*   **SI-001: Java Runtime Environment (JRE 1.4+)**
    *   The application requires this platform to execute.
*   **SI-002: Host Operating System File System**
    *   **Input:** Reads game definition files, AI module classes, and saved game files from user-specified or default directories.
    *   **Output:** Writes saved game state files to user-specified locations.

##### 3.2.4 Communications Interfaces
*   None required. This is a standalone desktop application.

#### 3.3 Domain Model (Key Entities)
```java
// Conceptual Entity Overview
Game {
    String gameId; // Unique identifier
    String name;
    String type;
    Rules rulesDefinition; // Loaded from file
}

GameSession {
    String sessionId;
    GameState currentState; // Board, turn, etc.
    List<Move> movesHistory;
}

Player {
    String playerId;
    PlayerType type; // Enum: HUMAN, AI
    AIStrategy aiStrategy; // Null if HUMAN
}

Move {
    String moveId;
    Player player;
    Action actionDetails; // Game-specific move data
}

OpeningPosition {
    String positionId;
    String configurationData; // e.g., initial board setup
    String gameTypeReference;
}
```

#### 3.4 Non-Functional Requirements

##### 3.4.1 Performance Requirements
*   **PER-001:** The default random AI shall compute and execute a move within **10 seconds** for any valid game position on the target hardware (450 MHz).
*   **PER-002:** The GUI shall remain responsive to user input (e.g., menu clicks, board interactions) during AI calculation. A "thinking..." indicator is recommended.

##### 3.4.2 Reliability & Availability
*   **REL-001:** The application shall run without critical crashes on supported Windows and Linux operating systems with a compatible JRE.
*   **REL-002:** File save operations shall include safeguards (e.g., confirmation dialogs for overwrites) to prevent accidental user data loss.

##### 3.4.3 Security Requirements
*   **SEC-001:** No specific security measures are required for authentication or network communication, as the application is standalone and does not handle personal user data.

##### 3.4.4 Usability Requirements
*   **USA-001:** A user familiar with the game rules shall be able to start a new game and make their first move within 2 minutes of launching the application.
*   **USA-002:** Context-sensitive help content shall be accessible from the main menu or help key (F1).

##### 3.4.5 Compliance
*   **COM-001:** The complete software, including source code, shall be released under the **GNU General Public License (GPL)**.

##### 3.4.6 Observability & Supportability
*   **OBS-001:** All errors (e.g., file not found, invalid game definition, illegal move) shall be communicated to the user through clear, non-technical messages in the GUI.
*   **OBS-002:** The system shall log operational errors (e.g., failure to load an AI module) to a standard error stream or log file for diagnostic purposes.

### 4. Appendices

#### 4.1 Acceptance Criteria (Gherkin Style)
*   **Scenario: Successful Game Play**
    *   **Given** the Triangulation Games application is running,
    *   **When** I select a game, choose a starting position, set Player 1 to Human and Player 2 to "Default Random AI", and start the game,
    *   **Then** a game board is displayed, I can make a move for Player 1, and the AI automatically makes a move for Player 2.
*   **Scenario: Game Conclusion**
    *   **Given** a game is in progress,
    *   **When** a player makes a move that meets the game's ending condition,
    *   **Then** no further moves are allowed and a message is displayed announcing the winner/final score.
*   **Scenario: Load User-Defined Game**
    *   **Given** a valid `my_new_game.xml` definition file is placed in the "games" directory,
    *   **When** I restart the application and open the "New Game" dialog,
    *   **Then** "My New Game" appears in the list of available games.

#### 4.2 Milestones & Release Strategy
1.  **Milestone 1 (Alpha):** Core Swing GUI framework. Basic input handling. Placeholder game logic.
2.  **Milestone 2 (Alpha):** Integration of default random AI. Functional human vs. AI play for one core game.
3.  **Milestone 3 (Beta):** Full implementation of three high-priority default triangulation games.
4.  **Milestone 4 (Beta):** Game definition file (XML) loading mechanism operational.
5.  **Milestone 5 (Release Candidate):** Save and load game state functionality complete.
6.  **Milestone 6 (Final Release):** All features integrated, tested, and documented. User and maintenance manuals prepared.

#### 4.3 Risk Management
| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| Complexity of academic game logic. | Medium | High | Maintain close collaboration with research client; implement and validate core games iteratively. |
| AI move calculation exceeds 10-second limit. | Medium | Medium | Profile and optimize default AI; document that user-developed AIs are responsible for their own performance. |
| Game definition format is too complex for target users. | High | Medium | Develop a comprehensive XSD schema and provide multiple, well-commented example files. |
| Cross-platform GUI inconsistencies. | Low | Medium | Adhere strictly to standard Swing components; establish early testing on both Windows and Linux. |

#### 4.4 Open Issues & TBDs
1.  **Issue:** Final specification and XML Schema Definition (XSD) for the game definition file.
    *   **Owner:** Development Team & Client (Researcher).
2.  **Issue:** Detailed Java API specification for third-party AI module developers.
    *   **Owner:** Development Team.
3.  **Issue:** Detailed mockups and style guide for the Java Swing user interface.
    *   **Owner:** Development Team.
4.  **Issue:** Packaging and distribution method (e.g., platform-specific installers vs. executable JAR).
    *   **Owner:** Development Team.

---
*Document End*