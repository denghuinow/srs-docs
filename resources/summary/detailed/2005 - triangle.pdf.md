# Detailed Summary: Triangulation Games Software Requirements

## Background and Scope
This document specifies the requirements for the Triangulation Games software, a Java-based application for playing and defining combinatorial triangulation games. The system serves as a platform for playing games (solitaire, human vs. computer, or two-player) based on the article "Games on Triangulations" and allows users to define new games without modifying the source code. Non-goals include network play, high-end graphics, and complex AI beyond a default random mover.

## Stakeholders Matrix and Use Cases
*   **Researchers**: Seek research value and theoretical problems; require a consistent, scientific program layout.
*   **Basic User / Game Player**: Seek entertainment and fun; require the system to run on low-end workstations and be easy to use.
*   **Game Developer**: Want a platform to test new triangular games; require ease of developing new games and clear documentation.
*   **Development Team**: Aim to develop a working program and learn; require an easy-to-use development environment.

**Main/Exception Scenarios (≤8):**
1.  **UC-001 Start Application**: User starts the app; system shows GUI. *Exception*: Error loading a game/AI informs user.
2.  **UC-002 Start New Game**: User selects game, opening position, and player types (human/AI). *Exception*: Empty game list prevents start.
3.  **UC-003 Select Opening Position**: User chooses from predefined or random starting positions for a selected game.
4.  **UC-004/005 Select Player Nature & AI**: User assigns human or AI (e.g., default random AI) to each player role.
5.  **UC-006 Change Player Mid-Game**: User substitutes a human player with an AI during an active game.
6.  **UC-008 Define New Game**: User defines a new game in an external file (e.g., XML); system loads it. *Exception*: Invalid file definition aborts load.
7.  **UC-009 Game Ends**: Game concludes when a predefined ending condition is met; system declares winner/scores.
8.  **UC-010/011 Save/Load Game**: User saves game state to a file or loads a saved game to continue. *Exception*: No file exists to load.

## Business Process
**Main Process: Play a Game (≤8 steps)**
1.  **Trigger**: User starts the application (UC-001).
2.  User initiates a new game (UC-002).
3.  System presents available games; user selects one.
4.  System offers opening positions; user selects one or chooses random (UC-003).
5.  System prompts for player type (Human/AI) for each player; user configures (UC-004/005).
6.  **Input**: User/AI makes moves according to game rules.
7.  System validates moves and updates game state.
8.  **Output**: Game ends when ending condition is met; system displays results (UC-009).

**Key Branch A: Modify Game Session (≤4 steps)**
1.  **Trigger**: User chooses to change player type mid-game.
2.  User selects a player to replace (UC-006).
3.  System prompts for new player type (Human/AI).
4.  Game continues with the new configuration.

**Key Branch B: Extend System (≤4 steps)**
1.  **Trigger**: Developer creates a new game definition file.
2.  File is placed in a predefined directory.
3.  On startup, system automatically discovers and loads the new game (UC-008).
4.  New game appears in the selection list for all users.

## Domain Model (Entities ≤8)
1.  **Game**: `gameId` (unique), `name` (required), `type` (required), `rulesDefinition` (required).
2.  **GameSession**: `sessionId` (unique), `currentState` (required), `movesHistory`.
3.  **Player**: `playerId` (unique), `type` (required: Human/AI), `aiStrategyReference` (conditional).
4.  **Move**: `moveId`, `playerReference` (required), `actionDetails` (required).
5.  **OpeningPosition**: `positionId` (unique), `configurationData` (required), `gameTypeReference`.
6.  **AIModule**: `aiId` (unique), `strategyName`, `sourceFileReference`.
7.  **SavedGame**: `saveId` (unique), `sessionData` (required), `timestamp` (required).
8.  **HelpContent**: `topicId`, `content` (required), `relatedGameReference`.

## Interfaces and Integrations (≤8)
1.  **System**: Java Swing GUI | **Direction**: Outbound | **Interaction**: User input/output | **Input**: Mouse clicks, keyboard commands | **Output**: Game board display, menus, dialogs | **SLA**: Responsive to user actions.
2.  **System**: File System | **Direction**: Inbound/Outbound | **Interaction**: Game/AI Definition & Save/Load | **Input**: Game definition files (XML/text), AI module files, save files | **Output**: Saved game state files | **SLA**: File operations confirmed; overwrites require user confirmation.
3.  **System**: Java Runtime Environment (JRE) | **Direction**: Inbound | **Interaction**: Execution Platform | **Input**: N/A | **Output**: N/A | **SLA**: Requires JRE version 1.4 or later.
4.  **System**: AI Module Loader | **Direction**: Inbound | **Interaction**: Dynamic AI Integration | **Input**: Compiled AI class/files | **Output**: AI available in player selection | **SLA**: Loads on startup; invalid modules fail gracefully.

## Acceptance Criteria
*   **Capability: Start and Play a Game**
    *   **Given** the application is installed, **when** a user starts it and selects a game, opening position, and human vs. AI players, **then** a game board is displayed and turns can be taken.
    *   **Given** a game is in progress, **when** a player makes a move that fulfills the ending condition, **then** the game stops and the result/score is displayed.
*   **Capability: Modify and Extend Games**
    *   **Given** a game is being played, **when** a user selects the option to change a player to AI, **then** the AI takes the next turn and play continues.
    *   **Given** a valid new game definition file is placed in the correct directory, **when** the application restarts, **then** the new game appears in the game selection menu.

## Non-Functional Metrics
*   **Performance**: AI must calculate next move within 10 seconds. Should be playable on a 450 MHz computer.
*   **Reliability**: Must run on both Linux and Windows OS with JRE 1.4+. File save operations must prevent accidental data loss.
*   **Security**: No specific security requirements as no personal data is stored.
*   **Compliance**: Released under GPL license.
*   **Observability**: User must be informed of errors (e.g., loading failures) via the GUI.

## Milestones and Release Strategy (≤6)
1.  Core application framework with GUI and basic input handling.
2.  Implementation of default random AI and support for human vs. AI play.
3.  Integration of the three high-priority default games (e.g., Monochromatic complete triangulation).
4.  Game definition file loading mechanism for user-defined games.
5.  Save and load game state functionality.
6.  Final release with documentation (user manual, maintenance manual).

## Risk List and Mitigation Strategies (≤8)
1.  **Risk**: Complexity of game logic from the academic paper. **Mitigation**: Close collaboration with the client (researcher) for clarification; implement core games first.
2.  **Risk**: AI performance exceeding the 10-second limit for complex positions. **Mitigation**: Optimize default random AI; set clear expectations for user-developed AIs.
3.  **Risk**: Game definition file format is too complex for non-programmers. **Mitigation**: Create detailed documentation and examples; consider a simple structured format like XML with a schema.
4.  **Risk**: Cross-platform GUI inconsistencies. **Mitigation**: Use Java Swing consistently and test early on target platforms (Linux, Windows).
5.  **Risk**: Low priority features (e.g., advanced AI loading) consuming excessive development time. **Mitigation**: Implement after core features are stable; scope may be reduced.

## Undecided Issues and Responsible Parties (≤8)
1.  **Exact syntax and schema for the external game definition file.** *Responsible: Development Team & Client.*
2.  **Detailed API/interface for third-party AI module development.** *Responsible: Development Team.*
3.  **Specific usability guidelines and detailed UI design.** *Responsible: Development Team.*
4.  **Priority and implementation details for lower-priority game types (e.g., Nimstring game).** *Responsible: Client & Development Team.*
5.  **Distribution and installation method for end-users.** *Responsible: Development Team.*