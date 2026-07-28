**Purpose & Scope**
GParted is a graphical partition editor for creating, reorganizing, and deleting disk partitions, operating as a frontend to the GNU Parted library.

**Core Functions**
*   Create, delete, resize, move, copy, and format disk partitions.
*   Check and repair supported file systems.
*   Manage partition tables and flags.

**Key Constraints**
*   Must use GNU libparted to detect and manipulate devices and partition tables.
*   Does not support logical volume management (LVM2).
*   Specific partition operations depend on third-party file system tools.