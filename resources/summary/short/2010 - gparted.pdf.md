# Short Summary: GParted 0.6.0-1 Requirements

## Background and objectives
GParted is a graphical partition editor for creating, reorganizing, and deleting disk partitions, serving as a frontend to the GNU Parted library. This document specifies the requirements for version 0.6.0-1, a LiveCD application that runs at system boot without installation.

## In scope
*   Core partition operations: create, delete, resize/move, copy/paste, format, and label partitions.
*   Support for multiple file systems including ext2/3/4, FAT16/32, NTFS, and others.
*   Management of partition tables (e.g., msdos, gpt) and partition flags (e.g., boot, hidden).
*   Basic system utilities: device information viewing, screenshot capture, and terminal access.
*   User interface for managing pending operations with undo/apply functionality.

## Out of scope
*   Logical Volume Management (LVM2) support.
*   Operations on file systems not supported by underlying libraries (libparted and optional tools).
*   Permanent installation or modification of the host operating system's files.
*   Advanced network configuration or remote management features.
*   Data recovery or backup services beyond partition copying.

## Stakeholders and core use cases
*   **Casual Users**: Individuals needing to manage disk partitions; require basic computer knowledge.
*   **Developers**: Contributors interested in improving the application, fixing bugs, and adding features.
*   **Testers**: Individuals who test beta versions and report bugs via the tracking system.
*   **Documentation Writers**: Individuals who create user guides and help files based on the software's functions.

**User Stories:**
1.  As a casual user, I want to resize a partition to free up disk space so that I can install a new operating system.
2.  As a casual user, I want to format a partition to a specific file system so that it is compatible with my intended use.
3.  As a casual user, I want to copy a partition to a new drive so that I can migrate my data and operating system.
4.  As a developer, I want to understand the system's functional requirements so that I can implement new features correctly.
5.  As a tester, I want a clear specification of system features so that I can design comprehensive test cases.
6.  As a documentation writer, I want a detailed description of the user interface so that I can create accurate user manuals.

## Success metrics
*   Successful completion of all core partition operations (create, delete, resize, copy, format) without data loss when used correctly.
*   Support for the listed file systems and partition table types as specified in the compatibility matrix.
*   The application boots and runs on standard x86 hardware from CD/USB media as intended.

## Major constraints
*   Dependence on third-party libraries (libparted) and optional file system tools for core functionality.
*   Must run as a LiveCD/USB application without installing to a hard drive.
*   Limited to x86-based computer architectures.
*   Does not support every operation on every file system; capabilities depend on underlying tools.
*   Requires a functional CD/DVD drive or USB port for booting the Live version.

## Undecided issues
*   Future implementation of Logical Volume Management (LVM2) support, as requested by users.
*   Expansion of supported file systems and operations in subsequent releases.
*   Potential enhancements to the graphical user interface based on user feedback.
*   Methods for improving error handling and user warnings during risky operations.
*   Strategies for better integration or support within various host operating systems.