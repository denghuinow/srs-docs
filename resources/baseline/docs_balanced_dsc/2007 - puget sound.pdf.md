# Software Requirements Specification (SRS)
## Moodle Enhancement Project for University of Puget Sound

**Document Version:** 1.0
**Date:** October 26, 2023
**Status:** Draft for Review
**Project Sponsor:** University of Puget Sound IT Department

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for the enhancement of the Moodle Learning Management System (LMS) for the University of Puget Sound. It serves as a formal agreement between stakeholders and the development team, providing a comprehensive blueprint for the project's scope, features, and constraints.

#### 1.2 Scope
This project aims to enhance the core Moodle platform to address specific functional gaps identified in the university's previous system (Blackboard). The scope includes:
*   Implementation of new features: Audio Recording/Portfolio and Enhanced System-Wide Search.
*   Redesign of the user interface for improved data flow, usability, and consistency with university branding and pedagogical practices.
*   Integration of key external services (SMS, wiki/blog engines).
*   All enhancements are **contingent upon the university's formal adoption of Moodle** as its primary courseware system and will be developed utilizing Moodle's existing APIs and plugin architecture to ensure maintainability.

**Out of Scope:**
*   Development of a completely new LMS from scratch.
*   Major modifications to Moodle's core authentication or enrollment systems, which will leverage existing university infrastructure (e.g., LDAP/SSO).
*   Replacement of Moodle's underlying database architecture.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **LMS:** Learning Management System.
*   **API:** Application Programming Interface.
*   **UI/UX:** User Interface / User Experience.
*   **SMS:** Short Message Service.
*   **SRS:** Software Requirements Specification.
*   **Admin:** System Administrator role.
*   **Course Page:** Any resource or activity page within a Moodle course (e.g., Assignment, Page, Wiki).

#### 1.4 References
*   Moodle Official Documentation: https://docs.moodle.org/
*   University of Puget Sound IT Strategic Plan.
*   Stakeholder Interview Summaries (Internal Document).

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides an overall description of the product and its operating environment. Section 3 details specific functional requirements. Section 4 outlines non-functional requirements. Appendices contain supplementary information.

### 2. Overall Description

#### 2.1 Product Perspective
This project is a major enhancement package for the open-source Moodle LMS. It will be implemented as a set of custom Moodle plugins, themes, and configurations that integrate seamlessly with the chosen base version of Moodle. The system must interface with:
*   University Directory Services (for user authentication).
*   External SMS Gateway Service.
*   Third-party Wiki and Blog engines (to be selected).

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Needs |
| :--- | :--- | :--- |
| **Student** | Primary consumer. Varies in technical proficiency. Needs clear, consistent navigation and timely information. | Access materials, submit assignments, track grades, receive notifications, record audio for language practice. |
| **Professor (Instructor)** | Content administrator and facilitator. Limited time for system management. | Create/manage course content, configure assignments, grade student work, communicate with students. |
| **System Administrator** | Technical expert responsible for system health, security, and updates. | Configure global settings, manage users, perform backups, monitor performance, apply patches. |

#### 2.3 Operating Environment
*   **Software:** Base system will be a specified version of Moodle (e.g., 4.x) running on a LAMP/LEMP (Linux, Apache/Nginx, MySQL/MariaDB, PHP) stack.
*   **Hardware:** Hosted on university-managed virtualized servers meeting Moodle's recommended specifications for 1000+ concurrent users.
*   **Browsers:** Must be fully compatible with the latest stable versions of Chrome, Firefox, Safari, and Edge.

#### 2.4 Design and Implementation Constraints
1.  **Moodle API Compliance:** All custom developments must use official Moodle APIs and follow Moodle development guidelines.
2.  **Database Integrity:** Core Moodle database schema shall not be altered directly. Custom data must use plugin-specific tables.
3.  **Accessibility:** The interface must meet WCAG 2.1 AA standards.
4.  **Responsive Design:** The enhanced UI must be fully responsive and functional on desktop, tablet, and mobile devices.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** The University will formally commit to adopting Moodle prior to the start of development.
*   **Dependency:** Availability of a stable, supported version of Moodle to serve as the development base.
*   **Dependency:** Successful procurement and API access to a reliable SMS gateway service.
*   **Assumption:** Sufficient server storage will be allocated for student audio portfolios.

### 3. System Features and Requirements

#### 3.1 Feature 1: Enhanced Assignment Submission & Configuration
**3.1.1 Description**
Professors must be able to configure individual assignment pages to accept multiple file uploads from students in a single submission action.

**3.1.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR1.1** | In the assignment creation/editing interface, the professor shall be presented with a checkbox option labeled "Allow multiple file submissions." | High |
| **FR1.2** | When the "Allow multiple file submissions" option is enabled, the student submission interface shall provide a mechanism to upload more than one file (e.g., a "Add another file" button or native multi-select). | High |
| **FR1.3** | The system shall display all uploaded filenames and sizes to the student before final submission. | Medium |
| **FR1.4** | The system shall enforce the global and assignment-specific maximum file size limits on each uploaded file. | High |

#### 3.2 Feature 2: Audio Recording and Portfolio Management
**3.2.1 Description**
Students, particularly in foreign language courses, must be able to record, save, and organize audio clips into a personal, persistent portfolio to track oral proficiency over time.

**3.2.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR2.1** | The system shall provide a "Record Audio" button or component within relevant assignment pages or a dedicated portfolio page. | High |
| **FR2.2** | Upon initiating a recording, the system shall use the browser's Media API to capture audio via the user's microphone, with visual feedback (e.g., waveform, timer). | High |
| **FR2.3** | The system shall encode captured audio in a speech-optimized, open format (e.g., Opus in a WebM container) to balance quality and file size. | High |
| **FR2.4** | The student shall be able to play back, re-record, label, and save the audio clip to their personal portfolio. | High |
| **FR2.5** | Each **Audio Portfolio Entry** shall be tagged with metadata: Owner (Student ID), Recording Date, Associated Course, and optional Assignment reference. | High |
| **FR2.6** | The student shall have a dedicated "My Audio Portfolio" view to browse, play, and manage all their saved clips, filterable by course and date. | High |
| **FR2.7** | The system administrator shall be able to set and enforce global storage quotas for student audio portfolios. | Medium |

#### 3.3 Feature 3: System-Wide Unified Search
**3.3.1 Description**
A persistent search bar, accessible from any page, shall allow users to find course pages, materials, and announcements across all their enrolled courses.

**3.3.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR3.1** | A search input field shall be present in the global page header (navigation bar). | High |
| **FR3.2** | Upon submitting a query, the system shall search across: Course titles, Page/Resource titles and content, Assignment descriptions, and Announcements. | High |
| **FR3.3** | Search results shall be returned and categorized (e.g., "Courses", "Assignments", "Pages") and ranked by relevance. | High |
| **FR3.4** | Search results shall be security-trimmed, showing only content from courses the user is enrolled in or has access to. | High |
| **FR3.5** | Each result shall include a direct link to the content and its parent course name. | Medium |

#### 3.4 Feature 4: Online Grading with Feedback History
**3.4.1 Description**
Professors shall be able to review student submissions, assign grades, provide textual feedback, and have a change history maintained for each gradebook entry.

**3.4.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR4.1** | From the assignment grading interface, the professor shall be able to enter a numerical score and/or select a grade from a predefined scale. | High |
| **FR4.2** | The professor shall be able to enter rich-text feedback in a dedicated feedback field for each student submission. | High |
| **FR4.3** | Upon saving the grade and feedback, the system shall create a **Gradebook Entry** and notify the student according to their notification preferences. | High |
| **FR4.4** | The system shall maintain an audit log (change history) for each gradebook entry, storing the previous value, new value, timestamp, and the grader's identity. | Medium |
| **FR4.5** | Professors shall be able to view this history from the grading interface. | Medium |

#### 3.5 Feature 5: Configurable Notification System
**3.5.1 Description**
Users shall be able to subscribe to and receive notifications via their preferred channel (Email or SMS) for events like new announcements or grade postings.

**3.5.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR5.1** | Each **User** shall have a profile section to set **Notification Preferences**, including preferred channel (Email, SMS, or both) for different event types. | High |
| **FR5.2** | When a professor posts a new announcement or a grade, the system shall trigger the notification process for affected students. | High |
| **FR5.3** | For users selecting SMS, the system shall format the message and route it via the integrated SMS gateway service. | High |
| **FR5.4** | The system shall implement a fallback mechanism: if an SMS fails to send, the notification shall be sent via email automatically. | Medium |
| **FR5.5** | Users shall be able to unsubscribe from notifications at the course level. | Low |

#### 3.6 Feature 6: Centralized Administrative Interface
**3.6.1 Description**
System administrators require a simplified, consolidated interface for managing global system settings, themes, and configurations.

**3.6.2 Functional Requirements**
| ID | Requirement | Priority |
| :--- | :--- | :--- |
| **FR6.1** | The admin interface shall present a dashboard with categorized, clearly labeled settings (e.g., "Themes & Layout", "Notification Services", "Storage Quotas", "Backup Configuration"). | High |
| **FR6.2** | The interface shall use a consistent, non-cluttered layout with clear save/cancel actions for each setting group. | High |
| **FR6.3** | The interface shall provide a direct link to the comprehensive, searchable online administrator documentation. | Medium |

### 4. Non-Functional Requirements

#### 4.1 Usability
*   **4.1.1** The administrative interface shall be designed for efficiency, allowing a trained system administrator to locate and change any major setting within three clicks from the dashboard.
*   **4.1.2** The overall UI shall adhere to a redesigned, consistent theme that reduces visual clutter by 20% compared to the default Moodle interface, as measured by stakeholder survey.

#### 4.2 Reliability & Availability
*   **4.2.1** The system shall have an operational availability of 99% during core academic hours (7:00 AM - 11:00 PM PST, Monday-Friday during active terms).
*   **4.2.2** Scheduled maintenance windows shall be configurable and communicated to users at least 48 hours in advance via system-wide announcement.

#### 4.3 Performance
*   **4.3.1** The system shall support a minimum of **1000 concurrent authenticated users** with average page load times under 2 seconds for 95% of requests.
*   **4.3.2** The unified search shall return results for common queries within 3 seconds.

#### 4.4 Supportability & Maintainability
*   **4.4.1** All custom code shall be documented inline following Moodle development standards.
*   **4.4.2** The system shall be designed to allow for updates to the core Moodle version with minimal rework to custom plugins (target: < 40 person-hours of effort for a minor version upgrade).

#### 4.5 Data Integrity & Security
*   **4.5.1** A full system backup (database and user-generated files, including audio portfolios) shall be executed automatically on a nightly basis.
*   **4.5.2** The system must support point-in-time restoration of any course or system data within a **6-hour Recovery Time Objective (RTO)** following a failure.
*   **4.5.3** All user data, especially audio recordings, shall be encrypted at rest.

#### 4.6 Documentation
*   **4.6.1** A context-sensitive, searchable online help system shall be available to end-users (students and professors).
*   **4.6.2** A separate, detailed technical administrator manual shall be provided, covering installation, configuration, backup/restore procedures, and troubleshooting.

### 5. Appendices

#### Appendix A: Data Dictionary (Key Entities)
*   **User:** `{user_id, role, first_name, last_name, email, phone, notification_prefs_json}`
*   **Course:** `{course_id, course_code, full_name, idnumber, start_date, end_date, settings_json}`
*   **Page/Resource:** `{cmid, course_id, name, module_type, config_json (e.g., allow_multiple_uploads: boolean)}`
*   **Assignment Submission:** `{submission_id, assignment_id, user_id, time_created, status, file_set}`
*   **Gradebook Entry:** `{entry_id, item_id, user_id, grader_id, score, feedback, time_modified, history_log}`
*   **Audio Portfolio Entry:** `{clip_id, user_id, course_id, assignment_id (optional), filename, filepath, title, date_recorded, format}`

#### Appendix B: Open Issues and Decisions Pending
1.  **Base Version:** The specific version of Moodle (e.g., 4.2, 4.3) to be used as the development base.
2.  **Audio Storage Quota:** The precise storage limit per student (e.g., 500MB) and policy for archiving/cleaning old clips.
3.  **Third-Party Engine Selection:** The specific wiki (e.g., MediaWiki) and blog (e.g., WordPress) engines for integration.
4.  **Backup Configuration:** Detailed schedule options (e.g., full weekly + incremental daily) and retention policy (e.g., 90 days).
5.  **External Search Integration:** Decision on whether to supplement internal search with an external engine (e.g., Google Search Appliance) and its scope.
6.  **Feature Prioritization:** Final sign-off on the inclusion of any lower-priority ("Priority 3") features not detailed in this SRS.

---
*This document is subject to change upon formal project initiation and resolution of pending issues.*