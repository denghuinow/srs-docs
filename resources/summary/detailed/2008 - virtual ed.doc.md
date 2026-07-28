# Detailed Summary: Virtual-ED Software Requirements Specification

## Background and Scope
Virtual-ED is a distance learning system designed for NJIT to enhance communication between professors and students through a secure application platform. The system aims to provide a classroom-like environment with features including audio/video streaming, file management, user profiles, chat, collaboration tools, and online testing. The scope covers the development of a web-based portal integrating these capabilities, with non-goals including support for non-Microsoft/Apple/Mozilla browsers, languages beyond those specified for documentation, and unlimited concurrent user scaling beyond existing database constraints.

## Stakeholders Matrix and Use Cases
*   **System Administrators:** Users with domain system privileges responsible for maintaining the entire system, managing enrollment, and creating virtual classes.
*   **Administrative End User (Professor):** Users with domain class privileges who maintain and support their enrolled class and users, operating the front-end application.
*   **Limited End User (Student):** Users with limited class privileges who can operate the front-end with read-only permissions and modify only their own profile.

**Main Scenarios:**
1.  User logs in and accesses the system menu.
2.  User initiates an instant messaging session with an online contact.
3.  User starts a video/audio call or conference with other users.
4.  User customizes their personal profile appearance and information.
5.  User uploads a file to their assigned virtual storage space.
6.  User downloads and submits a timed online exam.
7.  User accesses a recorded lecture as a podcast.
8.  User joins a shared whiteboard session for collaborative document editing.

**Exception Scenarios:**
1.  File upload exceeds storage quota.
2.  User rejects an incoming call or file transfer.
3.  Required software (e.g., media player) is not installed on the user's machine.

## Business Process
**Main Process: User Collaboration & Learning**
1.  **Trigger:** User authenticates via login.
2.  **Input:** Username and password.
3.  User selects a class from their dashboard.
4.  User chooses a feature (e.g., messaging, file space, exam).
5.  System presents the relevant interface (e.g., contact list, file tree, test link).
6.  User performs an action (e.g., sends message, uploads file, starts exam).
7.  System processes the action and updates the state (e.g., delivers message, stores file, starts timer).
8.  **Output:** User receives confirmation (e.g., message sent, file uploaded, exam submitted).

**Key Branch A: File Management**
1.  User selects "Virtual-Space."
2.  System displays file tree and available actions.
3.  User browses local machine and selects a file.
4.  System uploads file, checks quota, and updates the file tree.

**Key Branch B: Online Examination**
1.  User selects "Virtual-Exam" and clicks an available test.
2.  System prompts for confirmation and downloads the exam file.
3.  System starts a countdown timer for the allotted time.
4.  User uploads the completed file before the timer expires.

## Domain Model
*   **User:** ID (unique), Name, Password (required), Role (required: Admin/Professor/Student), ContactInfo.
*   **Class:** ClassID (unique), Name (required), ProfessorID (reference to User), Semester.
*   **Enrollment:** UserID (reference to User, required), ClassID (reference to Class, required), EnrollmentDate.
*   **Message:** MessageID (unique), SenderID (reference to User, required), RecipientID(s), Timestamp (required), Content.
*   **File:** FileID (unique), Filename (required), OwnerID (reference to User, required), ClassID (reference to Class), UploadDate, Size.
*   **Exam:** ExamID (unique), ClassID (reference to Class, required), ProfessorID (reference to User, required), TimeLimit, FileLink (required).
*   **Conference Session:** SessionID (unique), HostID (reference to User, required), StartTime, EndTime, Type (Audio/Video/Whiteboard).
*   **Podcast:** PodcastID (unique), ClassID (reference to Class, required), Title (required), MediaFileLink (required), DatePosted.

## Interfaces and Integrations
*   **NJIT User Database:** Inbound; Authentication & Enrollment; Input: User credentials; Output: User role and class list; SLA: Must support 250 concurrent users.
*   **FTP Server:** Outbound; File Storage Management; Input: File data and user/class metadata; Output: File storage confirmation; SLA: Quota enforcement and access control.
*   **Streaming Media Server:** Outbound; Audio/Video Delivery; Input: Live feed or media file; Output: Stream to clients; SLA: Support for live and on-demand streaming.
*   **Client Web Browser:** Bidirectional; Primary User Interface; Input: User interactions; Output: Rendered GUI and media; SLA: Compatibility with IE, Firefox, Safari; pop-ups and JavaScript enabled.
*   **Email System:** Outbound; Notifications; Input: Over-quota alerts, system messages; Output: Email to administrators/professors; SLA: Reliable delivery for critical alerts.

## Acceptance Criteria
**Capability: Instant Messaging**
*   Given a user is logged in and another user is online, when the user double-clicks the online contact's name, then a chat window opens for real-time text conversation.
*   Given a user is in a chat session, when the user clicks the file button and selects a file, then the system begins secure transmission of the file to the other party.

**Capability: Online Testing**
*   Given a student is viewing an untaken exam, when they click to start the exam, then the system downloads the test file and starts a countdown timer for the professor-allotted time.
*   Given a student is taking an exam, when they upload their completed file before the timer expires, then the system accepts the submission and stores it in the professor's folder.

## Non-functional Metrics
*   **Performance:** System must be accessible via broadband connection; Web-conferencing requires minimum 500 MHz CPU, 256 MB RAM.
*   **Reliability:** Target 99% uptime; scheduled maintenance with 24-hour user notification.
*   **Security:** Passwords must be 8-12 characters, alphanumeric, changed every 3 months; compliance with NJIT privacy and acceptable use policies.
*   **Compliance:** Adherence to NJIT policies regarding data content, harassment, and authorized use.
*   **Observability:** All chats, emails, and file shares are archived per NJIT policy for audit purposes.

## Milestones and Release Strategy
1.  Core platform with login, class selection, and basic GUI.
2.  Release 1: Instant Messaging, basic Virtual-Space (upload only), Customizable User Profile, Clean GUI V1.
3.  Release 1: Streaming Audio/Video, Test Admin - Virtual-Exam V1.
4.  Release 2: Enhanced Virtual-Space V2 (full file management), Clean GUI V2 (custom layouts).
5.  Release 2: Podcasts, Application Sharing/Whiteboards, Enhanced File Sharing.
6.  Final integration, user acceptance testing, and deployment.

## Risk List and Mitigation Strategies
1.  **Risk:** Existing NJIT database may be outdated, limiting concurrent users.
    *   **Mitigation:** Design to current 250-user constraint; plan for future scalability.
2.  **Risk:** System rollout may disrupt ongoing university sessions.
    *   **Mitigation:** Schedule deployments and validations during low-usage periods.
3.  **Risk:** Users may lack required hardware (webcam, microphone) or software (media players).
    *   **Mitigation:** Define clear minimum requirements in documentation and provide help desk support.
4.  **Risk:** Network bandwidth may affect streaming and conferencing quality.
    *   **Mitigation:** Specify minimum broadband requirements and design for graceful degradation.
5.  **Risk:** File sharing may introduce malware.
    *   **Mitigation:** Require antivirus software and include security warnings in the user agreement.
6.  **Risk:** Inappropriate use of collaboration tools (harassment, copyright violation).
    *   **Mitigation:** Enforce NJIT acceptable use policies, archive communications, and define clear reporting procedures.
7.  **Risk:** Project dependencies on external software interfaces (FTP, streaming servers).
    *   **Mitigation:** Early prototyping of integrations and clear SLA definitions with vendors.
8.  **Risk:** Resistance to adopting the new system by staff or students.
    *   **Mitigation:** Provide comprehensive training, manuals, online tutorials, and responsive help features.

## Undecided Issues and Responsible Parties
1.  Specific quota management rules for handling files that exceed space limits (System Architect).
2.  Final selection of FTP management and streaming media server software (Technical Lead).
3.  Detailed protocol for handling exam submissions that are late due to technical issues (Product Owner with NJIT).
4.  Exact format and distribution method for user documentation and tutorials (Documentation Lead).
5.  Integration specifics with the existing NJIT help desk for the "Help Feature" (Integration Specialist).
6.  Backup and disaster recovery procedures for user-uploaded content (System Administrator).
7.  Long-term scaling plan for the user database beyond the initial constraint (System Architect).
8.  Copyright and intellectual property policy for materials shared via the platform (Legal/Product Owner).