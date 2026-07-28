# Software Requirements Specification (SRS)
## Open Watcom C Compiler and Linker Linux Port with PIC and Shared Library Support

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review
**Project:** Open Watcom Linux Port
**Authors:** Open Watcom Development Team

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for porting the Open Watcom C Compiler (`wcc386`) and Linker (`wlink`) to the Linux operating system. The primary focus is to add support for generating Position-Independent Code (PIC) and handling Executable and Linkable Format (ELF) shared objects, thereby creating a complete, ABI-compliant toolchain for Linux/i386 development.

#### 1.2 Scope
The scope of this project encompasses modifications to the following core components of the Open Watcom toolchain:
*   **Open Watcom C Compiler (`wcc386`):** Enhancements to generate PIC and to output object files in ELF format.
*   **Code Generator (`CG386`):** Modifications for PIC-aware code generation and interfacing with the enhanced Object Writing Library.
*   **Object Writing Library (`OWL`):** Extensions to support writing full ELF object files, including necessary headers, sections, and PIC-specific relocations.
*   **Open Watcom Linker (`wlink`):** Extensions to build ELF shared objects (libraries), to link against existing system shared libraries, and to generate ELF executables with dynamic linking segments.
*   **Object Reading Library (`ORL`):** Fixes and enhancements to correctly parse and interpret existing Linux ELF shared libraries and object files.

Out of scope are:
*   Porting other Open Watcom compilers (e.g., Fortran, C++).
*   Modifications to the Open Watcom IDE or debugger.
*   Support for operating systems other than Linux.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **ABI:** Application Binary Interface.
*   **CG:** Code Generator.
*   **DLL:** Dynamic Link Library (used interchangeably with Shared Object in this context).
*   **ELF:** Executable and Linkable Format.
*   **GOT:** Global Offset Table.
*   **LSB:** Linux Standard Base.
*   **ORL:** Object Reading Library.
*   **OWL:** Object Writing Library.
*   **PDC:** Position-Dependent Code.
*   **PIC:** Position-Independent Code.
*   **PLT:** Procedure Linkage Table.
*   **SRS:** Software Requirements Specification.

#### 1.4 References
*   System V Application Binary Interface, Edition 4.1 (1997).
*   Linux Standard Base (LSB) Specification.
*   ELF-64 Object File Format Specification.
*   Open Watcom Source Code and Internal Documentation.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its stakeholders, and operating environment. Section 3 details the specific functional requirements. Section 4 outlines non-functional requirements. Appendices may contain supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
This project is a major enhancement to the existing Open Watcom toolchain, which historically targeted DOS, OS/2, and Windows. The port integrates the toolchain into the Linux ecosystem, requiring adherence to the Linux/ELF conventions and the System V i386 ABI. It interacts with the host Linux system's dynamic linker (`ld-linux.so`) and existing system libraries.

#### 2.2 Stakeholders and User Classes
| Stakeholder / User Class | Primary Interest / Responsibility |
| :--- | :--- |
| **Open Watcom Developers** | Implement, test, and maintain the ported code within the open-source repository. |
| **Linux Software Developers** | Use `wcc386` and `wlink` as a primary toolchain for building applications and libraries for Linux. |
| **System Integrators** | Package and distribute the Open Watcom tools for various Linux distributions. |
| **SciTech Software, Inc.** | Hold copyright, provide project oversight, and manage official releases. |

#### 2.3 User Stories
1.  As a Linux developer, I want to compile C code with PIC support so that I can create shared libraries.
2.  As a developer, I want the compiler to output object files in ELF format so that they are compatible with standard Linux tools (e.g., `ld`, `objdump`, `readelf`).
3.  As a developer, I want to link multiple ELF object files into a Linux executable using `wlink` so that I have a complete, usable toolchain.
4.  As a developer, I want to build an ELF shared object from PIC-compliant object files using `wlink` so that my libraries are position-independent and can be loaded dynamically.
5.  As a developer, I want to link my application against existing system shared libraries (e.g., `libc.so`) using `wlink` so that I can use standard Linux APIs.
6.  As an Open Watcom maintainer, I want the architectural changes for Linux/ELF/PIC support to integrate cleanly with the existing codebase for other platforms so that the port is sustainable and maintainable.

#### 2.4 Operating Environment
*   **Host System:** Linux (32-bit i386 architecture).
*   **Target System:** Linux (32-bit i386 architecture).
*   **Dependencies:** Standard C library (`libc`), system headers, and the dynamic linker (`ld-linux.so.2`).

#### 2.5 Design and Implementation Constraints
1.  **Backward Compatibility:** Changes must not break existing functionality for other target platforms (DOS, OS/2, Windows).
2.  **Code Structure:** Enhancements must follow the existing architectural patterns of the Open Watcom compiler (`front-end` -> `CG` -> `OWL`) and linker.
3.  **Open Source License:** All new code must be compatible with the Open Watcom License.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Compiler (`wcc386`) Requirements
*   **FR-CMP-01: PIC Code Generation**
    *   **Description:** The compiler shall generate position-independent code when invoked with the PIC command-line switch.
    *   **Input:** C source files, `-pic` (or TBD) switch.
    *   **Processing:** The compiler front-end shall signal the code generator (`CG386`) to enable PIC mode. `CG386` shall:
        *   Reserve the `EBX` register as the GOT base pointer.
        *   Generate function prologues to set up `EBX` via `call/pop` sequences or equivalent.
        *   Generate memory accesses to global/static data via the GOT (`[ebx+offset]`).
        *   Generate calls to external functions via the PLT.
    *   **Output:** Intermediate code flagged for PIC relocations.

*   **FR-CMP-02: ELF Object File Output**
    *   **Description:** The compiler shall produce object files in the ELF format.
    *   **Input:** Intermediate code, `-elf` (or TBD) switch.
    *   **Processing:** The `OWL` library shall be enhanced to write all necessary ELF structures: ELF header, section headers (`.text`, `.data`, `.bss`, `.rodata`, `.rel.text`, `.rel.data`, `.symtab`, `.strtab`), and symbol tables. `CG386` shall invoke OWL's ELF writer.
    *   **Output:** A valid ELF 32-bit relocatable object file (ET_REL).

##### 3.1.2 Linker (`wlink`) Requirements
*   **FR-LNK-01: Linking ELF Executables**
    *   **Description:** The linker shall combine multiple ELF object files into a statically or dynamically linked ELF executable.
    *   **Input:** ELF object files (`.o`).
    *   **Processing:** The linker shall use `ORL` to read input objects, resolve symbols, apply relocations, and manage sections.
    *   **Output:** A valid ELF 32-bit executable file (ET_EXEC or ET_DYN).

*   **FR-LNK-02: Building ELF Shared Objects**
    *   **Description:** The linker shall create an ELF shared object (dynamic library) when the output format is specified as `FORMAT ELF DLL`.
    *   **Input:** PIC-enabled ELF object files.
    *   **Processing:** The linker shall:
        *   Create dynamic sections (`.dynamic`, `.dynsym`, `.dynstr`, `.hash`).
        *   Construct a Global Offset Table (`.got`) and a Procedure Linkage Table (`.plt`).
        *   Apply dynamic relocations (`.rel.dyn`, `.rel.plt`).
        *   Set the ELF file type to `ET_DYN` and appropriate segment flags.
    *   **Output:** A valid ELF shared object (e.g., `libfoo.so`).

*   **FR-LNK-03: Linking Against Shared Objects**
    *   **Description:** The linker shall resolve undefined symbols against symbols defined in external ELF shared libraries.
    *   **Input:** ELF object files and shared library names (e.g., `LIBRARY libc.so`).
    *   **Processing:** `ORL` shall be enhanced to read dynamic symbols from shared objects. The linker shall:
        *   Record needed libraries in the `.dynamic` section (DT_NEEDED).
        *   For function calls, create PLT entries.
        *   For data accesses, create GOT entries.
    *   **Output:** An executable or shared object with correct dynamic dependencies.

*   **FR-LNK-04: Program Interpreter Segment**
    *   **Description:** For dynamically linked executables, the linker shall add a `PT_INTERP` program header segment.
    *   **Input:** Detection of dynamic linking requirements.
    *   **Processing:** The linker shall insert a segment pointing to the path of the dynamic linker (e.g., `/lib/ld-linux.so.2`).
    *   **Output:** An ELF file with a `PT_INTERP` segment.

##### 3.1.3 Library (`ORL`/`OWL`) Requirements
*   **FR-LIB-01: ORL ELF Shared Library Reading**
    *   **Description:** The Object Reading Library (`ORL`) shall correctly parse all relevant sections and symbols from existing Linux ELF shared libraries.
    *   **Detail:** This includes reading `.dynsym`, `.dynamic`, `.rel.*`, `.got`, `.plt` sections, and handling symbol visibility (binding).

*   **FR-LIB-02: OWL ELF Writing Enhancements**
    *   **Description:** The Object Writing Library (`OWL`) shall be capable of writing all ELF structures required for PIC and shared objects.
    *   **Detail:** This includes support for writing section types and flags specific to dynamic linking (e.g., `SHT_PROGBITS`, `SHF_ALLOC`, `SHF_WRITE`, `SHF_EXECINSTR`), dynamic tags, and PIC-specific relocation types (R_386_GOT32, R_386_PLT32, R_386_GLOB_DAT, R_386_JMP_SLOT, R_386_RELATIVE).

#### 3.2 Non-Functional Requirements

*   **NFR-01: Compatibility**
    *   The generated ELF files (objects, executables, shared libraries) must fully comply with the System V i386 ABI and the Linux Standard Base (LSB). Compliance shall be verified using standard tools (`readelf`, `objdump`, `ldd`).

*   **NFR-02: Performance**
    *   The compilation and linking speed for Linux targets shall not be significantly slower (>10%) than for existing platforms (e.g., Windows) for equivalent code. PIC code generation may have a known, minor runtime overhead as per the ABI.

*   **NFR-03: Maintainability**
    *   New code shall follow the existing modular architecture. Platform-specific code shall be isolated using preprocessor directives (`#ifdef __LINUX__`) or abstracted through existing platform layers.

*   **NFR-04: Testability**
    *   The implementation shall be verifiable through a dedicated test suite, including:
        *   Compiling and linking simple "Hello World" programs.
        *   Building and using a shared library.
        *   Linking against `libc`.
        *   Comparing output with that produced by GCC/GNU `ld`.

*   **NFR-05: Documentation**
    *   All major modifications to `CG386`, `OWL`, `ORL`, and the linker must include internal code comments. Command-line options must be documented in the official `wcc386` and `wlink` documentation.

*   **NFR-06: Open Source Compliance**
    *   The development process and final code contribution shall align with the open-source collaboration model of the Open Watcom project.

### 4. Supporting Information

#### 4.1 Milestones and Dependencies
1.  **Milestone 1: PIC Support in Compiler** – *Depends on: OWL ELF write enhancements.*
2.  **Milestone 2: ELF Object File Output** – *Depends on: Completion of Milestone 1 OWL work.*
3.  **Milestone 3: Shared Object Building in Linker** – *Depends on: ORL fixes and LoadELF module enhancements.*
4.  **Milestone 4: Using Shared Objects (Linking Against)** – *Depends on: ORL fixes for reading `.dynsym`.*
5.  **Milestone 5: Final Integration & Testing** – *Depends on: All previous milestones, availability of test suites.*

#### 4.2 Risks and Mitigation
| Risk | Probability | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| Complexity of CG386 modifications for PIC | Medium | High | Incremental development. Use RISC platform PIC support in CG as a reference implementation. |
| ABI compliance issues | Medium | High | Continuous testing with `readelf` and `objdump`. Develop compliance tests against the ABI spec. |
| Integration issues with existing multi-platform code | High | Medium | Frequent code reviews. Adherence to established coding patterns and preprocessor guard conventions. |
| Performance degradation in linker | Low | Medium | Profile critical paths (symbol resolution, relocation application) and optimize. |
| Incomplete OWL support for all needed ELF features | Medium | High | Early prototyping of OWL writer. Leverage existing ELF knowledge from ORL and other parts of the codebase. |

#### 4.3 Open Issues / TBD
1.  **Command-line Syntax:** Final decision on compiler switches (`-pic` vs `-fPIC` vs `-zpic`; `-elf` vs `-target=linux-elf`).
2.  **Symbol Handling:** Policy for `STT_NOTYPE` symbols encountered during dynamic linking.
3.  **Segment Layout:** Optimal mapping of `.bss` and other special sections into program headers (segments) for shared objects.
4.  **PDC Shared Objects:** Decision on whether to support non-PIC shared objects (poor practice, but technically possible).
5.  **OWL Scope:** Final determination of the extent of enhancements required in OWL to support the full i386 Linux ABI beyond the immediate PIC needs.
6.  **Versioning:** How the Linux port will be versioned in relation to main Open Watcom releases.