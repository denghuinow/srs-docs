# Balanced Summary: MultiMahjong Project

## Goals and Scope
MultiMahjong is a client-server computer game enabling single or multiplayer Mahjong over TCP/IP networks. The system consists of a MultiMahjongServer managing game sessions and MultiMahjongClients providing user interfaces, supporting up to four players with computer opponents filling empty slots. The product targets Mahjong enthusiasts with basic computer skills and will be commercially distributed by the client, Solid Software Pty Ltd.

## Stakeholders and User Stories
**Stakeholders:**
- **Steve Goschnick (Client)** - Managing Director of Solid Software who commissioned the product for commercial sale.
- **K-Team (Development Team)** - Six university students responsible for designing, implementing, and delivering the software.
- **Anthony Senyard (Supervisor)** - Provides academic oversight and guidance for the project.
- **End Users** - Players who purchase and use the MultiMahjongClient to play Mahjong.
- **Server Administrator** - Technical personnel who install and maintain the MultiMahjongServer on a network server.

**User Stories:**
1. As a player, I want to choose between single and multiplayer games so that I can play alone or with others.
2. As a multiplayer game creator, I want to set player counts and score limits so that I can customize game sessions.
3. As a player, I want visual indicators for valid moves so that I can follow Mahjong rules correctly.
4. As a server administrator, I want the server to relay game data between clients so that players can interact in real-time.
5. As a single player, I want computer opponents to complete the four-player requirement so that I can play without human opponents.
6. As a user, I want to save preferences between sessions so that I don't need to reconfigure settings repeatedly.

## Key Processes
1. **Game Initialization** - Triggered by user selecting "new game"; involves setting player preferences and connecting to server.
2. **Player Join Handling** - Triggered by user selecting "join game"; retrieves available sessions from server and establishes connection.
3. **Turn Management** - Triggered by game state changes; determines active player and enables valid move options.
4. **Move Validation** - Triggered by player action; checks compliance with Chinese Mahjong rules before execution.
5. **State Synchronization** - Triggered by any game action; propagates updates between server and all connected clients.
6. **Computer Opponent Processing** - Triggered when CO turn arrives; calculates moves based on visible game state.
7. **Game Termination** - Triggered by round completion or user request; cleans up resources and returns to main menu.

## Domain Data Elements
1. **Player** (Key: PlayerID) - Name, Icon, Score, WindPosition, ConnectionStatus
2. **Game Session** (Key: GameID) - CreatorID, ScoreLimit, PlayerCount, RoundNumber, Status
3. **Tile** (Key: TileID) - Type, Suit, Value, Position, Owner
4. **Move** (Key: MoveID) - PlayerID, TileID, ActionType, Timestamp, Validity
5. **Preferences** (Key: UserID) - PlayerName, IconPath, SoundSetting, DefaultGameType
6. **High Score** (Key: EntryID) - PlayerName, Score, DateAchieved, GameType

## Non-Functional Requirements
1. **Performance**: Computer opponents must respond within 60 seconds; move validation within 5 seconds.
2. **Scalability**: Server must support up to 10 simultaneous games (40 players).
3. **Portability**: Must run on Windows 95/98/NT, Mac OS 8, and Solaris via Java JDK 1.2.
4. **Usability**: Interface must fit 800×600 resolution with 16-bit color; support mouse and keyboard input.
5. **Reliability**: Clear error handling with distinction between fatal and non-fatal errors.
6. **Documentation**: Comprehensive user and administrator manuals in electronic and print formats.

## Milestones and External Dependencies
1. Completion of Software Requirements Specification (current document)
2. Delivery of Architectural Design Document
3. Implementation of core game logic with Chinese Mahjong rules
4. Integration testing of client-server communication
5. Final delivery with all Level 1 requirements implemented
6. Dependency: Availability of Java JDK 1.2 on target platforms

## Risks and Mitigation Strategies
1. **Network Latency**: Implement robust timeout handling and state synchronization protocols.
2. **Computer Opponent Complexity**: Start with basic rule-following AI, enhance with strategy later.
3. **Cross-Platform Compatibility**: Rigorous testing on all target operating systems early in development.
4. **Schedule Constraints**: Prioritize Level 1 requirements, defer Level 2/3 features as needed.
5. **Rule Implementation Errors**: Create comprehensive test suites based on official Mahjong rulebook.

## Undecided Issues
1. Specific algorithms for computer opponent difficulty levels (Beginner/Intermediate/Advanced)
2. Detailed animation sequences for game actions
3. Exact format and content of server log information
4. Implementation details for chat functionality in multiplayer games
5. Specific sound effects to associate with game actions
6. Complete set of graphical icons for player selection