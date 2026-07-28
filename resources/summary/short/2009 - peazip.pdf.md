# Short Summary: PeaZip 2.7.1 Requirements

## Background and objectives
PeaZip is a cross-platform, open-source file and archive manager that provides a graphical interface for various open-source archiving and compression utilities. The application aims to enable users to handle most available archive formats through a consistent, user-friendly interface while offering additional file management tools.

## In scope
*   Creating, updating, and extracting archives in supported formats (e.g., 7z, ZIP, RAR).
*   Providing file management utilities like secure deletion, file splitting/joining, and checksum calculation.
*   Offering two-factor authentication (password and optional keyfile) for archive security.
*   Supporting drag-and-drop operations between the system and application interfaces.
*   Allowing extensive customization of application features and interface through a settings menu.

## Out of scope
*   Requiring installation of other software for core functionality (all needed utilities are included).
*   Compression to read-only archive formats (only creation in fully supported formats).
*   Modification of archives in read-only supported formats.
*   Functioning without an operating system on the host computer.
*   Drag-and-drop from application to system on non-Windows operating systems.

## Stakeholders and core use cases
*   **End Users**: Individuals who use PeaZip to manage files and archives on their computer systems.
*   **Software Engineers/Developers**: Professionals who maintain, extend, or develop the PeaZip application.
*   **Project Maintainers**: Individuals responsible for overseeing the open-source project's development and releases.

**User Stories:**
1.  As an end user, I want to extract the contents of a compressed archive so that I can access the files within.
2.  As an end user, I want to create a compressed archive from multiple files so that I can save storage space and manage them as a single unit.
3.  As an end user, I want to securely delete files so that they cannot be recovered.
4.  As an end user, I want to password-protect an archive so that its contents are accessible only to authorized users.
5.  As an end user, I want to customize the application's interface and behavior through settings so that it better fits my workflow.
6.  As a developer, I want to understand the system's functional requirements so that I can implement or modify features correctly.

## Success metrics
*   Support for extracting content from all listed read-only archive formats.
*   Successful creation and updating of archives in all listed fully supported formats.
*   Positive user feedback on interface usability and feature set.

## Major constraints
*   Must be developed using Delphi/Kylix, Object Pascal, or Pascal programming languages.
*   Must be licensed under LGPL (open-source and free).
*   Requires an x86-compatible CPU due to performance-critical ASM code sections.
*   Must include all necessary backend utilities within its distribution packages.
*   Must maintain compatibility with 32-bit and 64-bit Windows, and POSIX (Linux/BSD/UNIX-like) operating systems.

## Undecided issues
*   Specific performance benchmarks for different compression algorithms and hardware.
*   Detailed list of all standard gtk/gdk libraries that might be missing on some systems.
*   Full specification for the "Run as different user" functionality under all operating systems.
*   Comprehensive error handling and help message catalog for all possible user errors.
*   Long-term roadmap for supporting new archive formats as they emerge.