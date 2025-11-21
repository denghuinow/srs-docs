Purpose & Scope: Qheadache solves a specific puzzle-based headache through a computer game. It is a standalone application with no external system integration. The system does not handle network communication, multiplayer, or advanced analytics beyond basic scoring.

Product Background / Positioning: The game is a simple standalone puzzle application targeting casual players. It requires Qt library support across compatible operating systems and runs independently without external dependencies.

Core Functional Overview:  
- Undo/Redo actions for last 1,000 moves  
- Real-time tracking of play duration and move count  
- Scoring system recording moves and time per player  
- Win condition triggered by positioning the large square block  
- Statistics window displaying top 10 player scores  

Key Users & Usage Scenarios: Casual players aged 8+ requiring no specialized training. Primary scenarios include playing a single game, reviewing statistics, and saving/loading progress. No permission tiers exist.

Major External Interfaces: Input via keyboard/mouse (with alternative pointing device support). Output requires 800x600 minimum display resolution. Uses Qt library for all graphical operations.

Key Non-functional Requirements: Must run on all Qt-supported operating systems. Single-user per machine. Statistics file stores exactly 10 player records.

Constraints, Assumptions & Dependencies: Requires 800x600 display resolution. Depends on Qt library for GUI. Statistics file management limits to 10 entries.

Priorities & Acceptance Approach: Core game mechanics (movement, scoring, win condition) are critical. Acceptance requires successful game completion with valid statistics recorded. File management is secondary.