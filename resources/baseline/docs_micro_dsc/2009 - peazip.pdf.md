# Software Requirements Specification (SRS) for PeaZip

**Document Version:** 1.0  
**Date:** 2023-10-27  
**Status:** Approved for Development

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for PeaZip, a cross-platform file and archive manager. It serves as a formal agreement between stakeholders, developers, and testers, providing a comprehensive description of the system's intended capabilities, constraints, and operating environment.

### 1.2 Scope
PeaZip is a desktop application that functions as a graphical user interface (GUI) frontend for a suite of open-source command-line compression and file management utilities. Its primary purpose is to simplify the creation, extraction, and management of compressed archives across multiple operating systems, while providing additional file utility functions such as secure deletion and file comparison.

**In-Scope:**
*   GUI for archive creation, update, and extraction.
*   Integration with underlying open-source compression tools (e.g., 7-Zip, p7zip, FreeArc).
*   Secure file deletion and byte-to-byte file comparison features.
*   Cross-platform compatibility (Windows, Linux, BSD).
*   Adherence to specified licensing and hardware constraints.

**Out-of-Scope:**
*   Development of the core compression/decompression algorithms (these are provided by third-party utilities).
*   Functionality dependent on non-x86 CPU architectures (e.g., ARM, RISC-V).
*   Native drag-and-drop from the application to the host system on non-Windows platforms.

### 1.3 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **GUI** | Graphical User Interface. |
| **LGPL** | GNU Lesser General Public License. A free software license that permits linking with proprietary software. |
| **x86** | The family of instruction set architectures based on the Intel 8086 CPU, including 32-bit (IA-32) and 64-bit (x86-64) variants. |
| **Archive** | A single file containing one or more files and/or directories, often compressed. |
| **Frontend** | An application that provides a user-friendly interface to interact with another program (the backend). |

### 1.4 References
*   GNU Lesser General Public License v2.1 or later.
*   Documentation for integrated utilities (7-Zip, p7zip, etc.).

### 1.5 Overview
The remainder of this document is structured as follows:
*   **Section 2:** Overall Description - Provides a high-level perspective of the product, its user characteristics, and constraints.
*   **Section 3:** Specific Requirements - Details all functional and non-functional requirements with precise specifications.

## 2. Overall Description

### 2.1 Product Perspective
PeaZip is a standalone, installable desktop application. It acts as an intermediary layer between the user and multiple backend command-line utilities (`7z`, `tar`, `gzip`, etc.). The system architecture is depicted below:

```
[User] <-> [PeaZip GUI] <-> [Wrapper/CLI Interface] <-> [Open-Source Utilities (7z, arc, etc.)] <-> [File System]
```

### 2.2 Product Functions (High-Level)
1.  **Archive Management:** Create, update, and extract archives in a wide variety of formats.
2.  **File Operations:** Provide secure deletion and binary file comparison beyond standard OS functions.
3.  **System Integration:** Offer a consistent GUI experience across supported operating systems, leveraging native OS features where possible (e.g., Windows shell integration).

### 2.3 User Characteristics
*   **End-Users:** General computer users with basic to intermediate technical skills who need to manage compressed files.
*   **Power Users:** Users who require advanced features like multi-format support, secure deletion, and checksum verification.
*   **Administrators:** System administrators who may deploy or script the use of the application's backend utilities.

### 2.4 Constraints
1.  **Hardware Constraint:** The software must be compatible with and run on x86-compatible CPUs (32-bit or 64-bit).
2.  **Licensing Constraint:** Any modification to the source code of PeaZip must be distributed in compliance with the GNU LGPL. The integrated open-source utilities retain their respective licenses (e.g., 7-Zip uses LGPL).
3.  **Platform-Specific Constraint:** The functionality to drag-and-drop files **from** the PeaZip application interface **to** the host system's desktop or file manager is explicitly required only for the MS Windows version. This feature may be limited or unavailable on Linux and BSD platforms.

### 2.5 Assumptions and Dependencies
*   **Assumption:** The target systems have necessary system libraries (e.g., GTK+, Qt, or native Windows APIs) to support the GUI.
*   **Dependency:** The correct backend compression utilities must be present on the system or bundled with the application for full functionality.
*   **Assumption:** Users have read/write permissions to the directories and files they intend to process.

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 User Interfaces
*   **UI-01:** The application shall present a main window with a dual-pane or single-pane file browser.
*   **UI-02:** It shall provide a context menu (right-click) in the file browser for core functions: "Add to archive...", "Extract here", "Extract to...", "Delete securely", "Compare".
*   **UI-03:** A toolbar shall offer quick access to frequently used actions (Create, Extract, Open).
*   **UI-04:** Dialog windows shall guide users through archive creation (format selection, compression level, password, etc.) and extraction (path selection, overwrite rules).

#### 3.1.2 Hardware Interfaces
*   **HW-01:** The software shall operate on any standard x86-compatible personal computer or virtual machine.

#### 3.1.3 Software Interfaces
*   **SI-01:** The application shall interface with the host operating system's file system APIs.
*   **SI-02:** It shall execute and manage processes for backend command-line utilities (e.g., `7z.exe`, `7za`).
*   **SI-03 (Windows Specific):** It shall implement Windows OLE/COM interfaces to enable drag-and-drop operations from the application to Windows Explorer.

#### 3.1.4 Communications Interfaces
*   Not applicable for this standalone desktop application.

### 3.2 Functional Requirements

#### 3.2.1 Archive Creation and Update
*   **FUNC-AC-01:** The system shall allow the user to select one or more files/directories and create a new compressed archive.
*   **FUNC-AC-02:** The user shall be able to select from multiple archive formats (e.g., 7Z, ZIP, TAR, GZIP, BZIP2, PAQ, ZPAQ).
*   **FUNC-AC-03:** The user shall be able to configure compression level (e.g., Store, Fast, Normal, Maximum, Ultra).
*   **FUNC-AC-04:** The user shall be able to add a password and enable encryption for supported formats (e.g., AES-256 for 7Z/ZIP).
*   **FUNC-AC-05:** The system shall allow updating (adding/removing files) existing archives of supported formats.

#### 3.2.2 Archive Extraction
*   **FUNC-AE-01:** The system shall allow the user to extract the entire contents of a supported archive.
*   **FUNC-AE-02:** The system shall allow the user to selectively extract specific files/folders from within an archive.
*   **FUNC-AE-03:** The user shall be able to choose the destination path for extraction.
*   **FUNC-AE-04:** The system shall handle password-protected archives, prompting the user for a password if required.

#### 3.2.3 File Operations
*   **FUNC-FO-01 (Secure Delete):** The system shall provide a function to overwrite a file's disk space with random data multiple times before deleting it, making recovery extremely difficult.
*   **FUNC-FO-02 (File Compare):** The system shall provide a function to compare two files byte-by-byte and report if they are identical or highlight the differences.

#### 3.2.4 System Interaction
*   **FUNC-SI-01 (Drag-and-Drop):** On Microsoft Windows, the system shall support dragging files from the PeaZip application window and dropping them onto the Windows desktop or file explorer windows.

### 3.3 Non-Functional Requirements

#### 3.3.1 Performance Requirements
*   **PERF-01:** Archive creation and extraction speed shall be primarily dependent on the performance of the underlying backend utilities. The GUI shall not introduce significant overhead (>5% time penalty in benchmark tests).
*   **PERF-02:** The GUI shall remain responsive (no "Not Responding" state) during long-running compression/decompression operations, providing progress feedback and allowing cancellation.

#### 3.3.2 Safety & Security Requirements
*   **SEC-01:** Passwords entered for archive encryption shall not be stored persistently in plain text.
*   **SEC-02:** The secure delete function shall implement a recognized algorithm (e.g., DoD 5220.22-M, Gutmann) as configured by the user.

#### 3.3.3 Software Quality Attributes
*   **QUAL-01 (Portability):** The core application logic shall be written in a portable language (e.g., Free Pascal/Object Pascal) to facilitate compilation for Windows, Linux, and BSD.
*   **QUAL-02 (Maintainability):** The source code shall be modular, clearly separating GUI code from the logic that interfaces with backend utilities.
*   **QUAL-03 (Usability):** The user interface shall be intuitive for common tasks, with advanced options available in dedicated dialog boxes.

#### 3.3.4 Legal & Compliance Requirements
*   **LEGAL-01:** The entire application, including any modified source code, shall be distributed under the terms of the GNU LGPL license.
*   **LEGAL-02:** All bundled third-party open-source utilities shall be distributed in compliance with their respective licenses, with appropriate attribution.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner | | | |
| Lead Developer | | | |
| QA Manager | | | |