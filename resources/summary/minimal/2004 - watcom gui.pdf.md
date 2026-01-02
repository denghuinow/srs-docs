**Purpose & Scope**: Port the low-level Open Watcom GUI library to the Linux platform using the GTK+ toolkit for the X Window System, enabling Open Watcom applications to run with a native graphical interface.

**Core Functions**:
*   Initialize the GUI library and manage the main event loop.
*   Create and manage windows, including dialogs and controls.
*   Handle basic user interaction (menus, toolbars, status windows).
*   Perform fundamental drawing and text rendering operations.

**Key Users**: Developers using the Open Watcom toolchain to create or run applications on Linux.

**Key Constraints**:
*   The system cannot use Windows or OS/2-style resource files; an alternative method for defining dialogs and strings is required.
*   The GTK+ toolkit does not support the Multiple Document Interface (MDI) "window-in-window" model.
*   The target system must have specific libraries including GTK+, GLib, Pango, and the X Window System installed.