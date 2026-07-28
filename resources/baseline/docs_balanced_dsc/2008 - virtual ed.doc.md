# Software Requirements Specification (SRS)
## For Virtual-ED Distance Learning System
**Document Version:** 1.0
**Date:** October 26, 2023
**Prepared for:** New Jersey Institute of Technology (NJIT)
**Prepared by:** [Your Name/Team Name]

---

### **1. Introduction**

#### **1.1 Purpose**
This document defines the functional and non-functional requirements for the Virtual-ED system. It is intended to serve as a comprehensive guide for the development team, project managers, stakeholders, and quality assurance personnel. This SRS will be used as the primary reference throughout the project lifecycle, including design, implementation, testing, and deployment.

#### **1.2 Document Conventions**
*   **Bold text** is used for key terms and section headings.
*   *Italic text* may be used for emphasis.
*   Requirements are uniquely identified with labels (e.g., `FR-1`, `NFR-2`).
*   All references to system components or user actions are presented in `monospace` font.

#### **1.3 Project Scope**
The Virtual-ED system is a secure, web-based distance learning platform designed to replicate and enhance the classroom experience for NJIT. Its core functionality centers on enabling real-time and asynchronous communication and collaboration between professors and students in a remote setting.

**In-Scope:**
*   User authentication and role-based access control.
*   Real-time audio/video conferencing and lecture streaming.
*   Synchronous text-based chat and instant messaging.
*   File management for distributing and submitting course materials, assignments, and exams.
*   Online testing with time limits and secure submission.
*   User profile management and interface customization.
*   Class and enrollment management by administrators and professors.

**Out-of-Scope:**
*   Development of original educational content.
*   Deep integration with non-NJIT third-party systems (e.g., external publisher platforms).
*   Full automation of exam grading (beyond collection and basic scoring for objective questions, as detailed in Undecided Issues).
*   Hardware provisioning for end-users.

#### **1.4 References**
*   NJIT IT Security and Acceptable Use Policies.
*   Project Charter for Virtual-ED.
*   Preliminary Stakeholder Interview Summaries.

---

### **2. Overall Description**

#### **2.1 Product Perspective**
Virtual-ED is a new, self-contained system that will integrate with the existing NJIT user authentication database. It operates as a client-server web application, accessible via supported browsers. The system is independent but must interoperate with NJIT's directory services for user identity.

#### **2.2 Product Functions**
The high-level functions of Virtual-ED include:
1.  **User Management:** Secure login, profile management, and role-based authorization.
2.  **Virtual Classroom:** Hosting and joining live, interactive video lectures with features for screen sharing and participant interaction.
3.  **Content Management:** Uploading, organizing, streaming, and downloading course files (lectures, syllabi, readings).
4.  **Assessment Management:** Creating, distributing, timing, and collecting exams and assignments.
5.  **Communication:** Facilitating real-time text chat (public/private) and asynchronous messaging.
6.  **Administration:** Creating classes, managing enrollments, and overseeing system health and user activity.

#### **2.3 User Classes and Characteristics**
| User Class | Characteristics | Key Responsibilities |
| :--- | :--- | :--- |
| **System Administrator** | Technical NJIT staff. Has full system access. | System configuration, user role assignment, performance monitoring, backup/restore. |
| **Professor (Admin End User)** | Faculty member. Has administrative rights within assigned classes. | Create/manage class content, host lectures, create/grade assessments, manage class enrollment. |
| **Student (Limited End User)** | Enrolled student. Has permissions limited to their enrolled classes and personal data. | Attend lectures, submit assignments/tests, access materials, communicate with peers and professors. |

#### **2.4 Operating Environment**
*   **Server:** Hosted on NJIT-managed infrastructure meeting performance requirements (see Section 3.3).
*   **Client:** Web browsers: Internet Explorer 7+, Firefox 3+, Safari 4+. Operating Systems: Windows XP/Vista, Mac OS X 10.5+.
*   **Network:** Requires broadband internet connection for optimal video conferencing functionality.

#### **2.5 Design and Implementation Constraints**
1.  Must use the existing NJIT user database schema as a base, requiring modification.
2.  All client-server communication must be encrypted using TLS 1.2 or higher.
3.  Must comply with NJIT's branding and web accessibility guidelines.
4.  Development must adhere to an iterative model with clear V1 and V2 milestones.

#### **2.6 Assumptions and Dependencies**
*   **Assumption:** NJIT will provide adequate funding for necessary hardware and software licenses.
*   **Assumption:** End-users possess basic computer literacy and have access to minimum required hardware (microphone, webcam).
*   **Dependency:** Successful modification and integration with the legacy NJIT user database.
*   **Dependency:** Availability of NJIT staff for training and User Acceptance Testing (UAT) during scheduled periods.

---

### **3. System Features**

This section details the functional requirements derived from user stories and key processes.

#### **3.1 Feature: User Authentication and Session Management**
**Description:** Users shall securely log in to the system using their NJIT credentials.
*   **FR-1:** The system shall authenticate users against the modified NJIT user database.
*   **FR-2:** Upon successful login, the system shall present a main menu/dashboard tailored to the user's role (Student, Professor, Admin).
*   **FR-3:** The system shall automatically log out a user after 30 minutes of inactivity.

#### **3.2 Feature: Live Virtual Classroom**
**Description:** Professors shall host and students shall join live, interactive video sessions.
*   **FR-4:** As a Professor, I shall be able to initiate a live video lecture session for any class I instruct.
*   **FR-5:** As a Student, I shall be able to join a live video lecture for any class in which I am enrolled.
*   **FR-6:** The system shall support real-time audio and video streaming between the host and all participants.
*   **FR-7:** As a Professor, I shall be able to share my entire desktop or a specific application window with all participants (User Story 4).
*   **FR-8:** The system shall provide a text-based chat panel within the live session for participants to ask questions or comment.

#### **3.3 Feature: File and Content Management**
**Description:** Users shall upload, download, and manage digital content.
*   **FR-9:** As a Professor, I shall be able to upload files (documents, presentations, videos) to a designated area for a specific class.
*   **FR-10:** As a Student, I shall be able to browse and download files posted to my enrolled classes.
*   **FR-11:** As a Student, I shall be able to upload assignment files to a private, professor-accessible folder associated with the specific assignment (User Story 2).
*   **FR-12:** The system shall display file metadata (name, uploader, date, size) in content lists.

#### **3.4 Feature: Assessments (Exams & Assignments)**
**Description:** Professors shall create and administer timed exams; students shall complete and submit them.
*   **FR-13:** As a Professor, I shall be able to create an online exam, setting a time limit and a due date/time (User Story 3).
*   **FR-14:** As a Professor, I shall be able to attach a file (e.g., PDF exam) to the assessment.
*   **FR-15:** As a Student, when I start an exam, the system shall start a countdown timer and allow me to download the exam file.
*   **FR-16:** As a Student, I shall be able to upload my completed exam file before the timer expires. The system shall block submission after the timer ends (Key Process 5).

#### **3.5 Feature: Communication and Messaging**
**Description:** Users shall communicate synchronously and asynchronously.
*   **FR-17:** As any User, I shall be able to see a list of other currently online users in my classes.
*   **FR-18:** As any User, I shall be able to initiate a private instant messaging session with any other online user (User Story 6).
*   **FR-19:** The system shall log all chat messages, storing sender, receiver, timestamp, and content.

#### **3.6 Feature: User Profile and Customization**
**Description:** Users shall manage their personal information and interface preferences.
*   **FR-20:** As any User, I shall be able to view and edit my personal profile information (e.g., display name, contact email).
*   **FR-21:** As any User, I shall be able to change my password, adhering to the security policy (see NFR-2).
*   **FR-22:** As any User, I shall be able to customize certain aspects of the interface appearance (e.g., theme color, font size) (User Story 5).

#### **3.7 Feature: System Administration**
**Description:** Administrators shall manage the system's core entities.
*   **FR-23:** As a System Administrator, I shall be able to create and deactivate user accounts and assign roles.
*   **FR-24:** As a System Administrator or Professor, I shall be able to create virtual class entities and manage the enrollment list.

---

### **4. External Interface Requirements**

#### **4.1 User Interfaces**
*   The interface shall be a responsive web application.
*   A consistent navigation menu shall be present across all pages, adjusted for user role.
*   All interactive elements (buttons, links) shall provide clear visual feedback.

#### **4.2 Hardware Interfaces**
*   The system shall interface with standard webcams and microphones via the browser's Media API.
*   Server hardware must meet specifications to support 250 concurrent users with mixed media workloads.

#### **4.3 Software Interfaces**
*   **NJIT User Database:** The system shall have read/write access to the modified `User` table for authentication and profile data.
*   **Web Server:** Apache 2.4+ or Nginx.
*   **Application Runtime:** Node.js 14+ or Python 3.8+.
*   **Database:** MySQL 5.7+ or PostgreSQL 12+.

#### **4.4 Communications Interfaces**
*   **HTTP/HTTPS:** For all standard web traffic.
*   **WebSocket/Socket.io:** For real-time features (chat, video conferencing signaling, live updates).
*   **SRTP/WebRTC:** For secure audio/video media streaming.

---

### **5. Non-Functional Requirements**

#### **5.1 Performance Requirements**
*   **NFR-1:** The system shall support at least **250 concurrent users** with acceptable performance.
*   **NFR-2:** The web conferencing module shall deliver video with a latency of less than 400ms for users with a broadband connection (>5 Mbps).
*   **NFR-3:** The system shall load the user dashboard within 3 seconds under normal load.

#### **5.2 Security Requirements**
*   **NFR-4:** User passwords shall be between 8 and 12 characters, contain letters and numbers, and shall be forced to change every 90 days.
*   **NFR-5:** All data transmission shall be encrypted using TLS 1.2+ protocols.
*   **NFR-6:** User sessions shall be managed with secure, HTTP-only cookies.
*   **NFR-7:** The system shall enforce role-based access control (RBAC) to prevent unauthorized access to functions or data.

#### **5.3 Usability Requirements**
*   **NFR-8:** The system shall provide contextual online help (`?` icons) and a searchable knowledge base.
*   **NFR-9:** Comprehensive printable user manuals (PDF) shall be available for download for each user class.
*   **NFR-10:** The system shall comply with WCAG 2.1 Level AA accessibility standards.

#### **5.4 Reliability & Availability**
*   **NFR-11:** The system shall have a target uptime of **99%** during core academic hours (7:00 AM - 11:00 PM EST).
*   **NFR-12:** Scheduled maintenance requiring downtime shall be announced to all users at least **24 hours** in advance.

#### **5.5 Compliance & Policy**
*   **NFR-13:** The system shall include a mandatory "Acceptable Use" splash screen upon first login, prohibiting discriminatory or inflammatory content as per NJIT policy.
*   **NFR-14:** All user-generated content shall be logged and traceable to the user account for accountability.

---

### **6. Data Model**
The core domain data elements are represented in the following simplified Entity-Relationship diagram:

```sql
-- Core Table Definitions (Simplified) --
USER (
    User_ID INT PK,
    Name VARCHAR(100),
    Password_Hash VARCHAR(255),
    Contact_Info VARCHAR(255),
    Role ENUM('Student', 'Professor', 'Admin'),
    Profile_Settings TEXT
);

CLASS (
    Class_ID INT PK,
    Class_Name VARCHAR(100),
    Instructor_ID INT FK -> USER(User_ID),
    Schedule TEXT,
    -- Enrollment managed via a junction table
);

FILE (
    File_ID INT PK,
    File_Name VARCHAR(255),
    Owner_ID INT FK -> USER(User_ID),
    Class_ID INT FK -> CLASS(Class_ID), -- Optional link
    Upload_Date DATETIME,
    File_Size BIGINT,
    Storage_Path VARCHAR(500)
);

ASSESSMENT (
    Assessment_ID INT PK,
    Title VARCHAR(200),
    Creator_ID INT FK -> USER(User_ID),
    Class_ID INT FK -> CLASS(Class_ID),
    Due_Date DATETIME,
    Time_Limit_Minutes INT,
    -- File_Reference would link to the FILE table
);

MESSAGE (
    Message_ID INT PK,
    Sender_ID INT FK -> USER(User_ID),
    Receiver_ID INT FK -> USER(User_ID), -- For simplicity; could be a group
    Timestamp DATETIME,
    Content TEXT,
    Type ENUM('Chat', 'System')
);
```

---

### **7. Appendices**

#### **7.1 Glossary**
*   **Concurrent Users:** Number of users with active, authenticated sessions at the same time.
*   **Podcast:** In this context, a recorded audio/video lecture file.
*   **RBAC:** Role-Based Access Control. A security paradigm restricting system access to authorized users based on their role.

#### **7.2 Undecided Issues & TBD**
1.  **Integration Scope:** Specific details of integration with other campus resources (e.g., library systems, calendar) beyond the user database remain to be defined.
2.  **Storage Quotas:** The logic for handling student file storage limits (warning, blocking uploads, archival) is pending a policy decision.
3.  **Release Planning:** The exact prioritization of features for the Minimum Viable Product (V1) versus a subsequent enhanced release (V2) requires stakeholder workshop.
4.  **Disaster Recovery:** Detailed procedures for backing up and restoring user-uploaded content need to be developed with NJIT IT.
5.  **Grading Automation:** The level of automation for exam grading (e.g., auto-grading for multiple choice) requires further analysis and specification.
6.  **UAT Process:** The formal process, participant selection criteria, and tools for User Acceptance Testing with NJIT staff are to be determined.