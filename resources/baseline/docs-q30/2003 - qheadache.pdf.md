```markdown
# Software Requirements Specification (SRS)
## Qheadache Puzzle Game

**Version:** 1.0  
**Date:** [Current Date]  
**Authors:** [Your Name/Team]

---

## Table of Contents
1. [Introduction](#1-introduction)
2. [Overall Description](#2-overall-description)
3. [System Features](#3-system-features)
4. [External Interface Requirements](#4-external-interface-requirements)
5. [Non-Functional Requirements](#5-non-functional-requirements)
6. [Other Requirements](#6-other-requirements)

---

## 1 Introduction

### 1.1 Purpose
This document specifies the requirements for Qheadache, a standalone puzzle-based computer game. It serves as a comprehensive description of all system functionalities, constraints, and interfaces for developers, testers, and stakeholders.

### 1.2 Scope
Qheadache is a single-player puzzle application that provides:
- Core puzzle gameplay with block movement mechanics
- Game state management (save/load functionality)
- Player performance tracking and statistics
- Local score recording system

**Out of Scope:**
- Network communication or multiplayer capabilities
- Integration with external systems
- Advanced analytics beyond basic scoring
- User account management or permission tiers

### 1.3 Definitions, Acronyms, and Abbreviations
- **Qt**: Cross-platform application framework used for GUI development
- **SRS**: Software Requirements Specification
- **GUI**: Graphical User Interface
- **Win Condition**: Game completion state achieved by positioning the large square block correctly

### 1.4 References
- Qt Framework Documentation
- Standard SRS template (IEEE 830)

## 2 Overall Description

### 2.1 Product Perspective
Qheadache is a self-contained desktop application with the following architecture:
```
┌─────────────────┐
│   Qheadache    │
│   Application  │
└────────┬────────┘
         │
┌────────▼────────┐
│   Qt Library    │
└────────┬────────┘
         │
┌────────▼────────┐
│  Operating     │
│   System       │
└─────────────────┘
```

### 2.2 Product Functions
- **Game Management**: Core puzzle mechanics and gameplay
- **State Tracking**: Real-time monitoring of moves and duration
- **Statistics Handling**: Score recording and top 10 leaderboard
- **File Operations**: Save/load game progress and statistics

### 2.3 User Characteristics
- **Primary Users**: Casual players aged 8+
- **Technical Skill**: No specialized training required
- **Usage Frequency**: Occasional, recreational use
- **Access Requirements**: Single user per machine installation

### 2.4 Operating Environment
- **Supported Platforms**: All Qt-supported operating systems (Windows, macOS, Linux)
- **Display Requirements**: Minimum 800×600 resolution
- **Dependencies**: Qt library installation
- **Input Methods**: Keyboard, mouse, or alternative pointing devices

### 2.5 Design and Implementation Constraints
- Must use Qt library for all graphical operations
- Statistics file limited to exactly 10 player records
- No network connectivity requirements
- Single-user operation only

### 2.6 Assumptions and Dependencies
**Assumptions:**
- Users have basic computer literacy
- Qt runtime libraries are available on target systems
- Display meets minimum resolution requirements

**Dependencies:**
- Qt framework availability
- Compatible operating system
- Adequate system resources for Qt applications

## 3 System Features

### 3.1 Game Play Management

#### 3.1.1 Description
Core puzzle gameplay featuring block movement mechanics with the objective of positioning a large square block to a specific location.

#### 3.1.2 Functional Requirements
- **FR-001**: The system shall allow players to move puzzle blocks using keyboard or mouse input
- **FR-002**: The system shall detect when the large square block reaches the win position
- **FR-003**: The system shall provide visual feedback for valid and invalid moves
- **FR-004**: The system shall initialize the game board to a consistent starting state

### 3.2 Undo/Redo System

#### 3.2.1 Description
Players can reverse or reapply their moves with support for up to 1,000 consecutive actions.

#### 3.2.2 Functional Requirements
- **FR-005**: The system shall support undo functionality for the last 1,000 moves
- **FR-006**: The system shall support redo functionality for previously undone moves
- **FR-007**: The system shall maintain move history state during game session
- **FR-008**: The system shall update the game display immediately after undo/redo operations

### 3.3 Game Statistics Tracking

#### 3.3.1 Description
Real-time tracking and display of game performance metrics including move count and play duration.

#### 3.3.2 Functional Requirements
- **FR-009**: The system shall track and display elapsed play time in real-time
- **FR-010**: The system shall count and display total moves made
- **FR-011**: The system shall record final score (moves + time) upon game completion
- **FR-012**: The system shall reset statistics when starting a new game

### 3.4 Scoring System

#### 3.4.1 Description
Recording and management of player scores based on move efficiency and completion time.

#### 3.4.2 Functional Requirements
- **FR-013**: The system shall calculate final score using move count and completion time
- **FR-014**: The system shall prompt for player name upon game completion
- **FR-015**: The system shall store player scores in persistent storage
- **FR-016**: The system shall associate scores with player identifiers

### 3.5 Statistics Display

#### 3.5.1 Description
Presentation of top 10 player scores in a dedicated statistics window.

#### 3.5.2 Functional Requirements
- **FR-017**: The system shall display the top 10 player scores in ranked order
- **FR-018**: The system shall update statistics display when new scores are recorded
- **FR-019**: The system shall provide navigation to statistics from main interface
- **FR-020**: The system shall format statistics for clear readability

### 3.6 Save/Load Functionality

#### 3.6.1 Description
Persistent storage and retrieval of game progress and player statistics.

#### 3.6.2 Functional Requirements
- **FR-021**: The system shall save current game state to file
- **FR-022**: The system shall load previously saved game state from file
- **FR-023**: The system shall maintain statistics file with exactly 10 records
- **FR-024**: The system shall handle file I/O errors gracefully

## 4 External Interface Requirements

### 4.1 User Interfaces
- **Main Game Window**: Puzzle board display with game controls
- **Statistics Window**: Top 10 scores display with player names
- **Menu System**: File operations (save/load) and navigation
- **Input Methods**: Keyboard shortcuts and mouse interactions

### 4.2 Hardware Interfaces
- **Input**: Standard keyboard and mouse/trackpad
- **Display**: Minimum 800×600 resolution support
- **Storage**: Local file system access for save files

### 4.3 Software Interfaces
- **Qt Framework**: GUI rendering, event handling, and cross-platform compatibility
- **Operating System**: Standard file I/O operations
- **No external APIs or web services required**

### 4.4 Communication Interfaces
- **None** - No network communication requirements

## 5 Non-Functional Requirements

### 5.1 Performance Requirements
- **Response Time**: Game actions (moves, undo/redo) shall respond within 100ms
- **Startup Time**: Application shall initialize within 3 seconds
- **File Operations**: Save/load operations shall complete within 2 seconds

### 5.2 Reliability Requirements
- **Availability**: 99% uptime during active sessions
- **Data Integrity**: No corruption of save files or statistics
- **Error Recovery**: Graceful handling of invalid operations

### 5.3 Usability Requirements
- **Learnability**: New users shall understand basic controls within 5 minutes
- **Accessibility**: Support for alternative pointing devices
- **Interface Clarity**: All game elements clearly visible at 800×600 resolution

### 5.4 Supportability Requirements
- **Platform Compatibility**: Consistent behavior across all Qt-supported OS
- **Maintainability**: Modular code structure for future enhancements
- **Documentation**: Clear code comments and user instructions

### 5.5 Design Constraints
- **Statistics Limit**: Exactly 10 records maintained in statistics file
- **Move History**: Maximum 1,000 moves in undo/redo buffer
- **Single User**: No concurrent multi-user support

## 6 Other Requirements

### 6.1 Priority Classification
**Critical (Must Have):**
- Core game mechanics (movement, win condition)
- Basic scoring system
- Statistics tracking

**Important (Should Have):**
- Undo/redo functionality
- Statistics display
- Save/load operations

**Secondary (Nice to Have):**
- Enhanced visual effects
- Additional puzzle variations
- Extended statistics

### 6.2 Acceptance Criteria
1. **Game Completion Test**: User can complete puzzle and trigger win condition
2. **Statistics Validation**: Scores properly recorded and displayed in top 10
3. **Undo/Redo Test**: 1,000 move history maintained and functional
4. **Cross-Platform Test**: Consistent operation on all supported Qt platforms
5. **File Operations Test**: Successful save/load of game state and statistics

### 6.3 Appendices
#### 6.3.1 Sample Statistics File Format
```json
{
  "top_scores": [
    {"player": "Player1", "score": 150, "moves": 45, "time": 105},
    {"player": "Player2", "score": 180, "moves": 52, "time": 128},
    ...
  ]
}
```

#### 6.3.2 Minimum System Requirements
- **RAM**: 512MB
- **Storage**: 50MB free space
- **Display**: 800×600 resolution
- **OS**: Any Qt-supported platform

---

**Document Approval**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Manager | | | |
| Lead Developer | | | |
| Quality Assurance | | | |
```