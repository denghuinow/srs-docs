**Purpose & Scope**: Port the low-level Open Watcom GUI library to Linux using the GTK toolkit for the X Window System.

**Core Functions**:
*   Initialize the GUI library and manage the main event loop.
*   Create and manage windows, dialogs, and standard UI controls (buttons, lists, menus).
*   Handle core UI operations: drawing, text rendering, input, and scrolling.

**Key Constraints**:
*   The system must have GTK+ and its dependent libraries (GLib, Pango, ATK, etc.) installed.
*   Cannot use Windows/OS2-style resource files; requires an alternative for dialogs and string tables.
*   Cannot implement the MDI "Windows in Window" model.