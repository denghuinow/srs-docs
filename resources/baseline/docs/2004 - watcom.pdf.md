```markdown
# Software Requirements Specification
## Open Watcom C Compiler/Linker Linux ELF Shared Object Support

**Version:** 1.0  
**Date:** [Current Date]  
**Status:** Draft  
**Authors:** [Author Names]

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

## 1. Introduction

### 1.1 Purpose
This document specifies the requirements for extending the Open Watcom C Compiler and Linker to support Position-Independent Code (PIC) and shared object building on Linux ELF platforms. The primary focus is on enabling the creation of Linux-compatible shared libraries while maintaining compatibility with existing Open Watcom toolchain workflows.

### 1.2 Scope
The scope of this project includes:

**In-Scope:**
- Modifications to Open Watcom C Compiler for PIC code generation
- Linker enhancements for ELF shared object creation
- Implementation of GOT (Global Offset Table) and PLT (Procedure Linkage Table)
- Support for required ELF relocation types
- Dynamic linking support with proper .dynamic sections
- Fixes for segment mapping in .data and .bss sections

**Out-of-Scope:**
- Full Linux porting of other Open Watcom components
- Compiler optimization improvements
- Complete Linux environment integration
- Support for non-ELF Linux formats
- Modifications to Open Watcom IDE or debugger components

### 1.3 Definitions and Acronyms

| Term | Definition |
|------|------------|
| PIC | Position-Independent Code |
| ELF | Executable and Linkable Format |
| GOT | Global Offset Table |
| PLT | Procedure Linkage Table |
| ORL | Object Reading Library (Open Watcom component) |
| WLCore | Watcom Linker Core component |
| SVR4 | System V Release 4 ABI |
| LSB | Linux Standard Base |

## 2. Overall Description

### 2.1 Product Perspective
This extension builds upon the existing Open Watcom development toolchain, specifically leveraging:
- **ORL (Object Reading Library)**: For ELF object file parsing
- **WLCore**: Core linker functionality
- **LoadELF**: Existing ELF loading capabilities

The system integrates with the Linux dynamic linker (`/lib/ld-linux.so.2`) and follows System V ABI specifications for ELF format compliance.

### 2.2 Product Functions
- Generate position-independent code with proper relocation handling
- Build shared objects supporting both PIC and position-dependent code
- Enable linking against existing Linux shared libraries
- Implement ELF-compliant dynamic linking mechanisms
- Handle ELF object files with correct section mapping

### 2.3 User Characteristics
**Primary Users:**
- **Linux Developers**: Creating shared libraries for Linux applications
- **Application Developers**: Linking applications against shared objects
- **Security-Conscious Systems**: Requiring position-independent code for ASLR

**Technical Proficiency:** Users are expected to be familiar with:
- C programming language
- Linux development environment
- Command-line compilation and linking
- Shared library concepts

### 2.4 Operating Environment
- **Target OS**: Linux distributions supporting ELF format
- **Architecture**: IA32 (x86) architecture
- **ABI Compliance**: System V ABI for i386
- **Dependencies**: Existing Open Watcom toolchain (open_watcom_devel_1.1.7)

### 2.5 Design and Implementation Constraints
- Must maintain backward compatibility with existing Open Watcom command-line interfaces
- Limited to modifications in compiler and linker components only
- Must adhere to Linux Standard Base Specification for IA32 Architecture
- Dependent on correct ELF object file handling as defined in System V ABI

## 3. System Features

### 3.1 PIC Code Generation

#### 3.1.1 Description
The compiler shall generate position-independent code when the `-pic` switch is specified, implementing proper access to global data and function calls through GOT and PLT mechanisms.

#### 3.1.2 Requirements
- **PIC.1**: The compiler shall generate code that accesses global data through the GOT
- **PIC.2**: The compiler shall generate function calls through the PLT for external functions
- **PIC.3**: The compiler shall handle PC-relative addressing for local symbols
- **PIC.4**: The compiler shall support the `-pic` command-line switch to enable PIC generation

### 3.2 Shared Object Building

#### 3.2.1 Description
The linker shall be capable of building ELF shared objects from object files, supporting both PIC and position-dependent code models.

#### 3.2.2 Requirements
- **SO.1**: The linker shall create ELF shared objects with proper segment alignment
- **SO.2**: The linker shall generate required `.dynamic` section with appropriate entries
- **SO.3**: The linker shall support building shared objects from both PIC and non-PIC object files
- **SO.4**: The linker shall implement the `-elfdll` option for ELF shared object creation

### 3.3 Relocation Handling

#### 3.3.1 Description
The system shall correctly process and generate all required ELF relocation types for proper dynamic linking.

#### 3.3.2 Requirements
- **REL.1**: Support `R_386_GOT32` relocation for GOT-relative global data access
- **REL.2**: Support `R_386_GOTOFF` relocation for GOT-relative local symbol access
- **REL.3**: Support `R_386_GOTPC` relocation for GOT-relative PC calculations
- **REL.4**: Support `R_386_PLT32` relocation for PLT-relative function calls
- **REL.5**: Support `R_386_PC32` relocation for PC-relative addressing
- **REL.6**: Support `R_386_32` relocation for absolute addressing

### 3.4 Section Mapping and Segment Fixes

#### 3.4.1 Description
The system shall correctly map `.data` and `.bss` sections to prevent segmentation faults and ensure proper memory layout.

#### 3.4.2 Requirements
- **SEC.1**: The linker shall map `.data` section with proper read-write permissions
- **SEC.2**: The linker shall map `.bss` section with proper zero-initialization
- **SEC.3**: The system shall ensure correct segment alignment for shared objects
- **SEC.4**: The linker shall prevent overlapping segment mappings

### 3.5 Dynamic Linking Support

#### 3.5.1 Description
The system shall enable dynamic linking with existing Linux shared libraries and support the creation of dynamically linkable shared objects.

#### 3.5.2 Requirements
- **DL.1**: The linker shall resolve symbols from system shared libraries
- **DL.2**: The system shall generate proper `.dynsym`, `.dynstr`, and `.hash` sections
- **DL.3**: The linker shall create necessary `DT_NEEDED` entries in `.dynamic` section
- **DL.4**: The system shall support both lazy and immediate binding

## 4. External Interface Requirements

### 4.1 User Interfaces

#### 4.1.1 Command-Line Interface
```bash
# Compilation with PIC support
wcc -elf -pic source.c

# Shared object creation
wlink -elfdll -o libexample.so obj1.o obj2.o

# Linking against shared libraries
wlink -elf program.o -lexample
```

### 4.2 Hardware Interfaces
- **Processor**: IA32 (x86) architecture
- **Memory**: Standard Linux memory management
- **No special hardware requirements**

### 4.3 Software Interfaces

#### 4.3.1 Linux Dynamic Linker
- **Interface**: `/lib/ld-linux.so.2`
- **Purpose**: Runtime dynamic linking and loading
- **Requirements**: Compliance with Linux dynamic linking conventions

#### 4.3.2 ELF Object Format
- **Standard**: System V ABI ELF Specification
- **Sections**: Standard ELF section types and attributes
- **Relocations**: i386-specific relocation types

#### 4.3.3 Open Watcom Components
- **ORL**: Object file reading and parsing
- **WLCore**: Core linking functionality
- **LoadELF**: ELF-specific loading capabilities

### 4.4 Communications Interfaces
- **Standard output/error**: Compiler and linker messages
- **File I/O**: Object files, shared libraries, executables
- **No network communications required**

## 5. Non-Functional Requirements

### 5.1 Reliability
- **REL.1**: The system shall correctly handle all specified ELF relocation types without crashes
- **REL.2**: Generated shared objects shall not cause segmentation faults during execution
- **REL.3**: The linker shall provide meaningful error messages for unsupported operations

### 5.2 Performance
- **PERF.1**: PIC code generation shall not significantly degrade compilation performance
- **PERF.2**: Shared object linking time shall be comparable to static linking for similar-sized inputs
- **PERF.3**: Runtime performance of PIC code shall follow standard Linux shared library performance characteristics

### 5.3 Compatibility
- **COMP.1**: Generated shared objects shall be compatible with standard Linux dynamic linker
- **COMP.2**: The system shall maintain compatibility with existing Open Watcom command-line interfaces where possible
- **COMP.3**: Object files shall be compatible with other ELF-compliant tools (objdump, readelf, etc.)

### 5.4 Maintainability
- **MAINT.1**: Code modifications shall follow existing Open Watcom coding standards
- **MAINT.2**: New functionality shall be properly documented in source code comments
- **MAINT.3**: The implementation shall be modular to facilitate future enhancements

## 6. Constraints, Assumptions & Dependencies

### 6.1 Constraints
- **CON.1**: Limited to Linux environments with ELF support
- **CON.2**: Dependent on existing Open Watcom source code (open_watcom_devel_1.1.7)
- **CON.3**: Must adhere to System V ABI specifications for ELF handling
- **CON.4**: No modifications to Open Watcom runtime libraries

### 6.2 Assumptions
- **ASM.1**: Target system follows Linux Standard Base Specification for IA32 Architecture
- **ASM.2**: Users have basic understanding of shared library concepts
- **ASM.3**: Development environment provides standard Linux development tools
- **ASM.4**: Existing Open Watcom components are stable and functional

### 6.3 Dependencies
- **DEP.1**: Correct functioning of ORL for ELF file parsing
- **DEP.2**: Proper symbol handling in WLCore component
- **DEP.3**: Availability of Linux system headers and libraries
- **DEP.4**: Resolution of existing relocation and symbol handling issues in base code

## 7. Acceptance Criteria

### 7.1 Priority-Based Acceptance Tests

#### 7.1.1 Highest Priority: Relocation Handling
- **TEST-REL-1**: Successful compilation and linking of code using `R_386_GOT32` relocations
- **TEST-REL-2**: Correct handling of `R_386_PLT32` relocations for external function calls
- **TEST-REL-3**: Proper processing of `R_386_PC32` relocations for position-independent code

#### 7.1.2 Second Priority: Section Mapping
- **TEST-SEC-1**: No segmentation faults when accessing global data in shared objects
- **TEST-SEC-2**: Correct zero-initialization of `.bss` section variables
- **TEST-SEC-3**: Proper read-write permissions for `.data` section in generated shared objects

#### 7.1.3 Third Priority: PIC Code Generation
- **TEST-PIC-1**: Successful compilation with `-pic` switch without errors
- **TEST-PIC-2**: Generated PIC code executes correctly when loaded at different addresses
- **TEST-PIC-3**: GOT and PLT are properly generated and utilized

### 7.2 Integration Tests
- **TEST-INT-1**: Successful "Hello, world" compilation and execution using shared objects
- **TEST-INT-2**: Linking against standard Linux shared libraries (libc, etc.)
- **TEST-INT-3**: Creation and usage of custom shared libraries between multiple applications
- **TEST-INT-4**: Compatibility testing with standard Linux tools (ldd, objdump, readelf)

### 7.3 Performance Benchmarks
- **TEST-PERF-1**: Compilation time with PIC enabled vs disabled (within 15% variance)
- **TEST-PERF-2**: Runtime performance of PIC code vs static code (within expected overhead)
- **TEST-PERF-3**: Shared object loading time comparable to gcc-generated shared libraries

---

## Appendix A: References

1. System V Application Binary Interface Edition 4.1
2. Linux Standard Base Specification
3. Open Watcom Development Environment Documentation
4. ELF: Executable and Linkable Format Specification

## Appendix B: Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial SRS document creation |
```