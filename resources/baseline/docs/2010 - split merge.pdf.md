```markdown
# Software Requirements Specification
## PDF Manipulation Tool

**Version:** 1.0  
**Date:** 2024-12-19  
**Status:** Final

---

## Table of Contents
1. [Introduction](#1-introduction)
2. [Overall Description](#2-overall-description)
3. [System Features](#3-system-features)
4. [External Interface Requirements](#4-external-interface-requirements)
5. [Non-Functional Requirements](#5-non-functional-requirements)
6. [Constraints, Assumptions & Dependencies](#6-constraints-assumptions--dependencies)
7. [Acceptance Criteria](#7-acceptance-criteria)

---

## 1 Introduction

### 1.1 Purpose
This document specifies the requirements for a free, open-source PDF manipulation tool that provides both graphical user interface (GUI) and console-based functionality. The software enables users to perform various PDF manipulation operations without commercial cost or licensing restrictions.

### 1.2 Scope
The system provides comprehensive PDF manipulation capabilities including splitting, merging, rotating, and visual reordering of PDF documents. The tool is designed to be platform-independent and accessible to both technical and non-technical users.

**In Scope:**
- PDF splitting by multiple criteria
- PDF merging and extraction
- Page rotation and reordering
- Both GUI and console interfaces
- Save/load working environments

**Out of Scope:**
- PDF viewing or content editing
- Security features (encryption/decryption)
- Integration with enterprise document management systems
- PDF form filling or annotation

### 1.3 Definitions, Acronyms, and Abbreviations
- **GUI**: Graphical User Interface
- **JRE**: Java Runtime Environment
- **GPLv2**: GNU General Public License version 2
- **PDF**: Portable Document Format

## 2 Overall Description

### 2.1 Product Perspective
This tool fills a market gap for multi-functional PDF handling software that is both free and open-source. It complements existing PDF viewers by providing manipulation capabilities that are typically only available in commercial software.

### 2.2 Product Functions
The core functionality includes:
- Split PDF documents using various criteria
- Merge multiple PDF files into single documents
- Rotate PDF pages in 90-degree increments
- Visually reorder pages via drag-and-drop interface
- Alternate page mixing for scanner output processing
- Environment saving for repetitive tasks

### 2.3 User Characteristics
**Primary User Groups:**
1. **General Users**: Non-technical individuals requiring simple PDF manipulation for personal document handling
2. **Developers**: Technical users utilizing console mode for batch processing and contributing to the open-source project

**User Assumptions:**
- Basic computer literacy for GUI users
- Command-line proficiency for console users
- Java Runtime Environment installation knowledge

### 2.4 Operating Environment
- **Platform**: Cross-platform (Windows, macOS, Linux)
- **Runtime**: Java Runtime Environment 1.6 or higher
- **Dependencies**: No external network services or third-party APIs required
- **Memory**: 254MB default (configurable for larger files)

## 3 System Features

### 3.1 PDF Splitting Capabilities
**3.1.1 Split by Page Count**
- Divide PDF into multiple documents based on specified page count
- Support for equal-sized chunks or custom page ranges
- Output naming convention with sequential numbering

**3.1.2 Split by Bookmarks**
- Use PDF bookmark structure to determine split points
- Maintain hierarchical organization in output files
- Preserve bookmark metadata in resulting documents

**3.1.3 Custom Rule Splitting**
- User-defined rules for splitting criteria
- Regular expression support for content-based splitting
- Flexible output configuration options

### 3.2 PDF Merging and Extraction
**3.2.1 Multi-PDF Merging**
- Combine multiple PDF files into single document
- Support for drag-and-drop file selection
- Preserve page order and orientation

**3.2.2 Page Extraction**
- Extract specific page ranges from source documents
- Support for discontinuous page selection
- Batch extraction from multiple source files

### 3.3 Page Alternation
**3.3.1 Scanner Output Processing**
- Alternate pages from two input PDFs
- Configurable alternation patterns
- Support for duplex scanning simulation

### 3.4 Rotation Operations
**3.4.1 Bulk Rotation**
- Rotate entire PDF documents in 90-degree increments
- Support for 90°, 180°, and 270° rotations
- Apply rotation to selected page ranges

### 3.5 Visual Page Management
**3.5.1 Drag-and-Drop Reordering**
- Visual interface for page rearrangement
- Thumbnail preview of pages
- Intuitive drag-and-drop functionality

**3.5.2 Page Deletion**
- Selective page removal via GUI
- Visual confirmation before deletion
- Undo capability for accidental deletions

### 3.6 Environment Management
**3.6.1 Save/Load Workspaces**
- Save current working environment including file selections and operations
- Load previously saved environments for repetitive tasks
- Export/import environment configurations

## 4 External Interface Requirements

### 4.1 User Interfaces
**4.1.1 Graphical User Interface (GUI)**
- **Technology**: Java Swing
- **Features**: 
  - Drag-and-drop file loading
  - Visual page thumbnails
  - Intuitive operation selection
  - Progress indicators for long operations
  - Context-sensitive help

**4.1.2 Console Interface**
- **Usage**: Command-line execution for batch processing
- **Features**:
  - Script-friendly parameter passing
  - Silent operation mode
  - Exit code reporting for automation
  - Comprehensive help system

### 4.2 Software Interfaces
- **Java Runtime**: Requires JRE 1.6 or higher
- **PDF Library**: Integrated PDF manipulation library
- **No External Dependencies**: Self-contained operation beyond JRE

### 4.3 Communication Interfaces
- **Update Checks**: Optional version update verification
- **No Network Operations**: All processing occurs locally
- **Offline Capable**: No internet connection required

## 5 Non-Functional Requirements

### 5.1 Performance Requirements
- **Response Time**: Direct response for all user interactions
- **Memory Usage**: Maximum 254MB default heap size (configurable)
- **File Processing**: Efficient handling of large PDF files (>100MB)
- **Concurrent Operations**: Single operation at a time with progress feedback

### 5.2 Safety Requirements
- **Input Preservation**: Original PDF files remain unchanged during processing
- **Data Integrity**: Output files maintain PDF specification compliance
- **Error Handling**: Graceful failure with informative error messages
- **Resource Cleanup**: Proper release of system resources after operations

### 5.3 Software Quality Attributes
- **Reliability**: Stable operation across multiple platforms
- **Usability**: Intuitive interface requiring minimal training
- **Maintainability**: Modular design supporting future enhancements
- **Portability**: Cross-platform compatibility via Java

### 5.4 License Compliance
- **Distribution**: Strictly GPLv2 licensed
- **Commercial Use**: No commercial redistribution allowed
- **Source Code**: Available and modifiable as per GPLv2 terms

## 6 Constraints, Assumptions & Dependencies

### 6.1 Constraints
- **Platform**: Dependent on Java Virtual Machine
- **Memory**: Limited by JVM heap size configuration
- **File Format**: Supports PDF specification 1.4 and later
- **License**: Must remain GPLv2 compliant

### 6.2 Assumptions
- Users have legitimate access to input PDF files
- No enterprise-level security requirements
- Single-user operation model
- Basic Java installation knowledge

### 6.3 Dependencies
- **Java Runtime**: JRE 1.6 or higher must be installed
- **Input Files**: User-provided PDF documents
- **Operating System**: No specific OS dependencies beyond JRE support

## 7 Acceptance Criteria

### 7.1 Functional Validation
All core features must pass the following tests:

**7.1.1 Splitting Operations**
- [ ] Split by page count produces correct number of output files
- [ ] Bookmark-based splitting maintains document structure
- [ ] Custom rules execute as specified

**7.1.2 Merging Operations**
- [ ] Multiple PDFs merge into single document correctly
- [ ] Page order preserved during merge operations
- [ ] Extraction produces accurate page subsets

**7.1.3 Rotation Operations**
- [ ] 90-degree rotations applied correctly to all pages
- [ ] Rotation does not corrupt document content
- [ ] Multiple rotation operations cumulative

**7.1.4 Visual Tools**
- [ ] Drag-and-drop reordering functions intuitively
- [ ] Page deletion removes specified pages only
- [ ] Thumbnail display accurate and responsive

### 7.2 Non-Functional Validation
- [ ] Memory usage remains within specified limits
- [ ] Original files remain unmodified during processing
- [ ] All operations complete with appropriate performance
- [ ] License compliance verified for distribution

### 7.3 Interface Validation
- [ ] GUI operates correctly across supported platforms
- [ ] Console interface supports all command-line operations
- [ ] Error conditions handled gracefully with user feedback

---

## Appendix A: Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-12-19 | SRS Generator | Initial SRS document creation |

## Appendix B: References

1. GNU General Public License v2.0
2. Java Platform Specifications
3. PDF Reference Manual (ISO 32000-1)
```