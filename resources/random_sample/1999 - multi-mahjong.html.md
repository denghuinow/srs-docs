# Ultra Short Summary
MultiMahjong is a single/multiplayer Mahjong game with client-server architecture supporting up to 4 players over TCP/IP.

- MVP points
  - MultiMahjongClient allows single-player mode against 3 computer opponents or multiplayer with human/computer players.
  - MultiMahjongServer enables network play by relaying data between clients.
  - Game follows Chinese Mahjong rules with tile picking, discarding, and Chow/Pung/Kong/Mahjong moves.
  - Players can create/join games, set names/icons, and specify score limits.

- Key constraints
  - Must be implemented using JDK 1.2 and run on Windows, Mac OS 8, or Solaris systems.
  - Computer opponents must respond within 1 minute.
  - Server must handle up to 10 simultaneous games (40 players).

- Major risks/undecided issues
  - Not mentioned.
  - Not mentioned.