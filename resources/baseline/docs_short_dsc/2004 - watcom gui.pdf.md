# Software Requirements Specification (SRS)
## Open Watcom Linux GUI Port

**Document Version:** 1.0  
**Date:** [Current Date]  
**Status:** Draft  
**Author:** [Author Name/Team]  
**Project Sponsor:** SciTech Software / Open Watcom Community

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the porting of the Open Watcom GUI library from its native Windows/OS2 environment to Linux using the GTK+ toolkit. The primary objective is to enable the Open Watcom Integrated Development Environment (IDE) and other GUI-based development tools to operate natively on Linux systems with a functional, consistent, and performant graphical user interface.

#### 1.2 Document Conventions
- Requirements are uniquely identified with labels (e.g., `FR-001`, `NFR-010`).
- **Bold** text indicates key terms or emphasis.
- `Monospaced` text denotes code, function names, or technical references.
- *Italicized* text is used for notes or clarifications.

#### 1.3 Intended Audience and Reading Suggestions
- **Project Managers & Stakeholders:** Focus on Sections 1, 2, and 5 for project scope, objectives, and constraints.
- **Developers & Architects:** Focus on Sections 3 and 4 for detailed functional and non-functional requirements.
- **QA/Test Engineers:** Focus on Sections 3, 4, and 5 for testable requirements and success criteria.

#### 1.4 Project Scope
This project involves creating a compatibility layer that translates calls from the existing Open Watcom GUI API (modeled on Windows/OS2 APIs) to the GTK+ 2.x/3.x toolkit on Linux. The ported library must allow unmodified Open Watcom GUI applications to be recompiled and run on Linux with minimal behavioral differences.

**In-Scope Items:**
- Porting core GUI library functions (window management, controls, messaging).
- Implementation of dialogs, menus, toolbars, and status bars using GTK widgets.
- Graphics and text rendering via GDK/Pango/Cairo.
- Event handling and message loop translation.
- Maintenance of API-level backward compatibility.

**Out-of-Scope Items:**
- A utility to convert Windows/OS2 resource (`.rc`, `.res`) files. *(Requires a separate tool)*.
- Implementation of the Multiple Document Interface (MDI) "Windows in Window" paradigm.
- A built-in help subsystem.
- Modification of system (window manager) menus.
- Direct loading of resource DLLs.

#### 1.5 References
- Open Watcom Official Documentation
- GTK+ 3.0 API Reference
- POSIX Standards
- ISO/IEC/IEEE 29148:2018 - Systems and software engineering — Life cycle processes — Requirements engineering

### 2. Overall Description

#### 2.1 Product Perspective
The ported GUI library is a new component within the existing Open Watcom toolchain ecosystem. It will replace the platform-specific GUI backend on Linux, sitting between the Open Watcom application code and the native GTK+/X11 layers.

```
[Open Watcom Application Code]
            |
            v
[Open Watcom GUI API Layer] <--- (This SRS covers this port)
            |
            v
[GTK+ Compatibility Layer (Linux)]  [Native Win/OS2 Layer (Windows/OS2)]
            |                                   |
            v                                   v
        [GTK+/GLib]                       [Win32/OS2 API]
            |                                   |
            v                                   v
        [X11/Wayland]                      [GDI/PM]
```

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Linux Application Developer** | Uses Open Watcom compilers; familiar with C/C++; may be new to Open Watcom IDE. | Run the Open Watcom IDE natively on Linux for development tasks. |
| **Cross-Platform Open Watcom User** | Develops applications for multiple platforms; expects consistent tool behavior. | GUI applications behave similarly on Linux as they do on Windows/OS2. |
| **System Administrator** | Responsible for deploying software across multiple Linux workstations. | Simple installation and dependency management for the library. |
| **GUI Library Maintainer (Developer)** | Understands both Open Watcom API and GTK+ internals. | Clean, maintainable code with clear mapping between API calls. |

#### 2.3 Operating Environment
- **Target OS:** Linux (kernel 2.6+)
- **Target Distributions:** Red Hat Enterprise Linux (and derivatives), SUSE Linux Enterprise Server, openSUSE, TurboLinux, and other major distributions with GTK+ support.
- **Required Libraries:** GTK+ (version 3.x recommended, 2.x fallback), GLib, Pango, Cairo, ATK.
- **Toolchain:** GNU Make, GCC, or Open Watcom's own cross-compiler for Linux.

#### 2.4 Design and Implementation Constraints
1.  **API Compatibility:** The library must maintain source-level compatibility with the existing Open Watcom GUI API. Existing applications should recompile without source modification.
2.  **GTK+ Model:** Must adapt object-oriented, signal-driven GTK+ paradigm to the procedural, message-driven Watcom/Win16 model.
3.  **Resource Files:** Cannot use Windows `.rc` files directly. Requires a runtime translation layer or a separate pre-processing conversion tool (out of scope).
4.  **No Native MDI:** The GTK+ toolkit does not support MDI natively. Must implement a workaround using tabbed notebooks or separate top-level windows, clearly documented as a behavioral difference.
5.  **Dependencies:** The final product must clearly declare its external library dependencies.

#### 2.5 Assumptions and Dependencies
- It is assumed the target Linux systems have a functional X11 or Wayland display server with a compatible window manager.
- The project depends on the stability and continued development of the GTK+ toolkit.
- Success is dependent on the existing Open Watcom GUI test suites being comprehensive and accurate.

### 3. System Features and Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Core Window Management
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-001** | The system shall provide a function to create a main application window (`GUIWinCreate`) mapped to a GTK `GtkWindow`. | High |
| **FR-002** | The system shall map window styles (e.g., `WS_VISIBLE`, `WS_BORDER`) to appropriate GTK window properties and decorations. | High |
| **FR-003** | The system shall implement basic window operations: show, hide, minimize, maximize, restore, move, and resize. | High |
| **FR-004** | The system shall translate and route window messages (e.g., `WM_PAINT`, `WM_CLOSE`, `WM_SIZE`) to GTK signals (`draw`, `delete-event`, `configure-event`) and back to application-defined message procedures. | Critical |

##### 3.1.2 Dialog Boxes and Controls
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-010** | The system shall create modal and modeless dialog boxes (`GUIDlgCreate`) using `GtkDialog`. | High |
| **FR-011** | The system shall support standard controls: buttons (`GtkButton`), static text (`GtkLabel`), edit boxes (`GtkEntry`, `GtkTextView`), listboxes (`GtkListBox`), comboboxes (`GtkComboBoxText`), and check/radio buttons (`GtkCheckButton`, `GtkRadioButton`). | High |
| **FR-012** | The system shall implement a mechanism to associate a numeric control ID (from Open Watcom) with a GTK widget pointer, enabling `GetDlgItem()`-like functionality. | High |

##### 3.1.3 Menus, Toolbars, and Status Bars
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-020** | The system shall create menu bars (`GtkMenuBar`), drop-down menus (`GtkMenu`), and menu items (`GtkMenuItem`) from API calls, translating command IDs. | Medium |
| **FR-021** | The system shall provide basic toolbar creation (`GtkToolbar`) with buttons and separators. | Medium |
| **FR-022** | The system shall implement a status bar area, typically at the bottom of a window, using a `GtkStatusbar` or `GtkLabel` within a layout container. | Medium |

##### 3.1.4 Drawing and Text Rendering
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-030** | The system shall handle `WM_PAINT` messages by providing a Cairo drawing context to the application's paint procedure. | High |
| **FR-031** | The system shall map GDI-like drawing functions (e.g., `MoveTo`, `LineTo`, `Rectangle`, `Ellipse`) to their Cairo equivalents. | High |
| **FR-032** | The system shall use Pango for text rendering, supporting basic fonts, sizes, and styles as specified by the Open Watcom API. | High |

##### 3.1.5 Event and Message Loop
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR-040** | The system shall implement a message loop (`GetMessage`, `DispatchMessage`) that polls the GTK main event loop (`gtk_main_iteration_do`). | Critical |
| **FR-041** | The system shall translate GTK signals (e.g., `clicked`, `changed`, `key-press-event`) into corresponding Open Watcom window messages (e.g., `WM_COMMAND`, `WM_CHAR`). | Critical |

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **NFR-001** | Window creation and response to user events (click, keypress) shall have perceived latency of less than 100ms on standard developer hardware. | Medium |
| **NFR-002** | The library's memory footprint shall not exceed 150% of the native Windows version for an equivalent application state. | Low |

##### 3.2.2 Compatibility & Usability
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **NFR-010** | The ported library shall allow 90% of the existing Open Watcom GUI sample programs to compile and run without source code modification. | Critical |
| **NFR-011** | Visual appearance and layout of controls shall be functionally equivalent, though they may adopt the native GTK/theme appearance. | High |
| **NFR-012** | Keyboard navigation (Tab order, accelerator keys) shall follow Linux desktop conventions where they diverge from Windows, with documentation of differences. | Medium |

##### 3.2.3 Maintainability & Support
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **NFR-020** | The code shall be modular, with clear separation between the generic API layer and the GTK-specific implementation. | High |
| **NFR-021** | The build system shall use standard Autotools or CMake, integrating with the broader Open Watcom build process. | High |
| **NFR-022** | Comprehensive API documentation shall be provided, focusing on the mapping between Open Watcom functions and GTK calls. | Medium |

### 4. External Interface Requirements

#### 4.1 User Interfaces
- The library itself has no direct user interface. It enables Open Watcom applications to have a UI on Linux.
- Applications will have the appearance of the user's selected GTK theme (e.g., Adwaita).

#### 4.2 Hardware Interfaces
- Indirectly interfaces with display hardware via X11/Wayland and GTK+.

#### 4.3 Software Interfaces
- **GTK+ (glib-2.0, gtk+-3.0):** Primary toolkit for all GUI components.
- **Pango (pango-1.0):** For text layout and rendering.
- **Cairo (cairo):** For 2D drawing operations.
- **Xlib/Wayland Client Libraries:** (Handled by GDK, not directly).
- **Standard C Library (libc):** For memory and string operations.

#### 4.4 Communications Interfaces
- Not applicable for this library.

### 5. Other Non-Functional Requirements

#### 5.1 Security
- The library shall not introduce security vulnerabilities such as buffer overflows in its translation layer. Input from the application API must be validated before passing to GTK.

#### 5.2 Portability
- The source code shall be written in ANSI C to ensure compatibility with both the Open Watcom compiler and GCC.
- The build system shall be portable across the major Linux distributions specified in Section 2.3.

### 6. Appendices

#### Appendix A: Glossary
- **API:** Application Programming Interface.
- **GDK:** GTK Drawing Kit, the low-level layer of GTK.
- **GDI:** Graphics Device Interface (Windows).
- **MDI:** Multiple Document Interface.
- **Pango:** Library for internationalized text layout and rendering.
- **PM:** Presentation Manager (OS/2).
- **Resource File (`.rc`):** A script file defining dialog layouts, menus, and strings in Windows/OS2.

#### Appendix B: Analysis Models
*To be populated during design phase:*
- High-level architectural diagram.
- Sequence diagram for window creation and message flow.
- State diagram for a dialog box interaction.

#### Appendix C: Issues and Decisions Log
This section tracks the resolution of undecided issues from the project summary.

| Issue | Decision / Resolution | Date | Rationale |
| :--- | :--- | :--- | :--- |
| String Resources | Use **gettext** (`libintl`) for runtime localization. Provide a utility to convert `.rc` string tables to `.po` files (separate tool). | TBD | Standard Linux practice, robust, widely supported. |
| Numeric Widget IDs | Implement a custom `GHashTable` within each window/dialog to map integer IDs to `GtkWidget*` pointers. | TBD | Efficient lookup, aligns with GTK's data management patterns. |
| UI Description Format | Implement a **custom XML conversion** utility (out-of-scope for core lib) that translates `.rc` files to a simple format, which the library can load at runtime. Avoid libglade dependency for simplicity. | TBD | Reduces external dependencies, provides more control over the mapping. |
| Window Class Registration | Simulate the concept using a structure containing the window procedure and default styles, registered in an internal library table. | TBD | Maintains the API abstraction without requiring true GTK class inheritance. |
| Memory Allocation | Use `g_malloc`/`g_free` (GLib) for all GTK-related objects to ensure compatibility. For internal library structures, use a consistent wrapper that can be tracked/debugged. | TBD | Ensures proper memory management within the GLib ecosystem. |

---
*This document is considered the authoritative source of requirements for the Open Watcom Linux GUI Port project. All subsequent design and implementation work shall be traced to the requirements contained herein.*