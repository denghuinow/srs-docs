# MultiMahjong - Software Requirements Specification

## System Overview
MultiMahjong is a single/multi-player Mahjong computer game consisting of two programs: MultiMahjongServer and MultiMahjongClient. The Server/Client architecture allows up to 4 players to play Mahjong against each other over a TCP/IP network. The MultiMahjongClient also supports single-player mode against computer opponents.

## System Architecture

### MultiMahjongServer
- Resides on a central computer connected to a TCP/IP network with a unique IP address
- Allows connections from MultiMahjongClients and communicates using IP
- Serves as a node for MultiMahjongClients, relaying data between clients
- Automates game initialization functions (randomizing tile order, seating positions)
- Stores game information database
- Contains High Scores list with top players' names and scores

### MultiMahjongClient
- Graphical user interface for player interaction
- Supports both single-player (stand-alone) and multi-player modes
- Processes computer opponent actions
- Communicates with MultiMahjongServer in multi-player mode

## Functional Requirements

### Game Initialization

#### Multi-Player Game Creation
- Users enter name and choose icon from predetermined list
- Select number of human and computer opponents (total of 4 players)
- Set score limit for winning a hand
- Begin game when all necessary human players have joined

#### Single-Player Game Creation
- Users enter name and choose icon
- Set score limit for winning a hand
- Play against 3 computer opponents

#### Joining Existing Games
- Retrieve list of available games from MultiMahjongServer
- Display game information: creator's name/icon, score limit, available positions
- Select and join desired game

### Game Play

#### Core Gameplay
- Enforce Chinese Mahjong rules for all moves
- Inform user when it's their turn to pick up a tile
- Retrieve and display other players' game changes from server
- Allow Chow/Pung/Kong/Mahjong actions when rules permit
- Enable tile picking and discarding on user's turn
- Notify users of other players' special conditions (fishing, Mahjong)
- Handle hand draws and round completion

#### User Interface Features
- Display user's tiles, wall, other players' tiles, revealed/exposed sets
- Show last discarded tile
- Provide action buttons (pick up, discard, Chow/Pung/Kong/Mahjong, reveal Kong)
- Grey out inactive buttons when actions are not permitted
- Display player information in tabbed frames (names, icons, wind of round, scores, limits)
- Show dead tiles

#### Computer Opponents (CO)
- Play according to Chinese Mahjong rules
- No access to concealed tiles or wall contents
- Read exposed/revealed hands and tile counts
- Perform basic strategic decisions (avoid discarding tiles in "almost finished" sets)
- Determine unplayed tiles based on game history
- Operate at different ability levels (Beginner, Intermediate, Advanced)
- Support look-ahead algorithms for advanced play

### Game Termination
- End after 4 rounds or user choice
- Allow users to end game at any stage
- Handle premature user departure by replacing with computer opponent
- Notify all clients when game ends

## Non-Functional Requirements

### User Characteristics
- MultiMahjongClient users: Anyone interested in Mahjong with basic PC knowledge
- MultiMahjongServer users: Network administrators with TCP/IP server knowledge
- No advanced networking knowledge required for players

### Implementation Constraints
- Written using JDK 1.2 (Java development kit)
- Follow Sun Microsystems coding standards
- Support multiple languages using Java's Unicode standard

### Hardware Constraints
- Runs on machines supporting JDK 1.2:
  - PC with Windows 95/98/NT
  - Macintosh with OS 8
  - Unix with Solaris 2.6 or 7
- Minimum requirements: 100 MHz processor, 32 MB RAM, 10 MB disk space, 16-bit video card (800x600)

### Performance Requirements
- Computer opponents respond within 1 minute
- Server handles up to 10 simultaneous games (40 players)
- Client calculates possible moves within 5 seconds

### Error Handling
- Nonfatal errors: Display error dialogue, allow game continuation
- Fatal errors: Display error dialogue, terminate program cleanly
- Include troubleshooting guide access for nonfatal errors

### Security
- No encryption required as data contains no private information
- Data exchange does not compromise system integrity

## User Interface Requirements

### MultiMahjongServer
- Command prompt interface for basic operation
- Optional graphical interface for administration (log info, game settings)

### MultiMahjongClient
- Graphical user interface with mouse and keyboard support
- 800x600 pixel screen resolution
- 16-bit color graphics
- Sound effects for game actions
- Keyboard shortcuts for mouse operations

### Main Window Components
- Player's tile faces
- Wall with remaining tiles
- Other players' tile backs
- Revealed/exposed tiles from all players
- Last discarded tile
- Action buttons with appropriate activation states
- Tabbed frames for player info, scores, and preferences

## Documentation Requirements

### MultiMahjongServer
- Administrator's manual (electronic format)
- Installation and operation instructions
- TCP/IP server configuration guidance
- Troubleshooting information
- Technical background on product development

### MultiMahjongClient
- User's manual (both hard copy and electronic)
- Installation instructions
- Game initiation and joining procedures
- Mahjong rules and scoring explanation
- GUI component descriptions
- Troubleshooting guide
- Online access to manual

### Development Documentation
- Software Quality Assurance Plan (SQAP)
- Software Requirements Specification (SRS)
- Software Architectural Design Document (SADD)
- Software Design Document (SDD)
- Software Verification & Validation Plan (SVVP) and Test Plan (TP)
- Source code (electronic and hard copy)

## Quality Attributes
- Portability across multiple operating systems
- Network transparency for multi-player games
- Responsive computer opponents with strategic capabilities
- Intuitive graphical interface with visual feedback
- Comprehensive error handling and recovery
- Extensible design supporting rule variations
- Unicode support for internationalization
- Performance optimization for network communication
