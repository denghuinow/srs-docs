# Software Requirements Specification (SRS)
## For Virtual-ED Distance Learning System
**Version:** 1.0
**Date:** October 26, 2023
**Prepared for:** New Jersey Institute of Technology (NJIT)
**Prepared by:** [Your Company/Team Name]

---

## 1. Introduction

### 1.1 Purpose
This document defines the functional and non-functional requirements for the Virtual-ED distance learning system. It is intended to serve as a comprehensive guide for the development team, project managers, stakeholders, and quality assurance personnel. The primary goal is to ensure a common understanding of the system's capabilities, constraints, and interfaces.

### 1.2 Document Conventions
*   **Bold text** is used for key terms and system entities.
*   *Italic text* is used for emphasis.
*   `Monospaced text` is used for user interface elements and technical references.
*   Requirements are uniquely identified as `FR` (Functional Requirement) or `NFR` (Non-Functional Requirement).

### 1.3 Project Scope
The Virtual-ED system is a secure, web-based portal designed to replicate and enhance a classroom environment for NJIT. It will integrate communication, collaboration, content management, and assessment tools into a single platform.

**In-Scope:**
*   Development of a web-based user interface compatible with Microsoft Internet Explorer, Apple Safari, and Mozilla Firefox.
*   User authentication and authorization integrated with the NJIT user database.
*   Real-time text-based instant messaging.
*   Audio and video conferencing capabilities.
*   Personal user profile management.
*   A virtual file storage space ("Virtual-Space") with quota management.
*   A timed online examination module ("Virtual-Exam").
*   Access to recorded lecture podcasts.
*   Collaborative whiteboard and application sharing sessions.
*   System administration tools for user, class, and enrollment management.

**Out-of-Scope (Non-Goals):**
*   Support for web browsers not listed in the compatibility matrix (Section 3.2).
*   Translation of user documentation into languages not specified by NJIT.
*   Scaling beyond the concurrent user limit imposed by the existing NJIT database infrastructure.
*   Development of native mobile applications (system is web-based).

### 1.4 References
*   NJIT IT Acceptable Use Policy
*   NJIT Data Privacy and Security Policy
*   Project Charter: Virtual-ED Distance Learning Initiative

## 2. Overall Description

### 2.1 Product Perspective
Virtual-ED is a new, self-contained web application that will integrate with several existing NJIT systems. It is not a modification of an existing product.

### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Responsibilities |
| :--- | :--- | :--- |
| **System Administrator** | Technically proficient; has full system access. | Maintain system health, manage global user enrollment, create/manage virtual classes, configure system settings. |
| **Professor (Administrative End User)** | Subject matter expert; manages a specific class. | Create/manage course content (exams, podcasts), moderate class collaborations, manage student file submissions, view student profiles. |
| **Student (Limited End User)** | Primary consumer of educational content. | Attend virtual sessions, submit assignments and exams, participate in chats and collaborations, manage personal profile and file space. |

### 2.3 Operating Environment
*   **Server Side:** Application server, database server, integrated FTP server, and streaming media server.
*   **Client Side:** Web browser (IE, Firefox, Safari) with JavaScript and pop-ups enabled. Web-conferencing features require a microphone, speakers, and optionally a webcam.
*   **Network:** Accessible via broadband internet connection.

### 2.4 Design and Implementation Constraints
1.  The system must authenticate users against the existing **NJIT User Database**.
2.  The client interface must be delivered via a standard web browser without requiring proprietary plugins.
3.  All user-generated content (chats, shared files) must be archived in compliance with NJIT policy.
4.  The initial design must support a concurrency limit of **250 users** as per the legacy database constraint.

### 2.5 Assumptions and Dependencies
*   The NJIT user database will provide accurate and timely role (Admin/Professor/Student) and class enrollment data.
*   Users will have the minimum required hardware and software as specified in Section 5.
*   External services (FTP Server, Streaming Media Server) will be available and meet their defined SLAs.
*   NJIT network bandwidth will be sufficient to support streaming media during typical usage.

## 3. System Features and Requirements

### 3.1 Functional Requirements

#### 3.1.1 User Authentication and Dashboard (FR-010)
**Description:** The system shall authenticate users and present a personalized dashboard.
*   **FR-010.1:** The system shall validate user credentials (username/password) against the NJIT User Database.
*   **FR-010.2:** Upon successful login, the system shall display a dashboard listing all classes in which the user is enrolled (based on role).
*   **FR-010.3:** The user shall be able to select a class from the dashboard to enter the class-specific environment.

#### 3.1.2 Instant Messaging and Presence (FR-020)
**Description:** The system shall enable real-time text chat between users within the same class.
*   **FR-020.1:** The system shall display a contact list showing other currently online users in the selected class.
*   **FR-020.2:** A user shall be able to initiate a chat session by double-clicking an online contact's name, opening a dedicated chat window. *[See AC-1]*
*   **FR-020.3:** Within a chat session, a user shall be able to send text messages in real-time.
*   **FR-020.4:** Within a chat session, a user shall be able to initiate a secure file transfer to the other party. *[See AC-2]*

#### 3.1.3 Audio/Video Conferencing (FR-030)
**Description:** The system shall support live audio and video communication between multiple users.
*   **FR-030.1:** A user (typically a Professor) shall be able to initiate a live audio or video conference session.
*   **FR-030.2:** Other users shall be able to join an active conference session.
*   **FR-030.3:** The system shall provide controls to accept or reject an incoming conference call request.

#### 3.1.4 User Profile Management (FR-040)
**Description:** Users shall be able to view and customize their personal profile information.
*   **FR-040.1:** All users shall be able to view their own profile, displaying information sourced from the NJIT database (e.g., name, ID).
*   **FR-040.2:** All users shall be able to edit customizable fields within their profile (e.g., profile picture, display name, contact preferences).
*   **FR-040.3:** Professors shall be able to view the profiles of students enrolled in their classes.

#### 3.1.5 Virtual-Space File Management (FR-050)
**Description:** The system shall provide personal and class-based file storage with quota enforcement.
*   **FR-050.1:** Upon selecting "Virtual-Space," the system shall display a navigable file tree for the user's personal and class-assigned storage.
*   **FR-050.2:** A user shall be able to upload a file from their local machine to a permitted location in their virtual space.
*   **FR-050.3:** The system shall check the user's storage quota before completing an upload. If the quota is exceeded, the upload shall be aborted and the user notified. *[See Exception 1]*
*   **FR-050.4:** A user shall be able to download, rename, and delete files for which they have appropriate permissions.

#### 3.1.6 Virtual-Exam Online Testing (FR-060)
**Description:** The system shall administer timed, file-based examinations.
*   **FR-060.1:** Professors shall be able to create an exam by uploading a question file, setting a time limit, and making it available to a class.
*   **FR-060.2:** Students shall see a list of available, untaken exams for their class.
*   **FR-060.3:** When a student starts an exam, the system shall download the exam file to the student's machine and start a countdown timer for the allotted time. *[See AC-3]*
*   **FR-060.4:** The student shall upload their completed answer file before the timer expires.
*   **FR-060.5:** Upon successful upload before the deadline, the system shall store the submission in a designated folder accessible only to the professor. *[See AC-4]*

#### 3.1.7 Podcast Lecture Access (FR-070)
**Description:** The system shall provide on-demand access to recorded lecture audio/video files.
*   **FR-070.1:** Professors shall be able to upload and publish media files (podcasts) to a specific class.
*   **FR-070.2:** Students shall be able to view a list of available podcasts for their class and select one to play via an integrated or external media player.

#### 3.1.8 Collaborative Whiteboard (FR-080)
**Description:** The system shall provide a shared, interactive whiteboard for real-time collaboration.
*   **FR-080.1:** A user shall be able to start a shared whiteboard session.
*   **FR-080.2:** Other invited users shall be able to join the session and simultaneously view and edit the shared whiteboard content.

#### 3.1.9 System Administration (FR-090)
**Description:** System Administrators shall have tools to manage the platform.
*   **FR-090.1:** Administrators shall be able to create, modify, and deactivate virtual `Class` entities.
*   **FR-090.2:** Administrators shall be able to manage `Enrollment` records, linking users to classes.
*   **FR-090.3:** Administrators shall be able to configure system-wide settings, including storage quotas and integration parameters.

### 3.2 External Interface Requirements

#### 3.2.1 User Interfaces
*   The primary interface shall be a web-based GUI rendered in compatible browsers (IE, Firefox, Safari).
*   The layout shall be clean and intuitive, following a dashboard-and-workspace model.
*   All interactive features shall be accessible via mouse and keyboard.

#### 3.2.2 Hardware Interfaces
*   The system requires no direct hardware interfaces on the server side beyond standard network and storage hardware.
*   Client-side hardware requirements are specified in Section 5.1.

#### 3.2.3 Software Interfaces
| Interface Name | Direction | Purpose | Data Input | Expected Output | SLA/Constraints |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **NJIT User DB** | Inbound | Authentication & Enrollment | Username, Password | User Role, List of enrolled ClassIDs | Must support 250 concurrent auth requests. |
| **FTP Server** | Outbound | File Storage | File binary, OwnerID, ClassID, Path | Storage confirmation/error | Must enforce user/class quotas and access control lists. |
| **Streaming Media Server** | Outbound | A/V Delivery | Live feed or media file URL | Media stream to client | Must support both live conferencing and on-demand podcast playback. |
| **Email System (SMTP)** | Outbound | Notifications | To, Subject, Body (e.g., quota alert) | Sent email | Reliable delivery for system-generated critical alerts. |

#### 3.2.4 Communications Interfaces
*   HTTP/HTTPS for web traffic.
*   WebSocket or similar technology for real-time features (chat, conferencing, whiteboard).
*   FTP/SFTP for file transfers to the storage server.
*   RTMP or HLS for streaming media.

## 4. Domain Model and Data Requirements
The system shall manage the following core entities and their attributes:

```yaml
User:
  - UserID: String, Unique, Primary Key
  - Name: String
  - Password: String, Required, Encrypted
  - Role: Enum(Admin, Professor, Student), Required
  - ContactInfo: String

Class:
  - ClassID: String, Unique, Primary Key
  - Name: String, Required
  - ProfessorID: String, Foreign Key to User, Required
  - Semester: String

Enrollment:
  - UserID: String, Foreign Key to User, Required
  - ClassID: String, Foreign Key to Class, Required
  - EnrollmentDate: DateTime

Message:
  - MessageID: String, Unique, Primary Key
  - SenderID: String, Foreign Key to User, Required
  - RecipientIDs: Array of Strings (Foreign Keys to User)
  - Timestamp: DateTime, Required
  - Content: Text, Required
  - Type: Enum(Chat, System)

File:
  - FileID: String, Unique, Primary Key
  - Filename: String, Required
  - OwnerID: String, Foreign Key to User, Required
  - ClassID: String, Foreign Key to Class (Optional)
  - UploadDate: DateTime, Required
  - Size: Integer, Required
  - Path: String, Required

Exam:
  - ExamID: String, Unique, Primary Key
  - ClassID: String, Foreign Key to Class, Required
  - ProfessorID: String, Foreign Key to User, Required
  - TimeLimit: Integer (minutes)
  - FileLink: String, Required
  - Status: Enum(Draft, Published, Closed)

ConferenceSession:
  - SessionID: String, Unique, Primary Key
  - HostID: String, Foreign Key to User, Required
  - ClassID: String, Foreign Key to Class
  - StartTime: DateTime
  - EndTime: DateTime
  - Type: Enum(Audio, Video, Whiteboard)

Podcast:
  - PodcastID: String, Unique, Primary Key
  - ClassID: String, Foreign Key to Class, Required
  - Title: String, Required
  - MediaFileLink: String, Required
  - DatePosted: DateTime, Required
```

## 5. Non-Functional Requirements

### 5.1 Performance Requirements
*   The web interface shall load the user dashboard within **3 seconds** over a standard broadband connection (>5 Mbps).
*   The system shall be designed to support the concurrent usage of **250 users** as per the integration constraint.
*   Client-side requirements for web-conferencing: Minimum 500 MHz CPU, 256 MB RAM.

### 5.2 Reliability & Availability
*   The system shall target an operational uptime of **99%**, excluding scheduled maintenance windows.
*   Scheduled maintenance requiring downtime shall be announced to all users at least **24 hours** in advance.

### 5.3 Security Requirements
*   Passwords shall be between **8 and 12 characters**, alphanumeric, and shall be required to change every **90 days**.
*   All authentication traffic shall be encrypted using TLS 1.2 or higher.
*   The system shall enforce role-based access control (RBAC) as defined in the user classes (Section 2.2).
*   The system shall archive logs of all chat conversations, file transfers, and system actions in an immutable format for audit purposes, per NJIT policy.

### 5.4 Compliance
*   The system and its use shall adhere to all relevant **NJIT IT Policies**, including Acceptable Use, Data Privacy, and policies regarding harassment and copyright.

## 6. Acceptance Criteria (Key Examples)
| ID | Scenario | Given | When | Then |
| :--- | :--- | :--- | :--- | :--- |
| **AC-1** | Initiate Chat | A user is logged in and another user in their class is online. | The user double-clicks the online contact's name. | A new chat window opens, allowing real-time text conversation. |
| **AC-2** | File Transfer in Chat | A user is in an active chat session. | The user clicks the file attachment button and selects a local file. | The system initiates a secure transfer, and the file is delivered to the other party. |
| **AC-3** | Start Timed Exam | A student is viewing a list of untaken exams. | The student clicks the "Start" button for an available exam. | The exam file downloads, and a persistent, on-screen countdown timer starts for the professor-allotted time. |
| **AC-4** | Submit Exam | A student is taking an exam with an active timer. | The student uploads their completed answer file and clicks "Submit" before the timer expires. | The system accepts the file, stores it securely in the professor's designated folder, and confirms submission success to the student. |

## 7. Appendices

### 7.1 Glossary
*   **Virtual-Space:** The personal and class-based online file storage system.
*   **Virtual-Exam:** The timed, file-based online testing module.
*   **Podcast:** A recorded audio or video lecture available for on-demand playback.
*   **SLA (Service Level Agreement):** A defined level of service for an external interface.

### 7.2 Open Issues and TBDs
1.  **Quota Management Rules:** Specific procedures for when a user exceeds their storage quota (e.g., automatic rejection vs. warning with override). *Responsible: System Architect*
2.  **External Software Selection:** Final vendor/product selection for the FTP and Streaming Media servers. *Responsible: Technical Lead*
3.  **Late Exam Protocol:** Detailed process for handling exam submissions that are late due to verified technical issues. *Responsible: Product Owner with NJIT*
4.  **Disaster Recovery:** Backup and restoration procedures for user-uploaded content on the FTP server. *Responsible: System Administrator*
5.  **Copyright Policy:** Clear policy governing intellectual property of materials shared on the platform. *Responsible: Legal/Product Owner*

---
*Document Approval:*

**Signature:** _________________________
**Name:** [Product Owner/Stakeholder Name]
**Title:** [Title]
**Date:** _________________________