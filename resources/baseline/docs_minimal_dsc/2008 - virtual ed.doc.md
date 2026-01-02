# Software Requirements Specification (SRS)
## Distance Learning Platform (DLP) for NJIT

**Document Version:** 1.0  
**Date:** [Current Date]  
**Authors:** [Project Team]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the NJIT Distance Learning Platform (DLP). The primary purpose of this document is to provide a detailed description of the system's capabilities, interfaces, and performance characteristics. It is intended for use by the project stakeholders, including developers, testers, project managers, and end-users, to ensure a common understanding of the system to be developed.

#### 1.2 Document Conventions
This document follows standard SRS conventions. Requirements are uniquely identified with labels (e.g., `FR-001`, `NF-002`). Functional requirements are prefixed with `FR`, and non-functional requirements with `NF`. All priorities are indicated as High (H), Medium (M), or Low (L).

#### 1.3 Project Scope
The NJIT Distance Learning Platform (DLP) is a secure, web-based application designed to facilitate effective professor-student communication and course management in a distance learning environment. The system will integrate with the existing NJIT user database and provide a suite of communication, content delivery, and assessment tools.

**In-Scope:**
*   User authentication and authorization via the existing NJIT user database.
*   Real-time text-based communication (one-to-one and group).
*   Audio/Video streaming for live lectures and on-demand playback.
*   File hosting, management, and assignment submission.
*   Online testing module for exam distribution, completion, and collection.
*   Web-based client accessible via specified browsers.
*   System administration tools for user and content management.

**Out-of-Scope:**
*   Development or modification of the existing NJIT user database.
*   Mobile-native applications (iOS/Android).
*   Integration with other external university systems (e.g., bursar, library).
*   Offline functionality for core features.
*   Creation of original course content.

#### 1.4 References
*   NJIT IT Policy Handbook
*   Existing NJIT User Database Schema & API Documentation
*   Web Content Accessibility Guidelines (WCAG) 2.1

#### 1.5 Definitions, Acronyms, and Abbreviations
| Term | Definition |
| :--- | :--- |
| **DLP** | Distance Learning Platform |
| **NJIT** | New Jersey Institute of Technology |
| **SRS** | Software Requirements Specification |
| **Admin End User** | User with elevated privileges (e.g., Professor, Instructor) |
| **Limited End User** | User with standard privileges (e.g., Student) |
| **A/V** | Audio/Visual |
| **Concurrent Users** | Number of users actively interacting with the system simultaneously |

---

### 2. Overall Description

#### 2.1 Product Perspective
The DLP is a new, self-contained web application that will operate within the NJIT IT ecosystem. It is a complementary system that must integrate with the **existing NJIT user database** for authentication. It does not replace any existing system but provides new, centralized functionality for distance learning.

#### 2.2 Product Functions (Summary)
The core functions of the DLP are:
1.  **Secure Communication:** Provide email, real-time group chat, and bulletin boards.
2.  **Content Delivery:** Enable live and on-demand streaming of audio/video lectures and conferences.
3.  **File Management:** Offer tools for users to store, manage, and submit files (e.g., assignments).
4.  **Online Assessment:** Support the full testing cycle: exam download, completion, and upload.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Responsibilities |
| :--- | :--- | :--- |
| **System Administrator** | Technical NJIT staff. Manages system health, configuration, and user support. | User account provisioning/de-provisioning, system monitoring, backup, and disaster recovery. |
| **Administrative End User (Professor/Instructor)** | Faculty member creating and managing course content. | Create/manage courses, post announcements, host A/V lectures, create/distribute/grade assignments and exams, moderate discussions. |
| **Limited End User (Student)** | Enrolled student participating in courses. | View course content, participate in chats and discussions, submit assignments, take exams, view grades. |

#### 2.4 Operating Environment
*   **Server Environment:** Linux/Windows server hosted in NJIT data center.
*   **Client Environment:** Web browsers: **Internet Explorer (latest stable version), Safari (latest stable version), Firefox (latest stable version)**.
*   **Database:** Must interface with the existing NJIT user database system.
*   **Network:** Standard university network and internet connectivity.

#### 2.5 Design and Implementation Constraints
1.  **Integration Constraint:** The system **must** authenticate users and pull basic profile information (name, role, enrolled courses) from the existing NJIT user database. It must not exceed the database's capacity of **250 concurrent connections**.
2.  **Deployment Constraint:** Updates and deployments must be scheduled to minimize downtime, as the university is in session. A rollback strategy is required.
3.  **Client-Side Constraint:** The application's client-side functionality must be fully compatible and tested with the specified web browsers (IE, Safari, Firefox).

#### 2.6 Assumptions and Dependencies
*   The existing NJIT user database will be available and provide a stable API or integration method.
*   Users will have access to a compatible web browser and a stable internet connection.
*   Sufficient server and bandwidth resources will be allocated by NJIT IT to support A/V streaming and file hosting.

---

### 3. System Features and Requirements

#### 3.1 Feature 1: User Authentication and Management
**Description:** Users will log in to the DLP using their existing NJIT credentials. The system will determine their role (Student, Professor, Admin) and present the appropriate interface and permissions.

**3.1.1 Functional Requirements**
*   `FR-001 (H)`: The system shall authenticate users against the existing NJIT user database.
*   `FR-002 (H)`: The system shall retrieve and display the user's full name and role upon successful login.
*   `FR-003 (M)`: The system shall allow System Administrators to manually deactivate/reactivate a user's DLP access without affecting their central NJIT account.
*   `FR-004 (M)`: The system shall automatically log out a user after 30 minutes of inactivity.

#### 3.2 Feature 2: Real-Time Communication
**Description:** The system will provide tools for synchronous (instant messaging) and asynchronous (email, bulletin boards) communication.

**3.2.1 Functional Requirements**
*   `FR-010 (H)`: The system shall provide a one-to-one instant messaging interface between any two users enrolled in a shared course.
*   `FR-011 (H)`: The system shall allow Administrative End Users to create and moderate group chat channels for their courses.
*   `FR-012 (H)`: The system shall provide a course-specific bulletin board for announcements and threaded discussions.
*   `FR-013 (M)`: The system shall support the sending and receiving of internal emails between users.

#### 3.3 Feature 3: Audio/Visual Streaming
**Description:** The system will support the delivery of live and recorded audio/video content.

**3.3.1 Functional Requirements**
*   `FR-020 (H)`: The system shall allow Administrative End Users to initiate a live A/V stream (lecture/conference) for their enrolled students.
*   `FR-021 (H)`: The system shall allow live streams to be recorded and saved for on-demand playback.
*   `FR-022 (H)`: The system shall allow Administrative End Users to upload pre-recorded A/V content for on-demand viewing.
*   `FR-023 (M)`: The system shall provide a basic "raise hand" or Q&A feature for students during live streams.

#### 3.4 Feature 4: File Hosting and Assignment Management
**Description:** Users will have personal and course-specific storage for files, with specific workflows for assignment submission.

**3.4.1 Functional Requirements**
*   `FR-030 (H)`: The system shall provide each user with a private file storage area.
*   `FR-031 (H)`: The system shall allow Administrative End Users to create assignments with a due date, instructions, and acceptable file formats.
*   `FR-032 (H)`: The system shall allow Limited End Users to upload files to fulfill an assignment before its due date.
*   `FR-033 (M)`: The system shall automatically timestamp submissions and prevent uploads after the due date has passed.

#### 3.5 Feature 5: Online Testing
**Description:** The system will provide a secure environment for distributing, completing, and collecting exams.

**3.5.1 Functional Requirements**
*   `FR-040 (H)`: The system shall allow Administrative End Users to upload an exam file (e.g., PDF, DOC) and make it available to a specific course at a scheduled time.
*   `FR-041 (H)`: The system shall allow Limited End Users to download the available exam file during the scheduled window.
*   `FR-042 (H)`: The system shall provide an interface for Limited End Users to upload their completed exam file before the deadline.
*   `FR-043 (M)`: The system shall log the time of download and upload for each student for audit purposes.

---

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
*   `NF-001`: The system shall support up to **250 concurrent users** as per the integrated database's limit.
*   `NF-002`: The instant messaging system shall deliver messages between users with a latency of less than 2 seconds under normal load.
*   `NF-003`: The A/V streaming system shall support a minimum of 50 concurrent viewers for a single live stream at standard definition (480p) quality.

#### 4.2 Security Requirements
*   `NF-010`: All authentication traffic (passwords) shall be encrypted in transit using TLS 1.2 or higher.
*   `NF-011`: Users shall only be able to access courses, files, and communications for which they are explicitly enrolled or authorized.
*   `NF-012`: Exam files uploaded by students shall be immediately locked from further modification and accessible only by the submitting student and the relevant Administrative End User.

#### 4.3 Availability & Reliability Requirements
*   `NF-020`: The system shall have a planned uptime of 99.5% during official university academic periods.
*   `NF-021`: Scheduled maintenance downtime shall be communicated to all users at least 72 hours in advance and shall not exceed 2 hours per month.
*   `NF-022`: User-uploaded files (assignments, exams) shall be backed up daily with a recovery point objective (RPO) of 24 hours.

#### 4.4 Usability Requirements
*   `NF-030`: The user interface shall be consistent across all major features and comply with NJIT's web accessibility guidelines.
*   `NF-031`: An Administrative End User shall be able to create a new assignment with all required fields in 5 steps or less.

#### 4.5 Browser Compatibility Requirements
*   `NF-040`: All core functionality shall be fully operational in the latest stable versions of Internet Explorer, Safari, and Firefox.
*   `NF-041`: The visual layout shall render consistently across the specified browsers, with acceptable degradation for non-core stylistic elements.

---
**Document End**