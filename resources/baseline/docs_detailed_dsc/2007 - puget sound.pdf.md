# Software Requirements Specification (SRS)
## Moodle Enhancement Project
### University of Puget Sound

**Document Version:** 1.0  
**Date:** October 26, 2023  
**Status:** Draft for Review  
**Authors:** Project Requirements Team  
**Stakeholders:** University Administration, Faculty, Students, Office of Information Services

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for enhancing the Moodle Learning Management System (LMS) at the University of Puget Sound. The purpose is to provide a comprehensive description of the system's intended capabilities, interfaces, and performance characteristics to guide development, testing, and implementation.

### 1.2 Scope
The project scope encompasses the development of custom enhancements to the core Moodle platform to address specific instructional needs. Enhancements will be implemented as modules or plugins utilizing Moodle's existing APIs and architecture.

**In-Scope Features:**
- Enhanced file management with multiple file upload support
- Integrated audio recording and portfolio management
- Course-level search functionality
- Improved grading interface with feedback mechanisms
- Social features including wiki and blog integration
- Notification system with email and SMS capabilities
- User interface redesign for improved usability
- RSS feed generation for course content

**Out-of-Scope Items:**
- Replacement of Moodle's core architecture
- Development of features already provided by adequate third-party services not requiring integration
- Complete overhaul of existing Moodle authentication systems
- Mobile application development (responsive web interface only)

### 1.3 Definitions, Acronyms, and Abbreviations

| Term | Definition |
|------|------------|
| LMS | Learning Management System |
| API | Application Programming Interface |
| RSS | Really Simple Syndication |
| SMS | Short Message Service |
| SMTP | Simple Mail Transfer Protocol |
| SLA | Service Level Agreement |
| RTO | Recovery Time Objective |
| UI/UX | User Interface/User Experience |

### 1.4 References
- Moodle Developer Documentation (latest version)
- University of Puget Sound IT Policies
- FERPA Compliance Guidelines
- WCAG 2.1 Accessibility Standards

### 1.5 Overview
This document is organized into the following sections:
- **Section 2:** Overall Description - Provides context, user characteristics, and constraints
- **Section 3:** Specific Requirements - Details functional and non-functional requirements
- **Section 4:** Appendices - Contains supplementary information

## 2. Overall Description

### 2.1 Product Perspective
The enhanced Moodle system will operate as an extension of the existing Moodle LMS. It will integrate with university systems while maintaining compatibility with standard Moodle updates and plugins.

```
┌─────────────────────────────────────────────────────────┐
│                 External Systems                         │
├─────────────────────────────────────────────────────────┤
│  • Email Server (SMTP)                                  │
│  • SMS Gateway                                          │
│  • Backup Storage System                                │
│  • University Directory Services                        │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│              Enhanced Moodle System                      │
├─────────────────────────────────────────────────────────┤
│  • Moodle Core with Custom Modules                      │
│  • Audio Processing Engine                              │
│  • Search Indexing Service                              │
│  • Notification Service                                 │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│                 Core Moodle Platform                     │
└─────────────────────────────────────────────────────────┘
```

### 2.2 User Characteristics

| User Role | Characteristics | Technical Proficiency |
|-----------|----------------|----------------------|
| **Student** | Primary consumer of course materials. Needs intuitive interface for accessing content, submitting assignments, and receiving notifications. | Varies from basic to advanced computer skills. |
| **Professor (Course Administrator)** | Creates and manages course content, grades assignments, configures course settings. Requires efficient tools for content management and student evaluation. | Generally proficient with educational technology. May require training for new features. |
| **System Administrator** | Maintains system health, performs updates, manages backups, and configures system-wide settings. | Highly technical with expertise in Moodle administration and server management. |

### 2.3 Operating Environment
- **Server:** Linux-based web server (Apache/Nginx)
- **Database:** MySQL/PostgreSQL compatible with Moodle
- **PHP Version:** As required by Moodle core version
- **Browser Support:** Latest versions of Chrome, Firefox, Safari, Edge
- **Mobile:** Responsive design for tablet and mobile browsers

### 2.4 Design and Implementation Constraints
1. Must utilize Moodle's plugin architecture and APIs
2. Must maintain compatibility with existing Moodle themes
3. Must comply with university branding guidelines
4. Must adhere to FERPA and university data privacy policies
5. Must support accessibility standards (WCAG 2.1 AA)

### 2.5 Assumptions and Dependencies
**Assumptions:**
1. Moodle will be adopted as the university's primary LMS
2. University will provide necessary server infrastructure
3. Stakeholders will participate in user acceptance testing
4. Existing Moodle user data can be migrated to the enhanced system

**Dependencies:**
1. Availability of Moodle core APIs for required functionality
2. Integration with university authentication systems
3. Third-party SMS gateway service availability
4. Adequate storage for audio portfolio files

## 3. Specific Requirements

### 3.1 Functional Requirements

#### 3.1.1 User Management
**FR-01:** The system shall extend Moodle's existing user roles to include enhanced permission sets for new features.

**FR-02:** Users shall be able to configure notification preferences (email/SMS) in their profile settings.

#### 3.1.2 Course and Page Management
**FR-03:** Professors shall be able to configure assignment pages to allow single or multiple file uploads.

```javascript
// Example configuration interface
{
  "page_type": "assignment",
  "allows_multiple_files": true,
  "max_files": 10,
  "allowed_formats": [".pdf", ".docx", ".zip"]
}
```

**FR-04:** The system shall provide an option to enable RSS feeds for course announcement pages.

**FR-05:** Professors shall be able to enable/disable notifications for specific course pages.

#### 3.1.3 File Management
**FR-06:** Students shall be able to upload multiple files to assignments configured for multiple uploads.

**FR-07:** The system shall validate file types and sizes according to course configuration.

**FR-08:** When a page is configured for single file upload only, the system shall prevent multiple file uploads and display an appropriate error message.

#### 3.1.4 Audio Recording and Portfolio
**FR-09:** Students shall be able to record voice clips using a browser-based recording interface.

**FR-10:** The system shall store audio clips in a speech-optimized format (format TBD).

**FR-11:** Audio clips shall be automatically archived to the student's personal portfolio upon submission.

**FR-12:** Users shall be able to play audio clips inline or download them as MP3 files.

**FR-13:** Professors shall be able to access and review student audio portfolios for their courses.

**FR-14:** The system shall enforce storage quotas for audio portfolios (quota TBD).

#### 3.1.5 Search Functionality
**FR-15:** A persistent search box shall be available in the page header or footer after login.

**FR-16:** When searching within a course context, results shall be limited to content within that course.

**FR-17:** Search results shall be ranked by relevance to the query.

**FR-18:** The system shall index course pages, assignments, and uploaded materials for search.

#### 3.1.6 Grading and Feedback
**FR-19:** Professors shall be able to grade assignments online and provide textual feedback.

**FR-20:** The system shall automatically update the gradebook when grades are entered.

**FR-21:** All grade changes shall be recorded in a grade history log.

**FR-22:** Students shall be able to view their grades and feedback through a unified interface.

#### 3.1.7 Collaboration Features
**FR-23:** The system shall integrate a wiki engine for collaborative document editing.

**FR-24:** Multiple students shall be able to simultaneously edit wiki pages with change tracking.

**FR-25:** The system shall integrate a blog engine for course-related blogging.

#### 3.1.8 Notification System
**FR-26:** The system shall send email notifications for configured events (new grades, announcements, etc.).

**FR-27:** The system shall send SMS notifications based on user preferences.

**FR-28:** Students shall receive notifications when new grades are posted.

**FR-29:** Professors shall receive notifications when assignments are submitted.

**FR-30:** Notification delivery attempts shall be logged for monitoring.

#### 3.1.9 Backup and Recovery
**FR-31:** The system shall perform scheduled nightly backups of all course data.

**FR-32:** System administrators shall be able to initiate manual backups.

**FR-33:** Backup files shall be compressed and transferred to designated backup storage.

### 3.2 Non-Functional Requirements

#### 3.2.1 Performance
**NFR-01:** The system shall support at least 1,000 concurrent users.

**NFR-02:** Common page loads shall respond within 3 seconds under normal load conditions (p95).

**NFR-03:** File uploads shall complete within reasonable time based on file size and network conditions.

**NFR-04:** Search queries shall return results within 2 seconds for typical course content.

#### 3.2.2 Reliability
**NFR-05:** System availability target shall be 99% excluding scheduled maintenance windows.

**NFR-06:** The system shall have a Recovery Time Objective (RTO) of 6 hours for full restoration.

**NFR-07:** Data backups shall have a 30-day retention period minimum.

#### 3.2.3 Security
**NFR-08:** User authentication and authorization shall be managed through Moodle core.

**NFR-09:** Student grade data shall be accessible only to that student and authorized course professors.

**NFR-10:** All user data shall be encrypted in transit using TLS 1.2 or higher.

**NFR-11:** Audio portfolio files shall be accessible only to the student and authorized professors.

#### 3.2.4 Compliance
**NFR-12:** The system shall adhere to University of Puget Sound data retention policies.

**NFR-13:** The system shall comply with FERPA regulations for educational records.

**NFR-14:** Audio files shall be stored in standard, open formats where applicable.

**NFR-15:** RSS feeds shall comply with RSS 2.0 specification.

#### 3.2.5 Usability
**NFR-16:** The user interface shall comply with WCAG 2.1 AA accessibility standards.

**NFR-17:** New features shall maintain consistency with existing Moodle interface patterns.

**NFR-18:** Critical user actions shall have confirmation dialogs to prevent errors.

#### 3.2.6 Observability
**NFR-19:** All system errors shall be logged with appropriate severity levels.

**NFR-20:** Critical user actions (grade changes, file deletions, etc.) shall be logged for audit purposes.

**NFR-21:** System performance metrics shall be collectible for monitoring dashboards.

### 3.3 Interface Requirements

#### 3.3.1 User Interfaces
**UI-01:** The interface shall be responsive and adapt to different screen sizes.

**UI-02:** A consistent navigation structure shall be maintained across all enhanced features.

**UI-03:** The search box shall be persistently visible in the page header.

#### 3.3.2 Hardware Interfaces
**HI-01:** The system shall support standard computer microphones for audio recording.

**HI-02:** The system shall support common file formats for upload and download.

#### 3.3.3 Software Interfaces
**SI-01:** **Moodle Core API**
- **Direction:** Internal
- **Purpose:** Data persistence and user management
- **Requirements:** Must maintain compatibility with base Moodle version
- **Data Format:** Moodle's internal data structures

**SI-02:** **Email Server (SMTP)**
- **Direction:** Outbound
- **Purpose:** Sending notifications
- **Input:** Recipient address, subject, message body
- **Output:** Email dispatch
- **SLA:** Delivery attempts logged; retry on failure

**SI-03:** **SMS Gateway**
- **Direction:** Outbound
- **Purpose:** Sending notifications
- **Input:** Recipient phone number, message text
- **Output:** SMS dispatch
- **SLA:** Use reliable provider; message delivery status monitored

**SI-04:** **Backup Storage System**
- **Direction:** Outbound
- **Purpose:** Scheduled data backups
- **Input:** System and course data dumps
- **Output:** Compressed backup files
- **SLA:** Nightly backups; restore capability within 6 hours

#### 3.3.4 Communication Interfaces
**CI-01:** HTTP/HTTPS for web interface
**CI-02:** SMTP for email notifications
**CI-03:** REST API for SMS gateway integration
**CI-04:** RSS 2.0 for web feeds

### 3.4 Data Requirements

#### 3.4.1 Data Model
The system shall extend the following core entities:

```sql
-- Extended User entity
User {
  user_id: UUID (PK)
  role: ENUM('Student', 'Professor', 'Admin')
  email: VARCHAR(255)
  notification_preferences: JSON
  sms_number: VARCHAR(20) NULLABLE
  audio_quota_used: INTEGER
}

-- Extended Course entity  
Course {
  course_id: UUID (PK)
  name: VARCHAR(255) NOT NULL
  administrator_id: UUID (FK to User)
  settings: JSON
}

-- New/Enhanced Page entity
Page {
  page_id: UUID (PK)
  course_id: UUID (FK to Course) NOT NULL
  type: ENUM('Assignment', 'Wiki', 'Forum', 'Announcement')
  title: VARCHAR(255) NOT NULL
  allows_multiple_files: BOOLEAN DEFAULT FALSE
  notifications_enabled: BOOLEAN DEFAULT FALSE
  feed_enabled: BOOLEAN DEFAULT FALSE
  max_file_uploads: INTEGER DEFAULT 1
}

-- File Submission entity
File_Submission {
  submission_id: UUID (PK)
  page_id: UUID (FK to Page) NOT NULL
  user_id: UUID (FK to User) NOT NULL
  file_references: JSON -- Array of file metadata
  timestamp: DATETIME NOT NULL
  status: ENUM('Submitted', 'Graded', 'Returned')
}

-- Audio Clip entity
Audio_Clip {
  clip_id: UUID (PK)
  user_id: UUID (FK to User) NOT NULL
  course_id: UUID (FK to Course) NULLABLE
  storage_format_data: BLOB
  original_filename: VARCHAR(255)
  duration_seconds: INTEGER
  file_size_bytes: INTEGER
  timestamp: DATETIME NOT NULL
  portfolio_tags: JSON
  is_archived: BOOLEAN DEFAULT TRUE
}

-- Gradebook Entry entity
Gradebook_Entry {
  entry_id: UUID (PK)
  page_id: UUID (FK to Page) NOT NULL
  user_id: UUID (FK to User) NOT NULL
  score: DECIMAL(5,2) NULLABLE
  possible_points: DECIMAL(5,2) NOT NULL
  feedback_text: TEXT
  feedback_file_id: UUID NULLABLE
  last_modified: DATETIME NOT NULL
  modified_by: UUID (FK to User)
}

-- Grade History entity
Grade_History {
  history_id: UUID (PK)
  entry_id: UUID (FK to Gradebook_Entry) NOT NULL
  old_score: DECIMAL(5,2) NULLABLE
  new_score: DECIMAL(5,2) NULLABLE
  change_timestamp: DATETIME NOT NULL
  changed_by: UUID (FK to User) NOT NULL
  change_reason: VARCHAR(500) NULLABLE
}

-- Notification Subscription entity
Notification_Subscription {
  subscription_id: UUID (PK)
  user_id: UUID (FK to User) NOT NULL
  page_id: UUID (FK to Page) NOT NULL
  method: ENUM('email', 'sms') NOT NULL
  is_active: BOOLEAN DEFAULT TRUE
  created_date: DATETIME NOT NULL
}
```

#### 3.4.2 Data Retention
- User data: Retained while user is active + 7 years after last login
- Course data: Retained for 7 years after course end date
- Audio portfolio: Retained while student is enrolled + 1 year after graduation
- Grade history: Permanent retention for audit purposes
- System logs: 90 days for operational logs, 7 years for audit logs

### 3.5 Business Rules

**BR-01:** Only professors and system administrators can configure course page settings.

**BR-02:** Students can only submit files to assignments before the due date (if set).

**BR-03:** Grade visibility to students is controlled by professor settings.

**BR-04:** SMS notifications are only sent to verified phone numbers.

**BR-05:** Audio portfolio access is restricted to the student and professors of courses where the audio was submitted.

### 3.6 Acceptance Criteria

#### 3.6.1 Multiple File Upload
**AC-01:** Given a professor has configured an assignment page to allow multiple files, when a student submits the assignment, then the student can attach and successfully upload more than one file.

**AC-02:** Given a page is configured for single file upload only, when a student attempts to upload multiple files, then the system prevents the action and displays an appropriate message.

#### 3.6.2 Audio Portfolio
**AC-03:** Given a student has recorded a voice clip, when they choose to submit it, then the clip is stored in their personal portfolio and is accessible for future review.

**AC-04:** Given a professor is viewing a student's portfolio, when they select a clip, then they can play the audio inline or download it as an MP3 file.

#### 3.6.3 Integrated Search
**AC-05:** Given a student is within a specific course, when they use the search box with a keyword, then results are displayed from within that course, ranked by relevance.

**AC-06:** Given a user is on any page after login, then a search box is persistently visible in the page header or footer.

#### 3.6.4 Notification System
**AC-07:** Given a student has enabled SMS notifications in their profile, when a new grade is posted, then the student receives an SMS notification within 5 minutes.

**AC-08:** Given a professor has enabled notifications for a course page, when the page is updated, then subscribed students receive notifications via their preferred method.

## 4. Appendices

### 4.1 Use Case Specifications

#### Use Case 1: Configure Multiple File Upload
**Actor:** Professor  
**Preconditions:** Professor is logged in and has administrative rights to the course  
**Main Flow:**
1. Professor navigates to assignment page settings
2. Professor selects "Allow multiple file uploads" option
3. Professor sets maximum number of files allowed (optional)
4. Professor saves settings
5. System updates page configuration

**Alternate Flow:** Invalid configuration (e.g., negative number of files) results in error message

#### Use Case 2: Submit Audio Assignment
**Actor:** Student  
**Preconditions:** Student is enrolled in course, assignment accepts audio submissions  
**Main Flow:**
1. Student navigates to audio assignment page
2. Student clicks "Record" button
3. Student grants microphone permissions
4. Student records audio clip
5. Student previews recording
6. Student clicks "Submit"
7. System saves audio to portfolio and attaches to assignment
8. System confirms successful submission

**Alternate Flow:** Recording fails - system displays error and allows retry

### 4.2 Risk Management

| Risk ID | Description | Probability | Impact | Mitigation Strategy | Owner |
|---------|-------------|-------------|--------|-------------------|-------|
| R-01 | Moodle APIs insufficient for required enhancements | Medium | High | Develop proof-of-concept early; explore module development | Dev Team |
| R-02 | Performance degradation under load | Medium | High | Implement performance testing early; optimize queries; caching | Dev Team |
| R-03 | Low professor adoption due to complexity | High | Medium | Involve professors in design; provide training | Training Team |
| R-04 | SMS notification costs prohibitive | Low | Medium | Default to email; monitor usage; set limits | Sys Admin |
| R-05 | Third-party integration security vulnerabilities | Medium | High | Choose mature projects; isolate integrations; regular updates | Dev Team |
| R-06 | Data loss from audio/files | Low | High | Include in backups; implement integrity checks | Sys Admin |

### 4.3 Open Issues and Decisions Pending

1. **Specific wiki/blog engines for integration**  
   *Responsible:* Development Team  
   *Decision Needed By:* Phase 2 Start

2. **SMS gateway provider selection**  
   *Responsible:* System Administrators / Project Sponsor  
   *Decision Needed By:* Phase 3 Start

3. **Speech-optimized audio format (Speex vs. Opus vs. other)**  
   *Responsible:* Development Team  
   *Decision Needed By:* Audio Module Development Start

4. **Default audio portfolio storage allocation per user**  
   *Responsible:* System Administrators / Stakeholder Committee  
   *Decision Needed By:* Beta Release

5. **Ongoing maintenance schedule and ownership**  
   *Responsible:* Office of Information Services Management  
   *Decision Needed By:* Project Completion

6. **Detailed rollout and training plan**  
   *Responsible:* Project Manager & Training Team  
   *Decision Needed By:* 60 days before Production Release

### 4.4 Milestones and Release Strategy

| Phase | Milestone | Deliverables | Target Date |
|-------|-----------|--------------|-------------|
| 1 | Requirements Finalization | Baseline SRS Document | Month 1 |
| 2 | Architectural Design | Integration Design Documents | Month 2 |
| 3 | Core Development | Priority 1 & 2 Features (File Upload, Audio, Search, Gradebook) | Month 4 |
| 4 | Alpha Testing | Internal testing with select users | Month 5 |
| 5 | Beta Release | Pilot department deployment (Foreign Languages) | Month 6 |
| 6 | Production Release | Full university deployment | Month 8 |

**Priority Classification:**
- **Priority 1:** Multiple File Upload, Basic Audio Recording, Course Search
- **Priority 2:** Gradebook Enhancements, Email Notifications, RSS Feeds
- **Priority 3:** SMS Notifications, Wiki/Blog Integration, Advanced Portfolio Features

### 4.5 Glossary of Terms

**Audio Portfolio:** A personal storage space for students to archive and manage audio recordings across courses.

**Course Page:** Any content page within a Moodle course (assignment, resource, forum, etc.).

**Grade History:** An immutable record of all changes made to gradebook entries.

**Notification Subscription:** A user's opt-in preference to receive updates about specific course pages.

**Speech-Optimized Format:** An audio compression format specifically designed for voice recording at lower bitrates.

---

**Document Approval**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Sponsor | | | |
| Lead Developer | | | |
| System Architect | | | |
| Quality Assurance Lead | | | |

**Revision History**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2023-10-26 | Requirements Team | Initial Draft |
| | | | |