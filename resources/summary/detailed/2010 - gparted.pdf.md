# Detailed Summary: GParted Version 0.6.0-1

## Background and Scope
This document specifies the requirements for GParted (Gnome Partition Editor) version 0.6.0-1, a graphical partition editor for creating, reorganizing, and deleting disk partitions. It is a frontend to the GNU Parted library (`libparted`) and runs as a LiveCD application, operating from system RAM without requiring installation. The scope includes core partition management functions, user interface flows, and integration with underlying system tools. Non-goals include supporting Logical Volume Management (LVM2) and implementing every possible operation for all file systems.

## Stakeholders Matrix and Use Cases
*   **Casual Users**: Individuals needing to partition drives, resize/move partitions, or clone data; require basic computer and partition knowledge.
*   **Developers**: Contributors interested in improving the application, fixing bugs, and adding features to the GParted community.
*   **Testers**: Individuals who test beta versions for bugs and errors, submitting findings to the bug tracking system.
*   **Documentation Writers**: Writers who use this specification to document the program's functions and features for user guides.

**Main Scenarios:**
1.  User boots from GParted Live media, selects language/keymap, and loads the graphical desktop.
2.  User views connected storage devices and their partition information.
3.  User creates a new partition table on a device (with data loss warning).
4.  User creates, resizes/moves, or deletes a partition on unallocated space.
5.  User copies a partition and pastes it onto another drive or unallocated space.
6.  User formats a partition to a specific file system (e.g., ext4, NTFS).
7.  User checks and repairs errors on a partition's file system.
8.  User manages partition flags (e.g., boot, hidden).

**Exception Scenarios:**
*   Pasting a partition over an existing one triggers a data loss warning.
*   Attempting an unsupported operation for a specific file system results in the action being unavailable or failing.

## Business Process
**Main Process: Partition Management**
1.  **Trigger**: User boots computer from GParted Live media.
2.  **Input**: User selections for boot mode, keymap, language, and video mode.
3.  **Process**: System loads GParted desktop environment.
4.  **Process**: User launches main GParted window from the desktop.
5.  **Process**: User selects a target storage device from a dropdown list.
6.  **Process**: User selects a partition or unallocated space and chooses an action (e.g., Create, Resize, Format).
7.  **Process**: User configures action parameters (e.g., size, file system) in a dialog.
8.  **Output**: Operation is queued; user must click "Apply" to execute all pending operations, which modifies the disk.

**Key Branch A: Undo/Apply Workflow**
1.  After configuring operations, they are listed as pending.
2.  User can "Undo Last Operation" or "Clear All Operations".
3.  User clicks "Apply All Operations" to execute.
4.  System performs the operations and updates the disk layout.

**Key Branch B: Device Refresh**
1.  **Trigger**: User plugs in a new storage device (e.g., USB drive) after GParted has booted.
2.  User selects "GParted -> Refresh Devices".
3.  System rescans for connected hardware.
4.  The new device appears in the device selection dropdown.

## Domain Model
*   **Device** (required: model, size, heads, sectors, cylinders; unique: path e.g., /dev/sda)
*   **Partition Table** (required: type [e.g., msdos, gpt]; reference: Device)
*   **Partition** (required: size, position; reference: Partition Table)
*   **File System** (required: type [e.g., ext4, NTFS]; reference: Partition)
*   **Operation** (required: type [Create, Delete, Resize, etc.], status [pending, applied]; reference: Partition)
*   **Flag** (required: name [e.g., boot, hidden]; reference: Partition - many-to-many)
*   **Pending Operations Queue** (required: list of Operation entities)

## Interfaces and Integrations
| System | Direction | Interaction Points / Theme | Input Key Points | Output Key Points | SLA Key Points |
| :--- | :--- | :--- | :--- | :--- | :--- |
| GNU Parted (`libparted`) | Outbound | Core partition manipulation | Device/partition details, operation type | Success/failure status, operation results | Must be version >=1.7.1 |
| File System Tools (e.g., e2fsprogs, ntfsprogs) | Outbound | File system-specific operations | Partition details, action (create, check, label) | Action completion status | Tools must be available for supported actions |
| System Hardware | Inbound | Device detection | Connected storage devices (HDD, USB) | Device list and properties | Requires functional CD/DVD or USB port for boot |
| Linux Kernel | Inbound/Outbound | Mounting/Unmounting | Partition path, mount point command | Mount status | Required for terminal-based mount operations |

## Acceptance Criteria
**Capability: Resize/Move Partition**
*   **Given** a formatted partition with free space adjacent to it,
*   **When** the user selects the partition and uses the Resize/Move action to shrink it,
*   **Then** the operation is added to the pending queue, and upon apply, the partition is resized without data loss, creating unallocated space.

**Capability: Copy and Paste Partition**
*   **Given** a source partition is copied to the clipboard,
*   **When** the user selects unallocated space on a target device and chooses Paste,
*   **Then** a dialog allows resizing/positioning of the pasted partition, and upon apply, an exact copy is created on the target.

**Capability: Check File System**
*   **Given** a selected partition with a supported file system (e.g., ext3),
*   **When** the user selects the "Check" action and applies it,
*   **Then** the file system is analyzed, errors are reported, and repairs are attempted if possible.

## Non-functional Metrics
*   **Performance**: Application loads and runs efficiently on standard x86 hardware without requiring high-end resources.
*   **Reliability**: Operations must preserve data integrity where specified (e.g., resize/move); clear warnings must be given for destructive actions.
*   **Security**: The Live environment runs with root/administrator privileges by design; users must exercise caution.
*   **Compliance**: Distributed under the GNU General Public License (GPL) version 2 or later.
*   **Observability**: Users can view pending operations and detailed device information; actions are not final until "Apply" is clicked.

## Milestones and Release Strategy
1.  Finalize requirements specification for version 0.6.0-1.
2.  Development and integration of core features against `libparted`.
3.  Alpha testing with internal/community testers.
4.  Beta release for public testing and bug reporting.
5.  Final release of GParted Live 0.6.0-1 ISO image.
6.  Publication of updated user documentation.

## Risk List and Mitigation Strategies
1.  **Data Loss**: Mitigation: Prominent warnings for destructive operations (delete, create table, overwrite paste); "Undo" function for pending ops.
2.  **Unsupported File System/Action**: Mitigation: UI grays out unavailable actions; reliance on underlying tool failure messages.
3.  **Hardware/Driver Incompatibility**: Mitigation: Support for common IDE, SATA, USB controllers; provide "failsafe" boot mode.
4.  **Failed Operation Mid-Process**: Mitigation: Use of transactional approach where possible via `libparted`; clear error reporting.
5.  **User Error (e.g., wrong device)**: Mitigation: Clear device labeling in UI; refresh devices function.
6.  **Corrupted Download/Burn of Live Media**: Mitigation: Provide checksums for ISO files and clear burning instructions.
7.  **Dependency on Outdated Libraries**: Mitigation: Specify minimum versions (e.g., Parted >=1.7.1) and package them with the Live image.
8.  **Lack of LVM2 Support**: Mitigation: Clearly document as a non-goal for this release; consider for future roadmap.

## Undecided Issues and Responsible Parties
1.  Implementation timeline for Logical Volume Management (LVM2) support. (Responsible: GParted Development Team)
2.  Prioritization of adding support for additional, less common file systems. (Responsible: GParted Development Team)
3.  Strategy for handling network updates to packages within the Live environment. (Responsible: GParted Development Team)
4.  Formalization of the beta testing and bug triage process. (Responsible: Project Maintainers & Testers)
5.  Localization strategy for languages beyond the initial supported set. (Responsible: Documentation & Community Team)