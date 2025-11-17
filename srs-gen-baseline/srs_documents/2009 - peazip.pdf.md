Here is a comprehensive Software Requirements Specification document for the PeaZip project, following professional standards and markdown formatting.

# Software Requirements Specification (SRS) for PeaZip

## 1. Introduction

### 1.1 Purpose
This document provides a detailed description of the Software Requirements Specification for PeaZip, a cross-platform file and archive manager. It specifies the functional and non-functional requirements, constraints, and system characteristics. This SRS is intended for use by the development team, project managers, and stakeholders to guide the design, implementation, and verification of the software.

### 1.2 Project Scope
PeaZip is a graphical file and archive management utility that provides a unified interface for numerous open-source compression technologies. The application enables users to create, extract, and manage archives and files across multiple operating systems, with an emphasis on security, flexibility, and user customization.

### 1.3 Definitions, Acronyms, and Abbreviations
- **SRS**: Software Requirements Specification
- **LGPL**: GNU Lesser General Public License
- **ASM**: Assembly Language
- **GUI**: Graphical User Interface
- **CPU**: Central Processing Unit
- **x86**: Family of instruction set architectures based on the Intel 8086 CPU

### 1.4 References
- LGPL License Version 2.1 or later
- Delphi/Kylix Development Environment Documentation
- Object Pascal Language Specification

## 2. Overall Description

### 2.1 Product Perspective
PeaZip is a standalone desktop application that serves as a front-end for various command-line compression utilities. It integrates these utilities into a cohesive graphical interface while adding additional file management capabilities.

### 2.2 Product Functions
The core functions of PeaZip include:
- Archive creation in multiple formats
- Archive extraction from various formats
- File management operations
- Security features including encryption
- Application customization

### 2.3 User Characteristics
The typical users of PeaZip are:
- **End Users**: Individuals requiring file compression/decompression capabilities
- **Power Users**: Users needing advanced file management and security features
- **System Administrators**: Professionals managing files across multiple systems

### 2.4 Constraints
#### 2.4.1 Technical Constraints
- Must be developed using Delphi, Kylix, or Object Pascal programming languages
- Requires x86-compatible CPU architecture due to performance-critical ASM code
- Must comply with LGPL open-source licensing requirements

#### 2.4.2 Platform Constraints
- Cross-platform compatibility required (Windows, Linux)
- Windows-specific feature: Drag-and-drop from application to system

### 2.5 Assumptions and Dependencies
- Underlying compression utilities (7-Zip, p7zip, etc.) are available and properly installed
- Target systems meet minimum hardware requirements for x86 compatibility
- Operating systems provide necessary APIs for file system operations

## 3. System Features and Requirements

### 3.1 Archive Creation

#### 3.1.1 Functional Requirements
**FR-001: Multi-format Archive Creation**
- The system shall allow users to create archives in the following formats:
  - 7Z
  - ZIP
  - TAR
  - GZIP
  - BZIP2
  - Other supported open-source formats

**FR-002: Optional Encryption**
- The system shall provide encryption options during archive creation
- The system shall support password-based encryption for sensitive formats
- The system shall implement industry-standard encryption algorithms

**FR-003: Compression Configuration**
- The system shall allow users to configure compression levels
- The system shall provide options for archive splitting by size
- The system shall support solid archive creation where applicable

### 3.2 Archive Extraction

#### 3.2.1 Functional Requirements
**FR-010: Multi-format Archive Extraction**
- The system shall extract contents from archives in all supported formats
- The system shall automatically detect archive format
- The system shall handle corrupted or partially damaged archives when possible

**FR-011: Extraction Options**
- The system shall provide options for extraction path selection
- The system shall support overwrite policies for existing files
- The system shall maintain directory structures during extraction

### 3.3 File Management

#### 3.3.1 Functional Requirements
**FR-020: Secure Deletion**
- The system shall provide secure file deletion using multiple pass algorithms
- The system shall implement recognized secure deletion standards (DoD 5220.22-M, Gutmann, etc.)
- The system shall provide verification of secure deletion operations

**FR-021: File Splitting and Joining**
- The system shall split large files into smaller segments of user-defined size
- The system shall rejoin split files to their original state
- The system shall maintain integrity checks during split/join operations

**FR-022: Checksum Calculation and Verification**
- The system shall calculate file checksums using multiple algorithms (MD5, SHA-1, SHA-256, etc.)
- The system shall verify file integrity against provided checksums
- The system shall generate checksum files in standard formats

### 3.4 Application Customization

#### 3.4.1 Functional Requirements
**FR-030: Settings Configuration**
- The system shall provide a comprehensive settings menu for application behavior customization
- The system shall allow interface theme and layout customization
- The system shall save user preferences between sessions

**FR-031: Integration Settings**
- The system shall configure file type associations
- The system shall manage context menu integrations where supported by the OS

## 4. External Interface Requirements

### 4.1 User Interfaces
- **Main Application Window**: Graphical interface for all archive and file operations
- **Context Menus**: OS-integrated right-click menus for quick access to common functions
- **Dialog Windows**: Modal windows for specific operations (save, extract, settings)
- **Progress Indicators**: Visual feedback for long-running operations

### 4.2 Hardware Interfaces
- **x86 CPU**: Required for performance-critical assembly code operations
- **Storage Systems**: Compatibility with FAT32, NTFS, ext4, and other common file systems
- **Input Devices**: Standard keyboard and mouse support

### 4.3 Software Interfaces
- **Operating Systems**: Windows (all supported versions), Linux (major distributions)
- **Compression Utilities**: Integration with 7-Zip, p7zip, and other open-source tools
- **File Systems**: Access to local and network file systems

### 4.4 Communication Interfaces
- No network communication interfaces required for core functionality
- Local inter-process communication with compression utilities

## 5. Non-Functional Requirements

### 5.1 Performance Requirements
**NF-001: Operation Performance**
- Archive creation and extraction operations shall utilize available system resources efficiently
- The application shall remain responsive during file operations
- Memory usage shall be optimized for large file operations

**NF-002: Startup Performance**
- The application shall initialize within 5 seconds on standard hardware
- The application shall load necessary compression modules efficiently

### 5.2 Safety and Security Requirements
**NF-010: Data Security**
- Encryption implementations shall use proven cryptographic algorithms
- Password handling shall follow security best practices
- Temporary files shall be securely handled and removed

### 5.3 Software Quality Attributes

#### 5.3.1 Reliability
- The system shall maintain data integrity during all operations
- The system shall handle unexpected errors gracefully without data loss
- The system shall provide operation recovery mechanisms where possible

#### 5.3.2 Usability
- The user interface shall be intuitive for both novice and advanced users
- Common operations shall be accessible with minimal steps
- Comprehensive help and documentation shall be provided

#### 5.3.3 Portability
- The codebase shall maintain compatibility across Windows and Linux platforms
- Platform-specific code shall be properly isolated and documented

### 5.4 Legal and Licensing Requirements
**NF-020: Open Source Compliance**
- The software shall be distributed under LGPL license
- All third-party components shall be compatible with LGPL requirements
- Source code shall be made publicly available

## 6. Other Requirements

### 6.1 Development Constraints
- Codebase must be maintained in Delphi/Kylix/Object Pascal
- Critical performance sections may be implemented in x86 Assembly
- All platform-specific implementations must be clearly documented

### 6.2 Platform-Specific Features
**PS-001: Windows-Specific Functionality**
- Drag-and-drop from application to Windows shell is supported
- Windows context menu integration available
- Windows-specific file attribute handling

**PS-002: Linux-Specific Functionality**
- Linux desktop environment integration
- POSIX compliance for file operations
- Linux file permission preservation

### 6.3 Installation and Deployment
- The application shall provide installer packages for supported platforms
- The application shall include all necessary compression utilities
- The application shall manage file associations during installation

---

## Appendix A: Supported Archive Formats

### Input/Extraction Formats
7Z, ACE, ARJ, BZ2, CAB, CHM, CPIO, DEB, DMG, FAT, GZ, HFS, ISO, LHA, LZH, LZMA, MBR, MSI, NSIS, NTFS, RAR, RPM, SquashFS, TAR, UDF, VHD, WIM, XAR, XZ, Z, ZIP

### Output/Creation Formats
7Z, BZ2, GZ, TAR, ZIP, Z

---

**Document Version:** 1.0  
**Last Updated:** [Current Date]  
**Status:** Draft