# Balanced Summary

## Goals and Scope
This document specifies the requirements for porting the Open Watcom GUI library to Linux using the GTK toolkit. The project aims to enable Open Watcom applications to run on Linux systems with native GUI functionality while addressing key compatibility challenges between Windows/OS/2 and GTK APIs.

## Roles and User Stories
- **As a developer**, I want to compile Open Watcom GUI applications on Linux so that they can run natively on Linux systems.
- **As an end user**, I want Open Watcom applications to display proper GUI elements so that I can interact with them effectively.
- **As a maintainer**, I want the ported library to handle resource files appropriately so that application resources are properly loaded.
- **As a tester**, I want consistent window management behavior so that application windows behave predictably across platforms.

## Key Processes
1. **Library Initialization** - Trigger: Application startup via GUIXMain()
2. **Window Creation** - Trigger: GUICreateWindow() call
3. **Dialog Management** - Trigger: GUICreateDialog() call
4. **Control Handling** - Trigger: GUIAddControl() calls
5. **Event Processing** - Trigger: GUIWinMessageLoop() starts
6. **Drawing Operations** - Trigger: Paint events
7. **Resource Cleanup** - Trigger: Application shutdown

## Domain Data Elements
- **Window** (Primary: HWND; Fields: title, position, size, style, parent)
- **Control** (Primary: ControlID; Fields: type, text, position, size, state)
- **Dialog** (Primary: DialogID; Fields: template, controls, modal flag)
- **Menu** (Primary: MenuID; Fields: items, hierarchy, enabled state)
- **Font** (Primary: FontHandle; Fields: name, size, style, metrics)
- **Resource** (Primary: ResourceID; Fields: type, data, language)

## Non-functional Requirements
- Compatibility with major Linux distributions (RedHat, SuSE, TurboLinux)
- Stable performance equivalent to native Windows/OS/2 versions
- Proper integration with X Window System
- Support for international text via Pango library
- Maintainable code structure for future enhancements
- Reasonable memory usage and startup time

## Milestones and External Dependencies
- GTK+ library version compatibility
- X Window System availability
- GLib, Pango, and ATK libraries
- Image format libraries (JPEG, PNG, TIFF)
- GNU compiler toolchain availability

## Risks and Mitigation Strategies
- **Resource file incompatibility** - Develop conversion utility for Windows/OS/2 resources
- **MDI window model limitations** - Implement parent-child window relationships as alternative
- **Help subsystem absence** - Integrate with desktop help systems
- **Numeric widget identifiers** - Maintain internal mapping system
- **API paradigm differences** - Create abstraction layer for GTK-specific implementations

## Undecided Issues
- Complete resource file handling strategy
- MDI "Windows in Window" alternative implementation
- Help system integration approach
- Static vs dynamic linking decision for deployment
- System menu modification capabilities
- Memory allocation algorithm compatibility