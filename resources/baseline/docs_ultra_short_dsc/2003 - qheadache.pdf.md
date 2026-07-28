# Software Requirements Specification (SRS)
## For Qheadache Puzzle Game

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Approved for Development

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the **Qheadache** puzzle game. The intended audience includes project stakeholders, developers, testers, and project managers. This document serves as the definitive source of requirements for the system's development.

### 1.2 Scope
Qheadache is a standalone, single-player desktop puzzle game. The core product is the game application itself, which allows a user to manipulate blocks on a board to solve a puzzle. The scope includes:
*   A graphical user interface (GUI) built with the Qt framework.
*   Core gameplay mechanics for block movement.
*   Game state management (save/load, undo/redo).
*   Persistent tracking of game statistics and a high-score list.
*   **Out of Scope:** Network/multiplayer functionality, multiple simultaneous users on a single machine, and any puzzle types beyond the specific one described herein.

### 1.3 Definitions, Acronyms, and Abbreviations
*   **GUI:** Graphical User Interface.
*   **OS:** Operating System.
*   **Qt:** A cross-platform application development framework.
*   **SRS:** Software Requirements Specification.
*   **Game State:** The complete representation of the puzzle at a point in time, including block positions, move count, and elapsed time.

### 1.4 References
*   Qt Framework Documentation: [https://www.qt.io/](https://www.qt.io/)

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 details the specific functional requirements. Section 4 outlines the non-functional requirements, including performance, design constraints, and software system attributes.

## 2. Overall Description

### 2.1 Product Perspective
Qheadache is a new, self-contained desktop application. It is not a component of a larger system. It interfaces with:
*   **The Qt Library:** For all graphical rendering, user input handling, and cross-platform abstraction.
*   **The Host OS File System:** For reading and writing saved game files and the persistent high-score data.

### 2.2 Product Functions (Summary)
1.  Present a graphical puzzle board with movable blocks.
2.  Allow the user to select and drag blocks using a mouse.
3.  Track and display real-time game statistics (moves, time).
4.  Provide undo and redo functionality for player actions.
5.  Save the current game state to a file and load it later.
6.  Maintain a persistent, sorted "Top Ten" high-score list.
7.  Allow the user to view the high-score list.
8.  Provide an option to reset all saved statistics (high scores).

### 2.3 User Characteristics
The sole type of user is a **Single Player**. This user is expected to be familiar with standard desktop GUI interactions (menus, mouse pointing, clicking, and dragging). No specialized training, skills, or physical abilities are required beyond the ability to use a standard keyboard and mouse.

### 2.4 Constraints
*   **Software Dependency:** The application must be developed using the Qt library (version to be specified).
*   **Portability:** Must run on Microsoft Windows and be readily portable to other OS platforms supported by Qt (e.g., Linux, macOS).
*   **Hardware:** Requires a pointing device (mouse or equivalent) and a keyboard. The display must support a minimum resolution of 800 x 600 pixels.
*   **User Concurrency:** Only one user per application instance.

### 2.5 Assumptions and Dependencies
*   It is assumed the target operating system provides a standard graphical environment compatible with Qt.
*   The project's successful portability is dependent on the correctness and compatibility of the Qt framework across platforms.
*   A valid Qt development and runtime license is assumed for distribution.

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 User Interfaces
*   **Primary Window:** Contains the main game board and a menu bar.
*   **Menu Bar:** Shall include the following standard menus:
    *   **Game:** Contains items for `New Game`, `Load Game...`, `Save Game...`, `Save Game As...`, and `Exit`.
    *   **Edit:** Contains items for `Undo` (Ctrl+Z), `Redo` (Ctrl+Y).
    *   **Scores:** Contains items for `View High Scores` and `Clear All Scores`.
*   **Game Board:** A fixed-size grid displaying the puzzle blocks. Blocks must be visually distinct and respond to mouse hover, click, and drag events.
*   **Statistics Display:** A persistent panel or status bar showing:
    *   `Moves: [Number]`
    *   `Time: [MM:SS]`
*   **Dialog Boxes:**
    *   File Open/Save dialogs (OS-native or Qt standard).
    *   High-Score dialog (displayed upon a winning condition if the score qualifies for the Top Ten, prompting for player name).
    *   High-Score List dialog (a read-only display of the Top Ten list).

#### 3.1.2 Hardware Interfaces
*   **Input:** Standard keyboard and mouse (or compatible pointing device).
*   **Output:** A graphical display capable of a minimum resolution of **800 x 600 pixels**.

#### 3.1.3 Software Interfaces
*   **Qt Framework:** The application shall be built against and require the Qt Core and Qt GUI modules (specific modules and minimum version to be defined).
*   **File System:** The application shall read from and write to the host OS's file system using standard paths (e.g., user's documents directory) for saved games (`*.qsave`) and the high-score data file (`scores.dat` or similar).

#### 3.1.4 Communications Interfaces
Not applicable. This is a standalone, non-networked application.

### 3.2 Functional Requirements

#### 3.2.1 Gameplay (FR1-FR4)
*   **FR-001: Block Selection & Movement**
    *   **Description:** The user shall be able to select a valid, movable block on the game board by clicking it with the mouse. The user shall be able to drag the selected block to an adjacent empty space. The move shall be finalized and the game state updated upon releasing the mouse button over a valid target location.
*   **FR-002: Puzzle Goal & Win Condition**
    *   **Description:** The game shall have a specific, pre-defined winning configuration of blocks. When the user arranges the blocks into this configuration, the game shall recognize the win condition, stop the game timer, and initiate the high-score entry process if applicable.
*   **FR-003: Undo Functionality**
    *   **Description:** The user shall be able to reverse the effects of their last move by selecting `Edit -> Undo` or pressing `Ctrl+Z`. This shall restore the game state (board configuration, move counter, timer) to the point before that move was executed.
*   **FR-004: Redo Functionality**
    *   **Description:** After one or more undo operations, the user shall be able to re-apply the undone move(s) by selecting `Edit -> Redo` or pressing `Ctrl+Y`.

#### 3.2.2 Game State Management (FR5-FR7)
*   **FR-005: Save Game State**
    *   **Description:** The user shall be able to save the complete current game state (board layout, move count, elapsed time) to a user-specified file via `Game -> Save Game As...`. A default save operation (`Game -> Save Game`) shall overwrite the previously used file if it exists.
*   **FR-006: Load Game State**
    *   **Description:** The user shall be able to load a previously saved game file via `Game -> Load Game...`. This shall replace the current game state entirely with the loaded state, resetting the display and statistics accordingly.
*   **FR-007: New Game Initialization**
    *   **Description:** The user shall be able to start a fresh game with a standard initial puzzle configuration via `Game -> New Game`. This shall reset the board, and set move count and elapsed time to zero.

#### 3.2.3 Statistics & Scoring (FR8-FR11)
*   **FR-008: Track Game Statistics**
    *   **Description:** The system shall continuously track and update: a) The total number of valid block moves made since the game started or was loaded. b) The elapsed time since the game started or was loaded. The timer shall pause when the game is won or the application is minimized/inactive (design decision to be confirmed).
*   **FR-009: Maintain High-Score List**
    *   **Description:** The system shall maintain a persistent, sorted list of the top ten (10) best scores. Each entry shall record: Player Name (string), Total Moves (integer), and Total Time (seconds/integer). The list shall be sorted primarily by Moves (ascending), and secondarily by Time (ascending) for ties.
*   **FR-010: Display High Scores**
    *   **Description:** The user shall be able to view the current Top Ten list at any time via `Scores -> View High Scores`.
*   **FR-011: Clear Statistics**
    *   **Description:** The user shall be able to permanently delete the persistent high-score list via `Scores -> Clear All Scores`, after a confirmation dialog.

#### 3.2.4 System Actions (FR12)
*   **FR-012: High-Score Entry**
    *   **Description:** Upon achieving a win condition, the system shall compare the player's score (moves, time) against the persistent Top Ten list. If it qualifies, a dialog shall appear prompting the user to enter their name. Upon confirmation, the list shall be updated, sorted, and persisted.

### 3.3 Non-Functional Requirements

#### 3.3.1 Performance Requirements
*   **PERF-001:** The application shall support undoing and redoing at least the last **one thousand (1000)** discrete player actions. The response time for undo/redo operations shall be perceived as instantaneous (< 100ms).
*   **PERF-002:** All graphical updates (block dragging, board redraw) shall occur smoothly without noticeable lag or flicker.

#### 3.3.2 Safety & Security Requirements
*   **SEC-001:** File operations (load/save) shall validate file formats to prevent crashes from corrupted or maliciously crafted files.

#### 3.3.3 Software Quality Attributes
*   **PORT-001:** The application shall be portable across all operating systems officially supported by the targeted version of the Qt framework without modification to the source code.
*   **USAB-001:** The user interface shall be intuitive and follow standard desktop application conventions. Tooltips may be used for icon buttons.
*   **RELI-001:** The application shall not crash due to user input errors. Invalid operations (e.g., loading a non-game file) shall be handled gracefully with an informative error message.
*   **MAIN-001:** The high-score data and save game files shall use a documented, simple format (e.g., JSON, plain text) to allow for easy inspection and repair if necessary.

#### 3.3.4 Design Constraints
*   **DC-001:** The source code shall be written in C++ and utilize the Qt API.
*   **DC-002:** The GUI layout shall be functional and legible at the minimum supported resolution of **800 x 600 pixels**.

## 4. Appendices

### 4.1 Priority & Acceptance Approach
*   **Priority 1 (Fundamental):** FR-001 (Block Movement), FR-002 (Win Condition). The game is not acceptable without these.
*   **Priority 2 (Important):** FR-003/004 (Undo/Redo), FR-005/006 (Save/Load), FR-008/009 (Statistics & High Scores). These are core to the specified feature set.
*   **Priority 3 (Useful):** FR-011 (Clear Stats).

**Acceptance Criteria:** The product will be considered accepted when it successfully fulfills all Priority 1 and Priority 2 requirements, operates stably within the defined constraints (Qt, resolution), and passes a defined suite of test cases validating core gameplay, data persistence, and error handling.

### 4.2 Open Issues
*   Specific puzzle configuration (size, block shapes, winning layout) is to be defined in a separate design document.
*   The behavior of the game timer when the application loses focus (pauses vs. continues) is to be finalized.
*   The exact Qt modules and minimum version (e.g., Qt 6.5) need to be specified.