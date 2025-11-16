# Balanced Summary

**Goals and scope**  
PeaZip is a cross-platform file and archive manager providing a graphical interface for open-source compression utilities. It enables users to create, update, and extract archives in multiple formats while offering file management tools like secure deletion and checksum verification. The software aims to be self-contained, requiring no additional installations for core functionality.

**Roles and user stories**  
- *As a general user*, I want to compress files into archives so that I can save storage space and organize data.  
- *As a security-conscious user*, I want to encrypt archives with passwords and keyfiles so that sensitive data remains protected.  
- *As an advanced user*, I want to split files into volumes so that I can manage large datasets across media.  
- *As a system administrator*, I want to access system tools through PeaZip so that I can perform maintenance tasks efficiently.  
- *As a novice user*, I want to use drag-and-drop functionality so that I can perform operations without complex navigation.

**Key processes**  
1. **Trigger: User launches application** → File manager interface loads for browsing system locations.  
2. **Trigger: User selects files and clicks "Add"** → Archive creation interface opens for compression setup.  
3. **Trigger: User selects archive and clicks "Extract"** → Extraction interface configures output path and parameters.  
4. **Trigger: User applies encryption settings** → Password and keyfile authentication secures the archive.  
5. **Trigger: User initiates any operation** → PeaLauncher displays real-time progress graphically.  
6. **Trigger: User accesses "Settings" menu** → Configuration interface allows customization of formats and tools.  
7. **Trigger: User drags files between system and application** → Objects are automatically added or extracted based on context.

**Domain data elements**  
- *Archive*: Name, Format, Encryption status, Size, Timestamp  
- *File*: Name, Path, Checksum, Size, Attributes  
- *User Settings*: Language, Default format, Toolbar layout, Security options  
- *System Location*: Path, Type (e.g., desktop, bookmarks), Access permissions  
- *Compression Job*: Source files, Destination, Algorithm, Progress status  
- *Security Credentials*: Password, Keyfile path, Encryption method

**Non-functional requirements**  
- Cross-platform compatibility (Windows, Linux, BSD, UNIX-like systems)  
- Self-contained deployment without external dependencies  
- Real-time progress visualization for all operations  
- Support for x-86 CPU architecture due to ASM-optimized sections  
- Configurable compression levels balancing speed and resource usage  
- Secure deletion preventing data recovery through multiple overwrite passes

**Milestones and external dependencies**  
- Integration of Lazarus IDE for development environment  
- Inclusion of GTK/GDK libraries for graphical components  
- Support for 40+ archive formats through bundled utilities  
- Packaging as portable edition for non-installation use  
- Documentation available through in-app help and online resources

**Risks and mitigation strategies**  
- *Risk: Incompatibility with uncommon archive formats* → Mitigation: Leverage multiple open-source compression backends.  
- *Risk: Performance issues with high-compression algorithms* → Mitigation: Implement multi-core optimization where possible.  
- *Risk: Security vulnerabilities in encryption* → Mitigation: Use peer-reviewed cryptographic libraries.  
- *Risk: Complex UI for novice users* → Mitigation: Provide tutorials and context-sensitive help.  
- *Risk: System resource exhaustion during large operations* → Mitigation: Implement progress monitoring and cancellation options.

**Undecided issues**  
- Cloud storage integration  
- Batch scripting automation  
- Mobile platform support  
- Plugin architecture for extensibility  
- Collaborative features  
- Not mentioned