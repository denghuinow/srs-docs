Here is a comprehensive Software Requirements Specification (SRS) document for the GParted project, structured according to professional standards.

# Software Requirements Specification (SRS) for GParted
**Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft

## 1. Introduction

### 1.1 Purpose
This document provides a detailed description of the Software Requirements Specification for GParted (GNOME Partition Editor), Version 1.0. It is intended for stakeholders, including developers, testers, project managers, and end-users, to serve as a definitive guide for the system's functionality, constraints, and operational environment. This SRS will be used as the basis for development, testing, and project validation.

### 1.2 Project Scope
GParted is a free and open-source graphical partition editor. It enables users to perform data management operations on disk partitions without the need for installation by running from a LiveCD or other bootable media. Its core value is providing a safe, intuitive, and powerful interface for disk management tasks that are typically performed at the system level, thereby making advanced storage configuration accessible to a broader range of users.

### 1.3 Definitions, Acronyms, and Abbreviations

| Term | Definition |
| :--- | :--- |
| **SRS** | Software Requirements Specification |
| **MVP** | Minimum Viable Product |
| **LiveCD** | A bootable CD/DVD/USB that contains an operating system runtime environment. |
| **Partition** | A logically independent section of a data storage device. |
| **File System** | A method and data structure for storing, retrieving, and managing files on a partition (e.g., ext4, NTFS, FAT32). |
| **LVM2** | Logical Volume Manager 2, a device-mapper framework that provides logical volume management for the Linux kernel. |
| **UI** | User Interface |

### 1.4 References
*   GNU General Public License (GPL)
*   GNOME Human Interface Guidelines (HIG)

### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product. Section 3 outlines the specific requirements, including functional, external interface, and non-functional requirements.

## 2. Overall Description

### 2.1 Product Perspective
GParted is a self-contained application designed to operate independently of an installed operating system. It is part of the ecosystem of system administration tools and relies on a stack of underlying Linux system utilities and libraries (e.g., `parted`, `e2fsprogs`, `ntfs-3g`) to perform low-level disk operations.

### 2.2 Product Functions
The high-level functions of GParted are:
*   **Visualization:** Provide a graphical representation of storage devices and their partition layout.
*   **Partition Management:** Create, delete, resize, and move disk partitions.
*   **Data Safety:** Perform resize and move operations in a manner that aims to preserve existing data.
*   **File System Operations:** Format partitions to various file systems and check/repair their integrity.
*   **Data Manipulation:** Copy the entire contents of a partition and paste it to a different location on a disk.

### 2.3 User Characteristics
The intended user base is diverse:
*   **System Administrators:** Experts who require powerful tools for disk management.
*   **Technical Enthusiasts:** Users with some technical knowledge who are installing or dual-booting operating systems.
*   **End-Users in Data Recovery Scenarios:** Users following guided instructions to resize partitions or recover data.

### 2.4 Constraints
1.  **Environmental Constraint:** The application requires a working Linux environment, typically accessed via a bootable LiveCD or USB media.
2.  **Functional Constraint:** The MVP does not support Logical Volume Management (LVM2). Operations on LVM physical volumes, volume groups, or logical volumes are outside the project's initial scope.
3.  **Dependency Constraint:** The application's functionality is dependent on the presence and correct operation of third-party command-line tools and libraries for specific file systems (e.g., `ntfsresize` for NTFS, `dosfsck` for FAT).

### 2.5 Assumptions and Dependencies
*   It is assumed that the user has a basic understanding of disk partitions and the risks associated with modifying them.
*   The application depends on the Linux kernel and a specific set of file system tools being available in the host environment.
*   The correct operation of the application is dependent on the underlying hardware and kernel drivers for disk access.

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 User Interfaces
The UI shall be a graphical desktop application conforming to the GNOME/GTK standards.
*   **Main Window:** Shall display a graphical representation of disks and partitions in a pane.
*   **Toolbar:** Shall provide quick access to frequently used operations (Create, Delete, Resize/Move, Copy, Paste, Undo, Apply).
*   **Menu Bar:** Shall provide comprehensive access to all operations and settings.
*   **Operation Pending List:** Shall display a list of operations queued for execution, allowing the user to review changes before applying them.

#### 3.1.2 Hardware Interfaces
The application shall interface directly with block devices (e.g., `/dev/sda`, `/dev/nvme0n1`) through the Linux kernel.

#### 3.1.3 Software Interfaces
The application shall call the following external command-line tools (non-exhaustive list):
*   `parted`, `fdisk`: For partition table manipulation (create, delete).
*   `e2fsprogs` (e.g., `resize2fs`, `e2fsck`): For ext2/3/4 file system operations.
*   `ntfs-3g` / `ntfsprogs` (e.g., `ntfsresize`, `ntfsfix`): For NTFS operations.
*   `dosfstools` (e.g., `mkfs.fat`, `fsck.fat`): For FAT16/FAT32 operations.
*   `hfsutils`, `xfsprogs`, `btrfs-progs`, etc.: For other supported file systems.

### 3.2 Functional Requirements

#### 3.2.1 FR-1: Partition Visualization
| **ID** | **FR-1** |
| :--- | :--- |
| **Description** | The system shall provide a visual representation of all detected storage devices and their partitions. |
| **Priority** | High |
| **Inputs** | System probe for block devices. |
| **Processing** | 1. Query the system for all available block devices.<br>2. Read the partition table for each device.<br>3. Determine file system type and usage for each partition.<br>4. Render a graphical layout in the main window. |
| **Outputs** | A graphical diagram showing devices as rectangles, with partitions as colored segments within, labeled with device name, size, file system, and used/unused space. |

#### 3.2.2 FR-2: Create Partition
| **ID** | **FR-2** |
| :--- | :--- |
| **Description** | The user shall be able to create a new partition in unallocated disk space. |
| **Priority** | High |
| **Inputs** | User selects unallocated space, chooses "Create", and specifies parameters (size, file system type, partition label). |
| **Processing** | 1. Validate that the selected space is sufficient and contiguous.<br>2. Add a "create partition" operation to the pending queue.<br>3. Upon application, execute the command to modify the partition table (e.g., `parted mkpart`). |
| **Outputs** | A new partition is created in the specified unallocated space. |

#### 3.2.3 FR-3: Delete Partition
| **ID** | **FR-3** |
| :--- | :--- |
| **Description** | The user shall be able to delete an existing partition. |
| **Priority** | High |
| **Inputs** | User selects an existing partition and chooses "Delete". |
| **Processing** | 1. Prompt the user for confirmation due to risk of data loss.<br>2. Add a "delete partition" operation to the pending queue.<br>3. Upon application, execute the command to remove the partition from the partition table. |
| **Outputs** | The selected partition is deleted, and its space is marked as unallocated. |

#### 3.2.4 FR-4: Resize/Move Partition
| **ID** | **FR-4** |
| :--- | :--- |
| **Description** | The user shall be able to resize or move an existing partition while preserving its data. |
| **Priority** | High |
| **Inputs** | User selects a partition, chooses "Resize/Move", and adjusts the start or end boundary graphically or numerically. |
| **Processing** | 1. Check the file system for errors before resizing.<br>2. Validate the new size/location is feasible.<br>3. Add a complex operation to the queue: first resize the file system (if shrinking), then move/resize the partition, then resize the file system (if expanding).<br>4. Execute the sequence of commands using tools like `parted` and file-system-specific resizers (e.g., `resize2fs`, `ntfsresize`). |
| **Outputs** | The partition is resized and/or moved to the new location with data integrity maintained. |

#### 3.2.5 FR-5: Format Partition
| **ID** | **FR-5** |
| :--- | :--- |
| **Description** | The user shall be able to format a partition to a specified file system. |
| **Priority** | High |
| **Inputs** | User selects a partition, chooses "Format to", and selects a file system type (e.g., ext4, NTFS, FAT32). |
| **Processing** | 1. Warn the user that all data on the partition will be erased.<br>2. Add a "format" operation to the pending queue.<br>3. Upon application, execute the appropriate `mkfs` command for the selected file system. |
| **Outputs** | The partition is formatted with the new, empty file system. |

#### 3.2.6 FR-6: Copy and Paste Partition
| **ID** | **FR-6** |
| :--- | :--- |
| **Description** | The user shall be able to copy the contents of one partition and paste it to another location on a disk. |
| **Priority** | Medium |
| **Inputs** | User selects a source partition and chooses "Copy". Then, user selects unallocated space and chooses "Paste". |
| **Processing** | 1. Verify the destination space is at least as large as the source partition.<br>2. Add a sequence of operations to the queue: create a new partition in the destination space, format it, and copy all data block-by-block from the source to the destination. |
| **Outputs** | A new partition is created which is a sector-by-sector or file-by-file copy of the source partition. |

#### 3.2.7 FR-7: Check and Repair File System
| **ID** | **FR-7** |
| :--- | :--- |
| **Description** | The user shall be able to check a partition's file system for errors and attempt to repair them. |
| **Priority** | Medium |
| **Inputs** | User selects a partition and chooses "Check". |
| **Processing** | 1. Ensure the partition is not mounted.<br>2. Execute the appropriate file system check tool (e.g., `e2fsck`, `ntfsfix`, `fsck`).<br>3. Parse and display the tool's output to the user. |
| **Outputs** | The file system is checked, errors are reported, and repairs are attempted if possible. |

#### 3.2.8 FR-8: Apply All Operations
| **ID** | **FR-8** |
| :--- | :--- |
| **Description** | The system shall queue all user-requested operations and execute them only upon an explicit "Apply" command. |
| **Priority** | High |
| **Inputs** | User clicks the "Apply" button in the toolbar. |
| **Processing** | 1. Present a final summary dialog listing every operation that will be performed.<br>2. Require user confirmation to proceed.<br>3. Execute each operation in the queue sequentially and in the correct order.<br>4. Display real-time progress and the output log of each command. |
| **Outputs** | All pending disk operations are physically written to the disk. |

### 3.3 Non-Functional Requirements

#### 3.3.1 Performance Requirements
*   The UI shall remain responsive during long-running operations (e.g., move, copy), providing progress feedback to the user.
*   Scanning and reading partition information for all devices should complete within 10 seconds on a system with typical hardware (e.g., 1-4 disks).

#### 3.3.2 Safety & Reliability Requirements
*   **Data Loss Prevention:** The application shall require explicit confirmation before executing any destructive operation (delete, format) or a sequence of operations (via the "Apply" step).
*   **Operation Validation:** The application shall perform feasibility checks before adding an operation to the queue (e.g., ensuring sufficient space for a new partition).
*   **Error Handling:** The application shall gracefully handle errors from underlying command-line tools, abort the operation sequence if a critical error occurs, and present a meaningful error message to the user.

#### 3.3.3 Security Requirements
*   The application requires root privileges to perform disk operations. This is inherent to its design as a system administration tool.

#### 3.3.4 Usability Requirements
*   The graphical representation of partitions must be intuitive and accurately reflect the disk's geometry.
*   Common tasks (Create, Delete, Resize/Move) should be accessible with a minimal number of clicks.
*   The application shall provide tooltips and contextual help for its functions.

### 3.4 Major Risks and Undecided Issues
1.  **Potential for Data Loss:** The primary risk associated with GParted is irreversible data loss resulting from user error, software bugs, or hardware failure during partition manipulation. **Mitigation:** Clear warnings, an operation queue that requires final confirmation, and encouraging users to back up data before proceeding.
2.  **Hardware/Software Compatibility:** Support for certain file systems or new storage technologies is dependent on the underlying tools and the Linux kernel version used in the LiveCD environment. This is an ongoing concern.