# Software Requirements Specification (SRS)
## For PeaZip File and Archive Manager
**Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for PeaZip, a cross-platform file and archive manager application. This document is intended to serve as a comprehensive guide for developers, testers, project managers, and stakeholders involved in the development, validation, and maintenance of the PeaZip software.

#### 1.2 Document Conventions
*   Requirements are uniquely identified with labels (e.g., `FR-001`, `NFR-001`).
*   **Shall** indicates a mandatory requirement.
*   *Italicized text* provides explanatory notes or clarifications.
*   This document uses Markdown formatting for structure and readability.

#### 1.3 Project Scope
PeaZip is a desktop application that provides a unified graphical user interface (GUI) for a multitude of open-source archiving and compression utilities. Its core purpose is to enable users to create, update, and extract archives across a wide range of formats, while also offering advanced file management and security tools. The application is self-contained, does not require network connectivity for primary operations, and is positioned as a free, open-source alternative to commercial tools like WinRAR and WinZip.

**In-Scope:**
*   GUI-driven archive creation, update, and extraction.
*   Secure file deletion.
*   File splitting and merging.
*   File integrity checking via checksums and hashes.
*   Archive encryption with two-factor authentication.
*   Centralized application configuration.
*   Compatibility with specified operating systems.
*   Drag-and-drop support (with OS-specific limitations).

**Out-of-Scope:**
*   Functioning as a web application or web service.
*   Built-in peer-to-peer file sharing or cloud storage integration.
*   Native archive format development (relies on bundled utilities).

#### 1.4 References
*   GNU Lesser General Public License (LGPL), Version 2.1 or later.
*   Lazarus IDE Documentation.
*   Documentation for underlying archiving utilities (e.g., 7-Zip, Pea, etc.).

### 2. Overall Description

#### 2.1 Product Perspective
PeaZip is a standalone, installable desktop application. It acts as an aggregator layer, presenting a consistent interface to the user while delegating core compression and extraction tasks to a suite of bundled, open-source command-line utilities. The system interfaces directly with the host operating system's file system.

#### 2.2 Product Functions (High-Level)
1.  Archive Management: Create, update, and extract from numerous archive formats.
2.  File Management: Browse, select, and manage files within a built-in file manager interface.
3.  Data Security: Encrypt/decrypt archives and securely delete files.
4.  Data Integrity: Generate and verify file checksums and cryptographic hashes.
5.  File Operations: Split large files into volumes and reassemble them.
6.  Configuration: Customize application behavior, appearance, and default operations.

#### 2.3 User Classes and Characteristics
*   **End User:** The sole user class. This includes any individual using a computer who needs to manage files and archives. Users are expected to have basic computer literacy but are not required to have knowledge of command-line tools or specific archive formats. No hierarchical permissions or roles exist within the application.

#### 2.4 Operating Environment
*   **Hardware:** x86-compatible CPU (32-bit or 64-bit).
*   **Software:**
    *   **Primary OS:** 32-bit and 64-bit versions of Microsoft Windows.
    *   **Secondary OS:** Any POSIX-compliant operating system (e.g., Linux distributions, BSD, UNIX-like systems).
*   **Dependencies:** The application package must include all necessary open-source archiving utilities (e.g., 7-Zip, Pea, etc.). No separate installation of these tools is required.

#### 2.5 Design and Implementation Constraints
1.  **Implementation Language:** The application shall be developed using Delphi, Kylix, Object Pascal, or Pascal.
2.  **Development Environment:** Development shall be conducted within the Lazarus IDE.
3.  **Licensing:** The application source code shall be licensed under the GNU Lesser General Public License (LGPL).
4.  **Drag-and-Drop:** Full drag-and-drop functionality *from* the application *to* the host OS file manager is constrained to the Microsoft Windows operating system.

#### 2.6 Assumptions and Dependencies
*   It is assumed that the host operating system provides a stable file system API.
*   The correct functioning of core archiving features is dependent on the successful integration and bundling of the underlying open-source utilities.
*   User acceptance testing must be performed on clean installations of the target operating systems.

### 3. System Features and Requirements

#### 3.1 Feature: Archive Creation and Management
**Description:** The user shall be able to create new compressed archives and modify existing ones.

**Requirements:**
*   `FR-001`: The system shall allow the user to select one or more files/folders from the built-in file manager or OS for archiving.
*   `FR-002`: The system shall present a dialog for creating a new archive, allowing the user to specify:
    *   Archive name and save location.
    *   Archive format (e.g., 7Z, ZIP, TAR, PEZ).
    *   Compression level (e.g., Store, Fast, Normal, Maximum).
    *   Encryption settings (see `FR-010`).
    *   Options for splitting into volumes (see `FR-012`).
*   `FR-003`: The system shall allow the user to add new files to an existing archive (update function).
*   `FR-004`: The system shall initiate the archiving process using the appropriate underlying utility based on user-selected format and options.

#### 3.2 Feature: Archive Extraction
**Description:** The user shall be able to extract the entire contents or selected files from a supported archive.

**Requirements:**
*   `FR-005`: The system shall allow the user to open an archive file and browse its contents in a dedicated view.
*   `FR-006`: The system shall allow the user to select specific files/folders within the archive for extraction.
*   `FR-007`: The system shall present a dialog for extraction, allowing the user to specify the target output path.
*   `FR-008`: The system shall prompt the user for a password and/or keyfile if the archive is encrypted.
*   `FR-009`: The system shall initiate the extraction process using the appropriate underlying utility.

#### 3.3 Feature: Security and Encryption
**Description:** The system shall provide mechanisms to protect data confidentiality and ensure secure data deletion.

**Requirements:**
*   `FR-010`: The system shall support encrypting archives using a password and an optional keyfile (two-factor authentication).
*   `FR-011`: The system shall **not** extract or display the contents of an encrypted archive without successful authentication using the correct password and keyfile (if set). `NFR-002`
*   `FR-012`: The system shall provide a "Secure Delete" function that overwrites a file's data on disk multiple times before removing its entry from the file system, rendering it unrecoverable by standard means. `NFR-002`
*   `FR-013`: The system shall **not** store passwords or keyfile paths in plaintext, in memory, or on disk in a manner recoverable by other users or applications. `NFR-002`

#### 3.4 Feature: File Operations and Integrity
**Description:** The system shall provide tools for file manipulation and verification.

**Requirements:**
*   `FR-014`: The system shall allow the user to split a single file into multiple smaller volume files of a user-defined size.
*   `FR-015`: The system shall allow the user to merge previously split volume files back into the original single file.
*   `FR-016`: The system shall be able to calculate and display various cryptographic hash values (e.g., SHA-256, MD5) and checksums (e.g., CRC32) for any selected file.
*   `FR-017`: The system shall allow the user to verify a file's integrity by comparing its calculated hash/checksum against a provided value.

#### 3.5 Feature: User Interface and Configuration
**Description:** The system shall provide an intuitive GUI and a centralized location for all settings.

**Requirements:**
*   `FR-018`: The system shall provide a main application window featuring a dual-pane file manager for browsing the host file system.
*   `FR-019`: The system shall support dragging files from the host OS file manager into the PeaZip application window for archiving or other operations.
*   `FR-020`: The system shall provide a comprehensive "Settings" or "Options" dialog that allows users to configure all aspects of the application, including:
    *   Default archiving format and compression level.
    *   File association settings.
    *   Interface themes and language.
    *   Security and secure deletion settings.
    *   Paths to external tools (if any).

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Graphical User Interface (GUI):** A native desktop GUI built with Lazarus components. Key windows include:
    *   Main File Manager Window
    *   Archive Creation Dialog
    *   Archive Extraction Dialog
    *   Settings/Options Dialog
    *   Checksum/Hash Calculation Dialog
*   **Interaction:** Primary input via mouse and keyboard. Support for context menus, toolbar buttons, and main menu navigation.

#### 4.2 Hardware Interfaces
*   Requires standard input devices (keyboard, mouse).
*   Interacts with persistent storage (HDD, SSD) via the host OS file system.

#### 4.3 Software Interfaces
*   **Host Operating System:** Interfaces via system APIs for file I/O, graphical rendering, and memory management.
*   **Bundled Utilities:** Communicates with bundled command-line archiving tools (e.g., `7z.exe`, `pea`) via standard input/output streams or command-line invocation.

#### 4.4 Communications Interfaces
*   Not applicable for core operations. The application does not require network interfaces for its primary functionality.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-001`: The application's CPU and RAM utilization shall be directly proportional to the complexity of the selected compression algorithm and level. Performance shall range from minimal resource usage for simple "store" operations to potentially exceeding 1 GB of RAM for complex, multi-threaded compression algorithms on large datasets.

#### 5.2 Security Requirements
*   `NFR-002`: The system shall enforce access control on encrypted archives, preventing all extraction and content listing without valid credentials. Sensitive user data (passwords, keyfile contents) shall be handled in volatile memory only and never written to disk or logged. The secure deletion function shall implement a recognized algorithm (e.g., DoD 5220.22-M, Gutmann) to prevent data recovery.

#### 5.3 Reliability and Availability
*   `NFR-003`: The application shall remain stable and responsive during all operations. It shall provide clear, informative error messages to the user in the event of invalid input (e.g., wrong password, corrupt archive), missing files, or insufficient system resources, and shall not crash or exit unexpectedly.

#### 5.4 Portability and Compatibility
*   `NFR-004`: The application shall be fully functional on 32-bit and 64-bit versions of the Microsoft Windows operating system (Windows 7 and later).
*   `NFR-005`: The application shall be fully functional on POSIX-compliant operating systems, including modern Linux distributions and BSD variants. A single codebase shall be maintained for all platforms where possible.

#### 5.5 Usability
*   The user interface shall be organized and intuitive, grouping related functions logically (e.g., all archive-related actions under an "Archive" menu).
*   Common tasks (extract here, add to archive) should be accessible via context menus within the file manager.

### 6. Acceptance Criteria
The product will be considered acceptable when it satisfies the following conditions:

1.  **Functional Completeness:** All functional requirements (`FR-001` through `FR-020`) are implemented and verified as working.
2.  **Security Compliance:** The security requirements (`NFR-002`) are rigorously tested and validated. No security-critical defects are open.
3.  **Cross-Platform Operation:** The application successfully installs and performs all core archiving functions (Create, Update, Extract) on at least one 32-bit Windows, one 64-bit Windows, and one POSIX (Linux) test environment without regression.
4.  **Error Handling:** The application meets the reliability requirements (`NFR-003`), gracefully handling errors and providing useful feedback.
5.  **Constraint Adherence:** The final product is released under the LGPL license and is developed within the specified technical constraints (Pascal/Lazarus).

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner | | | |
| Lead Developer | | | |
| QA Lead | | | |