# Software Requirements Specification (SRS)
## Combinatorial Triangulation Game Platform (CTGP)

**Document Version:** 1.0  
**Date:** [Current Date]  
**Authors:** [Project Team]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Combinatorial Triangulation Game Platform (CTGP). The primary purpose of this document is to provide a definitive description of the software for developers, testers, project managers, and stakeholders. It will serve as the foundation for the design, implementation, and verification phases of the project.

#### 1.2 Scope
The CTGP is a standalone, cross-platform Java application that provides an interactive environment for playing, defining, and analyzing combinatorial triangulation games as described in a specific theoretical article (reference to be supplied). The platform will include a graphical user interface (GUI) for gameplay, support for multiple player configurations (Human/Human, Human/AI, AI/AI), and a framework for defining new game rules without modifying the application's source code.

**In-Scope:**
*   Development of a Java-based desktop application.
*   Implementation of a graphical interface for game visualization and interaction.
*   Provision of several predefined triangulation games based on the referenced article.
*   A mechanism to define new games via external configuration files.
*   Implementation of player agents: Human (via GUI) and AI (including a default random-move AI).
*   Management of game state, rules enforcement, and turn-taking.

**Out-of-Scope:**
*   Web-based or mobile deployment.
*   Network/multiplayer functionality over a network.
*   Development of advanced, strategic AI (beyond the required random-move AI and the 10-second constraint).
*   Creation of the theoretical mathematical models for new games; the platform consumes defined rules.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **CTGP:** Combinatorial Triangulation Game Platform.
*   **SRS:** Software Requirements Specification.
*   **GUI:** Graphical User Interface.
*   **AI:** Artificial Intelligence (Player Agent).
*   **Triangulation:** In this context, a subdivision of a geometric shape (e.g., polygon) into triangles, meeting specific combinatorial rules as defined per game.
*   **Move:** A legal action taken by a player within the rules of a specific triangulation game.
*   **Game Definition:** An external file (e.g., JSON, XML) that specifies the rules, initial state, and win conditions for a triangulation game.

#### 1.4 References
1.  [To be inserted: Citation for the specific theoretical article on combinatorial triangulation games].
2.  IEEE Std 830-1998, IEEE Recommended Practice for Software Requirements Specifications.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its user classes, and operating environment. Section 3 details the specific functional and non-functional requirements. Appendices may include mock-ups, data format specifications, or glossary expansions.

---

### 2. Overall Description

#### 2.1 Product Perspective
The CTGP is a new, self-contained application. It may read from and write to the local file system to load game definitions and save/load game states. It has no direct dependencies on other software systems but requires a Java Runtime Environment (JRE).

#### 2.2 Product Functions (Summary)
1.  **Game Management:** Load, initialize, and manage the state of combinatorial triangulation games.
2.  **Visualization & Interaction:** Display the game board (triangulation state) graphically and allow human players to input moves via mouse/keyboard.
3.  **Player Agent Support:** Facilitate gameplay between different agent types (Human, AI).
4.  **Game Definition Interface:** Parse and validate external files to configure new games.
5.  **AI Framework:** Provide an interface for AI players, including a default implementation.
6.  **Game Administration:** Control game flow (start, pause, restart, undo/redo where logically permissible).

#### 2.3 User Classes and Characteristics
*   **Player:** Interacts with the GUI to play predefined games against another human or AI. Has basic computer literacy.
*   **Game Designer (Advanced User):** Creates and modifies external game definition files to explore new triangulation games. Requires understanding of the game theory concepts from the base article and basic file editing skills.
*   **AI Developer (Advanced User):** May implement custom AI classes adhering to the platform's AI interface, plugging them into the application for testing. Requires Java programming knowledge.

#### 2.4 Operating Environment
*   **Software:** Any operating system (Windows, macOS, Linux) with a compatible Java Runtime Environment (JRE) version 11 or higher installed.
*   **Hardware:** Standard desktop or laptop computer with a display supporting at least 1024x768 resolution. No specialized hardware required.

#### 2.5 Design and Implementation Constraints
1.  **Implementation Language:** The application core and GUI must be implemented in Java to ensure cross-platform compatibility.
2.  **AI Performance Constraint:** Any AI player must compute and select its next move within **10 seconds** on standard hardware for any valid game state in the predefined games.
3.  **Extensibility Constraint:** Adding new game rules must be possible without modifying or recompiling the application source code. This must be achieved through external, user-editable definition files.
4.  **Standalone Application:** The product must be distributable as a single, executable JAR file or equivalent bundled package.

#### 2.6 User Documentation
The application shall include integrated help documentation accessible from the GUI, covering:
*   How to play the included predefined games.
*   Instructions for using the interface (selecting modes, making moves).
*   A guide to the format for creating custom game definition files.

#### 2.7 Assumptions and Dependencies
*   It is assumed the user has a compatible JRE installed.
*   The mathematical validity of moves in custom game definitions is the responsibility of the Game Designer; the platform enforces syntactical and basic rule constraints but cannot guarantee logical consistency.

---

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 User Interfaces
*   **Main Window:** Contains a menu bar (File, Game, View, Help), a game visualization panel, a move history/log panel, and a control panel with buttons (e.g., New Game, Undo, Redo, Pause).
*   **Game Visualization:** A clear, graphical representation of the current triangulation state. Vertices and edges must be selectable for human move input. Visual distinction between players' moves.
*   **Dialogs:**
    *   "New Game" Dialog: To select from predefined games or load a custom game file, and to choose player types (Human/AI) for each player position.
    *   "Game Over" Dialog: To announce the winner and options to replay or quit.

##### 3.1.2 Hardware Interfaces
None.

##### 3.1.3 Software Interfaces
*   **Java Runtime Environment (JRE):** Version 11 or higher.
*   **File System:** Read access for loading game definition files. Read/Write access for saving/loading game states (optional feature).

##### 3.1.4 Communications Interfaces
None.

#### 3.2 Functional Requirements

##### 3.2.1 Game Core (GC)
*   **GC-1:** The system shall maintain an internal representation of the game state for a loaded triangulation game.
*   **GC-2:** The system shall validate all moves proposed by any player (human or AI) against the rules of the currently loaded game.
*   **GC-3:** The system shall detect and announce a terminal game state (win, loss, or draw as per game rules).

##### 3.2.2 Graphical User Interface (GUI)
*   **GUI-1:** The system shall display the current game board state visually, showing the underlying polygon, placed triangulation edges, and highlighting selectable elements.
*   **GUI-2:** The system shall allow a human player to input a move by selecting valid graphical elements (e.g., clicking on two vertices to propose a new edge) in accordance with the current game's rules.
*   **GUI-3:** The system shall update the visual display within 500 milliseconds of a valid move being made.
*   **GUI-4:** The system shall provide a text-based log/panel displaying the sequence of moves made during the current game.

##### 3.2.3 Game Definition & Loading (GDL)
*   **GDL-1:** The system shall include at least three distinct predefined triangulation games from the referenced theoretical article.
*   **GDL-2:** The system shall allow a user to load a new game by selecting an external game definition file via a standard file chooser dialog.
*   **GDL-3:** The system shall parse the game definition file. If the file format is invalid, the system shall display a descriptive error message and not alter the current game state.
*   **GDL-4:** The game definition file shall specify, at minimum: game name, initial board state, legal move generation rules, and win/loss conditions.

##### 3.2.4 Player Management (PM)
*   **PM-1:** The system shall support configuring a game for two players, where each player can be independently set as "Human" or "AI".
*   **PM-2:** For a "Human" player, the system shall accept input via the GUI as specified in **GUI-2**.
*   **PM-3:** For an "AI" player, the system shall request a move from the configured AI agent when it is that player's turn.

##### 3.2.5 Artificial Intelligence (AI)
*   **AI-1:** The system shall include a default "Random-Move" AI agent that selects a valid move uniformly at random from the list of all currently legal moves.
*   **AI-2:** The system shall provide a well-documented Java interface (e.g., `IAgent`) that allows for the integration of custom AI implementations.
*   **AI-3:** **Performance Requirement:** Any AI agent (default or custom), when requested for a move, must return a valid move or resign within **10 seconds** for any game state encountered in the predefined games. A timeout shall be enforced, and the AI shall be considered to have forfeited if it exceeds this limit.

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance Requirements
*   **PER-1:** The GUI shall remain responsive (no freezing) while an AI is computing a move.
*   **PER-2:** The application shall start and be ready for user interaction within 5 seconds on average hardware.
*   **PER-3:** AI move calculation timeout is defined as **10 seconds** (see **AI-3**).

##### 3.3.2 Safety Requirements
Not applicable.

##### 3.3.3 Security Requirements
*   **SEC-1:** The application shall not require elevated system privileges.
*   **SEC-2:** Loading external game definition files shall not execute arbitrary code.

##### 3.3.4 Software Quality Attributes
*   **Maintainability:** The code shall be modular, separating core game logic, GUI, AI interface, and file parsing into distinct components.
*   **Usability:** The interface shall be intuitive for a Player user class. Common actions (making a move, starting a new game) shall be achievable with minimal clicks.
*   **Portability:** The application shall function identically across Windows, macOS, and Linux platforms meeting the JRE requirement.
*   **Reliability:** The application shall not crash due to invalid user input in the GUI. All errors from parsing external files shall be handled gracefully with user-friendly messages.

---

### 4. Appendices

#### 4.1 Appendix A: Game Definition File Format (Preliminary)
The following is a proposed JSON schema for game definition files. This is subject to change during design.

```json
{
  "gameName": "Example Triangulation Game",
  "description": "A game based on Theorem X from the article.",
  "initialState": {
    "polygonVertices": 6,
    "preplacedEdges": [ [0,2], [1,4] ]
  },
  "moveRules": {
    "ruleType": "diagonalAddition",
    "constraints": [ "noCrossing", "noReuse" ]
  },
  "winCondition": {
    "type": "normalPlay", // or "misère"
    "description": "Player who makes the last legal move wins."
  }
}
```

#### 4.2 Appendix B: AI Interface Sketch
```java
/**
 * Interface for AI player agents.
 */
public interface IAgent {
    /**
     * Called by the system to request a move from the AI.
     * @param gameState An object representing the current game state.
     * @param legalMoves A list of all legal moves from the current state.
     * @return A valid move from the legalMoves list, or null to resign.
     */
    Move selectMove(GameState gameState, List<Move> legalMoves);
}
```

---
**End of Document**