# Software Requirements Specification (SRS)
## Moodle Enhancement Project for University of Puget Sound

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Prepared for:** University of Puget Sound, Instructional Technology Department  
**Prepared by:** [Your Name/Team Name]  
**Status:** Draft for Review

---

### 1. Introduction

#### 1.1 Purpose
This document defines the requirements for enhancing the existing Moodle Learning Management System (LMS) at the University of Puget Sound. The purpose is to address specific instructional functionality gaps by developing new features that integrate seamlessly via Moodle's existing APIs, thereby improving the teaching and learning experience without requiring a platform migration.

#### 1.2 Scope
The scope of this project includes the design, development, testing, and deployment of three core functional enhancements to the Moodle instance:
1.  A configurable multiple file upload utility.
2.  An integrated audio recording and voice clip portfolio system.
3.  A comprehensive search function for course page content.

All development will be conducted as Moodle plugins (likely *activity modules*, *blocks*, or *local plugins*) utilizing official Moodle APIs. The core Moodle system, its database schema (for standard tables), and its user interface framework will not be fundamentally altered. Out of scope are enhancements to other areas of Moodle (e.g., gradebook, calendar, messaging) and any functionality requiring core Moodle code hacks.

#### 1.3 Definitions, Acronyms, and Abbreviations
*   **API:** Application Programming Interface
*   **LMS:** Learning Management System
*   **Moodle:** Modular Object-Oriented Dynamic Learning Environment
*   **UPS:** University of Puget Sound
*   **SRS:** Software Requirements Specification
*   **UI:** User Interface
*   **UX:** User Experience

#### 1.4 References
*   Moodle Plugin Development Documentation: https://docs.moodle.org/dev/
*   Moodle API References
*   University of Puget Sound IT Security Policy
*   Project Charter: Moodle Enhancement Project

#### 1.5 Overview
The remainder of this document is structured as follows: Section 2 provides a general description of the product and its constraints. Section 3 details the specific functional and non-functional requirements. Appendices may include mockups, data models, or other supplementary information.

---

### 2. Overall Description

#### 2.1 Product Perspective
This project is an enhancement suite for the existing Moodle LMS. It will be implemented as a set of integrated plugins that extend Moodle's capabilities. The plugins will interact with the Moodle core via its standard APIs, reside within the Moodle file structure, and adhere to its security and permission models.

#### 2.2 Product Functions
The enhanced system shall provide the following high-level functions:
1.  **Bulk File Management:** Allow instructors and students to upload multiple files simultaneously to configured assignment, resource, or forum pages.
2.  **Audio Engagement:** Provide tools for recording audio directly in the browser, managing a personal library of recordings, and submitting or sharing these clips within course activities.
3.  **Content Discovery:** Enable users to search for text content within the various elements (resources, labels, forum posts, etc.) of a specific course.

#### 2.3 User Characteristics
*   **Instructors:** Primary users who create and manage course content. They require intuitive configuration tools for enabling/disabling features like multi-upload on specific pages.
*   **Students:** Primary users who interact with course content. They need simple, efficient tools for submitting work (files, audio) and finding information.
*   **Administrators:** Technical staff who install, configure, and maintain the plugins. They require manageable backup integration and performance monitoring.

#### 2.4 Constraints
1.  **Technical:** All enhancements **must** be developed using the existing, official Moodle APIs. Core Moodle file modifications are prohibited.
2.  **Performance:** The system, with all new features active, **must** support a minimum of 1000 concurrent users without significant degradation in response time (< 2 seconds for standard operations).
3.  **Operational:** A system backup mechanism must be in place. The schedule for backing up data related to the new features (e.g., audio files, search indices) must be configurable by system administrators.
4.  **Compliance:** The solution must adhere to UPS IT security policies, FERPA, and WCAG 2.1 AA accessibility standards.

#### 2.5 Assumptions and Dependencies
*   **Assumption:** The existing UPS Moodle infrastructure has sufficient storage and processing capacity to handle the additional load from audio files and search indexing.
*   **Dependency:** Project success is dependent on the stability and documentation of the relevant Moodle APIs for file handling, media recording, and database querying.
*   **Dependency:** Adequate testing resources (staging environment, user testing groups) will be available.

---

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 Multiple File Upload (FR-MFU)
*   **FR-MFU-1:** The system shall provide an interface element (e.g., a button or drag-and-drop zone) that allows users to select and queue multiple files for upload from their local device.
*   **FR-MFU-2:** Instructors shall be able to enable or disable the multiple file upload functionality on a per-activity/resource basis (e.g., within the settings of an Assignment or a Folder resource).
*   **FR-MFU-3:** The system shall display upload progress, success, or error messages for each individual file in the queue.
*   **FR-MFU-4:** The system shall validate file types and sizes based on the existing Moodle course/activity file restrictions.

##### 3.1.2 Audio Recording & Portfolio (FR-ARP)
*   **FR-ARP-1:** The system shall provide a "Record Audio" button within relevant activity interfaces (e.g., Assignment submission, Forum reply) that activates the browser's microphone access (with user permission).
*   **FR-ARP-2:** The recording interface shall provide standard controls: Record, Pause, Stop, Playback, and Delete.
*   **FR-ARP-3:** Upon stopping a recording, the user shall be able to save the clip. Saved clips shall be stored in a user-specific "Audio Portfolio" area within Moodle.
*   **FR-ARP-4:** The Audio Portfolio shall provide a management interface for the user to view, play, label, delete, or select existing clips for submission to an activity.
*   **FR-ARP-5:** The system shall save audio files in a efficient, web-compatible format (e.g., MP3 or Opus).

##### 3.1.3 Course Page Search (FR-CPS)
*   **FR-CPS-1:** A search block shall be available to add to course dashboards. This block shall contain a text input field and a search button.
*   **FR-CPS-2:** The search function shall index and make searchable text content from: Page resources, Label text, Description fields of activities and resources, and Forum post bodies (within that specific course).
*   **FR-CPS-3:** Search results shall be displayed in a ranked list, showing the title of the containing resource/activity, a snippet of the matched text, and a direct link to the context.
*   **FR-CPS-4:** The search index shall update automatically when course content is created or modified.

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance Requirements (PR)
*   **PR-1:** Under normal load (≤1000 concurrent users), all plugin page loads shall complete in under 2 seconds.
*   **PR-2:** File upload operations shall maintain stability and provide progress feedback even with slow network connections.
*   **PR-3:** The search index for a standard course (≤500 content items) shall return results in under 1 second.

##### 3.2.2 Security Requirements (SR)
*   **SR-1:** All features shall enforce Moodle's standard role-based capabilities (e.g., only users with 'submit assignment' capability can upload to an assignment).
*   **SR-2:** Audio recording shall only be initiated after explicit user consent via the browser's media permissions API.
*   **SR-3:** All user-generated content (uploaded files, audio recordings) shall be stored within Moodle's secure file system with appropriate access controls.

##### 3.2.3 Operational Requirements (OR)
*   **OR-1:** The system shall integrate with the institutional backup system. An administrator shall be able to configure the backup schedule (e.g., daily, weekly) for the data tables and files associated with the new plugins.
*   **OR-2:** All plugins shall be compatible with the university's specified version of Moodle (e.g., 4.x) and the next major release.

##### 3.2.4 Usability & Accessibility Requirements (UR)
*   **UR-1:** The user interface for all new features shall be consistent with the standard Moodle theme and UX patterns.
*   **UR-2:** All functionality shall be accessible via keyboard navigation.
*   **UR-3:** All interactive elements shall have appropriate ARIA labels and roles. The audio recording interface shall provide visual status indicators alongside auditory cues.

---

### 4. Appendices

#### 4.1 Data Schema (Preliminary)
*   **`plugin_audio_portfolio`:** Stores metadata for user audio clips (id, userid, title, filename, timecreated).
*   **`plugin_course_search_index`:** Stores indexed course content (id, courseid, cmid, contenttype, contenttext, timemodified).

#### 4.2 Open Issues
*   Determination of maximum audio recording length per clip.
*   Specific backup configuration interface details with the IT operations team.

---
**Document Approval:**

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| Project Sponsor | | | |
| Lead Developer | | | |
| IT Director | | | |