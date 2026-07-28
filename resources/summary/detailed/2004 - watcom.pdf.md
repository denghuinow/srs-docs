# Detailed Summary: Open Watcom Linux Port – Compiler/Linker SRS

## Background and Scope
This document outlines the requirements for porting the Open Watcom C Compiler and Linker to Linux, focusing on adding support for Position-Independent Code (PIC) and shared libraries (ELF shared objects). The goal is to enable the compiler to generate PIC and the linker to build and use shared objects, aligning with the Linux ABI. Non-goals include maintaining support for non-ELF formats (like OMF) for Linux output and extensive modifications to core code generation algorithms beyond PIC necessities.

## Stakeholders Matrix and Use Cases
*   **Compiler Developers (SciTech/Open Watcom Community):** Implement PIC generation and ELF object file output in the code generator (CG386).
*   **Linker Developers (SciTech/Open Watcom Community):** Extend the linker (wlink) to build and link against ELF shared objects.
*   **Linux System Integrators:** Ensure the produced binaries and libraries are compatible with standard Linux dynamic linking (e.g., `/lib/ld-linux.so.2`).
*   **End-User Developers:** Use `wcc386` and `wlink` to create Linux executables and shared libraries that interoperate with existing system libraries.

**Main Scenarios:**
1.  Compile a C source file to an ELF object file with PIC enabled.
2.  Link multiple ELF object files (PIC and non-PIC) into a Linux executable.
3.  Link ELF object files into a shared library (`.so` file).
4.  Link an executable against one or more existing shared libraries (`.so` files).

**Exception Scenarios:**
5.  Handle unresolved external symbols when linking against shared objects (requires PLT/GOT generation).
6.  Process ELF-specific relocation types (e.g., `R_386_GOT32`, `R_386_PLT32`) during linking.
7.  Read and parse existing ELF shared objects as linker input.
8.  Correctly map segments and sections (e.g., `.bss` alignment) for ELF executables and shared objects.

## Business Process
**Main Process: Build a Linux Shared Library**
1.  **Trigger:** User invokes `wcc386 -elf -pic -c source.c` to compile a PIC ELF object file.
2.  **Input:** C source code; **Output:** ELF relocatable object file (`.o`).
3.  **Process:** CG386 generates PIC code, uses OWL to write ELF sections, symbols, and relocations.
4.  **Trigger:** User invokes `wlink form ELF DLL libname.so ...` to link objects into a shared library.
5.  **Input:** One or more ELF object files (`.o`).
6.  **Process:** Linker (ORL/WLCore) processes objects, resolves PIC relocations, builds GOT/PLT, and creates `.dynamic` section.
7.  **Output:** ELF shared object file (`.so`) with type `ET_DYN`.
8.  **Key Branches:**
    *   **Building an Executable (non-DLL):** Process skips PT_DYNAMIC, uses PT_PHDR, and does not create `.dynamic` section.
    *   **Linking Against Shared Objects:** Linker adds `DT_NEEDED` entries and PT_INTERP header to the output executable.

## Domain Model
Key entities and their attributes:
*   **Object File (ELF):** `type` (ET_REL/ET_EXEC/ET_DYN), `sections[]` (reference), `symbols[]` (reference).
*   **Section:** `name` (required), `type` (e.g., PROGBITS, NOBITS), `flags` (e.g., ALLOC, EXECINSTR), `size`, `alignment`.
*   **Symbol:** `name` (required), `value`, `type` (e.g., STT_FUNC, STT_OBJECT), `binding` (STB_GLOBAL/STB_WEAK), `section` (reference).
*   **Relocation:** `offset` (required), `type` (e.g., R_386_32, R_386_PLT32), `symbol` (reference), `addend`.
*   **Global Offset Table (GOT):** `entries[]` (array of addresses), `_GLOBAL_OFFSET_TABLE_` symbol (required).
*   **Procedure Linkage Table (PLT):** `entries[]` (code stubs), associated with GOT entries and `R_386_JUMP_SLOT` relocations.
*   **Dynamic Section (`.dynamic`):** `tags[]` (array of `Elf32_Dyn` structures, e.g., DT_NEEDED, DT_SYMTAB).
*   **Program Header:** `type` (PT_LOAD, PT_DYNAMIC, PT_INTERP), `offset`, `vaddr`, `filesz`, `memsz`, `flags`.

## Interfaces and Integrations
*   **ORL (Object Reading Library) – Internal, Inbound:** Reads ELF/OMF/COFF object files. **Input:** Object file bytes. **Output:** Abstracted section, symbol, relocation handles. **SLA:** Must correctly map all ELF relocation types needed for PIC.
*   **OWL (Object Writing Library) – Internal, Outbound:** Writes ELF object files (used by RISC code gens, to be adopted by CG386). **Input:** Abstract code/data segments, symbols, relocations. **Output:** ELF file bytes. **SLA:** Must support all 386-specific ELF relocation types.
*   **CG386 Code Generator – Internal, Outbound:** Generates x86 machine code. **Input:** Intermediate representation (blocks/instructions). **Output:** Machine code bytes and relocation info. **SLA:** Must generate correct PIC prologue/epilogue and use EBX as GOT base.
*   **System Linker (`ld`) – External, Outbound (Testing):** Used for integration testing before `wlink` is fully functional. **Input:** ELF objects from `wcc386`. **Output:** Executable/shared library. **SLA:** Must accept Watcom-generated ELF objects without error.
*   **Linux Dynamic Linker (`ld-linux.so.2`) – External, Runtime:** Loads and links shared objects at runtime. **Input:** ELF executable with PT_INTERP and `.dynamic` section. **Output:** Running process. **SLA:** Must correctly resolve PLT/GOT entries from Watcom-generated binaries.

## Acceptance Criteria
**Capability: Generate PIC ELF Object File**
*   Given a C source file with an external function call and a global variable,
    When compiled with `wcc386 -elf -pic -c`,
    Then the output `.o` file contains `R_386_PLT32` relocation for the call and `R_386_GOT32` relocation for the variable access.
*   Given the same source file,
    When disassembled,
    Then the function prologue includes code to set up EBX as the GOT base register.

**Capability: Build a Shared Library**
*   Given multiple PIC ELF object files,
    When linked with `wlink form ELF DLL mylib.so`,
    Then the output `mylib.so` has file type `ET_DYN`, contains `.dynamic`, `.got`, and `.plt` sections, and has no PT_PHDR program header.
*   Given a shared library built with an exported function,
    When examined with `readelf -d`,
    Then the `.dynamic` section contains a `DT_SONAME` entry and any necessary `DT_NEEDED` entries.

## Non-Functional Metrics
*   **Performance:** Compiled PIC code should have comparable performance to GCC-generated PIC for similar constructs. Linking time for shared objects should scale linearly with input object count.
*   **Reliability:** The linker must not crash when processing valid ELF shared objects. The compiler must produce ELF files that are validated by `readelf` and `objdump`.
*   **Security/Compliance:** Output binaries must conform to the System V ABI (Intel386 supplement). Generated code must not introduce security vulnerabilities like incorrect relocation handling.
*   **Observability:** Compiler and linker should provide clear error messages for unsupported PIC constructs or ELF generation failures.

## Milestones and Release Strategy
1.  **M1:** CG386 can produce basic ELF object files (non-PIC) using OWL.
2.  **M2:** `wlink` can build working ELF executables (fixing existing bugs) and link simple PIC objects (using `ld` for testing).
3.  **M3:** CG386 fully implements PIC generation (prologue, data access, calls).
4.  **M4:** `wlink` can build ELF shared libraries from PIC objects.
5.  **M5:** `wlink` can create executables that dynamically link against system shared libraries (e.g., `libc.so`).
6.  **M6:** Integration testing complete; release candidate for the Open Watcom Linux port.

## Risk List and Mitigation Strategies
1.  **Risk:** Complexity of modifying CG386 for PIC/ELF is high. **Mitigation:** Prototype using OWL first, leverage existing RISC generator code (`rscobj.c`) as a reference.
2.  **Risk:** OWL lacks necessary 386-specific ELF features. **Mitigation:** Extend OWL in parallel, ensuring it meets the requirements mapped from the ABI.
3.  **Risk:** Incorrect GOT/PLT generation causes runtime crashes. **Mitigation:** Extensive testing with small test cases, comparing `objdump` output with GCC equivalents.
4.  **Risk:** Linker changes break existing OMF/COFF support. **Mitigation:** Maintain conditional compilation (`#ifdef`) and rigorous regression testing on non-ELF platforms.
5.  **Risk:** Performance overhead of PIC is significant. **Mitigation:** Profile generated code and optimize common paths; ensure optimizations are not disabled for PIC.
6.  **Risk:** The open-source codebase (`open_watcom_devel_1.1.7`) may have diverged. **Mitigation:** Work with the Open Watcom community, target a specific, stable commit or branch.
7.  **Risk:** Symbol type handling (STT_NOTYPE vs. STT_FUNC) is incorrect for dynamic linking. **Mitigation:** Implement accurate symbol type preservation from ORL through the entire link process.
8.  **Risk:** Estimation underestimates integration effort. **Mitigation:** Allocate buffer time in the schedule, especially for the final integration milestone.

## Undecided Issues and Responsible Parties
1.  **Final syntax for PIC command-line switch (`-pic` vs `-zpic`).** *Responsible: Compiler Developers.*
2.  **Handling of PDC (Position-Dependent Code) shared objects – implementation priority.** *Responsible: Linker Developers.*
3.  **Versioning strategy for the produced shared libraries (SONAME).** *Responsible: Linker Developers.*
4.  **Default behavior when targeting Linux: always generate ELF? Always require `-elf` flag?** *Responsible: Compiler Developers.*
5.  **Detailed design for mapping OMF-style fixups to OWL relocations in CG386.** *Responsible: Compiler Developers.*
6.  **Handling of TLS (Thread-Local Storage) in the Linux port (future scope).** *Responsible: TBD.*
7.  **Integration with Open Watcom's IDE/debugger for Linux.** *Responsible: TBD.*
8.  **Formal verification of ABI compliance for corner cases.** *Responsible: Quality Assurance/Developers.*