# Software Requirements Specification (SRS)
## For Qheadache Game
**Version:** 1.0
**Date:** October 26, 2023
**Status:** Draft for Review

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the Qheadache puzzle game. It serves as a formal agreement between stakeholders—including analysts, programmers, testers, and product management—and provides a comprehensive blueprint for the development, testing, and validation of the software.

### 1.2 Scope
The Qheadache product is a standalone desktop puzzle game application. Its core functionality includes:
*   Rendering an interactive game board with movable blocks.
*   Managing game state, including move tracking, timing, and win condition detection.
*   Providing undo/redo capabilities for player actions.
*   Persisting game state and player statistics via local file operations.
*   Displaying and managing a top 10 high score list.

**Out of Scope:**
*   Network multiplayer functionality.
*   Online leaderboards or cloud synchronization.
*   Advanced graphical effects (e.g., 3D rendering, particle systems) beyond the standard capabilities of the Qt library.
*   Mobile or web-based versions.

### 1.3 Definitions, Acronyms, and Abbreviations
*   **SRS:** Software Requirements Specification.
*   **UI:** User Interface.
*   **I/O:** Input/Output.
*   **OS:** Operating System.
*   **Qt:** A cross-platform application development framework.
*   **Block:** A movable game piece on the board.
*   **Game Session:** A single instance of gameplay from start to finish or until saved/loaded.

### 1.4 References
*   Qt Framework Documentation (version to be specified).
*   Project Charter for Qheadache Game.

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details specific functional requirements. Section 4 outlines non-functional requirements. Appendices contain supplementary information.

## 2. Overall Description

### 2.1 Product Perspective
Qheadache is a new, self-contained desktop application. It interacts with the host operating system's file system for data persistence and relies on the Qt library for its graphical user interface and core application logic.

### 2.2 Product Functions (High-Level)
1.  **Game Initialization:** Start a new game or load an existing one.
2.  **Block Manipulation:** Allow the player to select and move blocks via click-and-drag.
3.  **Game State Management:** Track moves, elapsed time, and board configuration.
4.  **Action History:** Support undo and redo of player moves.
5.  **Win Condition Detection:** Recognize when the puzzle is solved.
6.  **Scoring & Statistics:** Record completion metrics and maintain a top 10 leaderboard.
7.  **Data Persistence:** Save the current game state to a file and load it later.
8.  **User Interface:** Provide menus, dialogs, and visual feedback to the player.

### 2.3 User Characteristics
*   **Primary Actor (Player):** Aged 8 years or older. Possesses basic computer literacy, including use of a mouse, keyboard, and familiarity with standard desktop application menus and dialogs. No prior knowledge of the game is assumed.
*   **Secondary Actors:** Analyst, Programmer, Tester (as defined in Stakeholder Matrix).

### 2.4 Constraints
1.  **Technical:** Must be developed using the Qt application framework.
2.  **Platform:** Must be portable to Microsoft Windows and other operating systems officially supported by the chosen version of Qt.
3.  **Performance:** Must maintain responsiveness with an undo history of up to 1000 moves.
4.  **Legal:** Must comply with standard software licensing for the Qt library.

### 2.5 Assumptions and Dependencies
*   **Assumption:** The target operating system has a functional graphical desktop environment and standard file system.
*   **Dependency:** The project is dependent on the stability and features of the selected Qt library version.

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 User Interfaces
*   **Main Game Window:**
    *   Contains the primary game board (black background).
    *   Displays movable blocks (yellow).
    *   Includes a menu bar with the following structure:
        *   **Game:** New, Open..., Save, Save As..., Exit.
        *   **Action:** Undo, Redo.
        *   **Statistics:** View Top 10.
        *   **Help:** About, Rules.
    *   Displays a move counter and a game timer visibly on the board or in a status bar.
*   **Modal Dialogs:**
    *   **Finish Dialog:** Appears upon winning. Congratulates the player and, if the score qualifies, prompts for a name (max 20 characters) to record in the top 10.
    *   **Statistics Dialog:** Displays the top 10 scores in a tabular format (Rank, Player Name, Moves, Time).
    *   **File Dialogs:** Standard OS "Open" and "Save" dialogs for game files.
    *   **About Dialog:** Displays application name, version, copyright, and brief credits.
    *   **Error Dialogs:** Inform the user of problems (e.g., file cannot be written, corrupted save file).

#### 3.1.2 Hardware Interfaces
*   Standard mouse and keyboard input are required.
*   A display supporting a minimum resolution of 800 x 600 pixels is required.

#### 3.1.3 Software Interfaces
*   **Qt Library:** The application shall interface with the Qt framework for all GUI, event handling, and core data structure functionality.
*   **Operating System File System:** The application shall read from and write to the local file system using standard Qt file I/O classes.

#### 3.1.4 Communications Interfaces
Not applicable. This is a standalone application with no network communication requirements.

### 3.2 Functional Requirements

#### FR1: Game Session Management
*   **FR1.1:** The system shall allow the player to start a new game. Upon selection, the board shall be initialized to the standard starting puzzle configuration.
*   **FR1.2:** The system shall reset the move counter to zero and the game timer to 00:00 upon starting a new game.
*   **FR1.3:** The system shall track the current game state (`playing`, `paused`, `finished`).

#### FR2: Block Movement
*   **FR2.1:** The player shall be able to select a block by clicking on it with the mouse.
*   **FR2.2:** The player shall be able to move a selected block by dragging it with the mouse.
*   **FR2.3:** Block movement shall be constrained to the grid-based board. A block shall not be moved to a position where it would overlap another block or extend outside the board boundaries.
*   **FR2.4:** A valid block movement shall increment the move counter by one.

#### FR3: Action History
*   **FR3.1:** The system shall maintain a history of player moves.
*   **FR3.2:** The player shall be able to undo the last performed move via the "Undo" menu item or a keyboard shortcut.
*   **FR3.3:** The player shall be able to redo the last undone move via the "Redo" menu item or a keyboard shortcut, provided no new moves have been made since the last undo.
*   **FR3.4:** The system shall support undo/redo for a minimum of the last 1000 moves.

#### FR4: Game Completion
*   **FR4.1:** The system shall detect the win condition when the large 2x2 block is positioned such that its bottom edge aligns with the bottom edge of the game board.
*   **FR4.2:** Upon detecting a win, the system shall stop the game timer, change the game state to `finished`, and display the Finish Dialog.
*   **FR4.3:** The system shall evaluate the player's score (move count and time) against the stored top 10 list.
    *   *Undecided Issue #1: The sorting algorithm (e.g., primary by moves, secondary by time) must be finalized by the Analyst.*

#### FR5: Statistics and Scoring
*   **FR5.1:** If the player's score qualifies for the top 10, the Finish Dialog shall prompt the player to enter their name.
*   **FR5.2:** Upon confirmation, the system shall insert the new `PlayerStatistic` (name, move count, completion time) into the top 10 list, maintaining only the ten best scores.
*   **FR5.3:** The player shall be able to view the current top 10 scores via the "View Top 10" menu item, which opens the Statistics Dialog.
*   **FR5.4:** The top 10 list shall be persisted to a file (`statistics.dat` or similar) in the application's data directory.

#### FR6: Data Persistence (Save/Load)
*   **FR6.1:** The player shall be able to save the current game state (board configuration, move history, timer value, move count) to a file via the "Save" or "Save As..." menu items.
*   **FR6.2:** The saved file shall include a version header for future compatibility.
*   **FR6.3:** The player shall be able to load a previously saved game file via the "Open..." menu item.
*   **FR6.4:** Upon loading a file, the system shall restore the game board, timer, move counter, and move history exactly as they were saved, and set the game state to `playing`.
*   **FR6.5:** The system shall validate the structure and version of a save file before attempting to load it. If invalid or corrupted, an error message shall be displayed.
    *   *Undecided Issue #3: The behavior when loading a new game while a current game with unsaved progress is active must be defined by the Analyst (e.g., prompt to save first).*

#### FR7: Application Lifecycle
*   **FR7.1:** The player shall be able to exit the application via the "Exit" menu item or the window close button.
*   **FR7.2:** If the player attempts to exit while a game is in progress (`playing` state) and changes have been made since the last save, the system shall prompt the player to save the game before exiting (Exception Scenario 8).

### 3.3 Domain Model (Data Requirements)
The system shall manage the following core data entities, as detailed in the summary:

*   **GameSession:** Manages the state and timing of a play session.
*   **GameBoard:** Defines the grid and contains the blocks.
*   **Block:** Represents a movable entity with type, ID, and position.
*   **PlayerStatistic:** A record of a single completed game performance.
*   **GameStatistics:** The aggregated, sorted list of top scores.
*   **SavedGameFile:** A serialized representation of a `GameSession` and `GameBoard`.

### 3.4 Acceptance Criteria (Key Examples)
| Capability | ID | Given | When | Then |
| :--- | :--- | :--- | :--- | :--- |
| **Core Gameplay** | AC1 | The game is started. | The player clicks and drags a block. | The block moves with the mouse cursor without overlapping other blocks or exiting the board. |
| | AC2 | A block has been moved. | The player selects "Undo" from the Action menu. | The board reverts to the state before that move. |
| **Game Completion** | AC3 | The large 2x2 block is at the bottom of the board. | The game ends. | The system displays the "Finish Window with Statistics" **only if** the player's move count is in the top 10. |
| **Data Persistence** | AC4 | A game is in progress. | The player selects "Save Game". | The current block positions, move history, and timer are saved to a file. |
| | AC5 | A valid saved game file exists. | The player selects "Open Game" and chooses the file. | The game board and statistics are restored exactly as saved. |

## 4. Non-Functional Requirements

### 4.1 Performance Requirements
*   The graphical user interface must remain responsive, with visual feedback for block dragging occurring in real-time (no perceptible lag to the user).
*   The application must function correctly at a screen resolution of 800x600 and scale appropriately to higher resolutions.
*   Operations involving the undo/redo history (for up to 1000 moves) must execute quickly, with no noticeable pause for the user.

### 4.2 Reliability Requirements
*   The application must not crash due to user input in normal gameplay.
*   The application must handle external errors gracefully (e.g., "disk full," "file not found," "permission denied") by informing the user via a clear error message and returning to a stable state without data loss if possible.
*   The mean time between failures (MTBF) for critical gameplay functions should be extremely high.

### 4.3 Portability Requirements
*   The source code shall be written to be portable across all operating systems supported by the chosen version of the Qt framework, with Windows being the primary initial target.

### 4.4 Usability Requirements
*   The interface shall be intuitive for the target audience (ages 8+).
*   Menu items and dialogs shall use clear, non-technical language.
*   Visual feedback (e.g., block highlighting on hover, smooth dragging) shall be provided.
*   *Undecided Issue #2 & #4: Final visual theming and localization support are pending decisions.*

### 4.5 Security Requirements
*   No sensitive user data is collected or stored. Security requirements are minimal.
*   The application shall not execute code from loaded save files; files shall contain data only.

## 5. Appendices

### Appendix A: Undecided Issues & Ownership
1.  **Top 10 Score Algorithm:** Definition of sorting priority (moves vs. time). *Owner: Analyst/Product Owner.*
2.  **Detailed Visual Design:** Finalization of colors, fonts, icons, and spacing beyond the basic color scheme. *Owner: UI Designer/Programmer.*
3.  **Load Game with Unsaved Progress:** Specification of user prompt and workflow. *Owner: Analyst.*
4.  **Localization:** Decision on supporting multiple languages. *Owner: Product Owner.*
5.  **About Dialog Content:** Detailed text and information to be displayed. *Owner: Analyst.*

### Appendix B: Risk Mitigation Log
| Risk ID | Description | Probability | Impact | Mitigation Strategy | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| R1 | Qt library version incompatibility. | Medium | High | Lock and test against a specific, stable Qt LTS version from project start. | Planned |
| R2 | Save file corruption or version incompatibility. | Low | Medium | Include a version header and checksum in the save file format. Implement robust validation on load. | Planned |
| R3 | Performance degradation with large undo history. | Medium | Medium | Use efficient data structures (e.g., storing state diffs in a circular buffer) rather than full board snapshots. | Planned |
| R4 | Logic bugs in block movement/collision. | High | High | Develop comprehensive unit tests for the board and block movement algorithms. Implement peer code review. | Planned |

---
*This document is considered the authoritative source for requirements for the Qheadache Game project, Version 1.0.*