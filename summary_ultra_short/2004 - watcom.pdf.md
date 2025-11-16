# Ultra Short Summary
- Port the Open Watcom C Compiler and Linker to Linux by adding shared library and position-independent code support.

- MVP points
  - Add PIC support to the compiler, including GOT base register setup and PIC function prologues.
  - Implement ELF object file output in the code generator using OWL.
  - Extend the linker to build shared objects with dynamic sections, GOT, and PLT.
  - Enable the linker to use existing shared objects by adding program interpreter and required libraries support.

- Key constraints
  - The compiler currently only outputs OMF format, requiring ELF output implementation for PIC.
  - The linker must handle ELF-specific relocations and symbol types for dynamic linking.
  - Existing bugs in the linker must be fixed to support basic ELF executable creation.

- Major risks/undecided issues
  - Not mentioned.
  - Not mentioned.