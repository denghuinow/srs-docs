# Short Summary: Open Watcom Linux GUI Port

## Background and objectives
This document outlines the requirements for porting the Open Watcom GUI library from Windows/OS2 to Linux using the GTK toolkit. The goal is to enable Open Watcom development tools to run natively on Linux systems with a functional graphical user interface.

## In scope
- Porting low-level GUI library functions to GTK equivalents
- Implementing window creation, dialogs, and controls using GTK widgets
- Supporting basic GUI functionality (menus, toolbars, status bars)
- Handling text rendering and drawing operations via GTK/Pango
- Maintaining compatibility with existing Open Watcom application code

## Out of scope
- Windows/OS2-style resource file support (requires separate conversion utility)
- MDI "Windows in Window" model (GTK doesn't support this)
- Built-in help subsystem implementation
- System menu modification capabilities
- Direct resource DLL loading mechanisms

## Stakeholders and core use cases
**Stakeholders:**
- **Open Watcom developers**: Maintain and enhance the GUI library for cross-platform compatibility
- **Linux application developers**: Use Open Watcom tools for C/C++ development on Linux
- **SciTech Software**: Provide commercial support and maintenance for the ported library
- **Open source community**: Contribute to and benefit from open-source compiler tools on Linux

**User stories:**
1. As a Linux developer, I want to run Open Watcom IDE so that I can develop C/C++ applications natively on Linux
2. As an Open Watcom user, I want consistent GUI behavior across platforms so that my applications work similarly on Windows and Linux
3. As a system administrator, I want easy deployment of the ported library so that I can install it on multiple Linux workstations
4. As a GUI library maintainer, I want clear porting guidelines so that I can efficiently implement GTK equivalents of Windows API functions

## Success metrics
- Standard Open Watcom GUI samples compile and run correctly on Linux
- Open Watcom IDE launches and provides basic functionality on GTK-based Linux systems
- Ported library passes existing GUI test suites with equivalent behavior to Windows/OS2 versions
- Library can be compiled on major Linux distributions (RedHat, SuSE, TurboLinux)

## Major constraints
- GTK API is fundamentally different from Windows/OS2 APIs, requiring significant abstraction
- No direct support for Windows/OS2 resource files in GTK
- MDI window model not supported in GTK
- Must maintain backward compatibility with existing Open Watcom application code
- Target systems must have specific libraries installed (GTK+, GLib, Pango, etc.)

## Undecided issues
- Best approach for handling string resources (gettext vs custom implementation)
- How to implement numeric widget identifiers in GTK (which doesn't natively support them)
- Whether to use libglade for UI description or implement custom XML conversion
- How to handle window class registration concepts in GTK's classless system
- Memory allocation strategy for text buffers and other resources