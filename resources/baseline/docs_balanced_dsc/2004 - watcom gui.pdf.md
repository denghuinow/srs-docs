# Software Requirements Specification (SRS)
## Open Watcom Linux GUI Port

**Document Version:** 1.0
**Date:** [Current Date]
**Project:** Open Watcom GUI Library Port to Linux/GTK
**Sponsor:** SciTech Software, Inc.
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the requirements for the port of the low-level Open Watcom GUI library to the Linux platform using the GTK+ toolkit. The purpose is to provide a comprehensive guide for developers, ensuring the ported library enables existing Open Watcom GUI applications to run natively on Linux with a consistent and maintainable architecture.

#### 1.2 Document Conventions
*   **Bold text** is used for key terms and section references.
*   `Monospaced text` is used for code, function names, data types, and file names.
*   Requirements are uniquely identified as **FR** (Functional) or **NFR** (Non-Functional) followed by a numeric ID.
*   This document is formatted in Markdown for clarity and version control compatibility.

#### 1.3 Intended Audience and Reading Suggestions
*   **Open Watcom Developers:** Focus on Sections 2 (Overall Description), 3 (Specific Requirements), and 5 (External Interface Requirements).
*   **Project Sponsors & Managers:** Focus on Sections 1 (Introduction), 2.1 (Product Perspective), 2.5 (Constraints), and 6 (Non-Functional Requirements).
*   **Linux Application Developers:** Focus on Sections 2.2 (Product Functions), 3.3 (System Features), and 4 (Data Requirements).
*   **Quality Assurance Engineers:** Focus on Sections 3 (Specific Requirements) and 6 (Non-Functional Requirements) to derive test cases.

#### 1.4 Project Scope
This project encompasses the adaptation of the Open Watcom GUI library's API to utilize the GTK+ 2.x toolkit on the X Window System. The scope includes:
*   Mapping Windows/OS/2 GUI function calls to their GTK equivalents.
*   Designing and implementing a strategy for handling Windows-style resources (`.rc`, `.res` files).
*   Creating a native-looking interface that respects Linux desktop conventions.
*   Providing a library that can be linked both statically and dynamically.

The project explicitly **excludes**:
*   Porting the entire Open Watcom compiler suite.
*   Modifying the source code of existing Open Watcom applications.
*   Supporting GUI toolkits other than GTK+ for this port.
*   Emulating Windows-specific features with no logical Linux equivalent (e.g., direct registry access).

### 2. Overall Description

#### 2.1 Product Perspective
The ported GUI library is a component within the larger Open Watcom development suite. It acts as a compatibility layer, intercepting calls from applications written for the original Open Watcom GUI API and translating them into GTK+ operations. This positions the library as a system-level dependency for any Open Watcom GUI application targeted for Linux.

#### 2.2 Product Functions
The core functions of the ported library are:
1.  **Initialization & Termination:** Bootstrap the GTK environment and manage the main event loop.
2.  **Window Management:** Create, destroy, show, hide, and manage top-level and child windows.
3.  **Dialog Management:** Create modal and modeless dialogs from template definitions.
4.  **Control Management:** Instantiate and manage standard GUI controls (buttons, edit boxes, list boxes, etc.).
5.  **Event Handling:** Translate GTK signals (mouse, keyboard, paint) into the Open Watcom event callback model.
6.  **Graphical Output:** Provide functions for drawing text, lines, rectangles, and other primitives.
7.  **Resource Handling:** Load and interpret Windows/OS/2 resource data for use in the GTK environment.
8.  **Menu Management:** Create and manage menu bars, pop-up menus, and menu items.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Open Watcom Developer** | Expert in existing library internals, C programming. | Clear porting strategy, maintainable code, API compatibility. |
| **Linux Application Developer** | May be new to Open Watcom, wants to target Linux. | Easy compilation, native look-and-feel, clear documentation. |
| **Project Sponsor (SciTech)** | Manages project resources and strategic direction. | Accurate effort estimation, risk assessment, milestone tracking. |
| **End User** | Uses the final ported applications on a Linux desktop. | Application stability, familiar UI behavior, integration with desktop. |

#### 2.4 Operating Environment
*   **Software:** Linux-based operating systems (e.g., Ubuntu, Fedora, Debian). GTK+ 2.x development libraries, Pango, GLib. X Window System.
*   **Hardware:** Standard PC architecture compatible with Linux and X11.
*   **Development Tools:** GNU Compiler Collection (GCC), GNU Make, `pkg-config`, standard system linker.

#### 2.5 Design and Implementation Constraints
1.  **API Compatibility Constraint:** The library's public API must remain source-code compatible with the original Open Watcom GUI library.
2.  **Toolkit Constraint:** The implementation must be based on GTK+ 2.x, not GTK 3 or 4, for broader system compatibility.
3.  **License Constraint:** All code must conform to the Open Watcom license agreement.
4.  **Portability Constraint:** The library should not rely on distribution-specific features.

#### 2.6 User Documentation
Comprehensive documentation shall be produced, including:
*   API reference for the ported functions.
*   A porting guide for developers migrating applications.
*   Build instructions for the library itself.
*   Notes on known limitations and differences from the Windows/OS/2 behavior.

#### 2.7 Assumptions and Dependencies
*   **Assumption:** Application source code uses the standard Open Watcom GUI API and does not rely on undocumented behavior.
*   **Assumption:** Target Linux systems have a functional X server and GTK+ 2.x runtime installed.
*   **Dependency:** Successful porting is dependent on the stability and features of the GTK+ 2.x libraries.

### 3. System Features

#### 3.1 Feature: Library Initialization and Core Management
**FR-1:** The library shall initialize the GTK environment (`gtk_init`) and establish a main event loop upon the first GUI API call from the application.
**FR-2:** The library shall provide a cleanup function that properly destroys all GTK objects and terminates the GUI subsystem.

#### 3.2 Feature: Window System
**FR-3:** The library shall create a GTK window (`GtkWindow`) wrapped with a container hierarchy (`GtkVBox`, `GtkScrolledWindow`, `GtkViewport`, `GtkFixed`) to support absolute positioning of child controls.
**FR-4:** The library shall map Open Watcom window styles (e.g., `WS_VISIBLE`, `WS_BORDER`) to appropriate GTK window properties and decorations.
**FR-5:** The library shall manage a list of created windows and their associated callback functions.

#### 3.3 Feature: Dialog and Control Management
**FR-6:** The library shall create dialog boxes from in-memory template structures, translating each defined control (BUTTON, EDIT, LISTBOX, etc.) into its corresponding GTK widget (`GtkButton`, `GtkEntry`, `GtkTreeView`).
**FR-7:** The library shall assign a unique integer ID to each control, storing the mapping between this ID and the underlying `GtkWidget*` pointer.
**FR-8:** The library shall implement functions to show, hide, enable, disable, resize, and move controls via their integer IDs.

#### 3.4 Feature: Event Handling
**FR-9:** The library shall connect GTK signal handlers (e.g., "clicked", "key-press-event", "expose-event") to the relevant GTK widgets.
**FR-10:** The library shall translate GTK signal data into a generic Open Watcom `gui_event` structure and invoke the application-registered callback function for the affected window or control.

#### 3.5 Feature: Drawing and Fonts
**FR-11:** The library shall handle "paint" events by providing a drawing context and translating calls like `DrawText`, `DrawLine`, and `DrawRect` to Cairo operations via GTK's drawing area.
**FR-12:** The library shall use Pango for text rendering, mapping Open Watcom font requests (family, size, weight) to `PangoFontDescription` objects.

#### 3.6 Feature: Resource File Handling
**FR-13:** The library shall include a utility or runtime layer to parse Windows/OS/2 resource files (`.rc`/`.res`) to extract dialog templates, menus, and string tables.
**FR-14:** The library shall, at a minimum, support loading dialog templates from a converted XML format (e.g., for use with libglade) as a primary or fallback strategy.

#### 3.7 Feature: Menu System
**FR-15:** The library shall create menu bars (`GtkMenuBar`), menu items (`GtkMenuItem`), and pop-up menus (`GtkMenu`) from resource data or procedural API calls.
**FR-16:** The library shall trigger the appropriate application callback when a menu item is selected, passing the item's integer ID.

### 4. Data Requirements

#### 4.1 Internal Data Structures
The library will maintain the following core internal structures:

```c
typedef struct {
    GtkWidget*      window_handle;      /* Primary Key: GTK top-level window */
    void*           parent;             /* Pointer to parent window struct */
    gui_event_callback* event_callback; /* Application event handler */
    GList*          control_list;       /* List of gui_control in this window */
    GtkWidget*      menu_bar;           /* Attached menu bar widget */
    GtkWidget*      status_bar;         /* Attached status bar widget */
    /* ... other window state ... */
} gui_window;

typedef struct {
    int             control_id;         /* Primary Key: Application's ID */
    int             type;               /* BUTTON, EDIT, LIST, etc. */
    GtkWidget*      widget;             /* Pointer to the GTK widget */
    gui_window*     parent_window;      /* Back-reference to owning window */
    char*           text;               /* Control text/label */
    gui_rect        rectangle;          /* Position and size */
} gui_control;
```

#### 4.2 Resource Data
*   **Dialog Templates:** Stored in memory as arrays of control definitions, translatable to GTK widget creation sequences.
*   **Menu Structures:** Represented as hierarchical node structures containing item text, command IDs, and submenu pointers.
*   **String Tables:** Key-value pairs mapping string IDs to text, intended for integration with the `gettext` system for internationalization.

### 5. External Interface Requirements

#### 5.1 User Interfaces
The library itself has no direct user interface. Applications using the library will present UIs that must:
*   Adhere to Linux desktop conventions (window manager decorations, menu placement).
*   Respect the user's selected GTK theme for colors, widgets, and fonts.

#### 5.2 Hardware Interfaces
Indirect interface via the X Window System. The library requires a display server supporting the X11 protocol.

#### 5.3 Software Interfaces
*   **GTK+ 2.x:** Primary toolkit for all GUI operations.
*   **Pango:** For advanced text layout and font handling.
*   **GLib:** For core data structures, memory management, and the main event loop.
*   **Xlib:** Low-level access (via GTK) for display and input.
*   **Standard C Library:** For file I/O and basic runtime functions.

#### 5.4 Communications Interfaces
Not applicable for this library component.

### 6. Non-Functional Requirements

#### 6.1 Performance Requirements
**NFR-1:** The library shall introduce no perceivable input lag for standard user interactions (button clicks, typing) in typical tool/IDE applications.
**NFR-2:** Drawing operations for standard dialogs shall complete within 1/60th of a second (one frame at 60Hz) to prevent visible flicker.

#### 6.2 Safety Requirements
**NFR-3:** The library shall not cause segmentation faults or undefined behavior when presented with invalid parameters from the application; it shall return an appropriate error code.

#### 6.3 Security Requirements
**NFR-4:** The library shall not introduce security vulnerabilities such as buffer overflows in its internal string handling or data structure management.

#### 6.4 Software Quality Attributes
*   **Maintainability:** The code shall be modular, with clear separation between the API layer, the GTK mapping layer, and the resource handling layer.
*   **Portability:** The source code shall compile without modification on major Linux distributions and adhere to ANSI C standards where possible.
*   **Compatibility:** **NFR-5:** The library shall maintain functional API compatibility with the original Open Watcom GUI library, allowing existing applications to recompile and run with minimal source changes.
*   **Reliability:** **NFR-6:** The library shall manage GTK object lifetimes correctly, ensuring all widgets are properly referenced and destroyed to prevent memory leaks.

### 7. Appendices

#### 7.1 Glossary
*   **API:** Application Programming Interface.
*   **GTK:** GIMP Toolkit, a widget toolkit for creating graphical user interfaces.
*   **MDI:** Multiple Document Interface.
*   **Pango:** A library for internationalized text layout and rendering.
*   **Widget:** A graphical user interface element (e.g., button, window).

#### 7.2 Analysis Models
*   **Event Flow Model:** Application -> Open Watcom API Call -> Library GTK Mapping -> GTK Signal -> Library Event Translation -> Application Callback.
*   **Window Hierarchy Model:** GTK Window -> VBox -> (Optional ScrolledWindow) -> Viewport -> Fixed Container -> Child Controls.

#### 7.3 Issues List (Undecided/To Be Resolved)
1.  **String Table Strategy:** Finalize the design for integrating Windows string resources with Linux `gettext` (.po files).
2.  **Widget ID Management:** Determine the optimal global data structure for mapping integer control IDs to `GtkWidget*` pointers across all windows.
3.  **Dialog Template Implementation:** Choose between runtime translation of binary templates or mandatory pre-compilation to an XML intermediate format.
4.  **System Menu:** Decide if the GTK window's system menu should be modified to mimic Windows-style options (Restore, Move, Size, etc.).
5.  **Memory Allocation:** Specify whether to use Open Watcom's internal memory routines or standard `malloc/free` for GTK-related structures.
6.  **Advanced Feature Scope:** Define the process for handling API functions deemed low-priority or non-essential for the initial stable release.