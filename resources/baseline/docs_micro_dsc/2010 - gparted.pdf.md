# Software Requirements Specification (SRS) for GParted
**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Approved for Development

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for GParted (GNOME Partition Editor). The intended audience includes software developers, testers, project managers, and system administrators who will implement, validate, and utilize the application.

### 1.2 Scope
GParted is a free, graphical partition editor. It acts as a high-level frontend to the GNU Parted library (`libparted`), providing users with an intuitive interface to perform disk and partition management tasks. The software is designed to run on Linux-based operating systems.

**In-Scope:**
*   Graphical user interface (GUI) for disk and partition visualization and manipulation.
*   Operations on disk partition tables (e.g., MS-DOS, GPT).
*   Operations on partitions (create, delete, resize, move, copy, format).
*   Integrity checking and repair of supported file systems.
*   Management of partition flags (e.g., boot, hidden).

**Out-of-Scope:**
*   Management of Logical Volume Manager (LVM2) volumes, physical volumes, or volume groups.
*   Management of RAID arrays.
*   Direct, low-level disk manipulation (handled exclusively by `libparted` and file system tools).
*   Native operation on non-Linux operating systems (though it may run via compatibility layers).

### 1.3 Definitions, Acronyms, and Abbreviations
*   **GUI:** Graphical User Interface.
*   **GPT:** GUID Partition Table.
*   **`libparted`:** The GNU Parted library for disk partitioning and manipulation.
*   **LVM2:** Logical Volume Manager version 2.
*   **MS-DOS Partition Table:** A standard partition table format (also known as MBR).
*   **SRS:** Software Requirements Specification.

### 1.4 References
*   GNU Parted Library Documentation.
*   GTK+ / GTKmm Toolkit Documentation.
*   Manual pages for file system tools (e.g., `mkfs.ext4`, `fsck.ntfs`, `resize2fs`).

### 1.5 Overview
The remainder of this document describes the overall product perspective, features, and specific requirements in detail. It is structured to provide a complete specification for the development and testing of the GParted application.

## 2. Overall Description

### 2.1 Product Perspective
GParted is a standalone, self-contained application. It is a member of the GNOME suite of applications but can be used independently of the GNOME desktop environment. Its primary relationship is with lower-level system components:
*   **`libparted`:** The core engine for all partition table and generic partition operations.
*   **File System Tools:** Third-party utilities (e.g., `e2fsprogs`, `dosfstools`, `ntfs-3g`) for file system-specific operations (create, check, resize).
*   **Linux Kernel:** Provides device discovery (`/dev/sd*`, `/dev/nvme*`) and basic I/O.
*   **Graphical Toolkit (GTKmm):** Provides the widget library for building the user interface.

### 2.2 Product Functions
The high-level functions of GParted are:
1.  **Device Discovery & Visualization:** Detect all block storage devices and graphically display their partition layout.
2.  **Partition Table Management:** Create, write, and manage partition tables (MS-DOS, GPT).
3.  **Partition Manipulation:** Perform operations on individual partitions.
4.  **File System Operations:** Perform operations dependent on the specific file system type.
5.  **Operation Management:** Queue multiple operations, preview changes, and execute them in a defined, safe sequence.
6.  **Safety Features:** Prevent operations on mounted partitions where possible and require explicit overrides.

### 2.3 User Classes and Characteristics
*   **System Administrators:** Primary users. Technically proficient, requires detailed information and precise control.
*   **Advanced Home Users:** Secondary users. Has basic understanding of disk partitioning, needs a safe and clear interface.
*   **Live System Users:** Users running GParted from a Live CD/USB to manage the primary OS installation. Requires robust handling of various hardware.

### 2.4 Operating Environment
*   **Software:** Linux-based operating system with a graphical (X11 or Wayland) display server. Required libraries: `libparted`, `gtkmm`.
*   **Hardware:** Standard PC architecture with IDE, SATA, SCSI, or NVMe storage devices.
*   **Privileges:** Most operations require root (`sudo`) privileges to execute.

### 2.5 Design and Implementation Constraints
1.  **Core Dependency Constraint:** All device detection, partition table manipulation, and generic partition geometry operations **must** be performed using the **GNU `libparted` library**. Direct disk I/O or use of alternative libraries for these core functions is prohibited.
2.  **LVM Exclusion Constraint:** The application **must not** provide native management for LVM2 logical volumes, physical volumes, or volume groups. It may display LVM devices as simple block devices if presented as such by the kernel.
3.  **File System Tool Dependency:** Support for any specific file system operation (format, check, resize) is **contingent upon** the presence and correct function of corresponding third-party command-line tools on the host system (e.g., support for `ext4` requires `e2fsprogs`).
4.  **Graphical Toolkit:** The user interface shall be implemented using the **GTKmm** (C++ bindings for GTK+) framework to maintain consistency with the GNOME ecosystem.

### 2.6 Assumptions and Dependencies
*   It is assumed the user has a basic understanding of disk partitioning concepts.
*   The correct functionality and safety of file system operations depend entirely on the underlying third-party tools (`mkfs`, `fsck`, etc.).
*   `Libparted` is assumed to be a stable and reliable foundation for partition manipulation.

## 3. System Features

### 3.1 Feature: Device and Partition Visualization
**Description:** The application shall present a clear, hierarchical view of all storage devices and their partitions.
**Requirements:**
*   **3.1.1:** The main window shall list all detected block devices (e.g., `/dev/sda`, `/dev/nvme0n1`) in a pane.
*   **3.1.2:** Selecting a device shall display a graphical representation of its partition layout, showing partition size, type, file system, and used/unused space.
*   **3.1.3:** A detailed textual summary (model, size, partition table type) for the selected device shall be displayed.

### 3.2 Feature: Partition Table Management
**Description:** The user shall be able to manage the partition table on a selected disk.
**Requirements:**
*   **3.2.1:** The application shall allow the user to create a new MS-DOS or GPT partition table on a device, overwriting any existing data.
*   **3.2.2:** The current partition table type shall be clearly displayed in the device information panel.

### 3.3 Feature: Core Partition Operations
**Description:** The user shall be able to perform fundamental manipulations on a selected partition.
**Requirements:**
*   **3.3.1:** **Create:** Create a new primary, extended, or logical partition within available free space, specifying size, alignment, and file system type.
*   **3.3.2:** **Delete:** Remove an existing partition, freeing its space.
*   **3.3.3:** **Resize/Move:** Change the start and/or end sector of a partition, effectively resizing or moving it within the disk.
*   **3.3.4:** **Copy:** Copy the structure and data of a partition to another location on a disk (space permitting).
*   **3.3.5:** The application shall prevent operations on currently mounted partitions by default, providing a warning and an option to unmount or force the operation.

### 3.4 Feature: File System Operations
**Description:** The user shall be able to perform operations specific to the file system contained within a partition.
**Requirements:**
*   **3.4.1:** **Format:** Apply a supported file system (e.g., `ext4`, `ntfs`, `fat32`, `xfs`) to a partition, overwriting existing data.
*   **3.4.2:** **Check:** Perform a file system integrity check using the appropriate `fsck` tool.
*   **3.4.3:** **Label:** Set or change the volume label of a supported file system.
*   **3.4.4:** The availability of these operations shall be dynamically determined based on the detection of the required command-line tools on the system.

### 3.5 Feature: Partition Flag Management
**Description:** The user shall be able to set or clear partition attributes/flags.
**Requirements:**
*   **3.5.1:** For MS-DOS partition tables, the application shall allow toggling flags such as `boot`, `hidden`, `lba`.
*   **3.5.2:** For GPT partition tables, the application shall allow managing partition type GUIDs and attributes.

### 3.6 Feature: Operation Management and Execution
**Description:** The user shall be able to plan and execute a series of disk operations safely.
**Requirements:**
*   **3.6.1:** All user-requested operations shall be queued and displayed in a pending operations list.
*   **3.6.2:** The application shall provide a visual preview of the disk layout after applying all pending operations.
*   **3.6.3:** The user must explicitly initiate the execution of the pending queue (via an "Apply" button).
*   **3.6.4:** During execution, the application shall display a detailed progress log showing the output and status of each step.
*   **3.6.5:** Operations shall be executed in a logical and safe order (e.g., move operations before resize operations that depend on new space).

## 4. External Interface Requirements

### 4.1 User Interfaces
*   **Main Window:** Contains a device list, graphical partition map, operation pane, and menu/ toolbar.
*   **Dialogs:** Modal dialogs for specific operations (Create, Resize/Move, Format, etc.) with relevant input fields and warnings.
*   **Style:** Adherence to the current GNOME Human Interface Guidelines (HIG).

### 4.2 Hardware Interfaces
*   Interacts with block storage devices via the Linux kernel device interface (`/dev`).
*   No direct hardware control; all hardware interaction is mediated by `libparted` and the kernel.

### 4.3 Software Interfaces
*   **`libparted` (v3.0+):** Primary interface for all partition-level commands.
*   **File System Tools:** Called via command-line invocation (e.g., `system("mkfs.ext4 /dev/sda1")`).
*   **`udev`:** May be used for device change notification.
*   **`glib`/**`gtkmm`:** For core application runtime and GUI.

### 4.4 Communications Interfaces
Not applicable. GParted is a local desktop application with no network functionality.

## 5. Non-Functional Requirements

### 5.1 Performance Requirements
*   Device scanning and layout rendering for a standard disk (< 2TB) shall complete within 5 seconds.
*   The GUI shall remain responsive while long-running operations (e.g., copying a large partition) are in progress.

### 5.2 Safety Requirements
*   The application **shall not** allow the execution of operations that would destroy the root file system of the currently running OS without an explicit and severe warning.
*   Operations on mounted file systems shall be restricted or come with explicit data loss warnings.

### 5.3 Security Requirements
*   The application must be run with elevated privileges. It does not itself handle authentication but relies on the system's `sudo` or policykit mechanisms.

### 5.4 Software Quality Attributes
*   **Reliability:** Must correctly reflect the state of the disk and reliably execute the exact sequence of queued operations.
*   **Usability:** The interface must be intuitive enough for an advanced user to perform complex tasks without consulting the manual for basic operations.
*   **Maintainability:** The codebase shall be modular, clearly separating GUI logic, operation management, and `libparted` interaction.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Product Manager | | | |
| Lead Developer | | | |
| QA Lead | | | |