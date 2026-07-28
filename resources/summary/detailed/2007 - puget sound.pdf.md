# Detailed Summary: Moodle Enhancements for Puget Sound

## Background and Scope
This document outlines the functional and non-functional requirements for enhancing the Moodle courseware system to meet the specific instructional and educational needs of the University of Puget Sound. The scope focuses on developing core functionalities currently missing from Moodle, including improved file management, audio recording, search, grading, and social features, while also redesigning the user interface for better usability. The project assumes Moodle will be adopted and that enhancements will utilize its existing APIs. Non-goals include a complete replacement of Moodle's core architecture or developing features that are already adequately provided by third-party services not requiring integration.

## Stakeholders Matrix and Use Cases
*   **Student**: Primary consumer who accesses course materials, submits assignments, and participates in discussions.
*   **Professor (Course Administrator)**: Primary content manager who uploads materials, creates collaborative spaces, and grades assignments.
*   **System Administrator**: Responsible for maintaining system configuration, performing updates, and ensuring overall system reliability.

**Main Scenarios:**
1.  A professor configures a course page to allow multiple file uploads for a project submission.
2.  A student records and submits a voice clip for a language assignment, which is archived to their portfolio.
3.  A professor enables RSS web feeds for course announcements to keep students notified.
4.  A student uses the course-level search to quickly find a specific assignment page.
5.  A professor grades a submitted assignment online and provides textual feedback.
6.  Students collaboratively edit a document using the integrated wiki.
7.  A student receives an SMS notification when a new grade is posted.
8.  A system administrator performs a scheduled nightly backup of all course data.

## Business Process
**Main Process: Assignment Submission and Grading**
1.  **Trigger:** Student navigates to an assignment page.
2.  Student uploads required file(s) (single or multiple as configured by professor).
3.  System stores the submission and records a timestamp.
4.  Professor is notified (via configured method) of the new submission.
5.  Professor accesses the submission, reviews it, and assigns a grade.
6.  Professor may optionally attach feedback (text or file).
7.  System updates the gradebook and records the grade change in history.
8.  **Output:** Student is notified and can view the grade and feedback.

**Key Branch A: Audio Clip Submission for Portfolio**
1.  Student records a voice clip using the system's interface.
2.  Student previews the clip and chooses to submit it.
3.  System stores the clip in a speech-optimized format and archives it to the student's portfolio.
4.  Student or professor can later access, download (as MP3), or delete clips from the portfolio.

**Key Branch B: Subscription to Page Notifications**
1.  Professor creates a new course page (e.g., announcement) and enables notifications.
2.  System presents notification options (email/SMS) to enrolled students.
3.  Student selects preferred notification channel in their profile.
4.  When the page is updated, the system sends alerts to subscribed students.

## Domain Model
*   **User**: `user_id` (unique), `role` (required: Student/Professor/Admin), `email`, `notification_preferences`
*   **Course**: `course_id` (unique), `name` (required), `administrator_id` (reference to User)
*   **Page**: `page_id` (unique), `course_id` (reference, required), `type` (e.g., Assignment, Wiki, Forum), `title` (required), `allows_multiple_files` (boolean), `notifications_enabled` (boolean), `feed_enabled` (boolean)
*   **File Submission**: `submission_id` (unique), `page_id` (reference, required), `user_id` (reference, required), `file_references`, `timestamp` (required)
*   **Audio Clip**: `clip_id` (unique), `user_id` (reference, required), `storage_format_data`, `timestamp` (required), `portfolio_tags`
*   **Gradebook Entry**: `entry_id` (unique), `page_id` (reference, required), `user_id` (reference, required), `score`, `possible_points`, `feedback_text`, `last_modified` (required)
*   **Grade History**: `history_id` (unique), `entry_id` (reference, required), `old_score`, `new_score`, `change_timestamp` (required)
*   **Notification Subscription**: `subscription_id` (unique), `user_id` (reference, required), `page_id` (reference, required), `method` (required: email/SMS)

## Interfaces and Integrations
*   **Moodle Core API**: Direction: Internal. Interaction: All new enhancements. Input/Output: Leverages existing Moodle APIs for data persistence and user management. SLA: Must maintain compatibility with the base Moodle version.
*   **Email Server (SMTP)**: Direction: Outbound. Interaction: Sending notifications. Input: Recipient address, subject, message body. Output: Email dispatch. SLA: Delivery attempts logged; retry on failure.
*   **SMS Gateway**: Direction: Outbound. Interaction: Sending notifications. Input: Recipient phone number, message text. Output: SMS dispatch. SLA: Use reliable provider; message delivery status monitored.
*   **Backup Storage System**: Direction: Outbound. Interaction: Scheduled data backups. Input: System and course data dumps. Output: Compressed backup files. SLA: Nightly backups; restore capability within 6 hours.

## Acceptance Criteria
**Capability: Multiple File Upload**
*   Given a professor has configured an assignment page to allow multiple files, when a student submits the assignment, then the student can attach and successfully upload more than one file.
*   Given a page is configured for single file upload only, when a student attempts to upload multiple files, then the system prevents the action and displays an appropriate message.

**Capability: Audio Portfolio**
*   Given a student has recorded a voice clip, when they choose to submit it, then the clip is stored in their personal portfolio and is accessible for future review.
*   Given a professor is viewing a student's portfolio, when they select a clip, then they can play the audio inline or download it as an MP3 file.

**Capability: Integrated Search**
*   Given a student is within a specific course, when they use the search box with a keyword, then results are displayed from within that course, ranked by relevance.
*   Given a user is on any page after login, then a search box is persistently visible in the page header or footer.

## Non-functional Metrics
*   **Performance**: Support at least 1,000 concurrent users. Common page loads should respond within 3 seconds under normal load.
*   **Reliability**: System availability target of 99% (excluding scheduled maintenance). Configurable nightly backups with a restore time objective of 6 hours.
*   **Security**: User authentication and authorization managed via Moodle core. Student grade data accessible only to that student and authorized course professors.
*   **Compliance**: Adhere to University data retention and privacy policies. Utilize standard, open formats (e.g., RSS 2.0, MP3) where applicable.
*   **Observability**: All system errors and critical user actions (e.g., grade changes, file deletions) must be logged for audit and troubleshooting.

## Milestones and Release Strategy
1.  Finalize and baseline requirements specification.
2.  Complete architectural design for integrations (Audio, Search, Notifications).
3.  Develop and test core Priority 1 & 2 features (Multiple File Upload, Audio Recording, Search, Gradebook).
4.  Internal alpha testing with a select group of professors and students.
5.  Beta release to a pilot department (e.g., Foreign Languages) for real-world feedback.
6.  Production release of Priority 1, 2, and selected Priority 3 features to the entire university.

## Risk List and Mitigation Strategies
1.  **Risk:** Moodle's core APIs are insufficient or too restrictive for required enhancements.
    *   **Mitigation:** Develop proof-of-concept for the highest-risk integration (e.g., audio portfolio) early. Explore forking or module development if APIs are inadequate.
2.  **Risk:** Performance degradation under load with 1,000+ concurrent users.
    *   **Mitigation:** Implement performance testing early in the development cycle. Optimize database queries and consider caching strategies for frequently accessed data.
3.  **Risk:** Low adoption by professors due to complex new interfaces.
    *   **Mitigation:** Involve professor stakeholders in UI/UX design reviews. Provide comprehensive training and clear documentation for new features.
4.  **Risk:** SMS notification costs become prohibitive.
    *   **Mitigation:** Implement user preferences to default to email. Monitor usage and set per-user or system-wide limits if necessary.
5.  **Risk:** Integrating third-party wiki/blog software creates security or maintenance vulnerabilities.
    *   **Mitigation:** Choose mature, actively maintained open-source projects. Isolate integrations behind Moodle's authentication and keep them updated.
6.  **Risk:** Data loss from audio portfolio or file submissions.
    *   **Mitigation:** Ensure audio and file data are included in the nightly backup routine. Implement integrity checks on stored media files.

## Undecided Issues and Responsible Parties
1.  The specific, mature open-source wiki and blog engines to be integrated. (Responsible: Development Team)
2.  The choice of SMS gateway provider and associated cost structure. (Responsible: System Administrators / Project Sponsor)
3.  The exact speech-optimized audio format for storage (e.g., Speex, Opus). (Responsible: Development Team)
4.  The default allocation size for each user's audio portfolio space. (Responsible: System Administrators / Stakeholder Committee)
5.  The schedule and ownership for ongoing maintenance of the custom enhancements. (Responsible: Office of Information Services Management)
6.  The detailed rollout and training plan for end-users post-development. (Responsible: Project Manager & Training Team)