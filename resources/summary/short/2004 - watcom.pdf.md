**Short Summary**

**Background and objectives**  
This document outlines the technical approach for porting the Open Watcom C compiler and linker to Linux, focusing on adding support for Position-Independent Code (PIC) and shared libraries (shared objects). The goal is to enable the compiler to generate ELF object files with PIC and allow the linker to build and use shared objects, aligning with Linux ABI standards.

**In scope**  
- Adding PIC support to the compiler (wcc386) via new command-line switches and code generation.  
- Implementing ELF object file output in the code generator (CG386) using the Object Writing Library (OWL).  
- Extending the linker (wlink) to build shared objects, including dynamic sections, GOT, and PLT.  
- Enabling the linker to read and link against existing shared objects.  
- Fixing identified bugs in the existing ELF support within the linker and ORL.

**Out of scope**  
- Porting other Open Watcom tools or utilities beyond the C compiler and linker.  
- Supporting non-ELF object formats (e.g., COFF) for Linux output.  
- Implementing PIC for architectures other than x86 (i386).  
- Adding debugger or profiling integration specific to Linux.  
- Modifying the compiler’s front-end or optimizer beyond PIC-related changes.

**Stakeholders and core use cases**  
- **Open Watcom developers**: Responsible for implementing and maintaining the port.  
- **Linux software developers**: Users who will compile and link applications with Open Watcom on Linux.  
- **System integrators**: Those incorporating Open Watcom into Linux build environments.  
- **Open-source community**: Contributors testing and providing feedback on the port.  

**User stories**  
1. As a Linux developer, I want to compile C code with PIC support so that I can create shared libraries.  
2. As a developer, I want to link multiple object files into a shared object so that I can distribute reusable code.  
3. As a user, I want to link my executable against existing shared libraries so that I can use system libraries.  
4. As a developer, I want to use Open Watcom to build ELF executables so that they run natively on Linux.  
5. As a maintainer, I want the compiler to generate standard ELF relocations so that it interoperates with other tools.  
6. As a tester, I want to verify PIC and shared object functionality so that the port meets ABI compliance.

**Success metrics**  
- The compiler successfully generates ELF object files with PIC relocations (e.g., R_386_GOT32, R_386_PLT32).  
- The linker can produce working shared objects that are loadable by the dynamic linker.  
- Executables linked with shared objects run correctly on Linux without segmentation faults.

**Major constraints**  
- Must adhere to the System V ABI for i386 architecture.  
- Changes must integrate with existing Open Watcom codebase (version 1.1.7).  
- Limited to supporting ELF format only for Linux output.  
- PIC implementation depends on extending OWL and CG386, which are complex components.  
- Time and resource limitations for testing all edge cases in dynamic linking.

**Undecided issues**  
- Final naming and handling of command-line switches for PIC and ELF modes.  
- Handling of symbol types (e.g., STT_NOTYPE) in dynamic linking contexts.  
- Optimization strategies for PIC data access in the code generator.  
- Compatibility with various Linux distributions and dynamic linkers.  
- Versioning and release integration with the main Open Watcom project.