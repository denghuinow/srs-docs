**Purpose & Scope**
The system is a software application for playing and defining various combinatorial "triangulation games" based on a specific research article. It allows playing games as solitaire, against a computer AI, or with another human player. It does not function as a networked or online gaming platform.

**Product Background / Positioning**
This is a stand-alone application designed to realize the games described in the academic article "Games on Triangulations." It serves as both a playable implementation for researchers and a platform for defining new game types without modifying the core software code.

**Core Functional Overview**
*   Provide a graphical user interface operable with both mouse and keyboard.
*   Support multiple, user-definable triangulation games (initially three types: constructing, transforming, marking).
*   Allow selection of specific or random opening positions for a game.
*   Support two-player, turn-based play with either human or AI players.
*   Include a default AI that makes random legal moves.
*   Enable changing a player (e.g., from human to AI) during an active game.
*   Load new game definitions from external files at runtime.
*   End a game based on a condition defined in its external game file.

**Key Users & Usage Scenarios**
Primary users are **Players** (researchers or students from fields like mathematics or computer science) who play the games. A secondary user class is **Game Developers** who define new games using external files. A typical scenario involves a player starting a new game, selecting a game type and opening position, choosing opponents (human/AI), and playing until a win condition is met.

**Major External Interfaces**
The user interface consists of a main game window and dialog windows. The system requires a Java Runtime Environment (version 1.4 or later) and a graphical environment supported by Java Swing. It interacts with the local file system to load/save games and AI modules.

**Key Non-functional Requirements**
*   **Performance:** The default AI must calculate its next move within 10 seconds.
*   **Portability:** The system must run on both Linux and Windows operating systems.
*   **Usability:** The system must be fully operable using only a keyboard or only a mouse.
*   **Safety:** The system must request user confirmation before overwriting an existing file.

**Constraints, Assumptions & Dependencies**
*   The software must be implemented in Java and cannot depend on platform-specific libraries.
*   It assumes a Java Runtime Environment (JRE 1.4+) is installed on the target machine.
*   It is dependent on the Java Swing library for its graphical interface.
*   The software will be released under the GPL license.

**Priorities & Acceptance Approach**
High-priority features include the core GUI, multiple game support, opening position selection, the default random AI, external game definitions, and game end conditions. Medium-priority features include changing player types during a game and an in-game help function. Low-priority features include saving/loading games and loading new AI from files. Acceptance is based on the system fulfilling the specified functional requirements and meeting the defined non-functional metrics (e.g., AI response time).