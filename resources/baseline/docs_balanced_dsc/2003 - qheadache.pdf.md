# Software Requirements Specification (SRS)
## For Qheadache Puzzle Game
**Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for the Qheadache software project. It serves as a formal agreement between stakeholders (developers, testers, and end-users) and provides a comprehensive blueprint for the development team. The intended audience includes project managers, software developers, quality assurance testers, and technical writers.

#### 1.2 Project Scope
Qheadache is a standalone, single-player computerized puzzle game. The core gameplay involves manipulating blocks on a fixed board to achieve a specific winning configuration. The application will be developed using the Qt framework to ensure cross-platform compatibility. Key features include interactive block movement, an undo/redo system, persistent game state saving/loading, and tracking of player performance statistics. The software is targeted at a general audience, with a focus on accessibility for users aged 8 and above.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **SRS**: Software Requirements Specification
*   **GUI**: Graphical User Interface
*   **I/O**: Input/Output
*   **OS**: Operating System
*   **PK**: Primary Key

#### 1.4 References
*   Qt Framework Documentation: [https://doc.qt.io/](https://doc.qt.io/)

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements. Section 5 lists project milestones, dependencies, and risks.

---

### 2. Overall Description

#### 2.1 Product Perspective
Qheadache is a new, self-contained desktop application. It does not interact with other systems or require network connectivity. Its primary external dependency is the Qt library, which provides the foundation for the GUI and core application functionality across different operating systems.

#### 2.2 Product Functions (Summary)
*   Display an interactive game board with colored blocks.
*   Process user input for selecting and moving blocks via mouse.
*   Manage a stack of player actions to support undo and redo operations.
*   Detect the winning condition and conclude the game.
*   Record, persist, and display player statistics (moves, time).
*   Save the current game state to a file and load it later.
*   Present a menu-driven interface for accessing all features.

#### 2.3 User Characteristics
*   **Primary User (Player)**: Casual users aged 8+. Expected to have basic computer literacy (mouse manipulation, understanding of menus). No specific puzzle-solving expertise is required.
*   **Secondary Users**:
    *   **Developer**: Proficient in C++ and the Qt framework.
    *   **Tester**: Understands software testing principles and the game's rules.

#### 2.4 Design and Implementation Constraints
1.  **Technology**: Must be implemented using the Qt library (C++).
2.  **Platform**: Must be portable to all operating systems officially supported by the Qt library (e.g., Windows, Linux, macOS).
3.  **Input**: The primary input device is a mouse. Keyboard shortcuts for menus are secondary.
4.  **Architecture**: Must be a standalone, single-process application.

#### 2.5 Assumptions and Dependencies
*   The target machine has a functional mouse and a display supporting at least 800x600 resolution.
*   The Qt development libraries and runtime are available and correctly installed on the development and target systems.
*   The user has write permissions to the file system for saving game and statistics data.

---

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 User Interfaces
*   **Main Window**: Contains the game board (grid), a move counter, a timer, and a menu bar.
*   **Menu Bar**: Includes:
    *   *Game*: New, Save, Load, Undo, Redo, Exit.
    *   *Statistics*: View High Scores, Clear Statistics.
    *   *Help*: About, Rules.
*   **Block Elements**: Visually distinct rectangles and squares (minimum: large 2x2 block in yellow, other blocks in black). Must respond to mouse hover, click, and drag.
*   **Dialog Windows**:
    *   *Save/Load Dialog*: Native file chooser.
    *   *High Scores Dialog*: Modal window displaying a sorted list of top 10 entries (Player Name, Moves, Time, Date).
    *   *Win Dialog*: Appears on game completion, congratulates player, shows their stats, and prompts for name if a high score is achieved.
    *   *About/Rules Dialog*: Displays static text and version information.

##### 3.1.2 Software Interfaces
*   **Qt Framework**: Version 6.x or later. Used for GUI, event handling, data structures, and file I/O.
*   **File System**: The application will read from and write to standard user-accessible directories for save files (`*.qsave`) and the statistics file (`stats.dat` or similar).

#### 3.2 Functional Requirements

##### 3.2.1 Game Board & Block Management
*   **FR1: Board Initialization**
    *   **Description**: Upon starting a new game, the system shall initialize a board of fixed dimensions and place all puzzle blocks in their predefined starting positions.
*   **FR2: Block Selection**
    *   **Description**: The player shall be able to select a block by clicking on it with the mouse. The selected block shall provide visual feedback (e.g., highlight border).
*   **FR3: Block Movement**
    *   **Description**: The player shall be able to move a selected block by clicking and dragging it with the mouse. Movement shall be constrained to the board's grid and shall not overlap other blocks. The move counter shall increment by one for each valid discrete placement.
*   **FR4: Collision Detection**
    *   **Description**: The system shall prevent any block from being moved into a cell occupied by another block or outside the board boundaries.

##### 3.2.2 Game State Management
*   **FR5: Undo Functionality**
    *   **Description**: The player shall be able to select "Undo" from the menu to revert the board state to the move immediately prior to the current state. The move counter shall decrement accordingly.
*   **FR6: Redo Functionality**
    *   **Description**: If moves have been undone, the player shall be able to select "Redo" from the menu to reapply the most recently undone move. The move counter shall increment accordingly.
*   **FR7: Action History Limit**
    *   **Description**: The system shall maintain a history of at least the last 1000 player moves to support undo/redo operations.

##### 3.2.3 Game Progression
*   **FR8: Win Condition Detection**
    *   **Description**: The game shall be considered won when the large 2x2 yellow block is positioned such that its bottom edge is aligned with the bottom edge of the game board. (Note: Specific algorithm subject to refinement per Undecided Issues).
*   **FR9: Game Completion Sequence**
    *   **Description**: Upon detecting the win condition, the game shall stop the timer, disable block movement, and display the "Win Dialog."

##### 3.2.4 Statistics Management
*   **FR10: Statistic Recording**
    *   **Description**: Upon game completion, if the player's performance (prioritizing fewer moves, then faster time) qualifies for the top 10, the system shall prompt the player for their name and shall persist the `PlayerStatistic` record (Name, Moves, Time, Date).
*   **FR11: High Scores Display**
    *   **Description**: The player shall be able to view the top 10 high scores, sorted by best performance (fewest moves, then shortest time), via the "View High Scores" menu option or automatically after a winning game.
*   **FR12: Statistics Reset**
    *   **Description**: The player shall be able to permanently clear all saved high score records via a "Clear Statistics" menu option, after a confirmation prompt.

##### 3.2.5 Data Persistence
*   **FR13: Save Game**
    *   **Description**: The player shall be able to save the complete current `Game State` (block positions, move history, move count, elapsed time) to a user-specified file.
*   **FR14: Load Game**
    *   **Description**: The player shall be able to load a previously saved `Game State` from a file, restoring the board, move count, and timer to the exact point of saving. The undo/redo history for that session shall also be restored.

#### 3.3 Domain Data Model (Logical)
```plaintext
Entity: GameState
PK: SaveFileName (String)
- blockPositions: Array<Block>
- moveHistory: Stack<MoveAction>
- currentMoveCount: Integer
- elapsedTime: Time

Entity: PlayerStatistic
PK: PlayerName (String)
- totalMoves: Integer
- completionTime: Time
- recordDate: DateTime

Entity: Block
PK: BlockID (Integer)
- type: Enum(Square, Rectangle)
- dimensions: {width: Integer, height: Integer}
- currentPosition: {x: Integer, y: Integer}
- color: Color

File: StatisticsFile (Persistent)
- entries: List<PlayerStatistic> (Max 10, Sorted)
```

#### 3.4 User Stories Mapping to Functional Requirements
| User Story | Mapped Functional Requirements |
| :--- | :--- |
| 1. Select and move blocks | FR1, FR2, FR3, FR4 |
| 2. Undo and redo moves | FR5, FR6, FR7 |
| 3. Save and load progress | FR13, FR14 |
| 4. View completion time/move count | (Implied by UI: Timer & Counter display) |
| 5. See high-score list | FR10, FR11 |
| 6. Clear all statistics | FR12 |

---

### 4. Non-Functional Requirements

#### 4.1 Usability
*   **NFR1**: The user interface shall be intuitive for the target audience (ages 8+). All menu functions shall also have discoverable keyboard shortcuts (e.g., Ctrl+Z for Undo).
*   **NFR2**: The game shall provide immediate visual feedback for all player actions (selection, valid/invalid movement, win condition).

#### 4.2 Performance
*   **NFR3**: The application shall respond to user input (click, drag) with a latency of less than 100 milliseconds.
*   **NFR4**: The undo/redo system shall perform the undo or redo operation in constant time O(1) regardless of history size (up to the 1000 move limit).

#### 4.3 Reliability & Supportability
*   **NFR5**: The application shall not crash due to invalid player input. All file I/O operations (save, load) shall include error handling for common issues (file not found, permission denied, disk full) and inform the user with a clear message.
*   **NFR6**: The statistics and save file formats shall be documented to allow for potential data migration in future versions.

#### 4.4 Portability
*   **NFR7**: The source code shall compile and run without modification on Windows, Linux, and macOS, given the presence of the appropriate Qt runtime libraries.

#### 4.5 Implementation Constraints (Reiterated)
*   **NFR8**: The GUI shall be fully functional at a screen resolution of 800 x 600 pixels.
*   **NFR9**: The application shall be a single-user system per instance.

---

### 5. Project Aspects

#### 5.1 Development Milestones & Dependencies
1.  **M1: Core Engine Completion**: Implementation of board logic, block data structures, collision detection, and win condition logic. *Dependency: None.*
2.  **M2: GUI Implementation**: Creation of all Qt-based windows, dialogs, and the interactive game board visualization. *Dependency: M1.*
3.  **M3: Persistence Integration**: Implementation of file I/O for `GameState` (save/load) and `PlayerStatistic` management. *Dependency: M1, M2.*
4.  **M4: System Integration & Testing**: Full integration of all modules, comprehensive functional and cross-platform testing, bug fixing. *Dependency: M1, M2, M3.*
5.  **External Dependency**: The entire project is dependent on the Qt library. The chosen version will dictate available features and target platforms.

#### 5.2 Risks and Mitigation
| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| Complex collision logic bugs | Medium | High | **Mitigation**: Implement TDD for board logic module. Create a comprehensive suite of unit tests for all movement and collision scenarios. |
| File corruption on save/load | Low | Medium | **Mitigation**: Use robust, standard serialization (e.g., QDataStream). Include file signature/version checks. Implement user-friendly error dialogs. |
| Performance degradation with large undo history | Low | Medium | **Mitigation**: Use efficient data structures (e.g., two stacks for undo/redo, or a circular buffer). Store only move deltas, not full board states. |
| Cross-platform UI/behavior inconsistencies | Medium | Medium | **Mitigation**: Adhere strictly to Qt APIs. Conduct structured testing on virtual machines for each target OS early and often in the development cycle. |
| Puzzle difficulty inappropriate for audience | Medium | Medium | **Mitigation**: Conduct UAT with a small group from the target demographic after M2. Be prepared to adjust block starting positions based on feedback. |

#### 5.3 Undecided Issues (To Be Resolved)
1.  The precise geometric definition of the **win condition** ("bottom of the board") requires final specification.
2.  The final **visual design** (shades, highlights, animations, fonts) needs a style guide.
3.  The **persistent file format** (binary vs. text, exact location within user directory) must be specified.
4.  Detailed **error messages and handling** for all exceptional I/O and system states need to be cataloged.
5.  The content and layout of the **"About" and "Help"** dialogs require final copy and design.
6.  If sound is implemented, a **sound specification** (events, formats, volume control) is needed.

---
**Document Approval:**

*   **Product Owner:** ________________________ Date: ________
*   **Lead Developer:** ________________________ Date: ________
*   **QA Lead:** ________________________ Date: ________