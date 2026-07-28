# Detailed Summary: Open Watcom Linux GUI Port

## Background and Scope
This document outlines the requirements for porting the low-level Open Watcom GUI library to Linux using the GTK+ toolkit for the X Window System. The goal is to enable Open Watcom applications to run on Linux with a native graphical interface. The scope includes adapting the library's API to GTK+, handling platform-specific issues like resource files and MDI support, and ensuring compatibility with common Linux distributions. Non-goals include modifying the core Open Watcom compiler or runtime libraries beyond the GUI layer, and fully replicating Windows-specific features unsupported by GTK+ (e.g., native MDI "windows in window" model).

## Stakeholders Matrix and Use Cases
- **Open Watcom Development Team**: Responsible for implementing the port, ensuring API compatibility, and testing.
- **Linux End-Users**: Use Open Watcom tools on Linux for development, expecting a stable and native GUI experience.
- **System Administrators**: Deploy the ported library on Linux systems, ensuring dependencies are met.
- **Open Source Community**: Contribute to or review the port, as Open Watcom is open-source.

**Main Scenarios**:
1. **Library Initialization**: The GUI library initializes correctly on Linux using GTK+.
2. **Window Creation**: Applications can create and manage windows with standard controls.
3. **Dialog Handling**: Dialogs render and function similarly to Windows/OS/2 versions.
4. **Event Processing**: User interactions (clicks, key presses) are processed via GTK+ event loop.
5. **Resource Adaptation**: Resource files are handled via workarounds (e.g., XML conversion).
6. **Drawing Operations**: Basic drawing functions work using GTK+ drawing primitives.

**Exception Scenarios**:
1. **Missing MDI Support**: MDI "windows in window" fails gracefully or uses alternative layouts.
2. **Resource File Issues**: Fallback mechanisms for unsupported resource types.

## Business Process
**Main Process: GUI Application Startup**
1. **Trigger**: User launches an Open Watcom application on Linux.
2. **Input**: Application calls `GUIXMain()` to initialize GUI.
3. **Step 1**: Library sets up GTK+ environment and type definitions.
4. **Step 2**: Window classes are registered (stubbed for GTK+).
5. **Step 3**: Message loop starts via `gtk_main()`.
6. **Step 4**: Windows/dialogs are created using GTK+ widgets.
7. **Step 5**: Event handling processes user interactions.
8. **Output**: Application GUI is displayed and responsive.

**Key Branch: Dialog Creation**
1. **Trigger**: Application requests a dialog via `GUICreateDialog()`.
2. **Step 1**: Convert dialog resources to GTK+ XML format (if needed).
3. **Step 2**: Create GTK+ dialog window with controls.
4. **Step 3**: Map control IDs to GTK+ widget references.
5. **Output**: Functional dialog displayed.

**Key Branch: Drawing Operations**
1. **Trigger**: Application calls drawing function (e.g., `GUIDrawText()`).
2. **Step 1**: Convert coordinates to GTK+ fixed widget space.
3. **Step 2**: Use Pango for text rendering or GTK+ drawing functions.
4. **Step 3**: Update display via GTK+ paint mechanisms.
5. **Output**: Visual output on screen.

## Domain Model
- **GUIWindow**: Represents a top-level window. Fields: handle (required, unique), parent (reference), style flags.
- **GUIControl**: Base for UI controls. Fields: id (required, unique), type (e.g., button, edit), window (reference).
- **GUIEvent**: Captures user interactions. Fields: type (required), data, window (reference).
- **GUIFont**: Font information. Fields: name, size, style.
- **GUIColor**: Color representation. Fields: RGB values.
- **GUIResource**: Abstract resource data. Fields: type (e.g., string, dialog), identifier.
- **GUIMenu**: Menu structure. Fields: items (list), parent (reference).
- **GUIDialog**: Dialog instance. Fields: template (reference), controls (list).

## Interfaces and Integrations
- **GTK+ Library**: Direction: Inbound. Interaction: Widget creation and event handling. Input: API calls from ported library. Output: Rendered GUI and event signals. SLA: Must support GTK+ 2.x.
- **X Window System**: Direction: Inbound. Interaction: Low-level display and input. Input: GTK+ requests. Output: Window visuals. SLA: Compatible with common X11 implementations.
- **Resource File Converter**: Direction: Outbound. Interaction: Converts Windows/OS/2 resources to GTK+ format. Input: .rc files. Output: XML for libglade. SLA: Handles basic dialog and string resources.
- **Open Watcom Core Libraries**: Direction: Inbound. Interaction: Provides memory management and base types. Input: Allocation requests. Output: Memory blocks. SLA: Must not break existing functionality.

## Acceptance Criteria
- **Capability: Basic Window Display**
  - Given the library is initialized, when an application creates a window, then it appears on screen with correct title and size.
  - Given a window is created, when the user resizes it, then the content adjusts appropriately.
- **Capability: Dialog Interaction**
  - Given a dialog is open, when the user clicks a button, then the corresponding event is triggered.
  - Given an edit control, when text is entered, then it is displayed and retrievable.
- **Capability: Drawing**
  - Given a drawing function is called, when the window is visible, then the graphics render correctly.
  - Given text is drawn, when using different fonts, then it appears with correct metrics.

## Non-Functional Metrics
- **Performance**: Window creation within 100ms; drawing operations at interactive rates (≥30 FPS).
- **Reliability**: No crashes in standard use; graceful degradation for unsupported features.
- **Security**: Follow GTK+ security best practices; no introduction of vulnerabilities.
- **Compliance**: Adhere to LGPL for GTK+ usage; maintain Open Watcom licensing.
- **Observability**: Logging for initialization errors; debug modes for widget inspection.

## Milestones and Release Strategy
1. **Milestone 1**: Library initialization and basic window creation (6 hours estimated).
2. **Milestone 2**: Dialog support and control rendering (65 hours).
3. **Milestone 3**: Event handling and user interaction (27 hours).
4. **Milestone 4**: Drawing and font functions (24 hours).
5. **Milestone 5**: Menu, toolbar, and status bar (65 hours).
6. **Release**: Alpha for testing, then stable release after bug fixes.

## Risk List and Mitigation Strategies
1. **Risk**: GTK+ API differences cause incomplete feature support. **Mitigation**: Implement workarounds or document limitations.
2. **Risk**: Resource file conversion is incomplete. **Mitigation**: Provide manual conversion tools or fallback to runtime creation.
3. **Risk**: Performance overhead due to abstraction layers. **Mitigation**: Optimize critical paths; profile and refine.
4. **Risk**: Dependency on specific GTK+ versions. **Mitigation**: Test with multiple versions; statically link if necessary.
5. **Risk**: MDI unsupported breaks existing applications. **Mitigation**: Use tabbed or separate windows as alternative.
6. **Risk**: Help subsystem not portable. **Mitigation**: Integrate with Linux help systems (e.g., man pages, web help).
7. **Risk**: Testing coverage insufficient. **Mitigation**: Use automated tests and community beta testing.
8. **Risk**: License compatibility issues. **Mitigation**: Review licenses of all dependencies.

## Undecided Issues and Responsible Parties
1. **Resource File Handling**: How to fully convert string tables and numeric IDs. (Open Watcom Team)
2. **MDI Alternative**: What UI pattern to use instead of "windows in window". (Open Watcom Team)
3. **Help System Integration**: Whether to use GTK+ help or external systems. (Open Watcom Team)
4. **Static Linking**: Whether to statically link GTK+ for distribution. (System Administrators)
5. **Theme Consistency**: How to ensure visual consistency across Linux desktops. (Open Watcom Team)
6. **Input Method Support**: Handling for international input methods. (Open Watcom Team)
7. **Accessibility Features**: Compliance with ATK for accessibility. (Open Watcom Team)
8. **Backward Compatibility**: Ensuring existing applications require minimal changes. (Open Watcom Team)