**Purpose & Scope**
The system is a graphical partition editor for creating, reorganizing, and deleting disk partitions. It is a frontend to the GNU Parted library (libparted) and optional file system tools. It does not support logical volume management (LVM2) at present.

**Product Background / Positioning**
It is a Linux-based application that runs as a LiveCD/USB, residing in RAM and disappearing after reboot. It is a frontend to the command-line GNU Parted, providing a graphical interface. It depends on GNU libparted, Gtkmm, and various optional file system tools.

**Core Functional Overview**
*   Create or delete disk partitions.
*   Resize or move partitions while preserving data.
*   Copy and paste partitions (e.g., for disk cloning).
*   Format partitions to various file systems (e.g., ext2/3/4, NTFS, FAT32).
*   Create partition tables (e.g., msdos, gpt).
*   Check and repair file system errors.
*   Manage partition flags (e.g., boot, hidden).

**Key Users & Usage Scenarios**
Primary users are casual users needing to partition a drive, resize/move partitions, or clone data. They require basic understanding of disk partitions. The system also targets developers, testers, and documentation writers. All users have full administrative (root) access during a Live session.

**Major External Interfaces**
User interfaces are graphical (GTK+), presented via a main window with menus, toolbars, and dialogs. Hardware interfaces include hard disks, USB flash drives, and drives connected via IDE/SATA/RAID. It requires a functional keyboard, mouse, and CD/DVD drive or USB port to boot. Software interfaces are the underlying libparted and file system tools.

**Key Non-functional Requirements**
The application must run on x86-based computers regardless of the host operating system when booted from Live media. It is not computationally intensive and does not require significant system resources. No specific performance metrics or security constraints are defined for operations run from the Live environment.

**Constraints, Assumptions & Dependencies**
The system is constrained by the capabilities of the underlying libparted library and optional file system tools; not all operations are supported on all file systems. It assumes a working Linux environment (provided by the Live media) and a working CD/DVD drive or USB port for booting. It depends on third-party packages for file system manipulation.

**Priorities & Acceptance Approach**
Core partition operations (create, delete, resize/move, format) are fundamental. Support for a wide range of file systems and devices is a key quality. Acceptance is based on the successful, non-destructive completion of these operations on supported hardware and file systems, with clear user warnings for data-loss risks.