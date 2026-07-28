# Software Requirements Specification (SRS)
## Open Watcom C Compiler & Linker Port to Linux with PIC/Shared Library Support

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the enhancement of the Open Watcom C Compiler and Linker to support the Linux platform. The core enhancement is the addition of Position-Independent Code (PIC) and ELF shared library (shared object) generation and consumption capabilities. This document is intended for use by the development team, quality assurance, project managers, and stakeholders.

#### 1.2 Scope
The scope of this project is the modification of the existing Open Watcom compiler suite (`open_watcom_devel_1.1.7` source base) to enable it to function as a native Linux toolchain. This involves:
*   Extending the x86 code generator (`GC386`) to produce PIC for the ELF target.
*   Enhancing the compiler driver (`wcc386`) and object writing library (`OWL`) to generate standard ELF object files.
*   Extending the linker (`wlink`) and its core (`WLCore`) to build ELF shared libraries and link executables against them.
*   Correcting known bugs in the existing ELF support within the Object Reading Library (`ORL`) and linker.

**Out of Scope:**
*   Creation of a new object file format.
*   Development of a new code generator from scratch.
*   Support for Linux targets other than x86 (i386).
*   Modification of the compiler's front-end or optimization passes unrelated to PIC/ELF output.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **ABI:** Application Binary Interface
*   **ELF:** Executable and Linkable Format
*   **GOT:** Global Offset Table
*   **OMF:** Object Module Format (Watcom's traditional format)
*   **ORL:** Object Reading Library (Open Watcom component)
*   **OWL:** Object Writing Library (Open Watcom component)
*   **PIC:** Position-Independent Code
*   **PLT:** Procedure Linkage Table
*   **SRS:** Software Requirements Specification
*   **WLCore:** Linker Core (Open Watcom component)

#### 1.4 References
*   System V Application Binary Interface, Edition 4.1
*   System V ABI Intel386 Architecture Processor Supplement, Fourth Edition
*   `open_watcom_devel_1.1.7` Source Code Repository
*   Tool Interface Standard (TIS) Executable and Linking Format (ELF) Specification, Version 1.2

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its users, and constraints. Section 3 details the specific functional requirements. Section 4 outlines the non-functional requirements, including compatibility and performance.

### 2. Overall Description

#### 2.1 Product Perspective
This project is an enhancement module integrated into the existing Open Watcom open-source compiler suite. It modifies and extends several core subsystems:
*   **Compiler Driver (`wcc386`):** To accept new target flags.
*   **Code Generator (`GC386`):** To emit PIC sequences.
*   **Object Writing Library (`OWL`):** To write ELF32-i386 object files with necessary relocations.
*   **Linker (`wlink`) & WLCore:** To process ELF files, perform dynamic linking, and create shared objects.
*   **Object Reading Library (`ORL`):** To correctly parse ELF symbols and relocations from input files.

The system interacts with the host Linux operating system by producing binaries that are consumed by the Linux kernel loader and dynamic linker (`/lib/ld-linux.so.2`).

#### 2.2 Product Functions
The high-level functions of the enhanced system are:
1.  Compile C source code into ELF format object files, with or without PIC.
2.  Link multiple ELF object files into a statically linked Linux executable.
3.  Link multiple ELF object files (compiled as PIC) into an ELF shared library (`.so` file).
4.  Link an executable against one or more ELF shared libraries (both system and user-created).
5.  Correctly apply and resolve all ELF i386 relocations, especially those critical for PIC (`R_386_GOT32`, `R_386_PLT32`, `R_386_GOTOFF`, `R_386_RELATIVE`, etc.).

#### 2.3 User Characteristics
The primary user is a **C Developer** with:
*   Experience using command-line compiler toolchains.
*   A potential existing codebase targeting Watcom compilers.
*   A requirement to build applications or libraries for the Linux/x86 platform.
*   Familiarity with basic Linux development concepts (shared libraries, linking).

#### 2.4 Constraints
*   **Source Base:** All development must originate from the `open_watcom_devel_1.1.7` source code snapshot.
*   **Backward Compatibility:** Changes must not break the existing functionality for other platforms and output formats (e.g., OMF for DOS/OS2, PHARLAP).
*   **Architectural Integrity:** Modifications must fit within the existing architecture of the affected components (ORL, WLCore, GC386, OWL). A wholesale rewrite is not permitted.
*   **Foundation Bugs:** The implementation depends on first fixing identified bugs in the existing ELF handling code (e.g., incorrect `R_386_PC32` offset calculation, mishandling of `STT_NOTYPE` symbols).

#### 2.5 Assumptions and Dependencies
*   The development and testing environment is a standard x86-based Linux distribution.
*   The system C library (`libc.so`) and dynamic linker are present and conform to the System V ABI.
*   Other Linux system shared libraries (e.g., `libm.so`) are available for linking tests.
*   The existing Open Watcom codebase for other targets is stable and serves as a valid reference for coding styles and patterns.

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 User Interfaces
*   **Command-Line Tools:**
    *   `wcc386`: Must support new command-line switches.
        *   `-elf`: Specify ELF object file output format.
        *   `-pic`: Generate Position-Independent Code.
    *   `wlink`: Must support new command-line options for ELF and shared library control.
        *   `FORMAT ELF`: Specify ELF output format.
        *   `OPTION SONAME='name'`: Set the shared object name.
        *   `LIBRARY` / `FILE` directives must correctly accept ELF `.so` files.

##### 3.1.2 Hardware Interfaces
*   The generated machine code targets the Intel 386 (i386) and compatible processor architecture.

##### 3.1.3 Software Interfaces
*   **Input:** Standard ELF32 object files (`.o`), ELF shared libraries (`.so`), and Watcom C source files (`.c`).
*   **Output:** ELF32 executables, ELF32 shared libraries, and ELF32 relocatable object files.
*   **System Runtime:** The generated executables must correctly interface with the Linux dynamic linker (`/lib/ld-linux.so.2`) for loading and resolving symbols from dependent shared libraries.

#### 3.2 Functional Requirements

##### 3.2.1 Compiler (wcc386 / GC386) Requirements
| ID    | Requirement Description                                                                                               | Priority |
| :---- | :-------------------------------------------------------------------------------------------------------------------- | :------- |
| **C.1** | The compiler shall generate standard ELF32-i386 relocatable object files (`.o`) when the `-elf` flag is specified.    | High     |
| **C.2** | The compiler shall generate Position-Independent Code (PIC) sequences for all global data and function accesses when the `-pic` flag is specified in conjunction with `-elf`. | High     |
| **C.3** | The generated PIC code shall use the standard i386 ELF ABI model for addressing, utilizing a GOT (Global Offset Table) and PLT (Procedure Linkage Table) where appropriate. | High     |
| **C.4** | The compiler shall emit the correct ELF relocation types for PIC constructs (e.g., `R_386_GOT32` for GOT references, `R_386_PLT32` for function calls via PLT). | High     |
| **C.5** | The compiler shall maintain the ability to generate OMF format object files when the `-elf` flag is not used.         | Critical |

##### 3.2.2 Linker (wlink / WLCore / OWL) Requirements
| ID    | Requirement Description                                                                                               | Priority |
| :---- | :-------------------------------------------------------------------------------------------------------------------- | :------- |
| **L.1** | The linker shall correctly read and process symbols and relocations from input ELF object files (`.o`) and shared libraries (`.so`). | High     |
| **L.2** | The linker shall produce a statically linked ELF32-i386 executable when linking ELF objects without shared library dependencies. | High     |
| **L.3** | The linker shall be able to create an ELF shared library (`.so` file) from PIC-enabled ELF object files.              | High     |
| **L.4** | The created shared library shall contain a valid `.dynamic` section, including a `DT_SONAME` tag if specified via linker command. | High     |
| **L.5** | The linker shall correctly resolve `R_386_GOT32`, `R_386_PLT32`, `R_386_GOTOFF`, `R_386_GOTPC`, `R_386_32`, `R_386_PC32`, and `R_386_RELATIVE` relocations during static and dynamic linking. | Critical |
| **L.6** | The linker shall generate the necessary dynamic linking structures (`.dynsym`, `.dynstr`, `.hash`, `.rel.dyn`, `.rel.plt`) in executables and shared libraries that have dynamic dependencies. | High     |
| **L.7** | The linker shall write an ELF interpreter path (e.g., `/lib/ld-linux.so.2`) into the executable's program header when dynamic libraries are used. | Medium   |
| **L.8** | The linker shall maintain the ability to link for other formats (OMF, etc.) when `FORMAT ELF` is not specified.       | Critical |

##### 3.2.3 Object Library (ORL/OWL) Requirements
| ID    | Requirement Description                                                                                               | Priority |
| :---- | :-------------------------------------------------------------------------------------------------------------------- | :------- |
| **O.1** | The Object Reading Library (ORL) shall correctly parse all relevant ELF section types, symbol types (`STT_FUNC`, `STT_OBJECT`, `STT_NOTYPE`), and relocation entries used in PIC. | High     |
| **O.2** | The Object Writing Library (OWL) shall be extended to write all ELF relocation types required for PIC and dynamic linking (listed in L.5). | High     |
| **O.3** | The OWL shall correctly calculate and apply addends for ELF relocations during object file generation.                | Critical |

#### 3.3 Non-Functional Requirements

##### 3.3.1 Compatibility
*   **NFR.1:** All generated ELF files (executables and shared objects) shall fully conform to the System V ABI (Intel386 Architecture Processor Supplement).
*   **NFR.2:** Generated executables shall be loadable and executable by the standard Linux dynamic linker (`/lib/ld-linux.so.2`) on contemporary x86 Linux systems.

##### 3.3.2 Correctness & Reliability
*   **NFR.3:** The linker shall correctly resolve all symbol references and relocations, producing a binary with no unresolved symbols (unless explicitly allowed) and correctly patched addresses.
*   **NFR.4:** The system shall pass a dedicated test suite designed to validate PIC code generation, shared library creation, and dynamic linking behavior.

##### 3.3.3 Maintainability
*   **NFR.5:** Code modifications shall be integrated into the existing source tree following its established patterns and conventions.
*   **NFR.6:** Platform-specific code (ELF vs. OMF) shall be clearly isolated using pre-existing abstraction mechanisms (e.g., `#ifdef _ELF`) to prevent regression on other target platforms.

##### 3.3.4 Performance
*   **NFR.7:** The compilation and linking speed for ELF targets shall be comparable to the existing OMF target performance, with the understanding that PIC code generation and dynamic linking may introduce minor overhead.

### 4. Acceptance Criteria
Acceptance of the project will be determined by the successful execution of the following verification steps:

1.  **Basic ELF Workflow:** A simple "Hello, World" C program is compiled with `wcc386 -elf` and linked with `wlink` into an ELF executable. The executable runs successfully on Linux.
2.  **PIC Compilation:** A C source file containing references to global and static data is compiled with `wcc386 -elf -pic`. Inspection of the resulting object file (e.g., via `readelf -r`) confirms the presence of correct PIC-related relocations (`R_386_GOT32`, etc.).
3.  **Shared Library Creation:** Multiple PIC object files are linked into a shared library (`libtest.so`) using `wlink`. The library file is a valid ELF shared object with a `.dynamic` section and soname.
4.  **Dynamic Linking:** An executable is linked against the created `libtest.so` and a system library (e.g., `libm.so`). The executable runs, successfully calling functions from both libraries.
5.  **Test Suite:** A comprehensive test suite executes, validating the correct handling of all ELF relocation types and edge cases related to PIC and dynamic linking. The test suite must pass with a 100% success rate for the required functionality.
6.  **Regression Test:** The existing test suites for non-ELF, non-Linux targets (e.g., OMF for DOS) continue to pass without regression, confirming platform isolation.