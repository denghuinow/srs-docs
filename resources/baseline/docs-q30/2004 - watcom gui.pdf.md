# Software Requirements Specification (SRS)
## Open Watcom GUI Library Linux Port

**Version:** 1.0  
**Date:** [Current Date]  
**Status:** Draft

---

## Table of Contents
1. [Introduction](#1-introduction)
2. [Overall Description](#2-overall-description)
3. [System Features](#3-system-features)
4. [External Interface Requirements](#4-external-interface-requirements)
5. [Non-Functional Requirements](#5-non-functional-requirements)
6. [Constraints, Assumptions & Dependencies](#6-constraints-assumptions--dependencies)
7. [Acceptance Criteria](#7-acceptance-criteria)

---

## 1 Introduction

### 1.1 Purpose
This document specifies the requirements for porting Open Watcom's Windows GUI library to Linux using the GTK toolkit. The primary purpose is to enable cross-platform GUI compatibility for the Open Watcom Integrated Development Environment (IDE) on Linux systems.

### 1.2 Scope
The scope of this project includes:
- Creating a Linux-compatible GUI library that mimics Windows API behavior
- Integration with GTK 2.0+ as the underlying UI toolkit
- Replacement of Windows/OS2 API dependencies with GTK equivalents
- Maintenance of existing Open Watcom application logic without modification

**Out of Scope:**
- Windows-style resource file support
- MDI (Multiple Document Interface) "windows in window" model
- Built-in help subsystem implementation
- Windows API emulation beyond GUI components

### 1.3 Definitions and Acronyms

| Term | Definition |
|------|------------|
| GTK | GIMP Toolkit, a cross-platform widget toolkit |
| MDI | Multiple Document Interface |
| IDE | Integrated Development Environment |
| X Window System | Window system for bitmap displays |
| libglade | Library for loading GLADE interface files |

## 2 Overall Description

### 2.1 Product Perspective
This library serves as the foundational component for the Open Watcom IDE's Linux port, acting as a compatibility layer between the existing Windows-oriented application code and the Linux graphical environment.

### 2.2 Product Functions
- Window initialization and management
- Dialog creation and control handling
- Menu and toolbar management
- Text and font rendering
- Status bar implementation
- Scrolling functionality

### 2.3 User Characteristics
**Primary Users:** Open Watcom developers porting the IDE to Linux
- **Technical Expertise:** Advanced
- **Permissions:** Full access to porting tools and development environment
- **Experience:** Familiar with Open Watcom codebase and Linux development

### 2.4 Operating Environment
- **Target OS:** Linux distributions
- **UI Toolkit:** GTK 2.0+
- **Window System:** X Window System
- **Dependencies:** GTK development libraries, X11 development libraries

### 2.5 Design and Implementation Constraints
- Must maintain API compatibility with existing Open Watcom Windows GUI calls
- Cannot modify existing application business logic
- Must use GTK as the primary UI toolkit
- No support for Windows MDI model due to GTK limitations

## 3 System Features

### 3.1 Window Management
#### 3.1.1 Description
Provides window creation, destruction, and management functionality equivalent to Windows API.

#### 3.1.2 Requirements
- **WIN-001:** Create and initialize main application windows
- **WIN-002:** Handle window resize, minimize, maximize operations
- **WIN-003:** Manage window focus and z-order
- **WIN-004:** Implement window message processing loop
- **WIN-005:** Support modal and modeless window operations

### 3.2 Dialog Management
#### 3.2.1 Description
Handles creation and management of dialog boxes and controls.

#### 3.2.2 Requirements
- **DLG-001:** Create dialog boxes from programmatic definitions
- **DLG-002:** Manage standard controls (buttons, labels, text fields)
- **DLG-003:** Handle dialog message processing
- **DLG-004:** Support modal dialog execution
- **DLG-005:** Implement control positioning and layout

### 3.3 Menu and Toolbar System
#### 3.3.1 Description
Provides menu creation, management, and toolbar functionality.

#### 3.3.2 Requirements
- **MENU-001:** Create and manage application menus
- **MENU-002:** Handle menu item selection events
- **MENU-003:** Support nested menu structures
- **MENU-004:** Implement toolbar creation and button management
- **MENU-005:** Manage menu/toolbar state (enabled/disabled, checked)

### 3.4 Text and Font Rendering
#### 3.4.1 Description
Handles text display and font management across GUI elements.

#### 3.4.2 Requirements
- **TEXT-001:** Render text in windows and controls
- **TEXT-002:** Manage font selection and properties
- **TEXT-003:** Handle text measurement and layout
- **TEXT-004:** Support basic text formatting
- **TEXT-005:** Implement text drawing in various contexts

### 3.5 Status Bar and Scrolling
#### 3.5.1 Description
Implements status bar display and scrolling functionality.

#### 3.5.2 Requirements
- **STAT-001:** Create and manage status bar panels
- **STAT-002:** Update status bar text dynamically
- **STAT-003:** Implement scrollable window regions
- **STAT-004:** Handle scrollbar events and positioning
- **STAT-005:** Manage viewport adjustments during scrolling

## 4 External Interface Requirements

### 4.1 User Interfaces
- **Primary Interface:** GTK 2.0+ widget toolkit
- **Window System:** X Window System
- **Input:** Standard X11 input handling (keyboard, mouse)

### 4.2 Hardware Interfaces
- **Display:** X Window System compatible display
- **Input Devices:** Standard keyboard and mouse via X11

### 4.3 Software Interfaces
- **GTK 2.0+:** Primary UI toolkit dependency
- **Xlib/X11:** Low-level window system interface
- **libglade:** Optional interface for resource loading (partial solution)

### 4.4 Communication Interfaces
- **Inter-process Communication:** Standard X11 IPC mechanisms
- **Signal Handling:** POSIX signal handling for clean shutdown

## 5 Non-Functional Requirements

### 5.1 Performance Requirements
- Window creation time: < 100ms for standard windows
- Event processing latency: < 50ms for user input events
- Memory usage: Comparable to native GTK applications

### 5.2 Reliability Requirements
- **Availability:** 99.9% during normal operation
- **Mean Time Between Failures (MTBF):** > 720 hours
- **Error Recovery:** Graceful degradation on unsupported features

### 5.3 Compatibility Requirements
- Must maintain visual and behavioral consistency with Windows version
- Must support all GTK 2.0+ compatible Linux distributions
- Must not require modifications to existing Open Watcom application code

### 5.4 Portability Requirements
- **Target Platform:** Linux with X Window System
- **Architecture:** x86 and x86_64 architectures
- **Distribution:** Compatible with major Linux distributions (Red Hat, Debian, Ubuntu variants)

## 6 Constraints, Assumptions & Dependencies

### 6.1 Technical Constraints
- **HARD-CONSTRAINT-001:** No MDI "windows in window" support (GTK limitation)
- **HARD-CONSTRAINT-002:** No direct Windows resource file support
- **HARD-CONSTRAINT-003:** Must use GTK 2.0+ as UI toolkit

### 6.2 Dependencies
- **DEP-001:** GTK 2.0+ development libraries
- **DEP-002:** X Window System and development libraries
- **DEP-003:** Standard C library (glibc)
- **DEP-004:** Optional: libglade for resource conversion

### 6.3 Assumptions
- **ASSUMPTION-001:** Resource file conversion via libglade is acceptable for non-string resources
- **ASSUMPTION-002:** Developers will handle string resource externalization
- **ASSUMPTION-003:** No Windows-specific functionality beyond basic GUI required

## 7 Acceptance Criteria

### 7.1 Testing Approach
- **Primary Test:** GUI sample test (samp2.c) must execute successfully
- **Coverage Verification:** Automated testing of all critical functions
- **Platform Testing:** Verification on multiple Linux distributions

### 7.2 Priority-Based Acceptance

#### 7.2.1 Critical Priority (100% Coverage Required)
- Window creation and destruction
- Dialog box functionality
- Basic control handling (buttons, labels, text fields)
- Event processing loop
```c
// Example: Critical function test coverage
REQUIRE( CreateWindow() == SUCCESS );
REQUIRE( CreateDialog() == SUCCESS );
REQUIRE( ProcessMessages() == SUCCESS );
```

#### 7.2.2 High Priority (95% Coverage Required)
- Menu creation and management
- Toolbar implementation
- Text rendering
- Font management
- Status bar functionality
- Scrolling implementation

#### 7.2.3 Non-Critical (Not Required for Acceptance)
- Help subsystem implementation
- Advanced Windows-specific features
- MDI window management

### 7.3 Success Criteria
- All critical functions must pass comprehensive testing
- High-priority functions must achieve 95% test coverage
- Library must not crash during extended operation
- Visual behavior must match Windows version within GTK capabilities

---

## Appendix A: Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [Date] | [Author] | Initial SRS document |

## Appendix B: References
- Open Watcom IDE Source Code
- GTK 2.0 Reference Manual
- X Window System Protocol Reference
- Windows API Documentation for Comparative Analysis