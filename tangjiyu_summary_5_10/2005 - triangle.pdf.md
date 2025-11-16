# Triangulation Games - Software Requirements Specification

## 1. Introduction
This document describes the requirements for the Triangulation Games software, an application that enables playing various combinatorial games as solitaire, against computer AI, or with another player. The system also functions as a platform for defining new types of triangulation games.

## 2. Overall Description

### 2.1 Product Perspective
Triangular Games is a standalone software application based on the article "Games on Triangulations" [1], implementing games described in this research.

### 2.2 Product Features
The software supports multiple triangulation games that can be played solo or against another person. It features a graphical user interface primarily controlled by mouse but also keyboard-compatible. By default, the system implements three games: constructing, transforming, and marking. New games can be added without modifying the original application code and will be automatically selectable through the GUI.

### 2.3 User Classes and Characteristics
- **Players**: Main user class with academic backgrounds in mathematics, social sciences, and computer sciences. The interface is designed for users with varying technical experience levels.
- **Game Developers**: Users with experience in playing games and scientific background for creating new games. This class focuses on ease of defining new games.

### 2.4 Operating Environment
Implemented using Java platform for cross-platform compatibility. Requires:
- Mouse or keyboard
- Graphical user environment (X Window, Windows, Mac, etc.)
- Java Runtime Environment (version 1.4 or later)

### 2.5 Design and Implementation Constraints
- Must use Java environment as requested by client
- Cannot depend on platform-specific libraries
- Must run on any computer with Java 2 (version 1.4 or later) Runtime Environment
- Easy installation without external databases

### 2.6 User Documentation
Two end-user documentations will be provided:
- User manual describing system usage for playing
- Maintenance manual describing game specification, containing design documents, interfaces, source code, and plugin implementation guidance

### 2.7 Assumptions and Dependencies
Software will be released under GPL-license.

## 3. System Features

### 3.1 Graphical User Interface
**Priority**: Essential

**Functional Requirements**:
- GUI: System uses graphical user interface to display data to user
- GUI.keyboardInput: System can be used fully with keyboard
- GUI.mouseInput: System can be used fully with mouse

### 3.2 Multiple Game Types
**Priority**: High

**Supported Games**:
1. Constructing (a Triangulation)
   - Monochromatic complete triangulation (Priority 1)
   - Bichromatic complete triangulation (Priority 2)
   - Monochromatic triangle (Priority 3)
   - Bichromatic triangle (Priority 3)
2. Transforming (a Triangulation)
   - Monochromatic flipping (Priority 1)
   - All-green solitaire (monochromatic) (Priority 2)
   - Monochromatic flipping to triangle (Priority 3)
   - Bichromatic flipping (Priority 3)
   - Green wins solitaire (Priority 3)
3. Marking (a Triangulation)
   - Triangulation coloring game (monochromatic) (Priority 1)
   - Bichromatic coloring game (Priority 2)
   - Four-cycle game (monochromatic) (Priority 4)
   - Nimstring game (monochromatic) (Priority 4)

**Functional Requirements**:
- Game.Multiple: System supports multiple games and can load additional games from external source

### 3.3 Multiple Opening Positions
**Priority**: High

**Functional Requirements**:
- Game.MultipleOpeningPositions: System supports multiple opening positions applicable to all games

### 3.4 Human or Computer Players
**Priority**: Medium

**Functional Requirements**:
- Game.TwoPlayerSupport: System supports two player turn-based gaming

### 3.5 Default Random Artificial Intelligence
**Priority**: High

**Functional Requirements**:
- AI: System has artificial intelligence supporting every two-player game
- Game.TwoPlayerSupport: System supports two player turn-based gaming

### 3.6 Change Player Nature During Game
**Priority**: Medium

**Functional Requirements**:
- Game.ChangePlayer: System has embedded AI that takes over from player when requested

### 3.7 Load New Artificial Intelligence from File
**Priority**: Low

**Functional Requirements**:
- Game.LoadAI: System has files containing AI implementations that can be loaded
- Game.AIInterface: System prompts user about implementing new AIs

### 3.8 Games Defined Separately from Code
**Priority**: High (Essential)

**Functional Requirements**:
- Game.Defined: System supports defining new games without modifying source code
- Game.AutomaticSearch: System searches external source for games on startup and loads them

### 3.9 Predefined Game Ending Conditions
**Priority**: High

**Functional Requirements**:
- Game.End: All games end on predefined condition

### 3.10 Game Saving Feature
**Priority**: Low

**Functional Requirements**:
- Game.Save: System saves game in file
- Game.Load: System loads game from file

### 3.11 In-Game Help Function
**Priority**: Medium

**Functional Requirements**:
- Game.Help: System has embedded help file with basic solutions and hints

## 4. External Interface Requirements

### 4.1 User Interfaces
- UI-1: All user interfaces designed following common usability guidelines
- UI-2: Interface uses one main window for gameplay and dialog windows for settings

### 4.2 Hardware Interfaces
- HI-1: System functions on computer with screen output and keyboard/mouse input

### 4.3 Software Interfaces
- SI-1: Requires working Java environment and GUI supported by Java Swing library

## 5. Nonfunctional Requirements

### 5.1 Performance Requirements
- PR-1: System executes without problems on machines meeting Java runtime requirements
- PR-2: Basic AI operates fast enough with next move calculated within 10 seconds

### 5.2 Safety Requirements
- No network connections or security requirements
- File overwriting requires user confirmation to prevent data loss

### 5.3 Security Requirements
- No personal information stored, no specific security requirements

### 5.4 Software Quality Attributes
- SQA-1: System runs well on both Linux and Windows, playable with mouse, keyboard, or both

## 6. Stakeholders
- **Researchers**: Value research applications and theoretical problem solving
- **Basic Users/Players**: Seek entertainment and interesting game problems with easy-to-use interface
- **Game Developers**: Need platform for testing new triangular games with easy development methods
- **Development Team**: Focus on learning software project issues with easy-to-use development environment

## 7. Requirements State

### 7.1 Stable Requirements
All requirements with medium or high priority are stable and will not change.

### 7.2 Volatile Requirements
Low priority requirements may change during development if implementation proves wasteful.
