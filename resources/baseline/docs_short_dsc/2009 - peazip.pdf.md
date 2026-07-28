# Software Requirements Specification (SRS)
## For PeaZip 2.7.1

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for PeaZip version 2.7.1. It is intended for use by the project's stakeholders, including software developers, project maintainers, and quality assurance personnel, to ensure a common understanding of the system's capabilities, constraints, and goals.

#### 1.2 Document Conventions
*   **Bold text** is used for key terms and section references.
*   *Italic text* is used for emphasis.
*   `Monospaced text` indicates code, file paths, or user interface elements.
*   Requirements are uniquely identified as **FR** (Functional Requirement) or **NFR** (Non-Functional Requirement).

#### 1.3 Project Scope
PeaZip is a cross-platform, open-source file and archive manager. It provides a unified graphical user interface (GUI) for numerous open-source command-line utilities, enabling users to create, extract, and manage archives across a wide range of formats. Beyond archiving, it includes supplementary file management tools such as secure deletion, file splitting/joining, and checksum verification.

##### 1.3.1 In Scope
*   Creation, updating, and extraction of archives in fully supported formats.
*   Extraction from read-only supported archive formats.
*   File management utilities (secure delete, split/join, checksum/hash).
*   Archive security via two-factor authentication (password + optional keyfile).
*   Drag-and-drop operations from the host operating system into the PeaZip interface.
*   Extensive user customization via a comprehensive settings/options menu.
*   Self-contained distribution including all necessary backend utilities.

##### 1.3.2 Out of Scope
*   Requiring the user to install separate software for core archiving functionality.
*   Creating new archives in read-only supported formats.
*   Modifying existing archives in read-only supported formats (e.g., adding/removing files).
*   Operation without a host operating system.
*   Drag-and-drop operations *from* the PeaZip application *to* the host system on non-Windows operating systems.

#### 1.4 References
*   GNU Lesser General Public License (LGPL): [https://www.gnu.org/licenses/lgpl-3.0.html](https://www.gnu.org/licenses/lgpl-3.0.html)
*   PeaZip Project Website: [https://peazip.github.io/](https://peazip.github.io/)

### 2. Overall Description

#### 2.1 Product Perspective
PeaZip is a standalone desktop application. It acts as a front-end GUI wrapper for a suite of open-source, command-line archiving and hashing tools (e.g., 7-Zip, UPX, p7zip). The application integrates these tools into a cohesive system, managing their execution, parsing output, and presenting results within a consistent user interface.

#### 2.2 Product Functions (High-Level)
1.  **Archive Management:** Create, extract, update, and test archives.
2.  **Format Support:** Interface with utilities to handle numerous compression and archive formats.
3.  **Security:** Apply encryption and two-factor authentication to archives.
4.  **File Tools:** Provide utilities for secure deletion, file splitting/joining, and checksum calculation.
5.  **User Customization:** Allow configuration of application behavior, interface, and integration with the OS.
6.  **Cross-Platform Operation:** Provide a consistent experience across Windows and POSIX-compliant systems.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Goals |
| :--- | :--- | :--- |
| **End User** | Varying technical expertise. Needs to manage personal or work files. Values ease of use, reliability, and a broad feature set. | Compress files to save space, extract downloaded archives, securely delete sensitive data, protect archives with passwords. |
| **Software Developer** | Proficient in software development, familiar with the codebase (Object Pascal). Requires clear requirements and system understanding. | Implement new features, fix bugs, extend format support, maintain code quality. |
| **Project Maintainer** | Oversees project direction, releases, and community. Concerned with licensing, compatibility, and project sustainability. | Manage releases, ensure license compliance, coordinate development efforts, address community feedback. |

#### 2.4 Operating Environment
*   **Software:**
    *   **Windows:** 32-bit and 64-bit versions (e.g., Windows 7, 8, 10, 11).
    *   **POSIX:** Linux, BSD, and other UNIX-like operating systems.
*   **Hardware:**
    *   x86-compatible CPU (32-bit or 64-bit).
    *   Sufficient RAM and disk space as required by the host OS and target archive operations.

#### 2.5 Design and Implementation Constraints
1.  **Implementation Language:** The core application must be developed in Delphi, Kylix, Object Pascal, or Pascal.
2.  **License:** The entire application must be licensed under the GNU Lesser General Public License (LGPL).
3.  **Architecture:** Must include performance-critical sections written in Assembly (ASM) for x86 architecture.
4.  **Distribution:** Must be distributed with all necessary backend utilities; cannot depend on user-installed tools for core functions.
5.  **Portability:** The codebase must maintain compatibility for both Windows and POSIX (Linux/BSD) operating systems.

#### 2.6 Assumptions and Dependencies
*   The host system has a functional graphical desktop environment.
*   Necessary system libraries (e.g., GTK+ on Linux) are present or can be installed by the user/package manager.
*   Backend command-line utilities (7z, etc.) are stable and their output formats are predictable.

### 3. System Features

#### 3.1 Feature: Core Archive Operations
**Description:** The system shall allow users to perform fundamental actions on archives.

**3.1.1 Sub-Feature: Archive Creation**
*   **FR-1.1:** The system shall allow the user to create a new archive from a selection of files and/or folders.
*   **FR-1.2:** The user shall be able to select from a list of fully supported output formats (e.g., 7Z, ZIP, TAR).
*   **FR-1.3:** The user shall be able to configure compression level, dictionary size, and other algorithm-specific parameters.

**3.1.2 Sub-Feature: Archive Extraction**
*   **FR-1.4:** The system shall allow the user to extract the entire contents or specific files from a supported archive format.
*   **FR-1.5:** The system shall support extracting from both "fully supported" and "read-only supported" formats.
*   **FR-1.6:** The user shall be able to choose the destination path for extracted files.

**3.1.3 Sub-Feature: Archive Update**
*   **FR-1.7:** The system shall allow the user to add, delete, or rename files within an existing archive that is in a *fully supported* format.

#### 3.2 Feature: Archive Security
**Description:** The system shall provide mechanisms to control access to archive contents.

*   **FR-2.1:** The system shall allow the user to encrypt an archive using a password during creation or update.
*   **FR-2.2:** The system shall support two-factor authentication by allowing the use of an optional keyfile in addition to a password.
*   **FR-2.3:** The system shall prompt the user for credentials (password/keyfile) when attempting to open or extract from a password-protected archive.

#### 3.3 Feature: File Management Utilities
**Description:** The system shall provide tools for file manipulation outside of archiving.

**3.3.1 Sub-Feature: Secure Deletion**
*   **FR-3.1:** The system shall provide a utility to overwrite a file's data on disk multiple times before removing it, preventing recovery by standard means.

**3.3.2 Sub-Feature: File Split & Join**
*   **FR-3.2:** The system shall allow splitting a single large file into multiple smaller volumes of a user-defined size.
*   **FR-3.3:** The system shall allow rejoining previously split volumes to reconstruct the original file.

**3.3.3 Sub-Feature: Checksum & Hash**
*   **FR-3.4:** The system shall calculate and verify cryptographic hashes (e.g., SHA-256, MD5, CRC32) for selected files.

#### 3.4 Feature: User Interface & Customization
**Description:** The system shall offer a configurable graphical interface.

*   **FR-4.1:** The system shall provide a main application window displaying the host filesystem and archive contents.
*   **FR-4.2:** The system shall support drag-and-drop operations *from* the host operating system *into* the PeaZip interface for adding files to archives.
*   **FR-4.3:** On Windows systems, the system shall also support drag-and-drop *from* the PeaZip interface *to* the host system.
*   **FR-4.4:** The system shall provide a comprehensive settings/options dialog allowing users to customize:
    *   Interface themes and language.
    *   Default archiving and extraction behaviors.
    *   System integration (context menu, file associations).
    *   Program and compression settings.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   A graphical user interface (GUI) built for Windows (native) and POSIX systems (using GTK+ or similar).
*   Context menu integration in Windows Explorer and compatible Linux file managers.
*   Standard dialog boxes (Open, Save, Browse for Folder).

#### 4.2 Hardware Interfaces
*   Requires standard input devices (keyboard, mouse/touchpad).
*   No direct hardware control is specified.

#### 4.3 Software Interfaces
*   **Backend Utilities:** The application shall invoke and manage command-line utilities (e.g., `7z.exe`, `7za`, `upx`). It shall parse their standard output and error streams.
*   **Operating System APIs:** Shall use OS APIs for file operations, graphical rendering, and system integration (e.g., Windows Shell API, POSIX file ops).

#### 4.4 Communications Interfaces
*   Not applicable for this version. (No network or inter-process communication features are defined in scope).

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   **NFR-1:** Archive operations (compress/decompress) shall perform within the performance envelope of the underlying backend utilities (7-Zip, etc.).
*   **NFR-2:** The GUI shall remain responsive during long-running operations, providing progress feedback to the user.

#### 5.2 Safety & Security Requirements
*   **NFR-3:** Passwords shall not be stored in plaintext. They shall be held transiently in memory only for the duration of the operation.
*   **NFR-4:** The secure deletion function shall implement a recognized overwriting algorithm (e.g., DoD 5220.22-M, Gutmann).

#### 5.3 Software Quality Attributes
*   **Reliability (NFR-5):** The application shall not crash due to malformed archive files. Errors from backend utilities shall be caught and presented to the user in a comprehensible manner.
*   **Usability (NFR-6):** Common tasks (extract, create archive) shall be achievable within 3-4 user actions from the main interface.
*   **Portability (NFR-7):** The source code shall compile and function correctly on both Windows and POSIX target platforms without modification to core logic.
*   **Maintainability (NFR-8):** The code shall be modular, separating GUI logic from backend utility management.

### 6. Other Requirements

#### 6.1 Success Metrics
*   Functional verification of extraction from 100% of listed read-only archive formats.
*   Functional verification of creation and updating for 100% of listed fully supported formats.
*   Achievement of a positive (>75%) user satisfaction rating regarding interface usability and overall feature set in post-release feedback channels.

#### 6.2 Undecided / TBD Issues
1.  Establishing specific performance benchmarks for compression algorithms across different hardware.
2.  Defining a complete list of GTK/GDK library dependencies for all target Linux distributions.
3.  Finalizing the specification for "Run as different user" functionality across all supported operating systems.
4.  Creating a comprehensive catalog of error messages and help documentation for all potential user errors.
5.  Developing a long-term technical roadmap for the integration of new archive formats.

---
**Appendix A: Glossary**

| Term | Definition |
| :--- | :--- |
| **Fully Supported Format** | An archive format for which PeaZip can create, update, and extract archives using integrated backend utilities. |
| **Read-Only Supported Format** | An archive format for which PeaZip can only extract (read) archives, typically using integrated or external utilities where creation is not legally or technically feasible. |
| **Two-Factor Authentication** | In this context, the use of two independent factors (a password and a keyfile) to encrypt an archive, both of which are required for decryption. |
| **Backend Utility** | A separate, command-line program (e.g., 7-Zip's `7z`) that performs the actual compression, extraction, or hashing operations. |
| **POSIX** | Portable Operating System Interface; a family of standards for maintaining compatibility between Unix-like operating systems. |