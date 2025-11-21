Purpose & Scope  
Ports Open Watcom's Windows GUI library to Linux using GTK toolkit. Solves cross-platform GUI compatibility for Open Watcom IDE. Does not support Windows-style resource files, MDI "windows in window" model, or built-in help subsystem.  

Product Background / Positioning  
Serves as the foundation for Open Watcom IDE's Linux port. Integrates with GTK 2.0+ as the primary UI toolkit, replacing Windows/OS/2 API dependencies. Requires no changes to existing Open Watcom application logic.  

Core Functional Overview  
Window initialization and management. Dialog creation and control handling. Menu and toolbar management. Text and font rendering. Status bar and scrolling functionality.  

Key Users & Usage Scenarios  
Open Watcom developers porting IDE to Linux. Permissions: Full access to porting tools. Scenarios: Initializing windows, creating dialogs, handling menus, and rendering text in Linux environment.  

Major External Interfaces  
GTK 2.0+ toolkit as primary UI interface. X Window System. No interfaces to Windows API or resource files.  

Key Non-functional Requirements  
Must run on GTK 2.0+ with X Window System. No support for MDI window model. Resource file conversion required (partial solution via libglade). Must maintain identical visual behavior across platforms.  

Constraints, Assumptions & Dependencies  
Hard constraint: No MDI "windows in window" support in GTK. Dependency: GTK 2.0+ and X Window System. Assumption: Resource file conversion via libglade acceptable for non-string resources.  

Priorities & Acceptance Approach  
Critical: Core window/dialog functionality (100% coverage). High: Menu/toolbar handling (95% coverage). Acceptance: All critical functions must pass GUI sample test (samp2.c). Non-critical: Help subsystem (not implemented).