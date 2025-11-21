# Software Requirements Specification (SRS)
## MultiMahjong Game System

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
This document specifies the requirements for the MultiMahjong game system, a client-server based Mahjong game supporting both single-player and multiplayer modes. The intended audience includes project stakeholders, developers, testers, and technical writers.

### 1.2 Project Scope
MultiMahjong is a networked Mahjong game implementation that enables players to participate in Chinese Mahjong games either against computer-controlled opponents or with other human players over TCP/IP networks. The system consists of two main components: MultiMahjongClient and MultiMahjongServer.

### 1.3 Definitions, Acronyms, and Abbreviations
- **MVP**: Minimum Viable Product
- **TCP/IP**: Transmission Control Protocol/Internet Protocol
- **JDK**: Java Development Kit
- **Chow**: A move that collects three consecutive tiles of the same suit
- **Pung**: A move that collects three identical tiles
- **Kong**: A move that collects four identical tiles
- **Mahjong**: The winning move that completes a valid hand

### 1.4 References
- JDK 1.2 Documentation
- Chinese Mahjong Official Rules
- Windows, Mac OS 8, and Solaris System Specifications

## 2 Overall Description

### 2.1 Product Perspective
The MultiMahjong system follows a client-server architecture where the server facilitates communication between clients and manages game sessions. The system operates as a standalone application independent of other systems.

### 2.2 Product Functions
- Single-player mode against computer opponents
- Multiplayer mode with human players over network
- Game session management (create/join games)
- Player customization (names, icons)
- Chinese Mahjong rule enforcement
- Real-time game state synchronization

### 2.3 User Characteristics
- **Casual Gamers**: Users familiar with basic Mahjong rules
- **Network Players**: Users with basic network connectivity knowledge
- **Single Players**: Users preferring solo gameplay against AI opponents

### 2.4 Constraints
- **Technical**: Must use JDK 1.2 exclusively
- **Platform**: Must run on Windows, Mac OS 8, and Solaris
- **Performance**: Computer opponents must respond within 60 seconds
- **Scalability**: Server must support 10 simultaneous games (40 players total)

### 2.5 Assumptions and Dependencies
- Target systems have Java Runtime Environment compatible with JDK 1.2
- Network connectivity available for multiplayer mode
- Sufficient system resources for graphical display and network communication

## 3 System Features

### 3.1 Game Client (MultiMahjongClient)

#### 3.1.1 Single-Player Mode
**Description:** The client shall provide a single-player experience against three computer-controlled opponents.

**Requirements:**
- MM-CLIENT-001: The system shall initialize a game with one human player and three computer opponents
- MM-CLIENT-002: The system shall display the game board with all player hands visible to the human player
- MM-CLIENT-003: Computer opponents shall make moves according to Chinese Mahjong rules
- MM-CLIENT-004: The system shall enforce turn order and game rules consistently

#### 3.1.2 Multiplayer Mode
**Description:** The client shall connect to the server for multiplayer games with human and/or computer players.

**Requirements:**
- MM-CLIENT-005: The system shall establish TCP/IP connection to MultiMahjongServer
- MM-CLIENT-006: The system shall display available game sessions for joining
- MM-CLIENT-007: The system shall support mixed games with human and computer players
- MM-CLIENT-008: The system shall synchronize game state with server in real-time

#### 3.1.3 Player Customization
**Description:** Players shall be able to personalize their gaming experience.

**Requirements:**
- MM-CLIENT-009: The system shall allow players to set their display name
- MM-CLIENT-010: The system shall provide selectable player icons
- MM-CLIENT-011: The system shall allow specification of score limits for games

### 3.2 Game Server (MultiMahjongServer)

#### 3.2.1 Network Communication
**Description:** The server shall manage all network communications between clients.

**Requirements:**
- MM-SERVER-001: The system shall listen for incoming TCP/IP connections on a configurable port
- MM-SERVER-002: The system shall relay game data between connected clients
- MM-SERVER-003: The system shall handle client disconnections gracefully
- MM-SERVER-004: The system shall support up to 40 simultaneous player connections

#### 3.2.2 Game Session Management
**Description:** The server shall create, maintain, and terminate game sessions.

**Requirements:**
- MM-SERVER-005: The system shall support creation of new game sessions
- MM-SERVER-006: The system shall allow players to join existing game sessions
- MM-SERVER-007: The system shall manage up to 10 simultaneous game sessions
- MM-SERVER-008: The system shall enforce game rules across all sessions

### 3.3 Game Logic

#### 3.3.1 Chinese Mahjong Rules Implementation
**Description:** The system shall implement standard Chinese Mahjong rules.

**Requirements:**
- MM-GAME-001: The system shall implement tile drawing and discarding mechanics
- MM-GAME-002: The system shall support Chow moves (three consecutive tiles of same suit)
- MM-GAME-003: The system shall support Pung moves (three identical tiles)
- MM-GAME-004: The system shall support Kong moves (four identical tiles)
- MM-GAME-005: The system shall detect Mahjong (winning) conditions
- MM-GAME-006: The system shall calculate scores according to Chinese Mahjong rules

#### 3.3.2 Computer Opponent AI
**Description:** The system shall provide competent computer-controlled opponents.

**Requirements:**
- MM-AI-001: Computer opponents shall make valid moves according to game rules
- MM-AI-002: Computer opponents shall respond within 60 seconds for any move
- MM-AI-003: Computer opponents shall demonstrate basic strategic gameplay
- MM-AI-004: Computer opponents shall announce moves appropriately (Chow, Pung, Kong, Mahjong)

## 4 External Interface Requirements

### 4.1 User Interfaces
- Graphical user interface for game board display
- Player customization screens for names and icons
- Game lobby interface for session management
- Score display and game statistics

### 4.2 Hardware Interfaces
- Standard input devices (keyboard, mouse)
- Network interface card for TCP/IP communication
- Display supporting 800x600 resolution minimum

### 4.3 Software Interfaces
- **Operating Systems**: Windows, Mac OS 8, Solaris
- **Java Platform**: JDK 1.2
- **Network Protocol**: TCP/IP

### 4.4 Communication Interfaces
- TCP/IP sockets for client-server communication
- Custom application-level protocol for game data exchange
- Heartbeat mechanism for connection monitoring

## 5 Non-Functional Requirements

### 5.1 Performance Requirements
- MM-PERF-001: Computer opponents shall respond within 60 seconds
- MM-PERF-002: Server shall handle 10 simultaneous games (40 players)
- MM-PERF-003: Network latency shall not exceed 2 seconds for game state updates
- MM-PERF-004: Client application shall initialize within 10 seconds

### 5.2 Reliability Requirements
- MM-REL-001: System shall maintain game state consistency across disconnections
- MM-REL-002: Server shall achieve 99% uptime during operational hours
- MM-REL-003: Game data shall not be lost due to network failures

### 5.3 Portability Requirements
- MM-PORT-001: Application shall run identically on Windows, Mac OS 8, and Solaris
- MM-PORT-002: No platform-specific code dependencies allowed

### 5.4 Security Requirements
- MM-SEC-001: System shall prevent unauthorized game session access
- MM-SEC-002: Network communication shall be resistant to basic eavesdropping

## 6 Other Requirements

### 6.1 Development Constraints
- MM-CONST-001: Must be implemented using JDK 1.2 only
- MM-CONST-002: No external libraries beyond JDK 1.2 standard library
- MM-CONST-003: Source code must be compatible with specified target platforms

### 6.2 Legal and Compliance Requirements
- Game rules must comply with standard Chinese Mahjong regulations
- All intellectual property must be properly licensed or original

### 6.3 Documentation Requirements
- User manual covering game rules and interface operation
- Technical documentation for system administrators
- API documentation for potential future extensions

---

## Appendix A: Game Rules Summary

### Chinese Mahjong Basics
- 136 tiles consisting of three suits (Bamboo, Characters, Dots) and honor tiles
- Four players per game
- Objective: Complete a winning hand of 14 tiles (4 sets and 1 pair)
- Valid moves: Chow, Pung, Kong, Mahjong
- Scoring based on hand composition and winning method

### Supported Moves
1. **Chow**: Three consecutive tiles of the same suit
2. **Pung**: Three identical tiles
3. **Kong**: Four identical tiles
4. **Mahjong**: Completing a valid winning hand

---

**Document Approval**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Manager | | | |
| Lead Developer | | | |
| Quality Assurance | | | |