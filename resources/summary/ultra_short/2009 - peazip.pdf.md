**Purpose & Scope**
PeaZip is a cross-platform file and archive manager application. It provides a graphical frontend for numerous open-source archiving and compression utilities, enabling users to create, update, and extract archives, and offering additional file management tools. It does not function as a web application and does not inherently require network communication for its core operations.

**Product Background / Positioning**
The application was initially created as a frontend for the Pea archiving utility but evolved into a single, consistent GUI aggregating functionality from many underlying open-source utilities. It operates similarly to commercial tools like WinRAR and WinZip but supports a wider range of archive formats and is fully open-source. It is designed to be self-contained, not requiring the installation of other software packages to function.

**Core Functional Overview**
*   Create compressed archives in multiple formats.
*   Update existing archives by adding new files.
*   Extract contents from archives in a wide range of supported formats.
*   Securely delete files to prevent data recovery.
*   Split files into volumes and merge them back.
*   Calculate checksums and hashes for file integrity checking.
*   Encrypt archives using two-factor authentication (password and optional keyfile).
*   Configure all application features through a centralized settings interface.

**Key Users & Usage Scenarios**
Primary users are any computer system users needing to manage files and archives. There are no distinct permission levels. A typical scenario involves a user compressing a collection of documents into a single encrypted archive for backup, or extracting downloaded software from a compressed archive.

**Major External Interfaces**
The system provides a graphical user interface (GUI) with several main windows: a file manager, archive creation, archive extraction, and settings. It interfaces with the host operating system's file system and supports drag-and-drop operations between the application and the system. It requires an x86-compatible CPU.

**Key Non-functional Requirements**
*   **Performance:** CPU and RAM requirements are dictated by the chosen compression algorithm and level, ranging from minimal to over 1 GB for complex algorithms.
*   **Security:** Extraction from encrypted archives must not be allowed without the correct password and keyfile. Passwords and keyfiles must not be recoverable by other users via the application or system. Secure deletion must leave no recoverable data.
*   **Reliability:** The application must function and provide appropriate error messages even with incorrect user input or settings.
*   **Portability:** Must be compatible with 32-bit and 64-bit Microsoft Windows, and all POSIX-compliant operating systems (Linux, BSD, UNIX-like).

**Constraints, Assumptions & Dependencies**
*   Must be developed using Delphi/Kylix, Object Pascal, or Pascal.
*   Must be licensed under the LGPL.
*   Development is done within the Lazarus IDE.
*   Depends on the inclusion of underlying open-source archiving utilities within its distribution packages.
*   For full drag-and-drop functionality from the application to the system, the host OS must be Microsoft Windows.

**Priorities & Acceptance Approach**
Core archiving functions (create, update, extract) are fundamental. Security features for encryption and secure deletion are critical. Acceptance is based on the system correctly performing all specified functions across the required operating environments, adhering to the stated security constraints, and operating within the described performance parameters for chosen algorithms.