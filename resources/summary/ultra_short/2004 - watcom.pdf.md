**Purpose & Scope**
The system is a port of the Open Watcom C Compiler and Linker to the Linux platform. Its core purpose is to add support for generating and using Position-Independent Code (PIC) and shared libraries (ELF shared objects). It does not involve creating a new object file format or a completely new code generator from scratch.

**Product Background / Positioning**
This is an enhancement to the existing Open Watcom open-source compiler suite. The port integrates the compiler and linker into the Linux ecosystem, enabling them to produce and consume standard ELF binaries that are compatible with the Linux ABI and dynamic linker. It builds upon the existing codebase, specifically the ORL (Object Reading Library), WLCore (linker core), GC386 (x86 code generator), and OWL (Object Writing Library) components.

**Core Functional Overview**
1.  Generate Position-Independent Code (PIC) for x86/ELF.
2.  Produce ELF format object files from the C compiler (wcc386).
3.  Build ELF shared libraries (DLLs) using the linker (wlink).
4.  Link executables that can use pre-existing ELF shared libraries.
5.  Correctly process ELF-specific relocation types required for PIC and dynamic linking (e.g., R_386_GOT32, R_386_PLT32).

**Key Users & Usage Scenarios**
Primary users are C developers on Linux who require a Watcom-compatible toolchain. A typical scenario involves a developer using `wcc386` with new command-line switches (`-elf`, `-pic`) to compile a C source file into an ELF/PIC object file, then using `wlink` to link multiple such objects into either a Linux executable or a shared library.

**Major External Interfaces**
The system interfaces through command-line tools (`wcc386`, `wlink`). It must read and write standard ELF object files and shared libraries. It must interface correctly with the Linux dynamic linker (`/lib/ld-linux.so.2`) for executables using shared libraries.

**Key Non-functional Requirements**
*   **Compatibility:** Generated ELF files (executables, shared objects) must conform to the System V ABI (Intel386 supplement) and be loadable by the standard Linux dynamic linker.
*   **Correctness:** The linker must correctly resolve all specified ELF relocation types for both static and dynamic linking.
*   **Maintainability:** Changes should integrate with the existing Open Watcom source structure (e.g., ORL, WLCore, GC386) without breaking other platforms (e.g., OMF output for Windows).

**Constraints, Assumptions & Dependencies**
*   The implementation is based on the `open_watcom_devel_1.1.7` source base.
*   The existing OMF object file output from the code generator is a constraint; ELF output must be added alongside it.
*   The Object Writing Library (OWL) exists but lacks full support for 386 ELF relocations and needs extension.
*   Several bugs in the existing ELF handling within the linker (e.g., R_386_PC32 relocation offset, STT_NOTYPE symbol handling) must be fixed as a foundation.

**Priorities & Acceptance Approach**
The highest priority is enabling the basic workflow: compiling to ELF and linking a working Linux executable. The next priority is PIC/shared library support. Acceptance will be determined by the successful compilation and linking of test programs that use PIC and shared libraries, resulting in binaries that execute correctly on Linux. Test suites must verify correct handling of all new ELF relocation types and dynamic linking structures.