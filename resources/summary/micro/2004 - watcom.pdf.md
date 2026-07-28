**Purpose & Scope**: Port the Open Watcom C compiler and linker to Linux by adding support for Position-Independent Code and shared libraries.

**Core Functions**:
*   Generate Position-Independent Code (PIC) for the x86 architecture.
*   Build ELF-format shared objects (libraries).
*   Link executables that use existing shared objects.

**Key Constraints**:
*   Must comply with the System V i386 ABI specification for ELF, PIC, and dynamic linking.
*   The compiler's code generator must be extended to output ELF object files, not just OMF.
*   The linker must correctly process ELF-specific relocation types (e.g., R_386_GOT32, R_386_PLT32).