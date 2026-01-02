**Purpose & Scope**: The system is a Mahjong game enabling single-player and multiplayer (up to 4 players) sessions over a TCP/IP network, using a central server for multiplayer coordination.

**Core Functions**:
*   Initiate and join multiplayer games via a network server.
*   Play a standalone single-player game against computer opponents.
*   Enforce gameplay according to the Chinese rules of Mahjong.
*   Provide a graphical user interface for player interaction.

**Key Users**: Players interested in Mahjong with basic computer operation skills.

**Key Constraints**:
*   Implemented using JDK 1.2 (Java).
*   Must run on Windows, Mac OS, and Unix platforms supporting the Java Virtual Machine.
*   Computer opponents must respond within one minute.
*   The server must support up to 10 simultaneous games.