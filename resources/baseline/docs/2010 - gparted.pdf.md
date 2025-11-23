# Software Requirements Specification (SRS) for GParted

## 1. Introduction

### 1.1 Purpose
This document specifies the requirements for GParted (GNOME Partition Editor), a LiveCD-based disk partitioning tool. It serves as a comprehensive guide for developers, testers, and stakeholders to understand the system's capabilities, constraints, and operational parameters.

### 1.2 Scope
GParted is a graphical partition management application that operates as a LiveCD/LiveUSB system, running entirely in RAM without requiring installation on the host machine. The system provides complete disk partitioning functionality while explicitly excluding LVM support, data recovery guarantees, and direct operating system installation capabilities.

**In Scope:**
- Partition creation, deletion, resizing, and movement
- Partition copying and formatting
- File system checking and repair
- Partition flag management
- Operation via graphical user interface

**Out of Scope:**
- Logical Volume Manager (LVM) support
- Data recovery services or guarantees
- Operating system installation
- Persistent installation on host systems

### 1.3 Definitions, Acronyms, and Abbreviations
- **LiveCD**: A bootable CD containing an operating system that runs entirely in RAM
- **LVM**: Logical Volume Manager
- **GUI**: Graphical User Interface
- **libparted**: Core partitioning library used by GParted
- **RAM**: Random Access Memory

### 1.4 References
- GNU Parted Documentation
- libparted API Reference
- Linux File System Tools Documentation

## 2. Overall Description

### 2.1 Product Perspective
GParted serves as a graphical frontend to the GNU Parted command-line tool, providing an intuitive interface for partition management while maintaining compatibility with existing Linux ecosystems. The application operates independently of any host operating system through its LiveCD/LiveUSB implementation.

### 2.2 Product Functions
| Function | Description | Priority |
|----------|-------------|----------|
| Partition Creation | Create new partitions on storage devices | High |
| Partition Deletion | Remove existing partitions from storage devices | High |
| Partition Resizing | Modify partition sizes while preserving data | High |
| Partition Movement | Relocate partitions on disk | Medium |
| Partition Copying | Duplicate partitions between locations | Medium |
| Partition Formatting | Apply file systems to partitions | High |
| File System Checking | Verify file system integrity | Medium |
| File System Repair | Fix file system errors | Medium |
| Flag Management | Set partition attributes (bootable, hidden, etc.) | Medium |

### 2.3 User Characteristics
#### 2.3.1 Primary Users: Casual Users
- **Technical Level**: Basic to intermediate computer literacy
- **Primary Goal**: Perform disk partitioning tasks through graphical interface
- **Usage Pattern**: Occasional use for system maintenance or setup
- **Privileges**: Root access in LiveCD environment

#### 2.3.2 Secondary Users: Developers and Testers
- **Technical Level**: Advanced Linux and programming knowledge
- **Primary Goal**: Code development, testing, and quality assurance
- **Usage Pattern**: Regular interaction during development cycles
- **Privileges**: Root access with development tools

### 2.4 Constraints
- **Hardware**: Requires CD/DVD drive or USB port for booting
- **Architecture**: Limited to x86/x86-64 hardware platforms
- **Dependencies**: Requires libparted library and file system-specific tools
- **Exclusions**: No LVM support implemented
- **Persistence**: No data persistence after reboot

### 2.5 Assumptions and Dependencies
- Users possess basic understanding of disk partitioning concepts
- Hardware meets minimum requirements for Linux LiveCD operation
- Storage devices use standard interfaces (SATA, IDE, SCSI, USB)
- File system tools are available for supported file systems
- No network connectivity required for core operations

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 User Interfaces
**Main Application Window**
- Device selection panel displaying available storage devices
- Graphical partition layout representation
- Toolbar with primary operations (Create, Delete, Resize, etc.)
- Status bar showing operation progress and device information

**Dialog Interfaces**
- Partition creation dialog (size, type, file system selection)
- Resize/Move operation dialog with visual size adjustment
- Format partition dialog (file system type, options)
- Operation confirmation dialogs with warning messages

**Menu Structure**
```
File
  → Refresh Devices
  → Device Information
  → Exit

Edit
  → Undo
  → Apply All Operations

View
  → Device Information
  → File System Support
  → Available Operations

Partition
  → New
  → Delete
  → Resize/Move
  → Copy
  → Paste
  → Format to
  → Manage Flags

Help
  → About
  → Documentation
```

#### 3.1.2 Hardware Interfaces
- **Boot Media**: CD/DVD drives or USB ports for Live environment
- **Storage Devices**: Standard storage interfaces (SATA, IDE, SCSI, USB)
- **Memory**: Sufficient RAM for LiveCD operation and partitioning operations

#### 3.1.3 Software Interfaces
- **libparted**: Core partitioning operations library (v3.0+)
- **File System Tools**: 
  - e2fsprogs (ext2/ext3/ext4)
  - dosfstools (FAT16/FAT32)
  - ntfs-3g (NTFS)
  - xfsprogs (XFS)
  - btrfs-progs (BTRFS)
- **Graphical Environment**: GTK+ for GUI components

### 3.2 Functional Requirements

#### 3.2.1 Partition Management

**FR-001: Partition Creation**
```markdown
**Description**: System shall allow creation of new partitions on storage devices
**Input**: Device selection, partition size, type, file system
**Processing**: Validate parameters, check for available space, create partition
**Output**: New partition created with specified parameters
**Constraints**: Must not overwrite existing data without explicit confirmation
```

**FR-002: Partition Deletion**
```markdown
**Description**: System shall allow deletion of existing partitions
**Input**: Partition selection, confirmation
**Processing**: Verify selection, remove partition entry from partition table
**Output**: Partition removed and space marked as available
**Constraints**: Must require explicit user confirmation due to data loss risk
```

**FR-003: Partition Resizing**
```markdown
**Description**: System shall resize partitions while preserving data
**Input**: Partition selection, new size parameters
**Processing**: Verify file system support, resize file system, update partition table
**Output**: Partition resized with data integrity maintained
**Constraints**: Dependent on file system tool capabilities
```

**FR-004: Partition Movement**
```markdown
**Description**: System shall relocate partitions on disk
**Input**: Partition selection, new location parameters
**Processing**: Move partition data, update partition table
**Output**: Partition relocated to specified position
**Constraints**: High risk operation requiring multiple confirmations
```

#### 3.2.2 File System Operations

**FR-005: Partition Formatting**
```markdown
**Description**: System shall format partitions with specified file systems
**Input**: Partition selection, file system type, format options
**Processing**: Apply file system to partition, initialize structures
**Output**: Formatted partition ready for use
**Constraints**: Destroys existing data - requires confirmation
```

**FR-006: File System Checking**
```markdown
**Description**: System shall verify file system integrity
**Input**: Partition selection
**Processing**: Run file system check utility, analyze results
**Output**: Report file system health status
**Constraints**: Dependent on file system-specific tools
```

**FR-007: File System Repair**
```markdown
**Description**: System shall attempt to repair file system errors
**Input**: Partition selection, repair options
**Processing**: Execute file system repair utilities
**Output**: Repaired file system or error report
**Constraints**: No guarantee of data recovery or repair success
```

#### 3.2.3 Advanced Operations

**FR-008: Partition Copying**
```markdown
**Description**: System shall copy partition contents to another location
**Input**: Source partition, destination selection
**Processing**: Duplicate partition data and structure
**Output**: Identical copy of source partition
**Constraints**: Requires sufficient destination space
```

**FR-009: Flag Management**
```markdown
**Description**: System shall manage partition attributes and flags
**Input**: Partition selection, flag toggles (boot, hidden, etc.)
**Processing**: Update partition table flags
**Output**: Modified partition attributes
**Constraints**: Limited to supported partition table types
```

### 3.3 Non-Functional Requirements

#### 3.3.1 Performance Requirements
- **Boot Time**: LiveCD environment should boot within 2 minutes on standard hardware
- **Operation Response**: GUI should remain responsive during partitioning operations
- **Memory Usage**: Should not exceed 512MB RAM during normal operation
- **Operation Duration**: Partition operations should complete within reasonable time based on device speed and data size

#### 3.3.2 Reliability Requirements
- **Data Integrity**: Highest priority on preventing data loss during operations
- **Operation Atomicity**: Operations should be atomic where possible, with rollback capabilities
- **Error Handling**: Clear error messages and safe failure modes
- **Stability**: System should not crash during partitioning operations

#### 3.3.3 Usability Requirements
- **Learnability**: Casual users should be able to perform basic operations with minimal training
- **Efficiency**: Common tasks should be accessible through intuitive GUI elements
- **Error Prevention**: Clear warnings for destructive operations
- **Accessibility**: Compliance with standard Linux accessibility guidelines

#### 3.3.4 Supportability Requirements
- **Logging**: Detailed operation logs for troubleshooting
- **Documentation**: Comprehensive user and developer documentation
- **Testing**: Automated test suite for core functionality

#### 3.3.5 Implementation Constraints
- **Platform**: Must run on standard x86/x86-64 hardware
- **Dependencies**: Limited to open-source libraries and tools
- **Distribution**: LiveCD format with no installation requirement

### 3.4 Safety and Security Requirements
- **Data Safety**: Multiple confirmation steps for destructive operations
- **Access Control**: All operations run with root privileges in LiveCD mode
- **Validation**: Extensive parameter validation before executing operations
- **Warning Systems**: Clear, unambiguous warnings for risky operations

## 4. System Features

### 4.1 LiveCD Operation
The system shall operate entirely from bootable media without requiring installation, with all temporary data stored in RAM and cleared upon reboot.

### 4.2 Graphical Partition Management
Comprehensive GUI for all partitioning operations, replacing command-line tools with visual representation and point-and-click operation.

### 4.3 Multi-File System Support
Support for common Linux and cross-platform file systems including ext2/3/4, FAT16/32, NTFS, XFS, and BTRFS.

### 4.4 Operation Queueing
Ability to queue multiple operations and execute them in sequence with a single confirmation step.

## 5. Appendices

### 5.1 Accepted File Systems
- ext2, ext3, ext4
- FAT16, FAT32
- NTFS
- XFS
- BTRFS
- ReiserFS
- Linux SWAP

### 5.2 Supported Partition Tables
- MSDOS (MBR)
- GPT (GUID Partition Table)

### 5.3 Excluded Features
The following features are explicitly excluded from this specification:
- Logical Volume Manager (LVM) support
- Data recovery capabilities
- Operating system installation
- Network-based operations
- RAID management

---

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-01-01 | SRS Author | Initial SRS document creation |

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Manager | | | |
| Lead Developer | | | |
| Quality Assurance | | | |