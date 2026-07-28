# Software Requirements Specification (SRS)
## Open Watcom Linux GUI Port

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review
**Project:** Open Watcom GUI Library Port to Linux/GTK+

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the port of the low-level Open Watcom GUI library to the Linux operating system using the GTK+ toolkit. The primary purpose is to enable existing Open Watcom applications to present a native graphical user interface on Linux platforms with minimal source code modification.

#### 1.2 Document Conventions
*   **Bold text** is used for key terms and interface names.
*   `Monospaced text` denotes code, function names, and file names.
*   Requirements are uniquely identified as `FR-XXX` (Functional) or `NFR-XXX` (Non-Functional).

#### 1.3 Intended Audience and Reading Suggestions
*   **Open Watcom Development Team:** For implementation and testing guidance.
*   **Project Managers & Technical Leads:** For planning and tracking.
*   **System Administrators & Package Maintainers:** For deployment considerations.
*   **Open Source Contributors:** For understanding project scope and contribution areas.

#### 1.4 Project Scope
This project encompasses the adaptation of the Open Watcom GUI library's API to utilize the GTK+ 2.x toolkit on the X Window System. The scope includes:
*   Mapping GUI primitives (windows, dialogs, controls) to GTK+ widgets.
*   Implementing the GUI event loop using GTK+'s main loop.
*   Providing mechanisms to handle Windows/OS/2 resource files (e.g., `.rc`).
*   Implementing core drawing functions using GTK+ and Pango.
*   Ensuring basic compatibility with common Linux distributions.

**Out of Scope:**
*   Modification of the core Open Watcom compiler, linker, or C runtime libraries.
*   Full replication of Windows-specific GUI features with no GTK+ equivalent (e.g., native Multiple Document Interface "windows in window" model).
*   Porting of non-GUI related Open Watcom libraries.

#### 1.5 References
*   Open Watcom Project Documentation
*   GTK+ 2.x API Reference
*   X Window System Protocol
*   LGPL v2.1 License

---

### 2. Overall Description

#### 2.1 Product Perspective
The ported GUI library is a component within the larger Open Watcom toolchain. It sits as an abstraction layer between existing Open Watcom applications and the native Linux GUI subsystem (GTK+/X11). It must integrate seamlessly with the existing Open Watcom core libraries (memory management, base types).

#### 2.2 Product Functions (High-Level)
1.  **Initialization:** Bootstrap the GTK+ environment upon application start.
2.  **Window Management:** Create, destroy, and manage top-level and child windows.
3.  **Control Rendering:** Display standard UI controls (buttons, edits, lists, etc.).
4.  **Event Handling:** Translate and route user input (mouse, keyboard) to application code.
5.  **Dialog Management:** Create modal and modeless dialogs from resource definitions.
6.  **Resource Support:** Interpret or convert binary/RC resource data for use on Linux.
7.  **2D Drawing:** Provide basic vector and text drawing capabilities on window surfaces.
8.  **Menu & Toolbar Support:** Render and manage menu bars, popup menus, and toolbars.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Goals |
| :--- | :--- | :--- |
| **Linux End-User** | Uses Open Watcom tools (IDE, debugger) for development. Expects a stable, native-looking GUI. May not be familiar with Windows API specifics. | Run Open Watcom GUI applications reliably on Linux. Have a consistent and predictable user experience. |
| **Open Watcom Developer** | Deep knowledge of the existing GUI library API and internals. Responsible for implementing the port. | Create a maintainable, efficient, and API-compatible port. Document limitations and differences. |
| **System Administrator** | Deploys software on multiple Linux workstations. Manages dependencies and system compatibility. | Easy installation and clear dependency management. Stability in a multi-user environment. |
| **Open Source Contributor** | Interested in improving open-source tools. May submit patches or review code. | Understand the codebase and design decisions to contribute effectively. |

#### 2.4 Operating Environment
*   **Software:** Linux kernel (v3.0+), X Window System, GTK+ library (v2.24+), Pango, GLib.
*   **Hardware:** Standard x86 or x86_64 systems with graphical display capabilities.
*   **Distributions:** Target compatibility with mainstream distributions (e.g., Ubuntu LTS, Fedora, Debian Stable).

#### 2.5 Design and Implementation Constraints
1.  **API Compatibility:** Must maintain source-level compatibility with the existing Open Watcom GUI API (`GUIX*` functions). Breaking changes are not permitted.
2.  **License Compliance:** The final product must comply with the Open Watcom license and the LGPL of GTK+. Static linking implications must be evaluated.
3.  **Platform Abstraction:** The implementation must isolate GTK+-specific code to facilitate potential future ports to other toolkits.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** Existing Open Watcom applications use the standard GUI API and do not rely on undocumented behavior.
*   **Assumption:** Target Linux systems have a functional X11/GTK+ desktop environment installed.
*   **Dependency:** Project success depends on the stability and features of the GTK+ 2.x API.

---

### 3. System Features and Requirements

#### 3.1 Feature: Library Initialization and Core Lifecycle
**Description:** The library must initialize the GTK+ environment and manage the application lifecycle.

| Requirement ID | Description | Priority |
| :--- | :--- | :--- |
| **FR-010** | The library shall initialize the GTK+ library (`gtk_init`) and necessary type systems when `GUIXMain()` is called by the application. | High |
| **FR-011** | The library shall start the GTK+ main event loop (`gtk_main`) to process events. | High |
| **FR-012** | The library shall provide a clean shutdown path, ensuring all GTK+ resources are freed upon application exit. | Medium |

#### 3.2 Feature: Window Management
**Description:** The library must support the creation and management of top-level windows.

| Requirement ID | Description | Priority |
| :--- | :--- | :--- |
| **FR-020** | The library shall create a GTK+ `GtkWindow` when the application calls `GUIXCreateWindow()`. | High |
| **FR-021** | The created window shall respect the requested title, size, and style flags (e.g., border, minimize/maximize buttons) as specified in the API call. | High |
| **FR-022** | The library shall handle window resize, move, minimize, maximize, and close events, translating them into appropriate internal messages for the application. | High |
| **FR-023** | The library shall support the creation of child windows (e.g., for controls) as `GtkFixed` containers within a top-level window. | High |

#### 3.3 Feature: Dialog and Control Management
**Description:** The library must create dialogs and populate them with standard controls.

| Requirement ID | Description | Priority |
| :--- | :--- | :--- |
| **FR-030** | The library shall create a dialog (`GtkDialog`) when `GUICreateDialog()` is called. | High |
| **FR-031** | The library shall support basic controls mapped to GTK+ widgets: Button (`GtkButton`), Static Text (`GtkLabel`), Edit Box (`GtkEntry`/`GtkTextView`), List Box (`GtkTreeView`), Combo Box (`GtkComboBox`). | High |
| **FR-032** | Control IDs specified in the resource file or API shall be uniquely mapped to GTK+ widget references for event routing. | High |
| **FR-033** | Modal dialog behavior shall be implemented using `gtk_dialog_run()` or equivalent. | Medium |
| **FR-034** | The library shall provide a mechanism (e.g., conversion tool or runtime parser) to translate Windows `.rc` dialog resource definitions into a format usable by GTK+ (e.g., Glade XML). | Medium |

#### 3.4 Feature: Event Handling
**Description:** User input and system events must be captured and delivered to the application.

| Requirement ID | Description | Priority |
| :--- | :--- | :--- |
| **FR-040** | The library shall connect GTK+ signal handlers (e.g., "clicked", "key-press-event") to corresponding widgets. | High |
| **FR-041** | GTK+ signals shall be translated into the internal `GUIEvent` structure expected by the Open Watcom application. | High |
| **FR-042** | The library shall manage the queueing and dispatching of events via the GTK+ main loop, ensuring the application remains responsive. | High |

#### 3.5 Feature: Drawing and Text Rendering
**Description:** Basic 2D drawing and text output functions must be supported.

| Requirement ID | Description | Priority |
| :--- | :--- | :--- |
| **FR-050** | The library shall provide a drawing context that maps to a GTK+ `GdkWindow` or Cairo surface. | High |
| **FR-051** | Functions like `GUIDrawText()` shall use the **Pango** library for text layout and rendering, respecting font metrics. | High |
| **FR-052** | Basic vector drawing (lines, rectangles, polygons) shall be implemented using Cairo or `GdkDrawing` primitives. | Medium |
| **FR-053** | Color (`GUIColor`) and font (`GUIFont`) specifications shall be translated to their GTK+/Pango equivalents. | Medium |

#### 3.6 Feature: Resource File Adaptation
**Description:** The library must handle application resources (strings, dialogs, bitmaps).

| Requirement ID | Description | Priority |
| :--- | :--- | :--- |
| **FR-060** | The library shall implement a fallback strategy for resource loading. If a native GTK+ resource (e.g., Glade XML) is not found, it shall attempt to load a Windows `.res` or `.rc` file. | Medium |
| **FR-061** | A standalone resource conversion tool (out of scope for the *library itself*, but part of the project) shall be provided to translate `.rc` files to Glade XML format. | Low |
| **FR-062** | String table resources shall be loadable and accessible via the standard API (`GUILoadString`). | Medium |

#### 3.7 Feature: Menu, Toolbar, and Status Bar
**Description:** Common application frame elements must be supported.

| Requirement ID | Description | Priority |
| :--- | :--- | :--- |
| **FR-070** | The library shall create a menu bar (`GtkMenuBar`) with nested menus (`GtkMenu`, `GtkMenuItem`) from resource definitions. | Medium |
| **FR-071** | The library shall support a basic toolbar (`GtkToolbar`) with button icons. | Low |
| **FR-072** | The library shall support a status bar (`GtkStatusbar`) at the bottom of a window. | Low |

---

### 4. External Interface Requirements

#### 4.1 User Interfaces
The library itself has no direct user interface. It enables Open Watcom applications to present a GUI that shall be native to the Linux desktop (GTK+ theme).

#### 4.2 Hardware Interfaces
Indirect interface via X Window System for display and input devices.

#### 4.3 Software Interfaces
| Interface | Direction | Purpose & Interaction | SLA / Constraints |
| :--- | :--- | :--- | :--- |
| **GTK+ 2.x API** | Inbound | Primary target for all widget creation, event handling, and drawing. The library calls GTK+ functions. | Must support version 2.24+. Runtime dependency. |
| **Xlib / X Server** | Indirect (via GTK+) | Low-level display and input. GTK+ abstracts this interaction. | Compatible with standard X11 implementations. |
| **Open Watcom Core Libs** | Inbound/Outbound | Provides foundational types and memory management. The GUI library links with and uses these libraries. | Must maintain binary and functional compatibility. |
| **Resource Converter Tool** | Outbound | Standalone tool to convert `.rc` resources into GTK+ builder XML. The library may load the output of this tool. | Must handle common dialog and control definitions. |

#### 4.4 Communications Interfaces
Not applicable.

---

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   **NFR-001:** A top-level window shall be created and made visible within **100 milliseconds** of the API call on standard hardware.
*   **NFR-002:** Simple drawing operations (e.g., redrawing a dialog) shall maintain an interactive feel, targeting a perceived latency of < 33ms (≥30 FPS) for basic UI updates.
*   **NFR-003:** Event processing latency (click to application handler) shall be less than **50ms**.

#### 5.2 Safety & Security Requirements
*   **NFR-010:** The library shall not introduce security vulnerabilities (e.g., buffer overflows). It shall leverage GTK+'s safe APIs for input and data handling.
*   **NFR-011:** The library shall handle malformed or missing resource files gracefully without crashing the host application.

#### 5.3 Software Quality Attributes
*   **Reliability:** The library shall not cause application crashes during normal operation of supported features. **Mean Time Between Failure (MTBF)** for the GUI subsystem should be high.
*   **Maintainability:** Code shall be modular, with clear separation between the abstract GUI API and the GTK+ implementation. Comprehensive internal documentation is required.
*   **Portability:** While targeting Linux/GTK+, the internal design should abstract platform specifics to aid future ports.
*   **Compatibility:** The library's public API shall be **source-code compatible** with the original Windows/OS2 version. Existing applications should recompile and run with minimal changes.
*   **Observability:** The library shall provide a debug mode, configurable at runtime, which logs significant events (initialization errors, unsupported feature calls) to `stderr` or a log file.

#### 5.4 Compliance Requirements
*   The final work must be distributable under the Open Watcom License.
*   All use of GTK+ and related libraries must comply with the **GNU Lesser General Public License (LGPL) v2.1**.
*   Distribution decisions (static vs. dynamic linking) must respect LGPL requirements.

---

### 6. Other Requirements

#### 6.1 Acceptance Criteria
*   **AC-1:** The Open Watcom IDE (a complex GUI application) can be compiled with the new library and launched on Linux. Its main window appears with correct title, menu bar, and basic controls.
*   **AC-2:** Buttons in a test dialog can be clicked, generating the correct event messages in the application.
*   **AC-3:** Text typed into an edit control can be retrieved programmatically via the `GUIGetControlText()` API.
*   **AC-4:** A simple application that uses `GUIDrawText()` and `GUIDrawLine()` functions displays correct output in a window.

#### 6.2 Development Constraints & Milestones
| Milestone | Deliverables | Estimated Effort |
| :--- | :--- | :--- |
| **M1: Foundation** | Library links and initializes GTK+. Basic blank window creation works. | 6 hours |
| **M2: Controls & Dialogs** | Dialog creation from code. Support for core controls (Button, Label, Edit). | 65 hours |
| **M3: Event System** | Full event handling loop. User interactions are delivered to application. | 27 hours |
| **M4: Drawing** | Implementation of core drawing and text rendering functions. | 24 hours |
| **M5: Polish** | Menu, toolbar, status bar support. Resource file loader/converter tool. | 65 hours |
| **Release** | Alpha release for community testing, followed by stable release after bug fixes. | - |

#### 6.3 Risks and Mitigations
| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| **GTK+ API mismatch** | High | Medium | Document limitations clearly. Implement pragmatic workarounds where possible. |
| **Resource conversion complexity** | Medium | High | Provide a basic converter and a fallback to runtime control creation, documenting the manual steps required for complex resources. |
| **MDI (Multiple Document Interface) unsupported** | High | Medium | Implement an alternative UI pattern (e.g., tabbed interface or separate top-level windows) and provide guidance for application adaptation. |
| **Performance overhead** | Medium | Low | Profile critical paths (window creation, drawing). Optimize the mapping layer. |
| **Insufficient testing** | Medium | High | Develop a suite of automated test applications. Enlist the community for broad beta testing on different distributions. |

#### 6.4 Open Issues and TBDs
1.  **Resource ID Mapping:** Final strategy for handling Windows numeric resource IDs vs. Linux string-based names. *(Owner: Open Watcom Team)*
2.  **MDI Alternative Design:** Decision on the recommended UI pattern to replace the unsupported native MDI model. *(Owner: Open Watcom Team)*
3.  **Help System:** Specification for how application help (`.hlp` files) should be integrated (e.g., convert to HTML and use `yelp`). *(Owner: Open Watcom Team)*
4.  **Accessibility (ATK):** Define the level of accessibility support required for the initial release. *(Owner: Open Watcom Team)*
5.  **Distribution Packaging:** Decision on dynamic vs. static linking of GTK+ for end-user distribution packages. *(Owner: System Administrators / Package Maintainers)*

---
**Document Approval:**

*   *Technical Lead Signature:* ___________________________ *Date:* _________
*   *Project Manager Signature:* ___________________________ *Date:* _________