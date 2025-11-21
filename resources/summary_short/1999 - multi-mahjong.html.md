# Short Summary

- **Background and objectives**: MultiMahjong is a single/multiplayer Mahjong game developed for commercial use, supporting up to 4 players over TCP/IP with optional computer opponents. The goal is to provide an engaging, rule-compliant Mahjong experience accessible to users with basic computer skills.

- **In scope**:
  - MultiMahjongServer for hosting multiplayer games over TCP/IP.
  - MultiMahjongClient supporting single-player and network multiplayer modes.
  - Computer opponents to fill player slots when needed.
  - Gameplay following Chinese Mahjong rules.
  - Graphical user interface for client interactions.

- **Out of scope**:
  - Advanced server GUI for administration.
  - Real-time player chat during gameplay.
  - Support for custom player icons or images.
  - Undo or save game features in multiplayer mode.
  - Multi-language support using Unicode.

- **Roles and core use cases**:
  - As a player, I want to join or create a Mahjong game so that I can play against others or computer opponents.
  - As a server administrator, I want to run the MultiMahjongServer so that clients can connect and play multiplayer games.
  - As a user, I want to follow Chinese Mahjong rules so that the game is authentic and fair.

- **Success metrics**:
  - Computer opponents respond within 1 minute.
  - Server supports up to 10 simultaneous games (40 players).
  - Client calculates possible moves within 5 seconds after a discard.

- **Major constraints**:
  - Must be implemented using JDK 1.2 and follow Sun coding standards.
  - Must run on Windows 95/98/NT, Mac OS 8, or Solaris 2.6/7.
  - Minimum 800×600 resolution and 16-bit color for the GUI.
  - Requires TCP/IP network for multiplayer mode.
  - All Level 1 requirements must be met for product acceptance.

- **Undecided issues**:
  - Specific details of graphical animations.
  - Exact layout and behavior of server administration GUI.
  - Ability levels and styles for computer opponents.
  - Variations of Mahjong rules beyond Chinese standard.
  - Not mentioned: Support for non-Chinese language interfaces.