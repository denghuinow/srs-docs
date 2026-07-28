# Detailed Summary: PeaZip 2.7.1 Requirements

## Background and Scope
PeaZip is a cross-platform, open-source file and archive manager application designed to provide a unified graphical interface for numerous open-source archiving and compression utilities. Its core functions include creating, updating, and extracting archives across a wide range of formats, alongside file management tools like secure deletion, file splitting/joining, and checksum calculation. The application is self-contained, requiring no installation of other software, and is available for Windows, Linux, BSD, and other POSIX systems. Non-goals include not being a web application and not requiring specific communication interfaces for core functionality.

## Stakeholders Matrix and Use Cases
*   **End User**: Any computer user who needs to manage, compress, and extract files and archives; uses the GUI for daily operations.
*   **Software Engineer/Developer**: Responsible for developing, maintaining, and extending the PeaZip application based on the SRS.
*   **System Administrator**: May deploy and configure PeaZip across systems, potentially utilizing its portable version and system management tools.

**Main Scenarios:**
1.  User browses the filesystem via the File Manager interface to locate files.
2.  User selects multiple files and creates a compressed archive (e.g., 7Z, ZIP) with optional encryption.
3.  User extracts the contents of an existing archive to a specified folder.
4.  User updates an existing archive by adding new files to it.
5.  User employs file management tools (e.g., secure delete, file compare) on selected items.
6.  User configures application settings like language, default formats, and UI preferences.
7.  User drags and drops files between the system and PeaZip interfaces for quick archiving/extraction.
8.  User monitors the progress of an ongoing operation (e.g., compression) via the PeaLauncher graphical wrapper.

**Exception Scenario:**
*   User attempts to extract an encrypted archive without providing the correct password/keyfile, resulting in access denial.

## Business Process
**Main Process: Create and Secure an Archive**
1.  **Trigger/Input**: User selects files/folders in the File Manager.
2.  User navigates to the "Create Archive" interface (via toolbar, context menu, or drag-and-drop).
3.  User selects the desired archive format (e.g., 7Z, ZIP) and configures options (compression level, volume splitting).
4.  User sets an output path and filename for the new archive.
5.  User optionally enables encryption, setting a password and/or selecting a keyfile.
6.  User confirms the operation.
7.  **Output**: A new, optionally encrypted, compressed archive is created at the specified location. The original source files remain unchanged.

**Key Branch A: Extract Archive**
1.  **Trigger**: User selects an archive file.
2.  User navigates to the "Extract" interface.
3.  User specifies the target output folder.
4.  If the archive is encrypted, user provides the password/keyfile.
5.  User confirms extraction.
6.  **Output**: Archive contents are decompressed and saved to the target folder.

**Key Branch B: Update Existing Archive**
1.  **Trigger**: User selects an existing archive and additional files.
2.  User navigates to the "Create Archive" interface (the existing archive is pre-loaded).
3.  User adds the new files to the archive layout.
4.  User confirms the update operation.
5.  **Output**: The existing archive is modified to include the new files, retaining its name and location.

## Domain Model
*   **Archive**: Represents a compressed file container. Fields: Name (required), Format (required, e.g., 7Z, ZIP), Path (required), EncryptionStatus (reference to Encryption), Size.
*   **FileSystemObject**: A generic entity for files and folders browsed or managed. Fields: Name (required), Path (required), Type (File/Folder), Size, LastModifiedDate.
*   **Encryption**: Contains security details for an archive. Fields: Password, KeyfilePath, Algorithm (reference).
*   **Operation**: Tracks a user-initiated action like create, extract, or delete. Fields: Type (required), Status (Running/Complete/Error), ProgressPercentage, TargetObject (reference to Archive/FileSystemObject).
*   **UserSettings**: Stores user preferences. Fields: DefaultArchiveFormat, Language, UITheme, ToolbarConfiguration.
*   **CompressionFormat**: Defines a supported archiving algorithm. Fields: Name (required, unique, e.g., "7Z", "ZIP"), ReadSupport (boolean), WriteSupport (boolean).
*   **Checksum/Hash**: Result of a file integrity check. Fields: Algorithm (required, e.g., MD5, SHA256), Value (required), FileReference (reference to FileSystemObject).

## Interfaces and Integrations
*   **System**: Host Operating System (Windows, Linux, etc.)
    *   **Direction**: Bi-directional.
    *   **Interaction**: File system access for browsing, reading, writing, and deleting files/archives.
    *   **Input**: User requests for file operations.
    *   **Output**: Modified filesystem state (created archives, extracted files).
    *   **SLA**: Must handle standard OS file I/O errors gracefully.
*   **System**: Command-Line Utilities (7-Zip, Pea, etc.)
    *   **Direction**: Outbound from PeaZip.
    *   **Interaction**: PeaZip acts as a frontend GUI, invoking backend utilities for core compression/decompression tasks.
    *   **Input**: Parameters from PeaZip GUI (format, password, paths).
    *   **Output**: Standard output/error from the utility, captured by PeaLauncher for display.
    *   **SLA**: Utilities are bundled; PeaZip must manage their execution lifecycle.
*   **User**: Graphical User Interface (GUI)
    *   **Direction**: Inbound from User.
    *   **Interaction**: Primary user interaction point via windows (File Manager, Create Archive, Extract, Settings) and controls (buttons, menus, drag-and-drop).
    *   **Input**: Mouse clicks, keyboard shortcuts, text entry.
    *   **Output**: Visual feedback, progress indicators, error messages.
    *   **SLA**: UI must remain responsive during long operations.

## Acceptance Criteria
**Capability: Archive Creation with Encryption**
*   **Given** a user has selected files and opened the Create Archive interface,
*   **When** they choose the 7Z format, set a password, and start the operation,
*   **Then** a 7Z archive is created at the specified location and cannot be opened without the correct password.

**Capability: Archive Extraction**
*   **Given** an encrypted ZIP archive exists,
*   **When** a user selects it, provides the correct password in the Extract interface, and chooses a target folder,
*   **Then** the archive contents are fully extracted to the specified folder.

**Capability: Secure File Deletion**
*   **Given** a user selects a file and chooses the "Secure Delete" tool,
*   **When** the operation completes successfully,
*   **Then** the file is permanently removed from the storage device, preventing standard data recovery.

## Non-functional Metrics
*   **Performance**: Compression/decompression speed is dependent on the selected algorithm and system hardware (CPU/RAM). The GUI must remain responsive during long-running backend operations.
*   **Reliability**: The application must handle errors from backend utilities gracefully (e.g., corrupt archives, insufficient disk space) without crashing.
*   **Security**: Passwords and keyfiles for encrypted archives must not be stored or recoverable by the application after the operation. Secure delete must overwrite file data to prevent recovery.
*   **Compliance**: The software and its bundled utilities must be distributed under their respective open-source or royalty-free licenses (e.g., LGPL).
*   **Observability**: All major operations must provide real-time progress feedback via the PeaLauncher interface, including success/failure status upon completion.

## Milestones and Release Strategy
1.  Finalize requirements specification (this SRS).
2.  Core development: GUI framework and integration with primary backend utilities (7z, Zip).
3.  Feature development: Implement all file management tools (secure delete, compare, split/join).
4.  Testing phase: Functional, compatibility (cross-platform), and security testing.
5.  Beta release for community feedback.
6.  Final release of version 2.7.1 with updated documentation.

## Risk List and Mitigation Strategies
1.  **Risk**: Backend command-line utility fails or hangs during a long operation.
    *   **Mitigation**: Implement timeouts and process monitoring in PeaLauncher; provide user with option to cancel the operation.
2.  **Risk**: Incompatibility with a specific version of an operating system or missing system libraries (gtk/gdk).
    *   **Mitigation**: Clearly state system requirements; provide portable versions; include guidance for installing required libraries.
3.  **Risk**: User loses password for an encrypted archive.
    *   **Mitigation**: The application cannot and must not recover passwords. Provide clear warnings to users about this irreversibility during encryption setup.
4.  **Risk**: Bugs in the secure deletion tool leave recoverable data remnants.
    *   **Mitigation**: Use proven, multi-pass overwriting algorithms; conduct security audits on the deletion code.
5.  **Risk**: Performance issues on low-end hardware with high-compression algorithms.
    *   **Mitigation**: Set sensible default compression levels; provide clear UI indicators about expected resource usage for different algorithms.
6.  **Risk**: License compliance issues with bundled third-party utilities.
    *   **Mitigation**: Maintain an audited list of all bundled components and their licenses, ensuring redistribution terms are met.

## Undecided Issues and Responsible Parties
1.  **Issue**: Specific minimum hardware requirements (CPU speed, RAM) for optimal performance with advanced algorithms (e.g., LZMA, PPMd).
    *   **Responsible**: Development Team & Project Lead.
2.  **Issue**: Prioritization of adding support for new, emerging archive formats.
    *   **Responsible**: Project Lead & Community Feedback.
3.  **Issue**: Strategy for handling very large archives (multi-terabyte) regarding memory and UI responsiveness.
    *   **Responsible**: Architecture/Development Team.
4.  **Issue**: Localization process for adding new languages to the application.
    *   **Responsible**: Development Team & Community Volunteers.