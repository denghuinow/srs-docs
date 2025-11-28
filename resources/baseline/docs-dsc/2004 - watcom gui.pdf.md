Here is a comprehensive Software Requirements Specification (SRS) document for the Open Watcom GUI Library Port to Linux/GTK.

```markdown
# Software Requirements Specification
## Open Watcom GUI Library Port to Linux/GTK

**Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft  
**Authors:** [Your Name/Team]

---

## Table of Contents

1. [Introduction](#1-introduction)
   - [1.1 Purpose](#11-purpose)
   - [1.2 Project Scope](#12-project-scope)
   - [1.3 Definitions, Acronyms, and Abbreviations](#13-definitions-acronyms-and-abbreviations)
   - [1.4 References](#14-references)
2. [Overall Description](#2-overall-description)
   - [2.1 Product Perspective](#21-product-perspective)
   - [2.2 Product Functions](#22-product-functions)
   - [2.3 User Characteristics](#23-user-characteristics)
   - [2.4 Constraints](#24-constraints)
   - [2.5 Assumptions and Dependencies](#25-assumptions-and-dependencies)
3. [System Features and Requirements](#3-system-features-and-requirements)
   - [3.1 GUI Initialization and Management](#31-gui-initialization-and-management)
   - [3.2 Window Management](#32-window-management)
   - [3.3 Dialog and Control Rendering](#33-dialog-and-control-rendering)
   - [3.4 Text Rendering](#34-text-rendering)
   - [3.5 Common UI Controls](#35-common-ui-controls)
   - [3.6 Type Conversion and Handle Management](#36-type-conversion-and-handle-management)
4. [External Interface Requirements](#4-external-interface-requirements)
   - [4.1 User Interfaces](#41-user-interfaces)
   - [4.2 Hardware Interfaces](#42-hardware-interfaces)
   - [4.3 Software Interfaces](#43-software-interfaces)
   - [4.4 Communications Interfaces](#44-communications-interfaces)
5. [Non-Functional Requirements](#5-non-functional-requirements)
   - [5.1 Performance Requirements](#51-performance-requirements)
   - [5.2 Reliability Requirements](#52-reliability-requirements)
   - [5.3 Portability Requirements](#53-portability-requirements)
   - [5.4 Maintainability Requirements](#54-maintainability-requirements)
6. [Other Requirements](#6-other-requirements)
   - [6.1 Development Constraints](#61-development-constraints)
   - [6.2 Open Issues and Risks](#62-open-issues-and-risks)

---

## 1 Introduction

### 1.1 Purpose

This document specifies the requirements for porting the Open Watcom GUI library to Linux using the GTK toolkit. The primary objective is to enable existing Open Watcom applications to run natively on Linux systems while maintaining graphical interface compatibility and functionality.

### 1.2 Project Scope

The project involves creating a compatibility layer that translates Open Watcom GUI API calls to their GTK equivalents, allowing legacy applications to operate on modern Linux distributions without source code modification.

**In Scope:**
- Core GUI initialization and termination
- Basic window creation and management
- Standard UI controls (buttons, lists, labels, etc.)
- Dialog box rendering and management
- Text drawing and font handling
- Event handling and message processing

**Out of Scope:**
- Multiple Document Interface (MDI) support
- Windows/OS/2 resource file parsing
- Help subsystem integration
- Advanced graphics operations (GDI+ equivalents)

### 1.3 Definitions, Acronyms, and Abbreviations

- **GTK**: GIMP Toolkit, a cross-platform widget toolkit
- **GLib**: A low-level core library for GTK
- **Pango**: A library for internationalized text handling
- **HWND**: Window Handle (Windows API)
- **MDI**: Multiple Document Interface
- **MVP**: Minimum Viable Product
- **API**: Application Programming Interface
- **SRS**: Software Requirements Specification

### 1.4 References

- Open Watcom Project Documentation
- GTK+ 3.0 Reference Manual
- GLib Reference Manual
- Pango Documentation

## 2 Overall Description

### 2.1 Product Perspective

The ported GUI library will serve as a compatibility layer between existing Open Watcom applications and the Linux/GTK environment. It will intercept API calls from the application and translate them to appropriate GTK operations.

```
+---------------------+     +---------------------+     +-------------------+
| Open Watcom         |     | Ported GUI          |     | GTK+              |
| Application         |---->| Library Layer       |---->| Toolkit           |
|                     |     | (This Project)      |     |                   |
+---------------------+     +---------------------+     +-------------------+
```

### 2.2 Product Functions

The core functions of the ported library include:

1. **Initialization**: Initialize GTK environment and set up application context
2. **Window Management**: Create, destroy, and manage application windows
3. **Control Rendering**: Display and manage standard UI controls
4. **Event Handling**: Process user input and system events
5. **Text Rendering**: Display text with appropriate font and formatting
6. **Resource Management**: Handle memory and resource allocation

### 2.3 User Characteristics

The primary users of this system are:

- **Developers**: Maintaining or porting existing Open Watcom applications
- **End Users**: Running legacy Open Watcom applications on Linux systems
- **System Administrators**: Deploying and supporting the compatibility layer

### 2.4 Constraints

#### Technical Constraints:
- Must use GTK+ 3.0 or later as the underlying toolkit
- Must maintain API compatibility with existing Open Watcom applications
- Cannot modify source code of existing applications
- Must handle 32-bit to 64-bit type conversions where necessary

#### Platform Constraints:
- Target platform: Modern Linux distributions (Ubuntu 18.04+, RHEL 8+, etc.)
- Required libraries: GTK+ 3.0, GLib 2.0, Pango 1.0
- Architecture support: x86_64 primarily, with consideration for ARM64

### 2.5 Assumptions and Dependencies

**Assumptions:**
- Existing Open Watcom applications follow standard API usage patterns
- GTK+ 3.0 provides sufficient functionality to emulate required features
- Performance overhead of the translation layer is acceptable

**Dependencies:**
- Availability of GTK+ development libraries on target systems
- Compatibility with modern Linux display servers (X11 and Wayland)
- C compiler supporting both Open Watcom and Linux calling conventions

## 3 System Features and Requirements

### 3.1 GUI Initialization and Management

**3.1.1 Requirement: GUI System Initialization**
- **ID:** GUI-INIT-001
- **Description:** The library must initialize the GTK environment when the application starts
- **Priority:** High
- **Verification:** Unit testing, integration testing

**3.1.2 Requirement: Application Context Setup**
- **ID:** GUI-INIT-002
- **Description:** The library must create and maintain application context matching Open Watcom semantics
- **Priority:** High
- **Verification:** Application startup testing

### 3.2 Window Management

**3.2.1 Requirement: Window Creation**
- **ID:** WIN-CREATE-001
- **Description:** The system must create top-level windows with properties equivalent to Windows/OS2
- **Priority:** High
- **Verification:** Visual inspection, functional testing

**3.2.2 Requirement: Window Operations**
- **ID:** WIN-OPS-001
- **Description:** The system must support standard window operations: resize, minimize, maximize, close
- **Priority:** High
- **Verification:** User interaction testing

```c
// Example: Window creation API compatibility
HWND CreateWindow(...); // Must map to gtk_window_new()
```

### 3.3 Dialog and Control Rendering

**3.3.1 Requirement: Dialog Box Support**
- **ID:** DIALOG-001
- **Description:** The system must render modal and modeless dialog boxes using GTK containers
- **Priority:** High
- **Verification:** Dialog functionality testing

**3.3.2 Requirement: Control Layout**
- **ID:** LAYOUT-001
- **Description:** The system must approximate Windows dialog layout using GTK layout managers
- **Priority:** Medium
- **Verification:** Visual comparison with Windows version

### 3.4 Text Rendering

**3.4.1 Requirement: Text Drawing**
- **ID:** TEXT-001
- **Description:** The system must support basic text drawing operations with font selection
- **Priority:** High
- **Verification:** Text rendering tests

**3.4.2 Requirement: Font Management**
- **ID:** FONT-001
- **Description:** The system must map Windows font requests to available system fonts
- **Priority:** Medium
- **Verification:** Font rendering comparison

### 3.5 Common UI Controls

**3.5.1 Requirement: Button Controls**
- **ID:** CTRL-BTN-001
- **Description:** The system must render push buttons, checkboxes, and radio buttons
- **Priority:** High
- **Verification:** Control interaction testing

**3.5.2 Requirement: List Controls**
- **ID:** CTRL-LIST-001
- **Description:** The system must support list boxes and combo boxes
- **Priority:** High
- **Verification:** List population and selection testing

**3.5.3 Requirement: Input Controls**
- **ID:** CTRL-INPUT-001
- **Description:** The system must support text entry fields and edit controls
- **Priority:** High
- **Verification:** Text input testing

### 3.6 Type Conversion and Handle Management

**3.6.1 Requirement: Handle Translation**
- **ID:** TYPE-HWND-001
- **Description:** The system must map HWND handles to GTK window references
- **Priority:** High
- **Verification:** Handle validity testing

**3.6.2 Requirement: Data Type Compatibility**
- **ID:** TYPE-DATA-001
- **Description:** The system must handle 16-bit to 32/64-bit type conversions
- **Priority:** Medium
- **Verification:** Cross-platform data structure testing

## 4 External Interface Requirements

### 4.1 User Interfaces

The library itself has no direct user interface. It enables applications to display:

- Native-looking GTK windows and dialogs
- Standard UI controls consistent with Linux desktop themes
- Text rendering using system fonts

### 4.2 Hardware Interfaces

- **Display:** Supports standard Linux display servers (X11, Wayland)
- **Input:** Standard keyboard and mouse input through GTK event system
- **Graphics:** Utilizes system graphics capabilities through GTK/Cairo

### 4.3 Software Interfaces

**Required Libraries:**
- GTK+ 3.0: Primary GUI toolkit
- GLib 2.0: Core application support
- Pango 1.0: Text rendering and internationalization
- Cairo: Vector graphics rendering

**System Interfaces:**
- Linux system calls for process and memory management
- X11/Wayland protocols for display management

### 4.4 Communications Interfaces

No specific communication interfaces are required for the MVP. Future versions may require:

- Inter-process communication for advanced features
- Network connectivity for help system integration

## 5 Non-Functional Requirements

### 5.1 Performance Requirements

**5.1.1 Requirement: Startup Performance**
- **ID:** PERF-STARTUP-001
- **Description:** Application startup time should not exceed native Windows performance by more than 50%
- **Priority:** Medium

**5.1.2 Requirement: UI Responsiveness**
- **ID:** PERF-RESPONSE-001
- **Description:** UI operations should respond within 100ms for typical use cases
- **Priority:** High

### 5.2 Reliability Requirements

**5.2.1 Requirement: Application Stability**
- **ID:** RELI-STABLE-001
- **Description:** The library should not cause application crashes for standard API usage
- **Priority:** High

**5.2.2 Requirement: Memory Management**
- **ID:** RELI-MEMORY-001
- **Description:** The library must properly manage memory and avoid leaks
- **Priority:** High

### 5.3 Portability Requirements

**5.3.1 Requirement: Linux Distribution Support**
- **ID:** PORT-DISTRO-001
- **Description:** The library should work on major Linux distributions with GTK+ 3.0 available
- **Priority:** High

### 5.4 Maintainability Requirements

**5.4.1 Requirement: Code Organization**
- **ID:** MAINTAIN-CODE-001
- **Description:** The code should be modular with clear separation between API translation and GTK implementation
- **Priority:** Medium

## 6 Other Requirements

### 6.1 Development Constraints

#### API Compatibility Constraints:
- Must maintain binary compatibility where possible
- API function signatures cannot be changed
- Existing application code cannot be modified

#### Technical Limitations:
- GTK does not support Windows/OS2-style resource files natively
- MDI (Multiple Document Interface) "Windows in Window" model not supported in GTK
- Some Windows-specific visual behaviors may differ

### 6.2 Open Issues and Risks

#### High Priority Issues:

**6.2.1 Resource File Handling**
- **Issue:** Windows/OS2 resource files (.res) contain dialog templates, string tables, and menu definitions
- **Risk:** Applications may fail to start or display incorrectly without resource support
- **Mitigation:** Develop resource file parser or conversion tool

**6.2.2 String Table Support**
- **Issue:** String tables in resource files are commonly used for internationalization
- **Risk:** Applications may display incorrect text or fail to load
- **Mitigation:** Implement string table extraction and mapping

#### Medium Priority Issues:

**6.2.3 Help System Integration**
- **Issue:** Windows help system (WinHelp) integration is not addressed
- **Risk:** Help functionality in applications will be broken
- **Mitigation:** Map to Linux help viewers or implement compatibility layer

**6.2.4 Advanced Graphics Operations**
- **Issue:** Complex GDI operations may not have direct GTK equivalents
- **Risk:** Applications with custom drawing may display incorrectly
- **Mitigation:** Implement using Cairo graphics where possible

---

## Appendix A: MVP Feature Checklist

- [ ] GUI initialization and termination
- [ ] Basic window creation and management
- [ ] Standard window operations (resize, minimize, maximize)
- [ ] Dialog box rendering
- [ ] Basic controls: buttons, labels, text fields
- [ ] List controls: list boxes, combo boxes
- [ ] Text drawing with basic font support
- [ ] Event handling for user input
- [ ] Type conversion for window handles
- [ ] Memory management and cleanup

## Appendix B: Compatibility Risk Assessment

| Risk Area | Impact | Probability | Mitigation Strategy |
|-----------|--------|-------------|---------------------|
| Resource Files | High | High | Develop parser or conversion tool |
| MDI Support | Medium | Medium | Implement using GTK notebooks or separate windows |
| Font Metrics | Medium | Medium | Font mapping and metric adjustment |
| Help System | Low | High | Postpone to future release |
| Advanced GDI | Medium | Low | Implement using Cairo graphics |

---
**Document Revision History**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2023-10-26 | Initial Author | Initial draft creation |
```
This SRS document provides a comprehensive specification for the Open Watcom GUI library port to Linux/GTK. The document follows IEEE SRS standards and includes all necessary sections for development planning and implementation.