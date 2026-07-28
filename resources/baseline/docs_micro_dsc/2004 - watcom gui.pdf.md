# Software Requirements Specification (SRS)
## Port of Open Watcom GUI Library to Linux/GTK

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the requirements for a project to port the low-level Open Watcom GUI library from its native Windows/OS2 environment to the Linux operating system, utilizing the GTK toolkit for the X Window System. The primary audience for this document includes software architects, developers, testers, and project managers involved in the porting effort.

#### 1.2 Scope
The scope of this project is to create a functional, source-level compatible implementation of the core Open Watcom GUI API that allows existing applications built with this library to be recompiled and run on Linux/X11 with minimal source code changes. The port will map library calls to their GTK+ 3 equivalents, providing a similar look, feel, and programmatic behavior.

**In-Scope:**
*   Re-implementation of the core GUI API functions for window, dialog, and control management.
*   Mapping of drawing, text, input, and event-handling primitives to GTK.
*   Provision of build system (e.g., CMake, Make) for Linux.
*   Documentation of API differences and porting guide for application developers.

**Out-of-Scope:**
*   Modification of the original Open Watcom library source code for other platforms.
*   Porting of high-level frameworks or IDE components that may sit atop the GUI library.
*   Support for GTK versions other than the specified stable GTK+ 3.x.
*   Emulation of the Multiple Document Interface (MDI) "Windows in Window" model.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **API:** Application Programming Interface.
*   **GTK:** GIMP Toolkit, a widget toolkit for creating graphical user interfaces.
*   **GLib, Pango, ATK:** Core libraries supporting GTK (general-purpose utility, text rendering, and accessibility toolkits).
*   **MDI:** Multiple Document Interface.
*   **SRS:** Software Requirements Specification.
*   **UI:** User Interface.
*   **X11/X Window System:** The windowing system for bitmap displays, common on Unix-like operating systems.
*   **Open Watcom GUI:** The specific graphical user interface library provided by the Open Watcom compiler suite.

#### 1.4 References
*   Open Watcom Public License.
*   Open Watcom GUI Library API Documentation.
*   GTK+ 3 Reference Manual.
*   X Window System Protocol.

#### 1.5 Overview
The remainder of this document describes the overall description of the product (Section 2) and the specific requirements (Section 3). It details functional capabilities, constraints, and interfaces.

---

### 2. Overall Description

#### 2.1 Product Perspective
This port is a compatibility layer. It sits between existing Open Watcom GUI applications and the native Linux graphical environment. The system architecture is as follows:

```
[Recompiled Open Watcom Application]
            |
            | (Calls Open Watcom GUI API)
            |
    [Port Library (libowgui-gtk.so)]
            |
            | (Maps calls to GTK/GLib/X11)
            |
    [GTK+ 3, GLib, Pango, ATK]
            |
            | (X11 Protocol)
            |
    [X Server / Linux Desktop]
```

The port must maintain the same header files (`*.h`) as the original library to ensure source compatibility.

#### 2.2 Product Functions
The core functions of the ported library are:
1.  **Initialization & Event Loop:** Initialize the GTK toolkit and manage the main application event loop.
2.  **Window Management:** Create, destroy, show, hide, move, resize, and manage parent/child relationships for top-level windows and dialogs.
3.  **Control Management:** Create and manage standard UI controls (e.g., buttons, static text, edit boxes, list boxes, combo boxes, menus, scrollbars).
4.  **Graphical Operations:** Provide a device context (DC) abstraction for drawing lines, rectangles, text, and basic bitmaps.
5.  **Input Handling:** Process mouse and keyboard events, translating them into the library's expected message/event format.
6.  **Resource Abstraction:** Provide an alternative mechanism to load dialog layouts and string tables, replacing Windows/OS2 resource files.

#### 2.3 User Characteristics
The end-users are **software developers** who have existing source code for applications built with the Open Watcom GUI library. They are expected to have:
*   Knowledge of C programming.
*   Familiarity with the original Open Watcom GUI API.
*   Basic understanding of Linux development environments.

#### 2.4 Constraints
1.  **Technical Constraints:**
    *   The target system **must** have GTK+ 3 development libraries and their dependencies (GLib, Pango, ATK, etc.) installed.
    *   The library **cannot** depend on or parse Windows/OS2-style binary resource (`.res`, `.rc`) files.
    *   The MDI ("Windows in Window") model present in the original API **cannot** be implemented; affected functions must return a defined error code or no-op gracefully.
    *   The port must be compatible with a standard Linux linking and runtime model (e.g., ELF binaries, shared libraries).

2.  **Business Rules:** The implementation must be under an open-source license compatible with the Open Watcom Public License.

#### 2.5 Assumptions and Dependencies
*   It is assumed that the application's business logic is separate from the GUI code, making the port feasible.
*   The project's success depends on the accuracy and completeness of the original Open Watcom GUI API documentation.
*   The library depends on the continued stability of the GTK+ 3 API for the lifespan of the port.

---

### 3. Specific Requirements

#### 3.1 External Interface Requirements

**3.1.1 User Interfaces**
The library does not define a user interface itself but enables applications to create UIs. The created UIs will have the visual appearance of the current system GTK+ 3 theme.

**3.1.2 Hardware Interfaces**
*   Input: Standard keyboard and pointing device (mouse).
*   Output: Any display supported by the X Window System and the GTK+ toolkit.

**3.1.3 Software Interfaces**
*   **GTK+ 3.x:** Primary toolkit for widget creation and event management.
*   **GLib 2.x:** Required for core data structures, main loop, and utilities.
*   **Pango:** Used for all text rendering and font handling.
*   **Xlib or XCB (via GDK):** For low-level X11 display interaction (handled internally by GTK).
*   **Linux System Libraries:** `libc`, `libm`, `libpthread`.

**3.1.4 Communications Interfaces**
Not applicable.

#### 3.2 Functional Requirements

**3.2.1 Library Initialization and Control (FR-01)**
*   **FR-01.1:** The function `GUIInitialize()` must initialize the GTK toolkit and prepare the internal state of the library.
*   **FR-01.2:** The function `GUIMainLoop()` must start and manage the GTK main event loop, dispatching events to appropriate windows.
*   **FR-01.3:** The function `GUIYield()` must process pending GTK events without blocking.

**3.2.2 Window and Dialog Management (FR-02)**
*   **FR-02.1:** Functions `GUICreateWindow()`, `GUIShowWindow()`, `GUIMoveWindow()`, `GUIResizeWindow()`, and `GUIDestroyWindow()` must create and manage GTK windows with equivalent properties.
*   **FR-02.2:** Modal and modeless dialog creation functions must map to GTK dialog constructs (`GtkDialog`, `GtkMessageDialog`).
*   **FR-02.3:** **Constraint Implementation:** Dialog layouts must be constructed procedurally in code or loaded from an alternative format (e.g., XML defined by GTKBuilder), as binary resource files are not supported.

**3.2.3 Control Management (FR-03)**
*   **FR-03.1:** The library must provide functions to create standard controls: `GUIButton`, `GUIStatic`, `GUIEdit`, `GUIListBox`, `GUIComboBox`, `GUIMenu`.
*   **FR-03.2:** Controls must be parented correctly within windows/dialogs, maintaining the hierarchical z-order.
*   **FR-03.3:** Control styles (e.g., push button, checkbox, radio button) must be correctly mapped to GTK widget types.

**3.2.4 Drawing and Text Rendering (FR-04)**
*   **FR-04.1:** Functions for obtaining a Device Context (DC) for a window or control must return a structure that can be used with GTK's Cairo-based drawing.
*   **FR-04.2:** Drawing primitives (`LineTo`, `Rectangle`, `Ellipse`) must be implemented using Cairo drawing operations.
*   **FR-04.3:** Text output functions (`TextOut`, `DrawText`) must use Pango for layout and rendering, respecting provided font and color attributes.

**3.2.5 Input and Event Handling (FR-05)**
*   **FR-05.1:** Mouse events (move, click, scroll) must be captured from GTK signals and translated into the library's internal message queue or callback mechanism.
*   **FR-05.2:** Keyboard events must be processed, providing character and keycode information consistent with the original API's expectations.

**3.2.6 Resource and String Management (FR-06)**
*   **FR-06.1:** **Constraint Implementation:** Functions to load dialogs from resources must be re-implemented to load from an alternative source (e.g., embedded data, external XML files).
*   **FR-06.2:** **Constraint Implementation:** String table APIs must load strings from a plain-text format (e.g., `.po` files, JSON, custom text format) instead of binary resource tables.

**3.2.7 Non-Functional Requirements**

**3.2.7.1 Performance Requirements**
*   The library shall not introduce significant latency in UI responsiveness compared to a native GTK application performing similar operations.

**3.2.7.2 Safety & Security Requirements**
*   The library shall perform bounds checking and validate parameters to prevent crashes due to invalid input from the application, where feasible.

**3.2.8 Design Constraints**
*   The code shall be written in C (C99 standard).
*   The build system shall generate a shared library (e.g., `libowgui-gtk.so`).

#### 3.3 System Features
*(This section would typically list and cross-reference the Functional Requirements (FR-01 to FR-06) with use cases or scenarios. For brevity, it is noted that all FRs above constitute the system's features.)*

---

### 4. Appendices

#### 4.1 API Compatibility Matrix
*(To be completed during design phase. Will list original Open Watcom GUI functions and their implementation status in the port: "Fully Implemented", "Partially Implemented (Differences Noted)", "Not Implemented (Due to Constraint)", "N/A".)*

**Example:**
| Original Function | Port Status | Notes |
| :--- | :--- | :--- |
| `GUICreateMDIWindow()` | Not Implemented | MDI constraint. Returns `NULL`. |
| `GUILoadDialog()` | Partially Implemented | Loads from GTKBuilder XML, not `.res` file. |
| `GUITextOut()` | Fully Implemented | Uses Pango/Cairo. |

#### 4.2 Alternative Resource Format Specification
*(To be completed during design phase. Will specify the chosen format for dialog layouts and string tables, e.g., GTKBuilder XML schema for dialogs and a simple key-value text format for strings.)*

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Manager | | | |
| Lead Architect | | | |
| Quality Assurance | | | |