# Software Requirements Specification (SRS)
## Moodle Enhancement System for University of Puget Sound

**Document Version:** 1.0
**Date:** 2023-10-27
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements for the enhancement of the Moodle Learning Management System (LMS) at the University of Puget Sound. The purpose of this project is to develop a set of integrated features that will allow Moodle to replace the existing Blackboard platform, better serving the specific instructional and administrative needs of the university. This document is intended for use by the project stakeholders, development team, quality assurance team, and system administrators.

#### 1.2 Scope
The scope of this project is limited to the development of new features and modifications within the existing Moodle platform. All enhancements will be built as plugins or modules utilizing the standard Moodle Application Programming Interfaces (APIs) and architecture. The core Moodle system, including its fundamental user management, course creation, and basic assignment functionalities, is considered a pre-existing condition and will not be re-engineered.

**In-Scope:**
*   Development of a configurable multi-file upload component.
*   Creation of an audio recording portfolio system for students.
*   Implementation of a course-wide search utility.
*   Enhancement of the grading interface with grade history tracking.
*   Development of a notification system for email and SMS alerts.
*   Ensuring the system meets specified performance, backup, and concurrency constraints.

**Out-of-Scope:**
*   Replacement or major modification of core Moodle authentication or database structures.
*   Development of mobile-native applications (functionality must be accessible via Moodle's responsive web interface).
*   Major visual redesign of the core Moodle theme.
*   Data migration scripts from Blackboard to Moodle (this is a separate project).

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **API:** Application Programming Interface.
*   **LMS:** Learning Management System.
*   **SMS:** Short Message Service.
*   **UI:** User Interface.
*   **UX:** User Experience.
*   **Course Administrator:** Synonymous with "Professor," "Instructor," or "Teacher" in this context, referring to a user with editing rights in a Moodle course.
*   **Portfolio:** A curated collection of a student's audio recordings within the system.

#### 1.4 References
*   Moodle Plugin Development Guide: https://docs.moodle.org/dev/
*   Moodle API Documentation: https://docs.moodle.org/dev/APIs
*   University of Puget Sound IT Infrastructure Policies.

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product, its user classes, and operating environment. Section 3 details the specific functional requirements. Section 4 outlines all non-functional requirements, including performance, security, and design constraints.

---

### 2. Overall Description

#### 2.1 Product Perspective
This project is an enhancement module for the existing Moodle LMS. It will integrate seamlessly as a set of plugins, appearing as native functionality to the end-users. The system must interact with:
*   **Moodle Core:** For user authentication, course data, and basic framework.
*   **University Directory Services:** (Via Moodle) for user role information.
*   **Email Server:** For sending notification emails.
*   **SMS Gateway:** A third-party service for sending SMS notifications.
*   **University Backup Infrastructure:** For scheduled system backups.

#### 2.2 User Classes and Characteristics
| User Class | Characteristics | Key Responsibilities |
| :--- | :--- | :--- |
| **Student** | ~2000 potential users. Primary consumer of content. Varies in technical proficiency. | Upload files and audio recordings. Search for course content. View grades and feedback. Receive notifications. |
| **Professor (Course Administrator)** | ~150 potential users. Creates and manages course content. Expert in their field, varying in technical skill. | Configure file upload options for activities. Grade student assignments. View and manage grade history. Access all student audio portfolios in their courses. Trigger page updates. |
| **System Administrator** | ~5 users. High technical proficiency. Manages university IT systems. | Install and configure plugins. Manage system backups and restores. Monitor performance and logs. Configure global notification settings (SMS gateway, etc.). |

#### 2.3 Operating Environment
*   **Software:** The enhancements must be compatible with the university's deployed version of Moodle (e.g., Moodle 4.x+). Plugins must be developed using PHP and follow Moodle development standards.
*   **Hardware:** Must operate within the university's existing Moodle server infrastructure.
*   **Networks:** Must function over the university's campus network and be accessible via the public internet for off-campus users.

#### 2.4 Design and Implementation Constraints
1.  **API Constraint:** All new functionality **must** be implemented using the existing Moodle APIs and plugin architecture. Direct modifications to the Moodle core code are prohibited.
2.  **Concurrency Constraint:** The system, in conjunction with the core Moodle platform, must support **at least 1000 concurrent users**.
3.  **Backup Constraint:** The enhanced system must be compatible with the university's backup system, allowing for configurable schedule backups. A full system restore, including all new plugin data, must be possible **within a six-hour recovery time objective (RTO)**.

#### 2.5 Assumptions and Dependencies
*   It is assumed that the core Moodle installation is stable, patched, and supported.
*   The project depends on the availability of a reliable SMS gateway service with a compatible API.
*   Successful deployment depends on coordination with the University's System Administration team for backup integration and performance monitoring.

---

### 3. System Features and Requirements

#### 3.1 Configurable Multiple File Uploads (FR-01)
**Description:** Professors shall be able to configure specific activities or resources within a course to accept multiple file uploads from students in a single operation.

**Requirements:**
*   **FR-01.1:** In the editing interface for an Assignment activity, the professor shall be able to enable a "Multiple File Upload" option.
*   **FR-01.2:** When enabled, the professor shall be able to set a maximum number of files allowed per submission (e.g., 1-20, or unlimited).
*   **FR-01.3:** When enabled, the professor shall be able to set a list of permitted file extensions or types (e.g., .pdf, .docx, .jpg).
*   **FR-01.4:** From the student submission page, the student shall be presented with a drag-and-drop interface or a "Add more files" button to select multiple files.
*   **FR-01.5:** The system shall display a list of selected files with names and sizes before final submission.

#### 3.2 Student Audio Recording Portfolio (FR-02)
**Description:** Students shall be able to create, manage, and submit audio recordings. Recordings will be organized into a personal portfolio accessible across courses.

**Requirements:**
*   **FR-02.1:** From a relevant activity (e.g., a "Voice Assignment"), the student shall be able to click a "Record" button to capture audio directly via the browser microphone.
*   **FR-02.2:** The student shall be able to play back, re-record, or save the audio clip.
*   **FR-02.3:** Saved recordings shall be automatically stored in the student's personal "Audio Portfolio."
*   **FR-02.4:** The student shall have a dedicated "My Audio Portfolio" page to view, label, organize, and delete their past recordings.
*   **FR-02.5:** When submitting an assignment that accepts audio, the student shall have the option to either record new audio or select an existing recording from their portfolio.
*   **FR-02.6:** Professors shall be able to view and listen to any audio submission from the grading interface.

#### 3.3 Course-Wide Search Functionality (FR-03)
**Description:** A search box shall be available on all course pages, allowing users to find content within the current course.

**Requirements:**
*   **FR-03.1:** A persistent search bar shall be present in the main course navigation header.
*   **FR-03.2:** The search shall index: Activity/Resource titles and descriptions, File contents (where text is extractable, e.g., PDF, Word), Forum post titles and bodies, and Assignment instructions.
*   **FR-03.3:** Search results shall be displayed on a dedicated page, ranked by relevance, and clearly indicating the source activity/resource.
*   **FR-03.4:** The search feature shall respect Moodle's role-based permissions (e.g., a student cannot search and find hidden or future content).

#### 3.4 Grading Interface with Grade History (FR-04)
**Description:** Enhance the grading interface for professors to include a persistent view of grade history for each student and assignment.

**Requirements:**
*   **FR-04.1:** From the standard Moodle grading panel, the professor shall have an additional "Grade History" tab or section.
*   **FR-04.2:** This history shall display a log of all grade changes for the selected student and assignment, including: Date/Time of change, Grade value (from/to), User who made the change, and Optional reason/feedback associated with the change.
*   **FR-04.3:** The system shall automatically log all manual grade overrides and feedback updates.

#### 3.5 Email and SMS Notifications (FR-05)
**Description:** Users shall receive automated notifications via Email and/or SMS when specific events occur within a course they are enrolled in.

**Requirements:**
*   **FR-05.1:** The system shall generate notifications for the following events: When a professor updates a core course page or resource, when a new assignment is posted, and when a grade is released or updated.
*   **FR-05.2:** Users shall be able to configure their notification preferences per course, choosing between: Email, SMS, Both, or None.
*   **FR-05.3:** System Administrators shall be able to configure global SMS gateway settings (provider, API keys, sender ID).
*   **FR-05.4:** SMS messages shall be concise and contain a direct link to the relevant content in Moodle.

---

### 4. Non-Functional Requirements

#### 4.1 Performance Requirements
*   **PR-01:** The system shall support a minimum of **1000 concurrent users** without significant degradation in response time (< 2 seconds for page loads).
*   **PR-02:** The course-wide search (FR-03) shall return results for a typical course within **3 seconds** of initiating the query.
*   **PR-03:** Audio recording (FR-02) shall have a latency of less than **200ms** from record button press to capture initiation.

#### 4.2 Safety and Security Requirements
*   **SR-01:** All file uploads (FR-01) shall be scanned for malware using the university's standard antivirus tools.
*   **SR-02:** Audio files (FR-02) shall be stored in a manner accessible only to the student who created them, the professors of the courses they are enrolled in, and system administrators.
*   **SR-03:** Grade history (FR-04) shall be immutable and only accessible by professors and system administrators. Students shall not be able to view the change log.
*   **SR-04:** All communication with the SMS gateway (FR-05) shall be encrypted (HTTPS).

#### 4.3 Software Quality Attributes
*   **Maintainability:** All code shall be documented according to Moodle development standards to allow for future maintenance by university staff.
*   **Usability:** The new features shall maintain visual and interaction consistency with the existing Moodle interface. Tooltips and help text shall be provided for new configuration options.
*   **Reliability:** The system shall have an uptime of 99.5% during core academic hours (7:00 AM - 10:00 PM, Mon-Sun).

#### 4.4 Backup and Recovery Requirements
*   **BR-01:** All data generated by the new features (uploaded files, audio recordings, grade history logs, notification logs) **must** be included in the system's scheduled backups.
*   **BR-02:** The backup schedule shall be configurable by the System Administrator (e.g., daily incremental, weekly full).
*   **BR-03:** In the event of a failure, a complete system restore, including all data from the new features, must be executable **within a six-hour window** (Recovery Time Objective - RTO).

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| System Admin Representative | | | |