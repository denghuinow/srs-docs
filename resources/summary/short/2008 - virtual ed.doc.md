**Short Summary**

**Background and objectives**  
Virtual-ED is a distance-learning platform being developed for NJIT to enhance online education by providing a secure, interactive classroom environment. It aims to improve communication and collaboration between professors and students through features like real-time messaging, audio/video streaming, file management, and online testing.

**In scope**  
- Instant messaging for real-time text communication.  
- Streaming audio and video for live lectures and conferences.  
- Customizable user profiles with personal information and media.  
- Virtual file storage and management (Virtual-Space).  
- Online testing with timed exams and file uploads (Virtual-Exam).

**Out of scope**  
- Support for browsers other than Internet Explorer, Firefox, and Safari.  
- Languages beyond English for system documentation.  
- Integration with non-NJIT user databases.  
- Offline functionality for core features.  
- Mobile device compatibility.

**Stakeholders and core use cases**  
- **System Administrators**: Maintain the entire system, manage enrollment, and create virtual classes.  
- **Administrative End Users (Professors)**: Support their enrolled class and users via the front-end application.  
- **Limited End Users (Students)**: Operate the front-end with read-only permissions, except for profile modifications.  

*User stories*  
1. As a professor, I want to host a video lecture so that students can attend class remotely.  
2. As a student, I want to upload assignments to a secure folder so that I can submit work electronically.  
3. As a student, I want to chat with classmates in real time so that we can collaborate on projects.  
4. As a professor, I want to post exams online so that students can take timed tests remotely.  
5. As a student, I want to customize my profile so that peers can learn about my background.  
6. As a system administrator, I want to manage user accounts so that enrollment is controlled and secure.

**Success metrics**  
- System achieves 99% uptime during operational hours.  
- Supports at least 250 concurrent users without performance degradation.  
- Users report improved satisfaction with online interaction tools.

**Major constraints**  
- Development must occur while NJIT is in session, requiring minimal disruption to existing systems.  
- Only compatible with Windows XP/Vista and Mac OS, and specified browsers.  
- Current NJIT database may limit concurrent users to 250.  
- Users must have broadband internet, a webcam, and microphone for full functionality.  
- All system rollouts and validations must be scheduled during low-usage periods.

**Undecided issues**  
- Specific disk space quotas per student beyond initial 1GB/2GB allocations.  
- Final layout options for customizable GUI in Clean GUI V2.  
- Selection of antivirus software for mandatory file scanning.  
- Detailed integration plan with existing NJIT databases.  
- Exact scheduling for maintenance windows and upgrade deployments.