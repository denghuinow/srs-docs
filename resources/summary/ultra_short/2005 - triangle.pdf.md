**Purpose & Scope**  
The system enables playing combinatorial triangulation games (solitaire, against AI, or multiplayer) and serves as a platform for defining new games. It does not support networked play, personal data storage, or external database dependencies.  

**Product Background / Positioning**  
A standalone Java application based on academic research ("Games on Triangulations"), running on Windows/Linux/Mac via Java 1.4+. GPL-licensed, designed for researchers and game developers to explore theoretical game mechanics.  

**Core Functional Overview**  
- Support multiple game types (default: 3; extensible without code changes).  
- Customizable opening positions (including random selection).  
- Switch player types between human and AI mid-game.  
- Default random AI for all two-player games.  
- External game definition via simple files (e.g., XML/text).  
- Game termination on predefined conditions.  
- Save/load game states.  

**Key Users & Usage Scenarios**  
Primary: Players (academic users with varying technical skill; UI optimized for non-experts). Secondary: Game developers (define new games via files). Players interact via UI; developers modify external files.  

**Major External Interfaces**  
Java 1.4+ runtime with Swing GUI library. Input via mouse/keyboard; output via graphical display. No external databases or network interfaces.  

**Key Non-functional Requirements**  
- AI move calculation ≤10 seconds.  
- Cross-platform (Linux/Windows) via Java.  
- Runs on 450 MHz+ hardware.  
- All UIs support keyboard/mouse.  

**Constraints, Assumptions & Dependencies**  
Mandated Java platform (no platform-specific libraries). GPL license. Requires Java 1.4+ runtime. No network security or data storage needs.  

**Priorities & Acceptance Approach**  
High priority: Core games, AI, end conditions, external game definition. Low priority: Save/load, in-game help. Stable requirements (high/medium priority) will not change; low-priority features may be deferred.