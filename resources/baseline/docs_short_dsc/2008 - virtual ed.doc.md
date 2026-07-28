# Software Requirements Specification (SRS)
## For Virtual-ED Distance Learning Platform
**Document Version:** 1.0
**Date:** [Date of Generation]
**Prepared for:** New Jersey Institute of Technology (NJIT)
**Prepared by:** [Your Name/Team]

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the Virtual-ED distance-learning platform. It is intended to serve as a comprehensive guide for stakeholders, developers, testers, and project managers involved in the system's design, implementation, and validation. Any discrepancies between this document and project goals should be resolved prior to development.

#### 1.2 Document Conventions
This document uses standard SRS conventions. Requirements are uniquely identified with tags (e.g., `FR-001`, `NFR-010`). Key terms are **bolded** upon first use. All priorities are defined as:
*   **High (H):** Essential for core functionality and release.
*   **Medium (M):** Important but not critical for initial release.
*   **Low (L):** Desirable enhancement for future iterations.

#### 1.3 Project Scope
The **Virtual-ED** system is a web-based platform designed to enhance online education at NJIT by providing a secure, interactive virtual classroom environment. The system will facilitate improved communication and collaboration between professors and students through integrated real-time and asynchronous tools.

**In-Scope Features:**
*   Real-time text-based instant messaging.
*   Live audio and video streaming for lectures and conferences.
*   Customizable user profiles.
*   A virtual file storage and management system (Virtual-Space).
*   An online testing module with timed exams and file uploads (Virtual-Exam).

**Explicitly Out-of-Scope:**
*   Browser support beyond Internet Explorer, Firefox, and Safari.
*   Multi-language support for system documentation or UI.
*   Integration with external, non-NJIT user databases or systems.
*   Offline functionality for core features (messaging, video, exams).
*   Native mobile application or mobile-optimized web compatibility.

#### 1.4 References
*   NJIT IT Infrastructure Policies
*   NJIT Student/Faculty Database Schema (Reference)
*   Project Charter: Virtual-ED, Version 1.0

### 2. Overall Description

#### 2.1 Product Perspective
Virtual-ED is a new, self-contained web application that will integrate with existing NJIT authentication and user databases. It is not a modification of an existing system but will rely on NJIT's IT infrastructure for user identity management and network services.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Responsibilities |
| :--- | :--- | :--- |
| **System Administrator** | Technical staff with full system privileges. | System maintenance, user account management (create/disable), virtual class creation, overall system health monitoring. |
| **Professor (Administrative End User)** | Faculty member with elevated permissions within their assigned classes. | Host live video/audio lectures, post and grade exams/assignments, manage class-specific file storage, moderate communications. |
| **Student (Limited End User)** | Enrolled student with read-mostly permissions. | Attend lectures, submit assignments and exams, participate in real-time chat, customize personal profile, access course materials. |

#### 2.3 Operating Environment
*   **Server:** To be hosted on NJIT-approved infrastructure.
*   **Client OS:** Microsoft Windows XP, Windows Vista, or Mac OS.
*   **Client Browsers:** Internet Explorer, Firefox, Safari (latest stable versions as of project start).
*   **Network:** Users require broadband internet connection. Full feature use requires a webcam and microphone.

#### 2.4 Design and Implementation Constraints
1.  Development and deployment must minimize disruption to existing NJIT academic systems during active semesters.
2.  The system is constrained by the performance limits of the current NJIT database, initially supporting **250 concurrent users**.
3.  All major deployments, updates, and validations must be scheduled during predefined low-usage periods (e.g., semester breaks, weekends).
4.  All uploaded files must be scanned by a to-be-determined antivirus software before being stored or made available for download.

#### 2.5 Assumptions and Dependencies
*   It is assumed NJIT will provide reliable authentication services and user data feeds.
*   The system's performance is dependent on users having adequate broadband internet, a supported OS, and browser.
*   Success is dependent on finalizing integration plans with existing NJIT databases.

### 3. System Features and Requirements

#### 3.1 Feature: Real-Time Communication
**Description:** Provides tools for synchronous interaction between users.

**3.1.1 Instant Messaging**
*   `FR-001` (H): The system shall provide a text-based chat interface accessible within a virtual classroom. *[Supports User Story #3]*
*   `FR-002` (H): Messages shall be delivered and displayed to all connected participants in near real-time (< 2 sec latency).
*   `FR-003` (M): The system shall log chat history per class session for later retrieval by Professors and Students of that class.

**3.1.2 Audio/Video Streaming**
*   `FR-010` (H): The system shall allow Professors to initiate a live video and audio broadcast to students enrolled in their class. *[Supports User Story #1]*
*   `FR-011` (H): The system shall support at least one active video stream (Professor) and 250 concurrent audio/listening connections per virtual classroom.
*   `FR-012` (M): The system shall provide the Professor with controls to mute/unmute all student audio feeds.

#### 3.2 Feature: User Profile Management
**Description:** Allows users to manage their personal information and presence on the platform.
*   `FR-020` (M): The system shall allow all users (Students, Professors) to view and edit their own profile information (e.g., display name, bio, avatar). *[Supports User Story #5]*
*   `FR-021` (L): The system shall allow users to upload a profile picture within size and format constraints.
*   `FR-022` (H): Student profiles shall be viewable by other members of the same class. Professor profiles shall be viewable by all students in their classes.

#### 3.3 Feature: Virtual File Storage (Virtual-Space)
**Description:** Provides secure, role-based file storage and management for course materials and assignments.
*   `FR-030` (H): The system shall provide each Student with private, secure storage for assignment submission. *[Supports User Story #2]*
*   `FR-031` (H): The system shall provide Professors with class-level storage for distributing materials (syllabi, readings, etc.).
*   `FR-032` (H): The system shall enforce role-based permissions (Student: upload to own/assignment folders; Professor: read/write/delete for class folders).
*   `FR-033` (M): All uploaded files shall be automatically scanned for malware using the designated antivirus software.

#### 3.4 Feature: Online Testing (Virtual-Exam)
**Description:** Facilitates the creation, delivery, and submission of timed examinations.
*   `FR-040` (H): The system shall allow Professors to create exams, set time limits, and publish them to a specific class. *[Supports User Story #4]*
*   `FR-041` (H): Once a Student starts an exam, the system shall enforce the time limit and auto-submit upon expiration.
*   `FR-042` (H): The system shall support file uploads as part of an exam submission (e.g., for essays, code files).
*   `FR-043` (M): The system shall prevent the exam interface from being left (e.g., via tab switching) without logging an attempt event for Professor review.

#### 3.5 Feature: System Administration
**Description:** Provides tools for the overall management of the platform and its users.
*   `FR-050` (H): The System Administrator shall be able to create, disable, and enable user accounts (Students, Professors). *[Supports User Story #6]*
*   `FR-051` (H): The System Administrator shall be able to create and configure virtual classrooms and enroll users.
*   `FR-052` (M): The system shall provide an admin dashboard displaying system health metrics (uptime, active users, storage usage).

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
*   `NFR-001`: The system shall support **250 concurrent users** with no significant performance degradation (page load < 3 sec, feature response < 2 sec).
*   `NFR-002`: Video streaming shall support a minimum resolution of 640x480 at 15 FPS with latency under 5 seconds.
*   `NFR-003`: The system shall achieve **99% uptime** during official NJIT operational hours (7:00 AM - 11:00 PM, Monday-Sunday).

#### 4.2 Safety & Security Requirements
*   `NFR-010`: All user authentication shall be performed via NJIT's central authentication system (e.g., LDAP/Active Directory).
*   `NFR-011`: All data transmission shall be encrypted using TLS 1.2 or higher.
*   `NFR-012`: User permissions shall be strictly enforced at the application and data-access levels.
*   `NFR-013`: File uploads shall be restricted to specific, safe MIME types and extensions.

#### 4.3 Software Quality Attributes
*   **Usability:** The interface shall be intuitive enough for non-technical users to perform core tasks (join a lecture, submit an assignment) with less than 15 minutes of initial orientation.
*   **Reliability:** The system shall automatically save exam progress at 30-second intervals to prevent data loss in case of client-side disruption.
*   **Maintainability:** The system shall be designed with modular components (messaging, streaming, testing) to allow for independent updates and maintenance.

### 5. Appendices

#### 5.1 User Stories Mapping
| ID | User Story | Mapped Functional Requirements |
| :--- | :--- | :--- |
| US-1 | As a professor, I want to host a video lecture... | FR-010, FR-011 |
| US-2 | As a student, I want to upload assignments... | FR-030 |
| US-3 | As a student, I want to chat with classmates... | FR-001, FR-002 |
| US-4 | As a professor, I want to post exams online... | FR-040, FR-041, FR-042 |
| US-5 | As a student, I want to customize my profile... | FR-020, FR-021 |
| US-6 | As a system administrator, I want to manage user accounts... | FR-050, FR-051 |

#### 5.2 Success Metrics
1.  **Availability:** 99% uptime measured monthly during defined operational hours.
2.  **Concurrency:** Successful load testing with 250 simultaneous users performing typical tasks.
3.  **User Satisfaction:** Post-implementation survey shows ≥ 20% improvement in satisfaction scores related to online interaction tools compared to baseline.

#### 5.3 Open / Undecided Issues (To Be Resolved)
1.  Final determination of disk space quotas per user role beyond initial allocations (Student: 1GB, Professor: 2GB).
2.  Selection and procurement of the mandated antivirus scanning software.
3.  Detailed technical specification for integration with existing NJIT user databases.
4.  Finalized schedule for recurring maintenance windows and upgrade deployment procedures.
5.  Approval of final GUI layout options from the "Clean GUI V2" design prototypes.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| System Architect | | | |