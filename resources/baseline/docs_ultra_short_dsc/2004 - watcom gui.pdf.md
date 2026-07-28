# Software Requirements Specification (SRS)
## Open Watcom GUI Library Port to Linux (GTK+)

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review  
**Project:** Open Watcom GUI Library Port  
**Authors:** Open Watcom Development Team

---

### 1. Introduction

#### 1.1 Purpose
This document defines the requirements for the port of the low-level Open Watcom GUI library to the Linux platform using the GTK+ toolkit. The primary purpose is to enable existing Open Watcom applications to run on Linux with a native graphical user interface, without requiring modifications to the application source code. This SRS serves as the authoritative specification for developers implementing the port and for stakeholders verifying its completeness.

#### 1.2 Scope
The scope of this project includes the development of a library that maps the existing Open Watcom GUI API calls to their functional equivalents in the GTK+ 2.x toolkit and the X Window System.

**In-Scope:**
*   Implementation of the core Open Watcom GUI API functions for window, dialog, and control management.
*   Translation of drawing primitives (text, lines, rectangles) to GTK+/Cairo operations.
*   Implementation of the main event loop and message processing using GLib/GTK+.
*   Management of menus, toolbars, and status bars.
*   Static and dynamic linking support for the final library.

**Out-of-Scope:**
*   Support for compiling or interpreting Windows/OS2-style resource files (`.rc`, `.res`).
*   Implementation of a Multiple Document Interface (MDI) "windows-in-window" model.
*   Provision of a built-in help subsystem or help file viewer.
*   Modification of the native Linux window manager's system menu or decorations.
*   Porting of non-GUI related Open Watcom libraries.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **API:** Application Programming Interface.
*   **GDK:** GIMP Drawing Kit (low-level layer of GTK+).
*   **GLib:** General-purpose utility library for GTK+.
*   **GTK+:** GIMP Toolkit, a widget toolkit for creating graphical user interfaces.
*   **IDE:** Integrated Development Environment.
*   **MDI:** Multiple Document Interface.
*   **OS/2:** Operating System/2 (IBM).
*   **Pango:** Library for internationalized text layout and rendering.
*   **PM:** Presentation Manager (OS/2 GUI subsystem).
*   **SRS:** Software Requirements Specification.
*   **TrMem:** Open Watcom Memory Tracker library.
*   **WPI:** Open Watcom Programming Interface library.
*   **X11/X Window System:** The underlying windowing system for most Linux desktop environments.

#### 1.4 References
*   Open Watcom Project Documentation
*   GTK+ 2.x Reference Manual
*   X Window System Protocol
*   ISO/IEC/IEEE 29148:2018 - Systems and software engineering — Life cycle processes — Requirements engineering

#### 1.5 Document Overview
The remainder of this document describes the overall product perspective, specific functional and non-functional requirements, external interfaces, and other constraints for the Open Watcom GUI library port.

### 2. Overall Description

#### 2.1 Product Perspective
This port is a component of the broader Open Watcom project ecosystem. It acts as a compatibility layer, sitting between existing Open Watcom applications and the modern Linux graphical stack.

**System Interfaces:**
```
[Open Watcom Application] --> [Open Watcom GUI API] --> [This Port (libwgui_gtk.so/a)] --> [GTK+ / X11 / Pango / GLib] --> [Linux OS]
```

The port is a drop-in replacement for the original Windows/OS2 PM GUI library. It must maintain binary compatibility at the API level, ensuring that applications linked against the original library can be re-linked against the new library without source code changes.

#### 2.2 Product Functions
The core functions provided by the library are:
1.  **Initialization & Termination:** Initialize the GTK+ library and manage the application lifecycle.
2.  **Event Loop Management:** Run the main GLib event loop, translating and dispatching X11/GTK+ events to the application's message queue.
3.  **Window Management:** Create, destroy, show, hide, move, resize, and manage top-level windows and dialog boxes.
4.  **Control Management:** Create and manage standard GUI controls (e.g., buttons, static text, list boxes, combo boxes, edit fields, scrollbars).
5.  **Graphics Output:** Draw basic primitives including text, lines, rectangles (filled and framed), and handle device contexts (DC).
6.  **User Interface Components:** Create and manage menu bars, pull-down menus, pop-up menus, toolbars, and status bars.
7.  **Dialog Procedure Support:** Manage modal and modeless dialog boxes, including control message handling.

#### 2.3 User Characteristics
The end user of this product is a **software developer** who uses Open Watcom development tools (such as the IDE, debugger, or resource editor) on a Linux system. The user is technically proficient and understands the concept of library dependencies and linking. The user interacts directly with the ported Open Watcom application; the porting layer itself is invisible. There are no administrative users, roles, or privilege levels within the library.

#### 2.4 Constraints
*   **Technical:** The implementation is constrained by the architectural differences between the Win16/OS2 PM and GTK+/X11 models, particularly regarding resource files, MDI, and low-level window control.
*   **Platform:** The target platform is Linux running the X Window System. Other Unix-like systems or Wayland are not in scope.
*   **Dependency:** The project is dependent on the GTK+ 2.x series of libraries and their own dependencies (GLib, Pango, ATK). Support for GTK+ 3.x or 4.x is not required.
*   **Legal/Compatibility:** The library must maintain API/ABI compatibility with the documented Open Watcom GUI library to fulfill its core purpose.

#### 2.5 Assumptions and Dependencies
*   The target Linux system has a standard C development environment (GCC or equivalent) installed.
*   The target system has the necessary GTK+ 2.x development packages (`gtk2-devel`, `glib2-devel`, `pango-devel`, etc.) and X11 libraries available, unless static linking is used.
*   The Open Watcom application using this library also links against the supporting Open Watcom WPI and TrMem libraries.
*   The application's source code does not rely on undocumented behavior or side-effects of the original GUI library.

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 User Interfaces
Not applicable. This is a library with a programming interface (API), not a direct user interface.

##### 3.1.2 Hardware Interfaces
The library interfaces indirectly with display hardware via the X Window System and input devices via X11 input events.

##### 3.1.3 Software Interfaces
*   **Open Watcom GUI API:** The library shall provide a complete implementation of the public functions defined in the Open Watcom GUI library header files (e.g., `gui*.h`). The function signatures, data structures, and constants must be identical.
*   **GTK+ 2.x Library:** The library shall call GTK+ functions to create widgets, manage windows, and handle events.
*   **Xlib / XCB:** The library may use low-level X11 calls via GDK or directly for functionality not exposed by GTK+.
*   **Pango:** The library shall use Pango for all text layout and font rendering.
*   **Cairo:** The library shall use Cairo (via GDK) for all 2D drawing operations.
*   **GLib:** The library shall use GLib for the main event loop, timers, and data structures.
*   **Standard C Library:** The library shall use the system's standard C library.

##### 3.1.4 Communications Interfaces
Not applicable.

#### 3.2 Functional Requirements

##### 3.2.1 Core Library Initialization (FR-01)
**Description:** The library must initialize the GTK+ environment and set up necessary data structures.
**Requirement:** The `GUIInit` (or equivalent) function shall initialize the GTK+ library (`gtk_init`) and prepare the internal state for window management. It shall return a success/failure code as defined by the original API.

##### 3.2.2 Main Event Loop (FR-02)
**Description:** The library must run an event loop that processes X11/GTK+ events and translates them into Open Watcom GUI messages.
**Requirement:** The `GUIProcessMessages` (or equivalent) function shall implement a non-blocking poll of the GLib event queue. It shall translate GTK+ signals (e.g., `button-press-event`, `destroy`, `expose-event`) into corresponding Open Watcom messages (e.g., `WM_BUTTON1DOWN`, `WM_CLOSE`, `WM_PAINT`) and dispatch them to the appropriate window procedure.

##### 3.2.3 Window Creation and Management (FR-03)
**Description:** The library must create and manage top-level windows.
**Requirement:** The `GUICreateWindow` function shall create a GTK window (`GtkWindow`), apply specified styles (border, title bar, minimize/maximize buttons), and register an internal mapping between the GTK window and the Open Watcom window handle. Functions for moving (`GUIMoveWindow`), sizing (`GUISizeWindow`), showing (`GUIShowWindow`), and destroying (`GUIDestroyWindow`) shall operate on the corresponding GTK window.

##### 3.2.4 Dialog Box Management (FR-04)
**Description:** The library must support modal and modeless dialog boxes.
**Requirement:** The `GUIDialogBox` (or equivalent) function shall create a dialog window, typically a `GtkDialog` with appropriate buttons. For modal dialogs, it shall run a nested GTK event loop (`gtk_dialog_run`) while blocking the parent window. Control creation within the dialog shall follow FR-05.

##### 3.2.5 Control Creation and Management (FR-05)
**Description:** The library must create standard UI controls within windows and dialogs.
**Requirement:**
*   `GUICreateControl` shall create the appropriate GTK widget based on the control type:
    *   Button -> `GtkButton`
    *   Static Text -> `GtkLabel`
    *   Edit Field -> `GtkEntry` or `GtkTextView`
    *   List Box -> `GtkTreeView` with a `GtkListStore`
    *   Combo Box -> `GtkComboBox`
    *   Check Box -> `GtkCheckButton`
    *   Radio Button -> `GtkRadioButton`
*   The library shall manage the parenting of the control to its host window/dialog and forward relevant GTK signals (e.g., `clicked`, `changed`) as Open Watcom control notification messages.

##### 3.2.6 Drawing Operations (FR-06)
**Description:** The library must provide functions for drawing graphics and text.
**Requirement:**
*   Functions like `GUIDrawText`, `GUIDrawLine`, `GUIDrawRect` shall obtain a Cairo drawing context (`cairo_t`) from the target window or device context and perform the corresponding Cairo operations (`cairo_move_to`, `cairo_line_to`, `cairo_rectangle`, `cairo_stroke`, `cairo_fill`).
*   Text drawing shall use Pango within Cairo (`pango_cairo_show_layout`).
*   The library shall handle coordinate system translations between Open Watcom's client-area-relative coordinates and GTK/Cairo's coordinate space.

##### 3.2.7 Menu, Toolbar, and Status Bar (FR-07)
**Description:** The library must support the creation of menu bars, toolbars, and status bars.
**Requirement:**
*   **Menus:** Shall create a `GtkMenuBar` and `GtkMenuItem` hierarchy. Selection shall generate `WM_COMMAND` messages.
*   **Toolbars:** Shall create a `GtkToolbar` with `GtkToolButton` items. Button clicks shall generate `WM_COMMAND` messages.
*   **Status Bar:** Shall create a `GtkStatusbar` widget. The `GUIStatusText` function shall push messages to the status bar's context ID.

#### 3.3 Non-Functional Requirements

##### 3.3.1 Portability (NFR-01)
**Description:** The library source code must be compilable on a standard Linux distribution.
**Requirement:** The library shall compile without modification using GCC or a compatible ANSI C compiler on a system with the X11 and GTK+ 2.x development headers installed.

##### 3.3.2 Linkage Flexibility (NFR-02)
**Description:** The library must support different linkage methods.
**Requirement:** The build system shall produce both a shared object (`libwgui_gtk.so`) and a static archive (`libwgui_gtk.a`). The static archive shall contain all necessary logic to allow linking on a system with incompatible or missing GTK+ libraries, acknowledging that this will increase the final application binary size.

##### 3.3.3 Functional Equivalence (NFR-03)
**Description:** The behavior of the ported library should match the original as closely as possible within the constraints of GTK+.
**Requirement:** The visual appearance and interactive behavior of windows, dialogs, and controls shall be functionally equivalent to the original library, presenting a native GTK/Linux look and feel. Behavioral differences arising from platform conventions (e.g., dialog button order) are acceptable.

##### 3.3.4 Performance (NFR-04)
**Description:** The library should not introduce significant performance degradation.
**Requirement:** The library's event translation and drawing operations shall not cause perceptible lag in typical Open Watcom application usage (e.g., IDE text editing, dialog navigation). Performance is secondary to correctness and compatibility.

#### 3.4 System Features
*(This section is often used to group related functional requirements. It is omitted here as the FRs above are already logically grouped.)*

### 4. Verification and Acceptance

#### 4.1 Acceptance Criteria
The port will be considered acceptable when the following conditions are met:
1.  The library successfully compiles on a reference Linux system (e.g., a recent Fedora or Ubuntu LTS) with the required dependencies.
2.  A suite of standard Open Watcom GUI sample applications (e.g., `simple`, `dialog`, `controls`, `menu`) can be compiled and linked against the new library.
3.  These sample applications execute without crashing and demonstrate correct functionality for:
    *   Creating and closing multiple windows.
    *   Displaying and interacting with modal/modeless dialog boxes.
    *   Correct operation of all implemented control types (button clicks, text entry, list selection).
    *   Proper rendering of text and basic graphics.
    *   Functioning menus, toolbars, and status bars.
4.  The applications integrate with the Linux desktop (appear in the taskbar/window list, respond to window manager controls).

#### 4.2 Testing Approach
*   **Unit Testing:** Critical internal modules (e.g., message translation, coordinate mapping) should be unit tested.
*   **Integration Testing:** The library will be tested by linking and running the existing Open Watcom GUI sample suite.
*   **System Testing:** Key Open Watcom tools (e.g., the IDE prototype) will be used for broader system-level validation.

### 5. Appendices

#### Appendix A: Excluded Functionality
The following items are explicitly excluded from this port due to fundamental incompatibilities with the GTK+/X11 architecture:
*   **Windows/OS2 Resource File Support:** The library will not parse `.rc` or `.res` files. Applications must create their UI procedurally via API calls.
*   **MDI Framework:** The library will not support the MDI window management model. Applications requiring MDI will need to manage child windows as independent top-level windows.
*   **Window System Menu Modification:** The library cannot add, remove, or modify items in the window manager's system menu (the menu provided by the desktop environment's title bar).

#### Appendix B: Dependencies
*   **GTK+:** Version >= 2.24.0 (or a widely available stable 2.x series).
*   **GLib, Pango, ATK, Cairo:** Corresponding versions as required by the GTK+ dependency.
*   **X Window System:** X11 protocol, libX11.
*   **Open Watcom Libraries:** WPI (Open Watcom Programming Interface) and TrMem (Memory Tracker) libraries must be present for linking the final application.