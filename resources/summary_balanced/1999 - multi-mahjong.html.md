# Balanced Summary

- **Goals and scope**: MultiMahjong is a single/multiplayer Mahjong game supporting up to 4 players over TCP/IP. It includes a server-client architecture, computer opponents, and follows Chinese Mahjong rules. The client program is for commercial sale, while the server is centrally hosted.

- **Roles and user stories**:
  - As a player, I want to create or join a multiplayer game so that I can play with others online.
  - As a player, I want to play against computer opponents so that I can play when human players are unavailable.
  - As a player, I want to see game updates in real time so that I can follow other players' moves.
  - As a server administrator, I want to host the MultiMahjongServer so that clients can connect and play games.
  - As a user, I want to save my preferences so that my settings are retained between sessions.

- **Key processes**:
  1. **Trigger: Program start** – User selects to create or join a single/multiplayer game.
  2. **Trigger: Game creation** – User enters name, selects icon, and sets game parameters.
  3. **Trigger: Player action** – Player takes a turn by picking up or discarding a tile.
  4. **Trigger: Valid move** – System checks for Chow/Pung/Kong/Mahjong opportunities.
  5. **Trigger: Network event** – Server relays game state updates to all clients.
  6. **Trigger: Game end condition** – Game concludes after 4 rounds or player exit.
  7. **Trigger: Quit command** – User exits the program or returns to the main menu.

- **Domain data elements**:
  - **Player**: PlayerID, Name, Icon, Score, WindPosition
  - **Game**: GameID, ScoreLimit, CurrentRound, WindOfTheRound, PlayerList
  - **Tile**: TileID, Type, Position, Owner
  - **GameAction**: ActionID, PlayerID, TileID, ActionType, Timestamp

- **Non-functional requirements**:
  - CO response time under 1 minute.
  - Support for 10 simultaneous games (40 players) on the server.
  - Client must calculate valid moves within 5 seconds.
  - Run on Windows, Mac, Unix with JDK 1.2.
  - GUI operable at 800x600 resolution in 16-bit color.

- **Milestones and external dependencies**:
  - Implementation using JDK 1.2.
  - Dependency on TCP/IP network for multiplayer.
  - Use of Chinese Mahjong rulebook for game logic.
  - Delivery of administrator and user documentation.
  - Client sign-off on Level 1 requirements for acceptance.

- **Risks and mitigation strategies**:
  - Network latency affecting multiplayer experience – optimize data exchange and use efficient protocols.
  - CO intelligence may be too simplistic – implement basic strategy and tile tracking.
  - Cross-platform compatibility issues – adhere to Java standards and test on target OSes.
  - Insufficient player base for multiplayer – include robust single-player with COs.
  - Rule implementation errors – validate against authoritative Mahjong rulebook.

- **Undecided issues**:
  - Specific tile class implementation details.
  - Exact content of screen update commands.
  - Wind of the Round representation format.
  - Graphic request command structure.
  - Animation details for GUI actions.
  - Multi-language support implementation.