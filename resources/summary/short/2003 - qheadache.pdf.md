**Short Summary**

**Background and objectives**  
Qheadache is a computerized puzzle game designed to provide a simple, engaging experience for users aged 8 and above. The objective is to solve a specific puzzle by moving blocks on a board, with features for tracking performance and managing game state.

**In scope**  
- Core gameplay: selecting, moving, and arranging blocks on a defined board.  
- Game state management: undo/redo actions, saving/loading games, and exit procedures.  
- Statistics tracking: recording and displaying player scores (time and move count).  
- User interface: a main window with menus, board display, and dialog windows for game completion and statistics.  
- File handling: saving and loading game data, including block positions and player statistics.

**Out of scope**  
- Multi-user or network gameplay; only one user per machine is supported.  
- Advanced graphics or sound effects beyond basic interface elements.  
- Customizable board layouts or block designs beyond the specified dimensions.  
- Integration with external databases or online scoreboards.  
- Support for operating systems other than those compatible with the Qt library (though portability to Windows is specified).

**Stakeholders and core use cases**  
*Stakeholders:*  
- **Player**: Uses the game for entertainment and puzzle-solving.  
- **Developer**: Implements and maintains the software based on the SRS.  
- **Tester**: Validates functionality against requirements.  

*User stories:*  
1. As a player, I want to move blocks on the board so that I can solve the puzzle.  
2. As a player, I want to undo my last move so that I can correct mistakes.  
3. As a player, I want to save my game progress so that I can resume later.  
4. As a player, I want to view my statistics (time and moves) so that I can track my performance.  
5. As a player, I want to see a completion message when I solve the puzzle so that I know I have finished.  
6. As a developer, I want clear requirements for block movement and UI so that I can implement the game accurately.

**Success metrics**  
- Game can be completed by moving the large square block to the bottom of the board.  
- Statistics (time and move count) are accurately recorded and displayed.  
- Core functions (undo/redo, save/load) operate reliably without crashes.

**Major constraints**  
- Must use the Qt graphical library and support its compatible operating systems.  
- Requires a minimum screen resolution of 800x600 and input via mouse/keyboard.  
- Only supports a single user per instance; no multiplayer functionality.  
- Statistics are limited to storing the top 10 player records.  
- Block movement must prevent overlaps and maintain a minimum distance from other blocks.

**Undecided issues**  
- Specific error handling for file operations beyond basic permission/disk space checks.  
- Exact sound implementation details (mentioned but not required).  
- Adaptation requirements for non-standard hardware interfaces.  
- Memory constraints for storing undo/redo history (implied but not quantified).  
- Detailed validation of player name input in statistics recording.