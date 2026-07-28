**Balanced Summary**

**Goals and Scope**
Qheadache is a computerized puzzle game where players manipulate blocks on a board to solve a specific configuration. The software tracks player statistics, supports game save/load, and provides undo/redo functionality. It is a standalone application built with the Qt library, targeting users aged 8 and above.

**Stakeholders and User Stories**
*   **Player**: The end-user who interacts with the game to solve the puzzle.
*   **Developer**: Responsible for implementing and maintaining the software.
*   **Tester**: Ensures the game functions correctly according to the specifications.
1.  As a Player, I want to select and move blocks on the board so that I can solve the puzzle.
2.  As a Player, I want to undo and redo my moves so that I can correct mistakes.
3.  As a Player, I want to save and load my game progress so that I can continue playing later.
4.  As a Player, I want to view my completion time and move count so that I can track my performance.
5.  As a Player, I want to see a high-score list so that I can compare my results with others.
6.  As a Player, I want to clear all statistics so that I can reset the scoreboard.

**Key Processes**
1.  **Game Start**: The application launches, displaying the main game board and menu. (Trigger: User starts the application)
2.  **Block Manipulation**: The player selects, drags, and drops blocks within the board's constraints. (Trigger: Mouse click and drag)
3.  **Action History**: The player can undo or redo the last block movement via the menu. (Trigger: Menu selection for Undo/Redo)
4.  **Game Completion**: The game ends when the large 2x2 square block is moved to the bottom of the board. (Trigger: Specific block placement)
5.  **Statistics Recording**: Upon winning, the player's name, move count, and time are saved to a persistent file. (Trigger: Game completion with a high score)
6.  **File Operations**: The player can save the current game state or load a previously saved game from a file. (Trigger: Menu selection for Save/Load)
7.  **Statistics Display**: A window showing the top 10 player scores is displayed, either after a game ends or via menu request. (Trigger: Game end or menu selection)

**Domain Data Elements**
*   **Game State**: (Primary Key: Save File Name). Fields: Block Positions, Move History Stack, Current Move Count, Elapsed Time.
*   **Player Statistic**: (Primary Key: Player Name). Fields: Player Name, Total Moves, Completion Time, Record Date.
*   **Block**: (Primary Key: Block ID). Fields: Type (square/rectangle), Dimensions, Current Position (X, Y), Color.
*   **Statistics File**: (Primary Key: N/A - single file). Fields: List of PlayerStatistic records (max 10).

**Non-Functional Requirements**
1.  The user interface must support a minimum screen resolution of 800x600 pixels.
2.  The application must be portable across all operating systems supported by the Qt library.
3.  The software must handle up to 1000 actions in the undo/redo history.
4.  Input is primarily via mouse and keyboard.
5.  Only one user can play per instance/machine.
6.  Sound is an optional feature and not required for core gameplay.

**Milestones and External Dependencies**
1.  Completion of core game engine with block movement and collision logic.
2.  Implementation of the Qt-based graphical user interface.
3.  Integration of file I/O for game saves and statistics.
4.  Final testing and bug fixing phase.
5.  External Dependency: Availability and compatibility of the Qt development library.

**Risks and Mitigation Strategies**
1.  **Risk**: Complex block movement and collision detection may have bugs. **Mitigation**: Implement thorough unit testing for the board logic module.
2.  **Risk**: File corruption during save/load operations. **Mitigation**: Include data validation checks and provide clear error messages to the user.
3.  **Risk**: Performance issues with maintaining a large undo history (1000 moves). **Mitigation**: Use an efficient data structure (e.g., circular buffer) for the action history.
4.  **Risk**: Inconsistent behavior across different operating systems due to Qt. **Mitigation**: Conduct cross-platform testing on all target OSes during development.
5.  **Risk**: The puzzle may be too difficult or too easy for the target audience. **Mitigation**: Conduct user acceptance testing with a small group from the target age range.

**Undecided Issues**
1.  The specific algorithm for determining a "win" (beyond the large block's position) may need refinement.
2.  The visual design and color scheme beyond the basic black and yellow are not fully specified.
3.  The format and location of the persistent statistics file are not detailed.
4.  Error handling for edge cases (e.g., disk full when saving) is mentioned but not fully defined.
5.  The exact behavior of the "About" window and help content is only briefly described.
6.  Sound design requirements (types of sounds, when they play) are not specified.