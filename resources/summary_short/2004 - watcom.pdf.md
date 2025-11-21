# Short Summary

- **Background and objectives**: This document outlines the approach for porting the Open Watcom C Compiler and Linker to Linux, focusing on adding shared library and position-independent code (PIC) support to enable Linux-compatible ELF executables and shared objects.

- **In scope**:
  - Adding PIC support to the compiler.
  - Implementing building of shared objects (both PIC and PDC).
  - Implementing use of existing shared objects.
  - Extending ORL and WLCore for ELF and PIC relocations.
  - Enhancing LoadELF for shared object creation.

- **Out of scope**:
  - Expanding on internal processes or data structures.
  - Modifying non-ELF object formats like OMF.
  - Adding non-x86 architecture support.
  - Detailed implementation of optimization stages.
  - Support for non-Linux ELF variants.

- **Roles and core use cases**:
  - As a developer, I want to compile PIC code so that it can be used in shared libraries.
  - As a developer, I want to link shared objects so that my executable can use dynamic libraries.
  - As a developer, I want to build shared libraries so that my code can be reused across applications.

- **Success metrics**:
  - Successful compilation of PIC code into ELF object files.
  - Ability to build and link shared objects using wlink.
  - Correct execution of programs using shared libraries.

- **Major constraints**:
  - Based on Open Watcom version 1.1.7; some content may become outdated.
  - Only ELF format support is targeted; OMF is not extended.
  - PIC implementation must adhere to 386 ABI specifications.
  - Limited to x86 architecture for this port.
  - Relies on existing Open Watcom structures like ORL and OWL.

- **Undecided issues**:
  - Not mentioned.
  - Not mentioned.
  - Not mentioned.
  - Not mentioned.
  - Not mentioned.