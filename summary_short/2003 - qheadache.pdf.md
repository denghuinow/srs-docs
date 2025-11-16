# Short Summary

- **Background and objectives**: Qheadache is a computerized puzzle game designed to provide a simple gaming experience for users aged 8 and above, with the objective of solving a specific "headache" puzzle by moving blocks on a board.

- **In scope**:
  - Block movement, selection, and deselection on a fixed-size board.
  - Undo and redo functionality for up to the last thousand actions.
  - Player and game statistics tracking (time and number of moves).
  - Save, load, and exit game functionality.
  - Display of top 10 player scores in a statistics window.

- **Out of scope**:
  - Multiplayer or network gameplay.
  - Sound as a required feature.
  - Support for non-Qt operating systems.
  - Dynamic board size or block customization.
  - Touch or non-mouse/keyboard input devices.

- **Roles and core use cases**:
  - As a player, I want to move blocks to solve the puzzle so that I can complete the game.
  - As a player, I want to undo and redo moves so that I can correct mistakes.
  - As a player, I want to save and load my game progress so that I can resume play later.

- **Success metrics**:
  - Game can be completed by moving the large square block to the bottom.
  - Statistics are accurately recorded and displayed for top 10 performances.
  - Software runs on Windows and other Qt-supported operating systems.

- **Major constraints**:
  - Requires at least 800x600 screen resolution.
  - Must use Qt graphical library.
  - Input limited to mouse and keyboard.
  - Supports only one user per machine.
  - Board and block dimensions are fixed.

- **Undecided issues**:
  - Memory constraints: Not mentioned.
  - Site adaptation requirements: Not mentioned.
  - Communications interfaces: Not mentioned.
  - Start-up requirements: Not mentioned.
  - Apportioning of requirements: Not mentioned.