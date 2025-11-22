# Software Requirements Specification (SRS)
## Open Watcom GUI Library Linux Port

**Document Version:** 1.0  
**Date:** [Current Date]  
**Status:** Draft

---

## 1. Introduction

### 1.1 Purpose
This document specifies the requirements for porting Open Watcom's Windows GUI library to Linux using the GTK toolkit. The primary purpose is to enable cross-platform GUI compatibility for the Open Watcom Integrated Development Environment (IDE) on Linux systems while maintaining API compatibility with existing Windows applications.

### 1.2 Scope
The scope of this project includes:
- Creating a Linux-compatible GUI library that mimics Windows API behavior
- Integrating with GTK 2.0+ as the underlying UI toolkit
- Providing window management, dialog handling, and control rendering
- Maintaining source-level compatibility with existing Open Watcom applications

**Out of Scope:**
- Windows-style resource file support
- Multiple Document Interface (MDI) "windows in window" model
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

## 2. Overall Description

### 2.1 Product Perspective
This library serves as a compatibility layer between Open Watcom's Windows GUI API and Linux's native GTK toolkit. It replaces Windows/OS2 API dependencies while maintaining identical API signatures for existing application code.

### 2.2 Product Functions
- **Window Management**: Creation, destruction, and management of application windows
- **Dialog Systems**: Modal and modeless dialog implementation
- **Control Handling**: Standard UI controls (buttons, text fields, lists)
- **Menu Management**: Menu creation and event handling
- **Rendering Services**: Text and font rendering capabilities
- **UI Components**: Status bars and scrolling functionality

### 2.3 User Characteristics
**Primary Users:** Open Watcom developers porting the IDE to Linux
- **Technical Expertise:** Advanced
- **Permissions:** Full access to porting tools and development environment
- **Experience:** Familiar with Open Watcom codebase and cross-platform development

### 2.4 Operating Environment
- **Operating System:** Linux distributions supporting X Window System
- **UI Toolkit:** GTK 2.0 or later
- **Dependencies:** X Window System, GLib
- **Excluded Environments:** Windows API, Windows resource files

### 2.5 Design and Implementation Constraints
- Must use GTK 2.0+ as the underlying toolkit
- Cannot implement MDI window model due to GTK limitations
- Must maintain API compatibility with existing Open Watcom applications
- Resource files require conversion (libglade for non-string resources)

### 2.6 Assumptions and Dependencies
- GTK 2.0+ is available on target systems
- X Window System is the display server
- Resource file conversion via libglade is acceptable for non-string resources
- Existing Open Watcom application logic remains unchanged

## 3. System Features

### 3.1 Window Management (Critical Priority)

#### 3.1.1 Window Initialization
```c
// API Compatibility Requirement
BOOL InitializeWindow(HWND hWnd, LPCTSTR windowTitle, int width, int height);
```

**Requirements:**
- Create native GTK windows matching Windows API behavior
- Support window sizing and positioning
- Maintain window state persistence
- Handle window focus and activation events

#### 3.1.2 Window Operations
- Window show/hide functionality
- Minimize/maximize/restore operations
- Window closing and destruction
- Z-order management

### 3.2 Dialog System (Critical Priority)

#### 3.2.1 Dialog Creation
```c
// API Compatibility Requirement
HWND CreateDialog(HINSTANCE hInstance, LPCTSTR lpTemplate, HWND hWndParent, DLGPROC lpDialogFunc);
```

**Requirements:**
- Modal and modeless dialog support
- Dialog resource template conversion
- Parent-child window relationships
- Dialog message processing

#### 3.2.2 Control Management
- Standard control types: buttons, labels, text fields, lists
- Control event handling and messaging
- Layout management matching Windows behavior
- Focus and tab order management

### 3.3 Menu and Toolbar System (High Priority)

#### 3.3.1 Menu Management
- Menu bar creation and population
- Drop-down and context menu support
- Menu item event handling
- Menu state management (enable/disable, check/uncheck)

#### 3.3.2 Toolbar Implementation
- Toolbar creation and button management
- Tooltip support
- Button state management
- Integration with menu commands

### 3.4 Rendering Services (High Priority)

#### 3.4.1 Text Rendering
- Font selection and management
- Text drawing with proper metrics
- Text alignment and formatting
- Clipboard operations (cut/copy/paste)

#### 3.4.2 Basic Drawing
- Simple geometric primitives
- Color management
- Bitmap rendering support

### 3.5 UI Components (High Priority)

#### 3.5.1 Status Bar
- Multi-panel status bar implementation
- Text display and updating
- Size grip functionality

#### 3.5.2 Scrolling Support
- Scrollbar creation and management
- Scroll event handling
- Viewport management for scrollable areas

## 4. External Interface Requirements

### 4.1 User Interfaces
- **API Level:** Windows-style GUI API compatible with Open Watcom
- **Native Level:** GTK 2.0+ widget toolkit
- **Display Server:** X Window System

### 4.2 Hardware Interfaces
- Standard keyboard and mouse input
- Display output through X Window System
- No specialized hardware requirements

### 4.3 Software Interfaces

#### 4.3.1 GTK 2.0+
- Primary UI toolkit interface
- Version requirement: 2.0 or later
- Feature usage: Windows, dialogs, controls, menus

#### 4.3.2 X Window System
- Display server communication
- Window management services
- Input event handling

#### 4.3.3 libglade (Optional)
- Resource file loading for non-string resources
- UI layout description parsing

### 4.4 Communications Interfaces
- No network communication requirements
- Inter-process communication through standard X11 mechanisms

## 5. Non-Functional Requirements

### 5.1 Performance Requirements
- Window creation: < 100ms on standard hardware
- Event processing: Responsive within 50ms
- Redraw operations: Complete within frame refresh intervals

### 5.2 Compatibility Requirements
- **API Compatibility:** 100% source-level compatibility with Open Watcom Windows GUI API
- **Visual Compatibility:** Identical visual behavior and layout across platforms
- **Behavioral Compatibility:** Consistent user interaction patterns

### 5.3 Reliability Requirements
- No memory leaks in window lifecycle management
- Graceful handling of invalid API parameters
- Stable under continuous operation (IDE usage patterns)

### 5.4 Portability Requirements
- Linux distributions with GTK 2.0+ and X Window System
- Architecture independence (x86, x86_64)
- No distribution-specific dependencies

### 5.5 Maintainability Requirements
- Modular design separating Windows API layer from GTK implementation
- Comprehensive error logging and debugging support
- Clear separation between platform-specific and common code

## 6. Acceptance Criteria

### 6.1 Critical Functionality (100% Coverage Required)
- All window creation and management functions
- Complete dialog system implementation
- Control creation and event handling
- Must pass GUI sample test (`samp2.c`) without modifications

### 6.2 High Priority Functionality (95% Coverage Required)
- Menu system implementation
- Toolbar creation and management
- Text rendering and font management
- Status bar and scrolling functionality

### 6.3 Test Approach
- **Unit Testing:** Individual API function verification
- **Integration Testing:** `samp2.c` GUI sample application
- **Visual Testing:** Side-by-side comparison with Windows version
- **Compatibility Testing:** Existing Open Watcom applications

### 6.4 Success Criteria
- Open Watcom IDE compiles without modification
- IDE launches and displays main window correctly
- All dialogs and controls function as expected
- No regression in application behavior

## 7. Appendices

### 7.1 Excluded Features
The following Windows GUI features are explicitly not supported:

1. **MDI (Multiple Document Interface)**
   - Technical constraint: GTK does not support MDI model
   - Alternative: Use separate top-level windows or tabbed interface

2. **Windows Resource Files**
   - No native support for .rc files
   - Partial solution: libglade for UI layout descriptions
   - String resources require separate handling

3. **Built-in Help Subsystem**
   - Windows Help (HLP) format not supported
   - Alternative: External help viewer integration

### 7.2 API Compatibility Matrix

| Windows API Category | Implementation Status | GTK Equivalent |
|---------------------|----------------------|----------------|
| Window Management | Full Implementation | GtkWindow, GtkDialog |
| Dialog Boxes | Full Implementation | GtkDialog, GtkBox |
| Basic Controls | Full Implementation | GtkButton, GtkEntry, etc. |
| Menus | Full Implementation | GtkMenuBar, GtkMenuItem |
| Drawing | Basic Implementation | GDK Drawing |
| MDI | Not Supported | N/A |
| Resource Files | Partial (libglade) | GLADE files |

### 7.3 Dependencies and Constraints Summary

**Hard Dependencies:**
- GTK 2.0+ development libraries
- X Window System
- GLib 2.0+

**Technical Constraints:**
- No MDI support possible
- Resource file conversion required
- Help subsystem excluded from scope

**Assumptions:**
- Target users are developers familiar with porting challenges
- libglade provides acceptable resource file alternative
- Visual consistency is more important than pixel-perfect accuracy

---

**Document Approval**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Manager | | | |
| Lead Developer | | | |
| Quality Assurance | | | |