# Detailed Summary

## Background and Scope
This document outlines the approach for porting the Open Watcom C Compiler and Linker to Linux, focusing on adding shared library and position-independent code (PIC) support. The scope includes implementing PIC generation in the compiler, enabling the linker to build and use shared objects, and addressing existing bugs in the ELF handling. Non-goals include maintaining compatibility with non-ELF object formats like OMF for Linux targets and extending support to non-x86 architectures.

## Role Matrix and Use Cases
- **Developer**: Implements PIC support in compiler and shared object handling in linker.
- **Tester**: Validates generated PIC code and shared object functionality.
- **Build Engineer**: Integrates changes into Open Watcom build system.
- **End User**: Compiles and links C programs with shared libraries on Linux.
- **System Integrator**: Uses wlink to create ELF executables and shared objects.
- **Debugger**: Analyzes generated ELF files for correctness.

Main scenarios: Compile C code with PIC, link into shared library, link executable using shared libraries.
Exception scenarios: Handling unresolved symbols in shared objects, processing complex relocation types.

## Business Process
**Main Process (Building Shared Object)**
1. User compiles C source with PIC switch.
2. CG386 generates ELF object with PIC relocations.
3. User invokes wlink with ELF DLL option.
4. Linker processes ELF objects and shared libraries.
5. WLCore resolves symbols and applies relocations.
6. LoadELF writes ELF headers and segments.
7. Dynamic sections and PLT/GOT are generated.
8. Final shared object file is produced.

**Key Branch (Linking Executable with Shared Objects)**
Trigger: Input includes shared library.
1. ORL reads shared object symbols.
2. Linker adds DT_NEEDED entries.
3. PLT and GOT entries are created for external functions.
4. Program interpreter segment is added.

## Domain Model
- **Object File**: format (ELF/OMF), sections, symbols, relocations.
- **Symbol**: name (required), value, type (STT_FUNC/STT_NOTYPE), binding, section (reference).
- **Relocation**: type (required), offset, symbol (reference), addend.
- **Section**: name (required), type, flags, address, size.
- **Segment**: type (PT_LOAD/PT_DYNAMIC), offset, vaddr, filesz, memsz, flags.
- **Global Offset Table**: entries (array of addresses), _GLOBAL_OFFSET_TABLE_ symbol (required).
- **Procedure Linkage Table**: entries (code sequences), associated GOT entries.
- **Dynamic Section**: tags (DT_NEEDED/DT_SYMTAB), values/pointers.

## Interfaces and Integrations
- **ORL System**: Internal, bidirectional, reads/writes object files. Input: ELF/OMF files. Output: Abstract object representation. SLA: Must handle standard ELF constructs.
- **OWL System**: Internal, output, generates ELF objects. Input: Code generator intermediate representation. Output: ELF object files. SLA: Must produce valid ELF relocations.
- **CG386 System**: Internal, bidirectional, code generation. Input: Intermediate instructions. Output: Machine code with relocations. SLA: Must implement PIC addressing modes.
- **Linux Dynamic Linker**: External, input, loads shared objects. Input: DT_NEEDED entries. Output: Runtime linking. SLA: Must follow System V ABI.

## Acceptance Criteria
- Given C source compiled with -pic, when linked as shared object, then it loads at different addresses without relocation errors.
- Given executable linking against shared library, when run, then external functions resolve through PLT.
- Given static variable in PIC code, when accessed, then uses GOT-relative addressing.

## Non-functional Metrics
- **Performance**: PIC code within 10% overhead of PDC; linking time under 30s for medium projects.
- **Reliability**: Handles standard ELF shared libraries without crashes; supports common relocation types.
- **Security**: No executable stack markings in generated code; follows Linux ABI requirements.
- **Compliance**: Conforms to System V ABI for i386; produces valid ELF files.
- **Observability**: Provides meaningful error messages for relocation failures; debug symbols preserved.

## Milestones and Release Strategy
1. Fix existing ELF bugs in linker (2 weeks)
2. Implement ELF output in CG386 (6 weeks)
3. Add PIC support to code generator (6 weeks)
4. Enable shared object building in linker (4 weeks)
5. Add shared object usage support (4 weeks)
6. Integration testing and release (2 weeks)

## Risk List and Mitigation Strategies
- **Complex PIC implementation**: Mitigation: Prototype with GNU tools first, incremental development.
- **ELF specification complexity**: Mitigation: Reference validated ELF producers like GCC.
- **Backward compatibility breaks**: Mitigation: Maintain OMF support for Windows targets.
- **Performance overhead in PIC**: Mitigation: Optimize common cases, profile early.
- **Unsupported relocation types**: Mitigation: Implement critical relocations first, fail gracefully on others.
- **Build system integration**: Mitigation: Coordinate with Open Watcom maintainers.
- **Testing coverage**: Mitigation: Create comprehensive test suite with real-world libraries.
- **Documentation gaps**: Mitigation: Annotate code with ABI references.

## Undecided Issues and Responsible Parties
- Handling of STT_NOTYPE symbols in shared objects (Linker team)
- Optimal PLT entry structure for performance (Compiler team)
- Default PIC vs PDC compilation mode (Project leads)
- Support for ELF symbol visibility attributes (Not mentioned)
- Debug information format in shared objects (Not mentioned)
- Versioning scheme for shared libraries (Not mentioned)
- Thread-local storage support (Not mentioned)
- Exception handling in PIC code (Not mentioned)