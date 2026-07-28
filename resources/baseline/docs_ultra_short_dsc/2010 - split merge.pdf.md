# Software Requirements Specification (SRS)
## For: PDF Manipulation Tool (Open-Source Desktop Application)

**Document Version:** 1.0  
**Date:** [Current Date]  
**Status:** Approved

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for a free, open-source desktop application designed for manipulating Portable Document Format (PDF) files. The primary purpose of this document is to provide a complete description of the system's intended capabilities, interfaces, and performance characteristics. It serves as a reference for developers, testers, project managers, and stakeholders throughout the software development lifecycle.

### 1.2 Document Conventions
*   **Requirements:** Functional requirements are labeled as `FR-[Number]`. Non-functional requirements are labeled as `NFR-[Number]`.
*   **Priority:** All requirements listed in this document are of **High** priority and are considered implemented in the current version.
*   **Keywords:** The keywords `MUST`, `MUST NOT`, `SHALL`, `SHALL NOT`, `WILL`, and `WILL NOT` are to be interpreted as described in RFC 2119.

### 1.3 Project Scope
The system is a standalone desktop application that provides core PDF file manipulation functions through both a Graphical User Interface (GUI) and a Command-Line Interface (CLI). Its scope is strictly limited to the structural manipulation of PDF documents, including splitting, merging, reordering, and rotating pages. The system **does not** edit the internal content of PDF pages (e.g., modifying text, images, or annotations). It **does not** implement user management, authentication, or document-level security features of its own. All operations are non-destructive to source files.

### 1.4 Product Background and Positioning
This product is positioned as a free and open-source alternative to commercial PDF manipulation tools. Built on the Java platform, it achieves platform independence, allowing it to run on any operating system with a compatible Java Runtime Environment (JRE). The software is released under the GNU General Public License version 2 (GPLv2), ensuring it remains free and its source code is accessible for modification and distribution. An enhanced version of this application with extended capabilities exists separately.

## 2. Overall Description

### 2.1 Product Perspective
The application is a self-contained, installable desktop tool. It operates within the host operating system's environment, interacting primarily with the local file system for input and output. Its architecture is modular, allowing for potential future extensions via a plugin system (as implied by environment save/load functionality).

### 2.2 Product Functions (High-Level Summary)
1.  Split a single PDF document based on various criteria.
2.  Merge multiple PDF documents or selected page ranges.
3.  Interleave (alternate mix) pages from two source PDFs.
4.  Rotate pages within one or more documents.
5.  Provide a visual interface for direct page manipulation (reorder, rotate, delete, compose).
6.  Manage application state by saving and loading the working environment.
7.  Configure application settings and preferences.

### 2.3 User Classes and Characteristics
| User Class | Characteristics | Primary Interface |
| :--- | :--- | :--- |
| **General End-User** | Needs to perform common PDF tasks (split large scans, merge reports, reorder pages). Has basic computer literacy but may not be technically advanced. Prefers intuitive, visual interaction. | Graphical User Interface (GUI) |
| **Advanced User / System Administrator** | Requires automation, batch processing, or server-side integration. Comfortable with command-line tools and scripting. | Command-Line Interface (CLI) |
| **Contributor (Developer, Translator)** | Part of the open-source community. Works with the source code to fix bugs, add features, or provide localization. | N/A (External to application runtime) |

### 2.4 Operating Environment
*   **Software:** Java Runtime Environment (JRE) version 1.6 or higher.
*   **Operating Systems:** Any OS with a compatible JVM. Specifically tested and supported on:
    *   Microsoft Windows (XP and later)
    *   GNU/Linux (various distributions)
    *   Apple Mac OS X
*   **Hardware:** Standard hardware capable of running the host OS and JRE.

### 2.5 Design and Implementation Constraints
1.  The application **MUST** be developed in the Java programming language.
2.  The primary GUI **MUST** be implemented using the Java Swing toolkit.
3.  The application **MUST** be distributed under the GNU GPLv2 license.
4.  The application **MUST NOT** modify source PDF files directly; all output must be written to new files.

### 2.6 Assumptions and Dependencies
*   **Assumption:** All input files provided by the user are valid, well-formed PDF documents.
*   **Dependency:** A compatible JRE (1.6+) is pre-installed on the end-user's system.
*   **Dependency:** The application depends on underlying Java PDF libraries (e.g., iText, PDFBox) for low-level PDF processing, though these are not specified in the input and are considered an internal implementation detail for this SRS.

## 3. External Interface Requirements

### 3.1 User Interfaces
*   **Graphical User Interface (GUI):** A window-based interface built with Java Swing. It shall include menus, toolbars, dialog boxes, and a main workspace area for visual page manipulation (e.g., thumbnail view). It must support internationalization (i18n).
*   **Command-Line Interface (CLI):** A console application executable (`java -jar` or native script). It shall accept arguments and options to perform all core functions without graphical interaction, suitable for scripting.

### 3.2 Hardware Interfaces
None. The application interacts only with standard hardware through the host OS and JVM.

### 3.3 Software Interfaces
*   **Java Runtime Environment (JRE):** Interface with JRE 1.6+ APIs.
*   **Local File System:** Read input PDF files and write output PDF files.
*   **Network (Optional):** HTTP/HTTPS connection to a remote server to check for available application updates.

### 3.4 Communications Interfaces
The network update check will use standard HTTP/HTTPS protocols.

## 4. System Features

This section details the functional requirements.

### 4.1 Feature: Split PDF Documents
**Description:** The system shall allow the user to divide a single input PDF document into multiple output documents based on specified criteria.

**Requirements:**
*   `FR-1.1` The system shall provide a GUI dialog and CLI parameter to select a source PDF file for splitting.
*   `FR-1.2` The system shall support splitting by fixed page ranges (e.g., pages 1-5, 6-10).
*   `FR-1.3` The system shall support splitting by maximum file size (e.g., split into ~5MB chunks).
*   `FR-1.4` The system shall support splitting by top-level bookmarks present in the source document.
*   `FR-1.5` The system shall allow the user to specify an output directory and filename prefix for the resulting documents.
*   `FR-1.6` The system shall generate one new PDF file for each split segment.

### 4.2 Feature: Merge PDF Documents
**Description:** The system shall allow the user to combine multiple PDF source files, or selected pages from them, into a single output PDF document.

**Requirements:**
*   `FR-2.1` The system shall provide an interface to select and order multiple source PDF files.
*   `FR-2.2` The system shall allow the user to merge entire documents in the selected order.
*   `FR-2.3` The system shall allow the user to specify page ranges (e.g., "1, 3-5, 12") from each source document to include in the merge.
*   `FR-2.4` The system shall allow the user to specify the filename and location of the single output merged PDF.

### 4.3 Feature: Alternate / Mix Pages
**Description:** The system shall create a new document by interleaving pages from exactly two source PDF documents.

**Requirements:**
*   `FR-3.1` The system shall provide an interface to select exactly two source PDF files (Document A and Document B).
*   `FR-3.2` The system shall allow the user to define the alternation pattern (e.g., A1, B1, A2, B2... or A1, A2, B1, B2...).
*   `FR-3.3` The system shall handle source documents with differing page counts, applying the pattern until pages from one document are exhausted, then appending the remaining pages from the other document.

### 4.4 Feature: Rotate Pages
**Description:** The system shall apply rotation (90°, 180°, 270°) to pages within one or more documents.

**Requirements:**
*   `FR-4.1` The system shall allow rotation of all pages within a selected document.
*   `FR-4.2` The system shall allow selective rotation of only even-numbered or only odd-numbered pages within a document.
*   `FR-4.3` The system shall allow the user to apply the same rotation operation to multiple selected documents in batch.
*   `FR-4.4` The system shall provide visual feedback in the GUI showing the rotation state of pages.

### 4.5 Feature: Visual Page Manipulation
**Description:** The system shall provide a dedicated GUI workspace for interactive manipulation of pages.

**Requirements:**
*   `FR-5.1` **Visual Reorder:** The user shall be able to drag and drop page thumbnails within a single document to change their order.
*   `FR-5.2` **Visual Delete:** The user shall be able to select one or more page thumbnails and delete them from the working document.
*   `FR-5.3` **Visual Rotate:** The user shall be able to select one or more page thumbnails and apply a rotation directly.
*   `FR-5.4` **Visual Compose:** The user shall be able to open multiple source documents and drag pages from their thumbnails into a new, composite document preview.

### 4.6 Feature: Environment Management
**Description:** The system shall allow saving and restoring the complete state of a working session.

**Requirements:**
*   `FR-6.1` The system shall allow the user to save the current workspace state to a proprietary project file. This state includes:
    *   List of open source documents.
    *   Current page selection and order for visual composition.
    *   States of any active plugins or tools.
    *   Undo/redo history (if applicable).
*   `FR-6.2` The system shall allow the user to load a previously saved project file and restore the workspace to the exact saved state.

### 4.7 Feature: Application Configuration
**Description:** The system shall provide a settings dialog for user preferences.

**Requirements:**
*   `FR-7.1` The system shall allow the user to change the application's user interface language.
*   `FR-7.2` The system shall allow the user to modify the visual look and feel (theme) of the Swing interface.
*   `FR-7.3` The system shall allow the user to set default input and output directories.
*   `FR-7.4` The system shall allow the user to configure logging verbosity and log file location.

## 5. Non-Functional Requirements

### 5.1 Performance Requirements
*   `NFR-1` **Non-Destructive Operation:** The application **MUST NOT** alter, overwrite, or delete any user-specified input PDF file. All results **MUST** be written to new output files specified by the user.
*   `NFR-2` The application shall handle PDF documents of typical size (up to 500 pages, 100MB) without excessive memory consumption or unresponsive UI. For the CLI, progress should be indicated.

### 5.2 Reliability Requirements
*   `NFR-3` The application shall validate all user input (file paths, page numbers, parameters) and provide clear, informative error messages for invalid input without crashing.
*   `NFR-4` The application shall handle malformed or encrypted PDFs gracefully, informing the user of the specific problem (e.g., "File is encrypted and cannot be processed").

### 5.3 Portability Requirements
*   `NFR-5` The application **SHALL** be platform-independent and run on any operating system with a JVM compatible with JRE 1.6 specifications.
*   `NFR-6` The application's installation and execution **SHALL NOT** require administrator/root privileges for standard operations.

### 5.4 Maintainability & Legal Requirements
*   `NFR-7` The complete application source code **MUST** be publicly available and open for inspection and modification.
*   `NFR-8` The application **MUST** be distributed under the terms of the GNU General Public License version 2 (GPLv2).

### 5.5 Usability Requirements
*   `NFR-9` The GUI shall follow common desktop application conventions for its host OS where possible.
*   `NFR-10` The CLI shall provide a `--help` or `-h` option that prints usage instructions.

## 6. Acceptance Criteria

Acceptance of the system is based on the successful execution of test cases derived from this SRS. Core acceptance tests include:

1.  **Split Test:** Given a 20-page PDF, split by every 5 pages. Result: Four new PDFs of 5 pages each are created. Source file remains unchanged.
2.  **Merge Test:** Given three PDFs (A:3p, B:2p, C:4p), merge entirely. Result: One new 9-page PDF with pages in order A1-A3, B1-B2, C1-C4.
3.  **Rotate Test:** Given a PDF, rotate all pages 90° clockwise. Result: New PDF displays all pages rotated correctly. Source file orientation is unchanged.
4.  **CLI Batch Test:** Using the CLI, successfully merge a list of 10 PDFs specified in a script.
5.  **Error Handling Test:** Attempt to process a non-PDF file or specify a non-existent page number. Result: A clear error message is displayed, and no output file is created or source file altered.
6.  **Portability Test:** The same application JAR file executes core functions on Windows, Linux, and macOS systems with their respective JREs installed.

---
*This SRS document is considered complete for the current version of the application. Future enhancements will require a formal change management and prioritization process.*