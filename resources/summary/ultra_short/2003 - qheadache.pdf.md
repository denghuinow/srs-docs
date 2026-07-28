**Purpose & Scope**
The system is a computerized puzzle game called Qheadache. It provides an interface for solving a specific puzzle by moving blocks. It does not involve network play or multiple simultaneous users on one machine.

**Product Background / Positioning**
It is a standalone desktop application. It relies on the Qt graphical library and must run on all operating systems supported by Qt.

**Core Functional Overview**
*   Move blocks on a fixed-size board using mouse selection and drag.
*   Undo and redo the last thousand player actions.
*   Track and display game statistics: elapsed time and number of moves.
*   Save the current game state to a file and load a previously saved game.
*   Maintain a persistent top-ten score list, recording player name, moves, and time.
*   Display the list of high scores.
*   Erase all saved statistics.

**Key Users & Usage Scenarios**
The sole user type is a single player. The player starts a new game or loads a saved one, moves blocks to solve the puzzle, and can save progress. Upon winning, if they achieve a top-ten score, they can enter their name to be recorded on the high-score list.

**Major External Interfaces**
The user interface is graphical, using menus and a game board. It requires a keyboard, a mouse (or equivalent pointing device), and a display with a minimum resolution of 800x600 pixels. The software interfaces with the Qt library and the host operating system's file system.

**Key Non-functional Requirements**
*   The application must be portable to the Windows operating system (and others via Qt).
*   It must support undoing and redoing the last thousand player actions.
*   The display must support a minimum resolution of 800x600.
*   Only one user interacts with the application per machine instance.

**Constraints, Assumptions & Dependencies**
The product is dependent on the Qt graphical library. It assumes the operating system provides a compatible graphical environment, a mouse, and a keyboard.

**Priorities & Acceptance Approach**
Core gameplay (block movement, puzzle goal, basic win condition) is fundamental. Features like undo/redo, statistics, and file persistence are important but secondary. The game will be accepted when it correctly implements the puzzle mechanics, maintains the defined statistics, and operates within the specified technical constraints (Qt, resolution).