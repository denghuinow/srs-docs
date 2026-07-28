# Balanced Summary: Open Watcom Linux GUI Port

## Goals and Scope
This project aims to port the low-level Open Watcom GUI library to Linux using the GTK toolkit for the X Window System. The primary goal is to enable Open Watcom applications to run on Linux with a native graphical interface, requiring adaptation of Windows/OS/2 API dependencies to GTK equivalents. The scope includes detailed function-by-function porting guidelines, addressing inherent platform differences and resource handling challenges.

## Stakeholders and User Stories
*   **Open Watcom Developers:** Responsible for maintaining and enhancing the Open Watcom compiler suite and its associated libraries.
*   **Linux Application Developers:** Want to use Open Watcom tools to create GUI applications for the Linux platform.
*   **SciTech Software, Inc. (Project Sponsor):** Commissioned the research and specification, overseeing the project's direction and requirements.
*   **End Users of Ported Applications:** Expect native-looking and functioning GUI applications on their Linux systems.

**User Stories:**
1.  As an **Open Watcom Developer**, I want a clear porting strategy for the GUI library so that we can efficiently adapt it for Linux.
2.  As a **Linux Application Developer**, I want to compile my Open Watcom GUI application for Linux so that it runs with a native GTK interface.
3.  As a **Project Sponsor**, I want a detailed effort estimation and risk assessment so that the porting project can be planned and resourced effectively.
4.  As an **End User**, I want applications ported using this library to look and feel like standard Linux applications so that I have a consistent user experience.
5.  As an **Open Watcom Developer**, I want to handle Windows-style resource files in the Linux port so that existing application resources can be reused.
6.  As a **Linux Application Developer**, I want the ported library to have minimal external dependencies so that deployment on target systems is straightforward.

## Key Processes
1.  **Library Initialization:** Triggered by application startup; sets up the GTK environment and main event loop.
2.  **Window Creation:** Triggered by a request to create a new window; builds the GTK widget hierarchy (Window, Box, ScrolledWindow, Viewport, Fixed).
3.  **Dialog Creation:** Triggered by a request to create a dialog; translates control definitions into GTK widgets, handling layout and callbacks.
4.  **Control Management:** Triggered by user interaction or program logic; adds, resizes, shows, hides, or destroys interface controls (buttons, lists, etc.).
5.  **Event Handling:** Triggered by user input (clicks, keypresses) or system events; routes GTK signals to the appropriate Open Watcom GUI callbacks.
6.  **Drawing Operations:** Triggered by paint events; renders text, lines, and rectangles onto the drawing surface using GTK and Pango.
7.  **Resource Loading:** Triggered at initialization or dialog creation; attempts to translate or emulate Windows/OS/2 resource files for use with GTK.

## Domain Data Elements
*   **gui_window:** Primary Key: `GtkWidget* window_handle`. Key Fields: `parent`, `event_callback`, `control_list`, `menu_bar`, `status_bar`.
*   **gui_control:** Primary Key: `int control_id`. Key Fields: `type` (BUTTON, EDIT, LIST), `GtkWidget* widget`, `parent_window`, `text`, `rectangle`.
*   **Dialog Template:** Primary Key: `template_id`. Key Fields: `control_count`, `control_array`, `dialog_style`, `initial_size`.
*   **Menu Structure:** Primary Key: `menu_id`. Key Fields: `item_count`, `item_array` (text, id, submenu), `attached_window`.
*   **Font Information:** Primary Key: N/A (associated with window/style). Key Fields: `family`, `size`, `weight`, `PangoFontDescription*`.
*   **Color Set:** Primary Key: N/A (palette). Key Fields: `foreground_color`, `background_color`, `highlight_color`.

## Non-functional Requirements
1.  The ported library must be linkable both statically and dynamically.
2.  The library must maintain functional compatibility with the original API for existing Open Watcom applications.
3.  Performance of drawing and event handling should be acceptable for typical IDE and tool usage.
4.  The library must be compilable on standard Linux distributions with common development tools.
5.  The visual appearance should respect the user's GTK theme where possible.
6.  Memory management must be robust, preventing leaks in the GTK object hierarchy.

## Milestones and External Dependencies
1.  **Initial Stage Completion:** Basic library initialization and simple window display.
2.  **Core Functionality:** Implementation of window creation, dialogs, and common controls.
3.  **Sample Program Execution:** Successful execution of the standard `samp2.c` GUI sample.
4.  **Elaboration Stage Completion:** Full port of menus, drawing, fonts, and remaining controls.
5.  **Integration Testing:** Verification with larger Open Watcom components (e.g., the IDE).

**External Dependencies:** GTK+ 2.x libraries, Pango, GLib, X Window System, `pkg-config`, GNU make, and standard image libraries (JPEG, PNG, TIFF).

## Risks and Mitigation Strategies
1.  **Risk:** Incompatibility of Windows/OS/2 resource files with GTK.
    *   **Mitigation:** Develop a utility to convert resource data to XML for libglade; implement a fallback runtime translation layer.
2.  **Risk:** GTK's lack of support for the MDI "Windows in Window" model.
    *   **Mitigation:** Simulate using parent-child window relationships and tabbed interfaces where applicable; document the limitation.
3.  **Risk:** No built-in help subsystem equivalent in GTK.
    *   **Mitigation:** Implement help display using external viewers (e.g., `yelp`) or simple HTML/text dialogs.
4.  **Risk:** Significant effort required to map numerous low-level GUI functions.
    *   **Mitigation:** Follow the phased, function-by-function porting plan with continuous testing.
5.  **Risk:** Potential performance overhead from the layered widget hierarchy (Window->Box->ScrolledWindow->Viewport->Fixed).
    *   **Mitigation:** Profile critical paths and optimize the Fixed widget drawing operations.

## Undecided Issues
1.  Final strategy for handling string table resources from Windows/OS/2 (gettext integration details).
2.  Complete handling of numeric widget identifiers within the GTK object model.
3.  Detailed implementation approach for replicating Window Classes and Dialog Templates in GTK.
4.  Whether to attempt modification of the GTK window system menu or leave it standard.
5.  Specific memory allocation strategy for the GTK port (reuse existing or implement new).
6.  Handling of advanced or rarely used GUI features not covered in the initial porting plan.