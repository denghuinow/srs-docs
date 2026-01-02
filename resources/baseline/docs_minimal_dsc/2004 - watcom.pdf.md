# Software Requirements Specification (SRS)
## Open Watcom C Compiler/Linker Linux PIC & Shared Library Port

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Approved for Development

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the port of the Open Watcom C Compiler and Linker to the Linux platform. The primary objective is to extend the existing toolchain to support the generation of Position-Independent Code (PIC), the creation of ELF shared libraries, and the linking of executables against such libraries. This document is intended for use by the development team, quality assurance, project managers, and stakeholders.

#### 1.2 Scope
The scope of this project encompasses modifications and additions to the Open Watcom C Compiler (`wcc`) and Linker (`wlink`) to achieve full compatibility with the Linux/x86 ecosystem regarding shared objects. The project includes:
*   Enhancements to the code generator for the x86 target to emit PIC-compliant assembly.
*   Modifications to the linker to understand ELF dynamic linking semantics.
*   Addition of new command-line options to control PIC/PIE and shared library generation.
*   Ensuring output conforms to the System V ABI for i386 and standard ELF formats.

**Out of Scope:**
*   Porting other Open Watcom tools (e.g., debugger, resource compiler).
*   Support for other Linux architectures (e.g., x86_64, ARM).
*   Support for C++ or other languages within the Watcom suite.
*   Creation of a package manager or distribution system for the resulting libraries.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **ABI:** Application Binary Interface
*   **ELF:** Executable and Linkable Format
*   **GOT:** Global Offset Table
*   **PIC:** Position-Independent Code
*   **PIE:** Position-Independent Executable
*   **PLT:** Procedure Linkage Table
*   **SVR4:** System V Release 4
*   **SRS:** Software Requirements Specification

#### 1.4 References
*   *System V Application Binary Interface, Edition 4.1* (1997)
*   *Tool Interface Standard (TIS) Executable and Linking Format (ELF) Specification, Version 1.2* (1995)
*   *Open Watcom Project Documentation and Source Code*
*   *Linux `ld.so` man pages*

#### 1.5 Overview
The remainder of this document details the overall description of the product (Section 2) and the specific requirements (Section 3). It provides a complete description of the features and constraints for the successful port of the Open Watcom toolchain to modern Linux shared library conventions.

---

### 2. Overall Description

#### 2.1 Product Perspective
This project is a major enhancement to the existing Open Watcom C development toolchain. The compiler and linker are currently capable of generating statically linked executables and relocatable objects for Linux/x86. This project integrates them into the standard Linux dynamic linking model, allowing them to interoperate with system libraries (e.g., `libc.so`) and user-created shared objects.

#### 2.2 Product Functions
The enhanced product shall provide the following high-level functions:
1.  **PIC Code Generation:** Translate standard C source code into x86 machine code that can be loaded at any virtual address without relocation.
2.  **Shared Object Creation:** Combine multiple PIC-compliant object files into a single ELF shared library (`.so` file).
3.  **Dynamic Executable Linking:** Combine user object files with shared libraries to produce dynamically linked executables that resolve symbols at load time or runtime.
4.  **Static Linking:** Retain all existing functionality for creating statically linked executables and relocatable archives (`.a` files).

#### 2.3 User Characteristics
The primary users are **C language developers** who:
*   Have a requirement or preference to use the Open Watcom C compiler on Linux.
*   Need to develop applications or libraries that integrate with the standard Linux dynamic linking environment.
*   Are familiar with command-line compilation and linking procedures.
*   Possess an understanding of basic linking concepts (static vs. dynamic).

#### 2.4 Constraints
1.  **Output Format Constraint:** All generated executable, shared object, and relocatable object files **must** conform to the ELF format specification as defined by the System V ABI for i386.
2.  **ABI Compliance Constraint:** The generated code and linking operations **must** adhere to the calling conventions, register usage, and stack frame layout specified in the System V ABI for i386 to ensure compatibility with system libraries and other toolchains.
3.  **Platform Constraint:** The target platform for the output is Linux running on 32-bit x86 (i386) processors.
4.  **Backward Compatibility:** The modifications shall not break existing functionality for generating static executables and libraries unless required by ABI compliance.

#### 2.5 Assumptions and Dependencies
*   It is assumed the host build environment is a modern Linux system with necessary development tools.
*   The project depends on the existing Open Watcom codebase being in a compilable and stable state.
*   Successful operation depends on the host system's dynamic linker (`ld.so`) conforming to the SVR4 ABI.

---

### 3. Specific Requirements

#### 3.1 External Interface Requirements

##### 3.1.1 User Interfaces
*   **Command-Line Arguments:**
    *   Compiler (`wcc`):
        *   `-fpic` / `-fPIC`: Generate Position-Independent Code.
        *   `-shared`: Imply `-fPIC` and signal intent to produce a shared object (may affect code generation).
    *   Linker (`wlink`):
        *   `-shared`: Produce a shared object (`.so`) instead of an executable.
        *   `-soname <name>`: Set the internal `DT_SONAME` field of the shared object.
        *   `-Bdynamic` / `-Bstatic`: Specify dynamic or static linking for subsequent libraries (default: `-Bdynamic`).
        *   `-L<path>`: Add directory to library search path.
        *   `-l<name>`: Link against library `lib<name>.so` or `lib<name>.a`.
        *   `-e <entry>`: Set the entry point address (for executables).
        *   `-o <file>`: Set the output file name.

##### 3.1.2 Hardware Interfaces
*   The generated machine code must target the i386 ISA and be compatible with x86 processors supporting this ISA.

##### 3.1.3 Software Interfaces
*   **Input:** Standard C source files (`.c`), preprocessed source files, Watcom/ELF object files (`.o`), static libraries (`.a`), and shared libraries (`.so`).
*   **Output:** ELF format files: Relocatable objects (`.o`), Shared Objects (`.so`), and Executables (no extension, or user-specified).
*   **System Interaction:** The generated executables must correctly interface with the Linux kernel via system calls and with the runtime dynamic linker (`/lib/ld-linux.so.2`).

##### 3.1.4 Communications Interfaces
None.

#### 3.2 Functional Requirements

##### 3.2.1 Compiler (`wcc`) Requirements
*   **FR.1 PIC Code Generation:**
    *   **FR.1.1** When `-fpic` or `-fPIC` is specified, the compiler shall generate code that uses the Global Offset Table (GOT) and Procedure Linkage Table (PLT) mechanisms for all external data and function accesses.
    *   **FR.1.2** The compiler shall generate the `@GOT` and `@GOTOFF` relocations for absolute and relative data accesses, respectively.
    *   **FR.1.3** The compiler shall generate the `@PLT` relocation for function calls to external symbols.
    *   **FR.1.4** The prologue of PIC functions shall load the address of the GOT into a designated register (typically `%ebx`) as per i386 PIC ABI.

*   **FR.2 Object File Output:**
    *   **FR.2.1** The compiler shall always produce standard ELF relocatable object files (`.o`) for the i386 target.
    *   **FR.2.2** The object file shall contain the appropriate section headers (`.text`, `.data`, `.bss`, `.rodata`, `.rel.text`, `.rel.data`, etc.).
    *   **FR.2.3** Symbol tables shall be correctly populated with binding (`LOCAL`, `GLOBAL`) and type (`FUNC`, `OBJECT`) information.

##### 3.2.2 Linker (`wlink`) Requirements
*   **FR.3 Shared Object Creation:**
    *   **FR.3.1** When the `-shared` option is specified, the linker shall produce an ELF shared object file (`.so`).
    *   **FR.3.2** The output shall include a dynamic section (`.dynamic`) containing tags such as `DT_SONAME`, `DT_NEEDED`, `DT_SYMTAB`, `DT_STRTAB`, `DT_HASH`, etc.
    *   **FR.3.3** The linker shall create a GOT (`.got`) and a PLT (`.plt`) section if required by the input objects.
    *   **FR.3.4** The linker shall apply all necessary relocations, resolving internal symbols and setting up GOT/PLT entries for external symbols.
    *   **FR.3.5** The linker shall set the ELF file type to `ET_DYN`.

*   **FR.4 Dynamic Executable Linking:**
    *   **FR.4.1** The linker shall be able to accept shared libraries (`.so` files) specified with the `-l` option.
    *   **FR.4.2** It shall read the dynamic symbol tables from shared libraries to resolve undefined references in the input objects.
    *   **FR.4.3** The linker shall produce an executable of type `ET_EXEC` (or `ET_DYN` for PIE, a future consideration).
    *   **FR.4.4** The executable shall contain an `INTERP` program header pointing to the system dynamic linker (e.g., `/lib/ld-linux.so.2`).
    *   **FR.4.5** It shall populate the `.dynamic` section of the executable with `DT_NEEDED` entries for all linked shared libraries.

*   **FR.5 Static Linking:**
    *   **FR.5.1** All existing static linking capabilities must be preserved.
    *   **FR.5.2** The linker shall correctly process static libraries (`.a` files) when `-Bstatic` is in effect.

#### 3.3 Non-Functional Requirements

##### 3.3.1 Performance Requirements
*   **NF.1** The performance of PIC code generated by the compiler should be within the typical overhead range (5-15%) expected for i386 PIC versus non-PIC code.
*   **NF.2** Linking time for dynamic executables should be comparable to other native linkers (e.g., GNU `ld`) for projects of similar size.

##### 3.3.2 Reliability & Compatibility Requirements
*   **NF.3** The generated shared libraries and executables must be loadable and executable by the standard Linux dynamic linker.
*   **NF.4** The tools must be able to link against system shared libraries (e.g., `libc.so`, `libm.so`).
*   **NF.5** The output files must be inspectable and understandable by standard Linux tools (e.g., `readelf`, `objdump`, `ldd`).

##### 3.3.3 Portability & Maintainability Requirements
*   **NF.6** The new code for PIC generation and ELF dynamic linking shall be modular and well-documented within the existing Open Watcom source structure.
*   **NF.7** The implementation shall avoid unnecessary divergence from the standard i386/ELF ABI to facilitate future maintenance and potential ports to other ELF-based platforms.

#### 3.4 System Features
Not applicable for this toolchain project.

#### 3.5 Compliance Requirements
The system **shall** demonstrably comply with the System V ABI for i386, Chapter 4 (Object Files) and Chapter 5 (Program Loading and Dynamic Linking), as referenced in Section 1.4.

---
**Document Approval:**

*   Project Lead: ________________________ Date: ________
*   Lead Developer: ________________________ Date: ________
*   QA Lead: ________________________ Date: ________