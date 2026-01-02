# Software Requirements Specification (SRS)
## Block Puzzle Game

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Approved for Development

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the "Block Puzzle Game," a standalone, cross-platform desktop application. This document is intended for the development team, testers, project managers, and stakeholders to serve as a definitive guide for the system's capabilities, constraints, and expected behavior.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are labeled `FR-XXX`. Non-functional requirements are labeled `NFR-XXX`.
*   **Keywords:** The terms "MUST," "MUST NOT," "SHALL," "SHALL NOT," "SHOULD," and "MAY" are used as defined in IETF RFC 2119.
*   **User Interface:** References to UI elements are shown in *italics*.

#### 1.3 Project Scope
The Block Puzzle Game is a single-user, graphical puzzle application. The core product is the game executable, which allows a player to manipulate blocks on a board to solve a puzzle. The system tracks game progress, manages persistent high scores, and allows saving/loading of games. It excludes network multiplayer features, in-app purchases, user account management, or puzzle level editors.

#### 1.4 References
*   Qt Framework Documentation: [https://doc.qt.io/](https://doc.qt.io/)
*   IETF RFC 2119: Key words for use in RFCs to Indicate Requirement Levels.

### 2. Overall Description

#### 2.1 Product Perspective
This is a new, self-contained desktop application. It will interact with the host operating system's file system for saving/loading game states and high scores. It is built as a standalone executable using the Qt library, ensuring a consistent experience across supported platforms.

#### 2.2 Product Functions (Summary)
1.  Render an interactive game board with movable blocks.
2.  Process user input for block selection and movement.
3.  Manage a history stack for undo/redo operations.
4.  Track and display real-time game statistics (moves, time).
5.  Persist game state to and from a local file.
6.  Maintain and display a persistent, sorted list of the top ten scores.
7.  Provide an intuitive graphical user interface suitable for the target user demographic.

#### 2.3 User Characteristics
*   **Primary Actor:** The Player.
*   **Skill Level:** Possesses basic computer operation skills (using a mouse, understanding basic menu navigation).
*   **Age Range:** 8 years and older. The interface must be clear, intuitive, and not reliant on complex text instructions.
*   **Experience:** No prior experience with this specific game is assumed.

#### 2.4 Constraints
1.  **C-NFR-001:** The application SHALL be developed using the Qt application framework (version 6.x or later).
2.  **C-NFR-002:** The application SHALL run on all desktop operating systems officially supported by the chosen version of the Qt framework (typically includes Windows, macOS, and mainstream Linux distributions).
3.  **C-NFR-003:** The application's graphical user interface SHALL be fully functional and legible at a minimum screen resolution of 800 x 600 pixels.
4.  **C-NFR-004:** The application SHALL be designed for a single user per running instance. No concurrent multi-user features are required.

#### 2.5 Assumptions and Dependencies
*   The target machine has a compatible graphics system capable of rendering the Qt GUI.
*   The user has read/write permissions in the directory where the application saves its data.
*   The specific rules and victory condition of the puzzle are defined by the game logic module and are outside the direct scope of this SRS, except where they interface with the described functions.

### 3. System Features and Requirements

#### 3.1 Game Board Interaction
**Description:** This feature encompasses the core gameplay mechanics of manipulating blocks on the board.

**Requirements:**
*   **FR-010:** The system SHALL display a defined game board area within the main application window.
*   **FR-011:** The system SHALL render distinct, visually identifiable blocks within the board area.
*   **FR-012:** The player SHALL be able to select a single block by clicking on it with the primary mouse button. A selected block MUST provide clear visual feedback (e.g., highlight, border).
*   **FR-013:** The player SHALL be able to deselect a selected block by clicking on an empty area of the board or pressing a defined key (e.g., ESC).
*   **FR-014:** The player SHALL be able to move a selected block to an adjacent empty cell by pressing the arrow keys or by dragging and dropping it with the mouse.
*   **FR-015:** All block movements SHALL adhere to the game's specific movement rules and puzzle boundaries (e.g., cannot move through walls or other blocks unless defined by puzzle rules).

#### 3.2 Action History (Undo/Redo)
**Description:** This feature allows the player to revert or reapply their actions.

**Requirements:**
*   **FR-020:** The system SHALL maintain a history of all successful player actions (block moves, etc.).
*   **FR-021:** The system SHALL provide an "Undo" function (via menu item, toolbar button, or Ctrl+Z) to revert the last action in the history.
*   **FR-022:** The system SHALL provide a "Redo" function (via menu item, toolbar button, or Ctrl+Y/Ctrl+Shift+Z) to reapply the last undone action.
*   **FR-023:** The history stack SHALL support a minimum capacity of the last 1,000 player actions. Older actions MAY be discarded.
*   **FR-024:** The state of the Undo and Redo commands SHALL be reflected in the UI (e.g., grayed out when unavailable).

#### 3.3 Game Statistics
**Description:** This feature tracks and displays metrics about the current game session.

**Requirements:**
*   **FR-030:** The system SHALL track the total number of valid block moves made in the current game session.
*   **FR-031:** The system SHALL track the elapsed real-time since the start of the current game session.
*   **FR-032:** The system SHALL display the current move count and elapsed time in a clearly visible area of the UI (e.g., status bar, info panel). The timer SHALL be formatted as `MM:SS` or `HH:MM:SS`.
*   **FR-033:** Statistics tracking SHALL pause automatically when the game is in a paused state or a modal dialog (e.g., the high-score entry dialog) is open.

#### 3.4 Game State Persistence
**Description:** This feature allows saving the current game to a file and later resuming from that file.

**Requirements:**
*   **FR-040:** The system SHALL provide a "Save Game" function (via menu or button) that persists the complete current game state (board layout, block positions, game statistics, action history) to a user-specified file location.
*   **FR-041:** The system SHALL provide a "Load Game" function (via menu or button) that restores a game state from a previously saved file.
*   **FR-042:** The file format for saved games SHOULD be robust and include versioning information to handle compatibility with future versions of the application.
*   **FR-043:** Upon successful load, the application interface SHALL reflect the loaded state exactly, including the game statistics and the state of the undo/redo history.

#### 3.5 High Score Management
**Description:** This feature maintains a persistent, sorted list of the top ten best scores.

**Requirements:**
*   **FR-050:** When a puzzle is solved, the system SHALL calculate a score based on predefined criteria (e.g., based on move count and time).
*   **FR-051:** If the calculated score qualifies for the top-ten list, the system SHALL prompt the player to enter a name (up to 3 characters or a short alias).
*   **FR-052:** The system SHALL maintain a persistent, sorted list (highest score first) of the top ten scores, associated with the player's entered name and the date achieved.
*   **FR-053:** The system SHALL provide a "View High Scores" function that displays this list in a clear, tabular format within the application.
*   **FR-054:** The high score list SHALL be stored in a persistent location (e.g., a file or system registry) and loaded automatically when the application starts.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **UI-NFR-001:** The GUI SHALL be intuitive, with clear visual feedback for interactions. Icons SHOULD be used alongside text for key actions.
*   **UI-NFR-002:** The layout SHALL be responsive and remain usable at the minimum 800x600 resolution.
*   **UI-NFR-003:** The application SHALL include a main menu bar with standard sections: *File* (New Game, Load, Save, Exit), *Game* (Undo, Redo, Pause), and *Help* (Instructions, About).
*   **UI-NFR-004:** Critical game information (moves, timer) SHALL be constantly visible.

#### 4.2 Hardware Interfaces
*   **HI-NFR-001:** The application requires a pointing device (mouse, touchpad) or keyboard for input.
*   **HI-NFR-002:** The application requires a display supporting the minimum 800x600 resolution and color depth.

#### 4.3 Software Interfaces
*   **SI-NFR-001:** The application SHALL interface with the Qt libraries for all GUI, file I/O, and cross-platform abstraction.
*   **SI-NFR-002:** The application SHALL use the host OS's standard file dialogs for Save and Load operations.

#### 4.4 Communications Interfaces
Not applicable. This is a standalone application with no network communication requirements.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   **PERF-NFR-001:** The application SHALL respond to user input (clicks, key presses) with a latency of less than 100 milliseconds.
*   **PERF-NFR-002:** The graphical rendering of the board and blocks SHALL be smooth, with no visible flicker or lag during updates.
*   **PERF-NFR-003:** Loading a saved game state SHALL complete within 2 seconds for a standard puzzle size on average hardware.

#### 5.2 Safety Requirements
No specific safety requirements are identified for this software.

#### 5.3 Security Requirements
*   **SEC-NFR-001:** The application SHALL not require elevated (administrator/root) privileges to run or save data.
*   **SEC-NFR-002:** File operations (save/load) SHALL be confined to user-accessible directories to prevent unauthorized access to system files.

#### 5.4 Software Quality Attributes
*   **QA-NFR-001 (Usability):** A first-time user SHOULD be able to start a new game and perform basic moves without consulting a manual.
*   **QA-NFR-002 (Reliability):** The application SHALL not crash due to invalid player input. All user inputs SHALL be validated.
*   **QA-NFR-003 (Maintainability):** The source code SHALL be modular, separating core game logic, UI code, and data persistence into distinct components.
*   **QA-NFR-004 (Portability):** As per constraint C-NFR-002, the code SHALL compile and run on all Qt-supported platforms without modification to the source code for platform-specific issues.

---
*End of Document*