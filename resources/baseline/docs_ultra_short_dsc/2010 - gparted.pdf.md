# Software Requirements Specification (SRS)
## Graphical Partition Editor (GParted Frontend)

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for a graphical partition editor application. The primary purpose of this system is to provide an intuitive, graphical user interface for disk partition management, serving as a frontend to the GNU Parted library (`libparted`). This document is intended for use by the project stakeholders, developers, testers, and technical writers involved in the design, implementation, and validation of the system.

#### 1.2 Scope
The system, a Linux-based application, will enable users to perform disk partition operations including creation, deletion, reorganization, and formatting. It operates as a transient application from a LiveCD/USB environment, loading entirely into RAM and leaving no trace on the host system after reboot.

**In-Scope:**
*   Graphical management of partition tables (e.g., MS-DOS, GPT).
*   Core partition operations: create, delete, resize, move, copy, and paste.
*   Partition formatting for a variety of file systems using underlying tools.
*   File system checking and repair.
*   Management of partition flags (e.g., boot, hidden).
*   Operation on directly attached storage devices (HDD, SSD, USB drives).

**Out-of-Scope:**
*   Logical Volume Management (LVM2) support.
*   Network-attached storage management.
*   Persistent installation or configuration on a host hard drive.
*   Advanced RAID configuration or management.
*   Data recovery from corrupted partitions.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **GPT:** GUID Partition Table.
*   **GUI:** Graphical User Interface.
*   **Gtkmm:** C++ interface for the GTK+ GUI library.
*   **libparted:** The GNU partition editing library.
*   **LiveCD/USB:** A bootable operating system environment run from removable media without installation.
*   **MBR/MS-DOS:** Master Boot Record partition table type.
*   **SRS:** Software Requirements Specification.

#### 1.4 References
*   GNU Parted Manual
*   GTK+ Documentation
*   Gtkmm Tutorial

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its users, and operating constraints. Section 3 details the specific functional requirements. Section 4 outlines the non-functional requirements, including usability, performance, and design constraints.

---

### 2. Overall Description

#### 2.1 Product Perspective
This application is a self-contained, independent system that operates within a Linux Live environment. It acts as a mediator between the end-user and low-level disk manipulation libraries (`libparted`) and command-line file system tools (e.g., `mkfs`, `fsck`). Its position in the system architecture is illustrated below:

```
[User] <-> [Graphical Partition Editor (GTK+ GUI)] <-> [libparted API] <-> [Kernel Block Layer] <-> [Physical Disk]
                                                              |
                                                      [External FS Tools (e.g., mkfs.ext4, ntfsprogs)]
```

#### 2.2 Product Functions
The core functions of the system are:
1.  **Disk and Partition Visualization:** Display a graphical representation of storage devices and their partitions.
2.  **Partition Table Management:** Create new partition tables (e.g., msdos, gpt) on a storage device.
3.  **Partition Lifecycle Management:** Create, delete, resize, and move partitions.
4.  **Data Operations:** Copy partition contents to another location (cloning).
5.  **File System Management:** Format partitions to supported file systems and check/repair existing ones.
6.  **Attribute Management:** Set and clear partition flags (e.g., `boot`, `lba`, `hidden`).

#### 2.3 User Characteristics
| User Class | Description | Skill Level | Key Goals |
| :--- | :--- | :--- | :--- |
| **Casual User** | An individual needing to repartition a personal computer, resize an existing partition to install another OS, or clone a drive. | Basic understanding of disks, partitions, and file systems. Limited command-line proficiency. | Perform common tasks safely and intuitively without memorizing command syntax. |
| **Developer/Tester** | A contributor to the application itself or an integrator testing the tool on various hardware. | Advanced technical knowledge of disk structures, file systems, and software testing. | Verify functionality, test edge cases, and ensure compatibility with `libparted` and external tools. |
| **Documentation Writer** | A technical writer creating user guides or help content. | Good understanding of the application's features and target audience. | Accurately document workflows, warnings, and system capabilities. |

*All users operate with full administrative (root) privileges while the Live session is active.*

#### 2.4 Constraints
1.  **Technical Constraint:** Functionality is strictly limited by the capabilities of the underlying `libparted` library and the availability/version of optional file system tools (e.g., `ntfs-3g` for NTFS resizing).
2.  **Platform Constraint:** The application must be compiled for and run on x86 (and x86_64) architecture systems.
3.  **Environmental Constraint:** Requires a bootable Linux environment provided by the Live media. Cannot function as a native application within an arbitrary host OS without significant modification.
4.  **Dependency Constraint:** Core functionality depends on `libparted` and `Gtkmm`. Extended file system support depends on numerous third-party packages.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** The user's hardware (CD/DVD drive, USB port, keyboard, mouse) is functional and supported by the Linux kernel on the Live media.
*   **Assumption:** The user understands that partition operations carry a inherent risk of data loss.
*   **Dependency:** The GNU `libparted` library (v3.0 or later recommended).
*   **Dependency:** Gtkmm (C++ bindings for GTK+) for the graphical interface.
*   **Dependency:** A suite of optional file system tools (e.g., `e2fsprogs`, `dosfstools`, `ntfs-3g`, `xfsprogs`).

#### 2.6 Apportioning of Requirements
Future releases may consider requirements currently out of scope, such as:
*   Support for Logical Volume Management (LVM2).
*   Enhanced support for network and hardware RAID devices.
*   A scripting or batch operation interface.

---

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 User Interfaces
*   **UI-FR-1:** The application shall present a main window with the following elements:
    *   A menu bar containing: `File`, `View`, `Device`, `Partition`, `Tools`, `Help`.
    *   A toolbar with icons for frequent actions (Create, Delete, Resize/Move, Copy, Paste, Format, Check).
    *   A graphical pane displaying all detected storage devices as horizontal bars, with partitions shown as colored segments within them.
    *   A detailed list pane showing textual information (Device, Partition, Size, Used, Unused, Flags, File System) for the selected item.
    *   A status bar displaying messages, warnings, and pending operation information.
*   **UI-FR-2:** All destructive operations (Delete, Format, Create New Partition Table) shall require explicit user confirmation via a modal dialog box with a clear warning message.
*   **UI-FR-3:** The `Resize/Move` operation shall be initiated via a graphical dialog allowing manipulation of a partition's start and end points using a mouse or precise numerical input.

##### 3.1.2 Hardware Interfaces
*   **HW-FR-1:** The system shall interface with block storage devices accessible via the Linux kernel, including:
    *   Internal drives (IDE, SATA, SCSI, NVMe).
    *   External drives (USB, FireWire, eSATA).
    *   Hardware RAID volumes presented as single block devices.
*   **HW-FR-2:** The system requires standard input devices: a keyboard and a pointing device (mouse, touchpad).

##### 3.1.3 Software Interfaces
*   **SI-FR-1:** The system shall interact with the `libparted` library via its published C/C++ API for all partition table and geometry operations.
*   **SI-FR-2:** The system shall invoke external command-line utilities for file system-specific operations (e.g., `mkfs.ext4`, `ntfsresize`, `fsck.vfat`). The GUI shall parse the output of these tools to determine success/failure and present relevant messages to the user.

#### 3.2 Functional Requirements

##### 3.2.1 Device and Information Display
*   **FUN-1:** Upon startup, the system shall automatically scan for and display all recognized block storage devices.
*   **FUN-2:** The user shall be able to select any displayed device or partition to view its detailed properties (model, size, sector information, UUID, file system label, flags).

##### 3.2.2 Partition Table Operations
*   **FUN-3:** The user shall be able to create a new partition table (`msdos` or `gpt`) on a selected device, with a clear warning that this will destroy all existing partitions on that device.

##### 3.2.3 Partition Operations
*   **FUN-4:** **Create:** The user shall be able to create a new primary, extended, or logical partition within free space on a device, specifying its size, file system type, and alignment.
*   **FUN-5:** **Delete:** The user shall be able to delete a selected partition.
*   **FUN-6:** **Resize/Move:** The user shall be able to resize a selected partition (shrink or grow) and/or move its location on the disk, provided the underlying file system and `libparted` support the operation. Data integrity must be preserved.
*   **FUN-7:** **Copy/Paste:** The user shall be able to copy the contents of a selected partition to the clipboard and paste (clone) it to a free space area of equal or greater size on the same or a different device.

##### 3.2.4 File System Operations
*   **FUN-8:** **Format:** The user shall be able to format a selected partition (or free space intended for a new partition) to a supported file system (e.g., `ext2/3/4`, `NTFS`, `FAT16/32`, `XFS`, `Btrfs`). The list of available types shall be dynamically generated based on installed external tools.
*   **FUN-9:** **Check/Repair:** The user shall be able to perform a file system check on a selected partition and attempt to repair errors if any are found.

##### 3.2.5 Flag Management
*   **FUN-10:** The user shall be able to manage partition flags (e.g., `boot`, `hidden`, `raid`, `lvm`) for partitions on partition tables that support them.

##### 3.2.6 Operation Management
*   **FUN-11:** The system shall maintain a pending operations queue. No changes shall be written to disk until the user explicitly applies all pending operations.
*   **FUN-12:** The user shall be able to view, edit, and clear the pending operations queue before applying changes.

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance Requirements
*   **PER-1:** The graphical interface shall remain responsive during long-running operations (e.g., copying a large partition), providing progress feedback to the user.
*   **PER-2:** Device scanning at application start must complete within 10 seconds on a system with fewer than 10 attached storage devices.

##### 3.3.2 Usability Requirements
*   **USA-1:** The application shall follow standard GTK+/GNOME Human Interface Guidelines for layout and interaction.
*   **USA-2:** All user actions that risk data loss shall require a confirmation dialog with the option to cancel.
*   **USA-3:** Tooltips shall be provided for all toolbar buttons and non-obvious interface elements.
*   **USA-4:** The application shall provide meaningful, non-technical error messages when an operation fails, guiding the user towards a resolution where possible.

##### 3.3.3 Portability Requirement
*   **POR-1:** The application shall run on any x86-based computer capable of booting the provided Linux Live media, independent of the host machine's primary operating system.

##### 3.3.4 Reliability Requirements
*   **REL-1:** The application shall validate all user inputs (e.g., partition size, location) against physical device constraints and `libparted` rules before adding an operation to the queue.
*   **REL-2:** In the event of a critical error during the application of operations, the system shall attempt to halt the process and report the exact point of failure, minimizing data corruption.

##### 3.3.5 Design Constraint
*   **DES-1:** The system shall be designed with a clear separation between the GUI layer and the disk operation layer to facilitate maintenance and testing.

#### 3.4 Acceptance Criteria
Acceptance of the system will be based on the successful demonstration of the following scenarios on supported hardware:
1.  Booting the Live media and launching the application successfully.
2.  Creating a new GPT partition table on a USB drive.
3.  Creating a 10 GB `ext4` partition and a 5 GB `NTFS` partition on the drive.
4.  Safely resizing the `ext4` partition (shrinking by 2 GB).
5.  Formatting the `NTFS` partition to `FAT32`.
6.  Setting the `boot` flag on the `ext4` partition.
7.  Successfully applying all the above operations in a single batch, resulting in the correctly partitioned drive as specified.
8.  Displaying appropriate, clear warning dialogs for all destructive actions during the test.

---
**Document Approval**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Owner | | | |
| Lead Developer | | | |
| QA Lead | | | |