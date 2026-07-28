# Balanced Summary: PeaZip 2.7.1

## Goals and Scope
PeaZip is a cross-platform, open-source file and archive manager application designed to provide a unified graphical interface for numerous open-source archiving and compression utilities. Its primary scope is to enable users to create, update, extract, and manage archives across a wide range of supported formats, while also offering additional file management tools like secure deletion and file comparison.

## Stakeholders and User Stories
*   **End User:** Any computer user who needs to manage files and archives, responsible for using the application's features.
*   **Software Engineer/Developer:** Responsible for developing, maintaining, and extending the PeaZip application and its underlying utilities.
*   **Project Maintainer (e.g., Giorgio Tani):** Responsible for the overall project direction, integration of utilities, and core application development.

**User Stories:**
1.  As an **End User**, I want to create compressed archives from my files so that I can save storage space and group related files together.
2.  As an **End User**, I want to extract the contents of various archive formats so that I can access the original files.
3.  As an **End User**, I want to securely delete files so that they cannot be recovered.
4.  As an **End User**, I want to encrypt my archives with a password and keyfile so that their contents are protected from unauthorized access.
5.  As an **End User**, I want to customize the application's settings and interface so that it adapts to my workflow and preferences.
6.  As a **Software Engineer**, I want the application to be built with Lazarus IDE using Object Pascal so that I can contribute to its development within the established framework.

## Key Processes
1.  **Browse File System:** (Trigger: Application startup or user navigation) The user navigates through the computer's filesystem using the file manager interface to locate files and archives.
2.  **Select Objects:** (Trigger: User action in the file manager) The user selects one or more files or archives for subsequent operations using various selection tools.
3.  **Create/Update Archive:** (Trigger: User initiates "Add" or "Create archive") The user compresses selected files into a new archive or adds files to an existing one, choosing format, encryption, and other options.
4.  **Extract Archive:** (Trigger: User initiates "Extract" on an archive) The user decompresses and saves the contents of a selected archive to a specified location.
5.  **Apply File Tools:** (Trigger: User selects a utility like "Secure Delete" or "Compare") The user performs a non-archiving file management operation on the selected objects.
6.  **Configure Settings:** (Trigger: User opens the Settings interface) The user modifies application behavior, interface layout, and default parameters for various features.
7.  **Monitor Progress:** (Trigger: Any long-running operation starts) The PeaLauncher graphical wrapper displays real-time progress and results of the executing function.

## Domain Data Elements
*   **Archive:** (Primary Key: Archive Path/Name) Fields: Format, Compression Level, Encryption Status (Password/Keyfile), Timestamp, Size.
*   **File System Object:** (Primary Key: File Path) Fields: Name, Size, Type (File/Directory), Modification Date, Attributes.
*   **User Settings Profile:** (Primary Key: Profile Name) Fields: Default Archive Format, Interface Language, Toolbar Configuration, PeaLauncher Behavior.
*   **Operation Job:** (Primary Key: Job ID/Timestamp) Fields: Type (Create/Extract/Delete/etc.), Target Objects, Status (Running/Complete/Error), Result Summary.
*   **Checksum/Hash Data:** (Primary Key: File Path + Algorithm) Fields: Algorithm Name (e.g., MD5, SHA-256), Calculated Hash Value, Calculation Timestamp.

## Non-Functional Requirements
1.  **Compatibility:** Must run on 32-bit/64-bit Windows, Linux, BSD, and other POSIX-compliant operating systems.
2.  **Portability:** Must be available as a standalone portable application requiring no installation.
3.  **Security:** Must prevent extraction of encrypted archives without the correct password and optional keyfile; must ensure secure deletion leaves no recoverable data.
4.  **Usability:** Must provide a functional, easy-to-use interface accessible to users with varying levels of computer experience, supported by help documentation.
5.  **Self-Contained Operation:** Must include all necessary backend utilities; no separate installation of compression tools should be required.
6.  **Error Handling:** Must function gracefully and provide helpful messages in case of incorrect user input or settings.

## Milestones and External Dependencies
1.  **Core GUI Development:** Completion of the main application interfaces (File Manager, Create Archive, Extract, Settings).
2.  **Backend Integration:** Successful integration and bundling of all supported open-source archiving and compression utilities.
3.  **Cross-Platform Testing:** Verification of functionality on all target operating systems (Windows, Linux/BSD).
4.  **Documentation:** Completion of user help documents and tutorials.
5.  **External Dependency:** Reliance on standard GTK/GDK libraries for graphical components on some systems.

## Risks and Mitigation Strategies
1.  **Risk:** Complexity in maintaining compatibility with numerous, evolving backend archiving utilities.
    *   **Mitigation:** Implement a modular architecture for utility integration and establish clear interfaces.
2.  **Risk:** Performance issues with advanced compression algorithms (e.g., LZMA, PAQ) on low-resource systems.
    *   **Mitigation:** Provide user-configurable compression levels and clear warnings about resource requirements.
3.  **Risk:** Security vulnerability if encryption implementation is flawed.
    *   **Mitigation:** Rely on well-audited, standard encryption methods provided by the underlying utilities and conduct security reviews.
4.  **Risk:** Limited developer community due to niche programming language (Object Pascal/Delphi).
    *   **Mitigation:** Maintain comprehensive documentation and foster an open-source community to attract contributors.
5.  **Risk:** Inconsistent user experience across different operating system platforms.
    *   **Mitigation:** Use cross-platform GUI frameworks and conduct extensive UI/UX testing on each target platform.

## Undecided Issues
1.  Expansion of the list of supported archive formats for both reading and writing.
2.  Implementation details for advanced features like network drive integration or cloud storage support.
3.  Specific algorithms and number of passes for the "secure delete" function.
4.  Long-term strategy for supporting new operating system versions as they are released.
5.  Potential for adding scripting or batch operation capabilities beyond command-line output.
6.  Localization process and support for additional languages beyond those initially planned.