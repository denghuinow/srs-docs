Purpose & Scope  
PeaZip is a cross-platform file and archive manager providing a unified GUI for Open Source compression utilities. It handles creating, updating, extracting, and managing archives across supported formats (e.g., 7z, ZIP, RAR), and includes file management tools. It does not support web-based operations, requires no external installations, and excludes system-level integration beyond its standalone portable mode.

Product Background / Positioning  
PeaZip evolved from a frontend for the Pea archiving utility into a consolidated GUI aggregator for multiple Open Source compression tools. It positions itself as a free, open-source alternative to commercial tools like WinRAR, offering broader format support and additional features like two-factor authentication without requiring system modifications.

Core Functional Overview  
- Archive creation and update in supported formats (7z, ZIP, etc.)  
- Extraction of contents from compressed archives  
- Two-factor authentication (password + keyfile) for archive security  
- Secure deletion of files (multiple-pass overwrite)  
- Byte-to-byte file comparison and checksum verification  
- Drag-and-drop object transfer between system and application  
- Timestamp appending to archive names for backup purposes  

Key Users & Usage Scenarios  
Primary users include general computer users managing files/archives and experienced users leveraging CLI features. All users access core functions via GUI (file manager, archive creator, extraction interfaces). Experienced users utilize command-line execution and advanced settings; general users rely on intuitive GUI workflows without prior OS expertise.

Major External Interfaces  
Graphical user interfaces (file manager, archive creator, extraction, settings, PeaLauncher). Keyboard shortcuts for all core functions. Hardware interface requires x86-compatible CPU. No external communication protocols or web dependencies.

Key Non-functional Requirements  
- Security: Extraction of encrypted archives requires correct password/keyfile; secure deletion leaves no residual data.  
- Usability: No prior OS knowledge required; functions accessible via GUI without training.  
- Reliability: Functions operate correctly with invalid inputs, providing clear error messages.  
- Portability: Supports Windows (32/64-bit), Linux, BSD, and UNIX-like systems.  

Constraints, Assumptions & Dependencies  
LGPL license mandates open-source distribution and compatibility with proprietary software. Development requires Delphi/Object Pascal. Hardware dependency: x86 CPU for ASM performance-critical sections. No external software dependencies beyond standard libraries (e.g., GTK/gdk).

Priorities & Acceptance Approach  
Highest priority: Core archive functions (creation, extraction, security). Secondary: Usability and cross-platform support. Acceptance requires verified functionality of all core features against supported formats and error handling per security requirements. No performance metrics specified.