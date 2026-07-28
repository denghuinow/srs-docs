**Purpose & Scope**
The system is a port of the low-level Open Watcom GUI library to the Linux platform using the GTK+ toolkit. It enables existing Open Watcom applications to run on Linux with a native graphical interface. The port does not include support for Windows/OS2-style resource files, an MDI "windows-in-window" model, or a built-in help subsystem.

**Product Background / Positioning**
This port is part of the Open Watcom project, allowing its development tools and applications to be used on Linux. It replaces the original Windows/OS2 Presentation Manager dependencies with the GTK+ library, integrating the applications into the standard Linux desktop environment (X Window System).

**Core Functional Overview**
*   GUI library initialization and main event loop.
*   Creation and management of windows and dialogs.
*   Creation and management of standard UI controls (buttons, lists, edit fields).
*   Drawing of text, lines, and rectangles.
*   Menu, toolbar, and status bar management.

**Key Users & Usage Scenarios**
The primary user is a developer running Open Watcom tools (like the IDE) on Linux. The system runs as a library; the user interacts with the ported application, not the porting layer itself. There are no distinct user roles or permissions within the library.

**Major External Interfaces**
The system interfaces with the GTK+ library, the X Window System, and supporting libraries (GLib, Pango, GDK). Applications use the existing Open Watcom GUI API, which remains unchanged.

**Key Non-functional Requirements**
*   The ported library must compile and link on a target system with a standard C compiler, X11, and the required GTK+ libraries (GTK+, GLib, Pango, ATK, etc.).
*   The library can be linked statically if the target system lacks compatible GTK+ versions, accepting an increase in binary size.

**Constraints, Assumptions & Dependencies**
*   The port depends on the GTK+ 2.x toolkit and the X Window System.
*   It cannot support Windows/OS2 resource files, the MDI model, or modifying the window system menu due to GTK+ limitations.
*   The library assumes the use of the Open Watcom Programming Interface (WPI) and Memory Tracker (TrMem) libraries.

**Priorities & Acceptance Approach**
The priority is functional equivalence for the core GUI operations used by Open Watcom applications. Acceptance is achieved when the standard Open Watcom GUI sample programs compile, link, and run correctly on the Linux target, displaying and managing windows, dialogs, and controls.