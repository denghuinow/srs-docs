# Software Requirements Specification (SRS)
## Puget Sound Moodle Enhancements Project

**Document Version:** 1.0
**Date:** October 26, 2023
**Status:** Draft for Review
**Prepared for:** University of Puget Sound
**Prepared by:** [Project Team/Consultant Name]

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the enhancement of the Moodle Learning Management System (LMS) at the University of Puget Sound. The purpose is to provide a detailed description of the features to be developed, serving as a contractual agreement between stakeholders and the development team, and as a foundation for system design, implementation, and testing.

#### 1.2 Project Scope
This project involves targeted enhancements to an existing Moodle installation to address critical gaps identified as barriers to replacing the legacy Blackboard system. The scope is limited to developing specific new functionalities and configurations without undertaking a full system rebuild or major architectural changes.

**In-Scope Enhancements:**
*   Multiple file upload capability for assignments, forums, and other configurable pages.
*   Audio recording and portfolio management tools tailored for language learning.
*   Global search functionality with filtering across all course materials.
*   Enhanced gradebook with grading, feedback, and audit history.
*   Configurable RSS web feed integration for dynamic content updates.

**Out-of-Scope Items:**
*   Replacement of Moodle's native social/collaborative tools (e.g., forums, messaging).
*   Development of a new courseware system architecture.
*   Major modifications to core Moodle APIs or database schema.
*   Integration with external social media platforms (e.g., Facebook, Twitter).
*   Comprehensive UI/UX overhaul of existing Moodle interfaces.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **API:** Application Programming Interface
*   **LMS:** Learning Management System
*   **RSS:** Really Simple Syndication (or Rich Site Summary)
*   **UI/UX:** User Interface / User Experience
*   **OIS:** Office of Information Services (University of Puget Sound)
*   **SRS:** Software Requirements Specification

#### 1.4 References
*   Moodle Official Documentation (https://docs.moodle.org/)
*   University of Puget Sound IT Standards and Practices
*   Stakeholder Interview Summaries (Internal Document)

#### 1.5 Document Overview
This document is structured to present an overall description of the product, followed by specific functional and non-functional requirements, and concluding with appendices for supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
This project is an enhancement module for the existing Moodle LMS. It will operate as a set of integrated plugins and configurations that extend the core Moodle functionality. The system must interoperate seamlessly with the existing Moodle core, authentication system, and database.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Student** | Primary end-user. Varying technical proficiency. Needs intuitive access to materials and submission tools. | Submit assignments, access content, receive grades/feedback, track personal progress (e.g., language portfolio). |
| **Professor (Instructor)** | Content creator and course manager. Moderate to high technical proficiency. Needs efficient course administration tools. | Upload materials, create activities, configure features (uploads, RSS), grade assignments, provide feedback. |
| **System Administrator** | Technical expert. Responsible for system health, security, and configuration. Limited availability (per constraints). | Install/configure plugins, manage backups, monitor performance, apply updates with minimal disruption. |

#### 2.3 Operating Environment
*   **Software:** Existing Moodle installation (version to be specified), standard LAMP/LEMP stack (Linux, Apache/Nginx, MySQL/MariaDB, PHP).
*   **Hardware:** University-hosted servers meeting Moodle's recommended specifications for ~1,000 concurrent users.
*   **Network:** Accessible via university network and VPN, with 24/7 availability expectations.

#### 2.4 Design and Implementation Constraints
1.  **API Constraint:** Enhancements must utilize existing Moodle plugin APIs and hooks. Deep core modifications are prohibited.
2.  **Maintainability Constraint:** The system must be largely self-sustaining due to limited OIS staff. Plugins must be stable, well-documented, and easy to update.
3.  **Compliance Constraint:** All features must comply with University IT standards, accessibility guidelines (WCAG 2.1 AA), and FERPA data protection requirements.
4.  **Budget/Time Constraint:** Development is phased by priority. Priority 3 features are explicitly limited by timeline and budget.
5.  **Usability Constraint:** The interface for new features must be simple, intuitive, and responsive, maintaining consistency with the existing Moodle UI.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** The University will proceed with Moodle as the primary LMS, pending the success of this enhancement project.
*   **Assumption:** Adequate server storage is available for audio files and increased backup frequency.
*   **Dependency:** Project success is dependent on the stability and compatibility of the underlying Moodle core version.
*   **Dependency:** Final requirements for backup schedules and storage are dependent on University policy finalization.

### 3. System Features and Requirements

#### 3.1 Feature 1: Configurable Multiple File Upload
**3.1.1 Description**
Professors shall be able to enable or disable multiple file uploads on a per-activity basis (e.g., Assignment, Forum). When enabled, students can upload more than one file in a single submission action.

**3.1.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR1.1** | The system shall provide a configuration setting ("Allow multiple files") within the setup form for Assignment and Forum activities. | High |
| **FR1.2** | When enabled, the student submission interface shall display a dynamic interface to add, remove, and preview multiple files before final submission. | High |
| **FR1.3** | The system shall validate total upload size against the existing course/activity upload limit. | High |
| **FR1.4** | The system shall display all submitted files to the professor in the grading interface. | High |

#### 3.2 Feature 2: Audio Recording & Language Portfolio
**3.2.1 Description**
Students, particularly in language courses, shall be able to record audio directly within Moodle and manage recordings in a personal portfolio to track progress over time.

**3.2.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR2.1** | The system shall provide an "Audio Record" button within relevant activity types (e.g., Assignment submission, dedicated Portfolio activity). | High |
| **FR2.2** | The recording interface shall use the browser's MediaDevices API to capture microphone input, with visual feedback (e.g., level meter, record/stop buttons). | High |
| **FR2.3** | The system shall allow students to play back, re-record, and save the audio clip in a standard format (e.g., MP3, WebM). | High |
| **FR2.4** | The system shall provide a "My Language Portfolio" view where students can see a timeline of all their saved recordings, tagged with course/activity and date. | Medium |

#### 3.3 Feature 3: Global Course Search
**3.3.1 Description**
Students and professors shall be able to search for text across all pages and resources within their enrolled courses, with results filterable by course, activity type, and date.

**3.3.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR3.1** | A persistent "Search all my courses" field shall be available in the main site header. | High |
| **FR3.2** | The search shall index content from course pages, labels, assignment descriptions, forum posts, and resource files (text content). | High |
| **FR3.3** | The results page shall display matches with context snippets, title, course name, and activity type. | High |
| **FR3.4** | The results page shall provide filters to narrow results by Course, Content Type (e.g., Assignment, PDF, Forum), and Date Range. | Medium |

#### 3.4 Feature 4: Enhanced Gradebook with Feedback & History
**3.4.1 Description**
The gradebook shall be enhanced to provide a robust interface for grading, delivering detailed feedback, and maintaining a viewable history of grade changes.

**3.4.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR4.1** | The grading interface shall allow professors to enter a grade, select from pre-defined comment quick-keys, and enter rich-text/multimedia feedback for each student submission. | High |
| **FR4.2** | The system shall maintain an immutable audit log of all grade entries and changes, including timestamp and user who made the change. | High |
| **FR4.3** | Professors shall be able to view the history/audit log for any student's grade from within the gradebook. | Medium |
| **FR4.4** | Students shall be able to view their grade and associated feedback on their "User report" view, with clear indication of when feedback was provided. | High |

#### 3.5 Feature 5: Configurable RSS Web Feeds
**3.5.1 Description**
Professors shall be able to configure and display RSS feeds from external sources (e.g., news sites, academic journals, blog) on their course homepage or within specific topic sections.

**3.5.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR5.1** | The system shall provide an "RSS Feed" activity module that can be added to any course section. | Medium |
| **FR5.2** | When adding the activity, the professor shall specify the RSS feed URL, number of items to display, and whether to show description/summary. | Medium |
| **FR5.3** | The system shall cache feed content to avoid excessive external requests and display it in a formatted block within the course. | Medium |
| **FR5.4** | Feed updates shall be refreshed according to a configurable system-wide cron schedule (e.g., every 60 minutes). | Low |

#### 3.6 Feature 6: Configurable Backup Scheduling
**3.6.1 Description**
System Administrators shall have a simplified, reliable interface to configure automated backup schedules for course data, with options for frequency and retention.

**3.6.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR6.1** | The system shall provide an administrative interface to set automated backup schedules (e.g., daily, weekly) for all courses or courses by category. | High |
| **FR6.2** | The administrator shall be able to configure retention policies (e.g., keep 4 weekly backups, 12 monthly backups). | Medium |
| **FR6.3** | The system shall generate logs for each backup operation, indicating success/failure and data size. | Medium |
| **FR6.4** | Backup files shall be stored in a designated, secure filesystem location accessible for potential off-site transfer (process TBD). | Medium |

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
*   **PR1:** The system shall support **1,000 concurrent users** with a page load time of under 3 seconds for core actions (browsing, submitting) during peak periods.
*   **PR2:** Search queries across all courses for a single user shall return results within **5 seconds**.
*   **PR3:** Audio recording shall initiate capture within **2 seconds** of user permission grant.

#### 4.2 Availability & Reliability
*   **AR1:** The overall system, including new features, shall achieve **99% uptime** excluding planned maintenance windows.
*   **AR2:** The system shall have a Mean Time Between Failures (MTBF) of no less than 720 hours for newly developed components.

#### 4.3 Security & Compliance
*   **SC1:** All enhancements shall adhere to Moodle's native role-based permission system. No feature shall bypass these controls.
*   **SC2:** User-generated audio files shall be stored with permissions ensuring they are accessible only to the intended user, their professors, and system administrators.
*   **SC3:** The system shall maintain FERPA compliance, ensuring grade and feedback data is protected and auditable.

#### 4.4 Usability
*   **US1:** New configuration options for professors shall be located within the standard Moodle activity setup forms, following existing UI patterns.
*   **US2:** The interface for students to upload multiple files or record audio shall be learnable within 1 minute of first use, as validated by user testing.
*   **US3:** All new text and interfaces shall meet WCAG 2.1 AA accessibility standards.

#### 4.5 Maintainability & Support
*   **MS1:** All custom code shall be developed as discrete Moodle plugins, documented with inline comments and a README file explaining configuration.
*   **MS2:** The system shall be designed to allow for updates to the core Moodle version with minimal rework required for the enhancement plugins.

### 5. Appendices

#### Appendix A: User Stories Mapping to Requirements
| User Story | Mapped Requirement IDs |
| :--- | :--- |
| 1. Professor - Multiple file uploads | FR1.1, FR1.2, FR1.4 |
| 2. Language Student - Audio portfolio | FR2.1, FR2.2, FR2.3, FR2.4 |
| 3. Student - Search across courses | FR3.1, FR3.2, FR3.3 |
| 4. Professor - RSS feeds for announcements | FR5.1, FR5.2, FR5.3 |
| 5. Professor - Grade with feedback | FR4.1, FR4.4 |
| 6. SysAdmin - Configurable backups | FR6.1, FR6.2, FR6.3 |

#### Appendix B: Success Metrics Verification
*   **Metric 1 (1000 concurrent users):** Verified via load testing scripts simulating peak activity mix.
*   **Metric 2 (99% Uptime):** Monitored via institutional network monitoring tools (e.g., Nagios) over a 6-month post-launch period.
*   **Metric 3 (Priority 1 & 2 Implementation):** Verified via Requirement Traceability Matrix and User Acceptance Testing (UAT) sign-off on all High-priority requirements.

#### Appendix C: Open/Undecided Issues
1.  The implementation approach for wiki/blog integration (a Priority 3 feature) is deferred. Options include using existing Moodle plugins or limited custom development.
2.  Final institutional commitment to Moodle adoption is pending the successful delivery and evaluation of this project.
3.  Exact backup frequency (e.g., daily vs. weekly) and off-site storage protocol require final policy approval from University administration.
4.  The design for a unified notification subscription manager (beyond RSS) is deferred to a potential future phase.
5.  The approach for developing comprehensive end-user documentation (guides, videos) will be determined post-development, based on available resources.

---
*Document End*