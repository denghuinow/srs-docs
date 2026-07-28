# Software Requirements Specification (SRS)
## For: "Headache Solver" Puzzle Game

**Document Version:** 1.0
**Date:** October 26, 2023
**Status:** Approved for Development

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the "Headache Solver" computerized puzzle game. The intended audience includes project stakeholders, software developers, testers, and project managers. This document serves as the definitive guide for the system's capabilities, constraints, and interfaces.

#### 1.2 Scope
The product is a single-player, desktop-based puzzle game. The core objective is for the user to manipulate blocks on a defined game board to achieve a solved state, thereby "solving" a specific puzzle challenge. The software will include features for gameplay, action reversal/repetition, and performance tracking. The scope excludes online multiplayer functionality, user account management, and puzzle creation/editing tools.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **SRS:** Software Requirements Specification
*   **GUI:** Graphical User Interface
*   **Qt:** A cross-platform application development framework.
*   **OS:** Operating System
*   **Block:** A movable game element within the puzzle board.
*   **Move:** A single, valid player action that changes the state of the game board.

#### 1.4 References
*   Qt Framework Documentation: [https://doc.qt.io/](https://doc.qt.io/)
*   IEEE Std 830-1998: Recommended Practice for Software Requirements Specifications.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general product description. Section 3 details specific functional requirements. Section 4 outlines non-functional requirements, including performance, design constraints, and software quality attributes.

### 2. Overall Description

#### 2.1 Product Perspective
The "Headache Solver" is a standalone, shrink-wrapped desktop application. It does not require connection to external systems or databases for core functionality. High scores and statistics will be stored locally in a persistent file (e.g., JSON, XML, or SQLite).

#### 2.2 Product Functions (High-Level)
1.  **Gameplay Core:** Present a puzzle board with blocks. Accept and validate player moves.
2.  **Action History Management:** Maintain a stack of player actions to enable undo and redo operations.
3.  **Performance Analytics:** Track and calculate game statistics (time, move count).
4.  **Data Persistence:** Save and load high score lists and player statistics between application sessions.
5.  **User Interface:** Provide a visual and interactive interface for all game functions.

#### 2.3 User Characteristics
The end-user is assumed to be a casual computer user familiar with standard GUI interactions (clicking, dragging, using menus). No specialized training or prior puzzle-solving expertise is required.

#### 2.4 Constraints
1.  **Cross-Platform Compatibility:** The application must be built using the Qt library and must successfully run on all operating systems officially supported by the Qt version used in development (e.g., Windows, Linux, macOS).
2.  **Windows Portability:** A specific, tested, and distributable build for the Microsoft Windows OS must be created.
3.  **Display:** The application requires a graphical display with a minimum resolution of 800 x 600 pixels.
4.  **Input:** Primary input is expected via mouse/trackpad. Keyboard shortcuts for actions are desirable but not mandatory for core functionality.

#### 2.5 Assumptions and Dependencies
*   The target machines have a compatible Qt runtime installed or the application is distributed with the necessary libraries.
*   The specific rules and victory condition of the puzzle ("solving a specific headache") are defined in a separate game design document and can be implemented programmatically.

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 User Interfaces
*   **UI-F-001:** A main game window displaying:
    *   The puzzle board area.
    *   A move counter.
    *   A game timer.
    *   Visual representation of blocks.
*   **UI-F-002:** A main menu or toolbar with options: `New Game`, `Undo`, `Redo`, `View Statistics`, `View High Scores`, `Exit`.
*   **UI-F-003:** A statistics dialog displaying for the current or last completed game: Total moves, total time, date completed.
*   **UI-F-004:** A high scores dialog displaying a ranked list (top 10) of best performances, showing player name (or anonymous), moves, and time.
*   **UI-F-005:** The GUI shall be fully usable and visually coherent at a resolution of 800x600.

##### 3.1.2 Hardware Interfaces
*   **HI-F-001:** The system shall accept input from standard pointing devices (mouse, trackpad).
*   **HI-F-002:** The system shall output graphics to a standard computer monitor with a minimum resolution support of 800x600.

##### 3.1.3 Software Interfaces
*   **SI-F-001:** The application shall depend on the Qt libraries (Core, GUI, Widgets) for its operation.
*   **SI-F-002:** The application shall read from/write to a local file for persistent storage of high scores and settings.

#### 3.2 Functional Requirements

##### 3.2.1 Gameplay Functions
*   **FUN-GAME-001: Initialize Game**
    *   The system shall generate a new, solvable puzzle layout upon starting the application or selecting `New Game`.
*   **FUN-GAME-002: Move Block**
    *   The system shall allow the user to select and move a block to a valid adjacent empty space on the board via a mouse drag or click-move-click action.
    *   The system shall prevent moves to invalid positions.
*   **FUN-GAME-003: Detect Puzzle Completion**
    *   The system shall continuously check the board state against the solved condition.
    *   Upon detection of the solved state, the system shall stop the game timer, display a congratulatory message, and prompt the user to enter a name for the high score list.

##### 3.2.2 Action History Functions
*   **FUN-HIST-001: Undo Action**
    *   The system shall maintain a history of all successful player moves.
    *   Upon user request (e.g., clicking `Undo` or pressing `Ctrl+Z`), the system shall revert the game state to the state before the last move.
    *   The move counter shall be decremented accordingly.
*   **FUN-HIST-002: Redo Action**
    *   If an undo has been performed, the system shall allow the user to reapply the undone move(s) upon request (e.g., clicking `Redo` or pressing `Ctrl+Y`).
*   **FUN-HIST-003: History Capacity**
    *   The system shall be capable of storing and navigating through a history of at least the last **one thousand (1,000)** player actions.

##### 3.2.3 Statistics and Data Functions
*   **FUN-STAT-001: Track Game Metrics**
    *   The system shall increment a move counter for each valid block movement.
    *   The system shall run a game timer from the first move of a new game until puzzle completion.
*   **FUN-STAT-002: Display Statistics**
    *   The system shall display the current move count and elapsed time in real-time within the main game window.
    *   The system shall display detailed final statistics in a dedicated dialog upon game completion or user request.
*   **FUN-STAT-003: Manage High Scores**
    *   The system shall maintain a persistent, sorted list of high scores (best times, fewest moves).
    *   Upon game completion, if the score qualifies, the system shall add the entry to the list.
    *   The user shall be able to view the high score list via a menu option.

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance Requirements
*   **PERF-001:** The application shall launch from the OS desktop to the main menu in under 3 seconds on standard hardware.
*   **PERF-002:** User interface responses (e.g., button clicks, block movements) shall have a perceived latency of less than 100 milliseconds.
*   **PERF-003:** Undo and Redo operations shall be executed and rendered instantly from the user's perspective, regardless of history size (up to 1000 actions).

##### 3.3.2 Safety & Security Requirements
*   **SEC-001:** The local high-score file shall not be susceptible to corruption from unexpected application termination.
*   **SEC-002:** The application shall not require or request any network permissions or system-level access beyond reading/writing its own data file.

##### 3.3.3 Software Quality Attributes
*   **QUAL-001: Maintainability:** The source code shall be modular, with clear separation between game logic, user interface, and data persistence layers.
*   **QUAL-002: Usability:** The game shall be intuitively learnable within 2 minutes for a new user. All interactive elements shall provide clear visual feedback.
*   **QUAL-003: Portability:** The source code shall compile and run without modification on all Qt-supported platforms. Platform-specific code shall be isolated and minimized.

##### 3.3.4 Design Constraints
*   **DC-001:** The application shall be developed using the C++ programming language in conjunction with the Qt framework (version 6.x or later).
*   **DC-002:** The graphical assets (block images, icons) shall be in a format natively supported by Qt (e.g., PNG, SVG).

### 4. Appendices

#### 4.1 Appendix A: Glossary
*(Any additional terms can be defined here.)*

#### 4.2 Appendix B: Analysis Models
*(Optional: Could include mockups of the GUI, state diagrams for game flow, or entity-relationship diagrams for data storage.)*

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| QA Manager | | | |