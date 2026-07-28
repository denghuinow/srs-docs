# Software Requirements Specification (SRS)
## For the University of Puget Sound Moodle Enhancement Project

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the software requirements for a set of enhancements to the Moodle Learning Management System (LMS) for the University of Puget Sound. It is intended to serve as a comprehensive specification for developers, testers, project managers, and stakeholders, ensuring a common understanding of the system's capabilities and constraints. The primary goal is to refine Moodle to meet the university's specific instructional needs as a replacement for the existing Blackboard system.

#### 1.2 Document Conventions
*   **Priority Levels:**
    *   **Priority 1 (P1 - Core):** Mandatory for initial release. Fundamental to system operation and user acceptance.
    *   **Priority 2 (P2 - Important):** Mandatory for initial release. Significant value to key users.
    *   **Priority 3 (P3 - Desirable):** To be included as time and budget allow.
*   Requirements are uniquely identified as `FR` (Functional) or `NFR` (Non-Functional) followed by a numeric ID.
*   This document uses Markdown formatting for clarity.

#### 1.3 Project Scope
This project involves the development and integration of new modules and features *within* the existing Moodle platform. It is **not** a ground-up rebuild. The scope is strictly limited to adding the core functionalities enumerated in this document, leveraging Moodle's APIs, architecture, and plugin framework. All development is constrained by the capabilities and design patterns of the base Moodle system.

#### 1.4 References
*   Moodle Developer Documentation
*   University of Puget Sound IT Strategic Plan
*   Blackboard to LMS Migration Project Charter

### 2. Overall Description

#### 2.1 Product Perspective
This product is an enhanced instance of the Moodle LMS, positioned as a successor to the legacy Blackboard system. It will operate as a server-based web application, interacting with external systems for notifications (email/SMS) and incorporating third-party collaboration engines (wiki/blog).

#### 2.2 Product Functions
The enhanced system shall provide the following core functions:
1.  Multi-file upload management on course pages.
2.  Audio recording, portfolio organization, and management.
3.  Configurable web feed (RSS) generation for course content.
4.  Comprehensive content search across courses and system-wide.
5.  Online assignment grading with persistent grade history.
6.  Integrated wiki and blog functionality for student and faculty collaboration.
7.  Configurable email and SMS notifications for course activity.

#### 2.3 User Classes and Characteristics
| User Class | Characteristics | Key Goals |
| :--- | :--- | :--- |
| **Student** | Primary consumer; varies in technical proficiency. | Access course materials, submit assignments, collaborate with peers, receive updates, track grades. |
| **Professor (Course Administrator)** | Content expert; needs efficient course management tools. | Create/manage content, configure course features, grade assignments, communicate with students. |
| **System Administrator** | High technical proficiency; responsible for system health. | Install/configure system, manage users, perform backups/updates, monitor performance and security. |

#### 2.4 Operating Environment
*   **Software:** The enhancements will be developed for a standard LAMP/LEMP stack (Linux, Apache/Nginx, MySQL/MariaDB/PostgreSQL, PHP) as required by the core Moodle distribution.
*   **Hardware:** Must be deployable on university-managed virtual or physical servers.
*   **Browsers:** Must be compatible with current and immediately previous versions of major browsers (Chrome, Firefox, Safari, Edge).

#### 2.5 Design and Implementation Constraints
1.  All development **must** utilize the existing Moodle plugin architecture (e.g., Activity Modules, Blocks, Local Plugins) and public APIs.
2.  The database schema shall extend, not fundamentally alter, the core Moodle schema.
3.  The user interface must adhere to Moodle's theming framework to maintain visual consistency.
4.  Integration with third-party wiki/blog software must be achieved via standard protocols (e.g., OEmbed, LTI) or established Moodle integration patterns.

#### 2.6 Assumptions and Dependencies
*   **Assumption:** The core Moodle system is stable, secure, and provides a viable foundational platform for the required enhancements.
*   **Assumption:** The university's IT staff possesses or can acquire the necessary skills to maintain a Moodle-based system.
*   **Dependency:** Successful deployment depends on reliable external services for SMS gateway and email delivery.
*   **Dependency:** Project timelines are dependent on the stability and documentation of Moodle's core APIs.

### 3. External Interface Requirements

#### 3.1 User Interfaces
The system shall present a web-based user interface consistent with Moodle's standard theming and navigation. All new features must integrate seamlessly into the existing course page, administration block, and user profile layouts.

#### 3.2 Hardware Interfaces
None specified beyond standard server hardware requirements for Moodle.

#### 3.3 Software Interfaces
*   **SI-1: Email Gateway:** The system shall interface with the university's SMTP server to send notification emails.
*   **SI-2: SMS Gateway:** The system shall interface with a third-party SMS gateway API (e.g., Twilio, ClickSend) to send notification SMS messages.
*   **SI-3: Wiki/Blog Engine:** The system shall integrate with a specified third-party wiki (e.g., MediaWiki) and blog (e.g., WordPress) engine, allowing content to be embedded or linked within course contexts.

#### 3.4 Communications Interfaces
*   **CI-1:** HTTP/HTTPS for web browser communication.
*   **CI-2:** SMTP for email notifications.
*   **CI-3:** RESTful API or similar protocol for SMS gateway communication.

### 4. System Features

#### 4.1 Feature: Enhanced File Management
**4.1.1 Description & Priority**
Professors shall be able to configure specific course pages (e.g., assignment description pages, resource pages) to accept multiple file uploads from students in a single operation. (P1)

**4.1.2 Functional Requirements**
*   `FR-1.1`: The professor shall be able to enable/disable multi-file upload on a per-activity or per-resource basis during editing.
*   `FR-1.2`: When enabled, the student submission interface shall provide a drag-and-drop or multi-select file browser interface.
*   `FR-1.3`: The system shall display a list of uploaded files with names, sizes, and timestamps before final submission.
*   `FR-1.4`: The system shall enforce global and course-level file size and type restrictions.

#### 4.2 Feature: Audio Portfolio
**4.2.1 Description & Priority**
Users (primarily students) shall be able to record, upload, organize, and manage audio clips within a personal portfolio space, accessible across courses. (P1)

**4.2.2 Functional Requirements**
*   `FR-2.1`: The system shall provide an in-browser audio recorder (using the Web Audio API) requiring no additional plugins.
*   `FR-2.2`: Users shall be able to upload pre-recorded audio files.
*   `FR-2.3`: Users shall be able to create folders, tag, and annotate audio clips within their personal portfolio.
*   `FR-2.4`: Users shall be able to select clips from their portfolio to submit as assignments (e.g., for language courses).

#### 4.3 Feature: Configurable Web Feeds
**4.3.1 Description & Priority**
The system shall generate RSS/Atom feeds for course content updates. Professors shall be able to configure which page or activity types trigger feed updates. (P2)

**4.3.2 Functional Requirements**
*   `FR-3.1`: A configurable RSS feed shall be available for each course.
*   `FR-3.2`: Professors shall be able to select from a list of activity types (e.g., "Announcements," "New Assignments," "Forum Posts") to include in the feed.
*   `FR-3.3`: The feed shall include a title, description, publication date, and link to the new or updated content.

#### 4.4 Feature: Integrated Search
**4.4.1 Description & Priority**
The system shall provide a search function that indexes and returns results from content within a user's enrolled courses and, for administrators, across the entire system. (P1)

**4.4.2 Functional Requirements**
*   `FR-4.1`: A search box shall be present in the global site header.
*   `FR-4.2`: Search results shall be scoped by default to the user's current course context, with an option to search "All My Courses."
*   `FR-4.3`: Search results shall clearly indicate the course, activity type, and a relevant snippet of the matched content.
*   `FR-4.4`: System Administrators shall have a separate interface to search across all system content.

#### 4.5 Feature: Online Grading & History
**4.5.1 Description & Priority**
Professors shall be able to grade submitted assignments directly within the browser interface. All grade changes and feedback shall be maintained in a permanent, auditable history log. (P1)

**4.5.2 Functional Requirements**
*   `FR-5.1`: The grading interface shall display the student's submission and provide fields for numerical/letter grade, rubric scoring (if applicable), and text feedback.
*   `FR-5.2`: Every grade entry or modification shall create a permanent log entry recording the old value, new value, timestamp, and modifying user.
*   `FR-5.3`: Professors shall be able to view the grade history for any student assignment.

#### 4.6 Feature: Wiki & Blog Integration
**4.6.1 Description & Priority**
The system shall incorporate wiki and blog engines to facilitate collaboration. These may be integrated third-party tools presented within the Moodle interface. (P2)

**4.6.2 Functional Requirements**
*   `FR-6.1`: Professors shall be able to add a "Wiki" or "Blog" activity to a course.
*   `FR-6.2`: The wiki activity shall support collaborative page editing by enrolled users.
*   `FR-6.3`: The blog activity shall allow students to create individual or group posts, with commenting capabilities.

#### 4.7 Feature: Notification System
**4.7.1 Description & Priority**
Users shall be able to subscribe to receive email and/or SMS notifications for changes (e.g., new content, grades posted, forum replies) on specific course pages they select. (P2)

**4.7.2 Functional Requirements**
*   `FR-7.1`: Users shall have a personal "Notification Preferences" page to manage subscriptions.
*   `FR-7.2`: Preferences shall be configurable per-course and per-activity type.
*   `FR-7.3`: The system shall send notifications via the configured external gateways (SI-1, SI-2).
*   `FR-7.4`: Users must be able to opt-out of SMS notifications due to potential carrier charges.

### 5. Non-Functional Requirements

#### 5.1 Performance Requirements
*   `NFR-1 (Performance)`: The system shall support a minimum of **1000 concurrent authenticated users** with typical usage patterns (browsing, submitting, grading) without significant degradation in response time. Page load times for core actions shall remain under 3 seconds under this load.

#### 5.2 Reliability & Availability
*   `NFR-2 (Availability)`: The system shall target **99% uptime** over a calendar month, excluding announced maintenance windows.
*   `NFR-3 (Backup/Restore)`: All system data (database, user files, configuration) must be backed up on a configurable schedule (minimum daily). A full system restore from backup must be achievable within **six (6) hours**.

#### 5.3 Maintainability
*   `NFR-4 (Maintainability)`: The enhanced system must be maintainable by the university's existing IT staff. This requires:
    *   Clear documentation of all custom code and configuration.
    *   Adherence to Moodle's coding style and plugin guidelines.
    *   No modifications to the Moodle core code ("core hacking").

#### 5.4 Security
*   `NFR-5 (Security)`: All enhancements must inherit and comply with Moodle's built-in role-based access control and authentication systems. No feature shall bypass these security mechanisms.

### 6. Acceptance Criteria
Acceptance of the final deliverable will be based on verification that:
1.  All Priority 1 (P1) and Priority 2 (P2) functional requirements (`FR-1.x` through `FR-7.x`) are implemented and operational as described.
2.  The system demonstrably meets the quantified non-functional requirements (`NFR-1` through `NFR-5`) under load and recovery tests.
3.  The implementation passes the university's standard security review.
4.  All custom code is delivered with technical documentation for the IT maintenance team.

---
*Document End*