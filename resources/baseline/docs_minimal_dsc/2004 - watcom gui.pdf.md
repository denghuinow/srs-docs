# Software Requirements Specification (SRS)
## Open Watcom GUI Library Port for Linux (GTK+)

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the requirements for porting the low-level Open Watcom GUI library to the Linux platform. The port will utilize the GTK+ toolkit for the X Window System, enabling legacy Open Watcom applications to execute on modern Linux distributions with a native graphical user interface. This document is intended for project stakeholders, developers, and quality assurance personnel.

#### 1.2 Scope
The scope of this project encompasses the development of a shared library (`libgui.so`) that provides a functional equivalent to the original Open Watcom GUI API, but implemented using GTK+ 3.x on X11. The library will allow unmodified Open Watcom application binaries (or those recompiled with the Open Watcom toolchain for Linux) to create windows, dialogs, menus, and perform basic drawing operations.

**In-Scope:**
*   Implementation of core GUI initialization and event loop management.
*   Emulation of window, dialog, and basic control creation (buttons, labels, edit boxes, listboxes).
*   Support for basic user interaction events (clicks, key presses).
*   Implementation of fundamental Graphics Device Interface (GDI) operations for drawing lines, rectangles, text, and bitmaps.
*   Provision of an alternative mechanism to Windows/OS/2 resource files for defining dialog layouts and string tables.

**Out-of-Scope:**
*   Porting the entire Open Watcom toolchain or compiler.
*   Support for GTK+ 4 or Wayland display servers (target is GTK+ 3 on X11).
*   Emulation of complex Windows-specific controls or Common Controls (TreeView, Tab control, etc.) beyond the basic set.
*   Direct execution of Windows/OS/2 binary resource (`.res`, `.dlg`) files.
*   Implementation of the Multiple Document Interface (MDI) "window-in-window" model.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **API:** Application Programming Interface.
*   **GDI:** Graphics Device Interface (the drawing API in Windows/OS/2).
*   **GLib:** Low-level core library for GTK+.
*   **GTK+:** GIMP Toolkit, a widget toolkit for creating graphical user interfaces.
*   **MDI:** Multiple Document Interface.
*   **Pango:** A library for layout and rendering of text.
*   **SRS:** Software Requirements Specification.
*   **X11 / X Window System:** The windowing system for bitmap displays, common on Unix-like operating systems.
*   **OW:** Open Watcom.

#### 1.4 References
*   Open Watcom Public License.
*   GTK+ 3 Reference Manual.
*   Original Open Watcom GUI Library Documentation.

#### 1.5 Overview
The remainder of this document describes the overall description of the product (Section 2) and the specific requirements (Section 3). It details functional requirements, user interfaces, constraints, and system dependencies.

---

### 2. Overall Description

#### 2.1 Product Perspective
This port is a compatibility layer. It sits between legacy Open Watcom applications and the modern Linux graphical stack. The application calls the original Open Watcom GUI API, which is implemented by this new library using GTK+ primitives.

```
[Open Watcom Application] -> [OW GUI API Calls] -> [libgui.so (This Port)] -> [GTK+/X11] -> [Linux Display]
```

#### 2.2 Product Functions
The core functions of the library are:
1.  **Initialization & Core:** Initialize the GTK+ environment and manage the main event loop.
2.  **Window Management:** Create, destroy, show, hide, and manage top-level windows and modal/modeless dialogs.
3.  **Control Management:** Create and manage basic child controls (e.g., `STATIC`, `BUTTON`, `EDIT`, `LISTBOX`).
4.  **Event Handling:** Translate GTK+ signals (e.g., "clicked", "key-press-event") into the equivalent Open Watcom GUI event messages and deliver them to the application's window procedure.
5.  **Drawing Operations:** Implement a subset of GDI functions for drawing lines, rectangles, ellipses, text, and bitmaps onto window surfaces using Cairo (GTK+'s drawing library).
6.  **Resource Abstraction:** Provide a runtime method for applications to define dialog templates and string resources without using binary resource files.

#### 2.3 User Characteristics
The primary user of this system is a **Developer** who:
*   Uses the Open Watcom toolchain (compiler, linker) for Linux.
*   Maintains or develops applications originally targeted for 16-bit or 32-bit Windows or OS/2.
*   Has knowledge of C programming and the Open Watcom GUI API.
*   Requires the ability to run or test these applications on a Linux system without a full Windows emulator.

#### 2.4 Constraints
1.  **Resource File Incompatibility:** The system **shall not** use or parse Windows/OS/2 binary resource files (`.res`, `.rc`). An alternative, platform-native method (e.g., structured text files like JSON or XML, or runtime API calls) **must** be provided.
2.  **MDI Limitation:** Due to GTK+ lacking native support for the MDI paradigm, the library **shall** implement MDI parent windows as a standard window containing a simplified tabbed or tiled interface. Child MDI windows will be represented as independent top-level windows managed by the library. A clear mapping strategy must be documented.
3.  **System Dependencies:** The target runtime environment **must** have the following libraries installed:
    *   GTK+ 3.x
    *   GLib 2.x
    *   Pango 1.x
    *   X Window System libraries (X11)
    *   Cairo graphics library

#### 2.5 Assumptions and Dependencies
*   It is assumed the Open Watcom Linux toolchain is already installed and functional on the developer's system.
*   The success of the port depends on the accuracy and completeness of the original Open Watcom GUI API documentation.
*   Applications using only the defined subset of GUI functions will have the highest compatibility.

---

### 3. Specific Requirements

#### 3.1 External Interface Requirements

**3.1.1 User Interfaces**
The library itself has no direct user interface. It enables applications to present a native GTK+ interface. The appearance of windows, dialogs, and controls will conform to the current GTK+ theme active on the user's Linux desktop.

**3.1.2 Hardware Interfaces**
None. All interaction is through the X Window System.

**3.1.3 Software Interfaces**
*   **GTK+ 3.0 API:** The library shall link against and use GTK+ 3.x for all widget creation and management.
*   **Cairo API:** The library shall use Cairo for all drawing (GDI) operations.
*   **Open Watcom GUI API:** The library shall expose the standard Open Watcom GUI function signatures (e.g., `GUIInitialize`, `GUICreateWindow`, `GUIDrawText`).

**3.1.4 Communications Interfaces**
None required.

#### 3.2 Functional Requirements

**3.2.1 FR-001: Library Initialization and Event Loop**
*   **Description:** The library must initialize the GTK+ environment and manage the main event loop.
*   **Inputs:** Application startup call to `GUIInitialize`.
*   **Processing:** Register necessary GTK+ types, set up internationalization, prepare internal data structures.
*   **Outputs:** A running GTK+ main loop (`gtk_main()`) that processes events and dispatches them to the appropriate application windows.

**3.2.2 FR-002: Window Creation and Management**
*   **Description:** Create and manage top-level application windows and dialog windows.
*   **Inputs:** Parameters from `GUICreateWindow` (window style, position, size, parent handle, etc.).
*   **Processing:** Map Open Watcom window styles to GTK+ `GtkWindow` properties. Create a `GtkWindow` (or `GtkDialog`) and manage its lifecycle.
*   **Outputs:** A valid window handle (`HWND` equivalent) returned to the application. The window must respond to minimize, maximize, and close events.

**3.2.3 FR-003: Dialog and Control Creation**
*   **Description:** Create dialog boxes and child controls based on a dialog template.
*   **Inputs:** A dialog template definition (via the alternative resource method) or individual control creation calls.
*   **Processing:** Parse the template, create corresponding GTK+ widgets (`GtkButton`, `GtkLabel`, `GtkEntry`, `GtkListBox`), position them, and set their initial properties.
*   **Outputs:** A functional dialog with child controls that can receive user input and generate events.

**3.2.4 FR-004: Event Handling and Message Pump**
*   **Description:** Translate GTK+ signals into Open Watcom GUI messages and deliver them to the application's window procedure.
*   **Inputs:** GTK+ signals (e.g., "destroy", "button-press-event", "key-press-event").
*   **Processing:** Map the GTK+ signal to an equivalent Open Watcom message (e.g., `WM_DESTROY`, `WM_LBUTTONDOWN`, `WM_CHAR`). Pack relevant data (coordinates, key codes) into the message structure. Call the application's registered window procedure.
*   **Outputs:** The application receives familiar message types, allowing its existing event logic to function.

**3.2.5 FR-005: Basic Drawing Operations**
*   **Description:** Provide a functional subset of GDI drawing operations.
*   **Inputs:** Drawing calls (e.g., `GUIDrawLine`, `GUIFillRect`, `GUIDrawText`) with parameters.
*   **Processing:** Use Cairo to perform the corresponding drawing operation on the target window's or device context's drawing area. Handle clipping regions, pens, brushes, and fonts.
*   **Outputs:** Visual output rendered to the application window.

**3.2.6 FR-006: Alternative Resource Mechanism**
*   **Description:** Provide a method for applications to define dialog layouts and string tables without `.res` files.
*   **Inputs:** Resource definitions in an alternative format (e.g., a JSON file named `resources.json`).
*   **Processing:** Library provides an API (e.g., `GUILoadResources(const char *json_path)`) to parse this file at runtime and register dialog templates and strings internally.
*   **Outputs:** Dialog templates and strings are available for use via standard Open Watcom resource APIs (e.g., `GUIDialogBox`).

#### 3.3 Non-Functional Requirements

**3.3.1 Performance Requirements**
*   The library shall introduce minimal overhead to event processing. Event delivery from GTK+ to the application should occur with negligible latency (< 5ms under normal load).
*   Drawing operations for simple shapes and text shall be performant enough for typical business applications.

**3.3.2 Safety and Security Requirements**
*   The library shall not introduce security vulnerabilities such as buffer overflows. Input from application data structures must be validated where appropriate.

**3.3.3 Portability Requirements**
*   The source code shall compile on major Linux distributions (Ubuntu LTS, Fedora, Debian Stable) that provide the required GTK+ 3.x libraries.

#### 3.4 System Features
*   **Feature: Native Look and Feel.** Windows and controls will appear as standard GTK+ widgets, integrating seamlessly with the user's desktop environment.
*   **Feature: Resource File Abstraction.** The alternative resource mechanism decouples the application from a proprietary binary format, easing maintenance and portability.
*   **Feature: MDI Fallback Mode.** While not a true MDI, the library provides a functional workaround that allows MDI-based applications to run, preserving core functionality even if the window management model differs.

---

### 4. Appendices

#### 4.1 API Mapping (Preliminary Examples)
| Open Watcom API | GTK+ Equivalent / Action |
| :--- | :--- |
| `GUIInitialize()` | `gtk_init()`, internal setup |
| `GUICreateWindow(...)` | `gtk_window_new(GTK_WINDOW_TOPLEVEL)` |
| `GUIDialogBox(...)` | Parse internal template, create `GtkDialog` |
| `GUIDrawText(hdc, text, ...)` | `cairo_move_to(); cairo_show_text()` |
| `Message Loop` | `gtk_main()` and signal handlers |

#### 4.2 Alternative Resource File Format (Example: JSON)
```json
{
  "string_table": {
    "IDS_GREETING": "Hello, World!",
    "IDS_ERROR": "An error occurred."
  },
  "dialogs": [
    {
      "id": "IDD_ABOUT",
      "title": "About This App",
      "width": 300,
      "height": 200,
      "controls": [
        { "type": "STATIC", "id": -1, "text": "My Application", "x": 10, "y": 10, "w": 280, "h": 20 },
        { "type": "BUTTON", "id": "IDOK", "text": "OK", "x": 110, "y": 160, "w": 80, "h": 25 }
      ]
    }
  ]
}
```