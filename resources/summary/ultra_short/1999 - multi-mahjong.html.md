**Purpose & Scope**:  
MultiMahjong is a single/multiplayer Mahjong game requiring exactly 4 players. The system enables networked play (up to 4 players via TCP/IP) and single-player mode with 3 computer opponents. It excludes mobile support, cloud deployment, and non-Chinese Mahjong rule variations beyond core specifications.  

**Product Background / Positioning**:  
Developed for Solid Software Pty Ltd as a commercial product. No existing system; replaces manual Mahjong play with a server-client architecture where the MultiMahjongServer manages game state and the MultiMahjongClient handles user interaction.  

**Core Functional Overview**:  
- Game initiation: Create/join games with 4 players (human or computer opponents).  
- Computer opponent handling: 3 ability levels (Beginner/Intermediate/Advanced) with rule-compliant moves.  
- Real-time game state synchronization across clients.  
- Enforcement of Chinese Mahjong rules for all moves.  
- Score tracking with configurable hand limits.  
- Basic sound effects for game actions.  
- Round-based game progression (4 rounds per game).  
- Game termination and restart options.  

**Key Users & Usage Scenarios**:  
End-users (non-technical Mahjong players) use the client for gameplay. Server administrators (basic networking knowledge) manage the MultiMahjongServer. Single-player mode requires no network; multiplayer requires TCP/IP connectivity.  

**Major External Interfaces**:  
TCP/IP network for multiplayer communication. Java Virtual Machine (JDK 1.2) runtime environment. Client screens constrained to 800×600 resolution with 16-bit color.  

**Key Non-functional Requirements**:  
Computer opponents respond within 1 minute. Server supports up to 10 simultaneous games (40 players). Minimum client hardware: 100 MHz CPU, 32 MB RAM.  

**Constraints, Assumptions & Dependencies**:  
Mandatory use of JDK 1.2. No data encryption required (non-sensitive information). Server must run on a TCP/IP-connected machine. Single-player mode operates without the MultiMahjongServer.  

**Priorities & Acceptance Approach**:  
Acceptance requires all Level 1 functional and non-functional requirements. Level 2/3 features (e.g., undo, advanced UI) are future enhancements; Level 1 defines minimum viable product.