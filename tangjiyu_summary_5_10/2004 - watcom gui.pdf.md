# Open Watcom Linux Port - GUI Software Requirements Specification

## 1. Introduction

This document describes the requirements for porting the Open Watcom low-level GUI library to the Linux platform using the GTK toolkit for the X Window System. The porting effort aims to enable Open Watcom applications to run natively on Linux while maintaining compatibility with existing Windows and OS/2 implementations.

## 2. Target System Requirements

The ported library requires the following software components on the target Linux system:
- C compiler
- X Window System
- GTK+ libraries (version 2.0 or later)
- Related libraries: pkg-config, GNU make, JPEG/PNG/TIFF image libraries, FreeType, fontconfig, GNU libiconv, GNU gettext, GLib, Pango, ATK

## 3. Technical Approach

### 3.1 Porting Strategy
- Utilize GTK toolkit as the underlying windowing system
- Implement Watcom Programming Interface (WPI) functions using GTK equivalents
- Replace Windows/OS/2-specific types with GTK-compatible definitions
- Maintain existing GUI library API to ensure application compatibility

### 3.2 Widget Hierarchy
Implement standard Open Watcom GUI windows using the following GTK widget hierarchy:
- Window → Vertical Box → Scrolled Window → View Port → Fixed

## 4. Core Functional Requirements

### 4.1 GUI Library Initialization
- Initialize GUI system with main message loop
- Support program termination handling
- Manage resource cleanup procedures

### 4.2 Window Management
- Create and destroy windows with specified attributes
- Support window positioning and sizing
- Implement maximize, minimize, and restore operations
- Handle window visibility states
- Manage parent-child window relationships

### 4.3 Dialog Management
- Create dialog boxes from templates
- Support standard dialog controls
- Handle dialog initialization and termination
- Process dialog events and user interactions

### 4.4 Control Management
- Add, remove, and modify UI controls dynamically
- Support common control types: buttons, edit fields, static text, list boxes
- Enable/disable controls based on application state
- Manage control positioning and resizing
- Handle control visibility states

### 4.5 Text Handling
- Set and retrieve text from controls
- Support text selection operations
- Calculate text dimensions for layout purposes
- Handle font management and text metrics

### 4.6 Drawing Functions
- Draw lines, rectangles, and basic shapes
- Support color-based and attribute-based drawing
- Implement text rendering with various fonts
- Handle window repainting and refresh operations

### 4.7 Menu Systems
- Create and manage menu bars
- Support popup and floating menus
- Enable/disable menu items
- Handle menu item selection and events
- Support menu text modification

### 4.8 Scrolling
- Implement horizontal and vertical scroll bars
- Manage scroll ranges and positions
- Handle scroll events and user interactions
- Support scroll thumb positioning

### 4.9 Toolbars and Status Windows
- Create and manage toolbar interfaces
- Support floating and fixed toolbar configurations
- Implement status window functionality
- Handle status text display and updates

### 4.10 Event Handling
- Process mouse and keyboard events
- Support focus management between controls
- Handle window resize and move operations
- Implement callback mechanisms for UI events

### 4.11 Resource Management
- Handle string resources and localization
- Manage color selection and customization
- Support font selection dialogs
- Implement memory management for UI elements

## 5. Known Limitations

### 5.1 Platform-specific Constraints
- No support for Windows/OS/2-style resource files
- MDI "Windows in Window" model not available in GTK
- No built-in help subsystem (handled by desktop environments)
- Different approach to window building (no window classes)

### 5.2 Workarounds
- Use libglade library with XML for UI building
- Handle string resources through gettext library
- Implement parent-child window relationships as alternatives to MDI

## 6. Implementation Priorities

### 6.1 Critical Functions (Priority 1)
- GUI library initialization and message loop
- Basic window creation and management
- Dialog box implementation
- Core control management

### 6.2 Important Functions (Priority 2)
- Menu systems and toolbar implementation
- Scrolling functionality
- Text handling and drawing functions
- Event processing

### 6.3 Enhancement Functions (Priority 3)
- Advanced control types
- Specialized dialog functions
- Color and font management
- Help system integration
