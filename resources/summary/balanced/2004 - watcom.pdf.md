# Balanced Summary: Open Watcom Linux Port – Compiler/Linker SRS

## Goals and Scope
This document outlines the steps to port the Open Watcom C Compiler and Linker to Linux, focusing on adding support for Position-Independent Code (PIC) and shared libraries (ELF shared objects). The scope includes enhancing the compiler to generate PIC and ELF object files, and extending the linker to build and use shared objects, ensuring compatibility with the Linux ABI.

## Stakeholders and User Stories
- **Open Watcom Developers**: Responsible for implementing the port and maintaining the open-source codebase.
- **Linux Software Developers**: Use the Open Watcom tools to compile and link applications for Linux.
- **System Integrators**: Incorporate the ported tools into Linux development environments.
- **SciTech Software, Inc.**: Owns the copyright and oversees the project direction.

**User Stories:**
1. As a Linux developer, I want to compile C code with PIC support so that I can create shared libraries.
2. As a developer, I want to link ELF object files into executables using wlink so that I have a complete toolchain.
3. As a developer, I want to build shared objects from PIC code so that my libraries are position-independent.
4. As a developer, I want to link against existing shared libraries so that I can use system libraries.
5. As a developer, I want the compiler to output ELF format object files so that they are compatible with Linux tools.
6. As a maintainer, I want the changes to integrate smoothly with existing code so that the port is maintainable.

## Key Processes
1. **PIC Generation in Compiler** (Trigger: `-pic` switch): The compiler generates position-independent code by reserving EBX as the GOT base register and adding prologue/epilogue sequences.
2. **ELF Object File Output** (Trigger: `-elf` switch): The code generator (CG386) writes object files in ELF format using the Object Writing Library (OWL).
3. **Shared Object Building in Linker** (Trigger: `form ELF DLL`): The linker creates ELF shared objects with dynamic sections, GOT, and PLT.
4. **Dynamic Symbol Processing** (Trigger: Linking with shared objects): The linker reads shared objects via ORL and handles dynamic symbols and relocations.
5. **GOT/PLT Construction** (Trigger: Encountering PIC relocations): The linker builds Global Offset Table and Procedure Linkage Table entries for PIC.
6. **Program Interpreter Addition** (Trigger: Linking with shared libraries): The linker adds a PT_INTERP segment for dynamic linking.
7. **Final ELF File Generation** (Trigger: Linking completion): The linker writes the complete ELF executable or shared object with headers and sections.

## Domain Data Elements
- **Object File (ELF)**: Primary key: section index; fields: type, flags, address, offset, size.
- **Symbol**: Primary key: name; fields: value, type, binding, section, size.
- **Relocation**: Primary key: offset; fields: type, symbol, addend.
- **Segment (Program Header)**: Primary key: type; fields: offset, virtual address, file size, memory size, flags.
- **Global Offset Table (GOT)**: Primary key: entry index; fields: address, symbol reference.
- **Procedure Linkage Table (PLT)**: Primary key: entry index; fields: code sequence, GOT offset.

## Non-Functional Requirements
1. **Compatibility**: Output must adhere to the System V ABI for i386 and Linux Standard Base.
2. **Performance**: Code generation and linking should not introduce significant overhead.
3. **Maintainability**: Changes should integrate with existing Open Watcom code structure.
4. **Testability**: The implementation must be verifiable with standard Linux tools (readelf, objdump).
5. **Documentation**: Code changes should be documented for future maintenance.
6. **Open Source Compliance**: The port must align with the open-source nature of Open Watcom.

## Milestones and External Dependencies
1. **PIC Support in Compiler**: Depends on extending OWL and CG386.
2. **ELF Output from Compiler**: Depends on OWL enhancements.
3. **Shared Object Building in Linker**: Depends on ORL and LoadELF improvements.
4. **Using Shared Objects**: Depends on ORL fixes for reading shared libraries.
5. **Final Integration Testing**: Requires complete toolchain and test suites.

## Risks and Mitigation Strategies
1. **Complexity of CG386 Modifications**: Mitigation: Incremental development and reference to RISC code generators.
2. **ABI Compliance Risks**: Mitigation: Extensive testing with ABI documentation and Linux tools.
3. **Integration Issues with Existing Code**: Mitigation: Careful code reviews and adherence to existing patterns.
4. **Performance Degradation**: Mitigation: Benchmarking and optimization passes.
5. **Incomplete OWL Support**: Mitigation: Extend OWL as needed, leveraging existing ELF knowledge.

## Undecided Issues
1. Exact command-line switches for PIC and ELF in wcc386 (e.g., `-pic` vs `-zpic`).
2. Handling of STT_NOTYPE symbols in dynamic linking context.
3. Optimal segment mapping for .bss in shared objects.
4. Support for PDC shared objects versus PIC-only focus.
5. Extent of OWL enhancements required for full 386 ABI support.
6. Versioning and compatibility with future Open Watcom releases.