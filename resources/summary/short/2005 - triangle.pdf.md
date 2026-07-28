# Short Summary: Triangulation Games Software Requirements

## Background and Objectives
Triangulation Games is a Java-based application enabling users to play various combinatorial triangulation games (solitaire, vs. computer, or two-player) based on academic research. It also serves as a platform for defining new game types without modifying core code.

## In Scope
- Graphical user interface supporting mouse and keyboard input.
- Support for multiple pre-defined triangulation games (constructing, transforming, marking) with selectable opening positions.
- Ability to play against a human, computer AI (including a default random AI), or mix player types during a game.
- External definition of new games via files (e.g., XML) separate from source code.
- Game saving/loading functionality and in-game help.

## Out of Scope
- Network or multiplayer connectivity over a network.
- Advanced AI beyond a basic random move generator as a default.
- Platform-specific dependencies or libraries.
- Complex user authentication or personal data storage.
- Real-time performance optimization for highly complex AI calculations.

## Stakeholders and Core Use Cases
**Stakeholders:**
- **Researchers:** Provide theoretical foundation and seek new research problems; value scientific consistency.
- **Basic Users/Players:** Seek entertainment and relaxation; require ease of use and low-end hardware compatibility.
- **Game Developers:** Create and test new triangulation games; need clear documentation and easy development processes.
- **Development Team:** Build a functional application; focus on learning software project management and using a suitable development environment.

**Core User Stories:**
1. As a player, I want to start a new game from a menu so that I can choose between different triangulation game types.
2. As a player, I want to select an opening position (or random) so that I can begin the game with a preferred configuration.
3. As a player, I want to assign human or AI players at game start so that I can play solo, vs. computer, or with another person.
4. As a player, I want to change a player to AI mid-game so that I can continue if a human player leaves.
5. As a game developer, I want to define a new game in an external file so that it can be loaded and played without code changes.
6. As a player, I want to save and load game states so that I can resume play later.

## Success Metrics
- The application runs on standard hardware (450+ MHz) with Java 1.4+ and responds to AI moves within 10 seconds.
- Users can successfully define and load new games via external files without programming knowledge.
- The interface is usable with both mouse and keyboard on Windows and Linux.

## Major Constraints
- Must be implemented in Java for cross-platform compatibility (Windows, Linux, Mac).
- Cannot rely on platform-specific libraries or external databases.
- Default AI must support all two-player games with random move selection.
- Games must end based on predefined conditions specified in external definitions.
- Released under GPL license.

## Undecided Issues
- Priority and implementation details for low-priority features (e.g., loading custom AI from files).
- Specific file format and structure for external game definitions (e.g., XML vs. text).
- Detailed usability guidelines for the graphical interface beyond basic input methods.
- Exact set of opening positions for each game category beyond the basic ones referenced.
- Scope of the in-game help content and maintenance manual details.