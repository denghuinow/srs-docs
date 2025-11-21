# Detailed Summary

## Background and Scope
MultiMahjong is a client-server Mahjong game supporting single-player (against 3 computer opponents) and multi-player modes (up to 4 human players over TCP/IP). The system consists of MultiMahjongServer for game coordination and MultiMahjongClient for user interaction. Non-goals include advanced security features, multiple language support, and server-based computer opponent processing in the initial version.

## Role Matrix and Use Cases
- **Player**: Initiates games, makes moves, views game state
- **Computer Opponent**: Automated player following Mahjong rules
- **Server Administrator**: Manages MultiMahjongServer operation
- **Game Creator**: Sets up new games with preferences
- **Game Joiner**: Connects to existing multiplayer games

Main scenarios: Create single/multiplayer game, join existing game, make valid moves, handle computer opponent turns. Exception scenarios: Player disconnection, fatal errors, game draws.

## Business Process
**Main Process (Game Session):**
1. User launches client and selects game mode
2. Enter player details and preferences
3. Server initializes game (randomize tiles/seating)
4. Players take turns picking/discarding tiles
5. Validate moves against Chinese Mahjong rules
6. Update game state and display changes
7. Continue until hand completion or draw
8. Rotate winds and begin new hand or end game

**Key Branches:**
- Player Disconnection: Replace with CO, transfer game state (4 steps)
- Fatal Error: Display error, cleanup processes, terminate (3 steps)

## Domain Model
- **Player**: name (required), icon, score, wind_position
- **Game**: round_number, current_wind, score_limit (required), players (reference)
- **Tile**: type, suit, value, position (wall/discard/hand)
- **GameSession**: status, created_by (reference), start_time
- **ComputerOpponent**: difficulty_level, strategy_profile
- **Move**: player (reference), tile (reference), move_type, timestamp
- **Preferences**: sound_enabled, animation_enabled, custom_icon
- **HighScore**: player_name (required), score (required), date

## Interfaces and Integrations
- **MultiMahjongServer → MultiMahjongClient**: Game state updates, move validation, player join/leave notifications
- **MultiMahjongClient → MultiMahjongServer**: Player moves, game creation/join requests, preference updates
- **File System**: Save/load preferences, store high scores, error logging
- **User Input**: Mouse/keyboard events for tile selection and game actions

## Acceptance Criteria
- Given a player has launched the client, when they select single-player mode and enter preferences, then a game with 3 computer opponents should begin
- Given a player can make a Chow move, when valid conditions exist, then the Chow button becomes active and the move is processed
- Given a player disconnects during multiplayer, when replacement conditions are met, then a computer opponent takes over their position
- Given game completion conditions are met, when the final hand ends, then scores are finalized and players can start new games

## Non-functional Metrics
- **Performance**: CO response within 1 minute; move calculation within 5 seconds
- **Reliability**: Server supports 10 simultaneous games (40 players); graceful error handling
- **Security**: Basic data integrity; no encryption required for game data
- **Compliance**: JDK 1.2 compatibility; Sun coding standards
- **Observability**: Error logging; game state tracking

## Milestones and Release Strategy
1. Core game engine with single-player mode
2. Multiplayer networking implementation
3. Computer opponent basic intelligence
4. GUI completion and user documentation
5. Server administration features
6. Final integration and acceptance testing

## Risk List and Mitigation Strategies
- Network latency affecting multiplayer experience → Implement robust synchronization
- Computer opponent performance issues → Optimize algorithms and set time limits
- Cross-platform compatibility problems → Extensive testing on target platforms
- Rule implementation complexity → Modular rule validation system
- User interface usability concerns → Early prototyping and user feedback
- Server scalability limitations → Load testing and connection pooling
- Team coordination across components → Regular integration meetings
- Schedule constraints → Prioritize Level 1 requirements

## Undecided Issues and Responsible Parties
- Advanced computer opponent intelligence levels (Technical Researchers)
- Custom rule variations implementation (Client Liaison)
- Server GUI administration interface (Project Manager)
- Animation and sound effect details (Technical Researchers)
- High score persistence mechanism (Not mentioned)
- Multi-language support implementation (Not mentioned)
- Undo functionality in multiplayer (Not mentioned)
- Game save/load format specification (Technical Researchers)