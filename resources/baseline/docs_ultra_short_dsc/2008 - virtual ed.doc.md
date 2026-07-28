# Software Requirements Specification (SRS)
## NJIT Distance Learning Platform (DLP)
**Version:** 1.0
**Date:** October 26, 2023
**Status:** Draft for Review

---

### **1. Introduction**

#### **1.1 Purpose**
This document defines the functional and non-functional requirements for the NJIT Distance Learning Platform (DLP). The intended audience includes NJIT stakeholders, project managers, software developers, testers, and system administrators. This SRS serves as the primary reference for the project's scope, features, and constraints throughout the development lifecycle.

#### **1.2 Document Conventions**
*   **Priority:** Requirements are tagged as `[Priority: High]`, `[Priority: Medium]`, or `[Priority: Low]` based on the project priorities section.
*   **Terms:** Key terms are defined upon first use and in the glossary (Appendix A).
*   **Formatting:** Requirements are presented as numbered, testable statements.

#### **1.3 Project Scope**
The NJIT DLP is a secure, web-based application designed to enhance communication and collaboration between professors and students in a distance learning context. It provides integrated tools for real-time communication, content delivery, assessment, and collaboration.

**In-Scope:**
*   User authentication integrated with the existing NJIT user database.
*   Real-time text, audio, and video communication.
*   Administration of online exams and assignments.
*   Personal and shared file storage with quotas.
*   Lecture recording and distribution.
*   Collaborative tools (whiteboard, application sharing).
*   User profile management.

**Out-of-Scope:**
*   Replacement of core university administrative systems (e.g., student registration, financial systems, official email).
*   Development of native mobile applications (primary interface is web browser-based).
*   Creation or long-term archival of official student transcripts.

#### **1.4 References**
*   NJIT IT Security Policy
*   NJIT Student Code of Conduct
*   Existing NJIT User Database Schema

---

### **2. Overall Description**

#### **2.1 Product Perspective**
The DLP is a new, self-contained web application that will integrate with the modified NJIT user database. It operates alongside, but does not replace, existing systems like email and the student information system. It is positioned as a comprehensive virtual classroom environment.

#### **2.2 Product Functions**
The core functions of the DLP include:
1.  User authentication and role-based authorization.
2.  Real-time instant messaging between enrolled users.
3.  Hosting and participating in live audio/video conferences.
4.  Streaming on-demand recorded lectures (podcasts).
5.  Creating, administering, submitting, and grading online exams.
6.  Providing personal file storage with quota management.
7.  Enabling document collaboration and file sharing.
8.  Sharing applications and a collaborative whiteboard during sessions.
9.  Allowing users to create and customize personal profiles.
10. Providing system administrators with tools to manage classes, enrollments, and system settings.

#### **2.3 User Classes and Characteristics**
| User Class | Characteristics | Key Responsibilities |
| :--- | :--- | :--- |
| **System Administrator** | Technical staff, full system access. | User/class lifecycle management, system configuration, monitoring, enforcing policies. |
| **Professor (Administrative End User)** | Instructor of record, manages pedagogical content. | Create/manage course content, host lectures, enroll students, grade submissions, moderate communication. |
| **Student (Limited End User)** | Learner, participates in courses. | Attend lectures, submit assignments/exams, communicate with peers and professors, manage personal profile and files. |

#### **2.4 Operating Environment**
*   **Server:** Environment to support 250+ concurrent users with 99% uptime.
*   **Client:** Web browser on the following minimum configurations:
    *   **OS:** Windows XP/Vista, Mac OS X.
    *   **Browsers:** Internet Explorer 7+, Firefox 3+, Safari 4+.
    *   **Client Hardware:** 500 MHz CPU, 512 MB RAM.
    *   **Network:** Broadband connection (for conferencing features).
    *   **Peripherals:** Webcam and microphone (for conferencing).
    *   **Settings:** JavaScript and pop-up windows enabled.

#### **2.5 Design and Implementation Constraints**
1.  Development must occur during the active university semester.
2.  The system must only support the browsers and operating systems listed in Section 2.4.
3.  The user interface must be compartmentalized into clear sections (welcome, class selection, application launch).
4.  Must integrate with and modify the existing NJIT user database schema.

#### **2.6 Assumptions and Dependencies**
*   **Assumptions:**
    *   The existing NJIT database will be available for modification.
    *   End users possess adequate hardware, software, and network connectivity.
    *   Users will comply with requirements to enable browser features (JavaScript, pop-ups).
    *   University staff and students are willing to adopt the new system.
*   **Dependencies:**
    *   Successful modification of the NJIT user database.
    *   Securing funding for necessary hardware, software, and development personnel.
    *   Availability of reporting tools (Microsoft Excel, PDF readers) on client machines.

---

### **3. External Interface Requirements**

#### **3.1 User Interfaces**
The DLP shall present a web-based portal with the following key interface sections:
1.  **Welcome/Login Page:** Authentication against NJIT credentials.
2.  **Dashboard:** Upon login, a central hub displaying enrolled classes, upcoming events, and notifications.
3.  **Class Selection/Workspace:** A compartmentalized area for accessing features specific to a selected class (e.g., chat, video conferencing, files, exams).
4.  **Application Launch Area:** A dedicated pane or window for launching collaborative tools (whiteboard, application sharing).

#### **3.2 Hardware Interfaces**
The server hardware must meet performance specifications in Section 4. No direct hardware interfaces are required for end-users beyond standard peripherals (keyboard, mouse, webcam, microphone).

#### **3.3 Software Interfaces**
*   **SI-1:** The system shall interface with the **existing NJIT user database** for authentication and user role information.
*   **SI-2:** The system shall rely on the client's local **operating system** for basic file I/O operations (save, open).
*   **SI-3:** Generated reports (e.g., grade sheets) shall be exportable in formats readable by **Microsoft Excel** and standard **PDF readers**.

#### **3.4 Communications Interfaces**
*   **CI-1:** The system shall use **HTTP/HTTPS** for standard web communication.
*   **CI-2:** Real-time features (chat, conferencing) shall use appropriate protocols (e.g., **WebSockets, RTP**).
*   **CI-3:** For specific administrative or data transfer tasks, support for **SSH, FTP, and VPN** clients may be required.

---

### **4. System Features**
*(This section details the functional requirements. Each subsection corresponds to a major feature.)*

#### **4.1 User Authentication and Role Management**
*   **FR1.1:** The system shall authenticate users against the integrated NJIT user database. `[Priority: High]`
*   **FR1.2:** The system shall enforce role-based access control (System Administrator, Professor, Student) upon login. `[Priority: High]`

#### **4.2 Real-Time Communication**
*   **FR2.1:** The system shall provide a text-based instant messaging interface for users within the same class or designated group. `[Priority: High]`
*   **FR2.2:** The system shall support live audio/video conferencing, allowing a Professor to host and students to join a session. `[Priority: Medium]`
*   **FR2.3:** The system shall allow application and whiteboard sharing within a live conference session. `[Priority: Medium]`

#### **4.3 Content Delivery and Management**
*   **FR3.1:** The system shall allow Professors to record live lecture sessions and publish them as on-demand podcasts. `[Priority: Medium]`
*   **FR3.2:** The system shall provide each user with personal file storage. `[Priority: Medium]`
*   **FR3.3:** The system shall enforce a storage quota for each user's personal file storage. `[Priority: Medium]`
*   **FR3.4:** The system shall enable file sharing and document collaboration between users within a class. `[Priority: Medium]`

#### **4.4 Assessment and Grading**
*   **FR4.1:** The system shall allow Professors to create, schedule, and administer timed online exams. `[Priority: High]`
*   **FR4.2:** The system shall allow Students to submit exam answers and file-based assignments. `[Priority: High]`
*   **FR4.3:** The system shall provide an interface for Professors to grade submissions and assign grades. `[Priority: High]`
*   **FR4.4:** The system shall provide Students with a view of their grades for a class. `[Priority: High]`

#### **4.5 User Profile and Customization**
*   **FR5.1:** The system shall allow all users to create and customize a personal profile (e.g., display name, avatar, contact information). `[Priority: Medium]`

#### **4.6 Administrative Functions**
*   **FR6.1:** The system shall allow System Administrators to create and deactivate classes/courses. `[Priority: High]`
*   **FR6.2:** The system shall allow Professors to manage student enrollment within their assigned classes. `[Priority: High]`
*   **FR6.3:** The system shall provide System Administrators with a dashboard for system health monitoring and user management. `[Priority: High]`

---

### **5. Non-Functional Requirements**

#### **5.1 Performance Requirements**
*   **PER-1:** The system server shall support a minimum of **250 concurrent users** without significant degradation in response time (< 2 seconds for standard page loads). `[Priority: High]`
*   **PER-2:** Live audio/video streaming shall have a latency of less than **500ms** end-to-end under normal network conditions.

#### **5.2 Security Requirements**
*   **SEC-1:** User passwords shall be between **8 and 12 characters**, containing both letters and numbers. `[Priority: High]`
*   **SEC-2:** The system shall force password changes every **three months**. `[Priority: High]`
*   **SEC-3:** All user-generated content shall be subject to monitoring and must comply with **NJIT conduct policies**. `[Priority: High]`
*   **SEC-4:** All data transmission containing personal or grade information shall use secure protocols (HTTPS, SFTP). `[Priority: High]`

#### **5.3 Reliability & Availability**
*   **REL-1:** The system shall have an estimated operational uptime of **99%**, excluding scheduled maintenance. `[Priority: Medium]`
*   **REL-2:** Scheduled maintenance requiring downtime shall be announced to all users at least **24 hours** in advance. `[Priority: Medium]`

#### **5.4 Maintainability**
*   **MAIN-1:** Major system updates, rollouts, and validation tests shall be scheduled during periods of historically low usage (e.g., semester breaks, weekends). `[Priority: Low]`

---

### **6. Acceptance Criteria**
Final acceptance of the delivered system is contingent upon:
1.  Successful implementation of all functional requirements tagged as `[Priority: High]`.
2.  Substantial implementation of `[Priority: Medium]` requirements, with any omissions formally documented and agreed upon.
3.  The system meeting all specified performance thresholds, particularly supporting **250 concurrent users**.
4.  The system operating within the defined technical constraints (supported browsers, OS).
5.  Delivery within the agreed-upon project timeline and budget.

---

### **Appendix A: Glossary**
*   **DLP:** Distance Learning Platform.
*   **Concurrent Users:** Number of users actively interacting with the system simultaneously.
*   **Podcast:** An audio/video recording of a lecture, made available for on-demand download or streaming.
*   **Quota:** A fixed limit on the amount of disk storage space allocated to a user.

### **Appendix B: Usage Scenarios**
*   **Scenario A (Live Lecture):** Professor Smith starts a video conference for "CS 101." Students join, view the shared whiteboard, and ask questions via text chat. The lecture is recorded.
*   **Scenario B (Group Collaboration):** A student team uses the document collaboration and file-sharing tools within their "Design Project" group to edit a report simultaneously.
*   **Scenario C (Online Exam):** A Student logs in, navigates to "PHY 201," starts a timed exam, submits answers, and receives a confirmation. The Professor later grades the submission through the grading interface.
*   **Scenario D (Content Review):** A Student accesses the "Lecture Podcasts" section of "HIST 105" and downloads last week's recorded lecture.