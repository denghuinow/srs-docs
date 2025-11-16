# Balanced Summary

**Goals and scope**  
GParted is a graphical partition editor for creating, reorganizing, and deleting disk partitions. It serves as a frontend to GNU Parted, providing an accessible GUI for disk management tasks without requiring installation. The software supports multiple file systems and runs as a LiveCD application, operating in RAM and disappearing after reboot.

**Roles and user stories**  
- As a casual user, I want to resize partitions so that I can reorganize disk space without data loss.  
- As a casual user, I want to create new partitions so that I can install additional operating systems.  
- As a developer, I want to extend file system support so that more partition types can be managed.  
- As a tester, I want to validate partition operations so that software reliability is ensured.  
- As a documentation writer, I want clear feature descriptions so that user guides remain accurate.

**Key processes**  
1. Boot from LiveCD/USB media (trigger: system startup).  
2. Select keyboard layout and language (trigger: user input during boot).  
3. Launch GParted desktop environment (trigger: completion of setup steps).  
4. Choose disk device from available drives (trigger: user selection).  
5. Perform partition operations like create, resize, or copy (trigger: user action).  
6. Apply or undo pending operations (trigger: user confirmation).  
7. Reboot system to finalize changes (trigger: user command).

**Domain data elements**  
- Device: primary key=device path, fields=model, size, heads, sectors  
- Partition: primary key=partition path, fields=size, file system, flags, label  
- Partition Table: primary key=table type, fields=type, sectors, alignment  
- File System: primary key=file system type, fields=supported operations, tools  
- Operation: primary key=operation ID, fields=type, status, target partition  
- Pending Changes: primary key=change ID, fields=operations list, apply status

**Non-functional requirements**  
- Performance: Must run efficiently on standard x86 hardware with minimal resources.  
- Safety: Warn users of potential data loss during destructive operations.  
- Compatibility: Support common file systems like ext4, NTFS, and FAT32.  
- Usability: Provide intuitive graphical interface for partition management.  
- Portability: Operate as LiveCD across Windows, Linux, and Mac systems.  
- Reliability: Include undo functionality to revert unintended changes.

**Milestones and external dependencies**  
- Depend on GNU libparted for core partition manipulation.  
- Require file system tools (e.g., e2fsprogs, ntfsprogs) for extended support.  
- Compatible with x86 systems and standard CD/DVD or USB boot methods.  
- Support from third-party documentation and community forums.  
- Future implementation of LVM2 support requested by users.

**Risks and mitigation strategies**  
- Data loss during partition operations: Implement warnings and undo functionality.  
- Unsupported file systems: Rely on third-party tools and clear compatibility tables.  
- Hardware recognition failures: Provide device refresh capability in GUI.  
- User error in complex operations: Offer detailed documentation and tutorials.  
- Dependency on external packages: Bundle essential tools in LiveCD image.

**Undecided issues**  
- LVM2 logical volume management support: Not implemented in current version.  
- Additional file system support: Dependent on third-party tool availability.  
- Enhanced network configuration: Limited to basic Terminal commands.  
- Automated error recovery: Basic check/repair provided but not comprehensive.  
- Localization completeness: Coverage for less common languages unknown.  
- Real-time partition monitoring: Not mentioned in current specification.