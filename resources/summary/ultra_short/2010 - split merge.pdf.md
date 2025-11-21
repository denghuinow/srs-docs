Purpose & Scope  
Provides free, open-source PDF manipulation via GUI and console. Handles splitting, merging, rotating, and visual reordering of PDFs. Does not support PDF viewing, editing, or security features like encryption.  

Product Background / Positioning  
Free and open-source (GPLv2) tool filling a gap for multi-functional PDF handling without commercial cost. Complements existing PDF viewers but offers no integration with enterprise document management systems.  

Core Functional Overview  
- Split PDFs by page count, bookmarks, or custom rules.  
- Merge/extract pages from multiple PDFs into single documents.  
- Alternate mix pages from two PDFs (e.g., scanner outputs).  
- Rotate entire PDFs in 90° increments.  
- Visually reorder and delete specific pages via drag-and-drop.  
- Save/load working environments for repetitive tasks.  

Key Users & Usage Scenarios  
General users (non-technical) perform split/merge via GUI for personal document handling. Developers use console mode for batch processing and contribute code. No role-based permissions; all users access identical core features.  

Major External Interfaces  
GUI (Java Swing) for all user interactions. Console interface for command-line execution. Requires Java Runtime Environment (JRE) 1.6+. No network or third-party API dependencies beyond update checks.  

Key Non-functional Requirements  
- Memory: Max 254MB default (adjustable for large files).  
- Safety: Input PDFs unchanged during processing.  
- Performance: Direct response time for all operations.  
- License: Strictly GPLv2 (no commercial redistribution).  

Constraints, Assumptions & Dependencies  
Requires JRE 1.6+; platform-independent via Java. No security or user authentication needed. Depends on user-provided PDF files (not external services).  

Priorities & Acceptance Approach  
All listed features are implemented and stable; no new prioritization required. Acceptance validated by functional testing against core capabilities (split/merge/rotate/visual tools) and license compliance.