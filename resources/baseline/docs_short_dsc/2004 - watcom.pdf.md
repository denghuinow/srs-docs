# Software Requirements Specification (SRS)
## Open Watcom C Compiler & Linker Linux Port with PIC and Shared Library Support

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the porting of the Open Watcom C compiler (`wcc386`) and linker (`wlink`) to the Linux operating system. The primary focus is to add support for generating Position-Independent Code (PIC) and creating/linking against ELF shared libraries (shared objects), ensuring compliance with the System V Application Binary Interface (ABI) for the i386 architecture.

#### 1.2 Document Conventions
*   **Bold text** is used for emphasis.
*   `Monospaced text` denotes filenames, commands, code, or technical terms.
*   Requirements are uniquely identified as **FR** (Functional Requirement) or **NFR** (Non-Functional Requirement).

#### 1.3 Project Scope
This project encompasses modifications to the Open Watcom toolchain (version 1.1.7) to enable native Linux development. The core deliverables are a compiler capable of generating PIC-enabled ELF object files and a linker capable of producing and consuming ELF shared objects.

##### 1.3.1 In Scope
*   Enhancement of the `wcc386` compiler to support PIC code generation via new command-line switches.
*   Implementation of ELF object file output within the Code Generator (`CG386`) utilizing the Object Writing Library (`OWL`).
*   Extension of the `wlink` linker to build ELF shared objects, including necessary dynamic sections (`.dynamic`), Global Offset Table (GOT), and Procedure Linkage Table (PLT).
*   Enhancement of `wlink` to read and resolve symbols from existing system and user-provided shared objects (`.so` files).
*   Correction of identified defects in the existing ELF support within the linker and the Object Reading Library (`ORL`).

##### 1.3.2 Out of Scope
*   Porting of other Open Watcom utilities (e.g., debugger, resource compiler, IDE).
*   Support for non-ELF object file formats (e.g., COFF, OMF) for Linux targets.
*   Implementation of PIC for non-x86 architectures (e.g., x86_64, ARM).
*   Integration with Linux-specific debuggers (e.g., GDB) or profilers.
*   Modifications to the compiler front-end (parser, preprocessor) or optimizer logic unrelated to PIC mechanics.

#### 1.4 References
*   *System V Application Binary Interface, Edition 4.1* (1997)
*   *Tool Interface Standard (TIS) Executable and Linking Format (ELF) Specification, Version 1.2*
*   Open Watcom Project Source Code (Version 1.1.7)

### 2. Overall Description

#### 2.1 Product Perspective
This project is a major enhancement to the existing Open Watcom toolchain, integrating it into the modern Linux build ecosystem. It modifies core components (`CG386`, `OWL`, `wlink`, `ORL`) to interact correctly with the Linux ELF runtime environment.

#### 2.2 User Classes and Characteristics
*   **Open Watcom Developers:** Engineers implementing the changes. They require detailed knowledge of the existing codebase, ELF format, and the i386 ABI.
*   **Linux Software Developers:** End-users who will employ Open Watcom to build applications and libraries. They expect command-line switches and behavior consistent with GCC/clang for PIC and shared library operations.
*   **System Integrators:** Individuals incorporating the ported Open Watcom tools into cross-compilation environments, build scripts, or CI/CD pipelines.
*   **Open-Source Community:** Contributors and testers who will validate the port's functionality and ABI compliance.

#### 2.3 Operating Environment
*   **Target Platform:** Linux (kernel 2.6.32 or later, glibc 2.11 or later)
*   **Target Architecture:** Intel 32-bit (i386)
*   **Output Format:** ELF32
*   **Host Platform for Development:** Linux or a compatible environment capable of building Open Watcom.

#### 2.4 Design and Implementation Constraints
1.  **NFR-CON-1:** All generated code and object files must adhere to the System V ABI for i386.
2.  **NFR-CON-2:** Modifications must integrate seamlessly with the existing Open Watcom 1.1.7 codebase structure and build system.
3.  **NFR-CON-3:** The compiler and linker must output ELF format exclusively when targeting Linux.
4.  **NFR-CON-4:** PIC implementation is constrained by the existing architectures of `CG386` and `OWL`.
5.  **NFR-CON-5:** Project timelines limit exhaustive testing of all dynamic linking edge cases.

#### 2.5 Assumptions and Dependencies
*   The Linux dynamic linker (`ld-linux.so.2`) implements the standard ELF dynamic linking semantics.
*   The existing Open Watcom code generator and object file libraries can be extended without a full rewrite.
*   Necessary build tools (e.g., `make`, `gcc` for bootstrapping) are available in the development environment.

### 3. System Features and Requirements

#### 3.1 Feature: PIC Code Generation in Compiler
**Description:** The `wcc386` compiler shall be extended to generate Position-Independent Code suitable for inclusion in shared libraries.

**User Stories Addressed:** 1, 5

**Requirements:**
*   **FR-COMP-1:** The compiler shall accept a new command-line switch (e.g., `-fpic` or `-fPIC`) to enable PIC code generation mode.
*   **FR-COMP-2:** When PIC mode is enabled, the compiler shall generate code that accesses global data indirectly via the Global Offset Table (GOT).
*   **FR-COMP-3:** When PIC mode is enabled, the compiler shall generate function calls that use the Procedure Linkage Table (PLT) for external functions.
*   **FR-COMP-4:** The code generator (`CG386`) shall produce the standard ELF relocations for PIC, including but not limited to:
    *   `R_386_GOT32`
    *   `R_386_GOTOFF`
    *   `R_386_GOTPC`
    *   `R_386_PLT32`
*   **FR-COMP-5:** The compiler shall write object files in ELF32 format using the Object Writing Library (`OWL`), which must be extended to support necessary PIC-related sections and relocations.

#### 3.2 Feature: Shared Object Creation in Linker
**Description:** The `wlink` linker shall be able to combine object files into a valid ELF shared library (`.so` file).

**User Stories Addressed:** 2

**Requirements:**
*   **FR-LINK-1:** The linker shall accept a command-line option (e.g., `-shared`) to specify the output target is a shared object.
*   **FR-LINK-2:** When building a shared object, the linker shall create and populate all required dynamic linking sections (e.g., `.dynamic`, `.dynsym`, `.dynstr`, `.hash` or `.gnu.hash`).
*   **FR-LINK-3:** The linker shall construct a Global Offset Table (`.got`) and a Procedure Linkage Table (`.plt`) in the output shared object.
*   **FR-LINK-4:** The linker shall generate correct dynamic relocations (e.g., `R_386_JMP_SLOT`, `R_386_GLOB_DAT`) in the `.rel.dyn` and `.rel.plt` sections.
*   **FR-LINK-5:** The linker shall define the `SONAME` and needed library dependencies (`DT_NEEDED`) in the `.dynamic` section based on input and command-line arguments.

#### 3.3 Feature: Linking Against Shared Objects
**Description:** The `wlink` linker shall be able to resolve undefined symbols from pre-existing ELF shared libraries.

**User Stories Addressed:** 3, 4

**Requirements:**
*   **FR-LINK-6:** The linker shall accept command-line arguments (e.g., `-l<name>` and `-L<path>`) to specify shared libraries for input.
*   **FR-LINK-7:** The linker shall read and parse ELF shared objects using the Object Reading Library (`ORL`), which must be fixed/extended to correctly handle dynamic symbols and sections.
*   **FR-LINK-8:** The linker shall be able to produce an executable that has a `PT_INTERP` program header pointing to the dynamic linker (e.g., `/lib/ld-linux.so.2`) and a `.dynamic` section with required entries.
*   **FR-LINK-9:** The linker shall correctly resolve relative PLT/GOT offsets for calls to functions in shared libraries.

#### 3.4 Feature: ABI Compliance and Interoperability
**Description:** The toolchain's output must be compatible with standard Linux system tools and the runtime environment.

**User Stories Addressed:** 5, 6

**Requirements:**
*   **FR-ABI-1:** Generated object files must be readable and usable by standard Linux tools (e.g., `readelf`, `objdump`, `nm`).
*   **FR-ABI-2:** The linker must apply standard ELF symbol visibility and binding rules (e.g., `STB_GLOBAL`, `STB_WEAK`, `STV_DEFAULT`, `STV_HIDDEN`).
*   **FR-ABI-3:** The toolchain must correctly handle standard system startup files (e.g., `crt1.o`, `crti.o`, `crtn.o`) when linking executables.

### 4. External Interface Requirements

#### 4.1 User Interfaces
*   **Command-Line Interface:** All new functionality shall be exposed via command-line switches to `wcc386` and `wlink`. The syntax should follow common conventions (e.g., `-fpic`, `-shared`, `-soname=<name>`).

#### 4.2 Software Interfaces
*   **Object File Format:** ELF32 for i386.
*   **Dynamic Linker:** Interface with `/lib/ld-linux.so.2` as defined by the System V ABI.
*   **System Libraries:** Ability to link against `libc.so`, `libm.so`, and other standard `.so` libraries.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   **NFR-PER-1:** Code generated with PIC enabled shall have runtime performance characteristics consistent with other i386 PIC implementations (e.g., GCC's `-fPIC`). Minor overhead for GOT/PLT access is acceptable.

#### 5.2 Safety & Security Requirements
*   **NFR-SEC-1:** The linker shall not create shared objects or executables with invalid ELF structures that could crash the dynamic linker or cause system instability.

#### 5.3 Quality Requirements
*   **NFR-QUAL-1:** The success of the project shall be measured by the following metrics:
    *   Compiler successfully generates ELF object files containing standard PIC relocations.
    *   Linker produces shared objects that are loadable by the Linux dynamic linker (`ldd` does not report errors).
    *   Simple test executables, linked against both static and shared libraries, run correctly on Linux without segmentation faults or relocation errors.

### 6. Undecided Issues and Open Questions
1.  **Command-Line Syntax:** Final naming convention for PIC and ELF-mode switches (e.g., `-fpic` vs. `-qpic`, `-shared` vs. `-bd`).
2.  **Symbol Type Handling:** Strategy for setting symbol types (`STT_FUNC`, `STT_OBJECT`, `STT_NOTYPE`) in dynamic symbol tables.
3.  **PIC Optimizations:** Whether to implement PIC-specific optimizations in the code generator (e.g., relaxing GOT accesses for local symbols).
4.  **Compatibility Testing:** The specific set of Linux distributions and glibc versions to be officially validated.
5.  **Project Integration:** The process for merging changes into the upstream Open Watcom project repository and versioning of the release.

---
*This document is subject to change upon further analysis and stakeholder feedback.*