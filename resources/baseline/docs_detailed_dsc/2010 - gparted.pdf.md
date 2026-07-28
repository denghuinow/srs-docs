# Software Requirements Specification (SRS)
## For GParted (Gnome Partition Editor) Version 0.6.0-1

**Document Version:** 1.0
**Date:** [Current Date]
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for GParted (Gnome Partition Editor) version 0.6.0-1. It is intended for use by the development team, testers, documentation writers, and project stakeholders to ensure a common understanding of the system's capabilities, constraints, and behavior.

#### 1.2 Document Conventions
*   **Bold text** is used for emphasis.
*   `Monospaced text` denotes system components, code, or file paths.
*   Requirements are uniquely identified as `FR-XXX` (Functional) or `NFR-XXX` (Non-Functional).
*   This document uses Markdown formatting.

#### 1.3 Project Scope
GParted 0.6.0-1 is a graphical partition editor for creating, reorganizing, and deleting disk partitions. It serves as a frontend to the GNU Parted library (`libparted`) and is distributed as a LiveCD application that runs entirely from system RAM, requiring no installation on the target system.

**In-Scope:**
*   Core partition management operations (create, delete, resize/move, copy, format).
*   Management of partition tables (create new table).
*   File system operations (check, label) for supported file systems.
*   Management of partition flags (e.g., boot, hidden).
*   A graphical user interface (GUI) for device selection, operation configuration, and pending operation management.
*   Integration with `libparted` and file system-specific tools (e.g., `e2fsprogs`, `ntfsprogs`).

**Out-of-Scope (Non-Goals):**
*   Support for Logical Volume Management (LVM2).
*   Implementation of every possible operation for all existing file systems.
*   Network-based partitioning or remote administration.
*   Data recovery from damaged partitions.

#### 1.4 References
*   GNU Parted Library (`libparted`) Documentation, Version >=1.7.1.
*   GNU General Public License (GPL) version 2 or later.

### 2. Overall Description

#### 2.1 Product Perspective
GParted is a self-contained, standalone application within a Linux-based Live environment. It interacts with the following external systems:
1.  **GNU Parted (`libparted`):** The core engine for low-level partition manipulation.
2.  **File System Tools:** External packages (e.g., `mkfs.ext4`, `ntfsresize`) for file system-specific tasks.
3.  **Linux Kernel:** For hardware detection, device access, and mount operations.
4.  **System Hardware:** Storage devices (HDD, SSD, USB drives) presented via the kernel.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Goals |
| :--- | :--- | :--- |
| **Casual User** | Basic computer and partition knowledge. Needs to perform common tasks like resizing, creating, or formatting partitions. | Safely modify disk layout without data loss. Clear, intuitive interface. |
| **Developer** | Technical expertise in C++, GTK+, and `libparted`. Familiar with open-source contribution workflows. | Extend functionality, fix bugs, understand code structure and integration points. |
| **Tester** | Methodical, detail-oriented. Uses beta releases in varied hardware/software configurations. | Identify and report bugs, verify fixes, ensure stability. |
| **Documentation Writer** | Understands user needs and technical details. | Produce accurate, clear user guides and help documentation based on specified features. |

#### 2.3 Operating Environment
*   **Physical Environment:** Runs as a Live system from CD/DVD or USB media.
*   **Software Environment:** A custom Linux distribution with a GNOME-based desktop, `libparted` (>=1.7.1), and necessary file system tools.
*   **Hardware Environment:** Standard x86 (32-bit or 64-bit) hardware with CD/DVD or USB boot capability. Supports common storage controllers (IDE, SATA, USB).

#### 2.4 Design and Implementation Constraints
1.  **License:** Must be distributed under the GNU GPL v2 or later.
2.  **Dependency:** Core functionality is dependent on `libparted` API.
3.  **Architecture:** Must operate with root/administrator privileges to perform disk operations.
4.  **Live System:** Must be memory-efficient and not rely on persistent storage on the host machine.

#### 2.5 Assumptions and Dependencies
*   The user has a basic understanding of disk partitions and the risks of data loss.
*   The underlying `libparted` library and file system tools function correctly.
*   The host system's hardware is supported by the Linux kernel within the Live environment.

### 3. System Features and Requirements

#### 3.1 Feature: Device Discovery and Visualization
**Description:** The system shall detect all connected storage devices and visually present their partition layout.

**Requirements:**
*   `FR-010`: The application shall, upon launch, scan and list all detected block storage devices (e.g., `/dev/sda`, `/dev/sdb`) in a user-selectable dropdown menu.
*   `FR-011`: For the selected device, the application shall display a graphical representation of its partition table, showing partitions and unallocated space with size labels.
*   `FR-012`: The application shall display a detailed textual list of all partitions on the selected device, including: device path, partition number, size, file system type, used/unused space, and flags.
*   `FR-013`: The user shall be able to manually refresh the list of devices via a "GParted -> Refresh Devices" menu action.

#### 3.2 Feature: Partition Table Management
**Description:** The user can create a new partition table on a device, which erases all existing data.

**Requirements:**
*   `FR-020`: The user shall be able to select the "Device -> Create Partition Table..." action.
*   `FR-021`: Upon selection, a dialog shall appear with a prominent warning about data loss and a choice of partition table types (e.g., msdos, gpt).
*   `FR-022`: Creating a partition table shall be added as a pending operation, requiring the user to click "Apply" for execution.

#### 3.3 Feature: Core Partition Operations
**Description:** The user can perform basic actions on partitions and unallocated space.

**Requirements:**
*   `FR-030`: On a selected unallocated space, the user shall be able to select "Partition -> New" to open a dialog for creating a new partition, specifying size, alignment, and file system type.
*   `FR-031`: On a selected partition, the user shall be able to select "Partition -> Delete" to queue its deletion.
*   `FR-032`: On a selected partition, the user shall be able to select "Partition -> Resize/Move" to open a dialog allowing graphical or numerical adjustment of partition boundaries, provided the operation is supported by the file system.
*   `FR-033`: The UI shall gray out (disable) menu actions that are not applicable to the current selection (e.g., "Resize" for an unsupported file system).

#### 3.4 Feature: Copy and Paste Partition
**Description:** The user can copy a partition's structure and data to another location.

**Requirements:**
*   `FR-040`: The user shall be able to select a partition and choose "Edit -> Copy" to copy its details to an internal clipboard.
*   `FR-041`: The user shall be able to select unallocated space on any device and choose "Edit -> Paste" to open a dialog.
*   `FR-042`: The paste dialog shall show the size of the source partition and allow the user to resize or reposition the partition within the target unallocated space.
*   `FR-043`: If the target space overlaps an existing partition, a severe data loss warning must be displayed before the operation can be queued.

#### 3.5 Feature: File System Operations
**Description:** The user can manage the file system on a partition.

**Requirements:**
*   `FR-050`: On a selected partition, the user shall be able to select "Partition -> Format to" and choose a supported file system type (e.g., ext4, NTFS, FAT32) to queue a format operation.
*   `FR-051`: On a selected partition with a supported file system, the user shall be able to select "Partition -> Check" to queue a file system check and repair operation.
*   `FR-052`: The application shall rely on the underlying file system tool's output to report the success, failure, or findings (errors repaired) of a check operation.

#### 3.6 Feature: Manage Flags
**Description:** The user can set or clear partition flags.

**Requirements:**
*   `FR-060`: On a selected partition, the user shall be able to select "Partition -> Manage Flags".
*   `FR-061`: A dialog shall appear listing available flags (e.g., `boot`, `hidden`, `lba`) for the partition's type, with checkboxes indicating their current state.
*   `FR-062`: Changing a flag state shall be added as a pending operation.

#### 3.7 Feature: Pending Operations Queue
**Description:** The user can review, modify, and execute a batch of operations.

**Requirements:**
*   `FR-070`: All user-configured actions shall be added to a pending operations list without immediately writing to disk.
*   `FR-071`: The application shall display a list of all pending operations at the bottom of the main window.
*   `FR-072`: The user shall be able to select "Edit -> Undo Last Operation" to remove the most recently added pending operation.
*   `FR-073`: The user shall be able to select "Edit -> Clear All Operations" to empty the pending operations list.
*   `FR-074`: The user must click the "Apply" button to begin executing all pending operations.
*   `FR-075`: During execution, a progress dialog shall show the current operation and its status (success, failure, details).

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Main Window:** Contains a menu bar, device selection dropdown, graphical partition map, partition list, and pending operations panel.
*   **Operation Dialogs:** Modal dialogs for New, Resize/Move, Copy, Paste, Format, and Manage Flags actions. All destructive actions must contain clear warnings.
*   **Progress/Result Dialog:** Non-modal dialog showing the progress and final outcome of applied operations.

#### 4.2 Hardware Interfaces
*   The application interfaces with storage hardware via the Linux kernel block device interface (`/dev/sd*`, `/dev/hd*`).

#### 4.3 Software Interfaces
| Interface | Direction | Purpose | Data Format / Protocol |
| :--- | :--- | :--- | :--- |
| **GNU Parted (`libparted`)** | Outbound | Core partition geometry manipulation. | C API calls. Input: Device path, operation type, parameters. Output: Success/Failure status, error messages. |
| **File System Tools** | Outbound | File system creation, checking, resizing. | Command-line execution via system calls. Input: Tool name (e.g., `mkfs.ext4`), partition path, options. Output: Standard output/error streams. |
| **Linux Kernel** | Inbound/Outbound | Device discovery, mounting. | System calls (`ioctl`, mount syscalls). |

#### 4.4 Communications Interfaces
Not applicable for this version. The Live environment operates offline.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-001`: The main application window shall load within 5 seconds on typical hardware (Pentium 4/equivalent, 512MB RAM).
*   `NFR-002`: Device refresh and graphical layout rendering shall occur with negligible delay (<2 seconds) for devices with fewer than 20 partitions.

#### 5.2 Safety & Reliability Requirements
*   `NFR-010`: **Data Integrity:** For non-destructive operations like resizing supported file systems, the application shall ensure data is preserved upon successful completion.
*   `NFR-011`: **Fail-Safe Warnings:** Any operation that will irrevocably destroy data (Create Partition Table, Delete, Overwriting Paste) shall require explicit user confirmation via a dialog with a prominent warning.
*   `NFR-012`: **Transaction Safety:** The application shall rely on `libparted`'s transactional capabilities where possible to minimize the risk of leaving the disk in a corrupted state.

#### 5.3 Security Requirements
*   `NFR-020`: The Live environment runs with root privileges by necessity. The UI must not obscure the seriousness of this access level.
*   `NFR-021`: No authentication or authorization is required within the application itself, as it is a single-user, offline tool.

#### 5.4 Compliance
*   `NFR-030`: The software and its distribution shall comply with the GNU General Public License version 2 or later.

#### 5.5 Usability & Observability
*   `NFR-040`: The graphical partition map shall be intuitive, using distinct colors for different file systems and clear labels for sizes.
*   `NFR-041`: The status of all operations (pending, in progress, completed, failed) shall be clearly visible to the user at all times.
*   `NFR-042`: Detailed error messages from underlying tools (`libparted`, `fsck`) shall be presented to the user when an operation fails.

### 6. Other Requirements

#### 6.1 Acceptance Criteria
The following scenarios define successful implementation of key capabilities:

1.  **Resize/Move Partition:**
    *   **Given** a formatted ext4 partition with free space following it.
    *   **When** the user selects it, chooses "Resize/Move", shrinks the partition by 10GB, and applies the operation.
    *   **Then** the operation completes successfully, the partition is reduced in size, and 10GB of unallocated space appears after it. All original data remains accessible.

2.  **Copy and Paste Partition:**
    *   **Given** a 20GB FAT32 partition on `/dev/sda1` is copied to the clipboard.
    *   **When** the user selects a 25GB unallocated space on `/dev/sdb`, chooses "Paste", accepts the default size, and applies.
    *   **Then** a new 20GB FAT32 partition is created on `/dev/sdb`, and its contents are a copy of the source partition.

3.  **Check File System:**
    *   **Given** a selected ext3 partition.
    *   **When** the user selects "Check" and applies the operation.
    *   **Then** the file system check tool (`e2fsck`) runs, and its output (e.g., "0.5% non-contiguous", "clean") is displayed in the results dialog.

#### 6.2 Appendices

##### 6.2.1 Glossary
*   **LiveCD/Live Media:** A bootable operating system that runs from removable media without installation.
*   **Partition Table:** A data structure on a disk that defines the layout of partitions (e.g., MBR/MS-DOS, GPT).
*   **Unallocated Space:** Disk space not assigned to any partition.
*   `libparted`: The GNU partition editing library.

##### 6.2.2 Domain Model Summary
Entities and their key relationships:
*   A **Device** has one **Partition Table**.
*   A **Partition Table** contains many **Partitions**.
*   A **Partition** has one **File System** (may be `none` or `unknown`).
*   A **Partition** can have many **Flags**.
*   An **Operation** targets a specific **Partition** (or device for table creation).
*   The **Pending Operations Queue** is an ordered list of **Operation** entities.

##### 6.2.3 Risk Management
| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| Data Loss from User Error | Medium | Critical | Prominent warnings, undo for pending ops, clear device labeling. |
| Unsupported Operation Failure | High | Medium | UI disables unavailable actions; surface clear error messages from underlying tools. |
| Hardware Incompatibility | Low | High | Support common controllers; provide "failsafe" boot mode with generic drivers. |
| Corrupted Live Media | Low | High | Provide ISO checksums and verified burning instructions. |

---
*This document is considered the authoritative source of requirements for GParted version 0.6.0-1.*