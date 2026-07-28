# Software Requirements Specification (SRS)
## For Qheadache Puzzle Game

**Document Version:** 1.0
**Date:** [Current Date]
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the "Qheadache" puzzle game. It is intended to serve as a comprehensive guide for developers, testers, and project stakeholders to ensure a common understanding of the system's capabilities, constraints, and objectives.

#### 1.2 Document Conventions
- Requirements are categorized as Functional (FR) or Non-Functional (NFR).
- Priority is denoted as: **High (H)**, **Medium (M)**, **Low (L)**.
- All user interface specifications assume the use of the Qt library.
- The terms "shall" and "must" indicate mandatory requirements.

#### 1.3 Intended Audience and Reading Suggestions
- **Developers:** Should focus on Sections 2 (Overall Description), 3 (Specific Requirements), and 5 (External Interface Requirements).
- **Testers:** Should focus on Section 3 (Specific Requirements) to derive test cases.
- **Project Managers/Stakeholders:** Should focus on Sections 1 (Introduction) and 2 (Overall Description) for scope and high-level features.

#### 1.4 Project Scope
Qheadache is a single-player, desktop-based puzzle game. The core objective is for the player to manipulate blocks on a fixed board to solve a specific spatial puzzle. The system includes game state management (save/load, undo/redo), performance tracking, and a graphical user interface built with Qt. Features explicitly out of scope include multiplayer support, advanced multimedia, customizable game elements, and online connectivity.

#### 1.5 References
- Qt Framework Documentation (https://doc.qt.io/)
- IEEE Std 830-1998: Recommended Practice for Software Requirements Specifications.

### 2. Overall Description

#### 2.1 Product Perspective
Qheadache is a standalone desktop application. It interacts with the host operating system's file system for saving/loading games and statistics. It is built as a new product with no direct dependencies on other software, aside from the Qt runtime libraries.

#### 2.2 Product Functions (High-Level Feature List)
1.  **Game Board Rendering:** Display a defined puzzle board with movable blocks.
2.  **Block Manipulation:** Allow selection and movement of blocks via mouse or keyboard.
3.  **Puzzle Logic:** Enforce movement rules and detect the winning condition.
4.  **Game State Management:** Provide undo, redo, save game, load game, and new game functions.
5.  **Statistics Tracking:** Record and persistently store player performance metrics (time, moves) for the top 10 scores.
6.  **User Interface:** Provide menus, dialogs, and visual feedback for all user interactions.

#### 2.3 User Classes and Characteristics
- **Player (Primary User):** Age 8+. Expected to have basic computer literacy (mouse/keyboard use). No prior puzzle game experience is required. Motivations include entertainment, challenge, and improvement of personal scores.
- **Developer:** Responsible for implementing the system as specified in this document.
- **Tester:** Responsible for verifying the system meets the stated requirements.

#### 2.4 Operating Environment
- **Software:** Must be developed using the Qt application framework. Target operating systems are those supported by Qt (e.g., Windows, Linux, macOS).
- **Hardware:** Requires a display supporting a minimum resolution of 800 x 600 pixels. Standard mouse and keyboard input devices are required.

#### 2.5 Design and Implementation Constraints
1.  The graphical user interface must be implemented using the Qt library.
2.  The application must be portable across all operating systems supported by the Qt library used.
3.  The game must be designed for a single user per application instance.
4.  The statistics system shall store a maximum of the top 10 player records.
5.  Block movement logic must prevent overlaps and enforce a minimum distance (collision buffer) between blocks.

#### 2.6 User Documentation
In-game help or a tutorial is out of scope. A simple "About" dialog with basic version information may be included.

#### 2.7 Assumptions and Dependencies
- The host machine has sufficient disk space for save files and statistics.
- The user has appropriate file system permissions for reading/writing application data.
- The Qt runtime libraries are available on the target system.

### 3. System Features and Requirements

#### 3.1 Feature: Core Gameplay
**Description:** The player interacts with blocks on a fixed board to solve the puzzle.

**3.1.1 FR-01: Board Initialization (Priority: H)**
The system shall initialize and display a game board with a pre-defined layout of blocks at the start of a new game.

**3.1.2 FR-02: Block Selection (Priority: H)**
The system shall allow the user to select a block by clicking on it with the mouse. The selected block shall be visually highlighted.

**3.1.3 FR-03: Block Movement (Priority: H)**
The system shall allow the user to move the selected block in four directions (up, down, left, right) using either:
- Arrow keys on the keyboard.
- Mouse drag-and-drop (subject to movement constraints).
Movement shall be constrained to prevent the block from moving outside the board boundaries.

**3.1.4 FR-04: Collision Prevention (Priority: H)**
The system shall prevent any block from overlapping with another block. A minimum distance (e.g., 1 pixel or logical unit) shall be maintained between all blocks at all times.

**3.1.5 FR-05: Win Condition Detection (Priority: H)**
The system shall continuously monitor the board state. The puzzle is solved when the large square block is positioned at the designated target area at the bottom of the board. Upon detection, the system shall trigger the game completion sequence (see FR-14).

#### 3.2 Feature: Game State Management
**Description:** The player can control the flow of the game, correct mistakes, and persist progress.

**3.2.1 FR-06: Undo Action (Priority: H)**
The system shall provide an "Undo" function (via menu or shortcut) that reverts the game state to the state before the last block movement.

**3.2.2 FR-07: Redo Action (Priority: M)**
The system shall provide a "Redo" function (via menu or shortcut) that re-applies the last undone movement, if available.

**3.2.3 FR-08: Save Game (Priority: H)**
The system shall provide a "Save Game" function. It shall serialize the current game state (board layout, block positions, move count, elapsed time) to a user-specified file on disk.

**3.2.4 FR-09: Load Game (Priority: H)**
The system shall provide a "Load Game" function. It shall read a previously saved game file, restore the complete game state, and resume play from that point.

**3.2.5 FR-10: New Game (Priority: M)**
The system shall provide a "New Game" function that resets the board to its initial configuration, clears the current move count and timer, and clears the undo/redo history.

**3.2.6 FR-11: Exit Game (Priority: M)**
The system shall provide an "Exit" function. If a game is in progress, the system shall prompt the user to save their progress before terminating the application.

#### 3.3 Feature: Statistics Tracking
**Description:** The system records and displays player performance metrics.

**3.3.1 FR-12: Performance Metrics (Priority: H)**
During an active game, the system shall track and display in real-time:
- The total number of block moves made.
- The elapsed time since the game started.

**3.3.2 FR-13: Statistics Persistence (Priority: H)**
The system shall maintain a persistent, sorted list of the top 10 player scores. Each record shall store:
- Player name (entered upon game completion).
- Total moves taken to solve the puzzle.
- Total time taken to solve the puzzle.
- Date of completion.

**3.3.3 FR-14: Game Completion Dialog (Priority: H)**
Upon solving the puzzle, the system shall display a dialog window congratulating the player. This dialog shall:
- Display the final move count and time.
- Provide a field for the player to enter their name for the high-score list.
- Have buttons to submit the score, start a new game, or exit.

**3.3.4 FR-15: View Statistics (Priority: M)**
The system shall provide a "View Statistics" function that displays the top 10 scores in a dedicated dialog window, sorted primarily by fewest moves, then by shortest time.

#### 3.4 Feature: User Interface
**Description:** The system provides a clear and consistent interface for all interactions.

**3.4.1 FR-16: Main Window (Priority: H)**
The system shall present a main application window containing:
- A menu bar with standard menus (Game, Statistics, Help).
- A central, clearly rendered game board area.
- A status bar or panel displaying current moves and elapsed time.

**3.4.2 FR-17: Menu Structure (Priority: M)**
The menu bar shall contain at least the following:
- **Game Menu:** New, Save, Load, Undo, Redo, Exit.
- **Statistics Menu:** View Top Scores.
- **Help Menu:** About.

#### 3.5 Non-Functional Requirements

**3.5.1 NFR-01: Usability (Priority: H)**
The user interface shall be intuitive enough for the target audience (age 8+) to understand basic gameplay (selecting and moving blocks) within 5 minutes of first use.

**3.5.2 NFR-02: Reliability (Priority: H)**
Core functions (undo/redo, save/load, block movement) shall operate without causing the application to crash or become unresponsive.

**3.5.3 NFR-03: Performance (Priority: M)**
The game shall respond to user input (clicks, key presses) with a latency of less than 100 milliseconds. Screen refresh shall be smooth and without noticeable flicker.

**3.5.4 NFR-04: Portability (Priority: M)**
The application shall compile and run without modification on Windows and at least one other major OS (Linux/macOS) supported by the chosen Qt version.

**3.5.5 NFR-05: Data Integrity (Priority: M)**
Save game and statistics files shall be validated on load. Corrupted or invalid files shall be handled gracefully with an informative error message to the user, preventing application crash.

### 4. External Interface Requirements

#### 4.1 User Interfaces
- All interfaces will be graphical, built with Qt widgets.
- The main window layout is described in FR-16.
- Dialog windows shall be modal for game completion and statistics display.
- Consistent use of icons, tooltips, and keyboard shortcuts (e.g., Ctrl+Z for Undo, Ctrl+S for Save) is recommended.

#### 4.2 Hardware Interfaces
- Standard mouse and keyboard input are required.
- A display supporting 800x600 resolution or higher is required.

#### 4.3 Software Interfaces
- **Qt Library:** The application interfaces with the Qt framework for all UI, event handling, file I/O, and data serialization.
- **File System:** The application reads from and writes to the local file system using standard Qt file handling classes.

#### 4.4 Communications Interfaces
Not applicable. No network communication is required.

### 5. Other Non-Functional Requirements

#### 5.1 Safety and Security Requirements
- The application shall not execute or load external code from game files.
- Basic file operation errors (e.g., permission denied, disk full) shall be caught and reported to the user.

#### 5.2 Business Rules
- A "move" is defined as any discrete action that changes the position of a block, whether by keyboard or mouse.
- The high-score list is sorted first by lowest number of moves, then by shortest completion time. Only the top 10 unique entries are kept.

### 6. Appendices

#### Appendix A: Glossary
- **Block:** A game piece that occupies space on the board and can be moved by the player.
- **Board:** The fixed, bounded playing area where blocks are placed.
- **Game State:** The complete snapshot of a game at a point in time, including all block positions, move count, and elapsed time.
- **Qt:** A cross-platform application development framework used for creating graphical user interfaces.

#### Appendix B: Analysis Models
*(Optional: Could include initial mockups of the board layout, main window, and dialog designs here.)*

#### Appendix C: Issues List (Undecided/TBD)
1.  The maximum number of steps stored in the undo/redo history stack.
2.  The specific format and validation rules for player name input (e.g., max length, allowed characters).
3.  Detailed specification of error messages for all possible file I/O failures.
4.  Implementation details for any optional sound feedback.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner | | | |
| Lead Developer | | | |
| QA Lead | | | |