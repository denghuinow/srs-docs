# Software Requirements Specification (SRS)
## Open Watcom GUI Library Linux Port

**Document Version:** 1.0  
**Date:** [Current Date]  
**Status:** Draft

---

## 1. Introduction

### 1.1 Purpose
This document specifies the requirements for porting Open Watcom's Windows GUI library to Linux using the GTK toolkit. The primary purpose is to enable cross-platform GUI compatibility for the Open Watcom Integrated Development Environment (IDE) on Linux systems while maintaining API compatibility with existing application logic.

### 1.2 Scope
The scope of this project includes:
- Creating a Linux-compatible GUI library that mimics Windows API behavior
- Integrating with GTK 2.0+ as the underlying UI toolkit
- Providing window management, dialog handling, and control rendering
- Maintaining visual and behavioral consistency across platforms

**Out of Scope:**
- Windows-style resource file support
- Multiple Document Interface (MDI) "windows in window" model
- Built-in help subsystem implementation
- Windows API dependencies

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
This library serves as a compatibility layer between Open Watcom's existing Windows GUI API calls and the Linux GTK environment. It positions itself as the foundation for Open Watcom IDE's Linux port, replacing Windows/OS2 API dependencies with GTK equivalents.

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

### 2.4 Constraints
- **Technical Constraint:** No MDI "windows in window" support due to GTK limitations
- **Platform Constraint:** Must run on GTK 2.0+ with X Window System
- **Compatibility Constraint:** No support for Windows resource files
- **Architectural Constraint:** Must maintain API compatibility with existing Open Watcom applications

### 2.5 Assumptions and Dependencies
**Assumptions:**
- Resource file conversion via libglade is acceptable for non-string resources
- GTK 2.0+ is available on target Linux systems
- X Window System is the primary display server

**Dependencies:**
- GTK 2.0+ development libraries
- X Window System
- libglade for partial resource file support

## 3. System Features and Requirements

### 3.1 Core Window Management

#### 3.1.1 Functional Requirements

**FR-001: Window Initialization**
```c
// Must support equivalent of Windows CreateWindow() API
HWND CreateWindow(LPCTSTR className, LPCTSTR windowName, DWORD style, 
                  int x, int y, int width, int height, HWND parent, 
                  HMENU menu, HINSTANCE instance, LPVOID param);
```
- **Priority:** Critical
- **Description:** Create and initialize application windows using GTK equivalents
- **Acceptance Criteria:** 100% functional equivalence in window creation

**FR-002: Window Message Handling**
- **Priority:** Critical
- **Description:** Implement Windows message loop equivalent using GTK event system
- **Acceptance Criteria:** All window events properly routed to application handlers

**FR-003: Window Destruction**
- **Priority:** Critical
- **Description:** Proper cleanup and destruction of window resources
- **Acceptance Criteria:** No memory leaks or resource retention

### 3.2 Dialog System

#### 3.2.1 Functional Requirements

**FR-010: Dialog Creation**
```c
// Must support modal and modeless dialog creation
HWND CreateDialog(HINSTANCE instance, LPCTSTR template, HWND parent, DLGPROC dialogProc);
```
- **Priority:** Critical
- **Description:** Create dialogs from converted resource definitions
- **Acceptance Criteria:** Dialog appearance and behavior match Windows version

**FR-011: Dialog Control Management**
- **Priority:** Critical
- **Description:** Handle standard controls (buttons, edit boxes, lists, combo boxes)
- **Acceptance Criteria:** All control types render and function correctly

### 3.3 Menu and Toolbar System

#### 3.3.1 Functional Requirements

**FR-020: Menu Creation**
```c
// Support for menu creation and management
HMENU CreateMenu();
HMENU CreatePopupMenu();
```
- **Priority:** High
- **Description:** Convert Windows menu resources to GTK menu structures
- **Acceptance Criteria:** 95% functional coverage of menu operations

**FR-021: Menu Event Handling**
- **Priority:** High
- **Description:** Route menu selection events to appropriate handlers
- **Acceptance Criteria:** Menu commands properly execute application functions

**FR-022: Toolbar Implementation**
- **Priority:** High
- **Description:** Create and manage toolbar controls
- **Acceptance Criteria:** Toolbar buttons display and function correctly

### 3.4 Rendering and Display

#### 3.4.1 Functional Requirements

**FR-030: Text Rendering**
- **Priority:** Critical
- **Description:** Render text using compatible fonts and metrics
- **Acceptance Criteria:** Text appearance matches Windows rendering

**FR-031: Font Management**
- **Priority:** Critical
- **Description:** Create, select, and manage font resources
- **Acceptance Criteria:** Font rendering consistent across platforms

**FR-032: Status Bar Implementation**
- **Priority:** High
- **Description:** Create and update status bar controls
- **Acceptance Criteria:** Status information displays correctly

**FR-033: Scrolling Support**
- **Priority:** High
- **Description:** Implement scrollable areas and scroll bar controls
- **Acceptance Criteria:** Scrolling behavior matches Windows implementation

## 4. External Interface Requirements

### 4.1 User Interfaces
- **API Compatibility:** Must maintain identical function signatures to Windows version
- **Visual Consistency:** UI elements must maintain identical visual behavior across platforms
- **Input Handling:** Keyboard and mouse events must be processed identically

### 4.2 Hardware Interfaces
- **Display:** X Window System compatible displays
- **Input:** Standard keyboard and mouse devices

### 4.3 Software Interfaces
- **GTK 2.0+:** Primary UI toolkit interface
- **X Window System:** Display server interface
- **libglade:** For loading converted UI resource files
- **Standard C Library:** For basic runtime operations

### 4.4 Communications Interfaces
- **Inter-process Communication:** Standard X Window System IPC mechanisms
- **Signal Handling:** POSIX signal handling for application management

## 5. Non-Functional Requirements

### 5.1 Performance Requirements
- **Responsiveness:** UI operations must complete within 100ms for standard operations
- **Memory Usage:** Memory footprint should be comparable to Windows version ±15%
- **Startup Time:** Application initialization within 2 seconds on standard hardware

### 5.2 Safety Requirements
- **Resource Management:** Proper cleanup of all GTK resources on application exit
- **Error Handling:** Graceful degradation when encountering unsupported features

### 5.3 Security Requirements
- **No Elevated Privileges:** Library must not require special permissions
- **Input Validation:** All user input must be properly validated

### 5.4 Software Quality Attributes
- **Reliability:** 99% uptime during normal operation
- **Maintainability:** Code must be well-documented and modular
- **Portability:** Dependent only on specified GTK and X Window System APIs

### 5.5 Compatibility Requirements
- **API Compatibility:** 100% source-level compatibility with existing Open Watcom applications
- **Visual Compatibility:** Identical appearance and behavior to Windows version
- **Platform Support:** Linux distributions with GTK 2.0+ and X Window System

## 6. System Limitations

### 6.1 Known Limitations
- **MDI Support:** No Multiple Document Interface "windows in window" model
- **Resource Files:** No direct support for Windows .rc resource files
- **Help System:** Built-in help subsystem not implemented
- **Advanced Controls:** Some specialized Windows controls may have limited functionality

### 6.2 Workarounds
- **Resource Conversion:** Use libglade for converting non-string resources
- **MDI Alternative:** Implement tabbed interface or separate windows
- **Help System:** Rely on external help viewers or documentation systems

## 7. Acceptance Criteria

### 7.1 Testing Requirements

#### 7.1.1 Critical Path Testing
- **Test Case:** GUI sample test (samp2.c)
- **Requirement:** 100% pass rate for all critical functions
- **Scope:** Window creation, dialog management, basic controls

#### 7.1.2 High Priority Testing
- **Test Case:** Menu and toolbar functionality
- **Requirement:** 95% functional coverage
- **Scope:** Menu creation, event handling, toolbar operations

#### 7.1.3 Visual Verification
- **Test Case:** Side-by-side comparison with Windows version
- **Requirement:** Identical visual behavior and layout
- **Scope:** All implemented UI components

### 7.2 Performance Benchmarks
- **Metric:** Operation completion times
- **Standard:** Within 15% of Windows version performance
- **Measurement:** Automated timing tests for key operations

## 8. Appendix

### 8.1 Reference Materials
- GTK 2.0 Reference Manual
- Open Watcom Windows API Documentation
- X Window System Protocol Reference

### 8.2 Glossary
- **Porting:** Adapting software to run in different environment
- **Compatibility Layer:** Software that emulates one system's API on another
- **Widget:** GUI component or control in GTK terminology

---

**Document Approval**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Manager | | | |
| Lead Developer | | | |
| Quality Assurance | | | |