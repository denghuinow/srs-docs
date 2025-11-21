```markdown
# Software Requirements Specification
## Open Watcom C Compiler and Linker Linux Port with PIC and Shared Library Support

**Version:** 1.0  
**Date:** 2024-12-19  
**Status:** Draft  
**Authors:** Technical Requirements Team

---

## Table of Contents

1. [Introduction](#1-introduction)
   - [1.1 Purpose](#11-purpose)
   - [1.2 Scope](#12-scope)
   - [1.3 Definitions, Acronyms, and Abbreviations](#13-definitions-acronyms-and-abbreviations)
   - [1.4 References](#14-references)
   - [1.5 Overview](#15-overview)

2. [Overall Description](#2-overall-description)
   - [2.1 Product Perspective](#21-product-perspective)
   - [2.2 Product Functions](#22-product-functions)
   - [2.3 User Characteristics](#23-user-characteristics)
   - [2.4 Constraints](#24-constraints)
   - [2.5 Assumptions and Dependencies](#25-assumptions-and-dependencies)

3. [Specific Requirements](#3-specific-requirements)
   - [3.1 Compiler Requirements](#31-compiler-requirements)
   - [3.2 Linker Requirements](#32-linker-requirements)
   - [3.3 External Interface Requirements](#33-external-interface-requirements)
   - [3.4 System Features](#34-system-features)
   - [3.5 Non-Functional Requirements](#35-non-functional-requirements)

---

## 1 Introduction

### 1.1 Purpose
This document specifies the requirements for porting the Open Watcom C Compiler and Linker to Linux systems by adding Position-Independent Code (PIC) and shared library support. The target audience includes compiler developers, system programmers, and project stakeholders.

### 1.2 Scope
The project encompasses modifications to both the Open Watcom C compiler and linker to enable:
- Generation of Position-Independent Code (PIC)
- ELF object file output format support
- Creation and linking of shared libraries (.so files)
- Compatibility with existing Linux shared objects and dynamic linking infrastructure

### 1.3 Definitions, Acronyms, and Abbreviations

| Term | Definition |
|------|------------|
| **PIC** | Position-Independent Code - Code that can execute correctly regardless of its memory address |
| **ELF** | Executable and Linkable Format - Standard binary file format for Unix-like systems |
| **GOT** | Global Offset Table - Table used for accessing global variables in PIC |
| **PLT** | Procedure Linkage Table - Table used for function calls to shared libraries |
| **OMF** | Object Module Format - Current output format of Open Watcom compiler |
| **OWL** | Open Watcom Linker - The linker component being modified |

### 1.4 References
- System V Application Binary Interface
- ELF Specification Version 1.2
- Open Watcom Compiler Documentation
- Linux Standard Base Specification

### 1.5 Overview
This SRS document outlines the functional and technical requirements for enhancing the Open Watcom toolchain to support modern Linux binary formats and dynamic linking capabilities.

## 2 Overall Description

### 2.1 Product Perspective
The Open Watcom toolchain currently lacks support for Linux ELF format and dynamic linking. This project integrates the compiler and linker with the Linux executable ecosystem while maintaining backward compatibility with existing OMF format support.

### 2.2 Product Functions
1. **Compiler Enhancements**
   - Generate Position-Independent Code
   - Output ELF object files
   - Implement GOT-based addressing

2. **Linker Enhancements**
   - Create shared libraries (.so files)
   - Generate dynamic sections
   - Handle ELF relocations
   - Support program interpreter and dynamic dependencies

### 2.3 User Characteristics
- **Primary Users**: C developers targeting Linux systems
- **Technical Level**: Advanced users familiar with compiler toolchains
- **Expected Expertise**: Understanding of compilation, linking, and binary formats

### 2.4 Constraints

#### 2.4.1 Technical Constraints
- Current compiler only outputs OMF format
- Linker must handle ELF-specific relocations and symbol types
- Existing linker bugs must be resolved for basic ELF executable creation
- Must maintain compatibility with existing Open Watcom features

#### 2.4.2 Implementation Constraints
- Use OWL (Open Watcom Linker) for ELF object file output
- Follow System V ABI specifications for ELF and PIC
- Maintain cross-platform compatibility where possible

### 2.5 Assumptions and Dependencies
- Linux target system uses standard ELF implementation
- System V ABI conventions are followed by the host system
- Existing Open Watcom code generation architecture can be extended
- OWL linker architecture supports the required ELF extensions

## 3 Specific Requirements

### 3.1 Compiler Requirements

#### 3.1.1 PIC Support
**REQ-COMP-001**: The compiler shall generate Position-Independent Code when specified by command-line options.

**REQ-COMP-002**: The compiler shall implement GOT base register setup in function prologues for PIC.

**REQ-COMP-003**: The compiler shall generate PIC-compliant function prologues and epilogues.

**REQ-COMP-004**: The compiler shall use GOT-relative addressing for global data access in PIC mode.

#### 3.1.2 ELF Object File Generation
**REQ-COMP-005**: The compiler shall generate ELF format object files (.o) using OWL backend.

**REQ-COMP-006**: The compiler shall support ELF-specific symbol types and visibility attributes.

**REQ-COMP-007**: The compiler shall generate appropriate relocation entries for ELF object files.

### 3.2 Linker Requirements

#### 3.2.1 Shared Object Creation
**REQ-LINK-001**: The linker shall create shared library files (.so) with proper ELF dynamic sections.

**REQ-LINK-002**: The linker shall generate Global Offset Table (GOT) sections in shared objects.

**REQ-LINK-003**: The linker shall generate Procedure Linkage Table (PLT) sections for function calls.

**REQ-LINK-004**: The linker shall create dynamic symbol tables and hash sections.

#### 3.2.2 Dynamic Linking Support
**REQ-LINK-005**: The linker shall support specifying a program interpreter (PT_INTERP) for dynamic executables.

**REQ-LINK-006**: The linker shall process DT_NEEDED entries for required shared libraries.

**REQ-LINK-007**: The linker shall resolve symbols from shared libraries during linking.

**REQ-LINK-008**: The linker shall generate appropriate dynamic relocations.

#### 3.2.3 ELF Relocation Handling
**REQ-LINK-009**: The linker shall process ELF-specific relocation types including:
- R_386_GOT32
- R_386_PLT32
- R_386_COPY
- R_386_GLOB_DAT
- R_386_JMP_SLOT
- R_386_RELATIVE

**REQ-LINK-010**: The linker shall fix existing bugs preventing basic ELF executable creation.

### 3.3 External Interface Requirements

#### 3.3.1 Command-Line Interface
**REQ-CLI-001**: The compiler shall support `-fPIC` option to generate position-independent code.

**REQ-CLI-002**: The linker shall support `-shared` option to create shared libraries.

**REQ-CLI-003**: The linker shall support `-l<library>` and `-L<path>` options for library linking.

#### 3.3.2 File Format Interfaces
**REQ-FILE-001**: The compiler shall generate ELF32 object files compatible with Linux standards.

**REQ-FILE-002**: The linker shall produce ELF32 shared objects and executables.

**REQ-FILE-003**: The toolchain shall be able to link against existing Linux shared libraries.

### 3.4 System Features

#### 3.4.1 PIC Code Generation Feature
```c
// Example: PIC-compliant function prologue
void pic_function() {
    // GOT base register setup in prologue
    // GOT-relative global variable access
    // PIC-compliant function calls
}
```

**Requirements:**
- GOT base register (typically EBX) setup in function entry
- All global data accessed via GOT offsets
- Function calls use PLT-relative addressing

#### 3.4.2 Shared Library Creation Feature
**REQ-SHARED-001**: The linker shall create shared objects with proper:
- .dynamic section with DT_SONAME, DT_NEEDED entries
- .got and .plt sections
- .dynsym and .hash sections
- Appropriate segment headers (LOAD, DYNAMIC)

### 3.5 Non-Functional Requirements

#### 3.5.1 Performance Requirements
**REQ-PERF-001**: PIC code generation shall not introduce significant performance degradation compared to non-PIC code.

**REQ-PERF-002**: Shared library linking time shall be comparable to existing Linux toolchains.

#### 3.5.2 Compatibility Requirements
**REQ-COMPAT-001**: The enhanced toolchain shall maintain backward compatibility with existing OMF format projects.

**REQ-COMPAT-002**: Generated ELF files shall be compatible with standard Linux dynamic linkers (ld-linux.so).

#### 3.5.3 Quality Requirements
**REQ-QUAL-001**: The implementation shall pass relevant tests for ELF compliance.

**REQ-QUAL-002**: Generated shared libraries shall be loadable and executable by the system dynamic linker.

**REQ-QUAL-003**: The toolchain shall handle symbol versioning appropriately.

---

## Appendix A: ELF Section Requirements

### Required ELF Sections for Shared Objects
- `.text` - Executable code
- `.data` - Initialized data
- `.bss` - Uninitialized data
- `.got` - Global Offset Table
- `.plt` - Procedure Linkage Table
- `.dynamic` - Dynamic linking information
- `.dynsym` - Dynamic symbol table
- `.dynstr` - Dynamic string table
- `.hash` - Symbol hash table
- `.rel.dyn` - Runtime relocations
- `.rel.plt` - PLT relocations

## Appendix B: Relocation Types

### Essential x86 ELF Relocations
- **R_386_32** - 32-bit absolute address
- **R_386_PC32** - 32-bit PC-relative address
- **R_386_GOT32** - 32-bit GOT offset
- **R_386_PLT32** - 32-bit PLT entry offset
- **R_386_GOTOFF** - 32-bit GOT-relative offset
- **R_386_GOTPC** - 32-bit PC-relative GOT offset
- **R_386_RELATIVE** - Adjust by program base

---

*This document specifies the complete requirements for the Open Watcom Linux PIC and shared library support project. All requirements are subject to verification through testing and validation procedures.*
```