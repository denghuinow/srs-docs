# Software Requirements Specification for PeaZip

## 1. Introduction

### 1.1 Purpose
This document specifies software requirements for PeaZip version 2.7.1, a cross-platform file and archive manager application that provides a graphical interface for Open Source archiving and compression utilities.

### 1.2 Project Scope
PeaZip is a file and archive manager application offering archiving, compressing, and extracting capabilities. Key functions include:
- Creating and updating compressed archives
- Extracting content of compressed archives
- File and archive management tools (robust copy, split/join, secure deletion, byte comparison, checksums/hashes)
- Timestamp appending to archive names for backup purposes
- Two-factor authentication (password and keyfile) for archives
- Cross-platform compatibility with no additional software installation required

## 2. Overall Description

### 2.1 Product Perspective
PeaZip functions as a frontend GUI for multiple Open Source archiving and compression utilities, supporting a wide range of formats as a superset of WinRAR and WinZip capabilities. It operates independently of the host operating system and is available as a portable standalone application.

### 2.2 Product Features
- Archive creation in supported formats (7z, RAR, ZIP, etc.)
- Archive updating functionality
- Timestamp appending for archiving/backup purposes
- Two-factor authentication (password/keyfile)
- Archive content extraction
- Secure file/archive deletion
- Byte-to-byte file comparison
- Duplicate file detection and corruption checking
- File splitting and merging
- Information display (file count, modification dates, space occupation, file sizes)
- Hexadecimal content viewing
- Graphical monitoring of executed functions
- Command prompt execution capability

### 2.3 Operating Environment
- Compatible with all 64-bit and 32-bit Microsoft Windows versions
- Compatible with POSIX systems (Linux, BSD, UNIX-like OS)
- x86 compatible CPU requirement due to ASM performance sections
- Self-contained packages with all required software included

### 2.4 Design and Implementation Constraints
- Developed using Delphi/Kylix, Object Pascal, and Pascal languages
- Licensed under LGPL (100% Open Source and free)
- Developed under Lazarus IDE environment

## 3. System Features

### 3.1 System Feature 1: Browsing
Allows users to access all areas and objects of the computer system through multiple methods:
- Filesystem navigation
- Bookmarks access
- Recent archives access
- Direct path/archive opening
- Navigation toolbar (back, forward, up, refresh)

### 3.2 System Feature 2: Object Selection
Flexible selection methods for displayed objects in file manager interface:
- Select all objects
- Invert selection
- Selection by extension, attributes, size, and date
- Sort by selection status

### 3.3 System Feature 3: Interface Access and View Modes
Direct access to main application interfaces and view mode modification:
- Archiving layout access
- Extraction layout access
- Toggle browse/flat view
- Refresh functionality

### 3.4 System Feature 4: System Management Utilities
Access to computer system management tools:
- Disk utilities (clean, defrag, manage, remove)
- System management tools (control panel, computer management, task manager)
- Environment variables display
- System benchmark utility (MIPS and Core 2 Duo equivalent speed)

### 3.5 System Feature 5: File Management Utilities
Non-archiving related file management tools:
- Secure file deletion (multiple passes)
- Byte-to-byte file comparison
- File checking for duplicates and corruption
- File split/join functionality
- File information display
- Hexadecimal content preview

### 3.6 System Feature 6: Archive Extraction
Decompression and extraction of archive contents:
- Supported read-only formats: 7z, 7z-sfx, ARC/WRC, BZ2/TBZ2, GZ/TGZ, PAQ/LPAQ, PEA, QUAD/BALZ, split, TAR, UPX, ZIP, ACE, ARJ, CAB, CHM, COMPOUND, CPIO, ISO, Java archives, Linux packages, LHA/LZH, LZMA, Mac formats, NSIS, Open Office files, PAK/PK3/PK4, RAR, SMZIP, U3P, UDF, VHD, WIM, XAR, XPI, XZ, Z/TZ
- Multiple access methods through toolbar, context menus, and system integration
- Password/keyfile authentication for encrypted archives

### 3.7 System Feature 7: Archive Creation and Update
Compression of objects into archives and archive updating:
- Fully supported formats: 7z, 7z-sfx, ARC/WRC, BZ2/TBZ2, custom, GZ/TGZ, PAQ/LPAQ, PEA, QUAD/BALZ, split, TAR, UPX, ZIP
- Multiple access methods through menus, toolbar, and system integration
- Archive volume splitting capability
- Timestamp appending for backup purposes
- Password/keyfile encryption support

### 3.8 System Feature 8: Drag and Drop Support
Object transfer between system and application:
- Supported in file manager, create archive, and extraction interfaces
- File listing in archive creation interface when dragged to file manager
- Content extraction when dragged from application to system

### 3.9 System Feature 9: Two-Factor Authentication
Archive encryption with password and optional keyfile:
- Password requirement for encrypted archive access
- Optional keyfile for enhanced security
- Random password and keyfile generation capability
- Decryption support for encrypted files

### 3.10 System Feature 10: Graphic Progress Display
Real-time monitoring of executed functions through PeaLauncher:
- Progress information display
- Function result information
- Test/check feature support

### 3.11 System Feature 11: Feature Settings
Customization of application features:
- Language selection
- Backend application execution mode
- PeaLauncher behavior configuration
- Character encoding options
- Archive format preferences
- File management tool parameters
- Graphical interface customization (colors, icons, fonts, window opacity, toolbar buttons)

## 4. External Interface Requirements

### 4.1 User Interfaces
- File manager interface
- Create archive interface
- Extraction interface
- Settings interface
- PeaLauncher progress display
- Keyboard shortcuts support for all interfaces
- Mouse controls (double-click, right-click context menus, middle-click extraction)

### 4.2 Hardware Interfaces
- x86 compatible CPU requirement
- Minimal hardware requirements dependent on chosen algorithm and compression level

### 4.3 Software Interfaces
- Windows (32-bit and 64-bit) compatibility
- POSIX systems compatibility
- Self-contained packages with included dependencies

### 4.4 Communications Interfaces
- No mandatory communication interfaces
- Internet access recommended for online help and information

## 5. Other Nonfunctional Requirements

### 5.1 Performance Requirements
No specific performance requirements defined.

### 5.2 Safety Requirements
- Error handling with appropriate help messages
- Functionality with incorrect data/settings

### 5.3 Security Requirements
- Password/keyfile authentication for encrypted archives
- No password/keyfile recovery by other users
- Complete data removal in secure deletion procedures

### 5.4 Software Quality Attributes
- User-friendly interface suitable for users with minimal computer experience
- Comprehensive help documentation and tutorials
