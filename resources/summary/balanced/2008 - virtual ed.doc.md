# Balanced Summary: Virtual-ED

## Goals and Scope
Virtual-ED is a distance learning system designed for NJIT to enhance communication between professors and students via a secure application platform. Its core scope includes providing features such as audio/video streaming, file management, user profiles, chat, and online testing to create a classroom-like online environment. The system aims to improve collaboration and learning effectiveness for remote participants.

## Stakeholders and User Stories
*   **System Administrators:** Manage the entire system, including enrollment and virtual class creation, with full system control.
*   **Administrative End Users (e.g., Professors):** Maintain and support their enrolled classes and users through the application's front end.
*   **Limited End Users (e.g., Students):** Operate the front end with limited permissions, primarily able to modify their own profiles.

**User Stories:**
1.  As a **Student**, I want to **participate in live video lectures** so that **I can interact with the professor and classmates in real-time**.
2.  As a **Student**, I want to **upload assignments to a private folder** so that **I can submit work securely**.
3.  As a **Professor**, I want to **distribute and collect exams online** so that **students can take timed tests remotely**.
4.  As a **Professor**, I want to **share my desktop or applications** so that **I can conduct lectures using presentations or a whiteboard**.
5.  As a **User**, I want to **customize my profile and interface appearance** so that **I can personalize my learning environment**.
6.  As a **User**, I want to **instantly message other online users** so that **I can get quick answers to questions**.

## Key Processes
1.  **User Login:** Triggered by user accessing the system with credentials, resulting in display of the main menu.
2.  **Content Access & Download:** Triggered by user selecting a resource (e.g., lecture podcast, exam file), resulting in file streaming or download.
3.  **Real-time Communication Initiation:** Triggered by user selecting a contact, resulting in a chat, audio, or video call window opening.
4.  **File Management Operation:** Triggered by user action (e.g., click Upload/Browse), resulting in file transfer to/from server storage.
5.  **Assessment Submission:** Triggered by student completing a downloaded exam, resulting in file upload before a timer expires.
6.  **Profile/Interface Customization:** Triggered by user accessing preferences, resulting in changes to personal data or GUI settings.
7.  **Collaborative Session Hosting/Joining:** Triggered by user initiating or accepting an invitation, resulting in a shared workspace or conference.

## Domain Data Elements
*   **User:** (PK: User_ID) Name, Password, Contact_Info, Role, Profile_Settings.
*   **Class:** (PK: Class_ID) Class_Name, Instructor_ID, Schedule, Enrollment_List.
*   **File:** (PK: File_ID) File_Name, Owner_ID, Upload_Date, File_Size, Storage_Path.
*   **Message/Chat Log:** (PK: Message_ID) Sender_ID, Receiver_ID(s), Timestamp, Content, Type.
*   **Exam/Assignment:** (PK: Assessment_ID) Title, Creator_ID, Due_Date/Time_Limit, File_Reference, Grade.
*   **Lecture/Podcast:** (PK: Media_ID) Title, Presenter_ID, Recording_Date, File_Format, Access_Link.

## Non-functional Requirements
1.  **Performance:** System must support 250 concurrent users; web conferencing requires broadband user connections.
2.  **Security:** Users must maintain passwords (8-12 chars, changed quarterly); all data transfer must use secure protocols.
3.  **Compatibility:** Client-side support limited to Windows XP/Vista, Mac OS, and IE/Firefox/Safari browsers.
4.  **Usability:** System must provide online help, tutorials, and printable manuals for end-users.
5.  **Reliability:** Target system uptime is 99%, with scheduled maintenance notifications provided 24 hours in advance.
6.  **Safety/Policy:** Users are prohibited from posting discriminatory or inflammatory content, adhering to NJIT policies.

## Milestones and External Dependencies
1.  Completion and approval of this SRS document.
2.  Modification of existing NJIT user database to support new system entities.
3.  Acquisition of funding for necessary hardware, software, and personnel.
4.  Scheduling system rollouts and validation during periods of low current system usage.
5.  Availability and cooperation of NJIT staff to learn and adopt the new system.

## Risks and Mitigation Strategies
1.  **Risk:** Existing NJIT database may be outdated, limiting concurrent users.
    *   **Mitigation:** Plan for database upgrades as part of project funding and scope.
2.  **Risk:** System development occurs while university is in session, limiting deployment windows.
    *   **Mitigation:** Schedule deployments and major updates during announced low-usage periods.
3.  **Risk:** Users may lack adequate hardware (webcam, microphone) or bandwidth.
    *   **Mitigation:** Clearly communicate minimum requirements and offer alternative features (e.g., text chat).
4.  **Risk:** Potential for misuse (harassment, unauthorized sharing).
    *   **Mitigation:** Enforce strict security policies, logging, and user accountability per NJIT guidelines.
5.  **Risk:** Integration complexity with current campus systems and resources.
    *   **Mitigation:** Detailed interface analysis and phased integration approach.

## Undecided Issues
1.  Specific details of integration with other campus resources (beyond the user database).
2.  Final quota management logic for student file storage when limits are exceeded.
3.  The exact feature set prioritization for the first release (V1) versus the second release (V2).
4.  Detailed disaster recovery and data backup procedures for user-uploaded content.
5.  Specifics of the grading automation for online exams beyond basic collection.
6.  Formal process and tools for user acceptance testing (UAT) with NJIT staff.