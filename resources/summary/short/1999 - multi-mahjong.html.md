# Short Summary: MultiMahjong Project

## Background and Objectives
MultiMahjong is a client-server computer game enabling single or multiplayer Mahjong over TCP/IP networks. The primary objective is to create a commercial product where up to four players (human or computer opponents) can play Chinese Mahjong, with the client sold to users and the server hosted by the client.

## In Scope
- Client-server architecture supporting up to 4 players (human/computer) over TCP/IP.
- Single-player mode with 3 computer opponents.
- Gameplay following Chinese Mahjong rules, including tile handling and scoring.
- Basic graphical user interface for the client within 800x600 resolution.
- Essential documentation for installation and operation.

## Out of Scope
- Advanced computer opponent strategies (e.g., look-ahead algorithms).
- Real-time chat between players during gameplay.
- Multi-language support via Unicode.
- Server graphical user interface for administration.
- Animation and advanced sound effects in the client.

## Stakeholders and Core Use Cases
**Stakeholders:**
- **Steve Goschnick (Client)**: Managing Director of Solid Software Pty Ltd, responsible for commercial deployment and acceptance.
- **K-Team (Development Team)**: Responsible for design, implementation, and delivery of the MultiMahjong system.
- **Anthony Senyard (Supervisor)**: Provides oversight and guidance for the project.
- **End Users**: Players who use the MultiMahjongClient to play Mahjong, requiring intuitive gameplay.
- **Server Administrator**: Manages the MultiMahjongServer, ensuring network setup and operation.

**Core Use Cases:**
1. As a player, I want to create a new multiplayer game so that I can play with others over a network.
2. As a player, I want to join an existing game so that I can participate without hosting.
3. As a player, I want to play against computer opponents so that I can play when human players are unavailable.
4. As a player, I want to see game updates (e.g., discards, exposures) so that I can make informed moves.
5. As a player, I want to be notified of valid moves (e.g., Chow/Pung) so that I can follow Mahjong rules.
6. As an administrator, I want to run the server on a TCP/IP network so that clients can connect and play.

## Success Metrics
- Computer opponents respond within 1 minute during gameplay.
- Server handles up to 10 simultaneous games (40 players) without performance issues.
- Client calculates possible moves within 5 seconds after a discard.

## Major Constraints
- Must be developed using JDK 1.2 (Java) with Sun Microsystems coding standards.
- Requires compatibility with PCs (Windows 95/98/NT), Macintosh (OS 8), and Unix (Solaris).
- Minimum hardware: 100 MHz processor, 32 MB RAM, 10 MB disk space, 800x600 resolution.
- Network dependency for multiplayer mode (TCP/IP connection).
- All Level 1 requirements must be met for project acceptance.

## Undecided Issues
- Implementation details for the graphical user interface (e.g., exact layout and controls).
- Specific data structures for tile management and game state.
- Advanced features like undo/save in single-player mode.
- Ability for users to upload custom icons/images.
- Variations of Mahjong rules beyond the Chinese standard.