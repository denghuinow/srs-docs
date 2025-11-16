# Balanced Summary

## Goals and Scope
Qheadache is a computerized puzzle game where users manipulate blocks on a board to solve a specific headache. The product provides game mechanics, statistics tracking, and file management as a standalone application. It targets users aged 8+ with basic computer operation skills.

## Roles and User Stories
- **Player**: I want to move blocks on the board so that I can solve the puzzle
- **Player**: I want to undo/redo actions so that I can correct mistakes
- **Player**: I want to save/load games so that I can continue later
- **Player**: I want to view statistics so that I can track my performance
- **Player**: I want to complete the puzzle so that I can win the game

## Key Processes
1. **Game Start** (trigger: application launch)
2. **Block Selection** (trigger: mouse click on block)
3. **Block Movement** (trigger: mouse drag during movement state)
4. **Game Completion** (trigger: large square moved to bottom)
5. **Statistics Recording** (trigger: game completion with high score)
6. **Game Save/Load** (trigger: menu selection)
7. **Statistics Display** (trigger: menu selection or game end)

## Domain Data Elements
- **Game Session**: session_id, block_positions, move_count, elapsed_time, player_name
- **Player Statistics**: player_name, best_move_count, best_time, date_achieved
- **Game Board**: board_id, dimensions, block_configuration, current_state
- **Block**: block_id, dimensions, position, color
- **Move History**: move_id, previous_positions, timestamp
- **Statistics File**: file_id, top_players, game_records

## Non-functional Requirements
- Must support 800×600 minimum screen resolution
- Requires Qt graphical library compatibility
- Must be portable to Windows OS
- Supports keyboard and mouse input
- Single user per machine
- Undo/redo support for last thousand actions

## Milestones and External Dependencies
- Qt graphical library integration
- Windows OS compatibility
- File system access for game saves
- Statistics file management
- User interface implementation

## Risks and Mitigation Strategies
- **Platform compatibility issues**: Use Qt for cross-platform support
- **Performance with undo history**: Limit to 1000 actions
- **File corruption**: Implement error handling for save/load operations
- **User interface complexity**: Follow established Qt design patterns
- **Statistics data loss**: Implement file backup mechanisms

## Undecided Issues
- Sound implementation details
- Memory constraints
- Site adaptation requirements
- Network/communication interfaces
- Help system beyond About window
- Not mentioned