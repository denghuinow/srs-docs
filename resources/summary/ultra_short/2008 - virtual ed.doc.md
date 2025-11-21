**Purpose & Scope**  
Virtual-ED is a secure distance learning platform for NJIT, enabling real-time communication and collaboration between students and faculty. It provides audio/video streaming, instant messaging, file sharing, customizable profiles, and online exams. It does not replace existing email systems or handle non-educational content.  

**Product Background / Positioning**  
Virtual-ED integrates with NJIT’s existing infrastructure as a dedicated learning environment, supplementing but not replacing current systems like Moodle or Blackboard. It relies on NJIT’s user database (limited to 250 concurrent users) and requires modifications to support new features.  

**Core Functional Overview**  
- Real-time instant messaging (text-based, group/one-to-one)  
- Live and on-demand audio/video streaming for lectures and meetings  
- Customizable user profiles (contact info, background, fonts, video intro)  
- Virtual-Space file management (upload, share, organize files)  
- Online exam system with timed submissions via file upload  
- Lecture podcasting (downloadable audio/video recordings)  
- Collaborative whiteboard for real-time document sharing/editing  

**Key Users & Usage Scenarios**  
- **Administrators**: Full system control, class setup, user management.  
- **Faculty**: Create classes, host lectures, administer exams, manage files.  
- **Students**: Access materials, participate in chats/lectures, submit assignments, view profiles.  
*Permissions*: Students have limited profile edits; faculty manage class-specific resources; admins control system-wide settings.  

**Major External Interfaces**  
- Web browser interfaces (IE, Firefox, Safari only).  
- FTP for file storage and sharing (quota-managed).  
- External services: Microsoft Office (for exams), Real Player (for podcasts).  

**Key Non-functional Requirements**  
- **Availability**: 99% uptime; scheduled maintenance with 24-hour notice.  
- **Performance**: Minimum 1.5 Mbps download speed for streaming.  
- **Security**: Passwords 8–12 characters (letters/numbers), mandatory 3-month change; antivirus required for file transfers.  
- **Reliability**: Data loss possible during outages; content responsibility lies with users.  

**Constraints, Assumptions & Dependencies**  
- **Hard constraint**: Max 250 concurrent users due to legacy NJIT database.  
- **Dependency**: Requires existing NJIT user database (may need maintenance).  
- **Assumption**: Users have broadband internet, webcam, and microphone.  
- **Exclusion**: No support for non-English documentation or unsupported browsers.  

**Priorities & Acceptance Approach**  
- **High priority**: Real-time messaging, online exams, lecture podcasting.  
- **Medium priority**: File management, profiles, whiteboard.  
- **Acceptance**: All features validated against explicit functional requirements (e.g., 99% uptime, browser compatibility, exam submission workflows).