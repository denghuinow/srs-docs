# Open Watcom Linux Port - Compiler/Linker Software Requirements Specification

## 1. Introduction

This document outlines the requirements for porting the Open Watcom Compiler and Linker to the Linux platform, focusing on adding Position-Independent Code (PIC) support and shared object handling capabilities. The porting effort enables Open Watcom applications to run natively on Linux while maintaining compatibility with existing Windows and OS/2 implementations.

## 2. Key Components

### 2.1 Object Reading Library (ORL)
- API for reading various object file formats (ELF, OMF, COFF)
- Maps ELF relocations to abstract ORL linking information
- Provides uniform access to object file sections and symbols
- Handles relocation type mapping (R_386_32 → ORL_RELOC_TYPE_WORD_32, R_386_PC32 → ORL_RELOC_TYPE_REL_32)

### 2.2 WLCore (Linker Core)
- Performs basic linking tasks and interacts with ORL
- Maps ORL relocations to internal representation (FIX_OFFSET_32, FIX_REL, etc.)
- Converts ELF symbols to internal symbol structures
- Calculates segment addresses during the second pass

### 2.3 LoadELF
- Writes executable files in ELF format
- Creates ELF executable files (currently does not support shared objects)
- Handles ELF header, program headers, and section headers initialization
- Writes groups, relocations, debug information, and symbol tables

### 2.4 GC386 (Code Generator)
- Generates code for 32-bit x86 processors
- Uses machine-independent intermediate format with blocks and instructions
- Supports register sets and register operations
- Currently only outputs OMF format (needs ELF support for Linux)

### 2.5 Object Writing Library (OWL)
- Designed for writing object files in ELF and COFF formats
- Provides functions for creating ELF object files (sections, symbols, relocations)
- Used by RISC code generators (Alpha AXP, PowerPC)
- Lacks complete 386 ABI support

## 3. Technical Requirements

### 3.1 Position-Independent Code (PIC) Support
**Command Line Interface:**
- Add new switches to wcc386 for ELF (-elf) and PIC (-pic or -zpic) generation
- Pass PIC flags from compiler to code generator

**ELF Object File Generation:**
- Implement ELF output in CG386 using OWL library
- Map OMF-style fixups to OWL relocations
- Extend OWL with missing 386 ABI relocation types
- Handle global offset table (GOT) base register (EBX exclusion)

**PIC Implementation:**
- Generate position-independent function prologues with GOT setup
- Implement PIC function calls using PLT (R_386_PLT32)
- Support PIC data access with GOT relocations (R_386_GOT32, R_386_GOTOFF, R_386_GOTPC)
- Optimize static variable access with GOTOFF relocations

### 3.2 Building Shared Objects
**Linker Command Line:**
- Support existing "form ELF DLL" option for shared object generation

**ELF Header Modifications:**
- Set e_type to ET_DYN for shared objects instead of ET_EXEC

**Program Headers:**
- Remove unnecessary PT_PHDR for shared objects
- Add required PT_DYNAMIC segment for dynamic linking information

**Dynamic Section:**
- Create .dynamic section (SHT_DYNAMIC) with Elf32_Dyn entries
- Include DT_NEEDED, DT_PLTRELSZ, DT_PLTGOT, DT_HASH, DT_STRTAB, DT_SYMTAB, etc.

**Dynamic Symbols:**
- Create separate dynamic symbol table (.dynsym) and string table (.dynstr)
- Exclude local symbols from dynamic table (except sections)
- Link .hash section to dynamic symbol table

**Dynamic Relocations:**
- Merge all relocations into single .rel.dyn table
- Support both REL and RELA relocation formats
- Create PLT relocations (.rel.plt) for function calls

**Global Offset Table:**
- Build GOT when encountering R_386_GOT32/GOTOFF/GOTPC relocations
- Reserve entries for _DYNAMIC, PLT base, and PLT second entry
- Create R_386_GLOB_DAT relocations for unresolved external symbols
- Generate R_386_RELATIVE relocations for non-external symbols

**Procedure Linkage Table:**
- Create PLT for PIC function calls (R_386_PLT32)
- Reserve PLT entries for _DYNAMIC and second GOT entries
- Generate .plt section with jump slots
- Create R_386_JUMP_SLOT relocations for PLT entries

### 3.3 Using Shared Objects
**Object File Reading:**
- Enhance ORL to properly read shared object files
- Collect shared object dependency names for dynamic linking

**Program Interpreter:**
- Add PT_INTERP program header for executables using shared objects
- Specify /lib/ld-linux.so.2 as interpreter path

**Required Libraries:**
- Add DT_NEEDED entries to dynamic array for shared object dependencies
- Maintain proper dependency order in dynamic structure

## 4. Known Issues and Fixes

### 4.1 Relocation Issues
- Fix R_386_PC32 relocation offset calculation (4-byte error)
- Support STT_NOTYPE symbols in ELF files
- Correct segment mapping for .data/.bss sections

### 4.2 Symbol Handling
- Preserve symbol types during linking process
- Handle function symbols in shared objects correctly

## 5. Implementation Priority

### 5.1 Critical (High Priority)
- ELF object file generation in CG386
- Basic PIC support implementation
- Shared object building capabilities
- Dynamic linking infrastructure

### 5.2 Important (Medium Priority)
- Command line interface extensions
- Dynamic symbol table handling
- PLT/GOT generation and relocation
- Shared object dependency resolution

### 5.3 Enhancement (Low Priority)
- Advanced optimization for PIC code
- Comprehensive test suite development
- Documentation and examples
