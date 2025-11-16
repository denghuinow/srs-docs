# Short Summary

- **Background and objectives**: GParted is a graphical partition editor designed to create, reorganize, and delete disk partitions using a simple GUI, based on GNU Parted libraries. It aims to provide an accessible tool for disk management without requiring installation, running as a LiveCD from RAM.

- **In scope**:
  - Create, delete, resize, move, copy, and check partitions.
  - Format partitions to supported file systems (e.g., ext4, NTFS, FAT32).
  - Manage partition flags (e.g., boot, hidden).
  - View device information and refresh connected devices.
  - Undo, apply, or clear pending partition operations.

- **Out of scope**:
  - Logical Volume Management (LVM2) support.
  - Operations on unsupported file systems or actions not permitted by underlying tools.
  - Permanent installation or modification of host operating systems.
  - Network or communication features as a primary function.
  - Advanced data recovery or backup services.

- **Roles and core use cases**:
  - As a casual user, I want to resize partitions so that I can reorganize disk space without data loss.
  - As a developer, I want to extend file system support so that GParted can handle more disk formats.
  - As a tester, I want to validate partition operations so that the application remains stable and reliable.

- **Success metrics**:
  - Supports all listed file system actions (create, resize, check, etc.) without data corruption.
  - Runs on x86 systems regardless of host OS (Linux, Windows, macOS via LiveCD).
  - User interface remains simple and accessible for non-technical users.

- **Major constraints**:
  - Requires GNU Parted and specific file system tools as dependencies.
  - Limited to actions supported by underlying libraries (e.g., libparted).
  - No support for LVM or certain advanced storage configurations.
  - Operates only on x86-based hardware.
  - No responsibility for data loss; users must backup data before operations.

- **Undecided issues**:
  - Future support for LVM2.
  - Expansion to non-x86 architectures.
  - Enhanced network or remote management capabilities.
  - Integration with cloud or external storage systems.
  - Localization for additional languages beyond those listed.