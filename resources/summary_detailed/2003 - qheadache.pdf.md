# Detailed Summary

## Background and Scope
Qheadache is a computerized puzzle game where players manipulate blocks on a board to solve a specific "headache" challenge. The product runs as a standalone application using Qt graphical library and targets users aged 8+ with basic computer operation skills. Non-goals include network multiplayer functionality, advanced graphics, and complex AI opponents.

## Role Matrix and Use Cases
- **Player**: Main user who interacts with game interface
- Main scenarios: Start new game, Move blocks, Save/load game, View statistics
- Exception scenarios: Attempt invalid block movement, Exit without saving, Handle file errors

## Business Process
**Main Game Flow (8 steps)**:
1. Start application → Display main window with board
2. Select block via mouse click
3. Move block while avoiding overlaps
4. Repeat steps 2-3 until large block reaches bottom
5. Record player statistics
6. Display finish window
7. Save score if record broken
8. Show statistics window

**Key Branch - Save/Load (4 steps)**:
Trigger: Menu selection → File dialog → Serialize game state → Update display

**Key Branch - Undo/Redo (3 steps)**:
Trigger: Menu selection → Restore previous state → Update board display

## Domain Model
- **Game Board** (required: dimensions, blocks collection)
- **Block** (required: position, dimensions, type)
- **Player Statistics** (required: movement_count, play_time)
- **Game Statistics** (required: player_name, movement_count, play_time, unique per player)
- **Save File** (required: block_positions, movement_history, timestamp)
- **Menu System** (required: available_actions)

## Interfaces and Integrations
- **Qt Library**: Inbound, provides GUI components and OS abstraction
- **File System**: Outbound, handles game saves and statistics persistence
- **Input Devices**: Inbound, processes mouse/keyboard interactions

## Acceptance Criteria
- **Given** game is in progress **When** player moves large block to bottom **Then** end-game sequence triggers
- **Given** previous moves exist **When** player selects Undo **Then** board reverts to previous state
- **Given** statistics file exists **When** player views statistics **Then** top 10 scores display correctly

## Non-functional Metrics
- **Performance**: Responsive block movement (<100ms), Load saved games within 2 seconds
- **Portability**: Runs on Windows OS with Qt compatibility
- **Reliability**: Handles file I/O errors gracefully with user notifications

## Milestones and Release Strategy
1. Core game mechanics implementation
2. UI/UX completion with menu system
3. Save/load functionality
4. Statistics system integration
5. Testing and bug fixes
6. Version 1.0 release

## Risk List and Mitigation Strategies
- **Qt compatibility issues**: Test on multiple Qt versions during development
- **File corruption**: Implement backup mechanism for statistics files
- **Performance degradation**: Limit undo history to 1000 moves
- **User data loss**: Auto-save prompts on exit

## Undecided Issues and Responsible Parties
- Sound effect implementation details - Not mentioned
- Internationalization support - Not mentioned
- High score sharing mechanism - Not mentioned
- Block color customization - Not mentioned
- Mobile platform support - Not mentioned