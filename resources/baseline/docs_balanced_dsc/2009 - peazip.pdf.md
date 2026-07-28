# Software Requirements Specification (SRS)
## PeaZip 2.7.1 - Cross-Platform Archive Manager

**Document Version:** 1.0
**Date:** [Current Date]
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for PeaZip version 2.7.1. It serves as a comprehensive guide for stakeholders, developers, testers, and project managers involved in the development, maintenance, and use of the application. The primary audience includes the development team and project maintainers.

#### 1.2 Project Scope
PeaZip is a cross-platform, open-source file and archive manager. Its core purpose is to provide a unified graphical user interface (GUI) for a wide array of open-source archiving and compression utilities. The application enables users to create, extract, and manage archives across numerous formats, while also offering supplementary file management tools such as secure deletion, file comparison, and checksum verification.

**In-Scope:**
*   Development and maintenance of the core GUI application using Lazarus IDE/Object Pascal.
*   Integration of bundled, open-source backend utilities for compression, extraction, and file operations.
*   Support for creating, updating, browsing, and extracting from a defined set of archive formats.
*   Implementation of file management tools (secure delete, compare, checksum/hash).
*   Provision of a portable application package requiring no installation.
*   Configuration and customization of application settings and interface.

**Out-of-Scope:**
*   Development of the underlying compression/encryption algorithms (relies on integrated utilities).
*   Native cloud storage or network drive integration (see Undecided Issues).
*   Advanced scripting or automation interfaces beyond existing command-line output.
*   Creation of operating system kernel modules or deep system integration.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **GUI:** Graphical User Interface.
*   **SRS:** Software Requirements Specification.
*   **POSIX:** Portable Operating System Interface.
*   **GTK/GDK:** GIMP Toolkit / GIMP Drawing Kit (GUI libraries).
*   **LZMA:** Lempel–Ziv–Markov chain Algorithm.
*   **PAQ:** A family of high-compression algorithms.
*   **PeaLauncher:** The PeaZip graphical wrapper/process manager for executing operations.

#### 1.4 References
*   Lazarus IDE Documentation
*   GTK/GDK Library Documentation
*   Underlying Utility Documentation (e.g., 7-Zip, p7zip, FreeArc, UPX)

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product, its users, and constraints. Section 3 details the specific functional requirements. Section 4 outlines the non-functional requirements. Appendices may contain supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
PeaZip is a standalone, self-contained desktop application. It acts as a meta-tool, integrating multiple independent command-line utilities under a single GUI. It is independent of other applications but relies on system-provided GUI libraries (e.g., GTK) and runtime environments.

#### 2.2 User Classes and Characteristics
1.  **End User:**
    *   **Primary Actor.** Possesses varying levels of technical expertise.
    *   **Needs:** To easily manage archives and files, with options for security (encryption, secure delete) and customization.
    *   **Frequency:** Regular use for file management tasks.

2.  **Software Engineer/Developer:**
    *   **Secondary Actor.** Contributes to the open-source project.
    *   **Characteristics:** Proficient in Object Pascal/Delphi and the Lazarus IDE.
    *   **Needs:** A well-structured, documented codebase to facilitate development and maintenance.

3.  **Project Maintainer:**
    *   **Stakeholder.** Oversees project direction, core development, and utility integration.
    *   **Responsibilities:** Release management, architectural decisions, and community coordination.

#### 2.3 Operating Environment
*   **Software:** Must operate on 32-bit and 64-bit versions of:
    *   Microsoft Windows (e.g., Windows 7, 8, 10, 11)
    *   Linux distributions (via GTK/GDK libraries)
    *   BSD systems (via GTK/GDK libraries)
    *   Other POSIX-compliant operating systems
*   **Hardware:** Must function on standard PC hardware. Performance scales with CPU, RAM, and storage speed, particularly during compression/decompression.

#### 2.4 Design and Implementation Constraints
1.  **Implementation Language:** Core application must be developed in Object Pascal using the Lazarus IDE.
2.  **Portability:** Application must be distributable as a portable package with no formal installation process.
3.  **License:** The application and its integrated utilities must comply with open-source licensing models (e.g., LGPL).
4.  **Dependency Management:** All necessary backend utilities must be bundled; the application cannot require separate user installation of compression tools.

#### 2.5 User Documentation
Comprehensive user documentation shall be provided, including:
*   Integrated help files accessible from within the application.
*   Online tutorials and usage guides.
*   Command-line interface documentation for advanced users.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** Target systems have standard graphical desktop environments capable of running GTK/GDK-based applications (for Linux/BSD versions).
*   **Dependency:** The functionality for specific archive formats is dependent on the capabilities and stability of the underlying open-source utilities (e.g., 7-Zip).

### 3. System Features and Requirements

#### 3.1 Feature: File System Navigation and Selection
**Description:** The application shall provide a graphical file manager for browsing the filesystem and selecting objects for operations.

**Functional Requirements:**
*   **FR-1:** The system shall display a hierarchical view of directories and files.
*   **FR-2:** The system shall allow navigation via tree view, address bar, and history (back/forward).
*   **FR-3:** The system shall support standard file selection methods (click, Ctrl+click, Shift+click, drag-select).
*   **FR-4:** The system shall display core properties (name, size, type, modified date) for selected objects.

#### 3.2 Feature: Archive Creation and Update
**Description:** The user shall be able to create new archives or add files to existing archives from selected filesystem objects.

**Functional Requirements:**
*   **FR-10:** The system shall provide a dialog for creating a new archive, allowing the user to set:
    *   Archive name and output path.
    *   Archive format (e.g., 7Z, ZIP, TAR, PEZ).
    *   Compression level and method (e.g., Store, LZMA, PPMd).
    *   Encryption (password and optional keyfile).
    *   Archive splitting size.
    *   Additional options (e.g., solid archive, preserve paths).
*   **FR-11:** The system shall allow adding files to an existing compatible archive.
*   **FR-12:** The system shall validate user inputs (e.g., password strength, path validity) before starting the operation.

#### 3.3 Feature: Archive Extraction and Browsing
**Description:** The user shall be able to view the contents of an archive and extract them to a specified location.

**Functional Requirements:**
*   **FR-20:** The system shall allow an archive to be opened and its internal structure browsed in the file manager pane.
*   **FR-21:** The system shall provide an extraction dialog to specify:
    *   Output path.
    *   File overwrite behavior.
    *   Specific files to extract (if not extracting all).
*   **FR-22:** The system shall require valid credentials (password/keyfile) to extract or browse encrypted archives.
*   **FR-23:** The system shall support extracting from archives split across multiple volumes.

#### 3.4 Feature: File Management Tools
**Description:** The application shall provide utilities for file operations beyond archiving.

**Functional Requirements:**
*   **FR-30:** **Secure Delete:** The system shall permanently erase selected files/directories using a method that renders recovery infeasible. The specific algorithm and number of passes is an undecided issue (see Section 5.1).
*   **FR-31:** **File Compare:** The system shall compare two selected files and report differences (binary or textual).
*   **FR-32:** **Checksum/Hash:** The system shall calculate and verify cryptographic hash values (e.g., MD5, SHA-1, SHA-256, SHA-512) for selected files.

#### 3.5 Feature: Configuration and Settings
**Description:** The user shall be able to customize the application's behavior and interface.

**Functional Requirements:**
*   **FR-40:** The system shall provide a settings interface to modify:
    *   Default archive format and compression settings.
    *   Interface language and theme.
    *   Toolbar and menu configuration.
    *   PeaLauncher behavior (priority, window focus).
    *   File associations.
*   **FR-41:** The system shall allow settings to be saved to and loaded from named profiles.

#### 3.6 Feature: Operation Execution and Monitoring
**Description:** The system shall execute user-initiated operations and provide feedback on their progress and outcome.

**Functional Requirements:**
*   **FR-50:** The PeaLauncher component shall manage the execution of all backend utility jobs.
*   **FR-51:** The system shall display a progress dialog for long-running operations, showing:
    *   Overall progress percentage.
    *   Current file being processed.
    *   Estimated time remaining.
    *   Option to pause or cancel the operation.
*   **FR-52:** The system shall present a summary report upon job completion, indicating success, failure, or any errors encountered.
*   **FR-53:** The system shall log operation details (Job ID, Type, Target, Status, Result) for user reference.

### 4. Non-Functional Requirements

#### 4.1 Usability
*   **NFR-U1:** The interface shall be intuitive enough for a novice user to perform basic archive extraction and creation with minimal guidance.
*   **NFR-U2:** Advanced options shall be accessible but not obtrusive for basic tasks.
*   **NFR-U3:** Context-sensitive help shall be available for major dialog options.

#### 4.2 Performance
*   **NFR-P1:** The GUI shall remain responsive during long compression/decompression operations (the heavy processing is offloaded to backend utilities).
*   **NFR-P2:** The application startup time shall be under 5 seconds on average hardware.

#### 4.3 Security
*   **NFR-S1:** Encryption keys (passwords) shall never be written to disk in plaintext. They shall only be held in volatile memory for the duration of the operation.
*   **NFR-S2:** The secure delete function shall meet or exceed the data sanitization standard of a single-pass overwrite with random data, pending final algorithm selection.
*   **NFR-S3:** The application shall not execute or unpack archive contents automatically to prevent potential malware execution.

#### 4.4 Compatibility & Portability
*   **NFR-C1:** The Windows version shall be distributable as a standalone `.exe` or portable package.
*   **NFR-C2:** The Linux/BSD version shall be distributable as a self-contained tarball or via platform-specific packages (e.g., `.deb`, `.rpm`).
*   **NFR-C3:** User settings and profiles shall be stored in a platform-independent format within the application's portable directory.

#### 4.5 Reliability
*   **NFR-R1:** The application shall handle corrupt or malformed archive files gracefully, providing an informative error message without crashing.
*   **NFR-R2:** Operations shall be atomic where possible; a failed archive creation shall not leave a partially written archive file that appears valid.

#### 4.6 Error Handling
*   **NFR-E1:** All user-facing error messages shall be clear, informative, and suggest a possible corrective action.
*   **NFR-E2:** Internal errors shall be logged with technical details for developer diagnosis.

### 5. Other Requirements

#### 5.1 Undecided Issues / Open Questions
1.  **Supported Formats:** The final list of archive formats for read/write, read-only, and write-only support requires definition.
2.  **Secure Delete Specification:** The exact algorithm(s) (e.g., DoD 5220.22-M, Gutmann) and number of passes for the secure delete function must be finalized.
3.  **Advanced Integration:** The feasibility and scope of integrating network drive browsing or cloud storage APIs need investigation.
4.  **Scripting Interface:** Requirements for a more advanced batch scripting interface, beyond generating command-line calls, should be explored.
5.  **Localization Framework:** The process for adding new language translations must be formalized.
6.  **Long-term OS Support:** A strategy for testing and adapting to new major OS versions post-release is required.

#### 5.2 Appendices
*   **Appendix A: Data Dictionary** (Based on Domain Data Elements from input).
*   **Appendix B: Supported Format Matrix** (To be populated upon resolution of Undecided Issue #1).
*   **Appendix C: Use Case Diagrams** (Graphical representation of Key Processes).

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Maintainer | | | |
| Lead Developer | | | |
| QA Lead | | | |