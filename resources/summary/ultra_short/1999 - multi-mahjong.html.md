**Purpose & Scope**
The system is a Mahjong computer game supporting single-player and multiplayer modes over a TCP/IP network. It consists of a server and client application. The system enforces Chinese Mahjong rules and manages game state, but does not include data encryption or support for non-TCP/IP network protocols.

**Product Background / Positioning**
This is a new product with no existing system. The client program is intended for commercial sale to end-users. The server program will initially be hosted on infrastructure owned/operated by the client company, Solid Software Pty Ltd.

**Core Functional Overview**
1.  Establish and manage multiplayer games for up to four players via a central server.
2.  Support single-player games against three computer opponents.
3.  Enforce moves according to the standard Chinese rules of Mahjong.
4.  Allow users to create new games, join existing games, and specify human/computer opponents.
5.  Automatically calculate and indicate valid player moves (Chow, Pung, Kong, Mahjong).
6.  Relay game state changes (discards, exposed sets) between all connected clients.
7.  Provide a computer opponent (CO) capable of playing by the rules.

**Key Users & Usage Scenarios**
Primary users are individuals interested in Mahjong, with basic PC/Mac/Unix operating knowledge. A multiplayer game creator sets up a game and waits for others to join. A joiner selects an available game from a server list. All users interact via a graphical client to take turns picking up, discarding, and forming sets of tiles.

**Major External Interfaces**
The server communicates with multiple clients over a TCP/IP network. The client presents a graphical user interface for user interaction. The client also interfaces locally to manage computer opponent logic in single-player mode.

**Key Non-functional Requirements**
1.  The computer opponent must respond within 1 minute.
2.  The server must handle up to 10 simultaneous games (40 players).
3.  The client must calculate possible moves within 5 seconds of a discard.
4.  The client must run on any machine with a Java Virtual Machine supporting JDK 1.2 (e.g., Windows 95+, Mac OS 8, Solaris).
5.  The graphical user interface must fit within an 800x600 pixel resolution using 16-bit color.

**Constraints, Assumptions & Dependencies**
1.  The system must be implemented using JDK 1.2 (Java).
2.  The client assumes users' computers are correctly configured for TCP/IP networking.
3.  The server requires a unique IP address and knowledge of server administration from its operator.
4.  The reader of the requirements is assumed to be familiar with Chinese Mahjong rules.

**Priorities & Acceptance Approach**
All Level 1 requirements are essential and constitute the acceptance criteria for the product. Level 2 requirements are highly desirable but not mandatory for acceptance. Level 3 requirements are desirable future additions. The product is accepted if it meets all Level 1 requirements.