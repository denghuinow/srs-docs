# Balanced Summary: Triangulation Games Software Requirements

## Goals and Scope
The Triangulation Games software is an application for playing various combinatorial triangulation games, either as solitaire, against computer AI, or with another player. It also serves as a platform for defining new types of triangulation games based on academic research, with a focus on an easy-to-use graphical interface. The system is designed to be cross-platform and extensible without modifying core code.

## Stakeholders and User Stories
*   **Researchers:** Seek new research problems and require a consistent, scientific program layout.
*   **Basic User / Game Player:** Values entertainment and relaxation, needing the software to run on low-end workstations and be easy to use.
*   **Game Developer:** Interested in using the platform to test new triangular games, requiring good documentation for extending the system.
*   **Development Team:** Aims to develop a working program and learn software project practices.

**User Stories:**
1.  As a **Player**, I want to choose from multiple game types and opening positions so that I can explore different challenges.
2.  As a **Player**, I want to play against a human or a computer AI so that I can play alone or with a friend.
3.  As a **Player**, I want to save and load games so that I can continue playing later.
4.  As a **Game Developer**, I want to define new games in external files without modifying source code so that I can extend the platform easily.
5.  As a **Game Developer**, I want to load new AI implementations from files so that I can test different strategies.
6.  As a **User**, I want to access in-game help so that I can understand game rules and functionalities.

## Key Processes
1.  **System Start:** Triggered by user activation; the application loads and displays the main graphical interface.
2.  **New Game Setup:** Triggered by user menu selection; the system presents available games, opening positions, and player types (Human/AI) for configuration.
3.  **Gameplay:** Triggered by the start of a configured game; players (human or AI) take turns making moves on the triangulation.
4.  **Player Nature Change:** Triggered by user request during a game; a human player can be replaced by an AI (or vice versa) without restarting.
5.  **Game End Detection:** Triggered by a move that fulfills a predefined ending condition; the system declares a winner and displays scores.
6.  **Game Save/Load:** Triggered by user menu selection; the system writes the game state to a file or loads it to resume play.
7.  **External Resource Loading:** Triggered at startup or by user action; the system searches for and loads new game definitions or AI implementations from external files.

## Domain Data Elements
*   **Game:** (Game ID, Game Type, Ending Condition, Rules Definition, Supported Opening Positions)
*   **Player:** (Player ID, Player Type [Human/AI], AI Strategy Reference, Score)
*   **Game Session:** (Session ID, Current Game State, Current Player Turn, Move History, Session Start Time)
*   **Opening Position:** (Position ID, Position Type, Graph Coordinates, Associated Game Types)
*   **Artificial Intelligence (AI):** (AI ID, AI Name, Implementation File Path, Supported Games)
*   **Move:** (Move ID, Game Session ID, Player ID, Move Details, Timestamp)

## Non-Functional Requirements
1.  **Cross-Platform Compatibility:** The system shall run on any OS with Java Runtime Environment (JRE) version 1.4 or later and a graphical environment.
2.  **Performance:** The default AI must calculate its next move within 10 seconds.
3.  **Usability:** The interface must be fully operable via both mouse and keyboard.
4.  **Extensibility:** New games and AIs must be loadable from external files without code modification.
5.  **Data Safety:** File overwrites must require user confirmation to prevent accidental data loss.
6.  **Installation Simplicity:** Installation should be easy, with no external database dependencies.

## Milestones and External Dependencies
1.  Implementation of the three default game categories (Constructing, Transforming, Marking) with priority 1 games.
2.  Completion of the core graphical user interface and game engine.
3.  Finalization of the file format and system for defining and loading external games.
4.  **Dependency:** Availability and stability of the Java Swing library for the GUI.
5.  **Dependency:** Adherence to the theoretical game definitions from the referenced research article.

## Risks and Mitigation Strategies
1.  **Risk:** Overly complex game definition format for non-programmer developers.
    *   **Mitigation:** Use a simple, well-documented format (e.g., XML) and provide clear examples.
2.  **Risk:** AI performance degrades with complex game states, exceeding the 10-second response time.
    *   **Mitigation:** Implement performance monitoring and allow AI developers to specify complexity limits.
3.  **Risk:** Low priority features (e.g., advanced AI loading, game saving) consume disproportionate development time.
    *   **Mitigation:** Strictly prioritize implementation based on the defined priority table and client feedback.
4.  **Risk:** Inconsistent user experience across different operating systems due to Java Swing rendering.
    *   **Mitigation:** Early and frequent testing on target platforms (Linux, Windows).
5.  **Risk:** The research-oriented user base finds the interface too simplistic or the game implementations inaccurate.
    *   **Mitigation:** Engage stakeholder researchers early for feedback on prototypes and scientific correctness.

## Undecided Issues
1.  The exact file format (e.g., XML, custom text) for defining new games.
2.  The specific interface and API for third-party AI plug-in development.
3.  The detailed visual design and layout guidelines for the usability document.
4.  The mechanism for "random opening position" generation for each game type.
5.  The format and scope of the embedded help file content.
6.  The implementation priority for specific game variants listed as priority 3 or 4 in the table.