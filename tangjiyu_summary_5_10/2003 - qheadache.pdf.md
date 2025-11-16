# Qheadache Version 1.0 Software Requirements Specification

## 1. Introduction

### 1.1 Purpose
This document establishes requirements for the Qheadache product. The intended audience includes analysts, programmers, and testers of Qheadache.

### 1.2 Scope
The product is a computerized game that displays an interface used to solve a specific headache (puzzle). It runs as a standalone application using menus, graphics, and sounds.

### 1.3 Definitions, Acronyms, and Abbreviations
Not applicable.

### 1.4 References
Not applicable.

### 1.5 SRS Document Overview
This document provides a general description including user characteristics, hardware requirements, functional and data requirements. It contains general description in section 2 and specific requirements in section 3.

## 2. General Description

### 2.1 Product Perspective

#### 2.1.1 User Interfaces
The product runs as a standalone application with user interface using menus, graphics, and sounds.

#### 2.1.2 Hardware Interfaces
Requires keyboard and mouse for user interface. Requires graphical display with minimum resolution of 800*600.

#### 2.1.3 Software Interfaces
Uses Qt graphical library and must run with all operating systems that Qt supports.

#### 2.1.4 Communications Interfaces
Not applicable.

#### 2.1.5 Memory Constraints
Not applicable.

#### 2.1.6 Site Adaptation Requirements
Not applicable.

### 2.2 Product Functions

#### 2.2.1 Undo and Redo Actions
User must undo and redo last thousand actions.

#### 2.2.2 Time Passed to Play
Product must count and display time that user uses to play.

#### 2.2.3 Count of Action Number
Product must count and display number of user's actions.

#### 2.2.4 Score
Product must record score (time and number of counts) of a play associated with name of user.

#### 2.2.5 Score Window
Product must display window with all player's scores.

### 2.3 User Characteristics
No qualification necessary. Users range from age 8 beginners to advanced adult players.

### 2.4 Start Up Requirements
Not applicable.

### 2.5 Apportioning of Requirements
Not applicable.

## 3. Specific Requirements

### 3.1 External Interfaces
Requires mouse and keyboard for input. Hardware and operating system must provide 800x600 screen resolution. Sound not required to play game.

### 3.2 Functional Requirements

#### 3.2.1 Actions

##### 3.2.1.1 Presentation of the Board
Board is rectangular zone (height 5x, width 4x) where user moves blocks. Block unit x: 50-100 pixels. Blocks separated by margin of 0.1x.
- Four square blocks (side x)
- Four rectangular blocks (height 2x, width x)
- One rectangular block (height x, width 2x)
- One square block (side 2x)
Board is black, blocks are yellow.

##### 3.2.1.2 Block Selection
Left-click down on block changes game state to "Block movement".

##### 3.2.1.3 Block Deselection
Left-click up on selected block changes game state to "Block selection".

##### 3.2.1.4 Block Movement
Selected block follows mouse movement without overlapping other blocks or exiting game zone. Minimum distance of 0.05x from other blocks.

##### 3.2.1.5 Undo Action
User can cancel movement via menu selection. Displays block positions before last movement. Unavailable if no previous movement.

##### 3.2.1.6 Redo Action
User can redo canceled movement via menu selection. Displays block positions before last movement was canceled. Unavailable if previous action wasn't "undo".

#### 3.2.2 End of Game Management

##### 3.2.2.1 End of Game
Game ends when great square (2x block) is moved to bottom of board. All player statistics are frozen.

##### 3.2.2.2 Finish Window with Statistics
Displayed if player's block movements are fewer than highest recorded. Contains text "You win! Enter your name:", Edit Box (20 characters), and "OK" pushbutton. Player statistics recorded according to section 3.2.3.2.

##### 3.2.2.3 Simple Finish Window
Displayed if player's block movements are not fewer than highest recorded. Contains text "You win!" and "OK" pushbutton.

#### 3.2.3 Statistics Management

##### 3.2.3.1 Player Statistics Management
Records: number of block movements since start, time since start.

##### 3.2.3.2 Game Statistics Management
Game statistics composed of 10 player statistics. When new record is achieved, if 10 records already exist, player statistic with greatest number of block movements is erased.

##### 3.2.3.3 Statistics Erasing
User can erase all statistics via menu selection.

##### 3.2.3.4 Statistic Window
Player Statistics Window contains listbox of 10 lines. Each line shows player name, number of block movements, and time used to solve puzzle. Statistics read from game statistic file.

#### 3.2.4 File Management

##### 3.2.4.1 Open Game
User can open previously saved game via menu selection. Dialog box allows choosing file containing game data. Board is redrawn according to file data.

##### 3.2.4.2 Save Game
User can save current game via menu selection. If never saved, functions as "Save as...". Otherwise saves to previous file: current block positions, last 10000 previous positions, number of previous movements, and time passed.

##### 3.2.4.3 Save Game As
User can save current game to new file via menu selection. Dialog box allows choosing file. Saves current block positions, previous positions, number of previous movements, and time passed.

##### 3.2.4.4 Exit
User can stop game via menu selection. If game not saved, dialog asks if player wants to save. Options: "Yes" (performs Save action) or "No" (exits directly).

#### 3.2.5 Menu Bar

##### 3.2.5.1 Game Menu
Contains "Open game...", "Save Game...", "Save Game As...", and "Exit" in that order. Performs associated actions.

##### 3.2.5.2 Action Menu
Contains "Undo" and "Redo" in that order. Menu selection unavailable if associated action is unavailable.

##### 3.2.5.3 Statistics Menu
Contains "Display" and "Erase" in that order. "Display" shows statistic window. "Erase" erases statistics.

##### 3.2.5.4 Help Menu
Contains "About". Displays "About Window" with text "Qheadache 1.0 by Jean-Philippe Brossat jp_brossat@yahoo.fr".

### 3.3 Performance Requirements
Only one user per machine.

### 3.4 Software System Attributes
Software must be portable to Windows OS.
