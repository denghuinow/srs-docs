# Detailed Summary: PDF Split and Merge (v2.1.0)

## Background and Scope
This document specifies the requirements for PDF Split and Merge (PDFsam) v2.1.0, an existing open-source desktop application for manipulating PDF files. The tool provides a graphical user interface (GUI) and a command-line console to perform operations like splitting, merging, rotating, and visually reordering pages across one or more PDF documents. Its primary goal is to offer these capabilities for free through a simple, user-friendly interface. The scope is limited to the features described for the basic version; non-goals include web-based functionality, advanced document editing (e.g., content modification), and integration with proprietary PDF editors.

## Stakeholders Matrix and Use Cases
*   **End User (General)**: Uses the GUI to perform PDF manipulations for personal or professional tasks, relying on the intuitive interface.
*   **Power User/Administrator**: Utilizes the command-line console for batch processing, server-side jobs, or automating repetitive PDF tasks.
*   **Open Source Developer**: Contributes to the project's codebase, requiring understanding of Java and the existing architecture to extend features.
*   **Translator**: Helps localize the application by translating the interface into new languages not currently supported.
*   **Tester**: Validates application functionality against this specification to ensure quality and identify bugs methodically.

**Main & Exception Scenarios (≤8 total):**
1.  **Split Document**: User selects a PDF, chooses a split method (e.g., by page count, bookmarks), configures output naming, and executes.
2.  **Merge/Extract Documents**: User loads multiple PDFs, specifies page ranges for each, orders them, and merges into a single output file.
3.  **Alternate Mix**: User selects two PDFs, configures mix parameters (e.g., reverse order, page switch interval), and combines them alternately.
4.  **Rotate Pages**: User selects one or more PDFs, sets rotation angle and target pages (all/even/odd), and applies the rotation.
5.  **Visually Reorder/Compose**: User loads PDF(s), uses a thumbnail interface to select, reorder, delete, or rotate specific pages, and creates a new document.
6.  **Save/Load Environment**: User saves the current state of all plugin settings to a file and reloads it later to resume work or automate repetitive jobs.
7.  **Handle Protected PDF**: System prompts user for a password when a password-protected PDF is loaded for any operation.
8.  **Error Logging**: System writes log messages (info, warning, error) during operations, which the user can view, copy, or save for troubleshooting.

## Business Process
**Main Process: Execute PDF Manipulation via GUI**
1.  **Trigger**: User launches PDFsam application.
2.  User selects desired plugin from the left-hand plugins tree (e.g., Split, Merge).
3.  User imports one or more source PDF files via the file browser.
4.  System displays file metadata (pages, version); if file is encrypted, user enters password.
5.  User configures operation-specific parameters (e.g., split intervals, page selection, rotation degrees).
6.  User sets output preferences (destination path, filename pattern, compression, PDF version).
7.  User clicks the "Run" button to execute the operation.
8.  **Output**: System generates the manipulated PDF file(s) at the specified location and logs the activity.

**Key Branch A: Using Saved Environment**
1.  User loads a previously saved environment file (via menu or shortcut).
2.  System populates all plugin panels with the saved settings and file paths.
3.  User verifies or adjusts settings.
4.  User clicks "Run" to execute.

**Key Branch B: Using Command-Line Console**
1.  User invokes the console application from a terminal/shell.
2.  User issues a command with appropriate parameters (e.g., input files, operation type).
3.  Console processes the command without GUI interaction.
4.  **Output**: Operation completes, generating output files and/or status messages in the console.

## Domain Model (Entities ≤8)
*   **Document**: Represents an input or output PDF file.
    *   Fields: filePath (required), pageCount, pdfVersion, isEncrypted, password.
*   **Job/Plugin Task**: Represents a configured manipulation operation.
    *   Fields: type (required, e.g., "split", "merge"), parameters (JSON/XML), sourceDocuments (reference to Document list), outputSettings.
*   **Environment**: A saved snapshot of the application state.
    *   Fields: name, saveDate, pluginStates (reference to Job/Plugin Task list), workingDirectory.
*   **User Settings**: Global application preferences.
    *   Fields: language, lookAndFeel, logLevel, defaultWorkingDirectory, autoUpdateEnabled, defaultEnvironment (reference to Environment).
*   **Log Entry**: A record of an application event.
    *   Fields: timestamp (required), level (required: INFO/WARN/ERROR), message, sourcePlugin.
*   **Page Selection**: Defines a range or set of pages from a document.
    *   Fields: document (reference to Document, required), selectionString (e.g., "1-5, 10, 15-").
*   **Output Specification**: Defines how output files are named and saved.
    *   Fields: destinationPath, filenamePattern, compressionEnabled, pdfVersion.
*   **Thumbnail**: A visual representation of a PDF page.
    *   Fields: document (reference to Document, required), pageNumber (required), imageData.

## Interfaces and Integrations (≤8 total)
1.  **System**: PDF Rendering Library (e.g., iText)
    *   **Direction**: Internal / Outbound
    *   **Interaction**: Core PDF manipulation engine.
    *   **Input**: PDF bytes, operation commands.
    *   **Output**: Modified PDF bytes, operation status.
    *   **SLA**: Must handle standard PDF versions up to 1.7; errors must be caught and logged.

2.  **System**: Java Swing Framework
    *   **Direction**: Internal / Foundation
    *   **Interaction**: Provides all GUI components (windows, panels, buttons, tables).
    *   **Input**: User events (clicks, key presses).
    *   **Output**: Rendered UI, updated application state.
    *   **SLA**: Must be compatible with JVM 1.6+.

3.  **System**: Operating System File System
    *   **Direction**: Outbound
    *   **Interaction**: File I/O for reading PDFs and writing results.
    *   **Input**: File paths from user selection.
    *   **Output**: New PDF files, environment (.xml) files, log text files.
    *   **SLA**: Must respect OS file permissions; must not modify source files.

4.  **System**: Command-Line Shell
    *   **Direction**: Inbound
    *   **Interaction**: Console application entry point.
    *   **Input**: Text commands and arguments.
    *   **Output**: Status messages, error codes, generated files.
    *   **SLA**: Should provide clear help text and error messages for invalid commands.

5.  **System**: (Optional) Update Server
    *   **Direction**: Outbound
    *   **Interaction**: Checks for new application versions.
    *   **Input**: Current application version.
    *   **Output**: Notification if a newer version is available.
    *   **SLA**: Network call must not block GUI; should timeout gracefully.

## Acceptance Criteria
**For Splitting by Bookmarks:**
*   **Given** a PDF document with a defined bookmark structure,
*   **When** the user selects the "Split by bookmark level" option and runs the job,
*   **Then** the system creates one output PDF file for each section defined by the bookmarks of the selected level.

**For Visual Document Composition:**
*   **Given** multiple PDF documents are loaded into the Visual Composer plugin,
*   **When** the user drags thumbnails from the source panel to the composition panel, reorders them, and executes,
*   **Then** a single PDF is generated containing the selected pages in the specified order.

**For Environment Save/Load:**
*   **Given** the user has configured multiple plugins with files and settings,
*   **When** the user saves the environment, closes, and later reloads that environment file,
*   **Then** all plugins are restored to their previous state with file paths and parameters intact.

## Non-Functional Metrics
*   **Performance**: Application startup time should be under 5 seconds on average hardware. PDF processing speed should be comparable to file size (e.g., ~100 pages per second on standard hardware).
*   **Reliability**: The application must not crash on malformed user input (e.g., invalid page ranges); errors must be caught and reported via the log panel. Input PDF files must remain unaltered.
*   **Security**: No specific application-level security is required, but the system must not introduce vulnerabilities (e.g., path traversal) via file input fields.
*   **Compliance**: The software and its dependencies must comply with the GNU GPLv2 license. Distribution must include source code.
*   **Observability**: All operations must generate timestamped log entries at a user-configurable level (DEBUG, INFO, etc.). The log panel must allow filtering and export.

## Milestones and Release Strategy (≤6 items)
1.  **v2.1.0 Release (Current)**: Stabilize and document all existing basic features as per this SRS.
2.  **Translation Update Cycle**: Regular integration of new language translations from the community portal.
3.  **Enhanced Version Integration**: Plan for merging features from the separate "enhanced" version into the main branch or defining a clear plugin architecture for premium features.
4.  **Dependency Update**: Update core PDF library (e.g., iText) to a newer, maintained version for security and feature support.
5.  **Testing Suite Enhancement**: Develop or extend automated tests for core manipulation functions.
6.  **Community Bug Fix Release**: Address critical bugs reported via SourceForge, leading to a patch release (e.g., v2.1.1).

## Risk List and Mitigation Strategies (≤8 items)
1.  **Risk**: Core PDF library (iText) may have licensing changes or become obsolete.
    *   **Mitigation**: Monitor library development; evaluate alternative FOSS PDF libraries as a potential replacement.
2.  **Risk**: Large PDF files or complex operations could exceed default JVM memory, causing crashes.
    *   **Mitigation**: Document how users can increase JVM heap size via command-line arguments. Implement progressive loading for visual plugins.
3.  **Risk**: Community contribution and maintenance may slow down.
    *   **Mitigation**: Maintain clear documentation (this SRS, code comments) to lower the barrier for new developers.
4.  **Risk**: New PDF standards or features (e.g., complex encryption) may not be supported.
    *   **Mitigation**: Clearly state supported PDF versions in documentation. Rely on the underlying PDF library for compliance.
5.  **Risk**: The GUI, built on Swing, may appear dated compared to modern frameworks.
    *   **Mitigation**: Leverage Swing's theming ("Look and Feel") options to improve aesthetics. Prioritize functionality over major UI overhaul.
6.  **Risk**: Command-line console arguments could be complex and error-prone for users.
    *   **Mitigation**: Provide comprehensive help (`-h`), examples in documentation, and clear error messages.
7.  **Risk**: Saved environment files may contain absolute file paths that are invalid on another machine.
    *   **Mitigation**: Document this limitation. Consider storing paths relative to the environment file's location as a future enhancement.
8.  **Risk**: Operating system updates could break Java compatibility or installation.
    *   **Mitigation**: Clearly state JRE 1.6+ as a prerequisite. Test on latest stable versions of target OSes.

## Undecided Issues and Responsible Parties
1.  **Form Handling Strategy**: The merge feature mentions forms but lacks detailed requirements for handling form data during merge/extract. (Responsible: Lead Developer)
2.  **Plugin Architecture Roadmap**: The relationship and upgrade path between the "basic" and "enhanced" versions is not architecturally defined. (Responsible: Project Maintainer)
3.  **Update Mechanism**: The method for actually downloading and installing updates (beyond checking) is not specified. (Responsible: Lead Developer)
4.  **Batch Processing Limits**: Maximum number of files for merge or maximum pages for visual operations are not defined, posing potential performance cliffs. (Responsible: Lead Developer/Tester)
5.  **Accessibility Compliance**: No specific requirements for keyboard navigation or screen reader support beyond basic shortcuts. (Responsible: UI Developer)
6.  **Output File Naming Collisions**: Strategy for handling duplicate filenames when using patterns that don't guarantee uniqueness (e.g., `[BASENAME]`) is not detailed. (Responsible: Lead Developer)