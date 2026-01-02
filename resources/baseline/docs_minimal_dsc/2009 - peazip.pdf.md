# Software Requirements Specification (SRS) for PeaZip
**Document Version:** 1.0
**Date:** [Current Date]
**Status:** Draft

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for PeaZip, a cross-platform file and archive manager. It is intended to serve as a comprehensive guide for developers, testers, project managers, and stakeholders throughout the software development lifecycle.

### 1.2 Scope
PeaZip is a graphical user interface (GUI) application that integrates and provides a unified front-end for multiple open-source archiving and compression utilities. Its primary scope is to enable users to create, update, and extract compressed archives across a wide range of formats. Additionally, it provides a suite of auxiliary file management tools. The application is designed to be accessible to both novice and experienced computer users.

**In-Scope:**
*   Archive creation, update, and extraction.
*   Cross-platform GUI for archive operations.
*   Integrated file management utilities (secure delete, split/join, checksum).
*   Archive security features (passwords, keyfiles).
*   Support for specified operating systems and architectures.

**Out-of-Scope:**
*   Development of the underlying compression algorithms (relies on existing open-source utilities).
*   Native integration with cloud storage services.
*   Real-time file synchronization.
*   Advanced batch scripting or server-side automation beyond the provided GUI.

### 1.3 Definitions, Acronyms, and Abbreviations
*   **GUI:** Graphical User Interface.
*   **LGPL:** GNU Lesser General Public License.
*   **POSIX:** Portable Operating System Interface (a family of standards for maintaining compatibility between operating systems like Linux, BSD).
*   **x86:** Family of instruction set architectures based on the Intel 8086 CPU.
*   **Keyfile:** A file used as a second factor of authentication, in addition to a password, to encrypt/decrypt an archive.
*   **Checksum:** A small-sized datum derived from a block of digital data for the purpose of detecting errors.

### 1.4 References
*   GNU Lesser General Public License v3.0 (or later): [https://www.gnu.org/licenses/lgpl-3.0.html](https://www.gnu.org/licenses/lgpl-3.0.html)
*   POSIX Standard (IEEE Std 1003.1)

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its users, and constraints. Section 3 details the specific functional and non-functional requirements.

## 2. Overall Description

### 2.1 Product Perspective
PeaZip is a standalone, desktop application. It acts as a meta-wrapper, providing a consistent GUI layer for disparate command-line archiving tools (e.g., 7-Zip, Pea, UPX). It is not a module or plugin for another system.

### 2.2 Product Functions
The core high-level functions of PeaZip are:
1.  **Archive Management:** Create new archives, add files to existing archives, and extract files from archives.
2.  **Format Support:** Interface with utilities to handle numerous archive formats (e.g., 7Z, ZIP, RAR, TAR, GZ).
3.  **Security:** Protect archives using passwords and optional keyfiles (two-factor authentication).
4.  **File Utilities:** Offer tools for secure file deletion, splitting large files into parts, joining parts back together, and calculating file hashes/checksums.
5.  **User Interface:** Provide an intuitive, consistent GUI for all functions across supported platforms.

### 2.3 User Classes and Characteristics
*   **Novice User:** Has limited experience with archive managers. Requires a clear, intuitive interface with sensible defaults and guided workflows (e.g., "Extract Here" wizard).
*   **Standard User:** Comfortable with basic computer operations. Uses core create/extract functions and occasionally file utilities.
*   **Advanced User:** Understands compression settings, encryption methods, and uses advanced features like keyfile authentication, batch operations, and checksum verification.

### 2.4 Operating Environment
#### 2.4.1 Software Environment
*   **Primary OS Platforms:**
    *   Microsoft Windows (32-bit and 64-bit editions).
    *   POSIX-compliant operating systems (Linux distributions, BSD variants, and other UNIX-like systems).
*   **Dependencies:** The application depends on the presence of specific open-source archiving utilities (e.g., 7z, peazip). These may be bundled or required to be installed separately.

#### 2.4.2 Hardware Environment
*   **Processor:** An x86-compatible CPU (Intel, AMD, or compatible). This includes both 32-bit (i386) and 64-bit (x86_64) architectures.
*   **Other:** Sufficient RAM and disk space to handle the intended archive and file operations.

### 2.5 Design and Implementation Constraints
1.  **License:** The entire software must be licensed under the GNU LGPL. All dependencies and contributions must be compatible with this license.
2.  **Cross-Platform Consistency:** The GUI and core functionality must remain as consistent as possible between the Windows and POSIX versions, despite underlying OS differences.
3.  **Platform-Specific Feature Limitation:** The drag-and-drop operation **from** the PeaZip application **to** the host operating system's desktop or file manager is explicitly constrained to only function on Microsoft Windows. Drag-and-drop *into* PeaZip and internal drag-and-drop may be supported on all platforms.

### 2.6 Assumptions and Dependencies
*   **Assumption:** Users on POSIX systems have a functional desktop environment with standard GUI libraries (e.g., GTK+, Qt) installed.
*   **Dependency:** The project relies on the continued development and availability of the underlying open-source compression utilities it wraps.

## 3. Specific Requirements

### 3.1 External Interface Requirements
#### 3.1.1 User Interfaces
*   **UI-01:** A main window displaying the system's file tree and archive contents in a dual-pane layout.
*   **UI-02:** Context menus (right-click) for files and archives providing relevant actions (Extract, Add to Archive, etc.).
*   **UI-03:** Dedicated dialog windows for:
    *   Creating/Adding to an archive (with tabs/options for format, compression level, password, keyfile).
    *   Extracting archives (with path selection and overwrite rules).
    *   Configuring application settings.
*   **UI-04:** Support for system drag-and-drop for adding files to the application. Drag-and-drop *from* the application is limited per constraint 2.5.3.

#### 3.1.2 Hardware Interfaces
None beyond standard keyboard, mouse, and display support.

#### 3.1.3 Software Interfaces
*   **SI-01:** The application shall interface via command-line or API with the following (or equivalent) open-source utilities: 7-Zip, Pea, UPX, and other supported archivers.
*   **SI-02:** On POSIX systems, the GUI shall interface with the host's desktop environment for file selection and basic system integration.

#### 3.1.4 Communications Interfaces
Not applicable for this desktop application.

### 3.2 Functional Requirements
#### 3.2.1 Archive Creation & Update
*   **FR-01:** The system shall allow the user to select one or more files/folders from the filesystem and create a new compressed archive.
*   **FR-02:** The system shall present the user with configurable options during creation, including:
    *   Archive format (e.g., 7Z, ZIP, TAR.GZ).
    *   Compression level (e.g., Store, Fast, Normal, Maximum).
    *   Archive password (optional).
    *   Keyfile for encryption (optional, two-factor).
*   **FR-03:** The system shall allow the user to add files to or delete files from an existing archive (for formats supporting modification).

#### 3.2.2 Archive Extraction
*   **FR-04:** The system shall allow the user to select an archive file and extract all or a subset of its contents to a specified directory.
*   **FR-05:** The system shall prompt the user for a password and/or keyfile if the archive is encrypted.
*   **FR-06:** The system shall handle extraction conflicts (e.g., overwrite, rename, skip) based on user preference.

#### 3.2.3 File Management Utilities
*   **FR-07: Secure Deletion:** The system shall provide a tool to overwrite a file's disk space with random data multiple times before deleting it, making recovery improbable.
*   **FR-08: File Split/Join:** The system shall allow splitting a single large file into smaller volumes of a user-defined size and later re-joining those volumes into the original file.
*   **FR-09: Checksum/Hash Calculation:** The system shall calculate and display cryptographic hash values (e.g., MD5, SHA-256, CRC32) for selected files. It shall also verify files against provided hash values.

#### 3.2.4 Security
*   **FR-10:** The system shall support encrypting archives using AES-256 encryption when a password is set.
*   **FR-11:** The system shall support the use of a keyfile as a second authentication factor for archive encryption. The archive must require both the correct password and the exact keyfile to be opened.

### 3.3 Non-Functional Requirements
#### 3.3.1 Performance Requirements
*   **PER-01:** Archive operations (create/extract) shall have performance within 5% of the underlying command-line utility when using the same settings, accounting for GUI overhead.
*   **PER-02:** The GUI shall remain responsive (no "freezing") during long-running operations, providing a progress indicator and the option to cancel.

#### 3.3.2 Safety Requirements
Not applicable.

#### 3.3.3 Security Requirements
*   **SEC-01:** Passwords shall never be stored in plain text. They shall be held only in volatile memory for the duration of the operation.
*   **SEC-02:** The path to a user-selected keyfile shall not be logged or stored persistently in an insecure manner.

#### 3.3.4 Software Quality Attributes
*   **QA-01: Usability:** A novice user shall be able to successfully extract a common archive format (e.g., .zip) within 2 minutes of first launching the application, without consulting documentation.
*   **QA-02: Portability:** The codebase shall be compilable and executable on all target operating systems (Windows 32/64-bit, POSIX) from a single source repository with platform-specific conditionals.
*   **QA-03: Reliability:** The application shall not crash due to malformed archive files. It shall display an appropriate error message to the user.
*   **QA-04: Maintainability:** The code that interfaces with external archiving utilities shall be modular, allowing new archive format support to be added with minimal changes to the core GUI code.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| QA Manager | | | |