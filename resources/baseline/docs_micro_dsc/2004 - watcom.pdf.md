# Software Requirements Specification (SRS)
## Open Watcom C Compiler & Linker Port to Linux with PIC/Shared Library Support

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the porting of the Open Watcom C compiler (`wcc`) and linker (`wlink`) to the Linux operating system. The primary objective is to extend the toolchain to support the generation of Position-Independent Code (PIC) and the creation and linking of ELF-format shared libraries, enabling the development of modern, shared-library-based applications on Linux/x86.

#### 1.2 Scope
This project encompasses modifications to the Open Watcom C compiler's code generation backend and the linker's object file processing and output modules. The scope is limited to:
*   The Intel x86 (i386) architecture target.
*   The Linux operating system (generic glibc-based environment).
*   Adding support for the ELF object file format alongside the existing OMF format.
*   Implementing PIC generation and dynamic linking semantics as defined by the System V i386 ABI.

**Out of Scope:**
*   Support for other architectures (e.g., x86_64, ARM).
*   Porting other Open Watcom tools (e.g., debugger, resource compiler).
*   Modifications to the compiler's front-end (parser, optimizer) or linker's core resolution algorithms beyond ELF/PIC-specific logic.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **ABI:** Application Binary Interface
*   **ELF:** Executable and Linkable Format
*   **GOT:** Global Offset Table
*   **OMF:** Object Module Format (the existing format used by Open Watcom)
*   **PIC:** Position-Independent Code
*   **PLT:** Procedure Linkage Table
*   **SRS:** Software Requirements Specification

#### 1.4 References
*   *System V Application Binary Interface, Intel386 Architecture Processor Supplement, Fourth Edition.*
*   *Open Watcom C/C++/Fortran Compiler and Tools Source Code.*
*   *ELF-64 Object File Format Specification.*

#### 1.5 Overview
The remainder of this document details the overall description of the product (Section 2) and the specific requirements (Section 3). It is structured to provide a clear, actionable specification for software developers implementing the port.

### 2. Overall Description

#### 2.1 Product Perspective
The modified Open Watcom toolchain is a component within a larger software development ecosystem for Linux. It must interoperate with existing system tools (e.g., `ld.so` dynamic linker, `ar`, `objdump`) by producing compliant ELF binaries. It will exist as a replacement or alternative to existing toolchains like GCC and Clang for users requiring the specific characteristics of the Open Watcom compiler.

#### 2.2 Product Functions
The high-level functions of the enhanced product are:
1.  **Compile C source code** into ELF-format object files containing PIC.
2.  **Link multiple ELF object files** into a statically linked ELF executable.
3.  **Link multiple ELF object files** into a dynamically linked ELF shared object (`.so` file).
4.  **Link an executable** against pre-existing ELF shared objects, resolving symbols dynamically at runtime.

#### 2.3 User Characteristics
The intended users are experienced C developers and system programmers who:
*   Have a need or preference for the Open Watcom compiler on the Linux platform.
*   Understand the concepts of static vs. dynamic linking and library management.
*   Are familiar with command-line compiler and linker tools.

#### 2.4 Constraints
1.  **ABI Compliance:** All output must strictly comply with the *System V i386 ABI* for ELF structure, PIC implementation, and dynamic linking rules.
2.  **Backward Compatibility:** The modifications must not break the existing functionality of the compiler and linker for generating OMF-format files (e.g., for DOS/16-bit targets). The new ELF/PIC features are additive.
3.  **Source Code Integrity:** Changes should integrate with the existing Open Watcom codebase architecture, following its conventions and patterns.

#### 2.5 Assumptions and Dependencies
*   The development and target environment is a standard Linux distribution with standard system headers and libraries (glibc) installed.
*   The project assumes the availability of the complete Open Watcom source code.
*   Successful operation depends on the host system's dynamic linker (`ld-linux.so.2`) conforming to the same ABI.

### 3. Specific Requirements

#### 3.1 External Interface Requirements
**3.1.1 User Interfaces**
*   **Command-Line Arguments:** New flags must be added.
    *   Compiler (`wcc`): `-fpic` or `-fPIC` to enable PIC generation.
    *   Linker (`wlink`): `-shared` to produce a shared object. `-soname <name>` to set the shared object's internal name.
*   **Output Formats:** The linker must support a new `FORMAT` directive (e.g., `FORMAT ELF`) or equivalent command-line option to specify ELF output.

**3.1.2 Software Interfaces**
*   The compiler must generate ELF object files (`.o`) that are compatible with the GNU `binutils` tools (`objdump`, `readelf`, `ld`).
*   The linker must produce executables and shared libraries that are loadable by the Linux kernel and linkable by `/lib/ld-linux.so.2`.

#### 3.2 Functional Requirements

**3.2.1 Compiler (wcc) - Code Generation**
*   **FR-CG-1:** When the PIC flag (`-fpic`) is specified, the compiler's code generator shall produce position-independent machine code for the i386 architecture.
*   **FR-CG-2:** The compiler shall generate accesses to global data via the GOT.
    *   *Detail:* This requires replacing direct memory addresses with calculated addresses using a dedicated register (typically `%ebx`) pointing to the GOT.
*   **FR-CG-3:** The compiler shall generate calls to external functions via the PLT.
*   **FR-CG-4:** The compiler shall emit ELF-specific relocation types for PIC constructs, including but not limited to:
    *   `R_386_GOT32`
    *   `R_386_GOTOFF`
    *   `R_386_PLT32`
    *   `R_386_GLOB_DAT`
    *   `R_386_RELATIVE`
*   **FR-CG-5:** The compiler's object file writer module shall be extended to output files in the ELF32 format (in addition to OMF), including proper section headers (`.text`, `.data`, `.bss`, `.rodata`), symbol tables (`.symtab`, `.dynsym`), and relocation sections (`.rel.text`, `.rel.data`).

**3.2.2 Linker (wlink) - Object File Processing**
*   **FR-LD-1:** The linker shall be able to read and parse input object files in both OMF and ELF32 formats.
*   **FR-LD-2:** The linker shall correctly interpret and process all ELF relocation types listed in FR-CG-4.

**3.2.3 Linker (wlink) - Output Generation**
*   **FR-OG-1:** When the `-shared` option is specified, the linker shall produce an ELF shared object file (ET_DYN).
    *   *Detail:* The output must include a dynamic section (`.dynamic`), a dynamic symbol table (`.dynsym`), and necessary dynamic relocations (`.rel.dyn`, `.rel.plt`).
*   **FR-OG-2:** The linker shall be able to produce statically linked ELF executables (ET_EXEC).
*   **FR-OG-3:** The linker shall be able to produce dynamically linked ELF executables (ET_EXEC) that depend on shared objects.
    *   *Detail:* This requires generating a program header table (`PT_LOAD`, `PT_DYNAMIC`, `PT_INTERP`) and setting the correct interpreter path (e.g., `/lib/ld-linux.so.2`).
*   **FR-OG-4:** The linker shall resolve references from the executable to symbols defined in shared objects by setting up the required PLT and GOT entries in the output file.
*   **FR-OG-5:** The linker shall support the `-soname` option to embed a `DT_SONAME` entry in the dynamic section of a shared object.

#### 3.3 Non-Functional Requirements

**3.3.1 Performance**
*   **NF-PERF-1:** The runtime performance of generated PIC code should be within the typical overhead expectations for i386 PIC (e.g., extra indirection for global data/calls). No undue performance regression versus non-PIC code generation should be introduced in the compiler itself.

**3.3.2 Reliability**
*   **NF-REL-1:** The toolchain must not produce corrupt ELF files that crash the system linker (`ld`) or the dynamic loader (`ld.so`).
*   **NF-REL-2:** Generated shared libraries and executables must pass basic validation by the `readelf` and `objdump` utilities.

**3.3.3 Portability**
*   **NF-PORT-1:** The new ELF and PIC-related code should be conditionally compiled, ensuring the source base can still be built for native (non-ELF) Open Watcom targets.

**3.3.4 Compliance**
*   **NF-COMP-1:** As stated in Constraints, full compliance with the *System V i386 ABI* is a paramount requirement.

### 4. Appendices

#### 4.1 Example Usage Scenarios
```bash
# 1. Compile a source file to PIC object code
wcc -fpic -c mylib.c -o mylib.o

# 2. Create a shared library
wlink format elf shared system linux -soname libmylib.so.1 file mylib.o output libmylib.so.1.0

# 3. Compile a program using the shared library
wcc -c main.c -o main.o
# 4. Link the program against the shared library
wlink format elf system linux lib libmylib.so.1.0 file main.o output myprog
```

#### 4.2 Open Issues
*   Determination of the exact command-line syntax for new linker options (`format elf`, `system linux`) needs final alignment with existing `wlink` syntax.
*   Handling of weak symbols and versioned symbols in the dynamic symbol table may require further specification in a later revision.