# Balanced Summary

- **Goals and scope**: This document outlines the porting of Open Watcom Compiler and Linker to Linux, focusing on adding shared library and position-independent code support. It provides a detailed technical approach based on version open_watcom_devel_1.1.7, covering key components and implementation steps for PIC generation and shared object handling.

- **Roles and user stories**:
  - As a developer, I want to compile C code to ELF format so that I can create Linux executables.
  - As a developer, I want to generate position-independent code so that shared libraries can be loaded at different addresses.
  - As a developer, I want to build shared objects using the Open Watcom Linker so that I can create reusable Linux libraries.
  - As a developer, I want to link against existing shared objects so that my programs can use system libraries.
  - As a maintainer, I want to extend ORL and OWL components so that ELF features are fully supported.

- **Key processes**:
  1. Trigger: Compilation request; process: Parse command-line switches for ELF and PIC options.
  2. Trigger: Code generation; process: Map machine-independent instructions to x86 opcodes.
  3. Trigger: Object file output; process: Generate ELF sections and symbols using OWL.
  4. Trigger: Linking request; process: Read ELF objects via ORL and resolve relocations.
  5. Trigger: Shared object creation; process: Build dynamic sections and PLT/GOT structures.
  6. Trigger: Executable creation; process: Write ELF headers and program segments.
  7. Trigger: Integration; process: Test compiler and linker with shared library scenarios.

- **Domain data elements**:
  - **ELF Object File**: Primary key: section index; fields: type, flags, address, offset, size.
  - **Symbol**: Primary key: name; fields: value, binding, type, section handle.
  - **Relocation**: Primary key: offset; fields: type, symbol, addend.
  - **Group Entry**: Primary key: group number; fields: leaders, size, address.
  - **Instruction**: Primary key: instruction ID; fields: opcode, operands, type class.
  - **Dynamic Entry**: Primary key: tag; fields: value/pointer.

- **Non-functional requirements**:
  - Compatibility with System V ABI standards.
  - Maintainability through modular changes to CG386 and linker components.
  - Performance efficient PIC generation without significant overhead.
  - Correct handling of ELF relocations and symbol types.
  - Support for both PIC and position-dependent code (PDC).
  - Integration with existing Open Watcom build system.

- **Milestones and external dependencies**:
  - Completion of PIC support in code generator.
  - Implementation of shared object building in linker.
  - Testing with dietlibc and system libraries.
  - Dependency on System V ABI documentation.
  - Final integration of compiler and linker changes.

- **Risks and mitigation strategies**:
  - Risk: Complexity of CG386 modifications; mitigation: Incremental changes and reference to RISC implementations.
  - Risk: Incomplete ELF support in OWL; mitigation: Extend OWL with 386-specific features.
  - Risk: Symbol type handling errors; mitigation: Enhance ORL mapping for STT_FUNC and STT_NOTYPE.
  - Risk: Relocation calculation bugs; mitigation: Validate against objdump and readelf outputs.
  - Risk: Integration failures; mitigation: Comprehensive test suite with varied shared library cases.

- **Undecided issues**:
  - Command-line switch names for PIC (-pic vs. -zpic).
  - Handling of STT_NOTYPE symbols in dynamic linking.
  - Optimal GOT/PLT implementation for PDC shared objects.
  - Page alignment strategies for .bss sections.
  - Not mentioned.
  - Not mentioned.