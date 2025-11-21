Purpose & Scope  
The system enhances Moodle to address University of Puget Sound’s courseware needs, focusing on file management, audio portfolio tools, and navigation. It extends Moodle’s core functionality without replacing it or adding unrelated features like standalone learning analytics.  

Product Background / Positioning  
The enhancement targets Moodle as a replacement candidate for Blackboard, leveraging its existing APIs. It integrates with university practices and stakeholder feedback from interviews, prioritizing features missing in current Moodle versions.  

Core Functional Overview  
- Enable per-page multiple file uploads for course content (e.g., assignments).  
- Manage audio clips in a speech-optimized portfolio with MP3 download.  
- Toggle web feeds (RSS) per-page for content updates.  
- Implement course-level search with category-based results.  
- Maintain grade history with timestamps for assignment revisions.  
- Integrate wiki and blog engines for collaborative content.  

Key Users & Usage Scenarios  
Students submit assignments, view grades, and manage audio portfolios. Professors create courses, grade work, and configure page features. System administrators maintain the platform and manage backups. Students cannot view others’ grades; professors control course content.  

Major External Interfaces  
Interfaces with Moodle APIs for core functionality. No new external systems required beyond existing Moodle infrastructure.  

Key Non-functional Requirements  
Support ≥1,000 concurrent users. Maintain 99% uptime (24/7 availability). Perform nightly backups with 6-hour restore capability.  

Constraints, Assumptions & Dependencies  
Must use Moodle’s existing APIs; no new external systems. Success depends on Moodle’s adoption as the base platform.  

Priorities & Acceptance Approach  
Initial release delivers Priority 1 (gradebook, web feeds) and Priority 2 (file uploads, audio, search) requirements. Acceptance requires all Priority 1–2 features to be operational in the first release.