# **Software Requirements Specification (SRS)**
**For the**
**NJIT Distance Learning System (NDLS)**
**Version 1.0**

**Prepared by:** [Name/Team, e.g., Systems Analysis Team]
**Date:** [Date]
**For:** New Jersey Institute of Technology (NJIT)

---

## **Table of Contents**

1.  [Introduction](#1-introduction)
    1.1. [Purpose](#11-purpose)
    1.2. [Document Conventions](#12-document-conventions)
    1.3. [Intended Audience and Reading Suggestions](#13-intended-audience-and-reading-suggestions)
    1.4. [Project Scope](#14-project-scope)
    1.5. [References](#15-references)
2.  [Overall Description](#2-overall-description)
    2.1. [Product Perspective](#21-product-perspective)
    2.2. [Product Functions](#22-product-functions)
    2.3. [User Classes and Characteristics](#23-user-classes-and-characteristics)
    2.4. [Operating Environment](#24-operating-environment)
    2.5. [Design and Implementation Constraints](#25-design-and-implementation-constraints)
    2.6. [Assumptions and Dependencies](#26-assumptions-and-dependencies)
3.  [System Features and Requirements](#3-system-features-and-requirements)
    3.1. [Real-Time Communication Module](#31-real-time-communication-module)
    3.2. [File Hosting & Collaboration Module](#32-file-hosting--collaboration-module)
    3.3. [Online Testing Module](#33-online-testing-module)
    3.4. [Security & Administration](#34-security--administration)
4.  [External Interface Requirements](#4-external-interface-requirements)
    4.1. [User Interfaces](#41-user-interfaces)
    4.2. [Hardware Interfaces](#42-hardware-interfaces)
    4.3. [Software Interfaces](#43-software-interfaces)
    4.4. [Communications Interfaces](#44-communications-interfaces)
5.  [Non-Functional Requirements](#5-non-functional-requirements)
    5.1. [Performance Requirements](#51-performance-requirements)
    5.2. [Safety Requirements](#52-safety-requirements)
    5.3. [Security Requirements](#53-security-requirements)
    5.4. [Software Quality Attributes](#54-software-quality-attributes)
    5.5. [Business Rules](#55-business-rules)

---

## **1. Introduction**

### **1.1 Purpose**
This document describes the functional and non-functional requirements for the NJIT Distance Learning System (NDLS). The purpose of this system is to provide a secure, robust, and user-friendly platform that facilitates effective professor-student communication and academic interaction for distance learning at NJIT. This SRS serves as a contract between the development team and the stakeholders and will be the basis for design, implementation, testing, and project management.

### **1.2 Document Conventions**
This document follows standard IEEE SRS formatting conventions. Requirements are specified using the structure "The system shall..." Functional requirements are enumerated in Section 3. Markdown is used for formatting, with headers, lists, and emphasis for clarity.

### **1.3 Intended Audience and Reading Suggestions**
*   **Project Sponsors & Management:** Focus on Sections 1 (Introduction) and 2 (Overall Description) to understand scope and value.
*   **System Architects & Developers:** Focus on Sections 2 (Overall Description), 3 (System Features), and 4 (External Interfaces) for design and implementation details.
*   **Testers & QA Team:** Focus on Section 3 (System Features) and Section 5 (Non-Functional Requirements) to develop test plans and cases.
*   **End-Users (Professors, Students, Admins):** Focus on Section 2.3 (User Classes) and Section 3 (System Features) to understand system capabilities.

### **1.4 Project Scope**
The NJIT Distance Learning System (NDLS) will be a web-based application platform designed to bridge the communication gap in distance learning. Its core mission is to enable seamless, real-time interaction and structured academic activities between professors and students outside the traditional classroom.

**In-Scope:**
*   Secure user authentication and role-based authorization (Professor, Student, Administrator).
*   Real-time text-based chat, audio conferencing, and video conferencing between users within defined courses or groups.
*   Centralized file repository for course materials with upload, download, versioning, and basic management capabilities.
*   Synchronous document collaboration (e.g., simultaneous text editing).
*   Creation, scheduling, administration, submission, and automated grading (for objective questions) of online tests and quizzes.
*   A centralized administrative dashboard for user management, course enrollment, and system monitoring.

**Out-of-Scope:**
*   Integration with the official NJIT student information system (SIS) for automated enrollment (initial version).
*   Full-fledged Learning Management System (LMS) features like gradebooks, complex assignment workflows, or discussion forums.
*   Mobile-native applications (system will be browser-accessible only).
*   Offline functionality.

### **1.5 References**
*   IEEE Std 830-1998: IEEE Recommended Practice for Software Requirements Specifications.
*   NJIT IT Policy on Data Security and Privacy.
*   Project Charter: NDLS v1.0.

## **2. Overall Description**

### **2.1 Product Perspective**
The NDLS is a new, self-contained web application. It will operate within the NJIT IT infrastructure, leveraging existing authentication services (e.g., LDAP) where possible. It is envisioned as a complementary tool to existing NJIT systems, focusing specifically on interactive communication and assessment for distance learning.

### **2.2 Product Functions**
The high-level functions of the system are:
1.  **Real-Time Communication:** Facilitate live interaction via text, voice, and video.
2.  **Content Management & Collaboration:** Host files and allow for cooperative document editing.
3.  **Assessment:** Provide a platform for creating, delivering, and taking timed online tests.
4.  **User & System Management:** Administer user accounts, roles, courses, and system settings.

### **2.3 User Classes and Characteristics**
| User Class | Characteristics | Key Responsibilities |
| :--- | :--- | :--- |
| **Student** | Enrolled in one or more courses. Varying technical proficiency. Requires clear, intuitive interface. | Participate in live sessions, upload/download files, collaborate on documents, take tests. |
| **Professor** | Instructor for one or more courses. Needs efficient tools for content delivery and assessment. | Initiate/manage live sessions, upload course materials, create/administer tests, grade submissions. |
| **Administrator** | NJIT IT staff. High technical proficiency. Responsible for system health and user management. | Manage user accounts (add/disable), assign roles, configure system settings, monitor logs, schedule maintenance. |

### **2.4 Operating Environment**
*   **Server Environment:** Linux/Windows Server-based environment hosted in NJIT data centers.
*   **Client Environment (Explicitly Supported):**
    *   **Operating Systems:** Microsoft Windows XP, Windows Vista, Apple macOS.
    *   **Web Browsers:** Internet Explorer (latest version for OS), Mozilla Firefox (latest stable), Apple Safari (latest stable).
*   **Network:** Standard broadband internet connection for clients; high-speed LAN/WAN for servers.

### **2.5 Design and Implementation Constraints**
1.  **Browser Compatibility:** The client-side application **shall** be developed to be fully functional and tested exclusively on Internet Explorer, Mozilla Firefox, and Safari as specified in Section 2.4.
2.  **Client OS Compatibility:** The system **shall** be designed to operate on the specified client OSs (Windows XP, Vista, macOS) without requiring native software installation beyond the supported browsers.
3.  **Deployment Scheduling:** All major system rollouts, updates, and validation tests **shall** be scheduled during predefined periods of low system usage (e.g., weekends, early morning hours) to minimize user disruption.
4.  **Security:** The system **shall** comply with all NJIT data security and FERPA privacy policies.

### **2.6 Assumptions and Dependencies**
*   **Assumption:** Users will have a compatible browser and OS installed, a stable internet connection, and necessary peripherals (microphone, webcam) for audio/video features.
*   **Assumption:** Professors will be responsible for the content of their tests and materials.
*   **Dependency:** Availability of NJIT's network infrastructure and authentication services.
*   **Dependency:** Procurement and configuration of sufficient server hardware and bandwidth to support real-time audio/video streaming.

## **3. System Features and Requirements**

### **3.1 Real-Time Communication Module**
**3.1.1 Description:** This module provides tools for synchronous communication between users associated with a course.
**3.1.2 Requirements:**
*   **FR-1.1:** The system shall allow a Professor to initiate a scheduled or ad-hoc communication session (text, audio, or video) for a specific course.
*   **FR-1.2:** The system shall provide a text-based group chat room for each active session, with message persistence for the session duration.
*   **FR-1.3:** The system shall support audio conferencing for up to 25 simultaneous participants in a single session.
*   **FR-1.4:** The system shall support video conferencing for up to 10 simultaneous participants (video feeds) in a single session.
*   **FR-1.5:** The Professor shall have the ability to mute/unmute any participant in an audio/video session.
*   **FR-1.6:** The system shall include a "raise hand" feature for students to non-disruptively indicate a question.

### **3.2 File Hosting & Collaboration Module**
**3.2.1 Description:** This module allows for storage, sharing, and collaborative editing of course documents.
**3.2.2 Requirements:**
*   **FR-2.1:** The system shall provide a private file repository for each course, accessible only to enrolled users.
*   **FR-2.2:** Professors shall be able to upload, download, organize (into folders), and delete files within their course repository.
*   **FR-2.3:** Students shall be able to upload files to designated "assignment" folders and download files from any course folder.
*   **FR-2.4:** The system shall maintain basic version history for documents, storing the last 5 revisions.
*   **FR-2.5:** The system shall allow multiple users to collaboratively edit a plain-text or rich-text document in real-time, with changes visible to all editors simultaneously.

### **3.3 Online Testing Module**
**3.3.1 Description:** This module enables the creation, delivery, and submission of timed online assessments.
**3.3.2 Requirements:**
*   **FR-3.1:** Professors shall be able to create tests containing multiple-choice, true/false, and short-answer questions.
*   **FR-3.2:** Professors shall be able to schedule a test, setting a specific start time, duration, and deadline.
*   **FR-3.3:** The system shall automatically grade multiple-choice and true/false questions upon submission.
*   **FR-3.4:** During a test, the student's interface shall display a visible timer and prevent navigation away from the test page.
*   **FR-3.5:** The system shall automatically submit the test when the timer expires.
*   **FR-3.6:** Professors shall be able to view, manually grade (for short answers), and download results for their tests.

### **3.4 Security & Administration**
**3.4.1 Description:** Foundational requirements for access control and system management.
**3.4.2 Requirements:**
*   **FR-4.1:** All users shall authenticate with their NJIT UCID and password.
*   **FR-4.2:** The system shall enforce role-based access control (RBAC) as defined in Section 2.3.
*   **FR-4.3:** All real-time communication sessions and file transfers shall be encrypted using TLS 1.2 or higher.
*   **FR-4.4:** Administrators shall have a dashboard to view system status, active users, and audit logs.
*   **FR-4.5:** Administrators shall be able to enable/disable user accounts and assign/revoke user roles.

## **4. External Interface Requirements**

### **4.1 User Interfaces**
The UI shall be a clean, responsive web interface compatible with the browsers listed in 2.4. It shall consist of:
*   A login page.
*   A main dashboard showing enrolled courses and notifications.
*   Dedicated course pages with navigation to Communication, Files, and Tests.
*   Modal windows for video/audio communication.
*   A consistent header with user profile and logout controls.

### **4.2 Hardware Interfaces**
*   **Server:** Standard x86-64 server hardware.
*   **Client:** Must support audio input/output and video capture hardware for full functionality.

### **4.3 Software Interfaces**
*   **Database:** The system shall interface with a relational database (e.g., MySQL, PostgreSQL) for persistent data storage.
*   **Authentication Service:** The system shall interface with NJIT's central LDAP/Active Directory service for user credential validation.

### **4.4 Communications Interfaces**
*   **Signaling:** The real-time communication features shall use WebSocket connections for session control and signaling.
*   **Media Streaming:** Audio and video streams shall use WebRTC protocols for peer-to-peer or server-relayed communication.
*   **General:** All other client-server communication shall use HTTPS (RESTful API or similar).

## **5. Non-Functional Requirements**

### **5.1 Performance Requirements**
*   **PR-1:** The system shall support a concurrent user load of 500 users.
*   **PR-2:** The web application interface shall load any main page within 3 seconds over a standard broadband connection.
*   **PR-3:** Audio/video latency in communication sessions shall be less than 300ms end-to-end under normal network conditions.

### **5.2 Safety Requirements**
Not applicable for this software system.

### **5.3 Security Requirements**
*   **SR-1:** All passwords shall be stored using strong, salted cryptographic hashing (e.g., bcrypt).
*   **SR-2:** The system shall be protected against common web vulnerabilities (OWASP Top 10), including SQL injection, XSS, and CSRF.
*   **SR-3:** User sessions shall timeout after 30 minutes of inactivity.

### **5.4 Software Quality Attributes**
*   **Availability:** The system shall have 99.5% uptime during scheduled academic periods, excluding planned maintenance.
*   **Usability:** A new user shall be able to perform core functions (join a session, upload a file) with less than 5 minutes of orientation.
*   **Reliability:** The test submission process shall have 99.9% reliability; no student submission shall be lost due to system failure.
*   **Maintainability:** The system shall be designed with modular components, and code shall be documented to allow for efficient maintenance by NJIT IT staff.

### **5.5 Business Rules**
*   **BR-1:** Only users with a valid, active NJIT affiliation (student, faculty, staff) may have an account.
*   **BR-2:** A Student can only be enrolled in a course by an Administrator or the course Professor.
*   **BR-3:** A test, once started by a student, cannot be restarted. A single submission is final.
*   **BR-4:** All system maintenance and deployments must adhere to the scheduling constraint defined in Section 2.5.