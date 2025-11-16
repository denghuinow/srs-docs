# Short Summary

- **Background and objectives**: Triangulation Games is a Java-based application for playing combinatorial triangulation games, designed to support research and entertainment by enabling gameplay against AI or another player.
- **In scope**: Graphical user interface with mouse/keyboard support, multiple predefined triangulation games, ability to load new games from external files, support for human and AI players, and configurable opening positions.
- **Out of scope**: Network multiplayer support, platform-specific dependencies, advanced AI beyond random moves, complex user authentication, and real-time game collaboration features.
- **Roles and core use cases**:  
  - As a Player, I want to select and play triangulation games so that I can enjoy or study them.  
  - As a Game Developer, I want to define new games in external files so that they can be loaded and played without code changes.  
  - As a Researcher, I want to experiment with triangulation game configurations so that I can explore theoretical problems.
- **Success metrics**: Game loads and runs on Java 1.4+ environments, AI responds within 10 seconds per move, and users can successfully define and load new games via external files.
- **Major constraints**: Must use Java and Swing, no platform-specific libraries, must run on systems with Java Runtime Environment 1.4+, and installation must not require external databases.
- **Undecided issues**: Not mentioned.