# Detailed Summary: Qheadache Game

## Background and Scope
Qheadache is a computerized puzzle game where players manipulate blocks on a board to solve a specific configuration. The product is a standalone desktop application built using the Qt graphical library, targeting users aged 8 and above with basic computer operation skills. Its scope includes core gameplay, game state management, player statistics tracking, and file operations for saving/loading games. Non-goals include network multiplayer, online leaderboards, and advanced graphical effects beyond the specified Qt library capabilities.

## Stakeholders Matrix and Use Cases
*   **Player**: The end-user who interacts with the game to solve the puzzle and achieve a high score.
*   **Analyst**: Responsible for interpreting this specification to define system behavior and constraints.
*   **Programmer**: Develops the application code based on the functional and non-functional requirements.
*   **Tester**: Verifies that the implemented software meets all specified requirements.

**Main Scenarios:**
1.  **Start New Game**: Player launches the application, and the main game board is displayed.
2.  **Move a Block**: Player selects, drags, and drops a block to a valid new position on the board.
3.  **Undo/Redo Action**: Player uses the menu to revert or reapply the last block movement.
4.  **Win the Game**: Player successfully moves the large 2x2 block to the bottom of the board, triggering the end-game sequence.
5.  **Record High Score**: Upon winning with a top-10 score, player enters their name to save their statistics (move count and time).
6.  **View Statistics**: Player opens a window to view the list of top 10 scores.
7.  **Save/Load Game**: Player saves the current game state to a file or loads a previously saved game.

**Exception Scenario:**
8.  **Exit Without Save**: Player attempts to exit the game with unsaved progress and is prompted to save.

## Business Process
**Main Process: Play Game Session**
1.  **Trigger**: Player launches the application.
2.  **Input**: Player selects "New Game" or loads a saved game file.
3.  **Process**: Game board initializes; timer and move counter reset to zero.
4.  **Process**: Player performs block selection, movement, undo, and redo actions.
5.  **Process**: Game continuously tracks move count and elapsed time.
6.  **Process**: Player solves the puzzle by positioning the large block correctly.
7.  **Process**: System evaluates if the score qualifies for the top 10.
8.  **Output**: Appropriate finish window is shown; game session ends or returns to main menu.

**Key Branch A: Save Game Flow**
1.  **Trigger**: Player selects "Save" or "Save As" from the menu.
2.  **Input**: Player provides a filename (for "Save As").
3.  **Process**: System serializes block positions, move history, timer, and statistics.
4.  **Output**: Game state is written to a file.

**Key Branch B: Load Game Flow**
1.  **Trigger**: Player selects "Open Game" from the menu.
2.  **Input**: Player selects a valid saved game file.
3.  **Process**: System reads and deserializes the file data.
4.  **Output**: Game board and player statistics are restored to the saved state.

## Domain Model
*   **GameSession**: Represents a single instance of gameplay.
    *   `gameState` (required): e.g., "playing", "paused", "finished".
    *   `startTime` (required).
    *   `currentTime` (required).
*   **GameBoard**: The playing area containing blocks.
    *   `width`, `height` (required, constrained to 4x and 5x units).
    *   `scaleFactor` (required, constrained between 50-100 pixels).
*   **Block**: A movable element on the board.
    *   `blockId` (required, unique).
    *   `type` (required): e.g., "small square", "vertical rectangle", "large square".
    *   `positionX`, `positionY` (required).
*   **PlayerStatistic**: Performance data for a completed game.
    *   `playerName` (required, max 20 chars).
    *   `moveCount` (required).
    *   `completionTime` (required).
*   **GameStatistics**: Aggregates top scores.
    *   `topScores` (required, list of up to 10 PlayerStatistic references).
*   **SavedGameFile**: Persisted game state.
    *   `filename` (required, unique).
    *   `saveData` (required): Contains serialized board state and session data.

## Interfaces and Integrations
*   **User Interface (System: Qheadache, Direction: Outbound)**
    *   **Theme**: Graphical desktop application using Qt.
    *   **Key Points**: Main game board window, menu bar (Game, Action, Statistics, Help), modal dialogs for finish, statistics, and file operations.
    *   **SLA**: Responsive to user input with no perceptible lag during block dragging.
*   **File System (System: OS, Direction: Outbound)**
    *   **Interaction Point**: Read/Write operations for statistics and saved game files.
    *   **Input**: Serialized game data or player name/score.
    *   **Output**: Success confirmation or error message (e.g., disk full).
    *   **SLA**: File operations complete within a few seconds.

## Acceptance Criteria
**Capability: Core Gameplay**
*   **Given** the game is started, **when** the player clicks and drags a block, **then** the block moves with the mouse cursor without overlapping other blocks or exiting the board.
*   **Given** a block has been moved, **when** the player selects "Undo" from the Action menu, **then** the board reverts to the state before that move.

**Capability: Game Completion & Scoring**
*   **Given** the large 2x2 block is at the bottom of the board, **when** the game ends, **then** the system displays the "Finish Window with Statistics" if the player's move count is in the top 10.
*   **Given** the "Finish Window with Statistics" is open, **when** the player enters a name and clicks OK, **then** their score is saved to the statistics file and the Statistics Window is displayed.

**Capability: Data Persistence**
*   **Given** a game is in progress, **when** the player selects "Save Game", **then** the current block positions, move history, and timer are saved to a file.
*   **Given** a saved game file exists, **when** the player selects "Open Game" and chooses the file, **then** the game board and statistics are restored exactly as saved.

## Non-functional Metrics
*   **Performance**: The game must support undo/redo for the last 1000 actions. The UI must be responsive at a screen resolution of at least 800x600.
*   **Reliability**: The application must handle file I/O errors (e.g., permission denied, disk full) gracefully by displaying an error message without crashing.
*   **Portability**: The software must be portable to Windows OS and any other operating system supported by the Qt library.
*   **Usability**: The interface must be usable by individuals from age 8 upwards with no specific qualifications required.

## Milestones and Release Strategy
1.  Core game engine with board rendering and basic block movement.
2.  Implementation of undo/redo functionality and game state management.
3.  Integration of timer, move counter, and end-game detection logic.
4.  Development of statistics tracking, file I/O, and UI dialogs.
5.  Internal testing and bug fixing cycle.
6.  Release of Version 1.0 as a standalone, packaged executable.

## Risk List and Mitigation Strategies
1.  **Risk**: Qt library version incompatibility across different operating systems.
    *   **Mitigation**: Define and test against a specific, stable version of Qt early in development.
2.  **Risk**: Saved game file format may become corrupted or incompatible with future versions.
    *   **Mitigation**: Include a version header in the save file format and implement basic validation on load.
3.  **Risk**: Performance degradation with a large undo history (up to 1000 moves).
    *   **Mitigation**: Use efficient data structures (e.g., circular buffer) for storing game state snapshots.
4.  **Risk**: Insufficient testing for edge cases in block collision and movement logic.
    *   **Mitigation**: Develop unit tests for the block movement and board validation algorithms.

## Undecided Issues and Responsible Parties
1.  **The specific algorithm for determining the "top 10" scores** (e.g., primary sort by move count, then time). *Responsible: Analyst/Product Owner.*
2.  **The exact visual design and theming beyond the specified colors (black board, yellow blocks).** *Responsible: UI Designer/Programmer.*
3.  **Handling of unsaved progress when loading a new game from a file.** *Responsible: Analyst.*
4.  **Localization/internationalization support for UI text.** *Responsible: Product Owner.*
5.  **Detailed specification for the "About" window beyond the provided text.** *Responsible: Analyst.*