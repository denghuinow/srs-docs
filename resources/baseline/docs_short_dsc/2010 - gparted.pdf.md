# Software Requirements Specification (SRS)
## GParted LiveCD Version 0.6.0-1

**Document Version:** 1.0
**Date:** [Current Date]
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the functional and non-functional requirements for GParted (GNOME Partition Editor) version 0.6.0-1. It is intended for use by stakeholders, including developers, testers, documentation writers, and project managers, to ensure a common understanding of the system's capabilities, constraints, and objectives.

#### 1.2 Document Conventions
*   **Requirements IDs:** Functional requirements are prefixed with `FR-`. Non-functional requirements are prefixed with `NFR-`.
*   **Keywords:** The terms "MUST," "SHALL," "REQUIRED," "SHOULD," "MAY," and "OPTIONAL" are to be interpreted as described in IETF RFC 2119.
*   **User Interface (UI):** References to UI elements are shown in *italics*.

#### 1.3 Project Scope
GParted 0.6.0-1 is a graphical partition editor distributed as a bootable LiveCD/USB image. It provides a user-friendly frontend to the `libparted` library and other file system tools for managing disk partitions without requiring installation on a host operating system. The core value is enabling safe disk manipulation for tasks such as disk preparation, resizing, and data migration.

**In-Scope Features:**
*   Core partition operations (create, delete, resize/move, copy, format, label).
*   Support for multiple file systems (e.g., ext2/3/4, FAT16/32, NTFS).
*   Management of partition tables (msdos, gpt) and flags (boot, hidden).
*   Basic system utilities integrated into the Live environment.
*   A graphical user interface with pending operations management.

**Out-of-Scope Features:**
*   Logical Volume Management (LVM2).
*   Operations on file systems not supported by underlying tools (`libparted`, `mkfs`, `ntfsprogs`, etc.).
*   Permanent installation onto a hard drive.
*   Advanced networking or remote management.
*   Data recovery or backup services.

#### 1.4 References
*   GNU Parted Library (`libparted`) Documentation.
*   GParted Project Website and Wiki.
*   IETF RFC 2119: Key words for use in RFCs to Indicate Requirement Levels.

### 2. Overall Description

#### 2.1 Product Perspective
GParted is a self-contained, standalone system. It operates independently of any host OS by booting a minimal Linux environment from removable media. It interacts directly with system hardware (disk controllers, drives) via the Linux kernel and leverages external libraries (`libparted`) and command-line tools for specific file system operations.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Primary Goals |
| :--- | :--- | :--- |
| **Casual User** | Has basic computer literacy. Understands concepts of disks, partitions, and file systems. Not a system administrator. | Perform common partition tasks safely and intuitively without using command-line tools. |
| **Developer** | Skilled in C++, GTK+, and Linux system programming. Familiar with the GParted codebase and `libparted`. | Extend functionality, fix bugs, and improve code maintainability. |
| **Tester** | Understands software testing methodologies and partition management concepts. | Verify all features work as specified and identify defects. |
| **Documentation Writer** | Skilled in technical writing. Understands the user's perspective. | Produce accurate and helpful user guides and help content. |

#### 2.3 Operating Environment
*   **Hardware:** Standard x86 and x86-64 based personal computers.
*   **Boot Media:** CD/D-ROM or USB flash drive.
*   **Runtime Environment:** A custom, lightweight Linux distribution (LiveCD/USB environment).
*   **Dependencies:** GNU Parted library (`libparted`), GTK+ 2.x, and optional file system tools (e.g., `e2fsprogs`, `dosfstools`, `ntfsprogs`).

#### 2.4 Design and Implementation Constraints
1.  **C1:** The application SHALL function entirely from read-only boot media without installing files to a persistent hard drive.
2.  **C2:** All partition operations SHALL be performed through the `libparted` API or other well-defined command-line utilities. The application SHALL NOT implement low-level disk I/O directly.
3.  **C3:** The graphical user interface SHALL be built using the GTK+ 2.x toolkit.
4.  **C4:** Feature support for a given file system operation is constrained by the capabilities and presence of the underlying system tool (e.g., `ntfsresize` must be present for NTFS resize).

#### 2.5 Assumptions and Dependencies
*   The user's system BIOS/UEFI is configured to boot from the selected CD/DVD or USB media.
*   The target disk hardware is compatible with the standard Linux kernel drivers included in the Live environment.
*   The user possesses the prerequisite knowledge to understand the risks of partition manipulation (potential data loss).

### 3. System Features and Requirements

#### 3.1 Feature: Disk and Partition Visualization
**Description:** The application shall provide a clear graphical and textual representation of all detected storage devices and their partition layout.

| Requirement ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-1** | The main window SHALL display a list of all detected block storage devices (e.g., `/dev/sda`, `/dev/sdb`). | High |
| **FR-2** | Selecting a device from the list SHALL display a graphical partition map (bar representation) for that device. | High |
| **FR-3** | The partition map SHALL visually distinguish between partition table types (e.g., msdos vs. gpt), allocated space, and unallocated space. | High |
| **FR-4** | The application SHALL display detailed information for the selected device (model, size, path) and selected partition (file system, size, used space, flags). | High |
| **NFR-1** | The UI SHALL update the device list and graphical display within 2 seconds of a storage hardware change (e.g., USB drive connected). | Medium |

#### 3.2 Feature: Core Partition Operations
**Description:** The application shall allow users to modify partition tables and partitions through a set of core operations.

| Requirement ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-5** | The user SHALL be able to create a new partition table (msdos or gpt) on a selected device, with a clear warning that this will destroy all existing data. | High |
| **FR-6** | The user SHALL be able to create a new partition within unallocated space, specifying size, alignment, file system type, and label. | High |
| **FR-7** | The user SHALL be able to delete an existing partition. A confirmation dialog SHALL be required. | High |
| **FR-8** | The user SHALL be able to resize or move an existing partition (subject to **C4**), using a graphical drag interface or numerical input. | High |
| **FR-9** | The user SHALL be able to format a selected partition to a supported file system type (subject to **C4**), with the option to set a label. | High |
| **FR-10** | The user SHALL be able to manage partition flags (e.g., `boot`, `hidden`, `lba`) for partitions on supported partition tables. | Medium |
| **FR-11** | The user SHALL be able to copy the sector-by-sector content of a partition and paste it to unallocated space on the same or a different device. | Medium |
| **NFR-2** | For operations that risk data loss (delete, create table, format), the application SHALL require explicit user confirmation in a modal dialog. | High |
| **NFR-3** | The application SHALL prevent the user from scheduling impossible operations (e.g., overlapping partitions, resize beyond device capacity) by validating parameters before adding to the pending queue. | High |

#### 3.3 Feature: Pending Operations Management
**Description:** The application shall queue all requested changes and allow the user to review and apply them as a single batch.

| Requirement ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-12** | All user-requested operations SHALL be added to a pending operations list without immediately executing them on the disk. | High |
| **FR-13** | The pending operations list SHALL be visible to the user, showing the sequence of operations to be performed. | High |
| **FR-14** | The user SHALL be able to remove any operation from the pending list (*Undo*). | High |
| **FR-15** | The user SHALL be able to clear the entire pending operations list. | Medium |
| **FR-16** | Upon user command (*Apply*), the application SHALL execute all pending operations in the listed sequence. A final confirmation SHALL be required before writing to disk. | High |
| **NFR-4** | During batch execution, the application SHALL provide a progress dialog indicating the current operation and overall progress. | Medium |

#### 3.4 Feature: LiveCD System Utilities
**Description:** The application shall include basic utilities useful in a system recovery or maintenance context.

| Requirement ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-17** | The user SHALL be able to launch a system terminal from within the application. | Low |
| **FR-18** | The user SHALL be able to capture a screenshot of the GParted window and save it to a user-selected location (e.g., removable media). | Low |
| **FR-19** | The application SHALL provide an option to view detailed system information (e.g., kernel version, `libparted` version). | Low |

#### 3.5 Feature: File System and Tool Support
**Description:** The application's capabilities for specific file systems are determined by the presence of external tools.

| Requirement ID | Requirement Description | Priority |
| :--- | :--- | :--- |
| **FR-20** | The application SHALL support the following file systems for creation, formatting, and labeling (minimum): ext2, ext3, ext4, FAT16, FAT32, NTFS. | High |
| **FR-21** | Support for resize/move and copy operations SHALL be dynamically enabled or disabled in the UI based on the detection of the corresponding required tool (e.g., `ntfsresize` for NTFS). | High |
| **FR-22** | The *Help -> Contents* menu SHALL include a "Feature Overview" document that maps file system operations to the required external tools. | Medium |

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Main Window:** Contains menu bar, toolbar, device list pane, graphical partition map, and information panel.
*   **Dialogs:** Modal dialogs for each partition operation (Create, Resize/Move, Format, etc.), featuring appropriate controls (spin boxes, drop-downs, text entries).
*   **Pending Operations Pane:** A dedicated section or window listing queued operations with *Undo* buttons.
*   **Progress Dialog:** A non-interactive dialog showing operation progress during batch execution.

#### 4.2 Software Interfaces
*   **libparted (v1.8.0+):** Primary API for partition table manipulation, geometry calculation, and basic file system operations.
*   **Linux Kernel Block Layer:** Accessed via `/dev` nodes for low-level disk access performed by `libparted` and file system tools.
*   **File System Management Tools:** Executed via command-line (e.g., `mkfs.ext4`, `ntfsresize`, `dosfslabel`). GParted must parse their stdout/stderr for success/failure.

#### 4.3 Hardware Interfaces
*   The application interacts with storage hardware via standard Linux kernel drivers (AHCI, SATA, NVMe, USB Mass Storage) exposed as block devices (e.g., `/dev/sdX`, `/dev/nvmeXnY`).

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   The GUI SHALL remain responsive (no freezing for >1 second) while scanning devices or performing in-memory calculations for complex resize operations.
*   The time to apply operations is dependent on disk speed, tool speed, and data size, but the UI SHALL provide accurate progress feedback.

#### 5.2 Safety & Reliability Requirements
*   The application SHALL NOT allow the user to apply operations to a mounted partition (except for certain read-only checks). It SHALL attempt to unmount partitions automatically or provide clear instructions.
*   All disk writes SHALL be preceded by validation of the entire operation queue for logical consistency.
*   In the event of a tool failure during batch execution, the application SHALL halt the process, report the exact error to the user, and leave the disk in a well-defined state (preferably rolled back to the point before the failed operation, if possible).

#### 5.3 Usability Requirements
*   Common tasks (delete, format) SHALL be accessible in 3 or fewer clicks from the main window.
*   The graphical partition map SHALL provide visual feedback (highlighting, tooltips) during drag operations for resizing/moving.
*   Error messages SHALL be phrased in user-understandable language, avoiding raw kernel or library error codes where possible.

#### 5.4 Deployment Requirements
*   The final deliverable SHALL be a bootable ISO 9660 image file suitable for burning to CD/DVD or writing to a USB drive via `dd` or similar tools.
*   The Live environment SHALL automatically launch the GParted application on boot without requiring user intervention.

---
### Appendix A: Glossary
*   **LiveCD:** A complete operating system that runs from removable media without installation.
*   **Partition Table:** A data structure on a disk that defines the layout of partitions (e.g., MSDOS/MBR, GPT).
*   **Unallocated Space:** Disk space not assigned to any partition.
*   **libparted:** The GNU partition editing library providing the core logic for partition manipulation.

### Appendix B: Open Issues / Undecided Items
1.  Implementation timeline and technical design for LVM2 support.
2.  Prioritization list for new file system support (e.g., exFAT, Btrfs, ZFS).
3.  Specific UI/UX improvements to be targeted in the next design cycle.
4.  Enhancement of error recovery mechanisms for failed multi-step operations.
5.  Strategy for providing UEFI Secure Boot compatibility for the Live image.